import ptah
from ptah import view, cms, manage, auth_service

from ptah_minicms.app import ApplicationRoot
from ptah_minicms.actions import CATEGORY


ptah.register_layout(
    'ptah-page', ApplicationRoot, parent='workspace',
    renderer='ptah_minicms:templates/layout-ptahpage.pt')


@ptah.layout(
    'page', ApplicationRoot,
    renderer='ptah_minicms:templates/layout-page.pt')

class PageLayout(ptah.View):
    """ override 'page' layout

    layer - identifier, import order does matter, last imported wins
    """


@ptah.layout(
    'workspace', ApplicationRoot, parent='page',
    renderer='ptah_minicms:templates/layout-workspace.pt')

class WorkspaceLayout(ptah.View):
    """ same as PageLayout, it uses 'page' as parent layout """

    def update(self):
        self.user = ptah.auth_service.get_current_principal()
        self.ptahManager = manage.check_access(
            ptah.auth_service.get_userid(), self.request)
        self.isAnon = self.user is None


@ptah.layout(
    '', ptah.cms.Content, parent="workspace",
    renderer="ptah_minicms:templates/layout-content.pt")
class ContentLayout(ptah.View):
    """ Content layout """

    def update(self):
        self.actions = ptah.list_uiactions(
            self.context, self.request, CATEGORY)