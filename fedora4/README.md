# umd-fcrepo-solr: fedora4 core

UMD Libraries Solr Index for Fedora (fedora4 core)

## Key Components

* [Solr] index

## Docker Image

Uses the [Solr Docker base image](https://hub.docker.com/_/solr/), Solr 
version 7.7.3.

[Dockerfile](Dockerfile)

### Volumes

| Mount point     | Purpose              |
|-----------------|----------------------|
| `/var/opt/solr` | Persistent core data |

### Ports

| Port number | Purpose                  |
|-------------|--------------------------|
| 8983        | Solr web admin interface |

### Build

Clone the [umd-fcrepo-solr] repository and switch to the `fedora4` directory:

```zsh
git clone git@github.com:umd-lib/umd-fcrepo-solr.git
cd umd-fcrepo-solr/fedora4
```

Build the image:

```zsh
docker build -t docker.lib.umd.edu/fcrepo-solr-fedora4 .
```

### Run

```zsh
docker run -it --rm --name fcrepo-solr-fedora4 \
    -p 8983:8983 \
    docker.lib.umd.edu/fcrepo-solr-fedora4
```

The Solr web admin console will be at <http://localhost:8983/solr/#/>

The Java heap size can be controlled by setting the environment variable
`SOLR_FEDORA4_HEAP_SIZE`. The default if it is not set is `1024m`.

## History

This code comes from the
[solr-fedora4](https://github.com/umd-lib/umd-fcrepo-docker/tree/1.0.1/solr-fedora4)
subdirectory of the [umd-fcrepo-docker] project at the 1.0.1 release.

## License

See the [LICENSE](../LICENSE) file for license rights and limitations (Apache 2.0).


[Solr]: https://solr.apache.org/
[umd-fcrepo-solr]: https://github.com/umd-lib/umd-fcrepo-solr
[umd-fcrepo-docker]: https://github.com/umd-lib/umd-fcrepo-docker
[pytest]: https://pypi.org/project/pytest/
