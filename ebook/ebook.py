from bs4 import BeautifulSoup as BS
import subprocess

def toc(ind):
    code = BS(ind,'html5lib')
    code = code.find('ol',{'class':'tableofcontents'})
    toc = []
    for i in code.find_all('a'):
        toc.append(i.get('href') + 'index.html')
    return toc

def lowerheaders(html):
    s = html
    for i in [5,4,3,2,1]:
        headers = s.find_all('h' + str(i))
        for j in headers:
            j.name = 'h' + str(i+1)
    return s

def content(tableofcont):
    cont = "<meta charset='utf-8'>" + str(BS(open('./index.html'),'html5lib').main)
    for i in tableofcont:
        ch = BS(open(i),'html5lib').main
        cont = cont + str(lowerheaders(ch))[6:-7]
    return cont

def links(content):
    cont = BS(content,'html5lib')
    hyperlinks = cont.find_all('a')
    for link in hyperlinks:
        href = link['href']
        if href[0:2] == './':
            link['href'] = '#' + href[2:-1]
        if href[0:3] == '../':
            link['href'] = '#' + href[3:-1]
    return cont

def CommitId():
    idcmd = ['git','log','--pretty=format:"%H"','-n','1|cat|']
    commitid = subprocess.check_output(idcmd)
    commitid = commitid.decode()
    return commitid[1:-1]

def main():
    f = open('index.html','r')
    index = f.read()
    f.close
    stuff = str(links(content(toc(index))))
    commit = '<pre><code>' + CommitId() + '</code></pre>'
    stuff = stuff.replace('<!--CommitIdGoesHere-->',commit)
    #stuff.replace('heading','commit')
    print(stuff)

if __name__ == '__main__':
    main()





