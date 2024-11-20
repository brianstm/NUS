from fpdf import FPDF


def main():
    name = input("Enter your name: ")
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", ln=True)

    pdf.image("shirtificate.png", x=25, y=60, w=160)

    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)

    pdf.text(x=55, y=140, txt=f"{name} took CS50")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
