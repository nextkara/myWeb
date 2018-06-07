from django.shortcuts import render
from .models import menu
# Create your views here.
def testWeb(Request):
    listOfMenu = []
    listMenu = menu.objects.all()
    for x in listMenu:
        listOfMenu.append({'menu_link':x.menuLink, 'menu_img':x.menuImg, 'menu_name':x.menuName})
    return render(Request, 'monitor.html', {'info_dict': listOfMenu, 'path_request': 'monitor', 'name':'控制台'})


def testHelp(Request):
    listOfMenu = []
    listMenu = menu.objects.all()
    for x in listMenu:
        listOfMenu.append({'menu_link': x.menuLink, 'menu_img': x.menuImg, 'menu_name': x.menuName})
    return render(Request, 'help.html', {'info_dict': listOfMenu, 'path_request': 'monitor', 'name':'关于我们'})

def testWorklist(Request):
    listOfMenu = []
    listMenu = menu.objects.all()
    for x in listMenu:
        listOfMenu.append({'menu_link': x.menuLink, 'menu_img': x.menuImg, 'menu_name': x.menuName})
    return render(Request, 'worklist.html', {'info_dict': listOfMenu, 'path_request': 'monitor', 'name':'作业系统'})

def testUpload(Request):
    listOfMenu = []
    listMenu = menu.objects.all()
    for x in listMenu:
        listOfMenu.append({'menu_link': x.menuLink, 'menu_img': x.menuImg, 'menu_name': x.menuName})
    return render(Request, 'upload.html', {'info_dict': listOfMenu, 'path_request': 'monitor', 'name':'文件上传'})

def testDownload(Request):
    listOfMenu = []
    listMenu = menu.objects.all()
    for x in listMenu:
        listOfMenu.append({'menu_link': x.menuLink, 'menu_img': x.menuImg, 'menu_name': x.menuName})
    return render(Request, 'download.html', {'info_dict': listOfMenu, 'path_request': 'monitor', 'name':'文件下载'})