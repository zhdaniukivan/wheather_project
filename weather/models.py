from django.db import models


class CityName(models.Model):
    city_name = models.CharField(max_length=100)
    count_of_search= models.IntegerField(null=True)

    def __str__(self):
        return self.city_name


class UsersLastSearch(models.Model):
    user_id = models.IntegerField()
    city_name = models.ForeignKey(CityName, on_delete=models.PROTECT, null=True)
    last_searched = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return str(self.user_id)




