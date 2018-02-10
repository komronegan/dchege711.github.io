import os

SMMRY_API_KEY = os.environ["SMMRY_API_KEY"]

google_cloud_config = {
    "type": os.environ["gcloud_type"],
    "project_id": os.environ["gcloud_project_id"],
    "private_key_id": os.environ["gcloud_private_key_id"],
    "private_key": os.environ["gcloud_private_key"],
    "client_email": os.environ["gcloud_client_email"],
    "client_id": os.environ["gcloud_client_id"],
    "auth_uri": os.environ["gcloud_auth_uri"],
    "token_uri": os.environ["gcloud_token_uri"],
    "auth_provider_x509_cert_url": os.environ["gcloud_auth_provider_x509_cert_url"],
    "client_x509_cert_url": os.environ["gcloud_client_x509_cert_url"]
}
