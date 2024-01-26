from llama_index import download_loader
import pathlib as path


loader = download_loader("PDFReader")
data = loader.load_data(self=loader, file="analysis/Press_release.pdf")
