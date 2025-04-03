##Variable arguments with keyword

#using **

def variable_key_word(**names):
    for key, name in names.items():
        print(f"Hello, {name} ({key})")

variable_key_word(
    #We'll set the key word here (at the left)
    language = "French",
    name = "Javier",
    last_name = "Medina",
    age = 55
)

variable_key_word()