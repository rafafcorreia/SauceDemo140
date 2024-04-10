*** Settings ***
Library    RequestsLibrary

*** Variables ***
${url}    https://petstore.swagger.io/v2/pet
${id}    1237214124
${pet_name}    Pipoca
&{category}    id=0    name=string
@{photoUrls}    string
&{tag}    id=1    name=vacinado
@{tags}    ${tag}
${status}    disponivel

*** Test Cases ***
Post Pet
    ${body}    Create Dictionary    id=${id}    category=${category}    name=${pet_name}    photoUrls=${photoUrls}    tags=${tags}    status=${status}

    ${response}    POST    url=${url}    json=${body}
    
    Log To Console    ${response.json()}
    Status Should Be    200
    Should Be Equal    ${response.json()}[id]    ${{int($id)}}
    Should Be Equal    ${response.json()}[name]    ${pet_name}
    Should Be Equal    ${response.json()}[tags][0][id]    ${{int(${tag}[id])}}
    Should Be Equal    ${response.json()}[tags][0][name]    ${tag}[name]
    Should Be Equal    ${response.json()}[status]    ${status}

Get Pet
    ${response}    GET    ${{$url + '/' + $id}}
    
    Log To Console    ${response.json()}
    Status Should Be    200
    Should Be Equal    ${response.json()}[id]    ${{int($id)}}
    Should Be Equal    ${response.json()}[name]    ${pet_name}
    Should Be Equal    ${response.json()}[tags][0][id]    ${{int(${tag}[id])}}
    Should Be Equal    ${response.json()}[tags][0][name]    ${tag}[name]
    Should Be Equal    ${response.json()}[status]    ${status}

Put Pet
    ${body}    Evaluate    json.loads(open('./fixtures/json/pet2.json').read())
    ${response}    PUT    url=${url}    json=${body}

    Log To Console    ${response.json()}
    Status Should Be    200
    Should Be Equal    ${response.json()}[id]    ${{int($id)}}
    Should Be Equal    ${response.json()}[name]    ${pet_name}
    Should Be Equal    ${response.json()}[tags][0][id]    ${{int(${tag}[id])}}
    Should Be Equal    ${response.json()}[tags][0][name]    ${tag}[name]
    Should Be Equal    ${response.json()}[status]    ${body}[status]

Delete Pet
    ${response}    DELETE    ${{$url + '/' + $id}}
    
    Log To Console    ${response.json()}
    Status Should Be    200
    Should Be Equal    ${response.json()}[message]    ${id}
    