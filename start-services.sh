#!/bin/sh
(cd ./InternalApi; python3 manage.py runserver 8001) &
(cd ./SocialMediaService; python3 manage.py runserver 8002) &
(cd ./WebScraper; python3 manage.py runserver 8003) &
(cd ./Backend; python3 manage.py runserver 8004)