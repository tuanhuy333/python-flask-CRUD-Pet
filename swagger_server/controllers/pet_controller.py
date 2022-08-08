import connexion
from flask import render_template
import six

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.models.pets import Pets  # noqa: E501
from swagger_server import util
from swagger_server.services import pets_service


def add_pet(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: Pet to add to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
        print("abc123" + str(body))
        pets_service.add_pet(body)
    return {}, 201


def get_all_pets():  # noqa: E501
    """Gets all pets in the store

     # noqa: E501


    :rtype: Pets
    """
    petsAll = pets_service.get_all_pets()
    print("petsAll {pet}".format(pet = petsAll))
    pets_in_store = []
    for pet in petsAll:
        current_pet = Pet(id=pet["id"], breed=pet["breed"],price=pet["price"],name=pet["name"])
        pets_in_store.append(current_pet)
    return pets_in_store, 200


def get_pet(pet_id):  # noqa: E501
    """Get a pet in the store

     # noqa: E501

    :param pet_id: The id of the pet to retrieve
    :type pet_id: str

    :rtype: Pet
    """
    try:
        pet = pets_service.get_pet(pet_id)
        response = Pet(id=pet["id"], breed=pet["breed"],price=pet["price"],name=pet["name"])
    except KeyError:
        response = {},404
    return response


def remove_pet(pet_id):  # noqa: E501
    """Remove a pet in the store

     # noqa: E501

    :param pet_id: The id of the pet to remove from the store
    :type pet_id: str

    :rtype: None
    """
    try:
        pets_service.remove_pet(pet_id)
        response = {},200
    except KeyError:
        response = {},404
    return response



def update_pet(pet_id, new_pet):# noqa: E501
    """Update and replace a pet in the store

     # noqa: E501

    :param pet_id: The id of the pet to update from the store
    :type pet_id: str
    :param Pet: 
    :type Pet: dict | bytes

    :rtype: None
    """
   
    if connexion.request.is_json:
        new_pet = Pet.from_dict(connexion.request.get_json())  # noqa: E501

    try:
        pets_service.update_pet(pet_id, new_pet)
        response = {}, 200
    except KeyError:
        response = {}, 404

    return response
