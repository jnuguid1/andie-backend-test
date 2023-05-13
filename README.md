# andie-backend-test
For all POST views, request data should be stored in the body of the HTTP request as form data because I used request.POST for each function.  
For all GET views, data should be stored in the params of the request.  
  
Each view expects certain keys in the body/params which are detailed below:  
  
create_account function: username, password, full_name, email, phone  
delete _account function: id  
login function: username, password  
update_activity function: id, activity_data  
create_business function: business_name, category, location, phone_number  
delete_business function: id  
create_item function: business_id, item_name  
delete_item function: item_id  
edit_item function: item_attribute, new_value, item_id  
create_order: business_id, account_id, tax  
get_order_by_id function: account_id  

Login html response returns login details from successful login in the headers.  
get_all_orders and get_orders_by_id return a json as the response.
