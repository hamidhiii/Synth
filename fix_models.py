import os
import re

def convert_field(field_line):
    """
    Converts an Odoo field definition to a Django field definition.
    """
    field_line = field_line.strip()
    # Basic regex to capture name, type and arguments
    match = re.search(r'(\w+)\s*=\s*fields\.(\w+)\((.*)\)', field_line)
    if not match:
        return None
    
    name, odoo_type, args = match.groups()
    django_type = "models.TextField(blank=True, null=True)"
    
    # Mapping Odoo types to Django types
    mapping = {
        "Char": "models.CharField(max_length=255, blank=True, null=True)",
        "Integer": "models.IntegerField(default=0)",
        "Boolean": "models.BooleanField(default=False)",
        "Float": "models.FloatField(default=0.0)",
        "Monetary": "models.DecimalField(max_digits=20, decimal_places=2, default=0.0)",
        "Datetime": "models.DateTimeField(blank=True, null=True)",
        "Date": "models.DateField(blank=True, null=True)",
        "Text": "models.TextField(blank=True, null=True)",
        "Html": "models.TextField(blank=True, null=True)", # Simplification
        "Binary": "models.BinaryField(blank=True, null=True)",
        "Selection": "models.CharField(max_length=50, blank=True, null=True)", # Simplification
    }
    
    if odoo_type in mapping:
        django_type = mapping[odoo_type]
    elif odoo_type == "Many2one":
        rel_match = re.search(r"['\"](.+?)['\"]", args)
        if rel_match:
            rel_model = rel_match.group(1)
            # Convert to TextField to avoid "Model not found" errors during initial setup
            django_type = f"models.TextField(blank=True, null=True, help_text='Odoo Many2one: {rel_model}')"
    elif odoo_type == "One2many" or odoo_type == "Many2many":
        # Simplified as TextField for metadata or future reference
        django_type = "models.TextField(blank=True, null=True, help_text='Odoo relationship field')"
            
    return f"    {name} = {django_type}"

def migrate_module(module_name, source_models_dir, target_app_path):
    """
    Scans an Odoo models directory and generates a Django models.py file.
    """
    if not os.path.exists(source_models_dir):
        return
    
    os.makedirs(target_app_path, exist_ok=True)
    init_file = os.path.join(target_app_path, '__init__.py')
    if not os.path.exists(init_file):
        with open(init_file, 'w') as f: f.write("")

    all_models_content = "from django.db import models\n\n"
    
    for filename in os.listdir(source_models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            with open(os.path.join(source_models_dir, filename), 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract class definitions
            # This regex is simplified and might need refinement for complex inheritance
            class_matches = re.finditer(r'class\s+(\w+)\(models\.Model\):(.*?(?=class|\Z))', content, re.DOTALL)
            for match in class_matches:
                class_name = match.group(1)
                body = match.group(2)
                
                all_models_content += f"class {class_name}(models.Model):\n"
                lines = body.split('\n')
                has_fields = False
                for line in lines:
                    converted = convert_field(line)
                    if converted:
                        all_models_content += converted + "\n"
                        has_fields = True
                
                if not has_fields:
                    all_models_content += "    pass\n"
                all_models_content += "\n"
    
    with open(os.path.join(target_app_path, 'models.py'), 'w', encoding='utf-8') as f:
        f.write(all_models_content)

if __name__ == "__main__":
    # Base paths
    ADDONS_SRC = r'C:\Users\user\Desktop\jj\actpy\addons'
    DOMAINS_ROOT = r'C:\Users\user\Desktop\jj\NEURYNTH_ERP\domains'
    
    # Mapping of Odoo modules to Domains
    domain_map = {
        'crm': 'sales_crm',
        'sale': 'sales_crm',
        'account': 'accounting',
        'hr': 'hr',
        'stock': 'inventory',
        'mrp': 'manufacturing',
        # Add more as needed
    }
    
    for module, domain in domain_map.items():
        src_path = os.path.join(ADDONS_SRC, module, 'models')
        target_path = os.path.join(DOMAINS_ROOT, domain, f'neurynth_{module}')
        if os.path.exists(src_path):
            print(f"Migrating {module} to domain {domain}...")
            migrate_module(module, src_path, target_path)

    print("Migration cleanup completed.")
