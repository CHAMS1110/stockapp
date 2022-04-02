from django import forms


class TickerForm(forms.Form):
    ticker = forms.CharField(label='Ticker', max_length=5)


class PriceSearchForm(forms.Form):
        date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    