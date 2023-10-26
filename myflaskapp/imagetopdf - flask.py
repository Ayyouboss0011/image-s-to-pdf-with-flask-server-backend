from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
from PIL import Image

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('C:\\Users\\techn\\Downloads\\ilovepdf_pages-to-jpg\\myflaskapp\\static', filename))
        return convert_images_to_pdf(os.path.join('C:\\Users\\techn\\Downloads\\ilovepdf_pages-to-jpg\\myflaskapp\\static', filename), "output.pdf")
    
    return 'An error occurred'



def convert_images_to_pdf(image_file, output_file):
    image = Image.open(image_file)
    output_path = os.path.join('C:\\Users\\techn\\Downloads\\ilovepdf_pages-to-jpg\\myflaskapp\\static', output_file)

    image.save(output_path, "PDF", resolution=100.0)
    return send_file(output_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
