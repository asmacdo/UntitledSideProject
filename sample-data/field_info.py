FIELD_SCHEMA = {
field_info: {
    'boost_pads': [
        {'location': Vector3, 'is_full_boost': boolean},
    ],
    'num_boosts': int,
    'goals': [
        {'team_num': int, 'location': Vector3, 'direction': Vector3 },
    ],
    'num_goals': int
}
