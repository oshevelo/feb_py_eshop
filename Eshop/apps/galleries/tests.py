import os

from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.test import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status

from apps.galleries.models import Gallery
from apps.products.models import Product

class GalleryTestAPI(TestCase):
    def setUp(self):
        self.password = '12345'
        self.user = User.objects.create_user('John Doe', 'JohnDoe@gmail.com', self.password)

        p1 = Product.objects.create(name='testp', description='asd')
        # p2 = Product.objects.create(name='testp', description='asd')

        image_test1 = SimpleUploadedFile(name='photo1.jpg', content=open('static/test/photo1.jpg', 'rb').read(), content_type='image/jpeg')
        self.g1 = Gallery.objects.create(product=p1, name='test_g1', image=image_test1)
        self.g2 = Gallery.objects.create(product=p1, name='test_g2', image='')

        self.c = APIClient()


    def test_get_galleries_list(self):
        response = self.c.get('/galleries/')
        self.assertEqual(response.status_code, 200)
        # print(response.json())
        self.assertEqual(response.json(), {
            'count': 2, 'next': None, 'previous': None, 'results': [{'product': {'id': 1, 'name': 'testp'}, 'id': 1, 'name': 'test_g1', 'imageSmall_url': '/product_photos/CACHE/images/originals/2020/06/28/photo1_B2RtjbY/839f85b587be6cc83f63566deba9bfe3.jpg', 'imageMedium_url': '/product_photos/CACHE/images/originals/2020/06/28/photo1_B2RtjbY/1925cdad75b3215e1509df658f4e67e1.jpg', 'imageBig_url': '/product_photos/CACHE/images/originals/2020/06/28/photo1_B2RtjbY/af9d73e570948933a516ab4387b7bb2f.jpg'}, {'product': {'id': 1, 'name': 'testp'}, 'id': 2, 'name': 'test_g2', 'imageSmall_url': '/static/pictures/no_image.png', 'imageMedium_url': '/static/pictures/no_image.png', 'imageBig_url': '/static/pictures/no_image.png'}]})


    def zzztest_product_gallereis_pagination_list(self):
        response = self.c.get('/galleries/1/?limit=1&offset=1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 2, 
            'next': None, 
            'previous': 'http://testserver/galleries/1/?limit=1', 
            'results': [{
                'product': {
                    'id': 1, 
                    'name': 'testp'
                }, 
                'id': 2, 
                'name': 'test_g2', 
                'url': '/static/pictures/no_image.png', 
                'size': 'max', 
                'size_x': 250, 
                'size_y': 250
            }]
        })
    

    def zzztest_get_gallery(self):
        response = self.c.get('/galleries/1/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product': {
                'id': 1, 
                'name': 'testp'
            }, 
            'id': 1, 
            'name': 'test_g1', 
            'url': self.g1.image_url, 
            'size': 'middle', 
            'size_x': 150, 
            'size_y': 150
        })


    def zzztest_post_gallery(self):
        p1 = Product.objects.create(name='other product', description='asd')
        self.c.login(username=self.user.username, password=self.password)

        with open(os.path.join(settings.STATIC_ROOT, 'test', 'image_file.jpg'), mode='rb') as fp:
            response = self.c.post(
                '/galleries/1/',
                data={
                    "product": p1.id,
                    "name": "test_post_g",
                    "image": fp,
                    "size": "min",
                } 
            )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        created_object = Gallery.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'product': {
                'id': p1.id, # 2
                'name': 'other product'
            }, 
            'id': created_object.id, # 3
            'name': 'test_post_g', 
            'url': created_object.image_url, 
            'size': 'min', 
            'size_x': 50, 
            'size_y': 50
        })


    def zzztest_get_gallery_failed(self):
        response = self.c.get('/galleries/1/3/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'detail': 'Not found.'
        })


    def zzztest_gallereis_list_filter(self):
        response = self.c.get('/galleries/?id=&product=1&name=g1&size=')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 1, 
            'next': None, 
            'previous': None, 
            'results': [{
                'product': {
                    'id': 1, 
                    'name': 'testp'
                }, 
                'id': 1, 
                'name': 'test_g1', 
                'url': self.g1.image_url, 
                'size': 'middle', 
                'size_x': 150, 
                'size_y': 150
            }]
        })

        
    def zzztest_product_gallereis_list_filter(self):
        response = self.c.get('/galleries/1/?id=2&name=&size=m')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 1, 
            'next': None, 
            'previous': None, 
            'results': [{
                'product': {
                    'id': 1, 
                    'name': 'testp'
                }, 
                'id': 2, 
                'name': 'test_g2', 
                'url': '/static/pictures/no_image.png', 
                'size': 'max', 
                'size_x': 250, 
                'size_y': 250
            }]
        })


    def zzztest_product_not_gallereis_filter(self):
        response = self.c.get('/galleries/1/?id=42&product=&name=&size=')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 0, 
            'next': None, 
            'previous': None, 
            'results': []
        })


    def zzztest_patch_gallery(self):
        p1 = Product.objects.create(name='other product', description='asd')
        self.c.login(username=self.user.username, password=self.password)
        response = self.c.patch(
            '/galleries/1/1/', 
            data={
                "product": p1.id,
                "size": "max",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'product': {
                'id': p1.id, # 2
                'name': 'other product'
            }, 
            'id': 1, 
            'name': 'test_g1', 
            'url': self.g1.image_url, 
            'size': 'max', 
            'size_x': 250, 
            'size_y': 250
        })


    def zzztest_put_gallery(self):
        p1 = Product.objects.create(name='other product', description='asd')
        self.c.login(username=self.user.username, password=self.password)
        with open(os.path.join(settings.STATIC_ROOT, 'test', 'image_file.jpg'), mode='rb') as fp:
            response = self.c.put(
                '/galleries/1/2/',
                data={
                    "product": p1.id,
                    "name": "test_put_g",
                    "image": fp,
                } 
            )
        self.assertEqual(response.status_code, 200)
        created_object = Gallery.objects.get(id=response.json()['id'])
        self.assertEqual(response.json(), {
            'product': {
                'id': p1.id, # 2 
                'name': 'other product'
            }, 
            'id': 2, 
            'name': 'test_put_g', 
            'url': created_object.image_url, # self.g2.image_url: /static/pictures/no_image.png
            'size': 'max', # Почему не дефолтное значение (middle)?
            'size_x': 250, 
            'size_y': 250
        })


    def zzztest_delete_gallery(self):
        response = self.c.delete('/galleries/1/2/')
        self.assertEqual(response.status_code, 204) # No Content

