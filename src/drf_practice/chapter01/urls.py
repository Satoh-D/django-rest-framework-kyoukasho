from django.urls import path

import .views as api_views

urlpatterns = [
    # 本モデルの取得（一覧）・登録
    path('api/books/', api_views.BookListCreateAPIView.as_view()),
    # 本モデルの取得（詳細）・更新・一部更新・削除
    path('api/books/<pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view()),
]

