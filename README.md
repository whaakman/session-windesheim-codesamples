# Deploying Santa's delivery service sample app
This sample application contains application code for a frontend website that allows for a submission of "messages" to Azure Service Bus. The code is written in Python and leverages Flask for the frontend. A backend is created to read messages from the Azure Service Bus queue for processing. KEDA is leveraged to scale based on the Azure Service Bus queue to launch jobs for processing. 


## Setting up the environment
To run the sample application the following resources are required:

- Azure Kubernetes Service Cluster
- Azure Service Bus

### Deployment
1. Deploy Azure Kubernetes Service: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
2. Deploy Azure Sevice Bus and create a queue (named "messages" in our examples): https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quickstart-portal 
3. Create an Shared Access Policy for the newly created queue: https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-sas
4. Encode the connection string from the Shared Access Policy in Base64
5. Update _secret.yaml_ in the /yaml directory with the Base64 encoded connection string 
6. Configure KEDA on your Azure Kubernetes Services cluster: https://learn.microsoft.com/en-us/azure/aks/keda-deploy-add-on-cli
7. Deploy the solution as follows:
```AzureCLI
kubectl apply -f .\yaml\secret.yaml
kubectl apply -f .\yaml\shipment-delivery-service.yaml
kubectl apply -f .\yaml\keda-shipment-processor.yaml
```

That should be sufficient for you to submit messages to Azure Service Bus for processing! 

### Video
As part of Festive Tech Calendar 2023 we have recorded a video going through these steps: LINK HERE ONCE AVAILABLE
