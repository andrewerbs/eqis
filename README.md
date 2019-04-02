# myeqip-portal
The official web portal for the Myanmar Education Quality Improvement Program, built on [Wagtail](www.wagtail.io).



## Setup

1. Clone the "myeqip-portal" repository:

   ```bash
   git clone https://github.com/catalpainternational/myeqip-portal.git
   ```

2. Create a Python virtual envionment. myeqip-portal uses Python 3:

   ```bash
   python3 -m venv virtualenv
   ```

3. myeqip-portal installs necessary Python packages from `requirements.txt`. Install packages with:

   ```
   pip install -r requirements.txt
   ```

4. Create a database:

   ```bash
   ./manage.py migrate
   ```

5. Create a Wagtail superuser:

   ```bash
   ./manage.py createsuperuser
   ```

6. Run the Wagtail server:

   ```bash
   ./manage.py runserver
   ```