
# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Stack Configuration

When you hardcode the target account and Region as shown in the preceding example, the stack is always deployed to that specific 
account and Region. To make the stack deployable to a different target, but to determine the target at synthesis time, your stack 
can use two environment variables provided by the AWS CDK CLI: CDK_DEFAULT_ACCOUNT and CDK_DEFAULT_REGION. These variables are set 
based on the AWS profile specified using the --profile option, or the default AWS profile if you don't specify one.

```python
import os
MyDevStack(app, "dev", env=cdk.Environment(
    account=os.environ["CDK_DEFAULT_ACCOUNT"],
    region=os.environ["CDK_DEFAULT_REGION"]))
```

When you pass in your environment using **CDK_DEFAULT_ACCOUNT** and **CDK_DEFAULT_REGION**, the stack will be deployed in the account and Region 
determined by the AWS CDK CLI at the time of synthesis. This lets environment-dependent code work, but it also means that the synthesized 
template could be different based on the machine, user, or session that it's synthesized under. This behavior is often acceptable or even 
desirable during development, but it would probably be an **anti-pattern for production** use.

See more information in [Environment](!https://docs.aws.amazon.com/cdk/v2/guide/environments.html).

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


## Useful docs

[AWS CDK Best Practices](!https://docs.aws.amazon.com/cdk/v2/guide/best-practices.html)

Enjoy!
