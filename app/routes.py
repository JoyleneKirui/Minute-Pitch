import os
import secrets
from .email import mail_message
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm
from app.models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
 

@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(page=page,per_page=5)
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_photo(form_photo):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_photo.filename)
    photo_fn = random_hex + f_ext
    photo_path = os.path.join(app.root_path, 'static/photos', photo_fn)

    output_size = (125, 125)
    i = Image.open(form_photo)
    i.thumbnail(output_size)
    i.save(photo_path)

    return photo_fn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.photo.data:
            photo_file = save_photo(form.photo.data)
            current_user.image_file = photo_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.commit()
        flash('your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.bio.data = current_user.bio
    image_file = url_for('static', filename='photos/' + current_user.image_file)
    return render_template('account.html', title='Account', 
                            image_file=image_file, form=form)
  

@app.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')

@app.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

@app.route('/comment', methods=['GET', 'POST'])
@login_required
def comment(post_id):
    form = CommentForm()
    post = Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id=post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment=comment, user_id=user_id, post_id=post_id)
        new_comment.save_c()
        return redirect(url_for('comment', post_id=post_id))
    form = CommentForm()
    return render_template('comment.html', form=form, post=post, all_comments=all_comments)
