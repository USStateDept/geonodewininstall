@ECHO off

set PREFIX=%~dp0


REM set our other paths while we are at it

set GDAL_LIBRARY_PATH=%PREFIX%..\venv\Lib\site-packages\osgeo\gdal111.dll

set GEOS_LIBRARY_PATH=%PREFIX%..\venv\Lib\site-packages\osgeo\geos.dll
