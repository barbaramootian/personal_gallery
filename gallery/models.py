from django.db import models


# Create your models here.
# Location model
class Location(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        ordering = ['-name']
    @classmethod
    def get_locations(cls, id):
        locations = Location.objects.get(pk=id)
        return locations

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


# Category model
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-name']

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

# # Image model
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, image, name, description, category, location):
        self.image = image
        self.name = name
        self.description = description
        self.category = category
        self.location = locationn
        self.save()

    @classmethod
    def get_image_by_id(cls, id):
        result = cls.objects.get(id=id)
        return result

    @classmethod
    def filter_by_location(cls, id):
        result = cls.objects.filter(location__id=id)
        return result

    @classmethod
    def search_by_category(cls, category):
        result = cls.objects.filter(category__name=category)
        return result

        # help in updating model to allow easily read of the models
    def __str__(self):
        return self.name


