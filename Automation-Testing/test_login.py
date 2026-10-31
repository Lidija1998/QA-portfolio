def test_valid_login():

    username = "admin"
    password = "12345"

    assert username == "admin"
    assert password == "12345"

    print("Login test PASSED")


def test_invalid_login():

    username = "admin"
    password = "wrong"

    assert password != "12345"

    print("Invalid login test PASSED")


test_valid_login()
test_invalid_login()
