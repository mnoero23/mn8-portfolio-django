from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0002_post_imagen"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="autor",
            new_name="autor_legacy",
        ),
        migrations.AddField(
            model_name="post",
            name="autor",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="publicaciones",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
