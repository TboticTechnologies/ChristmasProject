from postmarker.core import PostmarkClient
import requests
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    name = ""
    email = ""
    message = ""
    if request.form == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
    return render_template('index.html')


postmark = PostmarkClient(server_token='29d9b643-488c-4cec-8f1b-ff5f7f019733')
postmark.emails.send(
  From=email,
  To='lsaner720@west-mec.org',
  Subject='Gift',
  HtmlBody='message'
)

if __name__ == '__main__':
    app.run(debug=True)