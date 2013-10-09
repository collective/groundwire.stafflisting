from five import grok
from groundwire.stafflisting import _
from plone.app.textfield import RichText
from plone.directives import form
from plone.namedfile.field import NamedBlobImage
from zope import schema

class IPerson(form.Schema):
    """A Person.
    """
    
    title = schema.TextLine(
            title = _(u"Name"),
        )

    position = schema.TextLine(
            title = _(u"Position"),
            required = False,
        )

    description = schema.Text(
            title = _(u"Summary"),
            description = _(u"A brief description of this person's role."
                            u"This will never show up in the same place "
                            u"as the full bio below, so you may overlap "
                            u"some of those details."),
        )

    text = RichText(
            title = _(u"Bio"),
            required = False
        )

    image = NamedBlobImage(
            title = _(u"Portrait"),
            description = _(u"Please upload an image. Keep portrait "
                            u"dimensions consistent throughout the site!"),
            required = False,
        )

    phone = schema.TextLine(
            title = _(u"Phone Number"),
            description = _(u"Include extension, if applicable. Be sure to "
                            u"Keep your formatting consistent throughout the "
                            u"site!"),
            required = False,
        )

    email = schema.TextLine(
            title = _(u"Email address"),
            description = _(u"This will be shown in a way that is hard for "
                            u"spammers to find."),
            required = False,
        )

    twitter = schema.TextLine(
            title = _(u"Twitter handle"),
            required = False,
        )

    skype = schema.TextLine(
            title = _(u"Skype username"),
            required = False,
        )

    blog = schema.TextLine(
            title = _(u"Blog url"),
            description = _(u"That is, a blog belonging just to this person "
                            u"that is relevant in the context of this site."),
            required = False,
        )

    other_contact = schema.TextLine(
            title = _(u"Other contact information"),
            description = _(u"Are there any other means of contacting this "
                            u"person not already covered above?"),
            required = False,
        )

class View(grok.View):
    grok.context(IPerson)
    grok.require('zope2.View')
