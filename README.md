# Threadlocal AWS clients and resources

Convinient access to threadlocal boto3 clients and resources.

## Usage

### Resource

Lots of boto3 aws modules have resources. For example easy to iterate all instances:
```python
from threadlocal_aws.resources import ec2

for instance in ec2().instances.all():
     print(instance.id)
```

You can get an item from dynamo with just two lines of code:
```python
from threadlocal_aws.resources import dynamodb_Table as table

dynamo_resp = table(region="eu-central-1", "my-table").get_item(Key="foo#bar#123")
```

Or iterate all objects in a bucket:
```python
from threadlocal_aws.resources import s3_Bucket as bucket

for s3_obj in bucket("my-unique-bucket").objects.all():
     print(s3_obj.key)
```

### Client

```python
from threadlocal_aws.clients import ec2

instance = ec2().describe_instances(InstanceIds=["i-0fd31cg97d77ddfff"])
```
