# пример наследования реализации из библиотеки django, где класс Form является базовым классом для создания форм.
# CustomContactForm наследует реализацию класса ContactForm, добавляя свойство label для поля subject.
# Класс CustomContactForm используется вместо ContactForm, когда необходимо создать форму с измененным поведением для поля subject.

from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class CustomContactForm(ContactForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].label = 'Weird Custom Subject'

########################################################################################

# пример льготного наследования от базового класса logging.Handler, кот. предоставляет стандартные методы для логирования в приложении.
# Например, в этом классе есть метод emit(), который отправляет запись журнала в заданный поток.

# CustomStreamHandlef, наследник logging.StreamHandler, использует метод emit(), но определяет свои собственные методы и атрибуты для конкретного типа потока вывода.

import logging

class CustomStreamHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        super().__init__(stream=stream)
        self._custom_attribute = "custom_value"

    def custom_behavior(self):
        print("Custom method called")

    def emit(self, record):
        super().emit(record)
        self.custom_behavior()
