Fast API assignment

We are looking to build an e-commerce application with following features -
    1. Users can sign up, login and purchase available products of various brands. Username is unique for each user.
    2. Platform admin can add/remove tenants(brands) and manage tenant users. Only users with admin role can be assumed as platform admins.
    3. Tenants can login to their domain to add/update/remove products of their own brand. Further, they can also manage the available quantity of products. Tenant user can login as a regular user to purchase products.
    4. Tenant user cannot login to another tenant’s domain
    5. Products can be categorized and filtered based on category.
    6. Products can be searched by their name. List all products that contains the search field in their name.
    7. Users can create order items. An order item consists of product and quantity.
    8. An order item for a product can be created only when the quantity is less than its available quantity.
    9. An order consists of order items, total quantity and total amount.
    10. Users can view their order history.
Build an application with FastAPI and implement login with Keycloak. You are expected to - 
    1. Define Models for Tenant, User, Role, Product, Order and OrderItems with correct mapping.
    2. Implement multi-tenancy for brands. Endpoints should be at tenant level (/tenantName/endpoint).
    3. Add necessary endpoints and routing to carry out each task.
    4. Adhere to the permissions and privileges to each role – Admin, Tenant and User roles.
    5. Implement pagination wherever necessary.
    6. Implement error handling wherever required.
    7. Add unit tests for each task. 
Bonus - Implement favourite product for users. User should be able to mark/unmark a product as favourite and retrieve the list of favourite products.


Suggested Routes and Their Functionalities:
User Routes:

Sign Up: Allow users to sign up.
Login: Allow users to log in.
Get All Users: Admins can view all users.
Get Single User: View a single user's details.
Update User: Update user details.
Delete User: Delete a user.
Tenant Routes:

Add Tenant: Admins can add new tenants.
Remove Tenant: Admins can remove tenants.
Get All Tenants: View all tenants.
Get Single Tenant: View a single tenant's details.
Update Tenant: Update tenant details.
Product Routes:

Add Product: Tenants can add new products.
Update Product: Tenants can update product details.
Remove Product: Tenants can remove products.
Get All Products: View all products.
Get Single Product: View a single product's details.
Search Products: Search products by name.
Filter Products: Filter products by category.
Order Routes:

Create Order: Users can create orders.
Get All Orders: View all orders.
Get Single Order: View a single order's details.
Update Order: Update order details.
Delete Order: Delete an order.
View Order History: Users can view their order history.
Order Item Routes:

Add Order Item: Users can add items to an order.
Update Order Item: Update order item details.
Remove Order Item: Remove an item from an order.
