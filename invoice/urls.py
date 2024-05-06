from django.urls import path
from . import views

urlpatterns = [
path('login',views.login, name='login'),
path('logout',views.logout, name='logout'),
path('dashboard',views.dashboard, name='dashboard'),
path('invoices',views.invoices, name='invoices'),
path('quotes',views.quotes, name='quotes'),
path('products',views.products, name='products'),
path('clients',views.clients, name='clients'),

#Create URL Paths
path('invoices/create',views.createInvoice, name='create-invoice'),
#Create URL Paths
path('quotes/create',views.createQuote, name='create-quote'),
path('invoices/create-build/<slug:slug>',views.createBuildInvoice, name='create-build-invoice'),
path('quotes/create-build/<slug:slug>',views.createBuildQuote, name='create-build-quote'),

#Delete an invoice
path('invoices/delete/<slug:slug>',views.deleteInvoice, name='delete-invoice'),
#Delete a Quote
path('quotes/delete/<slug:slug>',views.deleteQuote, name='delete-quote'),

#PDF and EMAIL Paths
path('invoices/view-pdf/<slug:slug>',views.viewPDFInvoice, name='view-pdf-invoice'),
path('invoices/view-document/<slug:slug>',views.viewDocumentInvoice, name='view-document-invoice'),
path('invoices/email-document/<slug:slug>',views.emailDocumentInvoice, name='email-document-invoice'),

#PDF and EMAIL Paths
path('quotes/view-pdf/<slug:slug>',views.viewPDFQuote, name='view-pdf-quote'),
path('quotes/view-document/<slug:slug>',views.viewDocumentQuote, name='view-document-quote'),
path('quotes/email-document/<slug:slug>',views.emailDocumentQuote, name='email-document-quote'),

#Company Settings Page
path('company/settings',views.companySettings, name='company-settings'),
]
