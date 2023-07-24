from uuid import uuid4

from django.db.models import Model, DateTimeField, UUIDField, CharField, FloatField, PositiveIntegerField, ForeignKey, \
    CASCADE, IntegerChoices, SET_NULL, ManyToManyField


class BaseModel(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title if hasattr(self, 'title') else str(self.id)


class Product(BaseModel):
    title = CharField(max_length=255)
    description = CharField(max_length=255)
    price = FloatField()
    categories = ManyToManyField('apps.Category', related_name='products')


class Category(BaseModel):
    title = CharField(max_length=255)


class Rate(BaseModel):
    class RateChoices(IntegerChoices):
        WORST = 1, 'Worst'
        BAD = 2, 'Bad'
        GOOD = 3, 'Good'
        BETTER = 4, 'Better'
        BEST = 5, 'Best'

    product = ForeignKey('apps.Product', CASCADE)
    rate = PositiveIntegerField(choices=RateChoices.choices, default=RateChoices.GOOD)
    user = ForeignKey('auth.User', SET_NULL, null=True, blank=True)
