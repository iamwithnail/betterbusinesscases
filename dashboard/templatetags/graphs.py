from django import template
import pygal
register = template.Library()


@register.inclusion_tag('dashboard/__graphbase.html')
def capital_costs():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    #from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)
    import pygal
    line_chart = pygal.Bar(width=400, height=300, explicit_size=True)
    line_chart.title = 'Capital Costs by organisation'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Stirling Council', [3617,1517,0,0,0])
    line_chart.add('Scottish Governmnet',  [3145, 953, 0,0,0,])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return {"filename": this_function_name}


@register.inclusion_tag('dashboard/__graphbase.html')
def revenue():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    #from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)
    import pygal
    line_chart = pygal.Bar(width=400, height=300, explicit_size=True)
    line_chart.title = 'Revenue Map'
    line_chart.x_labels = map(str, range(2016, 2020))
    line_chart.add('Revenue', [1933201,1967032,2008346,2051528,2092559])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return {"filename": this_function_name}


@register.inclusion_tag('dashboard/__graphbase.html')
def funding_envelope():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    #from excelmanager import get_cell_range
    #capital_costs_data = get_cell_range(0, 1, 5, 3)
    import pygal
    line_chart = pygal.Bar(width=400, height=300, explicit_size=True)
    line_chart.title = 'Funding Envelope'
    line_chart.x_labels = ("Capital", "Contingency")
    line_chart.add('Capital', [10250])
    line_chart.add('Contingency', [2415])

    line_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return {"filename": this_function_name}


@register.inclusion_tag('dashboard/__graphbase.html')
def summary_spend():
    import sys
    this_function_name = sys._getframe().f_code.co_name
    pie_chart = pygal.Pie(width=400, height=300, explicit_size=True)
    pie_chart.title = 'Option 3 Cost Categories'
    pie_chart.add('Pool', [7.6, 13.2, 22.7, 19.8, 2.8, 16.5,3.0,7.2,7.2])
    pie_chart.add('Flumes', [4.5,39.8,8.9,11.8,6.2,9.8,10.4,4.3,4.3])
    pie_chart.add('Dry Side', [4.5,39.8,8.9,11.8,6.2,9.8,10.4,4.3,4.3])
    pie_chart.render()
    pie_chart.render_to_file('static/img/graphs/'+this_function_name+'.svg')
    return {"filename": this_function_name}