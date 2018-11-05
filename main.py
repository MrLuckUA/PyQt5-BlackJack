#!/usr/bin/env python3
import sys
import random
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSlot


class Game(QtWidgets.QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        self.player_point = 0
        self.opponent_point = 0
        uic.loadUi('view.ui', self)
        self.exit_game.triggered.connect(self.close)
        self.restart_game.triggered.connect(self.restart)
        self.more_button.clicked.connect(self.more_clicked)
        self.stop_button.clicked.connect(self.stop_clicked)

    @pyqtSlot()
    def restart(self):
        self.player_point = 0
        self.opponent_point = 0
        self.opponent_point_lable.setText(str(self.opponent_point))
        self.player_point_lable.setText(str(self.player_point))
        self.winner_label.setText("")
        self.more_button.setEnabled(True)
        self.stop_button.setEnabled(True)

    @pyqtSlot()
    def stop_clicked(self):
        self.more_button.setDisabled(True)
        self.stop_button.setDisabled(True)
        self.opponent_move()

    @pyqtSlot()
    def more_clicked(self):
        self.add_player_point()

    @pyqtSlot()
    def close(self):
        sys.exit(app.exec_())

    def opponent_move(self):
        while not self.player_point < self.opponent_point:
            self.add_opponent_point()
            self.check_point()
        self.check_winner()

    def add_player_point(self):
        a = random.randrange(2, 12)
        self.player_point += a
        self.check_point()
        self.player_point_lable.setText(str(self.player_point))

    def add_opponent_point(self):
        a = random.randrange(2, 12)
        self.opponent_point += a
        self.check_point()
        self.opponent_point_lable.setText(str(self.opponent_point))

    def check_winner(self):
        if self.player_point > self.opponent_point:
            self.winner_label.setText("You WIN!!!")
        elif self.player_point < self.opponent_point:
            self.winner_label.setText("Opponent WIN!!!")
        else:
            self.winner_label.setText("DRAW!!!")
        self.check_point()

    def check_point(self):
        if self.player_point > 21:
            self.winner_label.setText("Opponent WIN!!!")
            self.more_button.setDisabled(True)
            self.stop_button.setDisabled(True)
        elif self.opponent_point > 21:
            self.winner_label.setText("You WIN!!!")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Game()
    window.show()
    sys.exit(app.exec_())
