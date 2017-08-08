
class UnAuthorizedException(Exception):
    """
        This is used when the password and user name didn't match
    """

    def __init__(self, message):
        self.message = message


class UserExistsException(Exception):
    """
       This is used When the email not exists in the database for reset password
    """

    def __init__(self, message):
        self.message = message


class InvalidTokenException(Exception):
    """
        This is used when the token for reset password is invalid
    """

    def __init__(self, message):
        self.message = message


class ResourceNotFound(Exception):
    """
        This exception is raised when the requested resource is not present on the database
    """

    def __init__(self, message):
        self.message = message


class InvalidType(Exception):
    """
    This exception is raised when the cart item type is not defined
    """

    def __init__(self, message):
        self.message = message


class RuleCheckerFailed(Exception):
    """
        This exception is raised when the rule checker failed
    """

    def __init__(self, message):
        self.message = message


class S3Exception(Exception):
    """
        This exception is raised when the file is tried to save or get from S3
    """

    def __init__(self, message):
        self.message = message


class InvalidCloneDirection(Exception):
    """
        This exception is raised when the clone direction is given apart from left or right
    """

    def __init__(self, message):
        self.message = message;


class CloneNotPossible(Exception):
    """
        This exception is raised when clone is not possible
    """

    def __init__(self, message):
        self.message = message


class AddingSectionNotPossible(Exception):
    """
        This exception is raised when there is no possibility of adding section
    """

    def __init__(self, message):
        self.message = message


class InvalidInput(Exception):
    """
        This exception is raised when the input is not equal to the expected input by server
    """

    def __init__(self, message):
        self.message = message


class ObjectDoesNotExist(Exception):
    """
        This Exception is raised when django get returns zero elements in query set
    """

    def __init__(self, message):
        self.message = message


class InvalidComponentsForSofa(Exception):
    """
        This Exception is raised when given components doesn't exist in the sofa
    """

    def __init__(self, message):
        self.message = message


class InvalidComponents(Exception):
    """
        This exception is raised when the given components doesn't match the product components
    """

    def __init__(self, message):
        self.message = message


class InvalidOptions(Exception):
    """
        This exception is raised when the given option doesn't match the product options
    """

    def __init__(self, message):
        self.message = message


class InvalidDesign(Exception):
    """
        This exception is raised when the given option doesn't match the product options
    """

    def __init__(self, message):
        self.message = message

