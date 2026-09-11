import arabic_reshaper
from bidi.algorithm import get_display

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.core.text import LabelBase


FONT = "Vazirmatn-Regular.ttf"

LabelBase.register(
    name="Vazir",
    fn_regular=FONT
)


def fa(text):
    text = str(text)
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)


# Colors
BG = (0.090, 0.106, 0.149, 1)
CARD = (0.14, 0.16, 0.21, 1)
TITLE = (0.000, 0.741, 0.000, 1)
PRIMARY = (0.082, 0.008, 0.490, 1)
PRIMARY_DARK = (0.361, 0.012, 0.082, 1)
TEXT = (0.890, 1.000, 0.969, 1)
FOREGROUND = (0, 0, 0, 1)
BACK = (0.612, 0.012, 0.012, 1)
SECONDARY = (0.878, 0.878, 0.863, 1)
GREEN = (0.09, 0.64, 0.30, 1)
RED = (0.86, 0.15, 0.15, 1)
GOLD = (0.90, 0.55, 0.05, 1)


# Medical courses
medicine_courses = [
    ("اسکلتی عضلانی", 2.4),
    ("ادراری تناسلی", 1.1),
    ("باکتری شناسی", 3),
    ("روانشناسی", 2),
    ("اپیدمیولوژی", 2),
    ("تاریخ تحلیلی", 2),
    ("اندیشه 2", 2),
    ("فیزیو کلیه", 0.8),
    ("بیو کلیه", 0.2),
    ("زبان عمومی", 2),
    ("آداب 1", 0.5),
    ("آداب 2", 0.5),
    ("تشریح قلب", 1.5),
    ("تشریح تنفس", 0.7),
    ("تشریح گوارش", 2),
    ("فیزیو قلب", 0.5),
    ("فیزیو گردش", 1.2),
    ("فیزیو تنفس", 0.7),
    ("فیزیو گوارش", 0.7),
    ("دیس 1", 0.57),
    ("دیس 2", 0.57),
    ("دیس 3", 0.56),
    ("تغذیه", 2),
    ("ایمنی", 2),
    ("تفسیر", 2),
    ("اندیشه 1", 2),
    ("تربیت بدنی", 1),
    ("پیش دو", 3),
    ("سروگردن", 1.7),
    ("تشریح اعصاب", 1.9),
    ("تشریح حواس ویژه", 0.9),
    ("فیزیو اعصاب و حواس", 1.5),
    ("زبان تخصصی 1", 3),
    ("انگل", 2),
    ("قارچ", 1),
    ("حوادث بلایا", 2),
    ("انقلاب", 2),
    ("تاریخ فرهنگ و تمدن", 2),
    ("مقدمات تشریح", 2.5),
    ("فیزیو سلول 2", 0.2),
    ("فیزیو سلول 1", 0.6),
    ("بیو سلول 1", 1.15),
    ("بیو سلول 2", 1.15),
    ("فیزیو خون", 0.4),
    ("اصول خدمات", 1.5),
    ("فارسی", 2),
    ("ایمنی ترافیک", 1),
    ("فیزیک پزشکی", 2),
    ("دفاع مقدس", 2),
    ("کلیات پاتولوژی", 0.5),
    ("پاتولوژی آماس،ترمیم بافتی و اختلالات", 0.6),
    ("پاتولوژی اختلالات سیستم ایمنی", 0.5),
    ("پاتولوژی نیوپلازی", 0.6),
    ("پاتولوژی اختلالات ژنتیک و بیماری های دوره", 0.5),
    ("پاتولوژی بیماری های محیطی،تغذیه ای", 0.4),
    ("پاتو عملی", 1),
    ("مهارت های زندگی", 2),
]


# Dentistry courses
dentistry_courses = [
    ("انگل شناسی، قارچ شناسی", 1),
    ("علوم تشریحی 2", 2),
    ("زبان پیش دانشگاهی 1", 2),
    ("باکتری شناسی عملی", 1),
    ("سلامت دهان و جامعه", 2),
    ("آسیب شناسی عمومی نظری", 2.5),
    ("روانشناسی و مهارت های ارتباطی", 2),
    ("اندیشه اسلامی 1 (مبدا و معاد)", 2),
    ("تربیت بدنی 1 (فقط مقاطع پیوسته)", 1),
    ("آیین زندگی (اخلاق کاربردی)", 2),
    ("بافت دندان در سلامت و بیماری", 2),
    ("انقلاب اسلامی ایران", 2),
    ("زبان پیش دانشگاهی 2", 2),
    ("اندیشه اسلامی 2", 2),
    ("اندیشه اسلامی 3 (نبوت و امامت)", 2),
    ("آشنایی با ارزشهای دفاع مقدس", 2),
    ("Preliminary Persian 1", 2),
    ("تربیت بدنی 1", 1),
    ("علوم تشریحی 3", 2),
    ("Preliminary Persian 2", 2),
    ("ایمنی شناسی نظری", 2.5),
    ("باکتری شناسی نظری", 2),
    ("فیزیک پزشکی", 1),
    ("فیزیولوژی عملی", 1),
    ("بیوشیمی نظری 2", 2),
    ("آناتومی و مورفولوژی دندانپزشکی (نظری - عملی)", 3),
    ("ژنتیک انسانی", 2),
    ("ادبیات فارسی", 2),
    ("زبان انگلیسی عمومی", 3),
    ("رادیولوژی دندان، فک و صورت نظری 1", 1),
    ("تفسیر موضوعی قرآن", 2),
    ("فیزیولوژی نظری 2", 2),
    ("ایمنی شناسی عملی", 0.5),
    ("آسیب شناسی عمومی عملی", 0.5),
    ("دانش خانواده و جمعیت", 2),
    ("فیزیولوژی نظری 1", 2),
    ("بیوشیمی نظری 1", 2),
    ("ویروس شناسی پزشکی", 1),
    ("علوم تشریحی 1", 2),
    ("علوم و معارف دفاع مقدس و مقاومت", 2),
    ("تاریخ فرهنگ و تمدن اسلام و ایران", 2),
    ("Preliminary Persian 2", 2),
    ("بیوشیمی عملی", 1),
    ("کاربرد رایانه در دندانپزشکی", 1),
    ("General Persian", 3),
    ("General English", 3),
    ("تاریخ تحلیلی صدر اسلام", 2),
    ("تغذیه در سلامت دهان", 1),
]


class Card(BoxLayout):

    def __init__(self, color=CARD, radius=18, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(*color)

            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(radius)]
            )

        self.bind(
            pos=self.update_rect,
            size=self.update_rect
        )

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class GPAApp(App):

    def build(self):
        self.title = "GPA Calculator"

        self.root_layout = BoxLayout(
            orientation="vertical",
            padding=dp(16),
            spacing=dp(10)
        )

        with self.root_layout.canvas.before:
            Color(*BG)

            self.bg_rect = RoundedRectangle(
                pos=self.root_layout.pos,
                size=self.root_layout.size
            )

        self.root_layout.bind(
            pos=self.update_background,
            size=self.update_background
        )

        self.show_home()

        return self.root_layout

    def update_background(self, *args):
        self.bg_rect.pos = self.root_layout.pos
        self.bg_rect.size = self.root_layout.size

    def make_label(
        self,
        text,
        font_size=16,
        color=TEXT,
        bold=False,
        **kwargs
    ):
        text = fa(text)

        if bold:
            text = "[b]" + text + "[/b]"

        return Label(
            text=text,
            markup=bold,
            font_name=FONT,
            font_size=dp(font_size),
            color=color,
            **kwargs
        )

    def show_home(self, *args):
        self.root_layout.clear_widgets()

        title = self.make_label(
            "محاسبه معدل",
            font_size=30,
            color=TITLE,
            bold=True,
            size_hint_y=None,
            height=dp(65)
        )

        subtitle = self.make_label(
            "رشته خود را انتخاب کنید",
            font_size=17,
            color=SECONDARY,
            size_hint_y=None,
            height=dp(40)
        )

        self.root_layout.add_widget(title)
        self.root_layout.add_widget(subtitle)
        self.root_layout.add_widget(BoxLayout())

        medicine_button = Button(
            text=fa("پزشکی"),
            font_name=FONT,
            font_size=dp(22),
            bold=True,
            background_normal="",
            background_color=PRIMARY,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(70)
        )

        medicine_button.bind(
            on_press=self.show_medicine
        )

        dentistry_button = Button(
            text=fa("دندانپزشکی"),
            font_name=FONT,
            font_size=dp(22),
            bold=True,
            background_normal="",
            background_color=PRIMARY_DARK,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(70)
        )

        dentistry_button.bind(
            on_press=self.show_dentistry
        )

        self.root_layout.add_widget(medicine_button)
        self.root_layout.add_widget(dentistry_button)
        self.root_layout.add_widget(BoxLayout())

        footer = self.make_label(
            "فقط نمره درس‌هایی را که این ترم برداشته‌اید وارد کنید",
            font_size=13,
            color=SECONDARY,
            size_hint_y=None,
            height=dp(45)
        )

        self.root_layout.add_widget(footer)

    def show_courses(self, title_text, courses):
        self.root_layout.clear_widgets()
        title = self.make_label(
            title_text,
            font_size=27,
            color=TITLE,
            bold=True,
            size_hint_y=None,
            height=dp(55)
        )

        self.root_layout.add_widget(title)

        info = self.make_label(
            "نمره هر درس را وارد کنید؛ درس‌های بدون نمره محاسبه نمی‌شوند",
            font_size=14,
            color=SECONDARY,
            size_hint_y=None,
            height=dp(40)
        )

        self.root_layout.add_widget(info)

        scroll = ScrollView(
            do_scroll_x=False,
            bar_width=dp(7)
        )

        course_grid = GridLayout(
            cols=1,
            spacing=dp(9),
            padding=dp(4),
            size_hint_y=None
        )

        course_grid.bind(
            minimum_height=course_grid.setter("height")
        )

        self.entries = []

        for index, (course_name, unit) in enumerate(
            courses,
            start=1
        ):

            row = Card(
                orientation="horizontal",
                padding=dp(10),
                spacing=dp(8),
                size_hint_y=None,
                height=dp(76)
            )

            number_label = self.make_label(
                f"{index}.",
                font_size=16,
                color=SECONDARY,
                bold=True,
                size_hint_x=0.10
            )

            course_info = BoxLayout(
                orientation="vertical",
                spacing=dp(1),
                size_hint_x=0.65
            )

            course_label = self.make_label(
                course_name,
                font_size=16,
                color=TEXT,
                bold=True,
                halign="right",
                valign="middle"
            )

            course_label.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            unit_label = self.make_label(
                f"{unit:g} واحد",
                font_size=13,
                color=SECONDARY,
                halign="right",
                valign="middle"
            )

            unit_label.bind(
                size=lambda instance, value:
                setattr(instance, "text_size", value)
            )

            course_info.add_widget(course_label)
            course_info.add_widget(unit_label)

            entry = TextInput(
                hint_text=fa("نمره"),
                font_name=FONT,
                multiline=False,
                input_filter="float",
                font_size=dp(17),
                size_hint_x=0.25,
                background_normal="",
                background_active="",
                background_color=(0.94, 0.96, 0.99, 1),
                foreground_color=FOREGROUND,
                cursor_color=PRIMARY,
                padding=[dp(8), dp(12)]
            )

            self.entries.append(
                (entry, unit)
            )

            row.add_widget(number_label)
            row.add_widget(course_info)
            row.add_widget(entry)

            course_grid.add_widget(row)

        scroll.add_widget(course_grid)

        self.root_layout.add_widget(scroll)

        result_card = Card(
            orientation="vertical",
            padding=dp(8),
            spacing=dp(2),
            size_hint_y=None,
            height=dp(100)
        )

        self.gpa_label = self.make_label(
            "معدل: --",
            font_size=21,
            color=TEXT,
            bold=True
        )

        self.units_label = self.make_label(
            "مجموع واحد: --",
            font_size=15,
            color=SECONDARY
        )

        self.status_label = self.make_label(
            "وضعیت: --",
            font_size=17,
            color=TEXT,
            bold=True
        )

        result_card.add_widget(
            self.gpa_label
        )

        result_card.add_widget(
            self.units_label
        )

        result_card.add_widget(
            self.status_label
        )
        self.root_layout.add_widget(
            result_card
        )

        calculate_button = Button(
            text=fa("محاسبه معدل"),
            font_name=FONT,
            font_size=dp(19),
            bold=True,
            background_normal="",
            background_color=GREEN,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(55)
        )

        calculate_button.bind(
            on_press=self.calculate_gpa
        )

        self.root_layout.add_widget(
            calculate_button
        )

        back_button = Button(
            text=fa("بازگشت"),
            font_name=FONT,
            font_size=dp(16),
            background_normal="",
            background_color=BACK,
            color=(1, 1, 1, 1),
            size_hint_y=None,
            height=dp(43)
        )

        back_button.bind(
            on_press=self.show_home
        )

        self.root_layout.add_widget(
            back_button
        )

    def show_medicine(self, *args):
        self.current_courses = medicine_courses

        self.show_courses(
            "دروس پزشکی",
            medicine_courses
        )

    def show_dentistry(self, *args):
        self.current_courses = dentistry_courses

        self.show_courses(
            "دروس دندانپزشکی",
            dentistry_courses
        )

    def calculate_gpa(self, *args):
        total_score = 0
        total_units = 0
        entered_courses = 0

        for entry, unit in self.entries:

            value = entry.text.strip()

            if value == "":
                continue

            try:
                score = float(value)

            except ValueError:
                self.gpa_label.text = fa(
                    "معدل: خطا"
                )

                self.units_label.text = fa(
                    "لطفاً فقط عدد وارد کنید"
                )

                self.status_label.text = fa(
                    "وضعیت: خطا"
                )

                return

            if score < 0 or score > 20:
                self.gpa_label.text = fa(
                    "معدل: خطا"
                )

                self.units_label.text = fa(
                    "نمره باید بین ۰ تا ۲۰ باشد"
                )

                self.status_label.text = fa(
                    "وضعیت: خطا"
                )

                return

            total_score += score * unit
            total_units += unit
            entered_courses += 1

        if entered_courses == 0:
            self.gpa_label.text = fa(
                "معدل: --"
            )

            self.units_label.text = fa(
                "حداقل یک نمره وارد کنید"
            )

            self.status_label.text = fa(
                "وضعیت: --"
            )

            return

        gpa = total_score / total_units

        self.gpa_label.text = fa(
            f"معدل: {gpa:.2f}"
        )

        self.units_label.text = fa(
            f"مجموع واحد: {total_units:g}"
        )

        if gpa > 17:
            self.status_label.text = fa(
                "وضعیت: عالی"
            )

            self.status_label.color = GOLD

        elif gpa >= 12:
            self.status_label.text = fa(
                "وضعیت: قبول"
            )

            self.status_label.color = GREEN

        else:
            self.status_label.text = fa(
                "وضعیت: مشروط"
            )

            self.status_label.color = RED


if __name__ == "__main__":
    GPAApp().run()
