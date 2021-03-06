""" app permissions and roles """
import ptah

AddPage = ptah.Permission('ptah_ws: Add page', 'Add page')
AddFile = ptah.Permission('ptah_ws: Add file', 'Add file')
AddFolder = ptah.Permission('ptah_ws: Add folder', 'Add folder')

ptah.Everyone.allow(ptah.cms.View)
ptah.Authenticated.allow(ptah.cms.AddContent)

Viewer = ptah.Role('viewer', 'Viewer')
Viewer.allow(ptah.cms.View)

Editor = ptah.Role('editor', 'Editor')
Editor.allow(ptah.cms.View, ptah.cms.ModifyContent)

Manager = ptah.Role('manager', 'Manager')
Manager.allow(ptah.cms.ALL_PERMISSIONS)

ptah.Owner.allow(ptah.cms.DeleteContent)
