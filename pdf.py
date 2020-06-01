from fpdf import FPDF


def simple_table(spacing=1, data):
    data = [['Имя', 'Фамилия', 'Отчество', 'Серия', 'Номер', 'Пол', 'Кто выдал', 'Дата выдачи', 'Фото'],]

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 9)
    col_width = 22
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height * spacing,
                     txt=item, border=1)
        pdf.ln(row_height * spacing)

    pdf.output('simple_table.pdf')


if __name__ == '__main__':
    simple_table()