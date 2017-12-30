## Setup up AWS 
1. Create an [AWS](https://aws.amazon.com/) Account. 
2. Search for the IAM Service.
3. Click on "Users". 
4. Click "Add user". 
5. Name the user anything you want related to your project.
6. Check Programmatic access only.
7. Press "Next".
8. Select "Attach existing policies directly". 
9. Search for AmazonRekognitionFullAccess and add that policy. 
10. Click next.
11. Click create user. 
12. Save the Access Key ID and the Secret Access Key. 

## Run aws-configure
```
python3 -m pip install awscli
aws-configure  #enter the access key and secret key from above, choose us-east-1 as your region, and choose defaults for everything else. 
```


## Install boto3
```python
python3 -m pip install boto3
```

## Install Pillow
```python
python3 -m pip install pillow
```

## Run the Demo
```python
python3 demo.py
```




