from flask import Flask,render_template,request
from python_employee import xmltojson,SortByName

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('employee.html')

@app.route('/employee',methods=['GET'])
def get():
    return xmltojson.homerun()

@app.route('/sort',methods=['GET'])
def sort():
    sortKey=request.args.get('sortby').lower().replace(" ","")
    return SortByName.sortFirst(sortKey)

if __name__=='__main__':
    app.run(debug=True)
