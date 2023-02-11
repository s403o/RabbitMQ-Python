## RabbitMQ-Python
Applying Message queue architecture using RabbitMQ

## Installing RabbitMQ using Docker
```bash
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management
```
## Running
- start the publisher ``` python3 publisher.py ``` You should see an output ***Sent notify message
Sent report message***
- start the consumer ```python3 consumer.py```, You should see an output ***Notifying eslam.adel.me@gmail.com***

## Architecture
![image](https://user-images.githubusercontent.com/38042656/218279597-51c58403-feb5-49e3-a51d-777835fbd4b1.png)
