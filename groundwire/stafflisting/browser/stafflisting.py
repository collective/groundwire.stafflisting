from Acquisition import aq_base
from groundwire.stafflisting.person import IPerson
from Products.CMFCore.utils import getToolByName
from zope.publisher.browser import BrowserView

class StaffListingTopicView(BrowserView):
    """
    A listing of people. Used by Topics.
    """

    def getPeople(self):
        """
        Returns a sorted list of full Person objects. Real people.
        """
        # by default, sort by gopip if no sort criterion is provided (since
        # it's not a sort criterion option by default)
        kw = dict(object_provides = IPerson.__identifier__,
                  full_objects = True,
                  )
        if hasattr(aq_base(self.context), "hasSortCriterion") and \
          not self.context.hasSortCriterion():
            kw['sort_on'] = 'getObjPositionInParent'
        return self.context.queryCatalog(**kw)

class StaffListingFolderView(StaffListingTopicView):
    """
    A listing of people. Used by Folders.
    """

    def getPeople(self):
        """
        Returns a sorted list of full Person objects. Real people.
        """
        portal_catalog = getToolByName(self.context, "portal_catalog")
        query = dict(object_provides = IPerson.__identifier__,
                     path = '/'.join(self.context.getPhysicalPath()),
                     sort_on = 'getObjPositionInParent',
                     )
        return [b.getObject() for b in portal_catalog(**query)]

