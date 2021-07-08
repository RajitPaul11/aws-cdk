from aws_cdk import (aws_ec2 as ec2, core as cdk)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CustomVpcStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "MyVPCbyCDK",cidr="10.0.0.0/16",
            nat_gateways=0,max_azs=2,
            subnet_configuration=[ec2.SubnetConfiguration(name="public",cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
                                  ec2.SubnetConfiguration(name="private",cidr_mask=24, subnet_type=ec2.SubnetType.ISOLATED)])

        