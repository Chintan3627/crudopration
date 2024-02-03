from django.shortcuts import render
from rest_framework.views import APIView
from .serilizer import postserilizer
from django.http import HttpResponse, JsonResponse
from .models import Post
class PostCrudView(APIView):

    def post(self,request):
        serlizer =  postserilizer
        serlizer_obj  = serlizer(data = request.data)
        if serlizer_obj.is_valid():
            serlizer_obj.save()
            return JsonResponse(serlizer_obj.data, status=201)
        return JsonResponse(serlizer_obj.errors, status=400)
    
    def get(self,request):
        data = Post.objects.all()
        serializer = postserilizer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def put(self,request,pk = None ):
        serlizer =  postserilizer
        serlizer_obj  = serlizer(data = request.data)
        if serlizer_obj.is_valid():
            instance =  Post.objects.get(id =pk)
            serlizer_obj.update(instance,serlizer_obj)
            return JsonResponse(serlizer_obj.data)
        return JsonResponse(serlizer_obj.errors, status=400)
    
    def delete(self,request,pk=None):
        Post.objects.delete(id = pk)
        return JsonResponse( status=200)
        
 
