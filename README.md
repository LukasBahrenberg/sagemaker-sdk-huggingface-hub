# sagemaker-sdk-huggingface-hub
helps to deploy a model from the huggingface hub directly to sagemaker via local python sagemaker sdk script


## get the aws credentials right
warning: these might not be considered best security practices:

```
cp .env.example .env
```

first create an aws user `sagemaker` with the permissions  policies `IAMFullAccess`, `AmazonS3FullAccess` and `AmazonSageMakerFullAccess`

this lets the user perform all necessary tasks on aws.

for this user create an access key and secret key and put them in the .env file.

then create a role `sagemaker_execution_role` with the trusted entity type `AWS service` and  choose as use case `SageMaker (- Execution)`.

this lets the sagemaker service perform all necessary tasks on aws.


## get huggingface model hub credentials

get a user access token from the hugging face profile page. then put it in the .env file. this lets you access private models from the model hub and ones that need an additional access permission like llama2.

## how to use

create and activate python venv, then install the requirements

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

now the script can be run with

```
python deploy.py
```

## todo

create public api a la: https://www.youtube.com/watch?v=3y_TcDNC0HE

this might best be done via the web interface.
