import os

from  flask import  Flask,render_template,request,flash,redirect,url_for
import mysql.connector
import os

app=Flask(__name__)
app.secret_key=os.urandom(25)
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  db="client"
)



@app.route("/")
def indexPage():
    cur=mydb.cursor()
    cur.execute("select * from  customer ORDER BY RAND() LIMIT 1 ")
    show=cur.fetchall()

    return render_template("index.html",show=show)



@app.route("/PageHome",methods=["Post"])
def PageHome():
    name=request.form["FirstName"]
    lastName=request.form["LastName"]
    Email=request.form["Email"]


    if(name=="") :
        flash("Enter your Name",category='Name')
        return redirect(url_for('indexPage'))


    if (lastName == ""):
        flash("Enter your LastName ",category='LastName')
        return redirect(url_for('indexPage'))
    if (Email=="" ):
        flash("Enter your Email",category='Email')
        return redirect(url_for('indexPage'))

    cur=mydb.cursor()
    cur.execute('insert into customer(FirstName, LastName,Email) values(%s,%s,%s) ',
                   (name,lastName,Email))
    mydb.commit()

    return redirect(url_for('indexPage'))


if __name__=='__main__':
    app.run(debug=True)