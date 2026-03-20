from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import math

Window.size = (300, 400)

class CalculatorApp(App):
    def build(self):
        self.operation = ""
        self.first_num = 0
        self.second_num = 0
        
        main_layout = BoxLayout(orientation='vertical', spacing=5, padding=5)
        
        self.display = TextInput(
            text='0',
            font_size=32,
            readonly=True,
            halign='right',
            size_hint=(1, 0.2)
        )
        main_layout.add_widget(self.display)
        
        buttons_layout = GridLayout(cols=4, spacing=3, size_hint=(1, 0.8))
        
        buttons = [
            ['7', self.on_button_press, '#9C27B0'],
            ['8', self.on_button_press, '#9C27B0'],
            ['9', self.on_button_press, '#9C27B0'],
            ['+', self.on_operation, '#FF9800'],
            ['4', self.on_button_press, '#9C27B0'],
            ['5', self.on_button_press, '#9C27B0'],
            ['6', self.on_button_press, '#9C27B0'],
            ['-', self.on_operation, '#FF9800'],
            ['1', self.on_button_press, '#9C27B0'],
            ['2', self.on_button_press, '#9C27B0'],
            ['3', self.on_button_press, '#9C27B0'],
            ['*', self.on_operation, '#FF9800'],
            ['0', self.on_button_press, '#9C27B0'],
            ['.', self.on_button_press, '#9C27B0'],
            ['/', self.on_operation, '#FF9800'],
            ['%', self.on_operation, '#FF9800'],
            ['C', self.clear_display, '#F44336'],
            ['√', self.square_root, '#4CAF50'],
            ['=', self.on_equal, '#4CAF50'],
            ['', None, ''],
        ]
        
        for btn_text, btn_func, btn_color in buttons:
            if btn_text:
                btn = Button(
                    text=btn_text,
                    font_size=24,
                    background_color=btn_color,
                    on_press=btn_func
                )
                buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        return main_layout
    
    def on_button_press(self, instance):
        current = self.display.text
        if current == '0':
            self.display.text = instance.text
        else:
            self.display.text = current + instance.text
    
    def on_operation(self, instance):
        self.first_num = float(self.display.text)
        self.operation = instance.text
        self.display.text = '0'
    
    def on_equal(self, instance):
        self.second_num = float(self.display.text)
        
        if self.operation == '+':
            result = self.first_num + self.second_num
        elif self.operation == '-':
            result = self.first_num - self.second_num
        elif self.operation == '*':
            result = self.first_num * self.second_num
        elif self.operation == '/':
            if self.second_num != 0:
                result = self.first_num / self.second_num
            else:
                self.display.text = 'Ошибка'
                return
        elif self.operation == '%':
            result = (self.first_num / self.second_num) * 100
        
        self.display.text = str(result)
    
    def clear_display(self, instance):
        self.display.text = '0'
        self.first_num = 0
        self.second_num = 0
        self.operation = ''
    
    def square_root(self, instance):
        num = float(self.display.text)
        if num >= 0:
            self.display.text = str(math.sqrt(num))
        else:
            self.display.text = 'Ошибка'

if __name__ == '__main__':
    CalculatorApp().run()
