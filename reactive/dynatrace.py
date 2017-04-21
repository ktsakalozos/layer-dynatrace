#!/usr/bin/env python

# Copyright 2015 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from shlex import split
from subprocess import check_call
from charms.reactive import set_state
from charms.reactive import when, when_any, when_not
from charmhelpers.core import hookenv
from charmhelpers.core.templating import render


@when_not('dynatrace.installed')
def install():
    '''Unpack and put the Dynatrace on the right places.'''
    hookenv.status_set('maintenance', 'Installing Dynatrace Agent.')

    env_id = hookenv.config('env_id')
    token = hookenv.config('token')
    if env_id == '' or token == '':
        hookenv.status_set('blocked', 'Please provide a environemnt ID and token')
        return

    connection_ep = hookenv.config('connection_ep')
    if connection_ep == '':
        connection_ep = "https://{}.live.dynatrace.com".format(env_id)

    context = {}
    context.update({'ENVIRONMENT_ID': env_id,
                    'CONNECTION_ENDPOINT': connection_ep,
                    'YOUR_TOKEN': token})

    render('dynatrace.yaml', '/var/tmp/dynatrace.yaml', context)
    command = '/snap/bin/kubectl create -f /var/tmp/dynatrace.yaml'
    hookenv.log(command)
    check_call(split(command))

    hookenv.status_set('active', 'Dynatrace Agent is Ready')
    set_state('dynatrace.installed')
