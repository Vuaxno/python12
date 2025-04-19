import pytest
from television import Television

def test_init():
    tv = Television()
    assert tv._status is False
    assert tv._muted is False
    assert tv._volume == Television.MIN_VOLUME
    assert tv._channel == Television.MIN_CHANNEL
    assert str(tv) == f"Power – False, Channel – {Television.MIN_CHANNEL}, Volume – {Television.MIN_VOLUME}"

def test_power_toggle():
    tv = Television()
    tv.power()
    assert tv._status is True
    assert "Power – True" in str(tv)
    tv.power()
    assert tv._status is False
    assert "Power – False" in str(tv)

def test_mute_toggle():
    tv = Television()
    tv.power()
    tv.mute()
    assert tv._muted is True
    tv.mute()
    assert tv._muted is False
    tv.power()
    tv.power()
    tv.mute()
    assert tv._muted is True

def test_channel_up_wrap_and_off():
    tv = Television()
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL + 1
    tv._channel = Television.MAX_CHANNEL
    tv.channel_up()
    assert tv._channel == Television.MIN_CHANNEL

def test_channel_down_wrap_and_off():
    tv = Television()
    tv.channel_up()
    tv.channel_down()
    assert tv._channel == Television.MIN_CHANNEL
    tv._channel = Television.MIN_CHANNEL
    tv.channel_down()
    assert tv._channel == Television.MAX_CHANNEL

def test_volume_up_behavior():
    tv = Television()
    tv.volume_up()
    assert tv._volume == Television.MIN_VOLUME + 1
    tv._volume = Television.MAX_VOLUME
    tv.volume_up()
    assert tv._volume == Television.MAX_VOLUME

def test_volume_down_behavior():
    tv = Television()
    tv._volume = Television.MAX_VOLUME
    tv.volume_down()
    assert tv._volume == Television.MAX_VOLUME - 1
    tv._volume = Television.MIN_VOLUME
    tv.volume_down()
    assert tv._volume == Television.MIN_VOLUME

def test_volume_unmute_on_change():
    tv = Television()
    tv._muted = True
    tv.volume_up()
    assert tv._muted is False
    tv._muted = True
    tv.volume_down()
    assert tv._muted is False
