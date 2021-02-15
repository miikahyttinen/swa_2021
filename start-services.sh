#!/bin/sh
(cd ./ApiGateway; python3 manage.py runserver 8001) &
(cd ./Backend; python3 manage.py runserver 8002) &
(cd ./InternalApi; python3 manage.py runserver 8003) &
(cd ./WebScraper; python3 manage.py runserver 8004) &