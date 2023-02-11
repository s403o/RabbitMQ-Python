import pika, json, sys, os

def main():
  # establish a connection with RabbitMQ server.
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()

  # establish the queue
  queue = channel.queue_declare('order_notify')
  queue_name = queue.method.queue

  # establish the binding
  channel.queue_bind(
    exchange = 'order',
    queue = queue_name,
    routing_key = 'order.notify' # binding key
  )

  def callback(ch, method, properties, body):
    payload = json.loads(body)
    print('Notifying {}'.format(payload['email']))
    ''' ## Generating report ##
    print(f"""
    ID: {payload.get('id')}
    User Email: {payload.get('user_email')}
    Product: {payload.get('product')}
    Quantity: {payload.get('quantity')}
    """)
    '''
    print('Done')

  # (auto_ack=True) => send acknowledgement to make sure message is delivered
  channel.basic_consume(on_message_callback = callback, queue = queue_name, auto_ack=True) 
  print('Waiting for notify messages')
  channel.start_consuming()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
      sys.exit(0)
    except SystemExit:
        os._exit(0)
