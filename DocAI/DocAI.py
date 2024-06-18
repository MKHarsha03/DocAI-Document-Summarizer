from flask import Flask, request, jsonify
import os
import openai
from PyPDF2 import PdfFileReader
from io import BytesIO

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

def extract_text_from_pdf(file):
    pdf_reader = PdfFileReader(BytesIO(file.read()))
    text = ""
    for page_num in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

def ask_openai(prompt, document_text):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=f"Document: {document_text}\n\nQuestion: {prompt}\nAnswer:",
    )
    answer = response.choices[0].text.strip()
    return answer

@app.route('/api/process_prompt', methods=['POST'])
def process_prompt():
    prompt = request.form.get('prompt')
    file = request.files.get('file')
    
    if file:
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        
        # Extract text from the uploaded PDF file
        document_text = extract_text_from_pdf(file)
        
        # Get the response from OpenAI
        response_message = ask_openai(prompt, document_text)
    else:
        response_message = "Please upload a document to get an answer."
    
    return jsonify({"message": response_message})

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
