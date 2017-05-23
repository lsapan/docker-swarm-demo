# Docker Swarm Demo
Docker containers have already changed the way we develop and ship software,
but container orchestration can seem like a very daunting task when you're
ready to scale up in production.

This project lays out a simplified example of how to deploy your app to Docker
Swarm, which is Docker's built-in container orchestration mechanism.

## What is the app?
It's a simple Flask app that tells you the id of the container the process is
running in, as well as the number of requests it has received.

A shared redis process is utilized so the request count is persistent.

## What are the takeaways here?
The goal is to demonstrate just how easy it is to deploy a stack of services
to a swarm. Without any work, the web workers will find the redis process
thanks to Docker's internal DNS magic. Additionally, the nginx and web services
can be scaled up as much as you wish. You'll be able to see how when you make
a request to the swarm, it will automatically load balance the requests across
the running containers. It also emphasizes just how easy Swarm makes it to
securely store and deploy your app's secrets.

## How do I get started?
To test the app on your computer without Swarm mode, simply run:
```
docker-compose up
```

If you're on a machine (or several machines) with Swarm, you can deploy it as
a stack:
```
echo "supersecretpassword" | docker secret create db_password -

docker stack deploy -c docker-compose.yml demo
```

The first line defines the `db_password` secret in your Swarm, and the second deploys the actual stack.
