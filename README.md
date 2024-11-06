# Set Tour Website

Welcome to the **Set Tour** travel agency website project! This is a web-based application built with Flask and SQLite that allows an admin to manage travel offers and users to view available offers. The site includes pages like Home, About, Contact, and Offers, all styled with HTML and CSS.

## Features

- **Admin Dashboard**: Allows the admin to add, edit, and delete travel offers.
- **Offers Page**: Displays a list of available travel offers to visitors.
- **Authentication**: Simple login system for admin access.
- **Responsive Design**: Adapts to different screen sizes for optimal viewing.
- **File Uploads**: Allows the admin to upload images for each travel offer.

## Technologies Used

- **Backend**: Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with basic animations and layout

## Project Structure

```plaintext
project-directory/
│
├── app.py               # Main application file
├── database/
│   └── offers.db        # SQLite database for storing offers
├── static/
│   ├── css/
│   │   └── style.css    # Main CSS file for styling
│   ├── images/          # Folder for static images and uploaded offers images
│   └── js/
│       └── script.js    # (Optional) JavaScript file if needed
└── templates/
    ├── index.html       # Homepage
    ├── about.html       # About page
    ├── contact.html     # Contact page
    ├── mainoffer.html   # Main offers overview
    ├── oferta.html      # Offers listing page
    ├── admin.html       # Admin dashboard for managing offers
    └── edit_offer.html  # Edit page for updating an existing offer
```

## Getting Started

### Prerequisites

- **Python 3.x**
- **Flask** and **Flask_SQLAlchemy** libraries

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/luckasz02/setourwebsite.git
   cd setourwebsite
   ```

2. **Set up a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Create the database**:

   Open a Python shell or use the command line:

   ```bash
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

5. **Run the server**:

   ```bash
   python app.py
   ```

6. **Access the site**:

   Open your browser and go to `http://127.0.0.1:5000`.

### Usage

1. **Admin Login**: Go to `http://127.0.0.1:5000/login` and log in as the admin.
2. **Manage Offers**: Add, edit, or delete offers from the admin dashboard.
3. **View Offers**: The public can view all available offers on the `oferta.html` page.

## License

Proprietary License - This project is the exclusive property of Set Tour Travel Agency. All rights reserved. No part of this project may be used, distributed, modified, or copied without explicit permission.

## Contact

For questions or feedback, please contact **Set Tour Travel Agency** at `lucadumitru02@gmail.com`.
