FROM registry.centos.org/openshift/jenkins-slave-base-centos7

RUN yum update -y && \
    yum install -y PyYAML python-requests docker mailx postfix epel-release && \
    yum install -y npm buildah && \
    yum clean all && \
    npm install -g dockerfile_lint

ADD ./ /opt/ccp-openshift/
VOLUME ["/opt/ccp-openshift/ccp/scanning", "/var/lib/containers"]
