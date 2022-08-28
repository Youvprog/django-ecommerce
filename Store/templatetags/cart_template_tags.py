from django import template
from Store.models import Cart

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        querySet = Cart.objects.filter(user=user, ordered=False)
        if querySet.exists():
            return querySet[0].orderitems.count()
    return 0