# Dockerfile for the generating the Solr image
#
# To build:
#
# docker build -t docker.lib.umd.edu/fcrepo-solr-fedora4:<VERSION> -f Dockerfile .
#
# where <VERSION> is the Docker image version to create.
FROM solr:7.7.3-slim
USER root
COPY --chown=solr:solr solr.in.sh /opt/solr/bin/
COPY --chown=solr:solr core /opt/solr/server/solr/mycores/fedora4/
RUN mkdir -p /var/opt/solr && chown solr:solr /var/opt/solr
VOLUME /var/opt/solr
USER solr
CMD ["bin/solr", "start", "-f"]
