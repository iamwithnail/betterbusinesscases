from django import template

register = template.Library()

@register.inclusion_tag('dashboard/__graphbase.html')
def capital_costs():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    #from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)
    import pygal
    line_chart = pygal.Bar(width=500, height=500, explicit_size=True)
    line_chart.title = 'Capital Costs by organisation'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Powys CC', [3617,1517,0,0,0])
    line_chart.add('Welsh Gment',  [3145, 953, 0,0,0,])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return {"filename": this_function_name}

@register.inclusion_tag('dashboard/__graphbase.html')
def revenue():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    #from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)
    import pygal
    line_chart = pygal.Bar(width=500, height=500, explicit_size=True)
    line_chart.title = 'Revenue Map'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Revenue', [1933201,1967032,2008346,2051528,2092559])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return {"filename": this_function_name}