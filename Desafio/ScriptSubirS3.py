import boto3
import os

os.environ["AWS_ACCESS_KEY_ID"] = 'inserir_sua_access_key_aqui'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'inserir_sua_secret_access_key_da_aws_aqui'
os.environ["AWS_DEFAULT_REGION"] = 'us-east-1'

bucket_name = 'desafio'
local_folder = 'Parquet/'

s3 = boto3.client(
    's3',
    aws_access_key_id='inserir_sua_access_key_aqui',
    aws_secret_access_key='inserir_sua_secret_access_key_da_aws_aqui',
    region_name='us-east-1'
)

i = 1
for root, dirs, files in os.walk(local_folder):
    for file in files:
        file_path = os.path.join(root, file)
        s3_object_key = os.path.relpath(file_path, local_folder)

        try:
            s3.upload_file(file_path, bucket_name, s3_object_key)
            print(f'Arquivo {i} foi enviado ao S3 com sucesso!')
            print(f'Successfully uploaded {file} to {bucket_name}/{s3_object_key}')
            i += 1 
        except Exception as e:
            print(f'Error uploading {file}: {e}')
