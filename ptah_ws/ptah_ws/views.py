from datetime import datetime
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotFound

import ptah
from ptah_ws import settings
from ptah_ws.root import SiteRoot


# access this view by going to http://localhost:8080/myview.html
# add ptah_ws.band=my band to .ini file, restart and render this view.

@view_config('myview.html',
             context=SiteRoot, wrapper=ptah.layout())
def my_view(request):
    data = {'context' : request.root,
            'happy' : settings.ptah_ws.happy,
            'favband' : settings.ptah_ws.band,
            'now' : datetime.now()}
    return str(data)


@view_config(
    context=ptah.cms.Content,
    permission=ptah.cms.View,
    wrapper=ptah.wrap_layout(),
    renderer="ptah_ws:templates/contentview.pt")

class DefaultContentView(ptah.form.DisplayForm):

    @property
    def fields(self):
        return self.context.__type__.fieldset

    def form_content(self):
        data = {}
        for name, field in self.context.__type__.fieldset.items():
            data[name] = getattr(self.context, name, field.default)

        return data


@view_config(
    'edit.html',
    context=ptah.cms.Content,
    wrapper=ptah.wrap_layout(),
    permission=ptah.cms.ModifyContent)
class EditForm(ptah.cms.EditForm):
    """ Content edit form """


@view_config(
    context=ptah.cms.Container,
    permission=ptah.cms.View,
    wrapper=ptah.wrap_layout(),
    renderer="ptah_ws:templates/listing.pt")

@view_config(
    'listing.html',
    context=ptah.cms.Container,
    permission=ptah.cms.View,
    wrapper=ptah.wrap_layout(),
    renderer="ptah_ws:templates/listing.pt")

class ContainerListing(ptah.View):

    def update(self):
        context = self.context
        request = self.request
        registry = request.registry

        self.deleteContent = ptah.check_permission(
            ptah.cms.DeleteContent, context)

        # cms(uri).read()
        # cms(uri).create(type)
        # cms(uri).delete()
        # cms(uri).update(**kwargs)
        # cms(uri).items(offset, limit)

        if self.deleteContent and 'form.buttons.remove' in request.POST:
            uris = self.request.POST.getall('item')
            for uri in uris:
                ptah.cms.wrap(uri).delete()

                self.message("Selected content items have been removed.")


@view_config(
    'rename.html', context=ptah.cms.Container,
    wrapper=ptah.wrap_layout(),
    renderer="ptah_ws:templates/folder_rename.pt")

class RenameForm(ptah.View):
    """ """


@view_config(
    '+', context=ptah.cms.Container,
    wrapper=ptah.wrap_layout(),
    renderer="ptah_ws:templates/adding.pt")

class Adding(ptah.View):

    def update(self):
        self.url = self.request.resource_url(self.context)

        types = [(t.title, t) for t in
                 self.context.__type__.list_types(self.context)]
        types.sort()

        self.types = [t for _t, t in types]

    def __call__(self):
        subpath = self.request.subpath
        if subpath and subpath[0]:
            tname = subpath[0]
            tinfo = ptah.cms.get_type('cms-type:%s'%tname)
            if tinfo is None:
                return HTTPNotFound

            return AddContentForm(tinfo, self, self.request)()

        return super(Adding, self).__call__()


class AddContentForm(ptah.cms.AddForm):

    def __init__(self, tinfo, form, request):
        super(AddContentForm, self).__init__(form, request)

        self.tinfo = tinfo
        self.container = form.context


@view_config('wstest.html', context=SiteRoot,
             wrapper=ptah.wrap_layout('workspace'),
             renderer='ptah_ws:templates/wstest.pt')
def wstest_view(request):
    return {}
