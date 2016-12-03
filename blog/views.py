from django.shortcuts import render

# Create your views here.
# The simplest view:
# -- blog/post_list.html is a template
def post_list(request):
    return render(request, 'blog/post_list.html', {})
