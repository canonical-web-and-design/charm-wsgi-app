# The Webteam WSGI charm

## No longer maintained

This charm was written for us to use in our deployed environments for our websites, instead of [the old one](https://launchpad.net/wsgi-app-charm). But we never got around to actually using the new charm.

We now run almost all our services in Kubernetes, and so I don't see us ever actually using this charm, and so we will no longer be maintaining this charm.

However, I do believe this charm and its associated layers ([layer-wsgi](https://github.com/canonical-webteam/layer-wsgi) and [layer-untar-resources](https://github.com/canonical-webteam/layer-untar-resources/)) are fairly well written and could be useful to anyone wanting to run a WSGI app with Juju.

Please let me (@nottrobin) know if you want to take over this project.

---

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
