# demonstrate template string functions
# In this example, we create a template string for sending out SMS notifications
# On successful enrolment of home internet packages
# Import Template class from string package
from string import Template

def main():
    # Usual string formatting with format()
    str1 = "You're practicing the use of {0} {1}".format("template", "strings")
    print(str1)    

    # TODO: Individual Practice on Dictiornary substitution
    # Create a template for sending out data subscription messages to customers
    email_template = Template("Congratulations. You have been subscribed to ${package} package of ${value} per month for Khs ${amount} per month")
    
    # Create internet packages nested dictionary
    internet_packs = {
        "package_bronze" : {
            "package" : "bronze",
            "value" : "8MB/S",
            "amount" : "2999.00"
        },
        "package_silver" : {
            "package" : "silver",
            "value" : "20MB/S",
            "amount" : "3999.00"
        },
        "package_gold" : {
            "package" : "gold",
            "value" : "40MB/S",
            "amount" : "4999.00"
        }
    }
    #substitute template values based on internet package 
    bronze_text = email_template.substitute(internet_packs["package_bronze"])
    silver_text = email_template.substitute(internet_packs["package_silver"])
    gold_text = email_template.substitute(internet_packs["package_gold"])

    # Print to see output
    print(bronze_text)
    print(silver_text)
    print(gold_text)
if __name__ == "__main__":
    main()
    