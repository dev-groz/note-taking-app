"""note_taking_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from notes.views import all_notes, get_note, create_note, remove_note, edit_note

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_notes),
    path('createnote/', create_note),
    path('removenote/<note_id>', remove_note),
    path('editnote/<note_id>', edit_note),
    path('note/<note_id>', get_note),
]
