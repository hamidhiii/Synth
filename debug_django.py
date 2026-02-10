import os
import sys
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
try:
    django.setup()
    from django.conf import settings
    from django.urls import get_resolver
    
    print(f"INSTALLED_APPS: {settings.INSTALLED_APPS}")
    
    resolver = get_resolver()
    print("\nURL Patterns:")
    for pattern in resolver.url_patterns:
        print(pattern)
        
    # Check if we can import neurynth_sale
    try:
        import neurynth_sale
        print("\nSuccessfully imported neurynth_sale")
        import neurynth_sale.urls
        print("Successfully imported neurynth_sale.urls")
    except Exception as e:
        print(f"\nFailed to import neurynth_sale: {e}")

except Exception as e:
    print(f"Error setting up Django: {e}")
