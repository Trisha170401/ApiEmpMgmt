from marshmallow import Schema, fields

class LoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)
    access_type = fields.Int(required=True)

class EmployeeSchema(Schema):
    emp_name = fields.Str(required=True)
    username = fields.Str(required=True)
    emp_id = fields.Int(required=True)
    age = fields.Int(required=True)
    role = fields.Str(required=True)
    dept = fields.Str(required=True)
    salary = fields.Int(required=True)

class VaccineSchema(Schema):
    username = fields.Str(required=True)
    vacine_type = fields.Str(required=True)
    latest_date = fields.Str(required=True)
    doses = fields.Int(required=True)
    boaster = fields.Bool(required=True)
