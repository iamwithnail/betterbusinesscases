from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from time import timezone
# Create your views here.


def options_main(request, dimension=""):
    from django.shortcuts import render
    if not dimension:
        return render(request, "case/options.html")
    else:
        from .models import Option
        options = Option.objects.filter(option_type=dimension)
        return render(request, "case/options.html", {"options": options, "dimension": dimension})


def options_new(request, dimension=""):
    print "DEBUG DIMENSION", dimension
    from .forms import OptionForm
    if request.method == "POST":
        form = OptionForm(request.POST)
        option = form.save()
        if form.is_valid():
            option = form.save(commit=False)

            option.save()
    else:
        if dimension:
            form = OptionForm(initial={"option_type": dimension})
            print "WITH DIMENSION"
        else:
            form = OptionForm
            print "WITHOUT"
    return render(request, 'case/option_edit.html', {'form': form,  "option": dimension})


def options_edit(request, pk):
    from .forms import OptionForm
    from .models import Option
    option = get_object_or_404(Option, pk=pk)
    if request.method == "POST":
        form = OptionForm(request.POST, instance=option)
        if form.is_valid():
            option = form.save(commit=False)
            option.save()
            print option.pk
            return redirect('case:options_detail', pk=option.pk)
    else:
        form = OptionForm(instance=option)
    return render(request, 'case/option_edit.html', {'form': form})


def options_detail(request, pk):
    from .models import Option
    option = get_object_or_404(Option, pk=pk)
    return render(request, 'case/option_detail.html', {'option': option})


def graphtest(request):
    return render(request, 'case/highcharts.html',)


def scoring(request, score_number):
    """Toggle "like" for a single color, then refresh the color-list page."""
    """color = None
    try:
        #There's only one object with this id, but this returns a list
        #of length one. Get the first (index 0)
        color = Color.objects.filter(id=color_id)[0]
    except Color.DoesNotExist as e:
        raise  ValueError("Unknown color.id=" + str(color_id) + ". Original error: " + str(e))

    print("pre-toggle:  color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")

    color.is_favorited = not color.is_favorited
    color.save()  #Commit the change to the database

    print("post-toggle: color_id=" + str(color_id) + ", color.is_favorited=" + str(color.is_favorited) + "")
    """
    #Render the just-clicked-on like-button.
    return  render_to_response("case/scoring_" + score_number+".html")


def index(request):
    return render_to_response('case/index.html')
