from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import openai
from PyPDF2 import PdfFileReader
from io import BytesIO

app = Flask(__name__)
cors=CORS(app)

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
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        messages=[
            {'role':'system','content':'Answer questions only related to the document. If questions about topics unrelated to the topic are asked respond by saying "Sorry, the question you asked is not related to the document. Please ask questions related to the document."'},
            {'role':'user','content':document_text},
            {'role':'user','content':prompt}
        ]
    )
    answer = response.choices[0].text.strip()
    return answer


@app.route('/api', methods=['POST'])
@cross_origin()
def process_prompt():
    prompt = request.form.get('prompt')
    file = request.files.get('file')
    
    if file:
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


