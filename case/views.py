from django.shortcuts import render_to_response

# Create your views here.


def dimension(request, dimension_number):
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
    return  render_to_response("case/dimension_" + dimension_number+".html")

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
