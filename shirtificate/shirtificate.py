from fpdf import FPDF

def create_pdf(name):
    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    
    #titre
    pdf.set_font("Helvetica", size=12)
    pdf.cell(0, 20, txt="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT", ln=True)
    
    #image
    pdf.image("shirtificate.png", x=0, y=0, w=210, h=297)

    #text on the image
    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    
    
    pdf.set_xy(0, 150)  
    pdf.cell(0, 10, txt=f"{name} took CS50", align="C", new_x="LMARGIN", new_y="NEXT", ln=True)
    
    pdf.output("shirtificate.pdf")

def get_name():
    return input("Name: ")

def main():
    name = get_name()
    create_pdf(name)

if __name__ == "__main__":
    main()