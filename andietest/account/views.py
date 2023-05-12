from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST

from account.models import Account, Activity, Business, Item

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
  activity = Activity(account=new_account, page_visits={})
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
