from django.test import TestCase
from .models import *

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='kids')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category_method(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)

class LocationTestClass(TestCase):

    def setUp(self):
        self.location= Location(name = 'Paris')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_updating_location(self):
        location = Location.get_location_id(self.Paris.id)
        location.update_location('Paris')
        location = Location.get_location_id(self.Paris.id)
        self.assertTrue(location.location == 'Paris')

    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)

class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(id=1,name='kids',pic='imageurl',description='happy kids')
        self.location= Location(name = 'KIgali')
        self.location.save_location()
        self.category = Category(name='kids')
        self.category.save_category()
        self.image.location.add(self.location)
        self.image.category.add(self.category)


    def test_image_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)
    def test_get_image_by_id(self):
        image= Image.get_image_by_id(self.image.id)
        self.assertTrue(len(image) == 1)
    def test_get_images(self):
        images = Image.get_images()
        self.assertTrue(len(images)>0)

    def test_filter_by_location(self):
       
       self.image.save_image()
       this_img = self.image.filter_by_location(self.image.location_id)
       image = Image.objects.filter(location=self.image.location_id)
       self.assertTrue(this_img, image)

    def test_delete_image_method(self):
        self.image.save_image()
        images = Image.objects.all()
        self.image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

    def tearDown(self):
        self.image.delete_image()
        self.category.delete_category()
        self.location.delete_location()