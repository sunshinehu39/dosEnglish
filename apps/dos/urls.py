# APP专用url配置
from django.urls import path,re_path,include
from .views import *
from django.views.generic import TemplateView

# 使用drf
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'goal',GoalListViewSet)
router.register(r'jhdiary',DiaryViewSet)
router.register(r'share',shareViewSet)
router.register(r'img',imgViewSet)

urlpatterns = [
    path('', dosView, name='dos'),  # DOS大学
    path('dosvip', dosvipView, name='dosvip'),  # DOS校友福利
    path('diary', DiaryView, name='Diary'),  # 日记
    path('addDiary', addDiaryView, name='addDiary'),  # 增加日记
    path('dossearch', dossearchView, name='dossearch'),  # DOS搜索引擎
    path('dosjh_detail', dosjh_detailView, name='dosjh_detail'),  # DOS江湖详情
    path('dialogue', dialogueView, name='dialogue'),  # 英语对话
    path('speech', speechView, name='speech'),  # 演讲
    path('poem', poemView, name='poem'),  # 吟诵
    path('qps', QPSView, name='qps'),  # 奇葩说
    path('book', bookView, name='book'),  # 好书
    path('signin', signinView, name='signin'),  # 签到
    path('alist', alistView, name='alist'),  # 活动列表
    path('uploadimg', uploadimg, name='uploadimg'),  # 图片上传
    path('it', ITnoteView, name='it'),  # 编程笔记

    re_path(r'api', include(router.urls)), # 使用drf

]
