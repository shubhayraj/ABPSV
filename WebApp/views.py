from django.shortcuts import render, get_object_or_404
from .models import Voter, GCand, BCand,Teacher
from .forms import Boy,Girl,Voters,VForm,TForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.
#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def gretrieve(request):
    clist=GCand.objects.all()
    return render(request,'MyApp/girl.html',{'clist':clist})

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def gshow(request,id=None):
    x=get_object_or_404(GCand,id=id)
    return render(request,'MyApp/gshow.html',{'x':x})

#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def gvote(request,id=None):
    y=get_object_or_404(GCand,id=id)
    if y:
        y.Gcount+=1
        y.save()
        a=request.session['AdNo']
        b=get_object_or_404(Voter,AdmisNo=a)
        if b:
            b.GCand=y.id
            b.save()
            if b.BCand==0:
                r=b.GCand==0
                return render(request,'MyApp/afterlogin.html',{'b':b})
            else:
                return render(request,'MyApp/bvoted.html')


def bretrieve(request):
    clist=BCand.objects.all()
    return render(request,'MyApp/boy.html',{'clist':clist})



def bvote(request,id=None):
    y=get_object_or_404(BCand,id=id)
    if y:
        a = request.session['AdNo']
        b = get_object_or_404(Voter, AdmisNo=a)
        if b.BCand != 0:
            y.Bcount += 1
            y.save()
            b.BCand = y.id
            b.save()
            if b.GCand == 0:
                return render(request, 'MyApp/afterlogin.html', {'b': b})
            else:
                return render(request, 'MyApp/bvoted.html')



def vlogin(request):
    if request.method == 'POST':
        if 'vot' in request.POST:
            initial = {'AdNo': request.session.get('AdNo', None)}
            form = VForm(request.POST)
            x = Voter.objects.all()
            temp=1
            if form.is_valid():
                for y in x:
                    print(form.cleaned_data['Dobv'])
                    if form.cleaned_data['AdNo'] == y.AdmisNo and form.cleaned_data[
                        'Dobv'] == y.Vdob and y.Votedone == False:
                        a = y.id
                        temp=0
                        b = get_object_or_404(Voter, id=a)
                        if b:
                            b.Votedone = True
                            b.save()
                        request.session['AdNo'] = form.cleaned_data['AdNo']
                        return render(request, 'MyApp/afterlogin.html', {'b': b})
                if (temp==1):
                    return render(request,'MyApp/invalid.html')

        elif 'adm' in request.POST:
            form=TForm(request.POST)
            x=Teacher.objects.all()
            if form.is_valid():
                for y in x:
                    print(form.cleaned_data['Tid'])
                    if form.cleaned_data['Tid']==y.Tid and form.cleaned_data['Tpass']==y.Tpass:
                        return render(request,'MyApp/adminprofile.html')

    return render(request,'MyApp/vlogin.html')


def afterlogin(request):
    return render(request,'MyApp/afterlogin.html')

@login_required()
def result(request):
    x=get_object_or_404(GCand,id=1)
    x1=GCand.objects.all()
    for x2 in x1:
        if x2.Gcount > x.Gcount:
            x=x2
    y=get_object_or_404(BCand,id=1)
    y1 = BCand.objects.all()
    for y2 in y1:
        if y2.Bcount > y.Bcount:
            y = y2
    return render(request,'MyApp/result.html',{'x':x,'y':y})



def admprof(request):
    return render(request,'MyApp/adminprofile.html')


def admboy(request):
    clist=BCand.objects.all()
    return render(request,'MyApp/admboy.html',{'clist':clist})
def orgcreate(request):
    form=Boy(request.POST or None,request.FILES or None)
    if form.is_valid():
        x=form.save()
        x.save()
        return HttpResponseRedirect('/')
    return render(request,'MyApp/bcreate.html',{'form':form})
def bret(request,id=None):
    x=get_object_or_404(BCand,id=id)
    return render(request,'MyApp/bretshow.html',{'x':x})
def bupdate(request,id=None):
    instance=get_object_or_404(BCand,id=id)
    form=Boy(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_burl())
    return render(request,'MyApp/bupdate.html',{'form':form})

def bdelete(request,id=None):
    instance=get_object_or_404(BCand,id=id)
    instance.delete()
    return render(request,'MyApp/bdelete.html')


def admgirl(request):
    clist=GCand.objects.all()
    return render(request,'MyApp/admgirl.html',{'clist':clist})
def gcreate(request):
    form=Girl(request.POST or None,request.FILES or None)
    if form.is_valid():
        x=form.save()
        x.save()
        return HttpResponseRedirect('/')
    return render(request,'MyApp/gcreate.html',{'form':form})
def gret(request,id=None):
    x=get_object_or_404(BCand,id=id)
    return render(request,'MyApp/gretrieve.html',{'x':x})
def gupdate(request,id=None):
    instance=get_object_or_404(GCand,id=id)
    form=Girl(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_url())
    return render(request,'MyApp/gupdate.html',{'form':form})

def gdelete(request,id=None):
    instance=get_object_or_404(GCand,id=id)
    instance.delete()
    return render(request,'MyApp/bdelete.html')


def admvoter(request):
    clist=Voter.objects.all()
    return render(request,'MyApp/admvoter.html',{'clist':clist})
def vcreate(request):
    form=Voters(request.POST or None,request.FILES or None)
    if form.is_valid():
        x=form.save()
        x.save()
        return HttpResponseRedirect('/')
    return render(request,'MyApp/vcreate.html',{'form':form})
def vret(request,id=None):
    x=get_object_or_404(BCand,id=id)
    return render(request,'MyApp/vretrieve.html',{'x':x})
def vupdate(request,id=None):
    instance=get_object_or_404(Voter, id=id)
    form=Voters(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_vurl())
    return render(request,'MyApp/vupdate.html',{'form':form})

def vdelete(request,id=None):
    instance=get_object_or_404(Voter,id=id)
    instance.delete()
    return render(request,'MyApp/bdelete.html')
