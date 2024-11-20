from django import forms
from .models import Purchase, Product

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['product', 'payment_screenshot' ,'name', 'mobile_number' , 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Customize the 'product' field (hidden field)
        if 'product' in self.fields:
            self.fields['product'].widget = forms.HiddenInput()

        # Add Tailwind CSS classes to form fields
        self.fields['payment_screenshot'].widget.attrs.update({
            'class': 'block w-full mt-2 p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600',
            'accept': 'image/*',  # Ensure it accepts only image files
        })

        # Optional: Customize labels or other fields here if needed
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'block w-full p-2 mt-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-600'
            })
            self.fields[field].label = self.fields[field].label.capitalize()  # Capitalize label text

