# Copyright 2012 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# NOTE(dolph): please try to avoid additional fixtures if possible; test suite
#              performance may be negatively affected.
import uuid

BAR_TENANT_ID = uuid.uuid4().hex
BAZ_TENANT_ID = uuid.uuid4().hex
MTU_TENANT_ID = uuid.uuid4().hex
SERVICE_TENANT_ID = uuid.uuid4().hex
DEFAULT_DOMAIN_ID = 'default'
ADMIN_ROLE_ID = uuid.uuid4().hex
MEMBER_ROLE_ID = uuid.uuid4().hex
OTHER_ROLE_ID = uuid.uuid4().hex

TENANTS = [
    {
        'id': BAR_TENANT_ID,
        'name': 'BAR',
        'domain_id': DEFAULT_DOMAIN_ID,
        'description': 'description',
        'enabled': True,
        'parent_id': DEFAULT_DOMAIN_ID,
        'is_domain': False,
        'tags': []
    }, {
        'id': BAZ_TENANT_ID,
        'name': 'BAZ',
        'domain_id': DEFAULT_DOMAIN_ID,
        'description': 'description',
        'enabled': True,
        'parent_id': DEFAULT_DOMAIN_ID,
        'is_domain': False,
        'tags': []
    }, {
        'id': MTU_TENANT_ID,
        'name': 'MTU',
        'description': 'description',
        'enabled': True,
        'domain_id': DEFAULT_DOMAIN_ID,
        'parent_id': DEFAULT_DOMAIN_ID,
        'is_domain': False,
        'tags': []
    }, {
        'id': SERVICE_TENANT_ID,
        'name': 'service',
        'description': 'description',
        'enabled': True,
        'domain_id': DEFAULT_DOMAIN_ID,
        'parent_id': DEFAULT_DOMAIN_ID,
        'is_domain': False,
        'tags': []
    }
]

# NOTE(ja): a role of keystone_admin is done in setUp
USERS = [
    # NOTE(morganfainberg): Admin user for replacing admin_token_auth
    {
        'id': uuid.uuid4().hex,
        'name': 'req_admin',
        'domain_id': DEFAULT_DOMAIN_ID,
        'password': 'password',
        'tenants': [],
        'enabled': True,
        'options': {},
    },
    {
        'id': uuid.uuid4().hex,
        'name': 'foo',
        'domain_id': DEFAULT_DOMAIN_ID,
        'password': 'foo2',
        'tenants': [BAR_TENANT_ID],
        'enabled': True,
        'email': 'foo@bar.com',
        'options': {},
    }, {
        'id': uuid.uuid4().hex,
        'name': 'two',
        'domain_id': DEFAULT_DOMAIN_ID,
        'password': 'two2',
        'enabled': True,
        'default_project_id': BAZ_TENANT_ID,
        'tenants': [BAZ_TENANT_ID],
        'email': 'two@three.com',
        'options': {},
    }, {
        'id': uuid.uuid4().hex,
        'name': 'badguy',
        'domain_id': DEFAULT_DOMAIN_ID,
        'password': 'bad',
        'enabled': False,
        'default_project_id': BAZ_TENANT_ID,
        'tenants': [BAZ_TENANT_ID],
        'email': 'bad@guy.com',
        'options': {},
    }, {
        'id': uuid.uuid4().hex,
        'name': 'sna',
        'domain_id': DEFAULT_DOMAIN_ID,
        'password': 'snafu',
        'enabled': True,
        'tenants': [BAR_TENANT_ID],
        'email': 'sna@snl.coom',
        'options': {},
    }
]

ROLES = [
    {
        'id': ADMIN_ROLE_ID,
        'name': 'admin',
        'domain_id': None,
    }, {
        'id': MEMBER_ROLE_ID,
        'name': 'member',
        'domain_id': None,
    }, {
        'id': '9fe2ff9ee4384b1894a90878d3e92bab',
        'name': '_member_',
        'domain_id': None,
    }, {
        'id': OTHER_ROLE_ID,
        'name': 'other',
        'domain_id': None,
    }, {
        'id': uuid.uuid4().hex,
        'name': 'browser',
        'domain_id': None,
    }, {
        'id': uuid.uuid4().hex,
        'name': 'writer',
        'domain_id': None,
    }, {
        'id': uuid.uuid4().hex,
        'name': 'service',
        'domain_id': None,
    }
]

# NOTE(morganfainberg): Admin assignment for replacing admin_token_auth
ROLE_ASSIGNMENTS = [
    {
        'user': 'req_admin',
        'tenant_id': SERVICE_TENANT_ID,
        'role_id': ADMIN_ROLE_ID
    },
]

DOMAINS = [{'description':
            (u'The default domain'),
            'enabled': True,
            'id': DEFAULT_DOMAIN_ID,
            'name': u'Default'}]

SERVICES = [{'id': uuid.uuid4().hex,
             'type': 'type_one',
             'enabled': True,
             'extra': {'description': 'This is a service for test.',
                       'name': 'service_one'}
             }]

REGIONS = [{'id': 'region_one'}, {'id': 'region_two'}]
