#!/bin/bash

if command -v docker; then
    echo "Docker is installed."
else
    echo "Docker is not installed"
    exit 1
fi

if command -v docker-compose; then
    echo "docker-compose is installed."
else
    echo "docker-compose is not installed"
    exit 1
fi

if [[ "$VIRTUAL_ENV" != "" ]]
then 
    echo "Running in $VIRTUAL_ENV venv."
    echo "Installing required modules..."
    pip install -e .
    if [ "$RUN_TESTS" ];
    then
        echo "Tests..."
        nosetests -vx
    fi
    echo "Building container.."
    docker build -t klarna-solver:latest . 
    echo "Starting proxy.."
    docker-compose up -d
    echo "Scaling.."
    docker-compose scale klarna_solver=5
    echo "Smoke tests..."
    python smoke_tests_requests.py
    echo "Some client/server tests and performance."
    python integration_tests.py
else
    echo "Make sure you are running in virtualenv."
fi
