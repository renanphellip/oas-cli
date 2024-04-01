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
                            'oneOf': [
                                {
                                    'type': 'object',
                                    'properties': {
                                        'function': {'type': 'string'},
                                        'functionOptions': {
                                            'type': ['object'],
                                            'minProperties': 1,
                                            'additionalProperties': {
                                                'oneOf': [
                                                    {'type': 'string'},
                                                    {'type': 'number'},
                                                    {'type': 'boolean'},
                                                ]
                                            },
                                        },
                                    },
                                    'required': ['function'],
                                },
                                {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'minProperties': 1,
                                        'properties': {
                                            'field': {'type': 'string'},
                                            'function': {'type': 'string'},
                                        },
                                        'required': ['field', 'function'],
                                    }
                                }
                            ]
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
