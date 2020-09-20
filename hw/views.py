from django.shortcuts import render
from django.http import HttpResponse
from hw import models
from django.contrib import messages
import os


# Create your views here.
up = False
the_name = {}
def index(request):
    return render(request, 'index.html')
    
def student(request):
    ctx={}
    if request.method != "POST":
        return render(request, "index.html")
    else:
        web_name=request.POST.get("name")
        web_id_num=request.POST.get("idnum")
        name=models.Student.objects.filter(id_num=web_id_num).filter(name=web_name)
        if name.exists():
            global up
            global the_name
            the_name = web_name
            up = True
            ctx['req'] = "快交作业吧ww " + web_name + " 请提交rar,7z,zip三种格式的压缩包"
            return render(request, 'up.html', ctx)
        else:
            ctx['rlt'] = "姓名或学号错误!"
            return render(request, 'index.html', ctx)
            
def upload(request):
    ctx = {}
    file_type = ["zip", "ZIP", "7z", "7Z", "rar", "RAR"]
    if up is True:
        if request.method == 'POST':
            hw = request.FILES['file']
            hw_name = request.FILES['file'].name
            ext = hw_name.rsplit(".", 1)[1]
            if ext not in file_type:
                ctx['req'] = "只能提交rar,7z,zip三种格式的压缩包哦";
                return render(request, "up.html", ctx)
            else:
                path = 'static/homework/' + the_name + "." + ext
                if request.FILES['file'].size < 5120000:
                    with open(path, mode='wb') as f:
                        for content in hw.chunks():
                            f.write(content)
                            ctx['req'] = "提交完成！辛苦啦~";
                            return render(request, "up.html", ctx)
                else:
                    ctx['req'] = "你上传的文件超过5MB啦！";
                    return render(request, "up.html", ctx)
    else:
        return render(request, "index.html")