Vin decoder service
=====================================

Simple vin decoder service uses <https://www.decodethis.com> as third party service and stores found data to postgres database.


Running
=====================================

for lunching service you have start the docker and lunch current command from root of project

```
docker-compose up
```

then you have to lunch migrations

```
docker-compose run web python manage.py migrate
```

after successful migrations running you can go to 

```
http://localhost:8000/docs/
```

for lookup available methods.


Testing
===========================================

Run current command for lunching tests:

```
docker-compose run web python manage.py test service
```



