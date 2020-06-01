from kivy import Config
from kivy.uix.image import Image
import pdf
Config.set('graphics', 'width', 1500)
Config.set('graphics', 'height', 800)
from kivy.app import App
import util
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyApp(App):

    dict_of_update = {}
    watcher = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Система паспортного учета'
        self.main_layout = BoxLayout(orientation='horizontal',)  # создаем главный макет, в котором будут макеты поиска и остальные
        self.list_of_data = {'Введите фамилию': 'last_name',    # словарь с данными кнопошек
                             'Введите имя': 'first_name',
                             'Введите отчество': 'patronymic',
                             'Серия': 'series',
                             'Номер': 'number_', 'Пол': 'sex',
                             'Кто выдал': 'whos_give',
                             'Дата выдачи': 'date_of_give',
                             'Фотография': 'photo'}

    def build(self):

        record_layout = BoxLayout(orientation='vertical',
                                  id='record',
                                  size_hint_x=.3)
        find_area = GridLayout(cols=9,
                               id="find",
                               )
        watch_area = BoxLayout(orientation='vertical',
                               size_hint_x=.3,
                               id="watch")

        self.watcher = TextInput(text='Введите данные',
                                 readonly=True,
                                 foreground_color=(1, 0, 0, 1)
                                 )
        record_layout.add_widget(self.watcher)
        for key, value in self.list_of_data.items():
            record_layout.add_widget(TextInput(hint_text=key,
                                               id=value,
                                               multiline=False))
        else:
            for button in 'Добавить', 'Удалить', 'Изменить', 'Поиск', 'Вывод в pdf':
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
            self.watcher.text = self.update()
        elif instance.text == 'Поиск':
            self.search()
        else:
            pdf.simple_table(data=util.print_all())

    def get_data_from_inputs(self):     # функция которая достает словарь или json объект из input'ов
        # след. цикл и вообще конструкция - добираемся до input'ов
        dict_of_data = {}  # словарь с данными полей, который мы и будем передавать
        for box_layout in self.main_layout.children:  # цикл на перебор всех макетов (тут нам нужен только рекорд)
            if box_layout.id == 'record':  # находим рекорд
                for widget in box_layout.children[4:-1]:
                    key, value = widget.id, widget.text
                    dict_of_data.update({key: value})
                    # widget.text = ''  # очистка поля после ввода (подумай, мб очищать только плохие поля, или все если верно)
        return dict_of_data

    def add(self):  # ДОБАВЛЕНИЕ (добавить визуала лучше, и проверки !!!!)
        result = util.add_in_db(**self.get_data_from_inputs())
        for box_layout in self.main_layout.children:  # цикл на перебор всех макетов (тут нам нужен только рекорд)
            if box_layout.id == 'record':  # находим рекорд
                for widget in box_layout.children[5:-1]:
                    if len(result) == 2:
                        if widget.id == result[1]:
                            widget.hint_text, widget.hint_text_color, widget.text = result[0], (1, 0, 0, 1), ''
                            return
                    else:
                        widget.text = ''
                else:   # тут возврат хинтов сделать
                    print()

    def remove(self):
        self.watcher.text = util.remove_from_db(self.get_data_from_inputs())

    def update(self):
        if len(tuple(1 for x in self.get_data_from_inputs().values() if x)) == 0:
            if len(self.dict_of_update) == 0:
                return 'Введите данные человека которого хотите изменить'
            else:
                return 'Введите данные человека которые хотите изменить'
        if len(self.dict_of_update) == 0:
            if util.check_in_db(self.get_data_from_inputs()):
                self.dict_of_update = self.get_data_from_inputs()
                return 'Введите новые данные для человека:'
            else:
                return 'Паспорт не найден'
        else:
            if util.check_on_of_all(self.get_data_from_inputs()):
                return 'Пользователь изменен'
            else:
                return 'Пользователь не изменен, ошибка в данных'

    def search(self):
        result = util.find_in_db(**self.get_data_from_inputs())
        if not result:
            return
        for layout in self.main_layout.children:
            if layout.id == 'find':
                layout.clear_widgets()
                for name_of_row in 'id', 'Имя', 'Фамилия', 'Отчество', 'Серия', 'Номер', 'Пол', 'Кто выдал', 'Дата выдачи':  # вывод кнопок
                    layout.add_widget(Button(text=name_of_row,
                                             size_hint_y=None,
                                             height=50))

                for row in result:  # печать результата поиска
                    id_ = str(row[0])
                    for cell in row[:-1]:
                        layout.add_widget(Button(text=str(cell),
                                                 size_hint_y=None,
                                                 height=50,
                                                 on_press=self.output_image,
                                                 id=id_))

    def output_image(self, instance):
        pic = Image(source=util.print_pic(int(instance.id)))
        for layout in self.main_layout.children:
            if layout.id == 'find':
                for button in layout.children:
                    if button.id == instance.id:
                        button.background_color = (1, 0, 0, 1)
                    else:
                        button.background_color = (1, 1, 1, 1)
            if layout.id == 'watch':
                layout.clear_widgets()
                layout.add_widget(pic)
                layout.add_widget(Button(text='Фотография пользователя',
                                         size_hint_y=.2))


if __name__ == "__main__":
    MyApp().run()
