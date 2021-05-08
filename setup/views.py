from django.shortcuts import render
from .models import Stream

#importing forms here
from .forms import StreamForm

# Creating forms here.
def streamDetails(request):
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
