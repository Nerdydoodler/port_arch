from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Email
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

db = SQLAlchemy(app)

# Models
class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(300), nullable=False)
    client = db.Column(db.String(100))
    year = db.Column(db.Integer)
    featured = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    logo_url = db.Column(db.String(300))
    category = db.Column(db.String(50))  # Entertainment, Publishing, etc.
    website_url = db.Column(db.String(300))

class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class MailingList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Forms
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])

class MailingListForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])

# Routes
@app.route('/')
def index():
    featured_artworks = Artwork.query.filter_by(featured=True).limit(6).all()
    return render_template('index.html', artworks=featured_artworks)

@app.route('/work')
def work():
    category = request.args.get('category', 'all')
    if category == 'all':
        artworks = Artwork.query.all()
    else:
        artworks = Artwork.query.filter_by(category=category).all()
    
    categories = db.session.query(Artwork.category).distinct().all()
    categories = [cat[0] for cat in categories]
    
    return render_template('work.html', artworks=artworks, categories=categories, current_category=category)

@app.route('/concept-art')
def concept_art():
    artworks = Artwork.query.filter_by(category='concept-art').all()
    return render_template('gallery.html', artworks=artworks, title='Concept Art')

@app.route('/illustration')
def illustration():
    artworks = Artwork.query.filter_by(category='illustration').all()
    return render_template('gallery.html', artworks=artworks, title='Illustration')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form)

@app.route('/mailing-list', methods=['POST'])
def mailing_list():
    form = MailingListForm()
    if form.validate_on_submit():
        subscriber = MailingList(email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('Thank you for joining our mailing list!', 'success')
        return redirect(url_for('index'))
    
    flash('Please enter a valid email address.', 'error')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    clients = Client.query.all()
    return render_template('about.html', clients=clients)

@app.route('/api/artwork/<int:artwork_id>')
def get_artwork(artwork_id):
    artwork = Artwork.query.get_or_404(artwork_id)
    return jsonify({
        'id': artwork.id,
        'title': artwork.title,
        'description': artwork.description,
        'image_url': artwork.image_url,
        'client': artwork.client,
        'year': artwork.year,
        'category': artwork.category
    })

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
