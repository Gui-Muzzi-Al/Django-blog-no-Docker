from site_setup.models import SiteSetup

def context_processor_example(request):
    """
    Example context processor that adds a variable to the context.
    """
    return {
        'exemple': 'This is an example context processor',
    }

def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()
    return {'site_setup': setup,}