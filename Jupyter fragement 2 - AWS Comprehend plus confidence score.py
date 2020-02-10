import boto3
import csv

# the AWS BOTO client that allows you to call AWS services from python. Working with Comprehend endpoint
client = boto3.client('comprehend')

# the Comprehend endpoint ARN reference 

end_point_arn = 'arn:aws:comprehend:eu-west-2:362308776760:document-classifier-endpoint/junkshon-comprehend-01'

# Confidence score threshold. Will only take Comprehend result for lable if the confidence score exceeds threshold
confidence_threshold = 0.5

# open file with label in first column and text to be labelled in second column
with open('ComprehendTrainingFile03.csv') as csv_file:
     csv_reader = csv.reader(csv_file)
     # set counters
     i=0
     c=0
     nc = 0
        
     for row in csv_reader:
        # count each row in csv 
        i = i + 1
        # label is in column 0
        system_software_label = row[0]
        #delete column 0 from row
        del row[0]
        
        # set payload to be the text string to be labelled - now in first column
        pay_load = row[0]
        #print('Payload: ', pay_load)
        # call to the Comprehend endpoint to classify document
        response = client.classify_document(
            Text = pay_load,
            EndpointArn = end_point_arn
        )
        # Comprehend returns a dictionary structure - a set of three Classes each with a name/confidence score pair
        # First pair is the name lable with the highest confidence score so we pick that one - index 0
        result = (response['Classes'][0]['Name'])
        confidence_score = (response['Classes'][0]['Score'])
        
        #print(result)
        # print label from file alongside calculated value
        #print('Label:', system_software_label, 'Result:', result)
        
        # check if confidence score exceeds threshold otherwise set result = 0 i.e. unlablelled and requiring manual review
        if confidence_score < confidence_threshold:
            nc = nc + 1
            result = 0
        # check if label matches predicted result
        if system_software_label == str(result):
            c = c + 1

print('Total Rows:', i)
print('Total Correct Predictions:', c)
print('Total of low confidence scores < 0.5 = ', nc)