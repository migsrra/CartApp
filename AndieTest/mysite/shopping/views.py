from django.shortcuts import render
from django.http import HttpResponse
from shopping.models import Account,Activity,Business,Inventory,Order
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

#This is just the default page view
def index(request):
    return HttpResponse("This is the view for the shopping app.")

#Function that creates an account, while creating an activity alongside it
@csrf_exempt
def createAccount(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        fullName = request.POST.get('full name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phone number')
        
        newAccount = Account(
            username = username,
            password = password,
            fullName = fullName,
            email = email,
            phoneNumber = phoneNumber
        )
        newAccount.save()
        
        newActivity = Activity(accountID = newAccount)
        newActivity.save()
        
        output = f"Congratulations {newAccount.fullName}, your account has been created with ID: {newAccount.ID}."
        return HttpResponse(output)
    else:
        return HttpResponse("Invalid Method",status=405)

#Functions that allows for account deletion
@csrf_exempt
def deleteAccount(request,accountID):
    #accountID = request.GET.get('accountID')
    
    #the above is for if we want to pass query parameters in Postman rather than modifying the 
    #target URL. If you would like to switch to this, remove the '<int:accountID>' in the deleteAccount path
    #in urls.py, and comment out the 'accountID' parameter in this function header. This applies to any view 
    #function that has parameters passed in the header
    
    try:
        record = Account.objects.get(ID = accountID)
    except:
        raise Http404("This account does not exist.")
    
    userToDelete = record.username    
    record.delete()
    output = f"{userToDelete}, your account has been deleted."
    return HttpResponse(output)   

#Function that allows for login and retrieval of account activity
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            accountToLogin = Account.objects.get(username = username,password = password)
            accountActivity = Activity.objects.filter(accountID = accountToLogin).first() 
            history = accountActivity.visitHistory
            
            output = f"Welcome {accountToLogin.username}. Here is your recent activity:\n {history}"
            return HttpResponse(output)
            
        except:
            raise Http404("Username or password not valid.")
        
    else:
        return HttpResponse("Invalid Method.",status=405)

#Function that edits an accounts activity model, appending the latestPage to it and removes the oldest
#visitHistory string if the length of visitHistory is more than five
@csrf_exempt
def editActivity(request,accountID):
    try:
        account = Account.objects.get(ID = accountID)
    except:
        raise Http404("This account does not exist.")
    
    activityToEdit = Activity.objects.filter(accountID = account).first()   
    
    if request.method == 'POST':
        latestPage = request.POST.get('latestPage')
        history = activityToEdit.visitHistory
        history.append(latestPage)
        
        if len(history) > 5:
            history = history[-5:]
        activityToEdit.visitHistory = history
        activityToEdit.save()
        
        return HttpResponse('Successfully edited account activity.')
    else:
        return HttpResponse("Invalid method.",status=405)

#Function that creates a business
@csrf_exempt
def createBusiness(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        location = request.POST.get('location')
        phoneNumber = request.POST.get('phone')
        
        newBusiness = Business(
            name = name,
            category = category,
            location = location,
            phoneNumber = phoneNumber
        )
        newBusiness.save()
        
        output = f"Your business, {newBusiness.name}, has been created with the ID: {newBusiness.ID}."
        return HttpResponse(output)
    else:
        return HttpResponse("Invalid method.",status=405)

#Function that deletes a business
@csrf_exempt 
def deleteBusiness(request,businessID):
    #businessID = request.GET.get('businessID')
    
    #the above is for if we want to pass query parameters in Postman rather than modifying the 
    #target URL. If you would like to switch to this, remove the '<int:accountID>' in the deleteBusiness path
    #in urls.py, and comment out the 'businessID' parameter in this function header.
    
    try:
        business = Business.objects.get(ID = businessID)
    except:
        raise Http404("This business does not exist.")
    
    businessNameToDelete = business.name
    business.delete()
    output = f"Business titled {businessNameToDelete} has been deleted."
    return HttpResponse(output)

#Function that creates an Inventory item
@csrf_exempt 
def createInventoryItem(request,businessID): #Assuming businessID attributed to item is also passed  
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        
        try:
            business = Business.objects.get(ID = businessID)
        except:
            raise Http404("Business specified does not exist.")
        
        newItem = Inventory(
            businessID = business,
            name = name,
            category = category,
            price = price,
            quantity = quantity
        )
        newItem.save()
        
        output = f"{newItem.name} has been added to the inventory for {business.name} with ID: {newItem.ID}."
        return HttpResponse(output)
    else:
        return HttpResponse("Invalid Method.",status=405)

#Function to delete an Inventory item
@csrf_exempt  
def deleteInventoryItem(request, inventoryID):
    try:
        itemToDelete = Inventory.objects.get(ID = inventoryID)
    except:
        raise Http404("This inventory item does not exist.")
    
    itemNameToDelete = itemToDelete.name
    itemToDelete.delete()
    output = f"Item titled {itemNameToDelete} has been deleted."
    return HttpResponse(output)

#Function to edit an Inventory item
@csrf_exempt
def editInventoryItem(request,inventoryID):
    try:
        itemToModify = Inventory.objects.get(ID = inventoryID)
    except:
        raise Http404("This inventory item does not exist")
    
    if request.method == 'POST':
        newName = request.POST.get('newName')
        newCategory = request.POST.get('newCategory')
        newPrice = request.POST.get('newPrice')
        newQuantity = request.POST.get('newQuantity')
        
        oldName = itemToModify.name
        itemToModify.name = newName
        itemToModify.category = newCategory
        itemToModify.price = newPrice
        itemToModify.quantity = newQuantity
        
        itemToModify.save()
        
        output = f"{oldName} item information has been modified to:\n Name: {itemToModify.name}\n \
            Category: {itemToModify.category}\n Price: {itemToModify.price}\n Quantity: {itemToModify.quantity}"
            
        return HttpResponse(output)
    else:
        return HttpResponse("Invalid method.",status=405)

#Below functions are for part 3 of the test
#This function creates an order object after checking to see if the products are valid
@csrf_exempt
def createOrder(request,businessID,accountID):
    if request.method == 'POST':
        #Checking if account and business exists
        try: 
            account = Account.objects.get(ID = accountID) 
        except:
            raise Http404("Account specified does not exist")
        try:
            business = Business.objects.get(ID = businessID)
        except:
            raise Http404("Business specified does not exist")
        
        
        #Acquire the JSONField list of products
        products = request.POST.get('products')
        products_dict = json.loads(products) #converts json string to dictionary object
        
        #Now we check to see if the order items are contained within the specified business,
        #And if there quantities are valid (More than one and less than total inventory amount)
        order_list = []
        for key,quantity in products_dict.items():
            try:
                product = Inventory.objects.get(ID = key,businessID = business)
            except:
                output = f"Product with ID {key}, is not present in this businesses."
                return HttpResponse(output,status=400)
            if quantity < 1:
                output = f"You cannot order less than one of {product.name}."
                return HttpResponse(output,status=400)
            elif quantity > product.quantity:
                output = f"This business does not have enough of {product.name} to statisfy your order."
                return HttpResponse(output,status=400)
            
            order_list.append({'product':product.ID,'quantity':quantity})
            
        order = Order(businessID = business,accountID = account)    
        order.products = order_list
        order.save()
        
        output = f"Order with ID {order.ID} was created {order.dateTime.strftime('%Y-%m-%d %H:%M')}. It has: \n {order.products}"
        return HttpResponse(output)
    else:
        return HttpResponse("Invalid Method.",status=405)

#Function that gets all orders that have been made and outputs them via a JsonResponse            
@csrf_exempt
def getAllOrders(request):
    allOrders = Order.objects.all() 
    order_list = []   
    for order in allOrders:
        currOrderDictionary = {
            'ID': order.ID,
            'businessID': order.businessID.ID,
            'accountID': order.accountID.ID,
            'products': order.products,
            'dateTime': order.dateTime.strftime('%Y-%m-%d %H:%M')
        }
        order_list.append(currOrderDictionary)
    return JsonResponse(order_list,safe=False)

#Function that gets all orders an account has made and outputs them via a JsonResponse
@csrf_exempt 
def getAccountOrders(request,accountID):
    try:
        account = Account.objects.get(ID = accountID)
    except:
        return Http404("Could not find specified account.")
    
    accountOrders = Order.objects.filter(accountID = account)
    order_list = []
    for order in accountOrders:
        currOrderDictionary = {
            'ID': order.ID,
            'businessID': order.businessID.ID,
            'accountID': order.accountID.ID,
            'products': order.products,
            'dateTime': order.dateTime.strftime('%Y-%m-%d %H:%M')
        }
        order_list.append(currOrderDictionary)
    return JsonResponse(order_list,safe=False)

#Extra function that finds order total given orderID
@csrf_exempt
def getOrderTotal(request,orderID):
    try:
        order = Order.objects.get(ID = orderID)
    except:
        return HttpResponse("The order specified does not exist.")

    orderTotal = 0
    for dict in order.products:
        currID = dict['product']
        currItem = Inventory.objects.get(ID = currID)
        singleItemPrice = currItem.price
        amountCurrProduct = float(singleItemPrice)*float(dict['quantity'])
        
        orderTotal = orderTotal + amountCurrProduct
    
    output = f"The order total comes to ${orderTotal} for orderID: {orderID}"
    return HttpResponse(output)

        
        
        
                
        
        


    
    
    


    
            
        
        
        
        
      
    

        
