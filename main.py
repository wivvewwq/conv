from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from virtualenv import run

# Курсы валют (можно подключить API для актуальных курсов)
exchange_rates = {
    'RUB': 1,
    'USD': 95,
    'EUR': 100,
    'CNY': 13
}


class CurrencyConverterApp(App):
    def build(self):
        # Основной layout приложения
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Ввод суммы
        self.amount_input = TextInput(hint_text='Введите сумму', multiline=False, input_filter='float')
        layout.add_widget(self.amount_input)

        # Выбор начальной валюты
        self.from_currency = Spinner(text='RUB', values=['RUB', 'USD', 'EUR', 'CNY'])
        layout.add_widget(self.from_currency)

        # Выбор конечной валюты
        self.to_currency = Spinner(text='USD', values=['RUB', 'USD', 'EUR', 'CNY'])
        layout.add_widget(self.to_currency)

        # Кнопка конвертации
        convert_button = Button(text='Конвертировать', on_press=self.convert_currency)
        layout.add_widget(convert_button)

        # Поле для отображения результата
        self.result_label = Label(text='Результат:')
        layout.add_widget(self.result_label)

        return layout

    def convert_currency(self, instance):
        # Получаем данные из интерфейса
        amount = float(self.amount_input.text)
        from_cur = self.from_currency.text
        to_cur = self.to_currency.text

        # Переводим из одной валюты в другую через рубли
        amount_in_rub = amount * exchange_rates[from_cur]  # Переводим в рубли
        result = amount_in_rub / exchange_rates[to_cur]  # Конвертируем в целевую валюту

        # Отображаем результат
        self.result_label.text = f'Результат: {result:.2f} {to_cur}'


# Запуск приложения
if __name__ == '__main__':
    CurrencyConverterApp().run()






