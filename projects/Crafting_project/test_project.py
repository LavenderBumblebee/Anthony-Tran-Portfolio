from project import check_dictionary, amount, craft_req
import pytest

def test_check_dictionary_correct():
    assert check_dictionary("CAP") == "🧢"
    assert check_dictionary (" cap" ) == "🧢"
    assert check_dictionary ("MAGIC wANd") == "🪄"
    assert check_dictionary ("wAND") == "🪄"
    assert check_dictionary (" wand  ") == "🪄"
    assert check_dictionary("bOMB") == "💣"
    assert check_dictionary ("  bomb  ") == "💣"
    assert check_dictionary ("tENT") == "🏕️"
    assert check_dictionary ("CAKE") == "🎂"
    assert check_dictionary ("   BoW   ") == "🏹"
def test_check_dictionary_error():
    with pytest.raises(IndexError):
        assert check_dictionary("dog") == ("No object by that name")
    with pytest.raises(IndexError):
        assert check_dictionary("capp") == ("No object by that name")
    with pytest.raises(IndexError):
        assert check_dictionary("cakes") == ("No object by that name")
    with pytest.raises(IndexError):
        assert check_dictionary("caps") == ("No object by that name")
    with pytest.raises(IndexError):
        assert check_dictionary("bows") == ("No object by that name")

def test_amount_correct():
    assert amount("cap", 2) == ("🧢",2)
    assert amount("wand", 3) == ("🪄", 3)
    assert amount("TENT", 5) == ("🏕️",5)
    assert amount("caKE",6) == ("🎂",6)
def test_amount_error():
    with pytest.raises(ValueError):
        assert amount("tent"," ") == "Put in a number for the second input"
    with pytest.raises(ValueError):
        assert amount("bow", "cap") == "Put in a number for the second input"
    with pytest.raises(ValueError):
        assert amount("cap", "bow") == "Put in a number for the second input"
    with pytest.raises(IndexError): # error caught under check_dictionary because amount has to go through check_dictionary
        assert amount ("l", "3") == "No object by that name"
    with pytest.raises(IndexError):
        assert amount("5","4") == "No object by that name"
    with pytest.raises(IndexError):
        assert amount("cop","5") == "No object by that name"


def test_craft_req_correct():
    assert craft_req("cap", 2) == "You need 10 cloth, 2 needle, and 2 spool to make 2 🧢's"
    assert craft_req("cap",1) == "You need 5 cloth, 1 needle, and 1 spool to make 1 🧢"
    assert craft_req("sword",5) == "You need 30 iron, 15 wood, and 5 hammer to make 5 ⚔'s"
    assert craft_req("bow",3) == "You need 30 string, 15 wood, and 9 rope to make 3 🏹's"
    assert craft_req("cake",1)== "You need 6 egg, 12 sugar, 1 milk bucket, and 15 flour to make 1 🎂"
    # add index Error's for first value to check wrong, and strings for second value for value error for the second input

def test_craft_req_error():
    with pytest.raises(IndexError):
        assert craft_req("1","4") == "No object by that name"
    with pytest.raises(IndexError):
        assert craft_req("bake","4") == "No object by that name"
    with pytest.raises(IndexError):
        assert craft_req("Cakes","cake") == "No object by that name"
    with pytest.raises(ValueError):
        assert craft_req("cake","object") == "Put in a number for the second input"
    with pytest.raises(ValueError):
        assert craft_req("sword","cake") == "Put in a number for the second input"


















