from controllers.customers import CustomerController
from flask import request

def customerRoutes(app):
  @app.route("/customers")
  def list():
    return CustomerController.list(request).to_json()

  @app.route("/customers/<customerId>")
  def getOne(customerId):
    return CustomerController.getOne(request, customerId).to_json()

  @app.route("/customers/search")
  def search():
    return CustomerController.search(request).to_json()

  return {"list": list, "getOne": getOne, "search": search}