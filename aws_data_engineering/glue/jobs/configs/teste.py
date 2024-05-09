import yaml

def split_s3_path(s3_path: str) -> tuple[str]:
    
    path_parts = s3_path.replace('s3://', '').split('/')
    bucket = path_parts.pop(0)
    key = '/'.join(path_parts)
    
    return bucket, key
    

with open('test.yaml', 'r') as yaml_file:
    glue_jobs_configs = yaml.safe_load(yaml_file)
    
    
# print({i['source_bucket'] for i in glue_jobs_configs})
print(split_s3_path('s3://bucket/teste/asdasd/teste.yaml/'))

x = {f'{i}' for i in range(10)}
print(x)
print(list(map(lambda y: '5' in y, x)))

print(list(map(lambda y: '5' in y, x)).index(True))
teste = any(map(lambda y: '5' in y, x))
if teste:
    print('yes')