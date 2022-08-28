from django import forms

class Shipping(forms.Form):
    first_name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    last_name = forms.CharField(max_length= 128, widget=forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    phone_number = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    city = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    postal_code = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'w-full px-4 py-3 text-sm border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600'}))
    check_save = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':"w-5 h-5 border border-gray-300 rounded focus:outline-none focus:ring-1"}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class':"flex items-center w-full px-4 py-3 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-blue-600", "rows":4, "cols":20}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':"w-full px-4 py-3 text-xs border border-gray-300 rounded lg:text-sm focus:outline-none focus:ring-1 focus:ring-blue-600", "rows":4, "cols":20}))
    

   
