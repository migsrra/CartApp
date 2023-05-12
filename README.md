# InternshipTest
This Django app is titled "shopping", as seen in the file paths. Here is a link to the Postman workspace I used to test this project: https://www.postman.com/migsrra/workspace/andie-test-workspace/collection/27372112-e16d9981-7068-4d51-a0ce-3850cac35823?action=share&creator=27372112. The requirements to this test went as follows:

1. Create a model system containing the following models and model
fields.

Account Model

  ○ ID (primary key)
  
  ○ Username
  
  ○ Password
  
  ○ Full name
  
  ○ Email
  
  ○ Phone number


Account Activity Model

  ○ ID (primary key)
  
  ○ Account ID (foreign key referencing Account Model)
  
  ○ Page visit history (array field that only stores the last 5 pages)


Business Model

  ○ ID (primary key)
  
  ○ Business name
  
  ○ Category
  
  ○ Location (optional, default is null)
  
  ○ Phone number


Inventory Item Model

  ○ ID (primary key)
  
  ○ Business ID (foreign key referencing Business Model)
  
  ○ Name
  
  ○ Category
  
  ○ Price
  
  ○ Quantity (optional, default to 1)
  

2. Using the models created above, create the following functions:

NOTE: You do not need to deal with bearer token generation and password protection
for this test.

● Create an account

  ○ NOTE: The Account Activity Model should be created alongside
    the Account Model


● Delete an account given its ID

  ○ The account activity associated with the account should also be
    deleted (HINT: Look at the ON_DELETE parameter for foreign
    keys)


● Login function for Account

  ○ Verify that the username and password are valid, otherwise throw
  error
  
  ○ Retrieve the account and it’s activity if valid


● Edit an Account’s connected activity model

  ○ You must do this given only the Account’s ID
  
  ○ This function should just append the latest page visited onto the
    field, and remove the oldest page visited
    

● Create a Business


● Delete a business given its ID

  ○ Inventory should also be deleted when a business is deleted
  

● Create an inventory item


● Delete an inventory item given its ID


● Edit any inventory item field (except for ID and business ID)


3. Once the model instances are successfully created, create a cart
system:

● For this, you will need to create an additional model to store the order
information

  ○ It will need to reference both the business and the account that is
  
    placing the order
  ○ For the products in the order, you will need to store them into a
    JSON field
    
    ■ All you need is the product ID and quantity in the JSON field
    
  ○ Add any other fields you think would be useful in an order
  
  
● Create a function to create an order


● Create a function to get all orders


● Create a function to get orders given a certain Account ID


● If you wish to add any other fields or helper functions onto the cart, you
  may do so at your discretion
  
For the third part, I added a funcion that calculates the total order cost of any order.
