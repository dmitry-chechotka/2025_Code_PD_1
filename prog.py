all_users = []


# 1. Apvienot datnes ‘admin.txt’ un ‘viesis.txt’ , datnēs jābūt vismaz vienam vārdam, vienam uzvārdam, lomai, vecumam.


# .txt text -> [] list, funkcija ar parametru
def list_create(filename):
    result = []
    with open(filename) as file:
        for line in file:
            result.append(line.split())
    return result


# Create lists, apvienot datnes into separate variables
admin_list = list_create("admin.txt")
viesis_list = list_create("viesis.txt")

all_users = admin_list + viesis_list


# Ievadīt visus datus un izdrukāt.

print("1. Ievadīt visus datus un izdrukāt. \n")


def print_list(chosenList):  # Saraksta variable drukāšana string veidā
    for user in chosenList:
        for element in user:
            print(element, end=" ")
        print()


print_list(all_users)

# 2. Aprēķināt:

print(
    "\n\n2. Aprēķināt vidējo administratora vecumu,  atrast visvecāko un visjaunāko administratoru.\n"
)


# Vidējo administratora vecumu
def average_age(chosenList):  # Atrada vidējo vecumu dotajā sarakstā
    total_age = 0
    for user in chosenList:
        total_age += int(user[3])
    average_age = total_age / len(chosenList)
    return average_age


print("Vidējais administratora vecums:")
print(average_age(admin_list), "gadi")


# Atrast visvecāko administratoru.
def youngest_user(chosenList):  # Atrada jaunāko useru dotajā sarakstā
    youngest_user = min(chosenList, key=lambda x: x[3])
    return youngest_user


youngest_admin = youngest_user(admin_list)

print("Visjaunākais administrators:")
print(
    youngest_admin[0]
    + " "
    + youngest_admin[1]
    + ", "
    + youngest_admin[2]
    + ", "
    + youngest_admin[3]
    + " gadi"
)


# Atrast visvecāko administratoru.
def oldest_user(chosenList):  # Atrada vecāko useru dotajā sarakstā
    oldest_user = max(chosenList, key=lambda x: x[3])
    return oldest_user


oldest_admin = oldest_user(admin_list)

print("Visvecākais administrators:")
print(
    oldest_admin[0]
    + " "
    + oldest_admin[1]
    + ", "
    + oldest_admin[2]
    + ", "
    + oldest_admin[3]
    + " gadi"
)

# 3. Izdrukāt cik apvienotajā datnē administratoru, cik viesu.

print("\n\n3. Izdrukāt cik apvienotajā datnē administratoru, cik viesu.\n")


def count_user_types(chosenList):
    admin_count = 0
    viesis_count = 0

    for user in chosenList:
        if user[2] == "administrators":
            admin_count += 1
        elif user[2] == "viesis":
            viesis_count += 1
        else:
            print("Invalid list value met on:")
            print(user)
            print("In provided list:")
            print(chosenList)
            print("Loop exited. No value has been returned.")
            break
    return (admin_count, viesis_count)


admin_count, viesis_count = count_user_types(all_users)

print(f"Apvienotajā datnē ir {admin_count} administratoru un {viesis_count} viesu.")
