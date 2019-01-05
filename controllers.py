from models import Customers

class CustomerController():
  @staticmethod
  def list(request):
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit

    return Customers.objects.skip( offset ).limit( limit )
  
  @staticmethod
  def getOne(request, customerId):
    return Customers.objects.get(id=customerId)
  
  @staticmethod
  def search(request):
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))
    offset = (page - 1) * limit
    query = request.args.get('qs', '')
    return Customers.objects.search_text(query).skip( offset ).limit( limit )
    