import json

# This script simulates a basic AI license compliance check.
# In a real-world scenario, 'Proveniq' would analyze code and dependencies.
# Here, we're demonstrating the *concept* of checking license terms against usage.

def check_license_compliance(model_info, usage_description):
    """Checks if the model's license terms are met by the usage.

    Args:
        model_info (dict): Information about the AI model, including its license.
        usage_description (str): A description of how the model is being used.

    Returns:
        bool: True if compliant, False otherwise.
        str: A message explaining the compliance status.
    """
    license_type = model_info.get('license', 'Unknown')
    is_commercial_use = 'commercial' in usage_description.lower()
    requires_attribution = model_info.get('requires_attribution', True)
    attribution_provided = 'attribution' in usage_description.lower()

    # --- Core Logic: Demonstrating license term checks ---
    if license_type == 'MIT' or license_type == 'Apache-2.0':
        # These licenses are generally permissive for commercial use
        if is_commercial_use and not requires_attribution:
            return True, f"'{license_type}' license allows commercial use without mandatory attribution."
        elif is_commercial_use and requires_attribution and attribution_provided:
            return True, f"'{license_type}' license allows commercial use with provided attribution."
        elif is_commercial_use and requires_attribution and not attribution_provided:
            return False, f"'{license_type}' license requires attribution for commercial use, but none was provided."
        else:
            return True, f"'{license_type}' license allows this usage."

    elif license_type == 'GPL-3.0':
        # GPL-3.0 is a strong copyleft license, typically for non-commercial or open-source distribution
        if is_commercial_use:
            return False, f"'{license_type}' is a copyleft license that may restrict commercial use without sharing source code."
        else:
            return True, f"'{license_type}' license is generally compatible with non-commercial use."

    else: # Default for unknown or restrictive licenses
        return False, f"License '{license_type}' has unclear or restrictive terms for this usage."
    # --- End of Core Logic ---

# --- Example Data ---
# In a real tool, this would be dynamically discovered.
models = [
    {
        'name': 'AwesomeAIModel',
        'version': '1.0',
        'license': 'MIT',
        'requires_attribution': True
    },
    {
        'name': 'SecureML',
        'version': '2.1',
        'license': 'Apache-2.0',
        'requires_attribution': False
    },
    {
        'name': 'OpenSourceAI',
        'version': '0.5',
        'license': 'GPL-3.0',
        'requires_attribution': True
    }
]

# --- Simulation of Usage Scenarios ---
usage_scenarios = [
    {'description': 'Using the model for internal research, with attribution.', 'is_commercial': False},
    {'description': 'Deploying the model in a commercial product, with attribution.', 'is_commercial': True},
    {'description': 'Deploying the model in a commercial product, without attribution.', 'is_commercial': True},
    {'description': 'Using the model for a non-profit project.', 'is_commercial': False}
]

# --- Running the Checks ---
print("--- AI License Compliance Simulation ---")

for model in models:
    print(f"\nModel: {model['name']} (License: {model['license']})")
    for scenario in usage_scenarios:
        # Construct a usage description string for the function
        full_usage_desc = scenario['description']
        if scenario['is_commercial']:
            full_usage_desc += ' (commercial use)'
        else:
            full_usage_desc += ' (non-commercial use)'

        is_compliant, message = check_license_compliance(model, full_usage_desc)
        status = "✅ COMPLIANT" if is_compliant else "❌ NON-COMPLIANT"
        print(f"  - Usage: {scenario['description']}\n    Status: {status}\n    Reason: {message}")

print("\n--- End of Simulation ---")
print("Note: This is a simplified demonstration. Real-world tools analyze code, dependencies, and specific license clauses.")
