# Klarna test solution

## Note before reading 

There obviously are many ways to solve this. One way it
can be to be event based, other way is that the calculations
between recursion steps can be also cached in Redis. Other
way is to not have any calculations in the API and just 
cache the result and have "workers" based on events calculate
the result. I choose the current solution since it didn't
require too much time to complete. After all this is only a 
coding test.

## What is missing?

I have added some basic tests, smoke test and integration tests.
Of course it can expanded to have more tests, but I don't want
to spent too much time on it.

The problems could be solved better with a different architecture.
I chose the fastest way to solve this test.

## Architecture

The service is creating using flask and uses Redis
for caching and Traefik for load-balancing. The solution
is spawn to multiple instance using docker and docker-compose.

request --> traefik  --> API -> Redis

There are currently 5 instances of the API spawned.

There are several ways of testing:
- Smoke tests
- Unittests
- Some simple integration tests that just "fire" stuff.

## Requirements for running the solution
- Docker
- docker-compose
- virtualenv
- Python3

## How to start?

If you have the requirements, just run the setup_and_start_service.sh

./setup_and_start_service.sh

## How the cache works?

As key is used -> function_name_arg1_arg2.. : result

## How the load balancer works?

gunicorn is used to spawn flask as a process and traefik is used to
redirect the traffic. Simple rule added to redirect the traffic.
