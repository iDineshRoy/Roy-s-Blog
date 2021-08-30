from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_exempt
from django.template.defaultfilters import slugify
from unidecode import unidecode
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def my_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        # return JsonResponse(serializer.data, safe=False)
        result_list = list(posts.values('title', 'text', 'tags', 'status', 'featured', 'author'))
        return HttpResponse(json.dumps(result_list))
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return None