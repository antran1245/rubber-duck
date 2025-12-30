from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class OptionLayout(QWidget):

    def __init__(self, title: str, buttons_list: list):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setSpacing(1)
        label = QLabel(title)
        label.setStyleSheet("color: white; font-size: 14px;")

        self.build_buttons(label, buttons_list)
        self.setLayout(self.layout)
        self.resize(140, 100)

    def build_buttons(self, label, buttons_list):
        for btn in buttons_list:
            btn.setStyleSheet(
                """
                      QPushButton {
                          background: rgba(30,30,30,180);
                          color: white;
                          padding: 6px;
                          border-radius: 8px;
                      }
                      QPushButton:hover {
                          background: rgba(60,60,60,200);
                      }
                  """
            )

        for element in [label, *buttons_list]:
            self.layout.addWidget(element)
