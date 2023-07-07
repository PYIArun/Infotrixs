app.route("/login", method=['POST'])
# def login():

#     if request.method == 'POST':
#         mydb = mysql.connector.connect(
#             host='localhost',
#             user= 'root',
#             password = "",
#             database = 'userdata'
#         )
#         cursor = mydb.cursor();
        
#         email = request.form('email')
#         password = request.form('password')

#         query = 'Select Email, Password from main where Email = "'+email+'" and Password = "'+password+'"; '
#         cursor.execute(query)
#         result = cursor.fetchone()
#         print(result[0])
#         print(result[1])
#         print(result[2])
#         print(result[3])
#         print(result[4])


#         # if result:
#         #     session['Email'] = result[1]



#         return render_template('profile.html')

#     return render_template("login.html")
