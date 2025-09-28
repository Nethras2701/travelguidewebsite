from django.shortcuts import render,redirect,get_object_or_404
from .models import Destination,Photo
from .forms import DestinationForm,PhotoForm
from django.utils import timezone

# Create your views here.
def create_destination(request):
    if request.method == 'POST':
        form=DestinationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form=DestinationForm()
    return render(request,'create_destination.html',{'form':form})

def destination_list(request):
    data=Destination.objects.all()
    return render(request, 'destination_list.html',{'data':data})

def destread(request, did):
    dest_data = get_object_or_404(Destination, id=did)
    return render(request, 'destread.html', {'dest_data': dest_data})


def addactivity(request):
    if request.method == 'POST':
        form=PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form=PhotoForm()
    return render(request,'addactivity.html',{'form':form})

def allactivity(request):
    cid = request.GET.get('destination_id')
    data=Destination.objects.all()
    if cid:
        data1 = Photo.objects.filter(destination_id = cid)
    else:
        data1=Photo.objects.all()
    return render(request, 'allactivity.html',{'data':data, 'data1':data1})

def activityofeachdest(request, did):
    destination = Destination.objects.get(id=did)
    photos = Photo.objects.filter(destination=destination)
    return render(request, 'activityofeachdest.html', {'data1': photos, 'destination': destination})

def actread(request, aid):
    act_data = get_object_or_404(Photo, id=aid)
    return render(request, 'actread.html', {'act_data': act_data})

def actupdate(request,pid):
    data = get_object_or_404(Photo,id=pid)
    if request.method == 'POST':
        form=PhotoForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('activityofeachdest', did=data.destination.id)
    else:
        form=PhotoForm(instance=data)
    return render(request,'actupdate.html',{'form':form})

def actdelete(request,pid):
    data = get_object_or_404(Photo,id=pid)
    if request.method == 'POST':
        data.is_deleted=True
        data.deleted_at=timezone.now() #keeps record of deleted time
        data.save()
        return redirect('allactivity')
    return render(request,'actdelete.html',{'data':data})

def acthistory(request):
    data = Photo.objects.filter(is_deleted=True)
    return render(request,'acthistory.html',{'data':data})

def actrestore(request,pid):
    data = get_object_or_404(Photo, id=pid, is_deleted=True)
    if request.method=='POST':
        data.is_deleted = False
        data.deleted_at=None
        data.save()
        return redirect('acthistory')
    return render(request,'actrestore.html',{'data':data})

def actdeleteperm(request, pid):
    data = get_object_or_404(Photo, id=pid)
    if request.method == 'POST':
        data.delete()
        return redirect('allactivity')    
    return render(request, 'actdeleteperm.html', {'data': data})
