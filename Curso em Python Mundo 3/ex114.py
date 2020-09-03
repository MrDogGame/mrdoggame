import urllib
import urllib.request
try:
    urllib.request.urlopen('http://pudim.com.br/')
except:
    print('ERROR: O site esta fora!')
else:
    print('O site esta funcionando!')