import colorama
from colorama import Fore, Style
from colors import colors
import hobbys
from hobbys import hobbys
import Fixing
import binascii
import webbrowser
from socialmedia import socialmedia

colorama.init()

print( """ 
██╗     ██╗███████╗████████╗    ██╗███╗   ██╗███████╗ ██████╗     ███╗   ███╗ █████╗ ██╗  ██╗███████╗███████╗██████╗ 
██║     ██║██╔════╝╚══██╔══╝    ██║████╗  ██║██╔════╝██╔═══██╗    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔════╝██╔══██╗
██║     ██║███████╗   ██║       ██║██╔██╗ ██║█████╗  ██║   ██║    ██╔████╔██║███████║█████╔╝ █████╗  █████╗  ██████╔╝
██║     ██║╚════██║   ██║       ██║██║╚██╗██║██╔══╝  ██║   ██║    ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══╝  ██╔══██╗
███████╗██║███████║   ██║       ██║██║ ╚████║██║     ╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗███████╗██║  ██║
╚══════╝╚═╝╚══════╝   ╚═╝       ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
""")

print(Fore.GREEN + Style.BRIGHT + "For Educational Purposes Only!!!")
print(Fore.GREEN + "This Code Made For Practicing And Doesn't publish! :)")
print(Fore.WHITE + "--------------------------------")

#collecting info from the user
FirstName = input(Fore.GREEN + Style.BRIGHT + "Enter Your First Name: ")  # FirstName of the user
LastName = input(Fore.GREEN + Style.BRIGHT + "Enter Your Last Name: ")    # LastName of the user
print(Fore.WHITE + Style.BRIGHT + "The User Is: " + Fore.GREEN + Style.BRIGHT + f"{FirstName} {LastName}!" + Style.RESET_ALL)
print(Fore.WHITE + "--------------------------------")

# Region of the user
region = input(Fore.GREEN + Style.BRIGHT + "Enter Region: ")
print(Fore.WHITE + "--------------------------------")

# IP of the user
ip_of_the_user = input(Fore.GREEN + Style.BRIGHT + "Enter IP Address: ")
# Open web page with IP information

webbrowser.open(f"https://ipinfo.io/{ip_of_the_user}")
print("IP information opened in your browser!")
print(Fore.WHITE + "--------------------------------")

# Phone number of the user
phone_number = input(Fore.GREEN + Style.BRIGHT + "Enter User Phone Number: ")
print(Fore.WHITE + "--------------------------------")

# Dad name of the user
dad_name = input(Fore.GREEN + Style.BRIGHT + "Enter Dad Name: ")
print(Fore.WHITE + "--------------------------------")

dad_phone = input(Fore.GREEN + Style.BRIGHT + "Enter Dad Phone Number: ")
print(Fore.WHITE + "--------------------------------")

# Mom name of the user
mom_name = input(Fore.GREEN + Style.BRIGHT + "Enter Mom Name: ")
print(Fore.WHITE + "--------------------------------")

# Mom phone
mom_phone = input(Fore.GREEN + Style.BRIGHT + "Enter Mom Phone Number: ")
print(Fore.WHITE + "--------------------------------")

# Dad age
dad_age = input(Fore.GREEN + "Enter Dad Age: ")
print(Fore.WHITE + "--------------------------------")

# Mom age
mom_age = input(Fore.GREEN + "Enter Mom Age: ")
print(Fore.WHITE + "--------------------------------")

# Gmail of the user
gmail = input(Fore.GREEN + Style.BRIGHT + "Enter Gmail Address (If There No Gmail Just Press Enter!) ")
print(Fore.WHITE + "--------------------------------")

# The user hobby
hobby = input(Fore.GREEN + Style.BRIGHT + "Enter Hobby: ")  # User enters their hobby
print(Fore.WHITE + "--------------------------------")

# If the user doesn't enter a valid hobby
while hobby.lower() not in [h.lower() for h in hobbys]:
    print(Fore.RED + "Please choose a valid hobby" + Style.RESET_ALL)
    hobby = input("Enter Hobby: ").lower().strip()

# Prompt user for their favorite color
favorite_color = input(Fore.GREEN + Style.BRIGHT + "Enter Favorite Color: ").strip().lower()

# Validate if the favorite color is in the list
while favorite_color not in [color.lower() for color in colors]:
    print(Fore.RED + "Please choose a valid color!")  # Ask for a valid color
    favorite_color = input(Fore.GREEN + "Enter Favorite Color: ").strip().lower()
print(Fore.WHITE + "--------------------------------")

#social media user
social = input("What Social Platform The User Using?").strip().lower()

# Validate if the entered social platform exists in the list
while social not in [platform.lower() for platform in socialmedia]:
    print(Fore.RED + "This social media doesn't exist.")
    social = input(Fore.GREEN + Style.BRIGHT + "Enter Social Platform The User Using?").strip().lower()


print(Fore.WHITE + "--------------------------------")
user_social = input("Enter User Account On Social Media: ")
user_password = input("Enter Password: ")
print(Fore.WHITE + "--------------------------------")

#social media dad
social1 = input("What Social Platform The Dad Using?")
while social1 not in [platform.lower() for platform in socialmedia]:
    print(Fore.RED + "This social media doesn't exist.")
    social1 = input(Fore.GREEN + Style.BRIGHT + "Enter Social Platform The User Using?").strip().lower()


print(Fore.WHITE + "--------------------------------")
user_social1 = input("Enter Dad Account On Social Media: ")
user_password1 = input("Enter dad Password: ")
print(Fore.WHITE + "--------------------------------")


#social media mom
social2 = input("What Social Platform The Mom Using?")
while social2 not in [platform.lower() for platform in socialmedia]:
    print(Fore.RED + "This social media doesn't exist.")
    social2 = input(Fore.GREEN + Style.BRIGHT + "Enter Social Platform The User Using?").strip().lower()
print(Fore.WHITE + "--------------------------------")
user_social2 = input("Enter Mom Account On Social Media: ")
user_password2 = input("Enter Mom Password: ")
print(Fore.WHITE + "--------------------------------")


# Ask if the user wants to show their stats
show_stats = input(Fore.RED + "Do You Want To Show Your Stats? If u Press -n- Stats Will Not Be Displayed. (y/n): ").lower().strip()
if show_stats == "y":
    print(Fore.GREEN + "--------------------------------")


    # Display user stats
    print(Fore.GREEN + Style.BRIGHT +
          f"1. Name: {FirstName}\n"
          f"2. Last Name: {LastName}\n"
          f"3. Region: {region}\n"
          f"4. Phone Number: {phone_number}\n"
          f"5. Dad Name: {dad_name}\n"
          f"6. Dad Phone: {dad_phone}\n"
          f"7. Mom Name: {mom_name}\n"
          f"8. Mom Phone: {mom_phone}\n"
          f"9. Dad Age: {dad_age}\n"
          f"10. Mom Age: {mom_age}\n"
          f"11. Gmail: {gmail}\n"
          f"12. Hobby: {hobby}\n"
          f"13. Favorite Color: {favorite_color}")
    print(Fore.GREEN + "--------------------------------")

    #social media list
    print(Fore.GREEN + Style.BRIGHT +
          f"1. user social: {social}\n"
          f"2. user social: {user_social}\n"
          f"3. user password: {user_password}\n")
    print(Fore.GREEN + "--------------------------------")

    #social media dad

    print(Fore.GREEN + Style.BRIGHT +
          f"1. dad social: {social1}\n"
          f"2. dad social: {user_social1}\n"
          f"3. dad password: {user_password1}\n")
    print(Fore.GREEN + "--------------------------------")

    #social media mom
    print(Fore.GREEN + Style.BRIGHT +
          f"1. mom social: {social2}\n"
          f"2. mom social: {user_social2}\n"
          f"3. mom password: {user_password2}\n")

#if the user press *n*
else:
    # Add this line at the very end of your code
    input(Fore.WHITE + "\nPress Enter to exit...")
