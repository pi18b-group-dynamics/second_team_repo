from fpdf import FPDF


def simple_table(data, spacing=1):
    data = [('id', 'Имя', 'Фамилия', 'Отчество', 'Серия', 'Номер', 'Пол', 'Кто выдал', 'Дата выдачи', 'Фото'), ] + data
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 9)
    # col_width = 22
    size_column = (10, 20, 20, 20, 15, 20, 10, 25, 25, 15)
    row_height = pdf.font_size
    for row in data:
        for item, col_width in zip(row, size_column):
            pdf.cell(col_width, row_height * spacing,
                     txt=str(item), border=1)
        pdf.ln(row_height * spacing)

    pdf.output('simple_table.pdf')


if __name__ == '__main__':
    pass