from flask import Flask, request, escape
from datetime import datetime
from random import randint


app = Flask(__name__)


@app.route('/')
def main():
    return"""
<html lang="en">
    <head>
        <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
            crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="../static/main.css">
        <style>
        .header{
        background-color: #FB6D3A;
        }
        .my_projects_list{
            
            font-size: 20px;
            line-height: 25px;
            color: #000;
        }
        body{
        background-color: #565E6A;
        }
        </style>
        <title>Homework Flask:</title>
    </head>
    <body>
    <div class="homework section">
        <h1 class="header">Homework:</h1>
        <ol class="my_projects_list">
        №1: <a href="/whoami/" class=home_project>whoami</a><br /> 
        №2: <a href="/source_code/" class=home_project>source_code</a><br /> 
        №3: <a href="/random/?length=42&specials=1&digits=0"class=home_project>random</a><br />
        </ol>
    </div>             
    </body>
</html>

"""


@app.route('/whoami/')
def whoami():
    ip_address: str = str(request.remote_addr)
    user_browser: str = str(request.headers.get('User-Agent'))
    server_time: str = str(datetime.now().strftime('%H:%M:%S'))
    return f"""
<html lang="en">
    <head>
        <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
            crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="../static/main.css">
        <style>
        .header{{
        background-color: #FB6D3A;
        }}
        .my_projects_list{{
            
            font-size: 20px;
            line-height: 25px;
            color: #000;
        }}
        body{{
        background-color: #565E6A;
        }}
        .values{{
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 25px;
        color: #A8A8A8;
        margin: 10 10 10px 10;
        }}
        
        </style>
        <title>Homework Flask:</title>
    </head>
    <body>
    <div class="homework section">
        <h1 class="header">Homework:</h1>
        <ol class="my_projects_list">
        <h5 class="values"> IP adress: {ip_address}</h5>
        <h5 class="values"> Browser: {user_browser}</h5>
        <h5 class="values"> Time: {server_time}</h5>  
        </ol>
    </div>             
    </body>
</html>
"""


@app.route('/source_code/')
def source_code():
    with open('./flask_application.py', "r") as file:
        open_file = file.readlines()
    text_file = escape(''.join(open_file))
    return f"""
<html lang="en">
    <head>
        <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
            crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="../static/main.css">
        <style>
        .header{{
        background-color: #FB6D3A;
        }}
        .my_projects_list{{
            
            font-size: 20px;
            line-height: 25px;
            color: #000;
        }}
        body{{
        background-color: #565E6A;
        }}
        .values{{
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 25px;
        color: #A8A8A8;
        margin: 10 10 10px 10;
        }}
        
        </style>
        <title>Homework Flask:</title>
    </head>
    <body>
    <div class="homework section">
        <h1 class="header">Homework:</h1>
        <ol class="my_projects_list">
        <h5 class="values"> Show code: {text_file}</h5>
    </ol>
    </div>             
    </body>
</html>
"""


@app.route('/random/')
def random():
    result: str = 'ERROR: Length out of range!'
    try:
        length: int = int(request.values.get('length', 0))
    except Exception:
        length = 0

    try:
        specials: int = int(request.values.get('specials', 0))
    except Exception:
        specials = 0

    try:
        digits: int = int(request.values.get('digits', 0))
    except Exception:
        digits = 0

    if 0 < length <= 100:
        result = ''
        length_sym: str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        specials_sym: str = '!"№;%:?*()_+'
        digits_num: str = '0123456789'

        if specials != 0:
            specials = 1
            length_sym += specials_sym

        if digits != 0:
            digits = 1
            length_sym += digits_num

        for i in range(length):
            result += length_sym[randint(0, len(length_sym)-1)]
    return f"""
<html lang="en">
    <head>
        <link rel="stylesheet"
            href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
            integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
            crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="../static/main.css">
        <style>
        .header{{
        background-color: #FB6D3A;
        }}
        .my_projects_list{{
            
            font-size: 20px;
            line-height: 25px;
            color: #000;
        }}
        body{{
        background-color: #565E6A;
        }}
        .values{{
        font-style: normal;
        font-weight: bold;
        font-size: 20px;
        line-height: 25px;
        color: #A8A8A8;
        margin: 10 10 10px 10;
        }}
        .my_work{{
        font-style: normal;
        font-weight: bold;
        font-size: 22px;
        line-height: 27px;
        color: white;
        margin-bottom: 10px;
        }}
        
        </style>
        <title>Homework Flask:</title>
    </head>
    <body>
    <div class="homework section">
        <h1 class="header">Homework:</h1>
        <ol class="my_projects_list">
        <li class="my_work">Length: {length};</li>
        <li class="my_work">Specials: {bool(specials)};</li>
        <li class="my_work">Digits: {bool(digits)};</li>
        <li class="my_work">Result: {result};</li>
    </ol>
    </div>             
    </body>
</html>
"""


app.run(debug=True, host='0.0.0.0')
