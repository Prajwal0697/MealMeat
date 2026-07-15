# MealMate

MealMate is a Django-based food delivery web application built with a custom `delivery` app. It allows customers to sign up, sign in, view restaurants, browse restaurant menus, add items to a cart, and complete checkout.

## Features

- Custom user signup and signin using a `Customer` model
- Restaurant listing page
- Menu pages for each restaurant
- Add to cart and cart overview
- Checkout flow using Razorpay SDK credentials from settings
- Admin home and restaurant management pages

## Project Structure

- `delivery/` - Django app containing models, views, templates, static files, and URLs
- `delivery/templates/delivery/` - HTML templates for signup, signin, restaurant list, cart, checkout, and failure pages
- `delivery/static/delivery/style.css` - shared styles for the app
- `meal_buddy/` - Django project configuration and settings
- `manage.py` - Django command line utility
- `requirements.txt` - Python dependencies

## Screenshots

Include screenshots in your GitHub repo by adding them to a folder such as `screenshots/` and referencing them here. Example:

- `screenshots/homepage.png`
- `screenshots/signup.png`
- `screenshots/customer_home.png`

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Prajwal0697/MealMeat.git
   cd MealMeat
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
5. Open the site:
   ```
   http://127.0.0.1:8000/
   ```

## Notes

- The app uses plain text password storage in the custom `Customer` model. This is not secure for production.
- To add screenshots, create a `screenshots/` folder and place image files there.
- The project currently uses `DEBUG = True` in settings for local development.
