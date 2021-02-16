from django.shortcuts import render
from .models import ImgClassifier
from .forms import ImgClassifierForm

def classification_detail(request, id):
    classifier_obj = ImgClassifier.objects.get(id=id)
    context = {'classifier_obj': classifier_obj}
    return render(request, 'classifier_detail.html',context)

def classification_list_view(request,id):
    classifier_qs = ImageClassifier.objects.all()
    context = {'classifier_object':classifier_qs}
    return render(request,'classifier_list.html',context)
 
def classifier_create_view(request):
    form = ImgClassifierForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, "classifier_create.html", context)
  
def classifier_update_view(request,id):
    classification_obj = ImgClassifier.objects.get(id=id)
    form = ImgClassifierForm(request.POST or None,request.FILES or None,instance=classification_obj)
    if form.is_valid() : 
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request,"classifier_update.html",context)
      
   
def classifier_delete_view(request,id):
    classifier_obj = ImgClassifier.objects.get(id=id)
    if request.methode == 'POST':
        classifier_obj.delete()
        return redirect('/')
    context = {'classifier_obj':classifier_obj}
    return render(request,'classifier_delete.html',context)