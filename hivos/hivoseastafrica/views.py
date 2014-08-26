from django.http import HttpResponseRedirect
from usermanagement.models import Menus
from services.views import *
from fundmanagement.views import *
from masterdata.views import *
from hrmanagement.views import *
from farmer.views import *
from meeting.views import *
from usermanagement.views import *
from events.views import *
from saccos.views import *
from inventory.views import *
from sharemanagement.views import *
from VAM.views import *
from procurement.views import *
from reports.views import *
from loan_management.views import *
from account_management.views import *
from loan_management.reports import *

def redirect_to(request, slug = None):
    try:
        key = request.GET.get('key')
        menus = Menus.objects.get(slug=slug)
        if menus.slug == "fund-management":
            return fundmgmt_home(request)
        elif menus.slug == "master-data":
            return master_data(request)
        elif menus.slug == "hr-management":
            from hrmanagement.views import main_data
            return main_data(request)
        elif menus.slug == "member":
            return farmer_home(request)
        elif menus.slug == "meeting":
            return meeting_data(request)
        elif menus.slug == "admin":
            return usermanagement_data(request)
        elif menus.slug == "events":
            return events_data(request)
        elif menus.slug == "saccos":
            return saccos_home(request)
        elif menus.slug == "projects":
            from projects.views import main_data
            return main_data(request)
        elif menus.slug == "budgets":
            from budget.views import main_data
            return main_data(request)
        elif menus.slug == "inventory":
            return inventory_data(request)
        elif menus.slug == "sharemanagement":
            return sharemanagement_data(request)
        elif menus.slug == "farmer-cultivate-detail":
            return farmer_cultivation(request)
        elif menus.slug == "procurement":
            return procurement_data(request)

        elif menus.slug in ["country", "sub-county", "master-data-service", 
                            "county", "village", "master-data-farmer", 
                            "master-data-hr-management", 
                            "master-data-share-management", 
                            "master-data-projects", "master-data-events",
                            "master-data-fund-management",
                            "master-data-inventory"]:
            return master_data(request)
        elif menus.slug == "service":
            return service_home(request)
        elif menus.slug == "loan":
            return loan_management_data(request)
        elif menus.slug == "configuration":
            return account_management_data(request)
        elif menus.slug == "saving-account":
            return create_new_functions(request)
        elif menus.slug == "transaction":
            return transaction_functions(request)
        elif menus.slug == "loan-process":
            return loan_process_functions(request)
        elif menus.slug == "loan-reports":
            return loan_report_function(request)
        elif menus.slug == "manage-productivity":
            return manage_productivity(request)
        elif menus.slug in [ "reports", "farmer-report"] :
            return reports_home(request)

    except Exception as e:
        #return HttpResponse(e.message)
        
        pass
    return HttpResponseRedirect('/')
