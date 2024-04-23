*** Settings ***
Library     RequestsLibrary

*** Variables ***
${url}    https://petstore.swagger.io/v2/pet
${id}    1237214124
${pet_name}    Pipoca
# Dicionario
&{category}    id=0    name=string
@{photoUrls}     
&{tag}    id=1    name=vacinado
# Lista
@{tags}    ${tag}
${status}    disponivel

*** Test Cases ***
Post Pet
    ${body}    Create Dictionary    id=${id}    category=${category}    name=${pet_name}    
    ...                             photoUrls=${photoUrls}    tags=${tags}    status=${status}

    ${response}    POST    url=${url}    json=${body}
    
    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
    Status Should Be    200
    Should Be Equal    ${response_body}[id]    ${{int($id)}}
    Should Be Equal    ${response_body}[name]    ${pet_name}
    Should Be Equal    ${response_body}[tags][0][id]    ${{int(${tag}[id])}}
    Should Be Equal    ${response_body}[tags][0][name]    ${tag}[name]
    Should Be Equal    ${response_body}[status]    ${status}

Get Pet
    ${response}    GET    ${{$url + '/' + $id}}
    
    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
    Status Should Be    200
    Should Be Equal    ${response_body}[id]    ${{int($id)}}
    Should Be Equal    ${response_body}[name]    ${pet_name}
    Should Be Equal    ${response_body}[tags][0][id]    ${{int(${tag}[id])}}
    Should Be Equal    ${response_body}[tags][0][name]    ${tag}[name]
    Should Be Equal    ${response_body}[status]    ${status}

Put Pet
    ${body}    Evaluate    json.loads(open('./fixtures/json/pet2.json').read())
    ${response}    PUT    url=${url}    json=${body}

    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
    Status Should Be    200
    Should Be Equal    ${response_body}[id]    ${{int($id)}}
    Should Be Equal    ${response_body}[name]    ${pet_name}
    Should Be Equal    ${response_body}[tags][0][id]    ${{int(${tag}[id])}}
    Should Be Equal    ${response_body}[tags][0][name]    ${tag}[name]
    Should Be Equal    ${response_body}[status]    ${body}[status]

Delete Pet
    ${response}    DELETE    ${{$url + '/' + $id}}
    
    ${response_body}    Set Variable    ${response.json()}
    Log To Console    ${response_body}
    Status Should Be    200
    Should Be Equal    ${response_body}[message]    ${id}
    