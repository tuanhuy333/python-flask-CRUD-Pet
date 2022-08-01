import connexion
import six

from swagger_server.models.pet import Pet  # noqa: E501
from swagger_server.models.pets import Pets  # noqa: E501
from swagger_server import util


def add_pet(body):  # noqa: E501
    """Add a new pet to the store

     # noqa: E501

    :param body: Pet to add to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_all_pets():  # noqa: E501
    """Gets all pets in the store

     # noqa: E501


    :rtype: Pets
    """
    return 'do some magic!'


def get_pet(pet_id):  # noqa: E501
    """Get a pet in the store

     # noqa: E501

    :param pet_id: The id of the pet to retrieve
    :type pet_id: str

    :rtype: Pet
    """
    return 'do some magic!'


def remove_pet(pet_id):  # noqa: E501
    """Remove a pet in the store

     # noqa: E501

    :param pet_id: The id of the pet to remove from the store
    :type pet_id: str

    :rtype: None
    """
    return 'do some magic!'


def update_pet(pet_id, Pet):  # noqa: E501
    """Update and replace a pet in the store

     # noqa: E501

    :param pet_id: The id of the pet to update from the store
    :type pet_id: str
    :param Pet: 
    :type Pet: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Pet = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
