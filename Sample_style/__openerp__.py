{
    'name': 'Sample Style',
    'category': 'web',
    'description': """
Sample style backend theme with hide/show menu option.
========================

""",
    'author': 'Marwen CHAARI',
    'website': 'https://www.genext-it.com',
    'version': '1.0',
    'icon': "/Sample_style/static/img/icon.png",
    'depends': ['base'],
    'license': 'AGPL-3',
    'summary': 'Theme,odoo,sample,style',
    'data' : [
          'sample.xml',
          'img.xml',
#         'views/webclient_templates.xml'
    ],
    'qweb' : [
#         'static/src/xml/*.xml',
    ],
    
    'installable': True,
    'auto_install': False,
    'application': True,
}
