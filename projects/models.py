from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="")
    price = models.IntegerField()


# p1 = Project(
#     title='Toy Cat',
#     description='A toy cat.',
#     technology='Django',
#     image='img/product1.png',
#     price="14"
# )
#
# p2 = Project(
#     title='Toy Dog',
#     description='A toy dog.',
#     technology='Django',
#     image='img/product2.png',
#     price="15"
# )
#
# p3 = Project(
#     title='Toy Pig',
#     description='A toy pig.',
#     technology='Django',
#     image='img/product3.png',
#     price="17"
# )
