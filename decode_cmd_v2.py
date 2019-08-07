# -*- coding: utf-8 -*-
import io,sys,re
reload(sys)
sys.setdefaultencoding('utf-8')

if len(sys.argv) != 2:
	print "ERROR: Se necesita 1 parametro"
	sys.exit(1)

def arreglo_reemplazo(line):
  n=1
  res=[line[i:i+n] for i in range(0, len(line), n)]
  return res

def arreglo_busqueda(line):
  res=line.split("=")
  res.pop(len(res)-1)
  res.pop(0)
  return res

def parse_string(line):
  res=re.findall(r'%([^%])%',line)
  linea=line
  for bloque in res:
    linea=linea.replace("%"+bloque+"%",reemplazo[busqueda.index(bloque)])
  return linea

f = io.open(sys.argv[1],mode="r",encoding="iso-8859-1")
for line in f:
  res1 = re.findall(r'set\s+\"@[a-zA-Z0-9]+@=( !#.*)$', line)
  res2 = re.findall(r'set\s+\"@[a-zA-Z0-9]+@=([^ !#]*)$', line)
  if len(res1) > 0:
    reemplazo=res1[0][:-1]
  if len(res2) > 0:
    busqueda=res2[0][:-1]
f.close()

reemplazo=arreglo_reemplazo(reemplazo)
#busqueda=arreglo_busqueda(busqueda)
busqueda=arreglo_reemplazo(busqueda)

http = []

f = io.open(sys.argv[1],mode="r",encoding="iso-8859-1")
for line in f:
  aux = re.findall(r'%%', line)
  if len(aux) > 0:
    linea = parse_string(line.rstrip())
    temp = re.findall(r'StrReverse\("(.*ptth)"\)', linea)
    if len(temp) > 0:
        http.append(temp[0][::-1])
    print linea
  else:
    print line
f.close()

print "-"*100
print "Las URL involucradas son:"
print "-"*100
for url in http:
    print url
