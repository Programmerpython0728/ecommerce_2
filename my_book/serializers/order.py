from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from my_book.models import Order,Product

class OrderSerializers(serializers.ModelSerializer):
    total_price=serializers.SerializerMethodField()
    class Meta:
        model=Order
        fields=["id",'product','customer','quantity','created_at','total_price','phone_number','is_paid']

        def get_total_price(self,obj):
            return obj.product.price * obj.quantity


        def validate_quantity(self,value):
            try:
                product_id=self.initial_data['product']
                product=Product.objects.get(id=product_id)

                if value>product.stock:
                    raise serializers.ValidationError("Not enough items in stock.")

                if value<1:
                    raise serializers.ValidationError("zakaslar soni 1dan kchik bo'lishi mumkin emas")

                return value
            except ObjectDoesNotExist:
                raise serializers.ValidationError("Product does not exist")
        def create(self,validate_data):
            order=Order.objects.create(**validate_data)
            product=order.product
            product.stock-=order.quantity
            product.save()
            self.send_confirmation_email("order")
            return order

        def send_confirmation_email(self, order):
            print(f"Sent confirmation email for Order {order.id}")







