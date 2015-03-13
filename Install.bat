@ECHO OFF
REM set variables
set /p geonodedir="GeoNode Install Dir (C:\GeoNode): " %=%
set /p geoserverdatadir="Geoserver Data Dir (C:\GeoNode\GeoNode\geoserver\data): " %=%
set /p baseurl="Base URL (localhost): " %=%
set /p databasename="Database Name (geonode): " %=%
set /p gisdatabasename="GIS Database Name (geonode_imports): " %=%
set /p postgresuser="Postgres user (postgres): " %=%
set /p postgrespwd="Postgres password : " %=%

REM Install Apache
MKDIR "C:\Program Files (x86)\Apache Software Foundation\"
XCOPY software\Apache24 "C:\Program Files (x86)\Apache Software Foundation\Apache24\" /e /y

REM Install the geonode software
MKDIR "%geonodedir%"
XCOPY software\GeoNode "%geonodedir%" /e /y


REM copy the data files over
XCOPY software\GeoNode\GeoNode\geoserver\geoserver\data %geoserverdatadir% /y /e

REM pass variables as python scripts to write the setup files
C:\Python27\python.exe fixtures\pyeditconfig.py --baseurl="%baseurl%" --geoserverdata="%geoserverdatadir%" --geonodedir="%geonodedir%" --databasename="%databasename%" --gisdatabasename="%gisdatabasename%" --postgresuser="%postgresuser%" --postgrespwd="%postgrespwd%"


REM install geogit and set path
XCOPY software\geogig "C:\Program Files (x86)\geogig\" /y /e


REM Do PSQL and create DBs
REM "C:\Program Files (x86)\PostgreSQL\9.3\bin\psql.exe"
SET PGPASSWORD=%postgrespwd%
"C:\Program Files (x86)\PostgreSQL\9.3\bin\psql.exe" -U %postgresuser% -c "CREATE DATABASE %databasename% WITH ENCODING 'UTF8'"
"C:\Program Files (x86)\PostgreSQL\9.3\bin\psql.exe" -U %postgresuser% -c "CREATE DATABASE %gisdatabasename% WITH ENCODING 'UTF8' TEMPLATE postgis_21_sample"


REM Make Apache a service this a service
START /wait "placeholder" "C:\Program Files (x86)\Apache Software Foundation\Apache24\bin\httpd.exe" -k install
START /wait "placeholder" "C:\Program Files (x86)\Apache Software Foundation\Apache24\bin\httpd.exe" -k start



REM initiate venv
%geonodedir%\venv\Scripts\activate.bat

REM run commands
python %geonodedir%\GeoNode\manage.py syncdb









