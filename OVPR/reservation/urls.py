from django.contrib import admin
from django.urls import path,include
from reservation import views
from reservation.views import *
from OVPR import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('searchresult/',views.searchresult,name='searchresult'),
    path('Login/',views.butt,name='Login'),
    path('contact/',views.but,name='send'),
    path('signedUp',views.signedUp,name='signedUp'),
    path('profile',Prof.log,name='log'),
    path('prof',Prof.prof,name='prof'),
    path('login',views.butt,name='Login'),
    path('signup/',views.sign,name='signup'),
    path('bookinfconfirmation',views.bcof,name='BOOK'),
    path('startbooking/',Prof.vechileregistration,name='startbooking'),
    path('confirmation',Prof.confirm,name='confirmation'),
    path('Payment',Prof.payment,name='Payment'),
    path('SucessPayment',Prof.sucesspayment,name='SucessPayment'),
    path('result',Prof.result,name='result'),
    path('selected',views.selected,name='selected'),
    path('Cancel/',Prof.canc,name='Cancel'),
    path('cancel/',Prof.cancel,name='cancel'),
    path('ShowBooking/',Prof.showBooking,name='ShowBooking'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
