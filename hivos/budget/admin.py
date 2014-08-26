from django.contrib import admin
from budget.models import Budget, Activity_Status, Budget_Activity, Budget_Strategy

admin.site.register(Budget)
admin.site.register(Activity_Status)
admin.site.register(Budget_Activity)
admin.site.register(Budget_Strategy)