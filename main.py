
from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():

    # Set Header
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(10, 20, 200, 20)

    # Set Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    pdf.set_text_color(180,180,180)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # Set Footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
    pdf.set_text_color(180,180,180)

pdf.output("output.pdf")