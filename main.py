from kivy.app import App
import util
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


class MyApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main_layout = BoxLayout(orientation='horizontal')

    def build(self):

        record_layout = BoxLayout(orientation='vertical',
                                  id='record')
        find_area = BoxLayout(orientation='vertical')
        watch_area = BoxLayout(orientation='vertical')

        list_of_data = {'Введите фамилию': 'last_name', 'Введите имя': 'first_name', 'Введите отчество': 'patronymic', 'Серия': 'series', \
                       'Номер': 'number_', 'Пол': 'sex', 'Кто выдал': 'whos_give', 'Дата выдачи': 'date_of_give', 'Фотография': 'photo'}

        record_layout.add_widget(TextInput(text='Введите данные',
                                           readonly=True,
                                           ))
        for key, value in list_of_data.items():
            record_layout.add_widget(TextInput(hint_text=key,
                                               id='Добавление - ' + value))
        else:
            for button in 'Добавить', 'Удалить', 'Изменить', 'Найти':
                record_layout.add_widget(Button(text=button,
                                                on_press=self.work_with_db))

        self.main_layout.add_widget(record_layout)
        self.main_layout.add_widget(find_area)
        self.main_layout.add_widget(watch_area)
        return self.main_layout

    def work_with_db(self, instance):   # функция работы кнопок удалить добавить и т.д.
        if instance.text == 'Добавить':
            self.add()
        elif instance.text == 'Удалить':
            self.remove()
        elif instance.text == 'Изменить':
            self.update()
        elif instance.text == 'Поиск':
            self.search()

    def add(self):  # ДОБАВЛЕНИЕ (добавить визуала лучше, и проверки !!!!)
        # след. цикл и вообще конструкция - добираемся до input'ов
        dict_of_data = {}   # словарь с данными полей, который мы и будем передавать
        for box_layout in self.main_layout.children:    # цикл на перебор всех макетов (тут нам нужен только рекорд)
            if box_layout.id == 'record':   # находим рекорд
                for widget in box_layout.children[5:-1]:
                    key, value = widget.id, widget.text
                    dict_of_data.update({key[key.find('- ') + 2:]: value})
                    widget.text = ''    # очистка поля после ввода (подумай, мб очищать только плохие поля, или все если верно)

        print(util.add_in_db(**dict_of_data))

    def remove(self):
        pass

    def update(self):
        pass

    def search(self):
        util.find_in_db()



if __name__ == "__main__":
    MyApp().run()
