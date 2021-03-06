import transaction
from pyramid.compat import text_
from pyramid.config import Configurator
from pyramid.asset import abspath_from_asset_spec

import ptah
import ptah_crowd

# Your custom application permissions
from ptah_minicms.permissions import Manager

# We will add Page during bootstrap of empty AppRoot
from ptah_minicms.page import Page

# application root
from ptah_minicms.root import APP_FACTORY

POPULATE_MINICMS_CONTENT = 'ptah-minicms-content'

@ptah.populate(POPULATE_MINICMS_CONTENT,
               title='Create minicms content',
               requires=(ptah_crowd.POPULATE_CREATE_ADMIN,))
def bootstrap_data(registry):
    """ create sample content """

    crowd_cfg = ptah.get_settings(ptah_crowd.CFG_ID_CROWD, registry)
    admin_id = crowd_cfg['admin-login']
    admin = ptah_crowd.CrowdFactory().get_user_bylogin(admin_id)

    root = APP_FACTORY()

    # give manager role to admin
    if admin.__uri__ not in root.__local_roles__:
        root.__local_roles__[admin.__uri__] = [Manager.id]

    # set authcontext so content shows created by admin
    ptah.auth_service.set_userid(admin.__uri__)

    # create default page
    if 'front-page' not in root.keys():
        page = Page(title='Welcome to Ptah')
        page.text = open(
            abspath_from_asset_spec('ptah_minicms:welcome.pt'), 'rb').read()

        root['front-page'] = page


def main(global_config, **settings):
    """ This is your application startup.
    """
    config = Configurator(root_factory=APP_FACTORY, settings=settings)

    # static assets
    config.add_static_view('ptah_minicms', 'ptah_minicms:static')

    config.scan()

    # init sqlalchemy engine
    config.ptah_init_sql()

    # init ptah settings
    config.ptah_init_settings()

    # enable rest api
    config.ptah_init_rest()

    # enable ptah manage
    config.ptah_init_manage()

    # populate database
    config.ptah_populate()

    return config.make_wsgi_app()
