import sys

from askhub.models import Post, PostType
from askhub.database import init_db, db_session
from askhub.forms import AskForm, AnswerForm

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import desc


app = Flask(__name__)
app.config.update(
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)
csrf = CSRFProtect(app)


@app.route('/')
def index():
    posts = Post.query.filter_by(parent_id=None).order_by(Post.created_at).all()

    return render_template('index.html', posts=posts)


@app.route('/question/<int:post_id>', methods=['GET', 'POST'])
def question(post_id):
    form = AnswerForm(request.form)

    if request.method == 'POST' and form.validate():
        post = Post(parent_id=post_id, body=form.body.data, type_id=PostType.ANSWER)

        db_session.add(post)
        db_session.commit()

        return redirect(url_for('question', post_id=post_id))

    post = Post.query.filter_by(id=post_id).first()
    answers = Post.query.filter_by(parent_id=post_id).order_by(desc(Post.created_at)).all()

    return render_template('question.html',
                           post=post,
                           form=form,
                           answers=answers)


@app.route('/ask', methods=['GET', 'POST'])
def ask():
    form = AskForm(request.form)

    if request.method == 'POST' and form.validate():
        post = Post(title=form.title.data,
                    body=form.body.data)

        db_session.add(post)
        db_session.commit()

        return redirect(url_for('question', post_id=post.id))

    return render_template('ask.html', form=form)


if __name__ == '__main__':
    if 1 < len(sys.argv) and sys.argv[1] == "--init-db":
        init_db()
        exit()

    app.run()
