from django.core.management.base import BaseCommand
from blog.models import Post


class Command(BaseCommand):
    help = 'Добавление постов в базу данных'

    def handle(self, *args, **options):
        posts_data = [
            {'title': 'Первый пост', 'content': 'Это первый тестовый пост', 'publication_flag': True, 'number_of_views': 0,},
            {'title': 'Второй пост', 'content': 'Это второй тестовый пост', 'publication_flag': False, 'number_of_views': 10,}
        ]

        for post_data in posts_data:
            post, created = Post.objects.get_or_create(**post_data)
            if created:
                self.stdout.write(self.style.SUCCES(f'Добавлен пост: {post.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Пост {post.title} уже существует'))
