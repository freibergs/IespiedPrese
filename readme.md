# 🛠️ IespiedPrese.lv Project

Welcome to the IespiedPrese.lv project! This is a Flask-based web application that allows users to browse and download various themes and plugins. The application also supports user authentication, cron jobs for product and user updates, subscription plans, history tracking, and more.

## 🚀 Installation

To run this project locally, follow these steps:

1. Clone the repository:  
   git clone https://github.com/freibergs/IespiedPrese.lv.git

2. Navigate to the project directory: 
   cd iespiedprese

3. Create and activate a virtual environment:  
   python -m venv venv  
   source venv/bin/activate  # MacOS/Linux  
   .\venv\Scripts\activate  # Windows

4. Install the required dependencies:  
   pip install -r requirements.txt

5. Create a `.env` file in the project root directory and add your environment variables:  
   COOKIE=[Page cookie]  
   HOST=[Plugin and theme repository]  
   SITEMAP_URLS=[Repository sitemaps, comma-separated]  
   USER_AGENT=Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0  
   STRIPE_KEY=[Stripe test/live key]  
   SECRET_KEY=[Any key/password]  
   PORT=[80 or 443]  
   DEBUG=[True or False]  
   DATABASE_URL=[Full postgres link]  
   BUCKETEER_AWS_ACCESS_KEY_ID=  
   BUCKETEER_AWS_SECRET_ACCESS_KEY=  
   BUCKETEER_AWS_REGION=eu-west-1  
   BUCKETEER_BUCKET_NAME=  
   CACHE_AGE=[Days, e.g., 365]  
   GA_MEASUREMENT_ID=[Google Analytics ID]  
   SPECIFIC_PATH=[Page to load GTag - '/' or '' means all pages]  

7. Use scripts to fetch initial data:  
   python cron_scripts\full_update.py  
   python cron_scripts\download_images.py

6. Launch the application:  
   python iespiedprese.py

## 📜 Licence

This project is licensed under the [MIT Licence](LICENSE.md).

## 📞 Kontakti

If you have any questions or suggestions, please contact me at hello@rihards.dev. More contact information can be found at https://rihards.dev.

Happy WordPressing! 😊
