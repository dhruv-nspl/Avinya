from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    dispatch_doc_no = fields.Char(string="Dispatch Doc No")
    term_of_delivery = fields.Text(string="Term Of Delivery")
    term_of_delivery = fields.Text(string="Term Of Delivery")
    dispatch_through = fields.Selection([
        ('sea',  'Sea'),
        ('air',  'Air'),
        ('road', 'Road'),
        ('rail', 'Rail'),
    ], string="Dispatch Through")
    
    # sea
    port_of_loading   = fields.Char(string="Port of Loading")
    port_of_discharge = fields.Char(string="Port of Discharge")
    bl_number  = fields.Char(string="Bill of Lading")
    vessel_name  = fields.Char(string="Vessel Name")
    container_no = fields.Char(string="Container No")
    container_type    = fields.Selection([
        ('20ft',   '20 FT'),
        ('40ft',   '40 FT'),
        ('reefer', 'Reefer'),
    ], string="Container Type")

    # air
    flight_no = fields.Char(string="Flight No")
    airline = fields.Char(string="Airline")
    awb_number = fields.Char(string="Air Waybill (AWB)")
    airport_from = fields.Char(string="Airport From")
    airport_to = fields.Char(string="Airport To")
    cargo_type = fields.Char(string="Cargo Type")
    
    # road
    vehicle_no   = fields.Char(string="Vehicle No")
    driver_name  = fields.Char(string="Driver Name")
    driver_phone = fields.Char(string="Driver Phone")
    lr_number    = fields.Char(string="Lorry Receipt (LR)")
    location_from = fields.Char(string="From")
    location_to    = fields.Char(string="To")

    # train
    train_no = fields.Char(string="Train No")
    wagon_no = fields.Char(string="Wagon No")
    railway_receipt = fields.Char(string="Railway Receipt")
    station_from = fields.Char(string="Station From")
    station_to = fields.Char(string="Station To")
    