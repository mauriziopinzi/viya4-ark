####################################################################
# ### viya_constants.py                                          ###
####################################################################
# ### Author: SAS Institute Inc.                                 ###
####################################################################
#                                                                ###
# Copyright (c) 2021-2022, SAS Institute Inc., Cary, NC, USA.    ###
# All Rights Reserved.                                           ###
# SPDX-License-Identifier: Apache-2.0                            ###
#                                                                ###
####################################################################

DISK_PRESSURE = 'False'
MEMORY_PRESSURE = 'False'
PID_PRESSURE = 'False'
# WORKER_MEMORY = '32779828Ki'
OS_IMAGE = 'CentOS Linux 7 (Core)'
NUMBER_OF_MASTER_NODES = 1
NUMBER_OF_WORKER_NODES = 1
SET = 'Current'
EXPECTED = 'Expected'
REVIEW_REQ = 'Review'
KEY_NOT_FOUND = 'Not Found'
INSUFFICIENT_PERMS = "Insufficient"
ADEQUATE_PERMS = "Adequate"
INGRESS_NGINX = "nginx"
INGRESS_ISTIO = "istio"
OPENSHIFT_INGRESS = "openshift"
NO_HOST_FOUND = "No_host_found"
INGRESS_CONTROLLER = "ingress_controller"
INGRESS_HOST = "ingress_host"
INGRESS_PORT = "ingress_port"
KUBECTL = "kubectl "
PERM_PERMISSIONS = "Permissions"
PERM_DEPLOYMENT = "Deployment"
PERM_SERVICE = "Service"
PERM_ROUTER = "Openshift Route"
PERM_AZ_FILE = "AzureFile Storage RWX"
PERM_AZ_FILE_PR = "AzureFilePremium Storage RWX"
PERM_AZ_DISK = "AzureDisk Storage"
PERM_AZ_DISK_STANDARD = "AzureDisk Standard Storage"
PERM_AWS_EBS = "AWS EBS Storage"
PERM_INGRESS = "Ingress"
PERM_SAMPLE_STATUS = "Sample Status"
PERM_CRD = "Custom Resource Definition"
PERM_CR = "Custom Resource"
PERM_STORAGE_CLASS = "Storage Class"
PERM_DELETE = "Delete "
PERM_CREATE = "Create "
PERM_GET = "Get "
KUBECTL_APPLY = " apply "
KUBECTL_DELETE = " delete "
PERM_SKIPPING = "Skipping"
PERM_REPLICASET = "ReplicaSet"
PERM_ROLE = "Role"
PERM_ROLEBINDING = "RoleBinding"
PERM_SA = "Service Account"
PERM_CLASS = "PreInstallUtils"
PERM_CR_RBAC = "Custom Resource with RBAC "
# Check cluster capacity for Memory against Percentage of Memory set in the viya_deployment_settings.ini
VIYA_PERCENTAGE_OF_INSTANCE = "85"
MEMORY_WITHIN_RANGE = " Memory within Range"
SERVER_K8S_VERSION = "Server_k8s_version"

# Any versions below this minimum are not supported
MIN_K8S_SERVER_VERSION = '<1.20'
