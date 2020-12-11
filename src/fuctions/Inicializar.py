import os


class Inicializar():
    #DIRECTORIO BASE
    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    #JSON Data
    Json = basedir + u'\jsons'

    Environment = 'PROD'

    #BROWSER DE PRUEBAS
    NAVEGADOR = u'Chrome'

    '''if Environment == 'Test':
        URL = 'https://test-portal.clarodrive.com/'''

    if Environment == 'PROD':
        URL = 'https://www.saucedemo.com/'
