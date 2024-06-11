# app.py

import os
import asyncio
from flask import Flask, render_template, request, redirect
import asyncio
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus import ServiceBusMessage

app = Flask(__name__)

# Replace these values with your Azure Service Bus fully qualified namespace and queue name
NAMESPACE_CONNECTION_STR = os.environ.get("NAMESPACE_CONNECTION_STR")
QUEUE_NAME = os.environ.get("QUEUE_NAME")

async def send_a_list_of_messages(sender, number_of_messages):
    # Create a list of messages and send it to the queue
    messages = [ServiceBusMessage("New order!") for _ in range(int(number_of_messages))]
    await sender.send_messages(messages)
    print(f"Submitted {number_of_messages} orders to queue!")

@app.route('/')
def index():
    # Add a variable to pass the count to the template
    count = request.args.get('count', default=0, type=int)
    return render_template('index.html', count=count)


@app.route('/send_message', methods=['POST'])
async def run():
    # create a Service Bus client using the connection string
    async with ServiceBusClient.from_connection_string(
        conn_str=NAMESPACE_CONNECTION_STR,
        logging_enable=True) as servicebus_client:
        # Get a Queue Sender object to send messages to the queue
        number_of_messages = request.form['number']
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        async with sender:
            # Send a list of messages
            await send_a_list_of_messages(sender, number_of_messages)
    return redirect(f'/?count={number_of_messages}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
