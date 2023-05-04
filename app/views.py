from flask import Flask, render_template, redirect, url_for, request, session, abort
from .session_interface import MySessionInterface
import time
app = Flask(__name__)
app.secret_key = b"?051k58484dserwsd__"  #verileri imzaladıktan sonra şifrelemek için kullandık
app.session_cookie_name = 'my_session_cookie'
app.session_interface = MySessionInterface() #kendi interfaceimizi belirttik
#kütüphaneleri import ettik ve


@app.route("/")
def Index():
      return render_template("index.html")

@app.route("/kayıtol")
def kayitol():
      return render_template("register.html")

@app.route("/success", methods=["POST"])
def success():
    return render_template("success.html"), 302, {'Refresh': '3; url=/'}

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/giris")
def giris():
      return render_template("login.html")
#post ve get metodu ile formdan veri çekme ve gönderme işlemi
@app.route('/login', methods=['GET', 'POST'])
def login():
      if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            if email == 'admin@gmail.com' and password == 'admin':
                  return redirect(url_for('success'))
            else:
                  return redirect(url_for('wrongusername'))
      return render_template('login.html')
#eğer kullanıcı giriş yaparsa ne olacak yapamazsa ne olacak diye belirledik.

@app.route('/newsletter' , methods=['POST'])
def newsletter():
    return render_template('newslettersuccess.html'), 302, {'Refresh': '3; url=/'}

@app.route('/wrongusername')
def wrongusername():
    return render_template('wrongusername.html'), 302, {'Refresh': '3; url=/giris'}

@app.route('/success', endpoint='success_page')
def success():
    return render_template('loginsuccess.html'), 302, {'Refresh': '3; url=/'} #302 kodu ile geçici yönlendirme yaparak 3 sn başka bir sayfada beklemesini sağladık

if __name__ == '__main__':
      app.run(debug=True)
