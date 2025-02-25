# umd-fcrepo-solr: fcrepo core

UMD Libraries Solr Index for Fedora (fcrepo core)

## Key Components

* [Solr] index

## Docker Image

Uses the [Solr Docker base image](https://hub.docker.com/_/solr/), Solr 
version 9.6.1.

[Dockerfile](Dockerfile)

### Volumes

| Mount point                  | Purpose              |
|------------------------------|----------------------|
| `/var/solr/data/fcrepo/data` | Persistent core data |

### Ports

| Port number | Purpose                  |
|-------------|--------------------------|
| 8983        | Solr web admin interface |

### Build

Clone the [umd-fcrepo-solr] repository and switch to the `fedora4` directory:

```zsh
git clone git@github.com:umd-lib/umd-fcrepo-solr.git
cd umd-fcrepo-solr/fcrepo
```

Build the image:

```bash
docker build -t docker.lib.umd.edu/fcrepo-solr-fcrepo .
```

### Run

```bash
docker run -it --rm --name fcrepo-solr-fcrepo \
    -p 8985:8983 \
    docker.lib.umd.edu/fcrepo-solr-fcrepo
```

The Solr web admin console will be at <http://localhost:8985/solr/#/>

**Note:** The convention is to run this core's container port-mapped to
port 8985 (instead of 8983) to avoid conflicts with the [fedora4 core][../fedora4].

## License

See the [LICENSE](../LICENSE) file for license rights and limitations (Apache 2.0).


[Solr]: https://solr.apache.org/
[umd-fcrepo-solr]: https://github.com/umd-lib/umd-fcrepo-solr
