import requests

def fetch_tenderly_simulation_data(url):
    res = requests.post(url)
    res.raise_for_status()  # Raise an exception if the request was unsuccessful
    return res.json()

def transform_tenderly_simulation_data(event):
    """
    Transforms transaction data received from the simulation to a json
    Includes relevant information for each type of action executed

    Events supported:
    - Approval (from the Safe executing payload)
    - ScopeTarget
    - RevokeTarget
    - ScopeAllowFunction
    - ScopeFunction
    - ScopeParameterAsOneOf
    - ScopeRevokeFunction
    
    Args:
    - event json with a single event call trace logs from tenderly simulation

    Returns:
    - json-like dict containing relevant information for the event
    """

    if event['name'] == 'Approval':
        """
        Approval Events
        - name: event name
        - token: ERC20 contract address being allowed
        - owner
        - spender
        - value
        """
        json_ = {
            'name': 'Approval',
            'token': event['raw']['address'],  # raw - address being called
            'owner': event['inputs'][0]['value'],  # 0 - position for `owner` in the Approve event
            'spender': event['inputs'][1]['value'],  # 1 - position for `spender` in the Approve event
            'value': event['inputs'][2]['value']  # 2 - position for `value` in the Approve event
        }
    
    elif event['name'] == 'ScopeTarget':
        """
        ScopeTarget Events
        - name: event name
        - roles_mod: Roles contract address (being called)
        - role
        - targetAddress
        """
        json_ = {
            'name': 'ScopeTarget',
            'roles_mod': event['raw']['address'],  # raw - address being called
            'role': event['inputs'][0]['value'],  # 0 - position for `role` in the ScopeTarget event
            'targetAddress': event['inputs'][1]['value'],  # 1 - position for the `targetAddress` in the ScopeTarget event
        }

    elif event['name'] == 'RevokeTarget':
        """
        RevokeTarget Events
        - name: event name
        - id: position of the transaction in the payload
        - roles_mod: Roles contract address (being called)
        - role
        - targetAddress
        """
        json_ = {
            'name': 'RevokeTarget',
            'roles_mod': event['raw']['address'],  # raw - address being called
            'role': event['inputs'][0]['value'],  # 0 - position for `role` in the RevokeTarget event
            'targetAddress': event['inputs'][1]['value'],  # 1 - position for the `targetAddress` in the RevokeTarget event
        }
    
    elif event['name'] == 'ScopeAllowFunction':
        """
        ScopeAllowFunction Events
        - name: event name
        - id: position of the transaction in the payload
        - roles_mod: Roles contract address (being called)
        - role
        - targetAddress
        - selector
        - options
        """
        json_ = {
            'name': 'ScopeAllowFunction',
            'roles_mod': event['raw']['address'],  # raw - address being called
            'role': event['inputs'][0]['value'],  # 0 - position for `role` in the ScopeAllowFunction event
            'targetAddress': event['inputs'][1]['value'],  # 1 - position for the `targetAddress` in the ScopeAllowFunction event
            'selector': event['inputs'][2]['value'],  # 2 - position of the `selector` in the ScopeAllowFunction event
            'options': event['inputs'][3]['value']  # 3 - position of the `options` in the ScopeAllowFunction event
        }

    elif event['name'] == 'ScopeFunction':
        """
        ScopeFunction Events
        - name: event name
        - id: position of the transaction in the payload
        - roles_mod: Roles contract address (being called)
        - role
        - targetAddress
        - functionSig
        - isParamScoped
        - paramType
        - paramComp
        - compValue
        - options
        """
        json_ = {
            'name': 'ScopeFunction',
            'roles_mod': event['raw']['address'],  # raw - address being called
            'role': event['inputs'][0]['value'],  # 0 - position for `role` in the ScopeFunction event
            'targetAddress': event['inputs'][1]['value'],  # 1 - position for the `targetAddress` in the ScopeFunction event
            'functionSig': event['inputs'][2]['value'],  # 2 - position of the `functionSig` in the ScopeFunction event
            'isParamScoped': event['inputs'][3]['value'],  # 3 - position of the `isParamScoped` in the ScopeFunction event - come in list format
            'paramType': event['inputs'][4]['value'],  # 4 - position of the `paramType` in the ScopeFunction event - not readble correctly in Tenderly simulation
            'paramComp': event['inputs'][5]['value'],  # 5 - position of the `paramComp` in the ScopeFunction event - not readble correctly in Tenderly simulation
            'compValue': event['inputs'][6]['value'],  # 6 - position of the `compValue` in the ScopeFunction event - come in list format
            'options': event['inputs'][7]['value']  # 7 - position of the `options` in the ScopeFunction event
        }

    
    elif event['name'] == 'ScopeParameterAsOneOf':
        """
        ScopeParameterAsOneOf Events
        - name: event name
        - id: position of the transaction in the payload
        - roles_mod: Roles contract address (being called)
        - role
        - targetAddress
        - functionSig
        - index
        - paramType
        - compValues
        """
        json_ = {
            'name': 'ScopeParameterAsOneOf',
            'roles_mod': event['raw']['address'],  # raw - address being called
            'role': event['inputs'][0]['value'],  # 0 - position for `role` in the ScopeParameterAsOneOf event
            'targetAddress': event['inputs'][1]['value'],  # 1 - position for the `targetAddress` in the ScopeParameterAsOneOf event
            'functionSig': event['inputs'][2]['value'],  # 2 - position of the `functionSig` in the ScopeParameterAsOneOf event
            'index': event['inputs'][3]['value'],  # 3 - position of the `index` in the ScopeParameterAsOneOf event
            'paramType': event['inputs'][4]['value'],  # 4 - position of the `paramType` in the ScopeParameterAsOneOf event - not readble correctly in Tenderly simulation
            'compValues': event['inputs'][5]['value'],  # 5 - position of the `compValues` in the ScopeParameterAsOneOf event - come in list format
        }

    elif event['name'] == 'ScopeRevokeFunction':
        """
        ScopeRevokeFunction Events
        - name: event name
        - id: position of the transaction in the payload
        - roles_mod: Roles contract address (being called)
        - role
        - targetAddress
        - selector
        """
        json_ = {
            'name': 'ScopeRevokeFunction',
            'roles_mod': event['raw']['address'],  # raw - address being called
            'role': event['inputs'][0]['value'],  # 0 - position for `role` in the ScopeRevokeFunction event
            'targetAddress': event['inputs'][1]['value'],  # 1 - position for the `targetAddress` in the ScopeRevokeFunction event
            'selector': event['inputs'][2]['value']  # 2 - position of the `selector` in the ScopeRevokeFunction event
        }
    
    else:

        json_ = {}
    
    return json_