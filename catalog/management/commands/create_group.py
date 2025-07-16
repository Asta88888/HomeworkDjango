from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с нужными правами'

    def handle(self, *args, **kwargs):
        group, created = Group.objects.get_or_create(name='Moderators')
        product_ct = ContentType.objects.get_for_model(Product)

        can_unpublish = Permission.objects.get(
            content_type=product_ct,
            codename='can_unpublish_product'
        )
        can_delete = Permission.objects.get(
            content_type=product_ct,
            codename='delete_product'
        )

        group.permissions.set([can_unpublish, can_delete])
        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана и права назначены.'))