import getopt
import sys
import os



def useage():
    print "invalid arguments"




def printConfigs(baseurl, geoserverdata, geonodedir, databasename, gisdatabasename, postgresuser, postgrespwd):


    with open("fixtures/config.xml", 'r') as of:
        configfile = of.read()
    print configfile
    configfile = configfile.replace("__baseurl__", baseurl)
    print geoserverdata
    with open(geoserverdata + "/security/auth/geonodeAuthProvider/config.xml", 'w') as wf:
        wf.write(configfile)
    with open(geonodedir + "/GeoNode/geoserver/data/security/auth/geonodeAuthProvider/config.xml", 'w') as wf:
        wf.write(configfile)


    with open("fixtures/httpd-vhosts.conf", 'r') as of:
        configfile = of.read()
    configfile = configfile.replace("__geonodedir__", geonodedir).replace("ServerName __baseurl__", "ServerName " + baseurl)
    with open("C:/Program Files (x86)/Apache Software Foundation/Apache24/conf/extra/httpd-vhosts.conf", 'w') as wf:
        wf.write(configfile)

    with open("fixtures/local_settings.py", 'r') as of:
        configfile = of.read()
    configfile = configfile.replace("http://__baseurl__/", "http://" + baseurl + "/").replace("__baseurl__", baseurl).replace("__geonodedir__", geonodedir).replace("'NAME': '__databasename__'", "'NAME': '" + databasename + "'")
    configfile = configfile.replace("'NAME': '__gisdatabasename__'", "'NAME': '" + gisdatabasename +"'", 100).replace("'USER': '__postgresuser__'", "'USER' : '" + postgresuser +"'", 100).replace("'PASSWORD': '__postgrespwd__'", "'PASSWORD': '" + postgrespwd + "'", 100)
    with open(geonodedir + "/GeoNode/geonode/local_settings.py", 'w') as wf:
        wf.write(configfile)

    with open("fixtures/web.xml", 'r') as of:
        configfile = of.read()
    configfile = configfile.replace("__geoserverdatadir__", geoserverdata)
    with open(geonodedir + "/GeoNode/geoserver/geoserver/WEB-INF/web.xml", 'w') as wf:
        wf.write(configfile)

    with open("fixtures/wsgi.py", 'r') as of:
        configfile = of.read()
    configfile = configfile.replace("__geonodedir__", geonodedir)
    with open(geonodedir + "/GeoNode/geonode/wsgi.py", 'w') as wf:
        wf.write(configfile)


    with open("fixtures/start_geoserver.bat", 'r') as of:
        configfile = of.read()
    configfile = configfile.replace("__geoserverdatadir__", geoserverdata).replace("__geonodedir__", geonodedir)
    with open(geonodedir + "/start_geoserver.bat", 'w') as wf:
        wf.write(configfile)


    for dname, dirs, files in os.walk(geonodedir + "/venv/Scripts"):
        for fname in files:
            if fname.endswith(('exe', 'pyc')):
                continue
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace("C:\\Users\\Administrator\\Desktop\\geonodewin_March\\software\\GeoNode", geonodedir)
            with open(fpath, "w") as f:
                f.write(s)


    


def main(argv):                          
    baseurl = "geonode.localhost" 
    geoserverdata =  "C:/GeoNode/GeoNode/geoserver/data"
    geonodedir = "C:/GeoNode"    
    databasename = "geonode"
    gisdatabasename = "geonode_imports"
    postgresuser = "postgres"
    postgrespwd = "postgres"

    opts, args = getopt.getopt(argv, "", ["help", "baseurl=", "geoserverdata=","geonodedir=", "databasename=", "gisdatabasename=", "postgresuser=", "postgrespwd="])
    try:                                
        opts, args = getopt.getopt(argv, "", ["help", "baseurl=", "geoserverdata=","geonodedir=", "databasename=", "gisdatabasename=", "postgresuser=", "postgrespwd="])
    except getopt.GetoptError:          
        usage()                         
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("help"):      
            usage()                     
            sys.exit()                  
        elif opt == '--baseurl':                         
            baseurl = arg                  
        elif opt == "--geoserverdata":
            print arg
            geoserverdata = arg.replace("\\", "/").strip("/")   
        elif opt == "--geonodedir": 
            geonodedir = arg.replace("\\", "/").strip("/")  
        elif opt == "--databasename": 
            databasename = arg     
        elif opt == "--gisdatabasename": 
            gisdatabasename = arg   
        elif opt == "--postgresuser": 
            postgresuser = arg     
        elif opt == "--postgrespwd": 
            postgrespwd = arg          
    printConfigs(baseurl, geoserverdata, geonodedir, databasename, gisdatabasename, postgresuser, postgrespwd)   



if __name__ == "__main__":
   main(sys.argv[1:])
