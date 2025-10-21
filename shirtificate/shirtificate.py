from fpdf import FPDF

class p(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")
    shirt(name)


def shirt(name):
    pdf = p()
    pdf.add_page(orientation="portrait")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{name} took CS50P", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
