# Generated by Django 2.1.9 on 2019-07-02 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("gsoc", "0037_auto_20190629_1627")]

    operations = [
        migrations.AlterField(
            model_name="scheduler",
            name="command",
            field=models.CharField(
                choices=[
                    ("send_email", "send_email"),
                    ("send_irc_msg", "send_irc_msg"),
                    ("revoke_student_permissions", "revoke_student_permissions"),
                    ("send_reg_reminder", "send_reg_reminder"),
                    ("add_blog_counter", "add_blog_counter"),
                    ("update_site_template", "update_site_template"),
                ],
                max_length=40,
            ),
        )
    ]
