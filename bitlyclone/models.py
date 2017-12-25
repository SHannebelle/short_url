from django.db import models
import random
import string


class ShortUrl(models.Model):
    url = models.URLField(verbose_name="URL to shorten", unique = True)
    code = models.CharField(max_length=6,unique = True)
    date = models.DateTimeField(auto_now_add = True,
                                verbose_name="Shortening Date")
    username = models.CharField(max_length = 30, blank = True, null = True)
    nb_access = models.IntegerField(default=0, verbose_name="Number of access to the URL")

    def __str__(self):
        return "[{0}] {1}".format(self.code,self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.randomcode(6)

        super(ShortUrl, self).save(*args,**kwargs)

    def randomcode(self, nb_chart):
        chart = string.ascii_letters + string.digits
        rand = [random.choice(chart) for _ in range(nb_chart)]

        self.code = ''.join(rand)

        class Meta:
            verbose_name = "Short URL"
            verbose_name_plural = "Short URLs"

