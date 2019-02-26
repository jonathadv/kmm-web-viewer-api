from django.contrib import admin

from app.models import (Kmmaccounts, Kmmbudgetconfig, Kmmcurrencies, Kmmfileinfo, Kmminstitutions, Kmmkeyvaluepairs,
                        Kmmpayees, Kmmprices, Kmmreportconfig, Kmmschedulepaymenthistory, Kmmschedules, Kmmsecurities,
                        Kmmsplits, Kmmtransactions)

admin.site.register((Kmmaccounts, Kmmbudgetconfig, Kmmcurrencies, Kmmfileinfo, Kmminstitutions, Kmmkeyvaluepairs,
                     Kmmpayees, Kmmprices, Kmmreportconfig, Kmmschedulepaymenthistory, Kmmschedules, Kmmsecurities,
                     Kmmsplits, Kmmtransactions,))
