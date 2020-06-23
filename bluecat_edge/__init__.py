import yaml
import os
import requests
from expiringdict import ExpiringDict
from bluecat_edge import color, classes

# Get our config
cfg_file = os.path.dirname(__file__) + '/config.yaml'
with open(cfg_file) as config_file:
    config = yaml.load(config_file, Loader=yaml.FullLoader)
master_token = ExpiringDict(max_len=1, max_age_seconds=285)
host = config['host']

#
# Compile all of our endpoints for use
GET_AUTH_TOKEN = '{}/v1/api/authentication/token'.format(host)
LIST_NAMESPACES = '{}/v1/api/namespaces'.format(host)
GET_NAMESPACE = '{}/v1/api/namespaces/{{}}'.format(host)
LIST_SITES = '{}/v3/api/sites'.format(host)
LIST_SITE_GROUPS = '{}/v1/api/customer/siteGroups'.format(host)
GET_SITE = '{}/v3/api/sites/{{}}'.format(host)
LIST_POLICIES = '{}/v5/api/policies'.format(host)
GET_POLICY = '{}/v5/api/policies'.format(host)
LIST_DLS = '{}/v1/api/list/dns'.format(host)
GET_QUERY_LOGS = '{}/v3/api/dnsQueryLogs?{{}}'.format(host)
GET_AUDIT_LOGS = '{}/v1/api/audit/logs?{{}}'.format(host)
COUNT_QUERIES = '{}/v1/api/customer/dnsQueryLog/count?siteName={{}}'.format(host)

def refresh_token():
    try:
        return "Bearer {}".format(master_token['Bearer'])
    except KeyError:
        credentials = {
            'grantType': 'ClientCredentials',
            'clientCredentials': {
                'clientId': config['clientId'],
                'clientSecret': config['clientSecret']
            }
        }
        response = requests.post(GET_AUTH_TOKEN, json=credentials).json()
        master_token[response['tokenType']] = response['accessToken']
        return "Bearer {}".format(master_token['Bearer'])


def list_ns():
    headers = dict(Authorization=refresh_token())
    response = requests.get(LIST_NAMESPACES, headers=headers).text
    ns_info = classes.Namespace.schema().loads(response, many=True)
    return ns_info


def get_ns(obj_id):
    headers = dict(Authorization=refresh_token())
    response = requests.get(GET_NAMESPACE.format(obj_id),
                            headers=headers).text
    ns_info = classes.Namespace.schema().loads(response)
    return ns_info


def list_sites():
    headers = dict(Authorization=refresh_token())
    response = requests.get(LIST_SITES, headers=headers).text
    site_info = classes.Site.schema().loads(response, many=True)
    return site_info


def get_site(obj_id):
    headers = dict(Authorization=refresh_token())
    response = requests.get(GET_SITE.format(obj_id),
                            headers=headers).text
    site_info = classes.Site.schema().loads(response)
    return site_info


def list_site_groups():
    headers = dict(Authorization=refresh_token())
    response = requests.get(LIST_SITE_GROUPS, headers=headers).text
    site_info = classes.SiteGroup.schema().loads(response, many=True)
    return site_info


def list_policies():
    headers = dict(Authorization=refresh_token())
    response = requests.get(LIST_POLICIES, headers=headers).text
    policy_info = classes.Policy.schema().loads(response, many=True)
    return policy_info


def get_policy(obj_id):
    headers = dict(Authorization=refresh_token())
    response = requests.get(GET_POLICY.format(obj_id),
                            headers=headers).text
    policy_info = classes.Policy.schema().loads(response)
    return policy_info


def list_dl():
    headers = dict(Authorization=refresh_token())
    response = requests.get(LIST_DLS, headers=headers).text
    dl_info = classes.DomainList.schema().loads(response, many=True)
    return dl_info


def get_queries(**query_items):
    query_elements = [(str(k) + "=" + str(v))
                      for k, v in query_items.items()]
    query_string = '&'.join(query_elements)
    headers = dict(Authorization=refresh_token())
    response = requests.get(GET_QUERY_LOGS.format(query_string),
                            headers=headers).text
    query_info = classes.Query.schema().loads(response, many=True)
    return query_info


def count_queries(site):
    headers = dict(Authorization=refresh_token())
    query_count = requests.get(COUNT_QUERIES.format(site),
                               headers=headers).json()
    return query_count['count']
