from datetime import datetime


def check_body_tasks(
    actual_keys: list,
    expected_keys: list = ('name', 'description', 'priority', 'deadline'),
) -> bool:
    expected_keys_set = set(expected_keys)
    actual_keys_set = set(actual_keys)
    if len(expected_keys_set.intersection(actual_keys_set)) == 4:
        return True
    return False


def check_datetime_fields(body: dict) -> dict | None:
    deadline_str = body.get('deadline')
    if deadline_str:
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d %H:%M')
            return {'deadline': deadline}
        except ValueError:
            return None