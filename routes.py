from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.forms import LoginForm, RegisterForm
from app.models import User, Artisan, Craft, Society

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/feed')
@login_required
def feed():
    # code for feed page
    pass

@app.route('/product/<int:product_id>')
@login_required
def product(product_id):
    # code for product page
    pass

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post = get_post(post_id)
    if post is None:
        abort(404)
    if request.method == 'POST':
        # update post logic here
        pass
    return render_template('edit.html', post=post)

@app.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        artisan_id = request.form['artisan_id']
        product = Product(name=name, description=description, price=price, artisan_id=artisan_id)
        db.session.add(product)
        db.session.commit()
        flash('Product created successfully!')
        return redirect(url_for('index'))
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)