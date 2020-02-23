
-login and signup
 
for login -> login.html, predefined django module inside project level urls.py file and then 
changes in home.html (in this project it is blog_list.html).

fields like new blog, updation and deletion are only be controlled by logged in user, thanks to
django predefined module (from django.contrib.auth.mixins import LoginRequiredMixin), mentioned
in views.py file of blog app.

for signup -> signup.html, seperate app (accounts.py) and also have content in its views.py and urls.py files.

-author privileges: (so that an author can make changes in only those blogs which are created by
them, means they can't make changes in the blogs made by other authors).

We will check if the author of the article is indeed the same user who is currently logged-in and trying to make a change. At the top of our articles/views.py
file add a line importing PermissionDenied. Then add a dispatch method for both
ArticleUpdateView and ArticleDeleteView.

- Rows and Columns adjustment for frontend

First you have to install django widget tweaks by using:

pip install django-widget-tweaks
