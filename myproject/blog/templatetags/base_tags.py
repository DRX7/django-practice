from django import template
from blog.models import Category

register = template.Library()



@register.simple_tag
def title():
    return "سایت"


@register.inclusion_tag('blog/partials/category_navbar.html')
def category_navbar():
    return {
        'category': Category.objects.filter(status=True)
    }


@register.inclusion_tag("registration/partials/link.html")
def link(request , link_name , content , icon):
    return {
        "request" : request,
        "link_name" : link_name,
        "link" : "account:{}".format(link_name),
        "content" : content,
        "icon" : icon,
    }
    