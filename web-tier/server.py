 
from flask import Flask, request
import boto3
from waitress import serve

app = Flask(__name__) #main app

s3connect = boto3.client('s3') #s3 connect code
s3bucket = "1234175958-in-bucket" #s3 bucket code
simpleDBconnect = boto3.client('sdb') #simpleDB connect
simpledomain = "1234175958-simpleDB" #simpleDB domain name
@app.route('/', methods=['POST']) #post requests to the root endpoint("/")
def project1p1():
    if 'inputFile' not in request.files:
        return "ERROR!"
    file = request.files['inputFile']
    filename = file.filename
    s3connect.upload_fileobj(file, s3bucket, filename)
    response = simpleDBconnect.get_attributes(
        DomainName = simpledomain,
        ItemName = filename,
        AttributeNames = ['classification']
    )
    if 'Attributes' in response:
         classification = response['Attributes'][0]['Value']
        return f"{filename}:{classification}"

if __name__ == '__main__':
    serve(app, host = '0.0.0.0', port = 8000, threads = 8) #port 8000
