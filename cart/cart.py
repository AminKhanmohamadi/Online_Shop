from products.models import Product

class Cart:
    def __init__(self , request):
        # گرفتن ریکویست کاربر
        self.request = request
        # گرفتن سشن کاربر
        self.session = request.session
        # اگر سبد خرید داشت بگیر
        cart = self.session.get('cart')
        # اگر سبد خرید نداشت بساز براش
        if not cart:
            cart = self.session['cart'] = {}
        # سبد خرید ساخته شد
        self.cart = cart
    # اضافه کردن یک محصول و تعدادش در سبد خرید
    def add(self , product , quantity=1 ):
        # گرفتن ایدی محصول
        product_id = str(product.id)
        # موجود نبود محصول در سبد خرید و اضافه کردن
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity' : quantity}
        # وجود محصول اضافه کردن تعداد جدید
        else:
            self.cart[product_id]['quantity'] += quantity

    def remove(self , product ):
        """
            Remove a product from the cart
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def save(self):
        self.session.modified = True


    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product.obj'] = product

        for item in cart.values():
            yield item

        # yield بصورت تکه تکه خروجی برمیگردونه ینی  در این مثال ابتدا محصول اول دوباره اجرا محصول دوم و تا انتها


    def __len__(self):
        return len(self.cart.keys())


    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        return sum(product.price for product in products)