from django.shortcuts import render, redirect, reverse, HttpResponse
from image_app.forms import LoadImageForm
from image_app.models import ImageStorage, History

def experiment(request):
    # print('\n'*2,'*'*20, *dir(request), '*'*20, '\n'*2, sep='\n')

    return HttpResponse('CHECK CONSOLE')


def check(request):
    if request.user.is_authenticated:
        if request.POST:
            print(f'\n\n\n{"1 уровень"}\n\n\n')
            form = LoadImageForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                print(f'\n\n\n{"2 уровень"}\n\n\n')
                new_record = form.save(commit=False)
                new_record.user = request.user
                new_record.save()
                History.objects.create(image_id=new_record.id, cause=1)
                return HttpResponse('<p>Файл записан</p><br><a href="http://127.0.0.1:8000/">Назад</a>')
            else:
                print(f'\n\n\n{"3 уровень"}\n\n\n')
                return HttpResponse('<p>ERROR</p><br><a href="http://127.0.0.1:8000/">Назад</a>')
        else:
            print(f'\n\n\n{"4 уровень"}\n\n\n')
            return render(request, template_name='image_app/home.html', context={'form': LoadImageForm()})
    else:
        return redirect(reverse('accounts:login'))






def profile(request):
    user = request.user
    image_list = ImageStorage.objects.filter(user=user)
    history_list = History.objects.filter(image__user=user).select_related('image')
    context = {
        'image_list': image_list,
        'history_list': history_list,
    }
    return render(request, 'image_app/profile.html', context=context)


"""
check
clean
clean_fields
date_error_message
delete
diff_against
from_db
full_clean
get_default_history_user
get_deferred_fields
get_history_type_display
get_next_by_history_date
get_next_by_timestamp
get_previous_by_history_date
get_previous_by_timestamp
history_change_reason
history_date
history_id
history_object
history_type
history_user
history_user_id
id
image
instance
instance_type
next_record
objects
pk
prepare_database_save
prev_record
refresh_from_db
revert_url
save
save_base
serializable_value
timestamp
unique_error_message
user
user_id
validate_unique
"""



# Create your views here.
