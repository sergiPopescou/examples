""" Generic folder implementation """
from ptah import cms
from ptah_minicms.permissions import AddFolder


class Folder(cms.Container):
    """
    A Folder model which subclasses ptah.cms.Container
    """

    __type__ = cms.Type(
        'folder',
        title = 'Folder',
        description = 'A folder which can contain other items.',
        permission = AddFolder)
