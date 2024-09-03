
import json
import re

def extract_whois_info(whois_str):
    # Define regex patterns to extract information
    patterns = {
        'registrar': r'Registrar:\s*(.+)',
        'registrant_name': r'Registrant Name:\s*(.+)',
        'registrant_organization': r'Registrant Organization:\s*(.+)',
        'registrant_street': r'Registrant Street:\s*(.+)',
        'registrant_city': r'Registrant City:\s*(.+)',
        'registrant_state_province': r'Registrant State/Province:\s*(.+)',
        'registrant_postal_code': r'Registrant Postal Code:\s*(.+)',
        'registrant_country': r'Registrant Country:\s*(.+)',
        'registrant_phone': r'Registrant Phone:\s*(.+)',
        'registrant_email': r'Registrant Email:\s*(.+)',
        'admin_name': r'Admin Name:\s*(.+)',
        'admin_organization': r'Admin Organization:\s*(.+)',
        'admin_street': r'Admin Street:\s*(.+)',
        'admin_city': r'Admin City:\s*(.+)',
        'admin_state_province': r'Admin State/Province:\s*(.+)',
        'admin_postal_code': r'Admin Postal Code:\s*(.+)',
        'admin_country': r'Admin Country:\s*(.+)',
        'admin_phone': r'Admin Phone:\s*(.+)',
        'admin_email': r'Admin Email:\s*(.+)',
        'tech_name': r'Tech Name:\s*(.+)',
        'tech_organization': r'Tech Organization:\s*(.+)',
        'tech_street': r'Tech Street:\s*(.+)',
        'tech_city': r'Tech City:\s*(.+)',
        'tech_state_province': r'Tech State/Province:\s*(.+)',
        'tech_postal_code': r'Tech Postal Code:\s*(.+)',
        'tech_country': r'Tech Country:\s*(.+)',
        'tech_phone': r'Tech Phone:\s*(.+)',
        'tech_email': r'Tech Email:\s*(.+)',
    }

    # Extract information using the defined patterns
    extracted_info = {key: re.search(pattern, whois_str) for key, pattern in patterns.items()}

    # Format extracted information into a dictionary
    formatted_info = {
        'registrar': extracted_info['registrar'].group(1) if extracted_info['registrar'] else None,
        'registrant': {
            'name': extracted_info['registrant_name'].group(1) if extracted_info['registrant_name'] else None,
            'organization': extracted_info['registrant_organization'].group(1) if extracted_info['registrant_organization'] else None,
            'street': extracted_info['registrant_street'].group(1) if extracted_info['registrant_street'] else None,
            'city': extracted_info['registrant_city'].group(1) if extracted_info['registrant_city'] else None,
            'state_province': extracted_info['registrant_state_province'].group(1) if extracted_info['registrant_state_province'] else None,
            'postal_code': extracted_info['registrant_postal_code'].group(1) if extracted_info['registrant_postal_code'] else None,
            'country': extracted_info['registrant_country'].group(1) if extracted_info['registrant_country'] else None,
            'phone': extracted_info['registrant_phone'].group(1) if extracted_info['registrant_phone'] else None,
            'email': extracted_info['registrant_email'].group(1) if extracted_info['registrant_email'] else None,
        },
        'admin': {
            'name': extracted_info['admin_name'].group(1) if extracted_info['admin_name'] else None,
            'organization': extracted_info['admin_organization'].group(1) if extracted_info['admin_organization'] else None,
            'street': extracted_info['admin_street'].group(1) if extracted_info['admin_street'] else None,
            'city': extracted_info['admin_city'].group(1) if extracted_info['admin_city'] else None,
            'state_province': extracted_info['admin_state_province'].group(1) if extracted_info['admin_state_province'] else None,
            'postal_code': extracted_info['admin_postal_code'].group(1) if extracted_info['admin_postal_code'] else None,
            'country': extracted_info['admin_country'].group(1) if extracted_info['admin_country'] else None,
            'phone': extracted_info['admin_phone'].group(1) if extracted_info['admin_phone'] else None,
            'email': extracted_info['admin_email'].group(1) if extracted_info['admin_email'] else None,
        },
        'tech': {
            'name': extracted_info['tech_name'].group(1) if extracted_info['tech_name'] else None,
            'organization': extracted_info['tech_organization'].group(1) if extracted_info['tech_organization'] else None,
            'street': extracted_info['tech_street'].group(1) if extracted_info['tech_street'] else None,
            'city': extracted_info['tech_city'].group(1) if extracted_info['tech_city'] else None,
            'state_province': extracted_info['tech_state_province'].group(1) if extracted_info['tech_state_province'] else None,
            'postal_code': extracted_info['tech_postal_code'].group(1) if extracted_info['tech_postal_code'] else None,
            'country': extracted_info['tech_country'].group(1) if extracted_info['tech_country'] else None,
            'phone': extracted_info['tech_phone'].group(1) if extracted_info['tech_phone'] else None,
            'email': extracted_info['tech_email'].group(1) if extracted_info['tech_email'] else None,
        }
    }

    # Convert to JSON
    return json.dumps(formatted_info, indent=4)

# Example WHOIS string
whois_string = """... (WHOIS data here) ..."""

# Extract and print JSON
print(extract_whois_info(whois_string))
