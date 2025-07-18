from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
profiles = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    bio = request.form['bio']
    skills = request.form['skills']
    profiles[name] = {
        'bio': bio,
        'skills': [skill.strip() for skill in skills.split(',')]
    }
    return redirect(url_for('profile', name=name))

@app.route('/profile/<name>')
def profile(name):
    if name not in profiles:
        return "Profile not found", 404
    data = profiles[name]
    return render_template('profile.html', name=name, bio=data['bio'], skills=data['skills'])

if __name__ == '__main__':
    app.run(debug=True)
