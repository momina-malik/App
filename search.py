from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        artisans = Artisan.query.filter(Artisan.name.like('%' + query + '%')).all()
        crafts = Craft.query.filter(Craft.name.like('%' + query + '%')).all()
        societies = Society.query.filter(Society.name.like('%' + query + '%')).all()
        return render_template('search_results.html', artisans=artisans, crafts=crafts, societies=societies)
    return render_template('search.html')

if __name__ == '__main__':
    app.run(debug=True)