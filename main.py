import flet as ft
from docx2pdf import convert

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تحويل Word إلى PDF"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.colors.BLUE_GREY_100  # لون خلفية الصفحة
    page.padding = 20

    # دالة تُنفذ عند النقر على الزر
    def convert_to_pdf(e):
        if not file_path.value:
            file_path.error_text = "الرجاء تحديد ملف Word!"
            page.update()
        else:
            try:
                # تحويل الملف
                output_file = file_path.value.replace(".docx", ".pdf")
                convert(file_path.value, output_file)
                page.clean()  # مسح المحتوى الحالي
                page.add(
                    ft.Column(
                        [
                            ft.Text(
                                value=f"تم تحويل الملف إلى PDF بنجاح!",
                                size=30,
                                weight="bold",
                                color=ft.colors.GREEN_900,
                            ),
                            ft.Text(
                                value=f"تم حفظ الملف كـ: {output_file}",
                                size=18,
                                color=ft.colors.BLUE_800,
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
            except Exception as ex:
                page.clean()
                page.add(
                    ft.Text(
                        value=f"حدث خطأ أثناء التحويل: {ex}",
                        size=20,
                        color=ft.colors.RED_900,
                    )
                )

    # حقل إدخال مسار الملف
    file_path = ft.TextField(
        label="أدخل مسار ملف Word",
        width=400,
        height=50,
        border_color=ft.colors.BLUE_700,
        text_size=18,
        color=ft.colors.BLUE_900,
    )

    # الزر
    convert_button = ft.ElevatedButton(
        text="تحويل إلى PDF",
        on_click=convert_to_pdf,
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        width=200,
        height=50,
    )

    # إضافة العناصر إلى الصفحة
    page.add(
        ft.Column(
            [
                ft.Text(
                    value="تحويل ملف Word إلى PDF",
                    size=30,
                    weight="bold",
                    color=ft.colors.BLUE_900,
                ),
                ft.Text(
                    value="أدخل مسار ملف Word واضغط على الزر لتحويله إلى PDF.",
                    size=18,
                    color=ft.colors.BLUE_800,
                ),
                file_path,
                convert_button,
            ],
            alignment="center",
            spacing=20,
        )
    )

# تشغيل التطبيق
ft.app(target=main)