from rest_framework import serializers

from shop.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book                        # シリアライザで利用するモデルを指定
        fields = ['id', 'title', 'price']   # シリアライザで利用するカラムを指定