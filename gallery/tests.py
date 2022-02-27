from django.test import TestCase
from .models import Image, Location, Category


# Create your tests here.
class LocationTestClass(TestCase):
    # Set up method for location

    def setUp(self):
        self.location = Location(name="Modern food")
        self.location.save_location()

    def tearDown(self):
        Location.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))


class CategoryTestClass(TestCase):
    # Set up method for category

    def setUp(self):
        self.category = Category(name="Modern food")
        self.category.save_category()

    def tearDown(self):
        Category.objects.all().delete()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))


# class ImageTestClass(TestCase):

#     # Set up method for image
#     def setUp(self):
#         self.location = Location(name='Narok')
#         self.location.save_location()

#         self.category = Category(name="Modern food")
#         self.category.save_category()

#         self.image = Image(image='pexels-christina-morillo-1181352_1.jpg', name="Modern food",
#                            description="The best food to have for dinner", date=None,
#                            category=self.category, location=self.location)



#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.image, Image))

#     # Testing Save Method
#     def test_save_method(self):
#         self.image.save_image()
#         images = Image.objects.all()
#         self.assertTrue(len(images) > 0)

#     def tearDown(self):
#         Image.objects.all().delete()
# # Added tes for category and location
#     def test_filter_by_location(self):
#         self.location = Image.filter_by_location("1")

#     def test_search_by_category(self):
#         self.category = Image.search_by_category("Modern food")

