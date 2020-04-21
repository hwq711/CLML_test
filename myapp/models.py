from django.db import models


# Create your models here.
class Drug(models.Model):
    drug_name = models.CharField(max_length=50)

    def __str__(self):
        return self.drug_name


class Relation(models.Model):
    drug_x = models.CharField(max_length=50)
    drug_y = models.CharField(max_length=50)
    relation_value = models.DecimalField(max_digits=10, decimal_places=6)


class Known_Relation(models.Model):
    drug_x = models.CharField(max_length=50)
    drug_y = models.CharField(max_length=50)
    relation_value = models.DecimalField(max_digits=10, decimal_places=6)
