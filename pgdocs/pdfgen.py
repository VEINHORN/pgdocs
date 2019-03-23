"""
Generate docs in PDF format
"""

import htmlgen
from xhtml2pdf import pisa


def generate(metadata):
    html = htmlgen.generate(metadata)

    with open("docs.pdf", "w+b") as outfile:
        pisa.CreatePDF(
            html, dest=outfile
        )
