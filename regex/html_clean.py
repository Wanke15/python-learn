import re
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
    
    
cleanhtml("<div><h1>Title</h1><p>A long text........ </p><a href=""> a link </a></div>")
# 'TitleA long text........  a link '
