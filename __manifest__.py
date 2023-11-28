{
    'name': 'Imtech Theme',
    'version': '1.0',
    'category': 'Theme/Creative',
    'summary': 'A custom theme for Odoo/Imtech',
    'description': """
        Custom theme using imtech colors(red white and black).
    """,
    'depends': ['base', 'web'],
    'data': [
        #'views/assets.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'imtech_theme_creator/static/src/css/main.css',
            'imtech_theme_creator/static/src/scss/theme_style.scss',
        ],
    },
}
