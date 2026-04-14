from django.shortcuts import render

PAGE_TEMPLATES = {
    'index': 'pages/index.html',
    'solution': 'pages/solution.html',
    'product': 'pages/product.html',
    'scenarios': 'pages/scenarios.html',
    'cases': 'pages/cases.html',
    'case-vnutripromyshlennaya-logistika': 'pages/cases/case-vnutripromyshlennaya-logistika.html',
    'case-odna-edinica-tehniki': 'pages/cases/case-odna-edinica-tehniki.html',
    'case-pogruzchik-priemka': 'pages/cases/case-pogruzchik-priemka.html',
    'case-park-tehniki': 'pages/cases/case-park-tehniki.html',
    'blog': 'pages/blog.html',
    'blog-wms-rms-pyramid': 'pages/blog-wms-rms-pyramid.html',
    'demo': 'pages/demo.html',
    'faq': 'pages/faq.html',
    'partners': 'pages/partners.html',
    'materials': 'pages/materials.html',
    'about': 'pages/about.html',
    'contacts': 'pages/contacts.html',
    'privacy': 'pages/privacy.html',
    'consent': 'pages/consent.html',
}


def page_view(request, page_name):
    template = PAGE_TEMPLATES.get(page_name)
    if not template:
        from django.http import Http404
        raise Http404
    return render(request, template)


def index(request):
    return render(request, 'pages/index.html')
