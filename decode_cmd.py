import io,sys,re

if len(sys.argv) != 2:
	print "ERROR: Se necesita 1 parámetro"
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
  res=re.findall(r'%[^%]%',line)
  linea=line
  for bloque in res:
    linea=linea.replace(bloque,reemplazo[busqueda.index(bloque)])
  return linea

f = io.open(sys.argv[1],mode="r",encoding="iso-8859-1")
for line in f:
  res1 = re.findall(r'set\s+\"@lo@=(.*)$', line)
  res2 = re.findall(r'set\s+\"@hi@=(.*)$', line)
  if len(res1) > 0:
    reemplazo=res1[0][:-1]
  if len(res2) > 0:
    busqueda=res2[0][:-1]
f.close()

reemplazo=arreglo_reemplazo(reemplazo)
busqueda=arreglo_busqueda(busqueda)

f = io.open(sys.argv[1],mode="r",encoding="iso-8859-1")
for line in f:
  aux = re.findall(r'%%', line)
  if len(aux) > 0:
    print parse_string(line.rstrip())
f.close()
