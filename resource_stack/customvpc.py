from operator import truediv
from aws_cdk import CfnOutput, Stack
from aws_cdk import aws_ec2 as _ec2
from constructs import Construct


class customvpcstack(Stack):

    def __init__(self, scope: Construct, construct_id: str,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
       # print(self.node.try_get_context('dev'))
        dev_config = self.node.try_get_context('envs')['dev']
      #  print(dev_config)

        custom_vpc = _ec2.Vpc (
            self,
            "CustomVpcId",
            cidr=dev_config['vpc_configs']['vpc_cidr'],
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                _ec2.SubnetConfiguration(
                    name="publicSubnet",cidr_mask=dev_config['vpc_configs']['cidr_mask'],subnet_type=_ec2.SubnetType.PUBLIC
                ),
                _ec2.SubnetConfiguration(
                    name="privateSubnet",cidr_mask=dev_config['vpc_configs']['cidr_mask'],subnet_type=_ec2.SubnetType.PRIVATE_WITH_NAT
                ),
                _ec2.SubnetConfiguration(
                    name="dbSubnet",cidr_mask=dev_config['vpc_configs']['cidr_mask'],subnet_type=_ec2.SubnetType.PRIVATE_ISOLATED
                )
           ]
        )
        CfnOutput(self,"CustomVPCoutput",value=custom_vpc.vpc_id,export_name="customvpcid")