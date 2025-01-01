# day26,student project,those text files also refers to this
from pathlib import Path
from fpdf import FPDF
import glob
import pandas as pd

filepaths = glob.glob("Current+Source+Code/files/*.txt")

pdf = FPDF(orientation="P",unit="mm",format="A4")


for filepath in filepaths:
    df=pd.read_csv(filepath)
    with open(filepath, 'r') as file:
        file_content = file.read()
    pdf.add_page()

    filename = Path(filepath).stem
    name=filename.title()

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=20,h=10,txt=name,ln=1)

    pdf.set_font(family="Times",size=8)
    pdf.multi_cell(w=0,h=7,txt=file_content)


pdf.output("output.pdf")