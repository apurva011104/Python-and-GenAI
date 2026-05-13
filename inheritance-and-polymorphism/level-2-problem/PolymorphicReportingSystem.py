class Report:
    def generate(self):
        print("Generating report...")


class PDFReport(Report):
    def generate(self):
        print("Generating PDF report...")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel report...")


reports = [PDFReport(), ExcelReport()]

for r in reports:
    r.generate()
