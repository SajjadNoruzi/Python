from pdfreader import PDFDocument, SimplePDFViewer

# get raw document
fd = open(file_name, "rb")
doc = PDFDocument(fd)

# there is an iterator for pages
page_one = next(doc.pages())
all_pages = [p for p in doc.pages()]

# and even a viewer
fd = open(file_name, "rb")
viewer = SimplePDFViewer(fd)