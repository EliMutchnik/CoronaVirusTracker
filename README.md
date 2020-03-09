# Corona Virus Tracker
This project will show a list of all and top 10 countries with confirmed corona cases.
The project is written in python3, using DataTables with Jinja templates, running inside a docker container.
The API used is the ArcGIS "ncov_cases" RestAPI service.

## Run the project
```
cd ./CoronaVirusCheck
docker-compose up -d
```

## Health check
http://localhost:5000/

## All countries with CoronaVirus confirmed cases (ordered alphabetically)
http://localhost:5000/all

## Top 10 countries with CoronaVirus confirmed cases (descending order)
http://localhost:5000/top

## License
[MIT](https://choosealicense.com/licenses/mit/)