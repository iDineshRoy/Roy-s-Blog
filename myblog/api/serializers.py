from django.http import request
from django.template.defaultfilters import slugify
from rest_framework import serializers
from unidecode import unidecode
from api.models import Post
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.fields import CurrentUserDefault


class PostSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='id', write_only=True)

    class Meta:
        model = Post
        # author = context['request'].user
        fields = ['title', 'text', 'tags', 'status', 'featured']
        # fields = '__all__'

    def save(self):
        author = CurrentUserDefault
        # slug =slugify(unidecode(self.validated_data['title']))

    def validate_author(self, value):
        return self.context['request'].user