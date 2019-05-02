# myeqip-portal

The official web portal for the Myanmar Education Quality Improvement Program, built on [Wagtail](www.wagtail.io).

## Set up the Back-end

1. Clone the "myeqip-portal" repository:

   ```bash
   git clone git@github.com:catalpainternational/myeqip-portal.git
   ```

2. Create a Python virtual envionment. myeqip-portal uses Python 3.6.7:

   ```bash
   python3 -m venv virtualenv
   ```

   or

   ```bash
   pyenv virtualenv 3.6.7 myeqip
   pyenv local myeqip
   ```

3. Installs necessary Python packages from `requirements.txt`. Install packages with:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a local settings file

    ```bash
    cd portal
    cp portal/local_settings_example.py portal/local_settings.py
    ```

5. Create a database using Postgres 9

    ```bash
    createdb myeqip_db
    ```

6. Apply migrations:

   ```bash
   ./manage.py migrate
   ```

7. Create a Wagtail superuser:

   ```bash
   ./manage.py createsuperuser
   ```

8. Run the Wagtail server:

   ```bash
   ./manage.py runserver
   ```

## Set up the Front-end

1. Building the front-end requires ["Yarn"](https://yarnpkg.com/en/). Install Yarn, navigate to the myeqip-portal's root directory, and run:

    ```bash
    yarn
    ```

2. You can compile SASS and JavaScript assets with:

    ```bash
    yarn run dev
    ```

3. Yarn can detect changes in these assets and rebuild them automatically. Use "watch":

    ```
    yarn run watch
    ```
