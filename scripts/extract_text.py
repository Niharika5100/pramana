import pymupdf

pdf = "data/documents/pdf1.pdf"
doc = pymupdf.open(pdf)

for page in doc:
    text = page.get_text("blocks")
    print(text)
