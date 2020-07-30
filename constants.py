from django import forms

HOBBIES = [
    ('none', 'Select'),
    ('gaming', 'Gaming'),
    ('outdoors', 'Outdoors'),
    ('pets', 'Pets'),
    ('fishing', 'Fishing'),
    ('cooking', 'Cooking'),
    ('grilling', 'Grilling'),
    ('beer wine liquor', 'Beer/Wine/Liquer'),
    ('drawing/graphic art', 'Drawing/Graphic Art'),
    ('reading', 'Reading'),
    ('smoking', 'Smoking'),
    ('music', 'Music'),
    ('swimming', 'Swimming'),
    ('working out', 'Working Out'),
    ('comics', 'Comics'),
    ('movies', 'Movies'),
    ('video games', 'Video Games'),
    ('camping', 'Camping'),
    ('hunting', 'Hunting'),
    ('hiking', 'Hiking'),
    ('gardening', 'Gardening'),
    ('traveling', 'Traveling'),
]

AGE_RANGE = [
    (0, 'Select'),
    (1, '0-6 Years Old'),
    (2, '7-12 Years Old'),
    (3, '13-15 Years Old'),
    (4, '17-20 Years Old'),
    (5, '21-28 Years Old'),
    (6, '29-35 Years Old'),
    (7, '36+ Years Old'),

]
PRICE_RANGE = [
    (0, 'Select'),
    (1, '$'),
    (2, '$$'),
    (3, '$$$'),
    (4, '$$$$'),
]

SORT_BY = [
    (0, 'Price Low to High'),
    (1, 'Price High to Low'),
    (2, 'Featured'),
    (3, 'Average Review'),
    (4, 'Most Recent'),
]