import flet as ft
from docx2pdf import convert

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تحويل Word إلى PDF"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.bgcolor = ft.colors.BLUE_GREY_100  # لون خلفية الصفحة
    page.padding = 20

    # متغير لتخزين مسار الملف المحدد
    selected_file_path = None

    # دالة تُنفذ عند اختيار ملف
    def on_file_selected(e: ft.FilePickerResultEvent):
        nonlocal selected_file_path
        if e.files:
            selected_file_path = e.files[0].path
            file_name.value = f"تم اختيار الملف: {e.files[0].name}"
            file_name.update()
        else:
            selected_file_path = None
            file_name.value = "لم يتم اختيار أي ملف."
            file_name.update()

    # دالة تُنفذ عند النقر على الزر
    def convert_to_pdf(e):
        if not selected_file_path:
            file_name.error_text = "الرجاء اختيار ملف Word!"
            page.update()
        else:
            try:
                # تحويل الملف
                output_file = selected_file_path.replace(".docx", ".pdf")
                convert(selected_file_path, output_file)
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

    # عنصر FilePicker لاختيار الملف
    file_picker = ft.FilePicker(on_result=on_file_selected)
    page.overlay.append(file_picker)  # إضافة FilePicker إلى الصفحة

    # نص لعرض اسم الملف المحدد
    file_name = ft.Text(
        value="لم يتم اختيار أي ملف.",
        size=18,
        color=ft.colors.BLUE_800,
    )

    # الزر لفتح نافذة اختيار الملف
    pick_file_button = ft.ElevatedButton(
        text="اختر ملف Word",
        on_click=lambda _: file_picker.pick_files(
            allowed_extensions=["docx"],  # السماح باختيار ملفات Word فقط
            dialog_title="اختر ملف Word",
        ),
        bgcolor=ft.colors.BLUE_700,
        color=ft.colors.WHITE,
        width=200,
        height=50,
    )

    # الزر لتحويل الملف
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
                    value="اختر ملف Word واضغط على الزر لتحويله إلى PDF.",
                    size=18,
                    color=ft.colors.BLUE_800,
                ),
                pick_file_button,
                file_name,
                convert_button,
            ],
            alignment="center",
            spacing=20,
        )
    )

# تشغيل التطبيق
ft.app(target=main)