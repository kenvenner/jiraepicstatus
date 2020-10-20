# may comment out in the future
import pprint
pp = pprint.PrettyPrinter(indent=4)

from atlassian import Jira

url= 'your-url'
username= 'your-account'
token='your-token-or-password'
ticket='your-ticket-number'


def jira_find_field( jira, fld, dumpall=False ):
    results = jira.get_all_fields()
    if dumpall:
        pp.pprint(results)
        return
    
    for result in results:
        if fld == result['name']:
            pp.pprint(result)


jira = Jira(
    url=url,
    username=username,
    password=token)

print('Field information in our instance')
jirafld = 'Epic Status'
jira_find_field( jira, jirafld )
# try different structures
epicstatus='In Progress'
jira_epic_done_field_formats = [
    {"customfield_10010":
         {"value": epicstatus
          }
    },
    { "customfield_10010" : [{"value" : epicstatus,}],},
    { "customfield_10010" : {"value" : epicstatus,},},
    { "customfield_10010" : epicstatus },
    { "fields" : { "customfield_10010" : {"value" : epicstatus,},},},
    { "fields" : { "customfield_10006" : {"value" : epicstatus,},},},
    { "customfield_10006" : {"value" : epicstatus,},},
]
print('-'*80)
print('Current value for this field')
result = jira.issue_field_value( ticket, "customfield_10010" )
print(result)
for jira_epic_done_fields in jira_epic_done_field_formats:
    print('-'*80)
    print('update json payload:')
    pp.pprint(jira_epic_done_fields)
    try:
        result = jira.update_issue_field( ticket, jira_epic_done_fields )
        print('epic status updated')
    except Exception as e:
        print(str(e))
