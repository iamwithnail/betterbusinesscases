from django.shortcuts import render_to_response, render, redirect, get_object_or_404
import pygal
def benefitsgraph(request):
    return render(request, 'dashboard/benefitsgraph.html',)

def get_function_name():
    import traceback
    return traceback.extract_stack(None, 2)[0][2]

def main(request):
    return render(request, 'dashboard/main.html')

def summarygraph(request):
    return render(request, 'dashboard/summarygraph.html',)

def capital_costs(request):
    import sys
    this_function_name = sys._getframe().f_code.co_name
    from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)

    line_chart = pygal.Bar(width=500, height=500, explicit_size=True)
    line_chart.title = 'Capital Costs by organisation'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Powys CC', [3617,1517,0,0,0])
    line_chart.add('Welsh Gment',  [3145, 953, 0,0,0,])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return render(request, 'dashboard/graphbase.html', {"filename": this_function_name})

def revenue(request):
    import sys
    this_function_name = sys._getframe().f_code.co_name
    from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)
    import pygal
    line_chart = pygal.Bar(width=500, height=500, explicit_size=True)
    line_chart.title = 'Revenue Map'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Revenue', [1933201,1967032,2008346,2051528,2092559])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return render(request, 'dashboard/graphbase.html', {"filename": this_function_name})


"""

Pickup J 5:50
Get ready 5:30
Shower 5:15
Run Home 4:30
Buy Moneyz 4:15
Train to LBG 15:53
Get Ready 15:30
"""