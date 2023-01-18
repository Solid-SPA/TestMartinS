from odoo import api, models, fields, _

class CarService(models.Model):
    _name = 'car.service'
    _description = 'Car Service'

    name = fields.Char("Name")