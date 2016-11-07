"crawl chinese article from internet"
import urllib

__url = "http://read.qidian.com/BookReader/HWmTBiMp_J81,7jKiW-KZflAex0RJOkJclQ2.aspx"

def crawl(output):
    url = urllib.urlopen(__url)
    content = url.read()
    out = open(output, "w")
    out.write(content)
    out.close()
    url.close()
    return