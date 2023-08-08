import csv
import os

errored_filenames = []

def extract_filename_data(filename):
    try:
        date_signed, company, full_name, _ = tuple(filename.split('_', maxsplit=3))
        try:
            first_name, last_name = tuple(full_name.split(' '))
        except ValueError as e:
            first_name, last_name = tuple(full_name.split(' '))

        date_signed = date_signed[0:2] + "/" + date_signed[2:4] + "/" + date_signed[4:6]

        return first_name, last_name, date_signed, company
    except ValueError as e:
        print(f"Error: {e}")
        errored_filenames.append(filename)
        return None, None, None, None


# print(extract_filename_data('221107_A&H_Andres Aguirre_Appearance.pdf'))

# Create CSV and header
with open('test.csv', 'w') as csvfile:
    fieldnames = ['First Name', 'Last Name', 'Date Signed', 'Company']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# Traves directory and append to CSV
for _, _, filenames in os.walk('.'):
    for filename in filenames:
        print(f"Processing {filename}...", end="")
        if filename.endswith('Appearance.pdf'):
            first_name, last_name, date_signed, company = extract_filename_data(filename)
            if first_name:
                with open('test.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow({'First Name': first_name, 'Last Name': last_name, 'Date Signed': '20' + date_signed, 'Company': company})
                    print("Done!")
        else:
            print("Name doesn't end in 'Appearance.pdf'. Skipped!")


print(f'\n[!!!] {len(errored_filenames)} errors:')
for filename in errored_filenames:
    print(filename)