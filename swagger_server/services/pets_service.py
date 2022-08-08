import json


def get_all_pets():
    pets = read_from_file()
    pets_in_store = []
    for k, v in pets.items():
        current_pet = {"id": k, **v}
        pets_in_store.append(current_pet)

    return pets_in_store


def remove_pet(id):
    pets = read_from_file()
    del pets[id]
    write_to_file(pets)


def update_pet(id, pet):
    pets = read_from_file()
    ids = pets.keys()
    pets[id] = {"name": pet.name, "breed": pet.breed, "price": pet.price}
    write_to_file(pets)


def add_pet(pet):
    pets = read_from_file()
    ids = list(pets.keys())
    new_id = int(ids[-1]) + 1
    pets[new_id] = {"name": pet.name, "breed": pet.breed, "price": pet.price}
    write_to_file(pets)
    print("Created {pet}".format(pet = pets[new_id]))


def get_pet(id):
    pets = read_from_file()
    pet = pets[id] # get pet
    pet["id"] = id  # add id
    return pet


def write_to_file(content):
    with open("swagger_server\services\pets.json", "w") as pets:
        pets.write(json.dumps(content))


def read_from_file():
    with open("swagger_server\services\pets.json", "r") as pets:
        return json.loads(pets.read())