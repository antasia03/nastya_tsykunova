is_allowed = (is_admin or (is_active and has_permission)) and not is_blocked
