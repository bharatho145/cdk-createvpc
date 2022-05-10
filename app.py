#!/usr/bin/env python3
import os

import aws_cdk as cdk

from resource_stack.customvpc import customvpcstack


app = cdk.App()

customvpcstack(app,"my-custom-vpc-stack")

app.synth()
