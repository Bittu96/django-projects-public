import io
import csv
from django.shortcuts import render
from django.contrib import messages
# from .forms import ThingForm, ItemForm
from .models import Thing, Item
from . import validators


def record_form(request):
    template = "records/record_form.html"
    context = {
        'thing_data': [],
        'item_data': [],
    }
    data_errors = dict()

    if request.method == "POST":
        tsv_file = request.FILES['tsv_file']
        if tsv_file.name.endswith('.tsv'):
            delimiter = '\t'
        elif tsv_file.name.endswith('.csv'):
            delimiter = ','
        else:
            messages.warning(
                request, 'Invalid file! please upload .csv or .tsv files only')
            return render(request, template, context)

        data_set = tsv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        messages.success(
            request, f"uploaded {tsv_file} successfully!")

        for column in csv.reader(io_string, delimiter=delimiter):
            if len(column) == 8: pass
            else:
                data_errors['file error'] = 'Terminated due to improper data formatting'
                break

            to_thing_data = {
                'code': column[0],
                'description': column[1],
                'date': column[2],
                'stat_one': column[3],
                'stat_two': column[4],
            }

            to_thing_data, data_errors = validators.validate_and_clean(
                'thing', to_thing_data)
            if to_thing_data['date'] == False:
                continue

            UNIQUE_CODE = column[0]
            try:
                thing_obj = Thing.objects.get(code=UNIQUE_CODE)
                for attr, value in to_thing_data.items():
                    setattr(thing_obj, attr, value)
                    thing_obj.save()
                if thing_obj in context['thing_data']:
                    context['thing_data'][context['thing_data'].index(
                        thing_obj)] = thing_obj
                else:
                    context['thing_data'].append(thing_obj)

            except Thing.DoesNotExist:
                thing_obj = Thing(**to_thing_data)
                thing_obj.save()
                context['thing_data'].append(thing_obj)

            to_item_data = {
                'thing': thing_obj,
                'name': column[5],
                'rating': column[6],
                'score': column[7],
            }
            to_item_data, data_errors = validators.validate_and_clean(
                'item', to_item_data)

            try:
                item_obj = Item(**to_item_data)
                item_obj.save()
            except:
                print('Problem with the item data')

            context['item_data'].append(item_obj)

    messages.warning(
        request, data_errors)
    context['all_thing_data'] = reversed(Thing.objects.all())
    context['all_item_data'] = reversed(Item.objects.all().order_by('name'))
    return render(request, template, context)


# def record_form(request):
#     t_form, i_form = ThingForm, ItemForm

#     if request.method == 'POST':
#         t_form = ThingForm(request.POST)

#         if t_form.is_valid():
#             t_form.save()
#             messages.success(
#                 request, 'success')

#     if request.method == 'POST':
#         i_form = ItemForm(request.POST)

#         if i_form.is_valid():
#             i_form.save()
#             messages.success(
#                 request, 'success')

#     context = {
#         'i_form': i_form,
#         't_form': t_form,
#         'thing_data': Thing.objects.all(),
#         'item_data': Item.objects.all(),
#     }
#     return render(request, 'records/record_form.html', context)
