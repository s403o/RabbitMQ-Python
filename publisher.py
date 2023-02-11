import pika, json, uuid

# establish a connection with RabbitMQ server.
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# establish a exchange
channel.exchange_declare(
  exchange= 'order',
  exchange_type= 'direct'
)

# the message
order = {
  'id': str(uuid.uuid4()),
  'email': 'eslam.adel.me@gmail.com',
  'product': 'macbook air m1',
  'quantity': 1
}

# send the email of the order when routing_key= order.notify
channel.basic_publish(
  exchange = 'order',
  routing_key = 'order.notify',
  body = json.dumps({'email': order['email']})
)

print('Sent notify message')

# send the whole order info when routing_key= order.report
channel.basic_publish(
  exchange = 'order',
  routing_key = 'order.report',
  body = json.dumps(order)
)

# print('Sent report message')
connection.close()