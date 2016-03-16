from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from time import timezone
# Create your views here.
from .models import Option, OPTION_TYPES, Score

def count_options():
    o = Option.objects.all()
    results = {}
    for selection in OPTION_TYPES:
        results.update({selection[0]: o.filter(option_type=selection[0]).count()})
    return results


def options_main(request, dimension=""):
    from django.shortcuts import render
    if not dimension:
        counts = count_options()
        print counts
        return render(request, "case/options.html", {"counts": counts})
    else:
        from .models import Option
        options = Option.objects.filter(option_type=dimension)

        return render(request, "case/options.html", {"options": options, "dimension": dimension})


def options_new(request, dimension=""):
    print "DEBUG DIMENSION", dimension
    from .forms import OptionForm
    if request.method == "POST":
        form = OptionForm(request.POST)
        if form.is_valid():
            option = form.save(commit=False)

            option.save()
    else:
        if dimension:
            form = OptionForm(initial={"option_type": dimension})
        else:
            form = OptionForm
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




def scoring(request, dimension):
    from django.shortcuts import render
    if not dimension:
        return render(request, "case/scores_main.html", {"": 1})
    else:
        from .models import Option
        scores = Scores.objects.filter(option_type=dimension)

        return render(request, "case/options.html", {"options": options, "dimension": dimension})
    #Render the just-clicked-on like-button.
    return  render_to_response("case/scoring_" + score_number+".html")



def wyswigeditor(request):
    return render (request, "case/wyswigeditor.html")

def index(request):
    return render_to_response('case/index.html')

def editor(request):
    return render(request, "case/editor.html")

def base(request):
    return render(request, "case/bootstrapbase.html")

def divtest(request):
    return render(request, "case/newbase.html")

