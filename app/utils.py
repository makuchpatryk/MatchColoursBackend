def get_error_message(self, exc) -> str:
    if hasattr(exc, 'message_dict'):
        return exc.message_dict
    error_msg = self.get_first_matching_attr(exc, 'message', 'messages')

    if isinstance(error_msg, list):
        error_msg = ', '.join(error_msg)

    if error_msg is None:
        error_msg = str(exc)

    return error_msg