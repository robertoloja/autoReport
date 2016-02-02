from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Title', 0)
p = document.add_paragraph('Things and such \n')
p.add_run('another thing').bold = True
document.add_page_break()

document.save('thing.docx')
