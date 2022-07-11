from django.shortcuts import render,redirect,reverse

from .models import Community,Post,User
from .serializers import CommunitySerializer, PostSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import CommForm, RegisterForm, PostForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from actstream import action
from actstream.models import Action
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
import requests

def pricing(request):
    return render(request,'pricing.html')
    
class UserCreate(CreateView):
  
    # specify the model for create view
    model = User
    success_url='/'
  
    # specify the fields to be displayed
  
    fields = ['username','first_name','last_name','email','bio','image','password']

class CommDetailView(DetailView):
    # specify the model to use
    model = Community

def ajax_posting(request):
    if request.is_ajax():
        text = request.POST.get('text', None) # getting data from first_name input 
        grp = Community.objects.all()
        for i in grp:
           name = i.id
      # getting data from first_name input 
        member = request.user.id
        comm = name
        res = requests.post('http://localhost:8000/api/posts',{'text':text,'member':member,'community':name})
        if text and member: #cheking if first_name and last_name have value
            response = {
                         'msg':'Your form has been submitted successfully' # response message
            }
            return JsonResponse(response) # return response as JSON
    
def home_view(request):
    context ={}
    comm = Community.objects.all()
    # create object of form
    form = CommForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "index.html",{'form':form,'comm':comm})
    
class CommunityList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        comms = Community.objects.all()
        serializer = CommunitySerializer(comms, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class CommunityDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Community.objects.get(pk=pk)
        except Community.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comm = self.get_object(pk)
        serializer = CommunitySerializer(comm)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        comm = self.get_object(pk)
        serializer = CommunitySerializer(comm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comm = self.get_object(pk)
        comm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
class PostList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PostDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data,member=request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class ActionList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        acts = Action.objects.all()
        serializer = ActionSerializer(acts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ActionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ActionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Action.objects.get(pk=pk)
        except Action.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        act = self.get_object(pk)
        serializer = ActionSerializer(act)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        act = self.get_object(pk)
        serializer = ActionSerializer(act, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        act = self.get_object(pk)
        act.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
