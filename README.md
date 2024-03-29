# Python and Kafka
This content is meant to be followed as a workshop.<br>
To give feedback please create an issue here:<br>https://github.com/eguezgustavo/python_kafka/issues

## Before running the examples
Clone this repository:<br>
````git clone https://github.com/eguezgustavo/python_kafka.git````

Change to the workshop directory:<br>
````cd python_kafka````

Create a virtual environment (be sure you have Python 3 installed on your machine):<br>
```virtualenv -p python3 venv```

Activate the virtual environment:<br>
```source venv/bin/activate```

Install all the dependencies:<br>
```pip install -r requirements.txt```

## Part 1. Python AsyncIO

**Step 1.** _Read_ this article https://realpython.com/async-io-python/<br>
**Step 2.** _Exercise_: Write a Python script to print in the screen a "5 seconds" message every 5 seconds and a "3 seconds" message every 3 seconds. The script should use the **asyncio** framework.

**Solution:** asyncio_exercise.py<br>
**Run the solution:** ```python asyncio_exercise.py```

## Part 2. Python and Kafka (No Async IO)
**You need to have docker installed on your machine for this step of the workshop.**

**Step 1.** Run Kafka with Docker

```
    export IP=Your Machine Ip Here
    docker-compose up
```

**Step 2.** Create a Kafka Producer

- Open another terminal session:
- Activate the environment
```
    source venv/bin/activate
```
- Create a producer by running this command:
```
    export IP=Your Machine Ip Here
    ./producer_cli.py
```

**Step 3.** Create a Kafka Consumer

- Open another terminal session:
- Activate the environment
```
    source venv/bin/activate
```
- Create a consumer by running this command:
```
    export IP=Your Machine Ip Here
    ./consumer_cli.py
```

**Step 4.** Send a test message

Write the following message on the terminal session where the producer was started and hit Enter:

```{"test": true}```

Change to the terminal session where the consumer was started and you should see the posted message.

**Step 5.** Check the code

Study the **producer_cli.py** and **consumer_cli.py** files to understand how python-kafka works.

## Part 3. Python and Kafka with Async IO

**Step 1.** _Exercise_: Create a single python script with 2 Kafka consumers for the same topic. When a message is received each consumer should print its name and the message body.

**Hint:** Use the producer_cli.py script to send messages<br>
**Hint:** User the _aiokafka_ library<br>
**Solution:** asyncio_kafka_exercise.py<br>
**Run the solution:** ```export IP=Your Machine Ip Here && python asyncio_kafka_exercise.py```

Study the **asyncio_kafka_exercise.py** script to understand how aiokafka works.

