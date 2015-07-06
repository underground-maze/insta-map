from django.contrib.auth.models import AbstractUser, UserManager


class InstaUser(AbstractUser):

    """ Custom user model for additional fields """

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        """ Set username equal to email """
        if not self.username:
            self.username = self.email
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'auth_user'
