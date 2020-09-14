# MySQL_Flask_Redis_Docker_Project


The main idea is to dockerize an E-voting application based on the blockchain Technologie :

  1- Using Flask µ-framework to build the backend.
  2- Using Redis as a cache memory.
  3- Breaking the monolithic architecture into microservices
  4- Using the blockchain technologie for data security. 
  5- Public Ledger to verify the votes.
  6- Creating wallets using the ECC algorithm to create-sign-verify transactions. 
  7- Using different cryptographic algorithms to encrypt data such as : Bcrypt and SHA256.
  8- Dockerizing the application.
  
So far, it's just a test to add citizens in the Admin_DB + Redis, extract citizens informations + comparing the latency of reading from a mysql database vs redis + using YAML to configure and scale services + Dockerizing these basics functionnalities.
  
