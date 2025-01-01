import pandas as pd
import glob
# glob is used to search files and paths
from fpdf import FPDF
from pathlib import Path
# pathlib is also used to read paths of files

filepaths = glob.glob("*.xlsx")
# it will search all the files with texts after *

for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")

    pdf = FPDF(orientation="P",unit="mm",format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    # Path(filepath).stem  it will read the stems of the files
    invoice_nr = filename.split("-")[0]
    date = filename.split("-")[1]

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8, txt=f"Invoice number.{invoice_nr}",ln=1)

    pdf.set_font(family="Times",size=16,style="B")
    pdf.cell(w=50,h=8, txt=f"Date-{date}",ln=1)

    columns = df.columns
    # df.columns shows all the columns of a file,whereas df.rows will show the rows under these columns
    columns = [item.replace("_"," ").title()for item in columns]
    pdf.set_font(family="Times",size=10)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index,row in df.iterrows():
        pdf.cell(w=30, h=8, txt=str(row["product_id"]),border=1)
        pdf.cell(w=70, h=8, txt=str(row["product_name"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]),border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]),border=1,ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times",size=10)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), border=1, ln=1)

    pdf.set_font(family="Times", size=10)
    pdf.cell(w=30,h=8,txt=f"The total price is {total_sum}",ln=1)

    pdf.set_font(family="Times", size=10,style="B")
    pdf.cell(w=25, h=8, txt="Narwal Building Material")
    pdf.image("pythonhow.png",  x=5, y=285, w=10)

    pdf.output(f"pdfs/{filename}.pdf")
    # if we put this outside the loop only the last file will get the changes not all the files