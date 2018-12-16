
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from .models import IncomeData, Gender, EducationLevel, IncomeLevel, SystemParameter, County, State
import json
from django.http import JsonResponse
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.plotly as py
import plotly.graph_objs as go
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd
import resource
import numpy as np
import time


# plotly.js test
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

# probably don't need'
from django.contrib.auth import get_user_model

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/chartjs.html', {"customers":10})

def get_data_chartjs(request, *args, **kwargs):
    data = {
        "sales":100,
        "customers":10,
    }
    return JsonResponse(data)

def chartjs(request):
    labels = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]

    return render(request, 'charts/chartjs.html', {})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 234, 122, 432, 235, 134]
        data = {
            'labels': labels,
            'default': 10,
        }
        usernames = [user.username for user in User.objects.all()]

        # items = IncomeData.objects.filter(year=2015)
        # years = {income_datum.year for income_datum in IncomeData.objects.all()}
        # years = list(years)
        # years.sort(reverse=True)
        # print(years)
        # return render(request, 'api/', {'items': items,
        #                                                   'years': years,
        #                                                   'states': State.objects.all(),
        #                                                   'income_levels': IncomeLevel.objects.all(),
        #                                                   'education_levels': EducationLevel.objects.all(),
        #                                                   'genders': Gender.objects.all()})
        return Response(data)

# end plotly.js test

# create chart counter to not allow more than 25 graphs to be made (Plotly's max for a free account)
def get_chart_counter():
    chart_counter = SystemParameter.objects.get(name='Chart Counter')
    counter = int(chart_counter.value)
    counter += 1
    if counter >= 10:
        counter = 0
    chart_counter.value = str(counter)
    chart_counter.save()
    return counter


def index(request):
    return render(request, 'charts/index.html', {})


def about(request):
    return render(request, 'charts/about.html', {})

def morecharts(request):
    items = IncomeData.objects.filter(year=2015)
    years = {income_datum.year for income_datum in IncomeData.objects.all()}
    years = list(years)
    years.sort(reverse=True)
    print(years)
    return render(request, 'charts/morecharts.html', {'items': items,
                                                  'years': years,
                                                  'states': State.objects.all(),
                                                  'income_levels': IncomeLevel.objects.all(),
                                                  'education_levels': EducationLevel.objects.all(),
                                                  'genders': Gender.objects.all()})


def graphs(request):
    # items = IncomeData.objects.filter(year='2015', gender=Gender.objects.get(pk=2), education_level=EducationLevel.objects.get(pk=1))
    items = IncomeData.objects.filter(year=2015)
    years = {income_datum.year for income_datum in IncomeData.objects.all()}
    years = list(years)
    years.sort(reverse=True)
    print(years)

    return render(request, 'charts/graphs.html', {'items': items,
                                                  'years': years,
                                                  'states': State.objects.all(),
                                                  'income_levels': IncomeLevel.objects.all(),
                                                  'education_levels': EducationLevel.objects.all(),
                                                  'genders': Gender.objects.all()})


def get_data(request):
    gender_id = request.GET.get('gender_id', '')
    education_level_id = request.GET.get('education_level_id', '')
    income_level_id = request.GET.get('income_level_id', '')
    year = request.GET.get('year', '')
    state_id = request.GET.get('state_id', '')

    items = IncomeData.objects.all()
    if gender_id != '':
        items = items.filter(gender_id=gender_id)
    if year != '':
        items = items.filter(year=year)
    if income_level_id != '':
        items = items.filter(income_level_id=income_level_id)
    if education_level_id != '':
        items = items.filter(education_level_id=education_level_id)

    if state_id != '':
        items = items.filter(county_state_id=state_id)

    # if state_id != '':
    #     items2 = []
    #     for item in items:
    #         if item.county.state_id == state_id:
    #             items2.append(item)
    #     items = items2

    data = []
    for item in items:
         data.append(item.to_dictionary())
    return JsonResponse({'data': data})


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get_data(request):
        gender_id = request.GET.get('gender_id', '')
        education_level_id = request.GET.get('education_level_id', '')
        income_level_id = request.GET.get('income_level_id', '')
        year = request.GET.get('year', '')
        state_id = request.GET.get('state_id', '')

        items = IncomeData.objects.all()
        if gender_id != '':
            items = items.filter(gender_id=gender_id)
        if year != '':
            items = items.filter(year=year)
        if income_level_id != '':
            items = items.filter(income_level_id=income_level_id)
        if education_level_id != '':
            items = items.filter(education_level_id=education_level_id)

        if state_id != '':
            items = items.filter(county_state_id=state_id)

        data = []
        for item in items:
            data.append(item.to_dictionary())
        return JsonResponse({'data': data})

# testing this
def graphs_line(request):
    # items = IncomeData.objects.filter(year='2015', gender=Gender.objects.get(pk=2), education_level=EducationLevel.objects.get(pk=1))
    items = IncomeData.objects.filter(year=2015)
    years = {income_datum.year for income_datum in IncomeData.objects.all()}
    years = list(years)
    years.sort(reverse=True)
    print(years)

    return render(request, 'charts/chartjsCopy.html', {'items': items,
                                                  'years': years,
                                                  'states': State.objects.all(),
                                                  'income_levels': IncomeLevel.objects.all(),
                                                  'education_levels': EducationLevel.objects.all(),
                                                  'genders': Gender.objects.all()})

# testing this too
def get_plotly_line_url(request):
    gender_id = request.GET.get('gender_id', '')
    education_level_id = request.GET.get('education_level_id', '')
    income_level_id = request.GET.get('income_level_id', '')
    year = request.GET.get('year', '')
    state_id = request.GET.get('state_id', '')

    items = IncomeData.objects.all()
    if gender_id != '':
        items = items.filter(gender_id=gender_id)
    if year != '':
        items = items.filter(year=year)
    if income_level_id != '':
        items = items.filter(income_level_id=income_level_id)
    if education_level_id != '':
        items = items.filter(education_level_id=education_level_id)

# not rendering the proper data
    if state_id != '':
        items = items.filter(county_id=state_id)

    # if state_id != '':
    #     items2 = []
    #     for item in items:
    #         if item.county.state_id == state_id:
    #             items2.append(item)
    #     items = items2

    counter = 0
    output = {}
    for item in items:
        if item.county.state.abbr == '':
            continue

        if item.county.state.abbr in output:
            output[item.county.state.abbr] += item.population
        else:
            output[item.county.state.abbr] = item.population

        if counter % 10 == 0:
            print(f'{round(counter/len(items)*100,2)}%')
        counter += 1

    abbr = list(output.keys())
    values = list(output.values())

    # add states to the output that aren't associated with any income data
    for state in State.objects.all():
        if state.abbr != '' and state.abbr not in abbr:
            abbr.append(state.abbr)
            values.append(0)


    # Create a trace
    trace = go.Scatter(
        x=[year],
        # y=[gender_id] //gender 0=female, 1=male
        # national numbers, takes into account education, gender and income level- missing-state
        y=[item.population]
        # y=[IncomeData.objects.all()] // doesn't work'

    )

    data = [trace]

    url = py.plot(data, filename='basic-line', auto_open=False)

    # url = py.plot(fig, filename='choropleth_full_usa' + str(get_chart_counter()), auto_open=False)
    # print(url)

    return HttpResponse(url)


def get_plotly_state_url(request):

    gender_id = request.GET.get('gender_id', '')
    education_level_id = request.GET.get('education_level_id', '')
    income_level_id = request.GET.get('income_level_id', '')
    year = request.GET.get('year', '')

    items = IncomeData.objects.all()
    if gender_id != '':
        items = items.filter(gender_id=gender_id)
    if year != '':
        items = items.filter(year=year)
    if income_level_id != '':
        items = items.filter(income_level_id=income_level_id)
    if education_level_id != '':
        items = items.filter(education_level_id=education_level_id)

    counter = 0
    output = {}
    for item in items:
        if item.county.state.abbr == '':
            continue

        if item.county.state.abbr in output:
            output[item.county.state.abbr] += item.population
        else:
            output[item.county.state.abbr] = item.population

        if counter % 10 == 0:
            print(f'{round(counter/len(items)*100,2)}%')
        counter += 1

    abbr = list(output.keys())
    values = list(output.values())

    # add states to the output that aren't associated with any income data
    for state in State.objects.all():
        if state.abbr != '' and state.abbr not in abbr:
            abbr.append(state.abbr)
            values.append(0)

    scl = [[0.0, 'rgb(245, 245, 245)'], [0.2, 'rgb(224,193,209)'], [0.4, 'rgb(183,112,147)'], \
           [0.6, 'rgb(153,51,102)'], [0.8, 'rgb(107,35,71)'], [1.0, 'rgb(45,15,30)']]

    # creates title for chart
    if gender_id == '' and education_level_id == '' and income_level_id == '' and year == '':
        chart_title = 'All Genders, Education and Income Levels, All Years'
    else:
        if gender_id == '':
            chart_title = 'All Genders' + '<br>'
        else:
            chart_title = Gender.objects.get(pk=gender_id).name + '<br>'

        if education_level_id == '':
            chart_title += 'All Education Levels ' + '<br>'
        else:
            chart_title += EducationLevel.objects.get(pk=education_level_id).name + '<br>'
        if income_level_id =='':
            chart_title += "All Income Levels " + '<br>'
        else:
            chart_title += IncomeLevel.objects.get(pk=income_level_id).name + '<br>'
        if year == '':
            chart_title += ' All Years '
        else:
            chart_title += year

    # sets up state map frame
    data = [dict(
        type='choropleth',
        colorscale=scl,
        autocolorscale=False,
        locations=abbr[-52:-1],
        z=values,
        locationmode='USA-states',
        text=['gender_id'],
        marker=dict(
            line=dict(
                color='rgb(255,255,255)',
                width=2
            )),
        colorbar=dict(
            title=chart_title)
    )]

    layout = dict(
        title='US Education and Poverty Info by State<br>(Hover for breakdown)',
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)'),
    )

    fig = dict(data=data, layout=layout)

    url = py.plot(fig, filename='d3-choropleth-map' + str(get_chart_counter()), auto_open=False)
    print(url)
    return HttpResponse(url)


def get_plotly_url(request):
    gender_id = request.GET.get('gender_id', '')
    education_level_id = request.GET.get('education_level_id', '')
    income_level_id = request.GET.get('income_level_id', '')
    year = request.GET.get('year', '')

    items = IncomeData.objects.all()
    if gender_id != '':
        items = items.filter(gender_id=gender_id)
    if year != '':
        items = items.filter(year=year)
    if income_level_id != '':
        items = items.filter(income_level_id=income_level_id)
    if education_level_id != '':
        items = items.filter(education_level_id=education_level_id)


    counter = 0
    output = {}
    for item in items:
        if item.county.fips == '':
            continue

        if item.county.fips in output:
            output[item.county.fips] += item.population
        else:
            output[item.county.fips] = item.population

        if counter % 10 == 0:
            print(f'{round(counter/len(items)*100,2)}%')
        counter += 1

    fips = list(output.keys())
    values = list(output.values())

    for county in County.objects.all():
        if county.fips != '' and county.fips not in fips:
            fips.append(county.fips)
            values.append(0)

    #this makes the graph look nice but it gives weird figures
    # top_populations = list(sorted(values, reverse=True))[:20]
    # max_value = sum(top_populations) / len(top_populations) / 10

    colorscale = ["#F5F5F5", "#f4eaef", "#ead6e0", "#e0c1d1", "#d6adc1", "#cc99b2", "#c184a3", "#b77093", "#ad5b84", "#a34775", "#993366",
                  "#892d5b", "#7a2851", "#6b2347", "#5b1e3d", "#4c1933", "#2d0f1e", "#0f050a"]

    if gender_id == '' and education_level_id == '' and income_level_id == '' and year == '':
        chart_title = 'All Genders, Education and Income Levels, All Years'
    else:
        if gender_id == '':
            chart_title = 'All Genders, '
        else:
            chart_title = Gender.objects.get(pk=gender_id).name + ', '
        if income_level_id =='':
            chart_title += "All Income Levels, "
        else:
            chart_title += IncomeLevel.objects.get(pk=income_level_id).name
        if education_level_id == '':
            chart_title += 'All Education Levels, '
        else:
            chart_title += EducationLevel.objects.get(pk=education_level_id).name + ', '
        if year == '':
            chart_title += 'All Years, '
        else:
            chart_title += year

    # endpoints colors
    # endpts = list(np.linspace(0, max_value, len(colorscale) - 1))
    average_population = ()
    # average_population = 100

    average_population = sum(item.population for item in items) / len(items)
    if len(items) < average_population:
        endpts = [50, 100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 7500, 10000, 50000, 100000]
    else:
        endpts = [1000, 25000, 35000, 40000, 50000, 75000, 125000, 150000, 200000, 300000, 500000, 1000000, 2000000, 5000000]


    fig = ff.create_choropleth(
        fips=fips, values=values, scope=['usa'],
        binning_endpoints=endpts, colorscale=colorscale,
        show_state_data=False,
        show_hover=True, centroid_marker={'opacity': 0},
        asp=2.9, title=chart_title,
        legend_title='Number of People',
        county_outline={'color': 'rgb(255,255,255)', 'width': 0.5}, round_legend_values=True,
    )

    url = py.plot(fig, filename='choropleth_full_usa' + str(get_chart_counter()), auto_open=False)
    print(url)

    return HttpResponse(url)




