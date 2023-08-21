from dataclasses import dataclass

@dataclass
class Podcast:
    # name: str 
    rss: str



@dataclass
class SubscriptionModel:
    user_email: str 
    podcasts: list[Podcast]
    receive_suggestions: bool

