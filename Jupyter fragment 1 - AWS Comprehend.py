import boto3
import csv

# the AWS BOTO client that allows you to call AWS services from python. Working with Comprehend endpoint
client = boto3.client('comprehend')

# the Comprehend endpoint ARN reference 

end_point_arn = 'arn:aws:comprehend:eu-west-2:362308776760:document-classifier-endpoint/junkshon-comprehend-01'

# open file with label in first column and text to be labelled in second column
with open('ComprehendTrainingFile03.csv') as csv_file:
     csv_reader = csv.reader(csv_file)
     # set counters
     i=0
     c=0
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
        # Comprehend returns a Dictionary structure - a set of three Classes each with a name/confidence score pair
        # First pair is the name lable with the highest confidence score so we pick that one - index 0
        result = (response['Classes'][0]['Name'])
        
        #print(result)
        # print label from file alongside calculated value
        #print('Label:', system_software_label, 'Result:', result)
        
        # check if label matches predicted result
        if system_software_label == str(result):
            c = c + 1

print('Total Rows:', i)
print('Total Correct Predictions:', c)