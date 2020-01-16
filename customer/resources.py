from datetime import date
from sqlalchemy_pagination import paginate

from . models import Customer
from webargs import fields, ValidationError
from webargs.falconparser import FalconParser
import falcon


class Parser(FalconParser):
    DEFAULT_VALIDATION_STATUS = 400


parser = Parser()
use_args = parser.use_args


def validate_age(dob):
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age > 18:
        return True
    raise ValidationError('Customer age must be greater than 18.')


create_customer_args = {
    'name': fields.String(location='json', required=True),
    'dob': fields.Date(location='json', required=True, validate=validate_age),
}

update_customer_args = {
    'name': fields.String(location='json', required=True),
    'dob': fields.Date(location='json', required=True),
}

pagination_args = {
    'page_num': fields.Int(missing=1),
    'limit': fields.Int(missing=25)
}


class CustomerItemResource:
    def on_get(self, req, resp, customer_id):
        cus = req.context.db_session.query(Customer).get(customer_id)
        if not cus:
            raise falcon.HTTPNotFound()
        results = {
            'customer': cus.as_dict,
        }
        resp.status = falcon.HTTP_200
        resp.media = results

    @use_args(update_customer_args)
    def on_put(self, req, resp, args, customer_id):
        cus = req.context.db_session.query(Customer).get(customer_id)
        if not cus:
            raise falcon.HTTPNotFound()
        cus.name = args['name']
        cus.dob = args['dob']
        req.context.db_session.commit()
        results = {
            'customer': cus.as_dict,
        }
        resp.status = falcon.HTTP_200
        resp.media = results

    def on_delete(self, req, resp, customer_id):
        cus = req.context.db_session.query(Customer).get(customer_id)
        if not cus:
            raise falcon.HTTPNotFound()
        req.context.db_session.delete(cus)
        req.context.db_session.commit()
        resp.status = falcon.HTTP_200
        resp.media = {}


class CustomerCollectionResource:
    @use_args(pagination_args)
    def on_get(self, req, resp, args):
        page_num = args['page_num']
        limit = args['limit']
        cus_list = req.context.db_session.query(Customer)
        page = paginate(cus_list, page_num, limit)
        results = {
            'customers': [cus.as_dict for cus in page.items],
            'total': page.total,
            'pages': page.pages,
            'next_page': page.next_page,
            'previous_page': page.previous_page,
        }
        resp.status = falcon.HTTP_200
        resp.media = results

    @use_args(create_customer_args)
    def on_post(self, req, resp, args):
        new_cus = Customer(
            name=args['name'],
            dob=args['dob']
        )
        req.context.db_session.add(new_cus)
        req.context.db_session.commit()
        resp.status = falcon.HTTP_201
        resp.media = {
            'id': new_cus.id
        }
