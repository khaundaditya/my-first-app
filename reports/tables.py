from reports.models import ManpowerReport
import django_tables2 as tables

class SimpleTable(tables.Table):
    class Meta:
        model =  ManpowerReport