from django.db import models
from benjamin.registration.models import User


# Create your models here.
class VirtueSet(models.Model):
    user = models.ForeignKey(User, related_name='virtue_sets', on_delete=models.CASCADE)
    title = models.TextField()

    def __str__(self):
        return "<VirtueSet belonging to user {0}".format(self.user.id)


class Virtue(models.Model):
    user = models.ForeignKey(User, related_name='virtues', on_delete=models.CASCADE)
    virtue_set = models.ForeignKey(VirtueSet, related_name='virtues', on_delete=models.CASCADE)
    title = models.TextField()
    image = models.ImageField(null=True, blank=True)
    personal_image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    personal_description = models.TextField(null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    personal_quote = models.TextField(null=True, blank=True)

    def __str__(self):
        return "<Virtue id: {0}".format(self.id)


class VirtueEntryManager(models.Manager):

    def on_same_day(self, user_id, virtue_id, date):
        try:
            same_day_entry = VirtueEntry.objects.get(
                user_id=user_id,
                virtue_id=virtue_id,
                date__day=date.day,
                date__month=date.month,
                date__year=date.year,
            )
        except VirtueEntry.DoesNotExist:
            same_day_entry = None

        return same_day_entry


class VirtueEntry(models.Model):
    objects = VirtueEntryManager()
    user = models.ForeignKey(User, related_name='virtue_entries', on_delete=models.CASCADE)
    virtue = models.ForeignKey(Virtue, related_name='virtue_entries', on_delete=models.CASCADE)
    date = models.DateTimeField()
    value = models.IntegerField()

    def __str__(self):
        return "<VirtueEntry id: {0}".format(self.id)
