from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView, CreateView

from products.forms import CommentForm
from products.models import Product, Comment


# Create your views here.

def hello (request):
    messages.info(request , 'this nooo')
    return render(request , 'products/hello.html')



class ProductListView(ListView):
    # model = Product
    queryset = Product.objects.filter(active=True)
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    paginate_by = 6



class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()

        return context


class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product_id = int(self.kwargs['product_id'])
        product = get_object_or_404(Product , id=product_id)
        obj.product = product
        messages.success(self.request, _('Your comment has been added.'))
        return super().form_valid(form)
