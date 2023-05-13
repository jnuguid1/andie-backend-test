from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST, require_GET

from account.models import Account, Activity, Business, Item, Order

# Create your views here.
@csrf_protect
@csrf_exempt
@require_POST
def create_account(request):
  data = request.POST
  new_account = Account(
      username=data.get("username", "user"), 
      password=data.get("password", "pass123"), 
      full_name=data.get("full_name", "Bob M"),
      email=data.get("email", "bob@mail.com"),
      phone_number=data.get("phone", "555555555"),
    )
  new_account.save()
  activity = Activity(account=new_account, page_visits=[])
  activity.save()
  response = "You are creating an account"
  return HttpResponse(response)

@csrf_protect
@csrf_exempt
@require_POST
def delete_account(request):
  data = request.POST
  account = get_object_or_404(Account, pk=data.get("id"))
  account.delete()
  response = "you are deleting an account"
  return HttpResponse(account)

@csrf_protect
@csrf_exempt
@require_GET
def login(request):
  data = request.GET
  account = get_object_or_404(
    Account, 
    username=data.get("username"), 
    password=data.get("password"),
  )
  return HttpResponse(account)

@csrf_protect
@csrf_exempt
@require_POST
def update_activity(request):
  data = request.POST
  activity = get_object_or_404(
    Activity, 
    account=Account.objects.get(pk=data.get("id"))
  )
  try:
    visits = activity.page_visits
    if len(visits) >= 5:
      visits.pop(0)
    visits.append(data.get("activity_data", "new_activity_data"))
    activity.page_visits = visits
    activity.save()
  except (KeyError, Activity.DoesNotExist):
    return Http404('Account not found')
  return HttpResponse(activity)

@csrf_protect
@csrf_exempt
@require_POST
def create_business(request):
  data = request.POST
  new_business = Business(
    business_name=data.get("business_name", "business123"),
    category=data.get("category"),
    location=data.get("location"),
    phone_number=data.get("phone_number"),
  )
  new_business.save()
  response = "You are creating a business"
  return HttpResponse(response)

@csrf_protect
@csrf_exempt
@require_POST
def delete_business(request):
  data = request.POST
  business = get_object_or_404(Business, pk=data.get("id"))
  business.delete()
  response = "You are deleting a business"
  return HttpResponse(response)

@csrf_protect
@csrf_exempt
@require_POST
def create_item(request):
  data = request.POST
  business = get_object_or_404(Business, pk=data.get("business_id"))
  try:
    business.item_set.create(
      item_name=data.get("item_name", "new item"),
      category=data.get("category", "item category"),
      price=data.get("price", 0.0),
      quantity=data.get("quantity", 2),
    )
    response = "You are creating an item"
    return HttpResponse(response)
  except (KeyError, Item.DoesNotExist):
    return Http404("Business does not exist")


@csrf_protect
@csrf_exempt
@require_POST
def delete_item(request):
  data=request.POST
  item = get_object_or_404(Item, pk=data.get("item_id"))
  item.delete()
  response = "You are deleting an item"
  return HttpResponse(response)

@csrf_protect
@csrf_exempt
@require_POST
def edit_item(request):
  data=request.POST
  item_attribute = data.get("item_attribute")
  new_value = data.get("new_value")
  response="You are editing an item"
  item = get_object_or_404(Item, pk=data.get("item_id"))
  try:
    if item_attribute == "item_name":
      item.item_name = new_value
      item.save()
    elif item_attribute == "category":
      item.category = new_value
      item.save()
    elif item_attribute == "price":
      item.price = new_value
      item.save()
    elif item_attribute == "quantity":
      item.quantity = new_value
      item.save()
    else:
        return Http404("Invalid attribute")
    return HttpResponse(response)
  except (KeyError, Item.DoesNotExist):
    return Http404("Item does not exist")

@csrf_protect
@csrf_exempt
@require_POST
def create_order(request):
  data=request.POST
  order=Order(
    business=Business.objects.get(pk=data.get("business_id")),
    account=Account.objects.get(pk=data.get("account_id")),
    products=[],
    tax=data.get("tax", 0.00)
  )
  order.save()
  return HttpResponse(order)

@csrf_protect
@csrf_exempt
@require_GET
def get_all_orders(request):
  orders=Order.objects.all()
  return HttpResponse(orders)

@csrf_protect
@csrf_exempt
@require_GET
def get_orders_by_id(request):
  data=request.GET
  account=Account.objects.get(pk=data.get("account_id"))
  orders=account.order_set.all()
  return HttpResponse(orders)
