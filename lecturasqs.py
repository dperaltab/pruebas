from boto.sqs.connection import SQSConnection
import simplejson as json

def lecturasqs():
	AWS_ACCESS_KEY_ID = 'AKIAJK6M2ZU2J66WGP2Q'
	AWS_SECRET_ACCESS_KEY = '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'

	conn = SQSConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

	q = conn.get_queue('myqueue') #seleccionamos el queue

	rs = q.get_messages(10) #la cantidad de mensajes a que va a leer
	
	f = open("/home/ubuntu/openerp/msgcolas.txt", "a")
	
	for x in range(len(rs)):
		lista = json.loads(rs[x].get_body())
		#falta definir los campos reales con que vvamos a trabajar en nuestra db (incompleto)
		importe_total = float(lista[3])
		sub_total = importe_total/1.18
		igvv = importe_total - sub_total
		#borrar
		f.write(str(lista)+'\n')
		f.close
		#q.delete_message(rs[x])

lecturasqs()
