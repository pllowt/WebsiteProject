from root import app,db
from root.models import User
from root.forms import LoginForm
from flask import render_template,request,url_for,flash,redirect,abort
from flask_login import login_user,logout_user,login_required


@app.route('/',methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    # Check form has been submitted
    if form.validate_on_submit():
        # Read database for username and choose first as username is unique. Will be None if not found.
        user = User.query.filter_by(username=form.username.data).first()
        # Check password is correct and username exists
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            
            next = request.args.get('next')
            
            if next == None: #or not next[0]=='/'
                flash('Login failed!')
                next = url_for('signin')
                
            return redirect(next)
    return render_template('signin.html',form=form)

@app.route('/home')
@login_required
def main():
    return render_template('home.html')

@app.route('/logout')
@login_required
def Logout():
    logout_user()
    flash('Successfully logged out')
    return redirect(url_for('signin'))

if __name__ == '__main__':
    app.run(debug=True)