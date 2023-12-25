from PySide6 import QtCore, QtWidgets
from src.client.login_widget import LoginWidget
from src.client.api.resolvers import student_login, staff_login


class AuthWidget(QtWidgets.QWidget):
    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super(AuthWidget, self).__init__(parent)
        self.init_ui()
        self.show()

    def init_ui(self) -> None:
        main_layout = QtWidgets.QVBoxLayout()
        input_layout = QtWidgets.QHBoxLayout()
        buttons_layout = QtWidgets.QHBoxLayout()

        self.setLayout(main_layout)
        main_layout.addLayout(input_layout)
        main_layout.addLayout(buttons_layout)

        self.login_widget = LoginWidget(self)
        login_button = QtWidgets.QPushButton("Войти")

        input_layout.addWidget(self.login_widget)
        buttons_layout.addWidget(login_button)

        main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        main_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setContentsMargins(0, 15, 0, 0)

        login_button.clicked.connect(self.on_login_click)

    def on_login_click(self) -> None:
        answer: dict = {}
        if self.login_widget.student_radio_button.isChecked():
            answer = student_login(self.login_widget.login_line_edit.text(), self.login_widget.password_line_edit.text())

        else:
            answer = staff_login(self.login_widget.login_line_edit.text(), self.login_widget.password_line_edit.text())

        if type(answer) is dict:
            QtWidgets.QMessageBox(
                QtWidgets.QMessageBox.Icon.Critical,
                "Error",
                answer['error'],
                QtWidgets.QMessageBox.StandardButton.Ok
            ).exec_()
