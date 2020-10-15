import random

from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framwork.validators import UniqueTogetherValidator
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    """本モデル用のシリアライザ"""

    class Meta:
        # 対象のモデルクラスを指定
        model = Book
        # 利用するモデルのフィールドを fields = [] で指定
        # 使用しないフィールドは exclude = [] で指定する
        exlcude = ['created_at']
        # P.54: 3. Metaクラスのvalidatorsに追加
        validators = [
            # タイトルと価格でユニークになっていることを検証
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=('title', 'price'),
                message='タイトルと価格でユニークになっていなければなりません。'
            )
        ]
        extra_kwargs = {
            'title': {
                'validators': [
                    RegexValidator(r'^D.+$', message='タイトルは「D」で始めてください'),
                ]
            }
        }
    
    def validate_title(self, value):
        """タイトルに対するバリデーションメソッド"""

        if 'Java' in value:
            raise serializers.ValidationError('タイトルには「Java」を含めないでください。')
        
        return value
    
    def validate(self, data):
        """複数フィールド間のバリデーション"""

        title = data.get('title')
        price = data.get('price')
        if title and '薄い本' in title and price and price > 3000:
            raise serializers.ValidationError('薄い本は3,000円を超えてはいけません。')

        return data


class BookListSerializer(serializers.ListSerializer):
    """複数の本モデルを扱うためのシリアライザ"""

    # 対象のシリアライザを指定
    child = BookSerializer()


class FortuneSerializer(serializers.Serializer):
    """今日の運勢を返すためのシリアライザ""""

    birth_date = serializers.DateField()
    blood_type = serializers.ChoiceField(choices=['A', 'B', 'O', 'AB'])
    # 出力時に get_current_date() が呼ばれる
    current_date = serializers.SerializerMethodField()
    # 出力時に get_focune() が呼ばれる

    def get_current_date(self, obj):
        return timezone.localdate()
    
    def get_fortune(self, obj):
        seed = '{}{}{}'.format(
            timezone.localdate(), obj['birth_date'], obj['blood_type']
        )
        random.seed(seed)
        return random.choice(
            ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆', '★★★★☆', '★★★★★']
        )
    
