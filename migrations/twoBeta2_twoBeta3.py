import zLOG
from Products.CMFCore.Expression import Expression
from Products.CMFCore.utils import getToolByName

def twoBeta2_twoBeta3(portal):
    """ Migrations from to 2.0 beta 2 to 2.0 beta 3 """
    out = []

    # as per bug #1600
    out.append("Altering my preferences to point at the member preferences panel")
    pm = portal.portal_membership
    actions = pm._cloneActions()
    for action in actions:
        if action.id=='preferences':
            txt = action.action.text.replace('personalize_form', 'plone_memberprefs_panel')
            action.action = Expression(txt)
    pm._actions = tuple(actions)

    # ensure that Plone Site is in portal_types
#    pt = getToolByName(portal, "portal_types")
#    if "Plone Site" not in pt.objectIds():
#        from Products.CMFPlone.Portal import factory_type_information
#        pt.manage_addTypeInformation(
#            factory_type_information['meta_type'],
#            id = factory_type_information['id'],
#            typeinfo_name = "CMFPlone: Plone Site"
#        )

    # and then in workflow remove any workflow from it
#    wt = getToolByName(portal, "portal_workflow")
#    wt.setChainForPortalTypes(("Plone Site"), "")


if __name__=='__main__':
    registerMigrations()

