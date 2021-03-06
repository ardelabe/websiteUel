from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # test purposes path('program/<str:program_title>', views.program, name='program'), 
    path('historia', views.historia, name='historia'),
    path('corpos', views.corpos, name='corpos'),
    path('orgaos', views.orgaos, name='orgaos'),
    path('canais', views.canais, name='canais'),
    path('arte', views.arte, name='arte'),
    path('esportes', views.esportes, name='esportes'),
    path('vida', views.vida, name='vida'),
    path('graduacao', views.graduacao, name='graduacao'),
    path('gradpage/<str:grad_title>', views.gradpage, name='gradpage'),
    path('post', views.post, name='post'),
    path('pospage/<str:pos_title>', views.pospage, name='pospage'),
    path('mestrado', views.mestrado, name='mestrado'),
    path('maspage/<str:mas_title>', views.maspage, name='maspage'),
    path('doutorado', views.doutorado, name='doutorado'),
    path('docpage/<str:doc_title>', views.docpage, name='docpage'),
    path('pesquisa', views.pesquisa, name='pesquisa'),
    path('laboratorios', views.laboratorios, name='laboratorios'),
    path('extensao', views.extensao, name='extensao'),
    path('assessoria', views.assessoria, name='assessoria'),
    path('guia_estudante', views.guia_estudante, name='guia_estudante'),
    path('biblioteca', views.biblioteca, name='biblioteca'),
]
