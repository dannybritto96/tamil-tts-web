from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
from django.conf import settings
from django.utils.encoding import smart_str
import requests
import mimetypes
import os
import time
import datetime


# Create your views here.
def index(request):
    if request.method == 'POST':
        file_name = None
        filename = None
        ip = request.POST.get('ttsInput')
        if ip == 'file':
            myFile = request.FILES['fileInput']
            fs = FileSystemStorage()
            filename = fs.save(myFile.name,myFile)
        elif ip == 'text':
            ttsText = request.POST.get('ttsText')
            ts = time.time()
            st = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
            filename = 'temp'+st+'.txt'
            f = open("media/"+filename,'a+')
            f.write(ttsText)
            f.close()
        file_name = filename.split('.')[0]
        file_name = file_name+'.mp3'
        files = {'fileInput':open("media/"+filename,'rb')}
        url = 'http://127.0.0.1:5000/tts'
        r = requests.post(url, files=files)
        return render(request,'tts_app/index.html',{'file_name':file_name})
    return render(request,'tts_app/index.html')

def download(request,file_name):
    file_path = settings.MEDIA_ROOT+'/'+file_name
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper,content_type=file_mimetype)
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    return response

@csrf_exempt
def getMp3(request):
    if request.method =='POST' and request.FILES['ttsAudio']:
        ttsAudio = request.FILES['ttsAudio']
        fs = FileSystemStorage()
        filename = fs.save(ttsAudio.name,ttsAudio)
        return HttpResponse("Success")
    return render(request,'tts_app/getMp3.html')
