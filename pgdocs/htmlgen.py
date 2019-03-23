"""
Generate docs in HTML format
"""

import markdown2
import mdgen


def generate(metadata):
    return markdown2.markdown(mdgen.generate(metadata), extras=["tables"])
