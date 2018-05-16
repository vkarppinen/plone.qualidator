

def validate_dublin_core(context):
    to_validate = [
        dict(name='Title', value=context.title),
        dict(name='Description', value=context.description)
    ]

    validations = []
    for item in to_validate:
        validations.append(handle_text_validation(item))

    return validations


def handle_text_validation(item):
    validation = dict(name=item['name'], errors=[])
    if len(item['value']) == 0:
        validation['errors'].append(
            u'{} should not be empty.'.format(item['name'])
         )

    return validation

