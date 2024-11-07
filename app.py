from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath('database/offers.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "your_secret_key"
app.config['UPLOAD_FOLDER'] = 'static/images/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
db = SQLAlchemy(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Define the Offer model
class Offer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=False)
    amenities = db.Column(db.String(200), nullable=True)  
    pricing_period = db.Column(db.String(10), nullable=False, default='day')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'admin' and password == 'password':  # Replace with secure credentials
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash('Invalid credentials. Please try again.')
    
    return render_template('login.html')

# Route for logging out
@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    flash("You have been logged out.")
    return redirect(url_for('login'))

# Main Pages Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for displaying offers on the oferta.html page
@app.route('/oferta')
def show_offers():
    offers = Offer.query.all()
    return render_template('oferta.html', offers=offers)

# Route for the admin page
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        price = float(request.form['price'])
        image = request.files['image']
        amenities = request.form['amenities']
        pricing_period = request.form['pricing_period']

        # Save image file
        image_filename = None
        if image and allowed_file(image.filename):
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

        # Create and save the new offer
        new_offer = Offer(
            title=title,
            description=description,
            price=price,
            image=image_filename,
            amenities=amenities,
            pricing_period=pricing_period
        )
        db.session.add(new_offer)
        db.session.commit()
        flash("New offer added successfully!")
        return redirect(url_for('admin'))

    offers = Offer.query.all()
    return render_template('admin.html', offers=offers)

# Route to delete an offer
@app.route('/delete/<int:offer_id>', methods=['POST'])
def delete_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    db.session.delete(offer)
    db.session.commit()
    flash("Offer deleted successfully!")
    return redirect(url_for('admin'))

# Route to edit an offer
@app.route('/edit/<int:offer_id>', methods=['GET', 'POST'])
def edit_offer(offer_id):
    offer = Offer.query.get_or_404(offer_id)
    if request.method == 'POST':
        offer.title = request.form['title']
        offer.description = request.form['description']
        offer.price = float(request.form['price'])
        offer.amenities = request.form['amenities']
        offer.pricing_period = request.form['pricing_period']

        # Handle new image upload if provided
        new_image = request.files.get('new_image')
        if new_image and allowed_file(new_image.filename):
            # Save the new image
            image_filename = secure_filename(new_image.filename)
            new_image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            offer.image = image_filename  # Update the image path in the database

        db.session.commit()
        flash("Offer updated successfully!")
        return redirect(url_for('admin'))
    return render_template('edit_offer.html', offer=offer)

if __name__ == '__main__':
    app.run(debug=True)