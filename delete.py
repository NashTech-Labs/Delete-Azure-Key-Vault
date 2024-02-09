from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.mgmt.keyvault import KeyVaultManagementClient

def delete_keyvault(vault_url, subscription_id, resource_group, keyvault_name):
    # Initialize the Key Vault client
    credential = DefaultAzureCredential()
    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    client = KeyVaultManagementClient(credential, subscription_id)
    
    # Delete the Key Vault
    client.vaults.delete(resource_group, keyvault_name)

# Example usage:
vault_url = "https://<your-key-vault-name>.vault.azure.net/"
subscription_id = "<your-subscription-id>"
resource_group = "<your-resource-group>"
keyvault_name = "<your-key-vault-name>"

delete_keyvault(vault_url, subscription_id, resource_group, keyvault_name)
