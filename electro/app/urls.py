from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products, name="products"),
    path("products/other-systems/", views.other_systems, name="other-systems"),
    path("products/hydraulic-filter/", views.hydraulic_filter, name="hydraulic-filter"),
    path("products/cooling-equipment/", views.cooling_equipment, name="cooling-equipment"),
    path("products/cooling-equipment/refrigerated/", views.refrigerated, name="refrigerated"),
    path("products/cooling-equipment/refrigerated/ru-series/", views.ru_series, name="ru-series"),
    path("products/cooling-equipment/refrigerated/ruw-series/", views.ruw_series, name="ruw-series"),
    path("products/cooling-equipment/refrigerated/split-systems/", views.split_systems, name="split-systems"),
    path("products/cooling-equipment/refrigerated/rc-refrig-series/", views.rc_refrig_series, name="rc-refrig-series"),
    path("products/cooling-equipment/non-refrigerated/", views.non_refrigerated, name="non-refrigerated"),
    path("products/cooling-equipment/non-refrigerated/cu-series/", views.cu_series, name="cu-series"),
    path("products/cooling-equipment/non-refrigerated/cuw-series/", views.cuw_series, name="cuw-series"),
    path("products/cooling-equipment/non-refrigerated/rc-non-refrig-series/", views.rc_non_refrig_series, name="rc-non-refrig-series"),
    path("products/cooling-equipment/coolants-supported/", views.coolants_supported, name="coolants-supported"),
    path("technology/", views.technology, name="technology"),
    path("technology/formulas/", views.formulas, name="formulas"),
    path("technology/cooling-systems/", views.coolsys_index, name="coolsys_index"),
    path("technology/cooling-systems/introduction/", views.coolsys_intro, name="coolsys-intro"),
    path("technology/cooling-systems/coolant-select/", views.coolant_select, name="coolant-select"),
    path("technology/cooling-systems/cooling-methods/", views.cooling_methods, name="cooling-methods"),
    path("technology/cooling-systems/pumps-reservoirs/", views.pumps_reservoirs, name="pumps-reservoirs"),
    path("technology/cooling-systems/closed-loop-sys/", views.closed_loop_sys, name="closed-loop-sys"),
    path("industries/", views.industries, name="industries"),
    path("sales/", views.sales, name="sales"),
    path("sales/price-list/", views.price_list, name="price-list"),
    path("sales/manual/", views.sales_manual, name="sales-manual"),
    path("sales/warranty/", views.sales_warranty, name="sales-warranty"),
    path("sales/cooling-sys-info/", views.cooling_sys_info, name="cooling-sys-info"),
    path("company/", views.company, name="company"),
    path("company/facilities/", views.company_facilities, name="company-facilities"),
    path("company/directions/", views.company_directions, name="company-directions")
]