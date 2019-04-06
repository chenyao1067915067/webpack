from django.shortcuts import render,get_object_or_404, render_to_response
# from django.http import HttpResponse
from rest_framework import status

from .models import Blog

# from Blog.forms import CommentForm
# from .forms import CommentForm
# Create your views here.

def index(request):
    blog = Blog.objects.all()
    # blog = get_object_or_404(Blog,pk=1)
    return render(request,'blog/index.html',{'blogs':blog})

def detail(request,id):
    blog = Blog.objects.get(pk=id)
    return render(request,'blog/detail.html',{'blog':blog})

from django.views.generic.base import TemplateView

class HelloView(TemplateView):
    __template_name = 'blog/detail.html'

    # def dispatch(self, request, *args, **kwargs):

    # def get(self, request, *args, **kwargs):

    def get_context_data(self, **kwargs):
        kwargs['hello'] = 'hello world'
        kwargs['world'] = 'gouzi'
        kwargs['ul'] = ['a','b', 'c']
        return super(HelloView,self).get_context_data(**kwargs)
#     *args

    # def post(self, request, *args, **kwargs):



# from rest_framework.views import APIView
# class TestApiView(APIView)

from rest_framework.views import APIView
from django.http import JsonResponse
from blog.serializers import BlogSerializer
from rest_framework.response import Response


class GetMessageView(APIView):
    def get(self,request, *args, **kwargs):
        # get = request.GET
        blogs = Blog.objects.all()
        blog_list = BlogSerializer(blogs, many=True).data
        res = {
            'status':1,
            'detail':blog_list
        }
        return Response(res)
    def post(self,request,*args,**kwargs):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
