from abc import ABC, abstractmethod


class UIControm(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControm):
    def draw(self):
        print("Drawing a text box.")


class DropDownList(UIControm):
    def draw(self):
        print("Drawing a dropdown list.")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
text_box = TextBox()
draw([ddl, text_box])  # Output: Drawing a dropdown list.
