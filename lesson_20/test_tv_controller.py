import pytest
import tv_controller

CHANNELS = ['BBC', 'Discovery', 'TV1000']
controller = tv_controller.TVController(CHANNELS)

def test_type_of_instance():
    assert isinstance(controller, tv_controller.TVController)

def test_input_list():
    assert controller.channels == CHANNELS

@pytest.mark.parametrize("index, string", [
    (controller.channels[0], 'BBC'),
    (controller.channels[1], 'Discovery'),
    (controller.channels[-1], 'TV1000')
])
def test_list_indexes(index, string):
    assert index == string

def test_first_channel():
    assert controller.first_channel() == CHANNELS[0]

def test_last_channel():
    assert controller.last_channel() == CHANNELS[-1]

@pytest.mark.parametrize("test_input, test_output", [
    (controller.turn_channel(1), 'BBC'),
    (controller.turn_channel(2), 'Discovery'),
    (controller.turn_channel(3), 'TV1000')
])
def test_turn_channel(test_input, test_output):
    assert test_input == test_output

@pytest.mark.parametrize("test_input, test_output", [
    (controller.next_channel(), 'Discovery'),
    (controller.next_channel(), 'TV1000'),
    (controller.next_channel(), 'BBC'),
])
def test_next_channel(test_input, test_output):
    controller.first_channel()
    assert test_input == test_output

@pytest.mark.parametrize("test_input, test_output", [
    (controller.previous_channel(), 'TV1000'),
    (controller.previous_channel(), 'Discovery'),
    (controller.previous_channel(), 'BBC'),
])
def test_previous_channel(test_input, test_output):
    controller.first_channel()
    assert test_input == test_output

def test_current_channel():
    assert controller.current_channel() == controller.channels[controller.counter]

@pytest.mark.parametrize("test_input, test_output", [
    (controller.is_exist(1), 'Yes'),
    (controller.is_exist(2), 'Yes'),
    (controller.is_exist(3), 'Yes'),
    (controller.is_exist(4), 'No'),
    (controller.is_exist('BBC'), 'Yes'),
    (controller.is_exist('TV1000'), 'Yes'),
    (controller.is_exist('Discovery'), 'Yes'),
    (controller.is_exist('TET'), 'No'),
])
def test_is_exist(test_input, test_output):
    assert test_input == test_output




