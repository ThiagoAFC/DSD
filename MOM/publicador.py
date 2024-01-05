import pika

# Conectar ao servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Criar uma fila
channel.queue_declare(queue='testefila')

# Mensagem a ser enviada
msg=input("Informe o texto da mensagem:")

# Publicar mensagem na fila
channel.basic_publish(exchange='', routing_key='testefila', body=msg)

print(" [x] Mensagem enviada para a fila")

# Fechar a conexão
connection.close()
