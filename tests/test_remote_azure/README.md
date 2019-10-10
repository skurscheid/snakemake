# Instruction for testing of Azure Storage integration
* in order to perform this test, an Azure Storage Account is required
* Both the storage account and an associated key or shared access signature (SAS) need to be passed to snakemake at runtime
* currently this is solved by setting and exporting environment variables called
** $AZURE_ACCOUNT
** $AZURE_KEY or
** $SAS_TOKEN
* furthermore, in the storage account, a container "snakemake-test" needs to be created prior to running the test
* Note regarding use of AZURE_KEY: The key associated with an Azure Storage account gives full permissions to all aspects
* of that specific Storage account. It is therefore not advisable to use this key outside of your own organization. An alternative
* to providing keys is the Shared Acess Signature which allows much more granular control of access privileges to a given
* storage account. The Azure Storage API accommodates the use of this transparently, and the SAS needs to be passed only at the time of instantiating AzureRemoteProvider 

