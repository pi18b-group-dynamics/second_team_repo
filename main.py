from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class MyApp(App):

    def build(self):
        main_layout = BoxLayout(orientation='horizontal')

        record_layout = BoxLayout(orientation='vertical')
        find_layout = BoxLayout(orientation='vertical')
        find_area = BoxLayout(orientation='vertical')

        list_of_data = 'Введите фамилию', 'Введите имя', 'Введите отчество', 'Серия', \
                       'Номер', 'Пол', 'Кто выдал', 'Дата выдачи', 'Фотография'

        for row in list_of_data:
            record_layout.add_widget(TextInput(hint_text=row,
                                               id='Добавление - ' + row))

        find_layout.add_widget(TextInput(text='Поиск',
                                         readonly=True))
        for row in list_of_data:
            find_layout.add_widget(TextInput(hint_text=row,
                                             id='Поиск - ' + row))

        main_layout.add_widget(record_layout)
        main_layout.add_widget(find_layout)
        main_layout.add_widget(find_area)
        return main_layout


if __name__ == "__main__":
    MyApp().run()
