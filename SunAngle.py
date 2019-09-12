
"""
Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises 
in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, 
which meansthat the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees.
If the input will be 
the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".
"""


def hours_to_min_converter(time):
    hours = int(time[:2])
    mins = int(time[3:])
    minutes = mins + hours * 60
    return minutes


def sun_angle(time):
    if hours_to_min_converter(time) < 359 or hours_to_min_converter(time) > 1080:
        return "I don't see the sun!"
    angle_of_sun = hours_to_min_converter(time) * 0.25 - 90
    return angle_of_sun


if __name__ == '__main__':
    print("Example:")
    print(hours_to_min_converter("07:12"))
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("18:00") == 180
    assert sun_angle("06:00") == 0
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
