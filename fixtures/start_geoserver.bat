@echo off
cd C:\Geonode\GeoNode\geoserver\data
"%JRE_HOME%\bin\java.exe" -Xmx512m -XX:MaxPermSize=256m  -DGEOSERVER_DATA_DIR=__geoserverdatadir__  -Dorg.eclipse.jetty.server.webapp.parentLoaderPriority=true  -jar __geonodedir__\GeoNode\downloaded\jetty-runner-8.1.8.v20121106.jar --log __geonodedir__\logs\jetty.log  __geonodedir__\GeoNode\scripts\misc\jetty-runner.xml &