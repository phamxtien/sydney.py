class NoConnectionException(Exception):
    pass

class NoResponseException(Exception):
    pass

class ThrottledRequestException(Exception):
    pass

class CaptchaChallengeException(Exception):
    pass

class ConversationLimitException(Exception):
    pass

class CreateConversationException(Exception):
    pass

class GetConversationsException(Exception):
    pass
