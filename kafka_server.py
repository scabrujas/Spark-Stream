import producer_server


def run_kafka_server():
    
    #Get the json file path
    input_file = "police-department-calls-for-service.json"

    #Produce data from file
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="police.service.calls",
        bootstrap_servers="localhost:9092",
        client_id="consumer-1",
        api_version=(0, 10, 1)
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()

