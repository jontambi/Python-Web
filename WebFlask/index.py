from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/tech')

def tech():
    return render_template('tech.html')

@app.route('/project')

def project():
    return render_template('project.html')

@app.route('/blog')

def blog():
    return render_template('blog.html')

if __name__ == '__main__':
    app.run(debug=True)