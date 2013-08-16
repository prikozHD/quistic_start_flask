#encoding: utf-8
from flask import Flask, request, url_for, render_template

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/user/<user_name>/')
def user_name(user_name):
    return "User: %s" % user_name


@app.route('/news/<slug>/')
def news_id(slug):
    try:
        slug = str(slug)
        print url_for('static', filename='style.css')
        return "News slug = %s " % slug
    except ValueError:
        return '404'


@app.route('/post/<int:id>')
def show_post(id):
    return "POST id: %s" % id


@app.errorhandler(404)
def page_not_found(e):
    app.logger.debug('e = %s' % e)
    return 'Page not found'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
