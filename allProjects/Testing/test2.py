alien_0 = {'color': 'green'}
alien_color = alien_0.get('color')
alien_points = alien_0.get('points', 0)
alien_speed = alien_0.get('speed')
print(alien_color)
print(alien_points)
print(alien_speed)

if not alien_speed: 
    print('its empty none')

# Define a list of users, where each user# is represented by a dictionary.
users = [ { 'last': 'fermi', 'first': 'enrico', 'username': 'efermi', }, { 'last': 'curie', 'first': 'marie', 'username': 'mcurie', },]
# Show all information about each 
#sers.print("User summary:")

for user_dict in users: 
    for k, v in user_dict.items(): 
        print(f"{k}: {v}") 
    print("\n")

squares = {x:x**2 for x in range(5)}
print(squares)

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)

# Output:
# [1, 2, 3, 4, 5]

