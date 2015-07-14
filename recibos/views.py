from django.shortcuts import render
from django.views.generic import View
from recibos.models import Withdrawal


class WithdrawalView(View):
    template_name = "withdrawal.html"

    def get(self, request, withdrawal_id):
        withdrawal = Withdrawal.objects.get(id=withdrawal_id)
        partner = withdrawal.partner
        cooperative = withdrawal.partner.cooperative
        return render(request, self.template_name,
                      {'withdrawal': withdrawal, 'partner': partner,
                       'cooperative': cooperative})
