from django import forms

HOBBIES = [
    ('none', 'Select'),
    ('gaming', 'Gaming'),
    ('outdoors', 'Outdoors'),
    ('pets', 'Pets'),
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