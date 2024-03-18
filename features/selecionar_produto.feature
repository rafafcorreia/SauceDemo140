Feature: Selecionar Produto

  Scenario: Selecionar produto "Sauce Labs Backpack"
    Given que acesso o site Sauce Demo
    When preencho os campos de login com usuario standard_user e senha secret_sauce
    Then sou direcionado para página Home

  Scenario Outline: Selecionar produto com exemplos
    Given que acesso o site Sauce Demo
    When preencho os campos de login com <usuario> e <senha>
    Then sou direcionado para página Home

    Examples: 
      | usuario       | senha        |
      | standard_user | secret_sauce |
      | visual_user   | secret_sauce |
