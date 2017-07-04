# The Webteam WSGI charm

This is the [Juju charm](https://jujucharms.com) for serving the Canonical Webteam's Python [WSGI](https://wsgi.readthedocs.io/en/latest/) applications.

## Basic usage

After being deployed with Juju, the charm needs to be configured with the location of your WSGI module, and then provided with a `.tar.gz` file containing your application code:

``` bash
juju deploy cs:~cwebteam/wsgi-app
juju config wsgi-app wsgi=myapplication.wsgi
juju attach wsgi-app build=./myapplication.tar.gz
```

## Development

This charm is built from two charm layers:

- [layer-wsgi](https://github.com/canonical-webteam/layer-wsgi)
- [layer-untar-resources](https://github.com/canonical-webteam/layer-untar-resources)

To build the charm locally, follow [the documentation](https://jujucharms.com/docs/2.1/developer-getting-started#assemble-the-layers).
