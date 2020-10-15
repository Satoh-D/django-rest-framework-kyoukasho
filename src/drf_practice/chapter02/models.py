import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Publisher(models.Model):
    """出版社モデル"""

    class Meta:
        db_table = 'chapter02_publisher'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='出版社名', max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

class Author(models.Model):
    """著者モデル"""

    class Meta:
        db_table = 'chapter02_author'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='著者名', max_length=20)
    created_at = models.DateTimeField(default=timezone.now)

class Book(models.Model):
    """本モデル"""

    # メタデータオプションを定義
    # via. https://djangoproject.jp/doc/ja/1.0/ref/models/options.html
    class Meta:
        # モデルの使うデータベーステーブルの名前を定義
        # 基本はクラス名から暗黙で推測を行ってくれるが、オーバーライドしたい場合に使う
        db_table = 'chapter02_book'
        # オブジェクトのリストを取得するときの並び順を定義
        ordering = ['created_at']
        # verbose_name: 人間可読なオブジェクト名の単数形
        # verbose_name_plural: 人間可読なオブジェクト名の複数形
        # これらを使うことで管理画面での表示内容（モデルの名前）が変わる
        # via. https://codor.co.jp/django/how-to-use-verbose-name
        verbose_name = verbose_name_plural = '本'

    # primary_keyを指定することで該当フィールドが主キーとなる
    # primary_keyを指定しない場合はid(AutoIncrement)のフィールドが暗黙的に追加される
    # RESTfulなAPIではリソースを特定する識別子がURLの一分となるため、推測されにくいUUID形式にするのがベストプラクティス
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=20, unique=True)
    price = models.IntegerField(verbose_name='価格', null=True)
    # 出版社.idの外部キー
    # publisher_id: 関連するPublisherの主キーを参照
    # publisher: 関連するPublisher自体を参照
    # book_set: Publisherから関連するBookを参照
    publisher = models.ForeignKey(Publisher,  verbose_name='出版社', on_delete=models.SET_NULL, null=True)
    # 著者と本を多対多でリレーションする
    # authors: 関連するAuthorを参照
    # book_set: Authorから関連するBookを参照
    authors = models.ManyToManyField(Author, verbose_name='著者', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class BookStock(models.Model):
    """本の在庫モデル"""

    class Meta:
        db_table = 'chapter02_book_stock'

    # book_id: 関連するBookの主キーを参照
    # book: 関連するBook自体を参照
    # bookstock: Bookから関連するBookStockを参照
    book = models.OneToOneField(Book, verbose_name='本', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='在庫数', default=0)