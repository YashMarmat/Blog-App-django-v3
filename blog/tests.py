from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Blog


class BlogTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@gmail.com',
            password = 'secret',
        )
        
        self.blog = Blog.objects.create(
            title = 'A good title',
            body = 'any description',
            author = self.user,
        )
    
    def test_string_representation(self):           # testing __str__(self) of models.py 
        blog = Blog(title='sample title')
        self.assertEqual(str(blog), blog.title)

    def test_get_absolute_url(self):
        self.assertEqual(self.blog.get_absolute_url(), '/1')
    
    def test_blog_content(self):
        self.assertEqual(f'{self.blog.title}', 'A good title')
        self.assertEqual(f'{self.blog.body}', 'any description')
        self.assertEqual(f'{self.blog.author}', 'testuser')


    def test_blog_list_view_for_logged_in_user(self): # new        
        self.client.login(username = 'testuser', email='test@gmail.com', password='secret')
        request = self.client.get(reverse('blog_list'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'A good title')
        self.assertTemplateUsed(request, 'blog_list.html')
    
    def test_blog_list_view_for_logged_out_user(self):
        self.client.logout()
        request = self.client.get(reverse('blog_list'))
        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request, '/accounts/login/?next=/')  # if not logged in then the user gets redirected to this url
        request = self.client.get('/accounts/login/?next=/')  # if user request for this url, they recieve below content
        self.assertContains(request, 'Log In') # on login page there should be a text 'Log In'
        self.assertTemplateUsed(request, 'registration/login.html') # tampate used 

    def test_detail_page_for_logged_in_user(self):
        self.client.login(username = 'testuser', email='test@gmail.com', password='secret')
        request = self.client.get(reverse('blog_detail', args = '1'))
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'A good title')
        self.assertContains(request, 'any description')   
        self.assertTemplateUsed(request, 'blog_detail.html')
    
    def test_detail_page_for_logged_out_user(self):
        self.client.logout()
        request = self.client.get(reverse('blog_detail', args = '1'))
        self.assertEqual(request.status_code, 302) # send loggout user to different page
        self.assertRedirects(request, '/accounts/login/?next=/1') # redirects the user to login page   

        
    def test_blog_create_for_logged_in_user(self):
        self.client.login(username = 'testuser', email='test@gmail.com', password='secret')
        request = self.client.post(reverse('blog_new'), {
            'title': 'my new blog',
            'body': 'my new description',
            'author': self.user,
        })
        self.assertEqual(request.status_code, 200)
        self.assertContains(request, 'my new blog')
        self.assertContains(request, 'my new description')
        self.assertContains(request, 'testuser')

    def test_blog_create_not_logged_in_user(self):
        self.client.logout()
        request = self.client.post(reverse('blog_new'), {
            'title': 'my new blog',
            'body': 'my new description',
            'author': self.user,
        })
        self.assertEqual(request.status_code, 302)
        self.assertRedirects(request, '/accounts/login/?next=/new/')        


    def test_blog_update_view_for_logged_in_user(self):
        self.client.login(username = 'testuser', email='test@gmail.com', password='secret')
        request = self.client.post(reverse('blog_update', args = '1'), {
            'title': 'updated title', 
            'body': 'updated description',
        })
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'blog_update.html')
    
    def test_blog_update_for_not_logged_in_user(self):
        self.client.logout()
        request = self.client.post(reverse('blog_update', args = '1'), {
            'title': 'updated title', 
            'body': 'updated description',
        })
        self.assertEqual(request.status_code, 403)  # Forbidden for logged out user 

    def test_blog_delete_view_for_logged_in_user(self):
        self.client.login(username = 'testuser', email='test@gmail.com', password='secret')
        request = self.client.post(reverse('blog_delete', args = '1'))
        self.assertEqual(request.status_code, 302)

    def test_blog_delete_view_for_not_logged_in_user(self):
        self.client.logout()
        request = self.client.post(reverse('blog_delete', args = '1'))
        self.assertEqual(request.status_code, 403)  # Forbidden for logged out user 

