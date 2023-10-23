import os
import json

from dotenv import load_dotenv
import boto3
import sagemaker
from sagemaker.huggingface import HuggingFaceModel, get_huggingface_llm_image_uri

load_dotenv()

INSTANCE_TYPE = "ml.g5.2xlarge" # this bigger instance seems to be needed for the model. otherwise it errors.
MODEL_NAME = 'meta-llama/Llama-2-7b-chat-hf'
HUGGING_FACE_HUB_TOKEN = os.environ.get('HUGGING_FACE_HUB_TOKEN')

iam = boto3.client('iam')
role = iam.get_role(RoleName='sagemaker_execution_role')['Role']['Arn']
sess = sagemaker.Session()

hub = {
	'HF_MODEL_ID': MODEL_NAME,
	'SM_NUM_GPUS': json.dumps(1),
	'HUGGING_FACE_HUB_TOKEN': HUGGING_FACE_HUB_TOKEN,
}

huggingface_model = HuggingFaceModel(
	image_uri=get_huggingface_llm_image_uri("huggingface",version="1.1.0"),
	env=hub,
	role=role, 
)

predictor = huggingface_model.deploy(
	initial_instance_count=1,
	instance_type=INSTANCE_TYPE,
    container_startup_health_check_timeout=300,
)

output = predictor.predict({
	"inputs": "Boston is the capital of ",
})

print(output)

# delete aws resources
predictor.delete_endpoint()
huggingface_model.delete_model()
