# Generated by Django 4.0.4 on 2022-05-19 15:17

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('isModerator', models.IntegerField(db_column='isModerator', default=False)),
                ('isAdministrator', models.IntegerField(db_column='isAdministrator', default=False)),
                ('profilePic', models.TextField(blank=True, db_column='profilePic', null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'Korisnik',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('articleId', models.AutoField(db_column='articleId', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=25)),
                ('slug', models.CharField(max_length=25, unique=True)),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2022, 5, 19, 15, 17, 41, 322328))),
                ('isValidated', models.IntegerField(db_column='isValidated')),
                ('textContent', models.TextField(db_column='textContent')),
                ('previewPicture', models.TextField(blank=True, db_column='previewPicture', null=True)),
                ('numOfLikes', models.IntegerField(default=0)),
                ('korisnikId', models.ForeignKey(db_column='korisnikId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.AutoField(db_column='categoryId', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('questionId', models.AutoField(db_column='questionId', primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('answer1', models.CharField(blank=True, max_length=50, null=True)),
                ('answer2', models.CharField(blank=True, max_length=50, null=True)),
                ('answer3', models.CharField(blank=True, max_length=50, null=True)),
                ('answer4', models.CharField(blank=True, max_length=50, null=True)),
                ('points', models.IntegerField()),
                ('correct', models.IntegerField()),
                ('articleId', models.ForeignKey(db_column='articleId', on_delete=django.db.models.deletion.DO_NOTHING, to='learnopedia.article')),
            ],
            options={
                'db_table': 'Question',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('commentId', models.AutoField(db_column='commentId', primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('createdAt', models.DateTimeField(default=datetime.datetime(2022, 5, 19, 15, 17, 41, 323121))),
                ('articleId', models.ForeignKey(db_column='articleId', on_delete=django.db.models.deletion.DO_NOTHING, to='learnopedia.article')),
                ('korisnikId', models.ForeignKey(db_column='korisnikId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='KorisnikLikedArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleId', models.ForeignKey(db_column='articleId', on_delete=django.db.models.deletion.DO_NOTHING, to='learnopedia.article')),
                ('korisnikId', models.ForeignKey(db_column='korisnikId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'KorisnikLikedArticle',
                'unique_together': {('korisnikId', 'articleId')},
            },
        ),
        migrations.CreateModel(
            name='KorisnikArticleGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('articleId', models.ForeignKey(db_column='articleId', on_delete=django.db.models.deletion.DO_NOTHING, to='learnopedia.article')),
                ('korisnikId', models.ForeignKey(db_column='korisnikId', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'KorisnikArticleGrade',
                'unique_together': {('articleId', 'korisnikId')},
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleId', models.ForeignKey(db_column='articleId', on_delete=django.db.models.deletion.DO_NOTHING, to='learnopedia.article')),
                ('categoryId', models.ForeignKey(db_column='categoryId', on_delete=django.db.models.deletion.DO_NOTHING, to='learnopedia.category')),
            ],
            options={
                'db_table': 'ArticleCategory',
                'unique_together': {('articleId', 'categoryId')},
            },
        ),
    ]
