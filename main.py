# Import necessary libraries
import os
import subprocess

def convert_djvu_to_pdf(input_djvu, output_pdf):
    try:
        # Check if input DJVU file exists
        if not os.path.exists(input_djvu):
            raise FileNotFoundError(f"The file {input_djvu} does not exist.")

        # Use DjVuLibre's `ddjvu` command line tool to convert DJVU to PNM format
        pnm_filename = output_pdf.replace(".pdf", ".pnm")
        subprocess.run(["/opt/homebrew/bin/ddjvu", "-format=pnm", input_djvu, pnm_filename])

        # Check if PNM file was created successfully
        if not os.path.exists(pnm_filename):
            raise Exception("Conversion to PNM failed.")

        # Use ImageMagick's `convert` command line tool to convert PNM to PDF
        subprocess.run(["/opt/homebrew/bin/convert", pnm_filename, output_pdf])

        # Check if PDF file was created successfully
        if not os.path.exists(output_pdf):
            raise Exception("Conversion to PDF failed.")

        # Clean up intermediate PNM file
        os.remove(pnm_filename)

        print(f"Conversion successful. PDF saved as {output_pdf}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_djvu_file = "RL.djvu"
output_pdf_file = "RL.pdf"
convert_djvu_to_pdf(input_djvu_file, output_pdf_file)

