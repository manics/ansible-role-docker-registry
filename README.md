Docker Registry
===============

Setup a Docker Registry, managed with Systemd.
This is a development role.
Authentication is not currently enabled.

Requires Docker on the host system (not automatically installed).


Role Variables
--------------

Optional variables:
- `docker_registry_storage_directory`: Directory for storing Docker Registry data, you may want to use an alternative location due to the size of Docker images
- `docker_registry_storage_directory_wait`: Maximum time to wait for the storage directory to appear before starting the registry in seconds (useful for remote mounts), default disabled
- `docker_registry_version`: Docker registry image version, you probably shouldn't touch this
- `docker_registry_listen_port`: Listen on this port, default `5000`


Example Playbook
----------------

Simple example (uses default storage overlay driver):

    - hosts: localhost
      roles:
        - role: openmicroscopy.docker
        - role: openmicroscopy.docker-registry


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk
