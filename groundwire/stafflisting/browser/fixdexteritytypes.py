from zope.publisher.browser import BrowserPage
from Products.CMFCore.utils import getToolByName
from plone.dexterity.interfaces import IDexterityFTI

TYPES_TO_FIX = [
    'groundwire.stafflisting.person',
]

class FixDexterityTypes(BrowserPage):
    """
    Modifies the add_view_expr on our Dexterity FTIs so that they behave
    correctly when added to a folder where a collection is the default item.
    """
    
    def __call__(self):
        
        portal_types = getToolByName(self.context, 'portal_types')
        for fti in portal_types.objectValues():
            if IDexterityFTI.providedBy(fti) and fti.id in TYPES_TO_FIX:
                add_view_expr = "python:object.restrictedTraverse('plone_context_state').folder().absolute_url() + '/++add++%s'" % fti.getId()
                fti._setPropValue('add_view_expr', add_view_expr)
        
        return 'Success!'