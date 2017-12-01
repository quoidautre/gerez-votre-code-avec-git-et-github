#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import httplib, time
import urlparse, os.path


def get_server_status_code(url):
    """
    Download just the header of a URL and
    return the server's status code.
    """
    # http://stackoverflow.com/questions/1140661
    host, path = urlparse.urlparse(url)[1:3]    # elems [1] and [2]
    print "host : ", host, " | path : ", path
    try:
        conn = httplib.HTTPConnection(host)
        conn.request('HEAD', path)
        print " | status : " , conn.getresponse().status
        return conn.getresponse().status
    except StandardError as e:
        print "StandardError : ", e
        return None

def check_url(url):
    """
    Check if a URL exists without downloading the whole file.
    We only check the URL header.
    """
    # see also http://stackoverflow.com/questions/2924422
    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return get_server_status_code(url) in good_codes

if __name__ == '__main__':
    file_to_read = "urls.txt"

    if os.path.isfile(file_to_read):
        file = open(file_to_read, "r")
        for line in file:
            line = line.strip("\n")
            line = line.replace(" ", "")
            if check_url(line):
                print(line, " ok")
            else:
                print(line, " is out of control...!")

        time.sleep()
    else:
        print "<!> fichier urls non trouvé !"

print "That's all folk..."
