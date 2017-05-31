from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Function,platfromApiJson
import requests
from django.http.response import StreamingHttpResponse
from . import staic
import csv
from platformProtal import util
# Create your views here.

def index(request):
    function_list = Function.objects.all()
    return render(request,'index.html',{'function_list': function_list})

@csrf_exempt
def serach(request):
    ret = {}
    print(request.is_ajax())
    if request.is_ajax():
        print(request.POST['data'])
        fun = Function.objects.filter(id=request.POST['data']).first()
        para = request.POST['para']
        apijson = platfromApiJson(funcode=int(fun.funcode.code),database=fun.dataase.name,fun=fun.content,para=para,limit=fun.limit,output=fun.output)
        data = json.dumps(apijson.convert_to_dict())
        url = "{}/api?data={}".format(staic.platformApiURL,data)
        ret = requests.request('GET',url)
        if ret.status_code==requests.codes.ok:
            ret = json.loads(ret.text)
            print(ret)
        #softtype = request.GET.get('func')
        return HttpResponse(json.dumps(ret), content_type='application/json')

def download(request):
    fun = Function.objects.filter(id=request.GET['data']).first()
    para = request.GET['para']
    apijson = platfromApiJson(funcode=int(fun.funcode.code),database=fun.dataase.name,fun=fun.content,para=para,limit=fun.limit,output=fun.output)
    data = json.dumps(apijson.convert_to_dict())
    url = "{}/api?data={}".format(staic.platformApiURL,data)
    ret = requests.request('GET',url)
    if ret.status_code==requests.codes.ok:
        ret = json.loads(ret.text)
        title,datas = util.json_to_csv(json.loads(str(json.dumps(ret['data']))))
        #print(title)
        print(datas)
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename=my.csv'

        # Create the CSV writer using the HttpResponse as the "file."
        writer = csv.writer(response)
        writer.writerow(title)
        for data in datas:
            ro = []
            for ti in title:
                ro.append(data[ti])
            writer.writerow(ro)
        return response