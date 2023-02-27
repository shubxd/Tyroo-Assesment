# Tyroo-Assesment

Steps:
1. Take pull of the master branch for above project and create a virtual environment
2. install requirements.txt given
3. run command: python manage.py migrate
4. to run server: python manage.py runserver
5. to insert data, python manage.py data_insert first
6. if not for step 5, or after step 5 use post apis mentioned in the api collection named: tyroo_assesment.postman_collection.json
7. use signup api to create your account, use login api to get jwt tokens, in case tokens get expired, use refresh token api for getting new jwt. in case of logout, refresh token is blacklisted.
8. all apis are ready to use.
