__author__ = 'patriot'

from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import (ListProperty, NumericProperty)
from kivy.app import App


class GridEntry(Button):
    coords = ListProperty([0, 0])


class TicTacToeGrid(GridLayout):
    status = ListProperty([0,0,0, 0,0,0, 0,0,0])
    current_player = NumericProperty(1)
    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)

        for row in range(3):
            for column in range(3):
                grid_entry = GridEntry(coords = (row,column))
                grid_entry.bind(on_release = self.button_pressed)
                self.add_widget(grid_entry)

    def button_pressed(self, button):
        print ('{} button clicked!'.format(button.coords))
        player = {1: 'O', -1: 'X'}
        colours = {1: (1,0,0,1), -1: (0,1,0,1)}
        row, column = button.coords

        status_index = 3*row + column
        already_played = self.status[status_index]

        if not already_played:
            self.status[status_index] = self.current_player
            button.text = {1: 'O', -1: 'X'}[self.current_player]
            button.background_color = colours[self.current_player]
            self.current_player *= -1

    def on_status(selfself, instance, new_value):
        status = new_value

        sums = [sum(status[0:3]),
                sum(status[3:6]), sum(status[6:9]), sum(status[0::3]),
                sum(status[1::3]), sum(status[2::3]), sum(status[::4]),
                sum(status[2:-2:2])]

        if 3 in sums:
            print("Os win!")
        elif -3 in sums:
            print("Xs win!")
        elif 0 not in self.status:
            print("Draw!")

class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()

if __name__ == "__main__":
    TicTacToeApp().run()