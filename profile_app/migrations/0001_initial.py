from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, default='profile_img.jpg', null=True, upload_to='photos/')),
                ('gender', models.CharField(default=None, max_length=1)),
                ('age', models.IntegerField(default=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),

            ],
        ),
    ]
