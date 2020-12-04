# country_codes app

Run Docker application: docker-compose up --build   
Default run has 2 commands: import to DB table from csv (implemented by django management command) and after that run REST API Server with 2 endpoints:

http://127.0.0.1:5000/locode/?code=<search param by code field>  
http://127.0.0.1:5000/locode/?name_wo_diacr=<search param by name_wo_diacritics field>  
***
example:  
http://127.0.0.1:5000/locode/?code=---4  
http://127.0.0.1:5000/locode/?name_wo_diacr=Gamba  

If you want run web server without upload csv table use command:  
`bash -c "python3 manage.py runserver 0.0.0.0:5000`  
instead     
`bash -c "python3 manage.py import_data '2020-1 UNLOCODE CodeListPart1.csv' && python3 manage.py runserver 0.0.0.0:5000" ` 
in docker-compose.yml file (line 23)
