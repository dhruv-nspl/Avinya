{
    "name": "NSPL Custom Reports",
    "version": "19.0.1.0",
    "author": "Namah Softech Private Limited",
    "company": "Namah Softech Private Limited",
    "website": "https://namahsoftech.com",
    "category": "Sales",
    "depends": ['base', 'sale_management', 'purchase','account'],
    "data": [
        "reports/custom_header.xml",
        "reports/purchase_order_template.xml",
        "reports/commercial_invoice_template.xml",
        "reports/tax_invoice_template.xml",
        "reports/quatation_template.xml",
        "views/account_move_views.xml",
        "views/company_signature_view.xml",
        "views/res_bank_views.xml",
        
    ],
    "installable": True,
    "application": False,
}
