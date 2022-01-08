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
    