from django.urls import path, register_converter
from datetime import datetime

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
from app.views import file_list, file_content


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format)

    def to_url(self, value):
        return value.strftime(self.format)


register_converter(DateConverter, 'dtc')


urlpatterns = [
    path('', file_list, name='file_list'),
    path('<dtc:date>/', file_list, name='file_list'),
    path('file/<str:name>/', file_content, name='file_content'),
]
