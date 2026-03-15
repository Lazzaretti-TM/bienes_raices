from odoo import fields, models 

class Estateproperty(models.Model):
    _name = "estate.property"
    _description = "Property"
    
    name = fields.Char(required=True)
    description = fields.Text()
    postcode= fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float(required=True)
    selling_price= fields.Float()
    bedrooms = fields.Integer()
    living = fields.Integer()
    facades= fields.Integer()
    garage= fields.Boolean()
    garden= fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
      ("north", "North"),
      ("south", "South"),
       ("east", "East"),
      ("west", "West"),   
        
        
    ])
     
    
    
    

