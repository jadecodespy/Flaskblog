
from flask import render_template
from application import app
from application.models import Posts
from application.forms import PostsForms



@app.route('/')
@app.route('/home')
def home():
    all_posts = Posts.query.all()
    return render_template('home.html', title='Home', posts=all_posts)



@app.route('/about')
def about():
    return render_template('about.html' , title="About" , desc="This is about blogs")



@app.route('/login')
def login():
    return render_template('login.html' , title="Login" , desc= "This is the login page")


@app.route('/register')
def register():
    return render_template('register.html' , title="Register" , desc= "This is the registration page")

@app.route('/post', methods=['GET', 'POST'])
def post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Posts(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            title = form.title.data,
            content = form.content.data
        )

        db.session.add(postData)
        db.session.commit()

        return redirect(url_for('home'))

    else:
        print(form.errors)

    return render_template('post.html', title='Post', form=for
