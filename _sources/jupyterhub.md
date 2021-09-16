

## Setting up JupyterHub for the students

follow instruction on https://zero-to-jupyterhub.readthedocs.io/

### 2021-09-13

- finished [Setting up Kubernetes on Google](https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/google/step-zero-gcp.html)

      gcloud container clusters create   --machine-type n1-standard-2   --num-nodes 2   --zone europe-west6-a   --cluster-version latest agi-hs21
      kubectl create clusterrolebinding cluster-admin-binding \
      >   --clusterrole=cluster-admin \
      >   --user=nilsratnaweera@hotmail.com

- next step: [Setting up Helm](https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/setup-helm.html#setup-helm)

