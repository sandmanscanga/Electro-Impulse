from django.shortcuts import render


""" Home """
def home(request):
    return render(request, "app/index.html")


""" Products """
def products(request):
    return render(request, "app/products/index.html")


""" Products / Other Systems """
def other_systems(request):
    return render(request, "app/products/other-systems.html")


""" Products / Hydraulic & Filtering """
def hydraulic_filter(request):
    return render(request, "app/products/hydraulic-filter.html")


""" Products / Cooling Equipment """
def cooling_equipment(request):
    return render(request, "app/products/cooling-equipment/index.html")


""" Products / Cooling Equipment / Refrigerated """
def refrigerated(request):
    return render(request, "app/products/cooling-equipment/refrigerated/index.html")


""" Products / Cooling Equipment / Refrigerated / RU Series """
def ru_series(request):
    return render(request, "app/products/cooling-equipment/refrigerated/ru-series.html")


""" Products / Cooling Equipment / Refrigerated / RUW Series """
def ruw_series(request):
    return render(request, "app/products/cooling-equipment/refrigerated/ruw-series.html")


""" Products / Cooling Equipment / Refrigerated / Split Systems """
def split_systems(request):
    return render(request, "app/products/cooling-equipment/refrigerated/split-systems.html")


""" Products / Cooling Equipment / Refrigerated / RC Refrigerated Series """
def rc_refrig_series(request):
    return render(request, "app/products/cooling-equipment/refrigerated/rc-refrig-series.html")


""" Products / Cooling Equipment / Non-Refrigerated """
def non_refrigerated(request):
    return render(request, "app/products/cooling-equipment/non-refrigerated/index.html")


""" Products / Cooling Equipment / Refrigerated / CU Series """
def cu_series(request):
    return render(request, "app/products/cooling-equipment/non-refrigerated/cu-series.html")


""" Products / Cooling Equipment / Refrigerated / CUW Series """
def cuw_series(request):
    return render(request, "app/products/cooling-equipment/non-refrigerated/cuw-series.html")


""" Products / Cooling Equipment / Refrigerated / RC Non-Refrigerated Series """
def rc_non_refrig_series(request):
    return render(request, "app/products/cooling-equipment/non-refrigerated/rc-non-refrig-series.html")


""" Products / Cooling Equipment / Coolants Supported """
def coolants_supported(request):
    return render(request, "app/products/cooling-equipment/coolants-supported.html")


""" Technology """
def technology(request):
    return render(request, "app/technology/index.html")


""" Technology / Formulas """
def formulas(request):
    return render(request, "app/technology/formulas.html")


""" Technology / Cooling Systems """
def coolsys_index(request):
    return render(request, "app/technology/cooling-systems/index.html")


""" Technology / Cooling Systems / Introduction """
def coolsys_intro(request):
    return render(request, "app/technology/cooling-systems/introduction.html")


""" Technology / Cooling Systems / Coolant Selection Chart """
def coolant_select(request):
    return render(request, "app/technology/cooling-systems/coolant-select.html")


""" Technology / Cooling Systems / Cooling Methods """
def cooling_methods(request):
    return render(request, "app/technology/cooling-systems/cooling-methods.html")


""" Technology / Cooling Systems / Pumps & Reservoirs """
def pumps_reservoirs(request):
    return render(request, "app/technology/cooling-systems/pumps-reservoirs.html")


""" Technology / Cooling Systems / Closed Loop Systems """
def closed_loop_sys(request):
    return render(request, "app/technology/cooling-systems/closed-loop-sys.html")


""" Industries """
def industries(request):
    return render(request, "app/industries/index.html")


""" Sales """
def sales(request):
    return render(request, "app/sales/index.html")


""" Sales / Price List """
def price_list(request):
    return render(request, "app/sales/price-list.html")


""" Sales / Manual """
def sales_manual(request):
    return render(request, "app/sales/manual.html")


""" Sales / Warranty """
def sales_warranty(request):
    return render(request, "app/sales/warranty.html")


""" Sales / Cooling System Info """
def cooling_sys_info(request):
    return render(request, "app/sales/cooling-sys-info.html")


""" Company """
def company(request):
    return render(request, "app/company/index.html")


""" Company / Facilities """
def company_facilities(request):
    return render(request, "app/company/facilities.html")


""" Company / Directions """
def company_directions(request):
    return render(request, "app/company/directions.html")
