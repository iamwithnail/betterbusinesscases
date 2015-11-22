from django.shortcuts import render_to_response

# Create your views here.


def dimension(request, dimension):
    from django.shortcuts import get_object_or_404, render
    from django.http import HttpResponseRedirect, HttpResponse
    from django.core.urlresolvers import reverse

    from .models import Option
    def submit_option(request, dimension):
        option = get_object_or_404(Option, option_type=dimension)
        try:
            selected_option = option.option_set.get(option_type=request.POST['dimension'],
                                                    strength=request.POST['strength'],
                                                    text=request.POST['text']
                                                    )
        except (KeyError, Option.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'case/options.html', {
                'dimension': dimension,
                'error_message': "You didn't enter any text.",
            })
        else:
            option = Option.objects.create(option_type=request.POST['dimension'],
                                           strength=request.POST['strength'],
                                           text=request.POST['text']
                                           )
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse(option, args=(option.option_type,)))

    return render_to_response("case/options.html", dimension)

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
