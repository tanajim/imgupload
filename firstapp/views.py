from django.shortcuts import render
from .forms import Imgforms
from .models import Imguploading
# Create your views here.
def home_pg(request):
    # userimg = Imguploading.objects.all()
    # if request.method == 'POST':
    # userimg = Imgforms(data=request.POST,files=request.FILES)
    # print(userimg)
    # if userimg.is_valid():
    #     userimg.save()
    #     inst = userimg.instance
    #     print('in if statements')
    #     # return render(request,'homepg.html',{'objall':inst})
    # # else:
    #     formall = Imgforms()
    #     modelall = Imguploading.objects.all()
    #     contents = {'formall':formall,'modelall':modelall}
    #     return render(request,'homepg.html',contents)
    # else:
    # print('in else statements')
    formall = Imgforms()
    modelall = Imguploading.objects.all()
    contents = {'formall':formall,'modelall':modelall}
    return render(request,'homepg.html',contents)