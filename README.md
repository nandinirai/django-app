# django-app
# Use the following to insert data into liftapp_elevator

# INSERT INTO liftapp_elevator (name, curr_floor, direction, is_available,is_door_open) VALUES
#   ('Elevator 1', 1, TRUE, TRUE, TRUE),
#   ('Elevator 2', 10, FALSE, TRUE, TRUE),
#   ('Elevator 3', 5, TRUE, TRUE, TRUE);
# Inorder to run the below app
# run poetry install
# incase if you don't have poetry run pip install poetry first
# then run migrations by using the command python manage.py migrate
# also find the attached file and import it in postman in order to test the apis
# use thid to run the server on local host 'python manage.py runserver'