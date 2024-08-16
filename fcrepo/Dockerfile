# Dockerfile for the generating the Solr image
#
# To build:
#
# docker build -t docker.lib.umd.edu/fcrepo-solr-fcrepo:<VERSION> -f Dockerfile .
#
# where <VERSION> is the Docker image version to create.
FROM solr:9.6.1-slim
USER root
COPY --chown=solr:solr core /var/solr/data/fcrepo/
USER solr
RUN mkdir -p /var/solr/data/fcrepo/data
VOLUME /var/solr/data/fcrepo/data
CMD ["bin/solr", "start", "-f"]
