""" file content implementation """
import sqlalchemy as sqla
from pyramid.view import view_config

import ptah
from ptah import cms
from ptah_ws.permissions import AddFile


class File(cms.Content):
    """
    A File model that subclasses ptah.cms.Content
    """

    __tablename__ = 'ptah_ws_files'

    __type__ = cms.Type(
        'file',
        title = 'File',
        description = 'A file in the site.',
        permission = AddFile,
        addview = 'addfile.html',
        )

    blobref = sqla.Column(
        sqla.Unicode,
        info = {'title': 'Data',
                'field_type': 'file',
                'uri': True})

    @cms.action(permission=cms.ModifyContent)
    def update(self, **data):
        """ Update file content. """
        fd = data.get('blobref')
        if fd:
            blob = ptah.resolve(self.blobref)
            if blob is None:
                blob = cms.blobStorage.create(self)
                self.blobref = blob.__uri__

            blob.write(fd['fp'].read())
            blob.updateMetadata(
                filename = fd['filename'],
                mimetype = fd['mimetype'])

        self.title = data['title']
        self.description = data['description']

    @cms.action(permission=cms.View)
    def data(self):
        """ Download data. """
        blob = ptah.resolve(self.blobref)
        if blob is None:
            raise cms.NotFound()

        return {'mimetype': blob.mimetype,
                'filename': blob.filename,
                'data': blob.read()}


@view_config('download.html', context=File, permission=cms.View)
def fileDownloadView(context, request):
    data = context.data()

    response = request.response
    response.content_type = data['mimetype'].encode('utf-8')
    response.headerlist = {
        'Content-Disposition':
        'filename="%s"'%data['filename'].encode('utf-8')}
    response.body = data['data']
    return response


@view_config(
    context=File,
    permission=cms.View,
    wrapper=ptah.wrap_layout(),
    renderer='ptah_ws:templates/file.pt')
def fileView(context, request):
    return {'resolve': ptah.resolve,
            'format': ptah.format}


@view_config('addfile.html', context=cms.Container, permission=AddFile)
class FileAddForm(cms.AddForm):

    tinfo = File.__type__

    def chooseName(self, **kw):
        filename = kw['blobref']['filename']
        name = filename.split('\\')[-1].split('/')[-1]

        i = 1
        n = name
        while n in self.container:
            i += 1
            n = '%s-%s'%(name, i)

        return n
