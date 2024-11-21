from django.contrib import admin
from django.utils.html import format_html
from .models import Product , Purchase , PaymentQr

class PaymentAdmin(admin.ModelAdmin):
  list_display = ('user', 'product' ,'payment_screenshot', 'mobile_number' ,'email' , 'purchased_at'  )

  @admin.display(description='Image')
  def image_tag(self, obj):
      if obj.image:
          return format_html('<img src="{}" style="height: 100px;"/>', obj.image.url)
      return 'No Image'

admin.site.register(Product)
admin.site.register(Purchase , PaymentAdmin)
admin.site.register(PaymentQr)
