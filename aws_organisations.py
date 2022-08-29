# #get the aws organisations acc
# aws_org = boto3.client('organizations')
# # create a paginator with aws org to list all the accounts under organisations
# paginator = aws_org.get_paginator('list_accounts')
# page_iterator = paginator.paginate()

# # then iterate through every page of accounts
# for page in page_iterator:
#     for account in page['Accounts']:
#         aws_accounts.append(account['Id'])
#         print('Account ID', account['Id'])