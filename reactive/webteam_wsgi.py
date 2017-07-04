# Core packages
import os

# Third-party packages
from charmhelpers.core.hookenv import config, status_set
from charmhelpers.core.templating import render
from charms.reactive import (
    hook,
    is_state,
    remove_state,
    set_state,
    when,
)


@when('resources.build.available')
def update():
    remove_state('resources.build.available')
    set_state('wsgi.source.available')


@hook('verify-relation-joined')
def setup_http_check():
    """
    Setup HTTP check
    """

    status_set('maintenance', '[wsgi-app] Installing HTTP check')
    render(
        source='check_webservice.cfg.jinja2',
        target='/etc/nagios/nrpe.d/check_webservice.cfg',
        perms=0o444,
        context=config(),
    )
    status_set('maintenance', '[wsgi-app] Installed HTTP check')


@hook('update-status')
def update_status():
    if not os.listdir('/srv') or is_state('resources.build.missing'):
        build_missing()
    elif is_state('wsgi.available'):
        build_deployed()


@when('resources.build.missing')
def build_missing():
    status_set('blocked', '"build" resource missing: Please attach a build')


@when('wsgi.available')
def build_deployed():
    build_filepath = '/srv/BUILD_LABEL'
    port = config('port')

    if os.path.exists(build_filepath):
        with open(build_filepath) as build_file:
            build_label = build_file.read().strip()

        status_set(
            'active',
            'Build {build_label} running on port {port}'.format(**locals())
        )
    else:
        status_set(
            'active',
            'Latest build running on port {port}'.format(**locals())
        )
