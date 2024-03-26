from aws_cdk import (
    Stack,
    aws_s3 as s3,
    RemovalPolicy,
    CfnOutput,
)
from constructs import Construct

class O2ArenaS3Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, input_metadata, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # S3 bucket creation
        self.bucket = s3.Bucket(self, "landing-zone",
                    # Let CDK to delete the bucket if this is empty:
                    removal_policy=RemovalPolicy.DESTROY)

        # Return bucket auto-generated name
        CfnOutput(self, "Output-1", value=self.bucket.bucket_arn)
