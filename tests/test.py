from scratch import Channel
import pytest

def test_str():
    channel_id = Channel("UCMCgOm8GZkHp8zJ6l7_hIuA")
    assert channel_id.__str__() == "Youtube-канал: вДудь"


def test_lt():
    channel_id = Channel("UCByhZ-JEe5OOZSuq0uaXOng")
    other_id = Channel("UCMCgOm8GZkHp8zJ6l7_hIuA")
    assert (channel_id.subscriber_count > other_id.subscriber_count) is True


