# pdf_generation.py

from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Podcast Summary Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def create_report(self, summary, output_file):
        self.add_page()
        self.chapter_title('Key Takeaways')
        self.chapter_body(summary['takeaways'])
        self.chapter_title('Quotes')
        self.chapter_body(summary['quotes'])
        self.output(output_file)

# Example usage
if __name__ == "__main__":
    report = PDFReport()
    summary = {
        'takeaways': 'The main takeaway from the episode is...',
        'quotes': '"This is a quote from the podcast."'
    }
    report.create_report(summary, 'podcast_summary.pdf')