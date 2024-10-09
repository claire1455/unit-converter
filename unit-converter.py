def get_user_input():
    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the unit to convert from (e.g., km, mi, kg, lb): ").lower()
    to_unit = input("Enter the unit to convert to (e.g., mi, km, lb, kg): ").lower()
    return value, from_unit, to_unit

def determine_conversion_type(from_unit, to_unit):
    metric_units = ['km', 'm', 'cm', 'mm', 'kg', 'g', 'l', 'ml']
    imperial_units = ['mi', 'yd', 'ft', 'in', 'lb', 'oz', 'gal', 'qt', 'pt', 'cup']
    
    if from_unit in metric_units and to_unit in imperial_units:
        return "metric_to_imperial"
    elif from_unit in imperial_units and to_unit in metric_units:
        return "imperial_to_metric"
    else:
        return "invalid"

def convert_metric_to_imperial(value, from_unit, to_unit):
    conversions = {
        ('km', 'mi'): 0.621371,
        ('m', 'ft'): 3.28084,
        ('cm', 'in'): 0.393701,
        ('mm', 'in'): 0.0393701,
        ('kg', 'lb'): 2.20462,
        ('g', 'oz'): 0.035274,
        ('l', 'gal'): 0.264172,
        ('ml', 'fl oz'): 0.033814
    }
    
    if (from_unit, to_unit) in conversions:
        return value * conversions[(from_unit, to_unit)]
    else:
        return None

def convert_imperial_to_metric(value, from_unit, to_unit):
    conversions = {
        ('mi', 'km'): 1.60934,
        ('yd', 'm'): 0.9144,
        ('ft', 'm'): 0.3048,
        ('in', 'cm'): 2.54,
        ('lb', 'kg'): 0.453592,
        ('oz', 'g'): 28.3495,
        ('gal', 'l'): 3.78541,
        ('qt', 'l'): 0.946353,
        ('pt', 'ml'): 473.176,
        ('cup', 'ml'): 236.588
    }
    
    if (from_unit, to_unit) in conversions:
        return value * conversions[(from_unit, to_unit)]
    else:
        return None

def main():
    print("Welcome to the Unit Converter!")
    
    while True:
        value, from_unit, to_unit = get_user_input()
        conversion_type = determine_conversion_type(from_unit, to_unit)
        
        if conversion_type == "metric_to_imperial":
            result = convert_metric_to_imperial(value, from_unit, to_unit)
        elif conversion_type == "imperial_to_metric":
            result = convert_imperial_to_metric(value, from_unit, to_unit)
        else:
            result = None
        
        if result is not None:
            print(f"{value} {from_unit} is equal to {result:.4f} {to_unit}")
        else:
            print("Invalid conversion. Please check your units and try again.")
        
        if input("Do you want to perform another conversion? (y/n): ").lower() != 'y':
            break
    
    print("Thank you for using the Unit Converter!")

if __name__ == "__main__":
    main()
