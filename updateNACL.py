# function to update NACL with IP address range to block
def update_nacl(nacl_id, ip_range):
    import boto3
    import os
    import json
    import logging

    # Set up logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create NACL client
    ec2 = boto3.client('ec2')

    # Get the NACL entry to update
    try:
        response = ec2.describe_network_acls(
            NetworkAclIds=[nacl_id]
        )
        logger.info("NACL entry to update: %s", response)
    except Exception as e:
        logger.error("Error getting NACL entry: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error getting NACL entry')
        }

    # Update the NACL entry
    try:
        response = ec2.replace_network_acl_entry(
            NetworkAclId=nacl_id,
            RuleNumber=response['NetworkAcls'][0]['Entries'][0]['RuleNumber'],
            Protocol='-1',
            RuleAction='deny',
            Egress=False,
            CidrBlock=ip_range,
            PortRange={
                'From': 0,
                'To': 65535
            }
        )
        logger.info("NACL entry updated: %s", response)
        return {
            'statusCode': 200,
            'body': json.dumps('NACL entry updated')
        }
    except Exception as e:
        logger.error("Error updating NACL entry: %s", e)
        return {
            'statusCode': 500,
            'body': json.dumps('Error updating NACL entry')
        }