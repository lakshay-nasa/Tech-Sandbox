from odf import text, teletype
from odf.opendocument import load

def odt_to_latex(input_file, output_file):
    # Load the ODT file
    doc = load(input_file)

    # Extract the text from the document
    textdoc = []
    for para in doc.getElementsByType(text.P):
        textdoc.append(teletype.extractText(para))

    # Join the text into a single string
    textstr = "\n".join(textdoc)

    # Write the LaTeX code to the output file
    with open(output_file, "w") as f:
        f.write("\\documentclass{article}\n")
        f.write("\\usepackage[utf8]{inputenc}\n")
        f.write("\\begin{document}\n")
        f.write(textstr)
        f.write("\\end{document}")

# Example usage
odt_to_latex("input.odt", "output.tex")
