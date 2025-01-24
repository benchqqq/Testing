import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تطبيق متقدم"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.colors.BLUE_GREY_100  # لون خلفية الصفحة
    page.padding = 20

    # دالة تُنفذ عند النقر على الزر
    def say_hello(e):
        if not name_input.value:
            name_input.error_text = "الرجاء إدخال اسمك!"
            page.update()
        else:
            page.clean()  # مسح المحتوى الحالي
            page.add(
                ft.Column(
                    [
                        ft.Text(
                            value=f"مرحبًا، {name_input.value}!",
                            size=40,
                            weight="bold",
                            color=ft.colors.BLUE_900,
                        ),
                        ft.ElevatedButton(
                            text="العودة",
                            on_click=lambda e: page.go("/"),  # العودة إلى الصفحة الرئيسية
                            bgcolor=ft.colors.BLUE_700,
                            color=ft.colors.WHITE,
                        ),
                    ],
                    alignment="center",
                    spacing=20,
                )
            )

    # حقل إدخال النص
    name_input = ft.TextField(
        label="أدخل اسمك",
        width=300,
        height=50,
        border_color=ft.colors.BLUE_700,
        text_size=18,
        color=ft.colors.BLUE_900,
    )

    # الزر
    submit_button = ft.ElevatedButton(
        text="تقديم",
        on_click=say_hello,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        width=150,
        height=50,
    )

    # إضافة العناصر إلى الصفحة
    page.add(
        ft.Column(
            [
                ft.Text(
                    value="مرحبًا بك في تطبيقنا!",
                    size=30,
                    weight="bold",
                    color=ft.colors.BLUE_900,
                ),
                ft.Text(
                    value="أدخل اسمك واضغط على الزر لترى التحية.",
                    size=18,
                    color=ft.colors.BLUE_800,
                ),
                name_input,
                submit_button,
            ],
            alignment="center",
            spacing=20,
        )
    )

# تشغيل التطبيق
ft.app(target=main)