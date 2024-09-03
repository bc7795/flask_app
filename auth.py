from flask import Blueprint , render_template ,request ,flash
auths=Blueprint('auth',__name__)
@auths.route('/login',methods=['GET','POST'])
def login():
    return render_template("login.html")
@auths.route("/logout")
def logout():
    return "<p>logout<p>"
@auths.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        if len(email)<=4:
            flash('email must be more than 4 charecters.',category='error')
        elif len(firstName)==0:
            flash('enter first name',category='error')
        elif len(password1)<=2:
            flash('password must be more than 2 charecters',category='error')
        elif password2!=password1:
            flash('please enter the correct password',category='error')
        else:
            flash('account created succesfully',category='success')
    return render_template("sign-up.html")

