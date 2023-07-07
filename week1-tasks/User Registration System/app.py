from flask import Flask, render_template, url_for, request, session, redirect
import mysql.connector
import bcrypt

app = Flask(__name__)
app.secret_key = 'Arun_Chandra'


@app.route("/", methods= ['GET','POST'])
def register():

    if request.method == 'POST':
    
        mydb = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password = "",
            database = 'userdata'
        )

        firstname = request.form['first-name']
        lastname = request.form['last-name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        hashed_password_str = hashed_password.decode('utf-8')
        cursor = mydb.cursor();

        cursor.execute('Insert into main(FirstName, LastName, Email, Phone, Password) values ("'+firstname+'","'+lastname+'","'+email+'","'+phone+'","'+hashed_password_str+'");')
        mydb.commit()
        cursor.close()
        flag = True
        return render_template("register.html", flag= flag)

    return render_template("register.html")


@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        mydb = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password = "",
            database = 'userdata'
        )
        cursor = mydb.cursor();
        
        email = request.form['email']
        password = request.form['password']

        query = 'Select Email, Password from main where Email = "'+email+'" ;'
        cursor.execute(query)
        result = cursor.fetchone()

        retrieved_hashedpw = bytes(result[1])

        if result:
            if bcrypt.hashpw(password.encode('utf-8'), retrieved_hashedpw):
                session['Email'] = result[0]
                cursor.close()
                return redirect('/profile')
        
        cursor.close()
        flag = True
        return render_template('login.html', flag = flag)

    return render_template("login.html")

@app.route("/profile", methods=['GET', 'POST'])
def manageProfile():
    if 'Email' in session:
        email = session['Email']
        
        mydb = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password = "",
            database = 'userdata'
        )
        cursor = mydb.cursor();
        
        query = 'Select FirstName, LastName, Email, Phone from main where Email = "'+email+'";'
        cursor.execute(query)
        result = cursor.fetchone()

        if request.method == 'POST':
            newFirstName = request.form['firstName']
            newLastName = request.form['lastName']
            # newEmail = request.form['email']
            newPhone = request.form['phone']
            newPassword = request.form['password']

            hash_pw = bcrypt.hashpw(newPassword.encode('utf-8'), bcrypt.gensalt())
            hash_pw_str = hash_pw.decode('utf-8')

            # if newEmail != session['Email']:
            #     session['flag'] = True
            #     return redirect('/profile')
            # else:
            #     session['flag'] = False

            cursor.execute('update main set FirstName = "'+newFirstName+'" where Email = "'+email+'"')
            cursor.execute('update main set LastName = "'+newLastName+'" where Email = "'+email+'"')
            cursor.execute('update main set Phone = "'+newPhone+'" where Email = "'+email+'"')
            cursor.execute('update main set Password = "'+hash_pw_str+'" where Email = "'+email+'"')
            # cursor.execute('update main set Email = "'+newEmail+'" where Email = "'+email+'"')
            # session['Email'] = newEmail;
            mydb.commit()
            cursor.execute('Select FirstName, LastName, Email, Phone from main where Email = "'+session['Email']+'"')
            result = cursor.fetchone()
            cursor.close()
            flag= True
            return render_template('profile.html', result = result, flag=True)
        
        cursor.close()
        return render_template('profile.html', result = result)

    return redirect('/login')


@app.route('/logout')
def logout():
    session.clear()

    return redirect('/login')


app.run(debug=True)
