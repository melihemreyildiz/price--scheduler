Docker Harici Kurulum
    Python kurulmalı (Python 3.8). Dokumantasyon:
            https://www.python.org/downloads/
 
    Python projesi için virtual environement kurulmalıdır. Dokumantasyon:
        https://docs.python.org/3/library/venv.html
    
    Python proje bağımlılıkları kurulmalı:
    
      $ cd bitexen
      $ source venv/bin/activate
      $ pip install -r requirements.txt
    
  Veritabanı migrationları yoksa onlar oluşturulmalı.

      $ python manage.py makemigrations          
      $ python manage.py migrate   

Docker:

    $ docker-compose up -d (interactive shell)
    $ docker-compose down (durdurmak için)