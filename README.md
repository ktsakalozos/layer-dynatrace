# Dynatrace

Dynatrace APM tools provide user experience analysis that identifies and resolves application performance issues faster than ever before.

## Deployment

This charm is a subordinate of Kubernetes master, therefore you should have a
Kubernetes deployment already in place.

Please take a look at the [Canonical Distribution of Kubernetes](https://jujucharms.com/canonical-kubernetes/)
or the [Kubernetes core](https://jujucharms.com/kubernetes-core/) bundles for 
examples of complete models of Kubernetes clusters.

Since the Dynatrace needs priviliged containers you should also make sure this option in enabled in the Kuberneted deployment:

    juju config kubernetes-master allow-privileged=true
    juju config kubernetes-worker allow-privileged=true

Deploying the Instana charm is done with:

    juju deploy cs:~dynatrace-charms/dynatrace
    juju add-relation kubernetes-master dynatrace

At this point the charm should be 'blocked' prompting you to provide the token and the environment id.

    juju config dynatrace env_id=<your_env_id_provided_by_dynatrace>
    juju config dynatrace token=<your_token_provided_by_dynatrace>


# More information

 - [Kubernetes github project](https://github.com/kubernetes/kubernetes)
 - [Dynatrace](https://www.dynatrace.com/)
