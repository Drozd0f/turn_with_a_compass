def direction(facing: str, turn: int) -> str:
    directions = {
        'N': 0,
        'NE': 45,
        'E': 90,
        'SE': 135,
        'S': 180,
        'SW': 225,
        'W': 270,
        'NW': 315
    }
    result = ((directions[facing] + turn) // 45) % 8
    return list(directions)[result]


if __name__ == '__main__':
    assert direction("S", 180) == "N"
    assert direction("SE", -45) == "E"
    assert direction("W", 495) == "NE"
