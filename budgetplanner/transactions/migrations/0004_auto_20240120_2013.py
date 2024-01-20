from django.db import migrations


def add_category_data(apps, schema_editor):
    ExpenseCategory = apps.get_model('transactions', 'ExpenseCategory')
    category_list = [
        "Rent",
        "Car Insurance",
        "Groceries",
        "Utilities",
        "Health Insurance",
        "Internet Bill",
        "Dining Out",
        "Electricity Bill",
        "Gas Bill",
        "Water Bill",
        "Phone Bill",
        "Transportation",
        "Clothing",
        "Entertainment",
        "Gym Membership",
        "Childcare",
        "Education",
        "Healthcare",
        "Home Repairs",
        "Travel",
        "Gifts",
        "Pet Expenses",
        "Charity Donations",
        "Hobbies",
        "Taxes",
        "Insurance Premiums",
        "Subscription Services",
        "Home Maintenance"
    ]

    for category_name in category_list:
        ExpenseCategory.objects.create(name=category_name)


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0003_auto_20240120_2011'),
    ]

    operations = [
        migrations.RunPython(add_category_data),
    ]
