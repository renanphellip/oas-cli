ruleset_schema = {
    'type': 'object',
    'properties': {
        'rules': {
            'type': 'object',
            'patternProperties': {
                '^[a-zA-Z0-9_-]+$': {
                    'type': 'object',
                    'properties': {
                        'description': {'type': 'string'},
                        'message': {
                            'oneOf': [
                                {'type': 'string'},
                                {'type': 'array', 'items': {'type': 'string'}},
                            ]
                        },
                        'documentation': {
                            'oneOf': [
                                {'type': 'null'},
                                {'type': 'string'},
                                {'type': 'array', 'items': {'type': 'string'}},
                            ]
                        },
                        'severity': {
                            'type': 'string',
                            'enum': ['error', 'warn'],
                            'default': 'warn',
                        },
                        'given': {
                            'oneOf': [
                                {'type': 'string'},
                                {'type': 'array', 'items': {'type': 'string'}},
                            ]
                        },
                        'then': {
                            'type': 'object',
                            'properties': {
                                'function': {'type': 'string'},
                                'functionOptions': {
                                    'type': ['object'],
                                    'minProperties': 1,
                                    'additionalProperties': {'type': 'string'},
                                },
                            },
                            'required': ['function'],
                        },
                    },
                    'required': ['description', 'message', 'given', 'then'],
                }
            },
        }
    },
    'required': ['rules'],
    'additionalProperties': False,
}
