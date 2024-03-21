Feature: Selecionar Produto

  Scenario: Selecionar produto "Sauce Labs Backpack"
    Given que acesso o site Sauce Demo
    When preencho os campos de login com usuario standard_user e senha secret_sauce
    Then sou direcionado para página Home

  Scenario Outline: Login invalido
    Given que acesso o site Sauce Demo
    When preencho os campos de login com usuario <usuario> e senha <senha>
    Then exibe mensagem <mensagem>

    Examples: 
      | usuario       | senha        | mensagem                                                                  |
      | standard_user | uva          | Epic sadface: Username and password do not match any user in this service |
      | standard_user |              | Epic sadface: Password is required                                        |
      | fulano        | secret_sauce | Epic sadface: Username and password do not match any user in this service |
      | fulano        | uva          | Epic sadface: Username and password do not match any user in this service |
      | fulano        |              | Epic sadface: Password is required                                        |
      |               | secret_sauce | Epic sadface: Username is required                                        |
      |               | uva          | Epic sadface: Username is required                                        |
      |               |              | Epic sadface: Username is required                                        |
