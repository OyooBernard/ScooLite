from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, HttpResponse
from .models import Stream

#importing forms here
from .forms import StreamForm

# Creating forms here.
def addStream(request):
    context = {}
    #creating  object of form
    form = StreamForm(request.POST or None)

    if form.is_valid():
        form.save()
        streams = Stream.objects.all()
        return render(request, "stream_view.html", {'streams': streams})
    else:
        form = StreamForm()
        return render(request, 'stream.html', {'form': form, })

#View all streams
def viewStreams(request):
    streams = Stream.objects.all()
    return render(request, "stream_view.html", {'streams': streams})

#Stream edit form
def editStream(request, id = None):
    #post = get_object_or_404(Stream, id=id)
    post = Stream.objects.get(id=id)  
    if request.method == "POST":
        form = StreamForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect("/editstream/"+str(post.id))
            #return HttpResponse("Saved")
    else:
        form = StreamForm(instance=post)
        return render(request,'editstream.html',{'form':form, 'streams':post})
