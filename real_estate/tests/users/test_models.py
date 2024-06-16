import pytest


def test_user_str(base_user):
    """Test the custom user model str representation"""

    assert base_user.__str__() == f"{base_user.username}"


def test_user_short_name(base_user):
    """Test the custom user model get_short_name method works"""

    short_name = f"{base_user.username}"
    assert base_user.get_short_name == short_name


def test_user_full_name(base_user):
    """Test the custom user model get_full_name method works"""

    full_name = f"{base_user.first_name} {base_user.last_name}"
    assert base_user.get_full_name == full_name


def test_base_user_email_is_normalized(base_user):
    """Test the user's email gets normalized"""

    email = "alpha@RState.com"
    assert base_user.email == email.lower()


def test_super_user_email_is_normalized(create_superuser):
    """Test the super user's email gets normalized"""

    email = "alpha@RState.com"
    assert create_superuser.email == email.lower()


def test_super_user_is_not_staff(user_factory):
    """Test that an error is raised if the super user has is_staff true"""

    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=False)

    assert str(err.value) == "Superuser must have is_staff=True"


def test_super_user_is_not_super_user(user_factory):
    """Test that error is raised if the super user is not the super user."""

    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=False, is_staff=True)

    assert str(err.value) == "Superuser must have is_superuser=True"


def test_create_user_with_no_email(user_factory):
    """Test that error is raised if email is not passed for the user"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email=None)

    assert str(err.value) == "Base User Account: An email address is required"


def test_create_user_with_no_username(user_factory):
    """Test that error is raised if username is not passed for the user"""

    with pytest.raises(ValueError) as err:
        user_factory.create(username=None)

    assert str(err.value) == "Users must submit a username"


def test_create_user_with_no_first_name(user_factory):
    """Test that error is raised if firstname is not passed for the user"""

    with pytest.raises(ValueError) as err:
        user_factory.create(first_name=None)

    assert str(err.value) == "Users must submit a first name"


def test_create_user_with_no_last_name(user_factory):
    """Test that error is raised if lastname is not passed for the user"""

    with pytest.raises(ValueError) as err:
        user_factory.create(last_name=None)

    assert str(err.value) == "Users must submit a last name"


def test_create_super_user_with_no_email(user_factory):
    """Test that error is raised if email is not passed for the user"""

    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=True, email=None)

    assert str(err.value) == "Admin Account: An email address is required"


def test_create_super_user_with_no_password(user_factory):
    """Test that error is raised if password is not passed for the user"""

    with pytest.raises(ValueError) as err:
        user_factory.create(is_superuser=True, is_staff=True, password=None)

    assert str(err.value) == "Superuser must have a password"


def test_user_email_incorrect(user_factory):
    """Test that error is raised if the invalid email is provided"""

    with pytest.raises(ValueError) as err:
        user_factory.create(email="fake.com")

    assert str(err.value) == "You must provide a valid email address!"
