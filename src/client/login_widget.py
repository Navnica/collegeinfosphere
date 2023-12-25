from PySide6 import QtCore, QtWidgets


class LoginWidget(QtWidgets.QWidget):
    login_line_edit: QtWidgets.QLineEdit
    password_line_edit: QtWidgets.QLineEdit

    def __init__(self, parent: QtWidgets.QWidget) -> None:
        super(LoginWidget, self).__init__(parent)
        self.init_ui()
        self.show()

    def init_ui(self) -> None:
        main_layout = QtWidgets.QVBoxLayout()
        input_layout = QtWidgets.QHBoxLayout()
        input_layout_label = QtWidgets.QVBoxLayout()
        input_layout_line_edit = QtWidgets.QVBoxLayout()
        group_box_layout = QtWidgets.QVBoxLayout()

        self.setLayout(main_layout)
        main_layout.addLayout(input_layout)
        input_layout.addLayout(input_layout_label)
        input_layout.addLayout(input_layout_line_edit)

        login_label = QtWidgets.QLabel("Логин")
        password_label = QtWidgets.QLabel("Пароль")
        self.login_line_edit = QtWidgets.QLineEdit()
        self.password_line_edit = QtWidgets.QLineEdit()
        group_box = QtWidgets.QGroupBox("Я")
        self.student_radio_button = QtWidgets.QRadioButton("Студент")
        self.staff_radio_button = QtWidgets.QRadioButton("Сотрудник")

        input_layout_label.addWidget(login_label)
        input_layout_label.addWidget(password_label)
        input_layout_line_edit.addWidget(self.login_line_edit)
        input_layout_line_edit.addWidget(self.password_line_edit)
        group_box.setLayout(group_box_layout)
        main_layout.addWidget(group_box)
        group_box_layout.addWidget(self.student_radio_button)
        group_box_layout.addWidget(self.staff_radio_button)

        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.student_radio_button.setChecked(True)

        main_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        main_layout.setContentsMargins(0, 0, 0, 0)
