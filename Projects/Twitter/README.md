In this Data Engineering I project I've done the following : 

1) Extracting Tweets from Tweeter using Tweepy

2) I created an EC2 instance on AWS and installed Airflow

3) On Airflow I created a DAG that runs the Python function that uses Twitter API to extract tweets

4) Created a Bucket on S3 and saved the the tweets on it.


Bugs : 

1) Connection to EC2 : solved by adding :8080 to the Instance's DNS and add a rule in the Security Group Inbound

2) Connection to Airflow server (run on EC2) : Solved by allowing Serial Control Access, then configuring an OS password, and finally desactivating the firewall using the Serial Console


3) Connection between EC2 Instance and the S3 Bucket : In EC2 instance->Actions->Create IAM role then create a role and give full access to EC2 and S3. Then go to the Instance-> modify IAM->choose new role and update.
