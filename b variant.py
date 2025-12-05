

def fix_inventory_codes(codes):
    standardized=[]
    for code in raw_codes:
       fixed_code= code.replace('-', '').replace(' ','')
       upper_code=fixed_code.upper()
       if len(upper_code)<3:
         continue
       standardized.append(upper_code)
    return standardized
    
raw_codes = [
    "abc-123",
    "  X-99 ",
    "prod 456",
    "a-1",       # Too short after cleaning (becomes "A1")
    "super-item"
]
fixed_codes = fix_inventory_codes(raw_codes)
print(fixed_codes)