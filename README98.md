# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39abdce0-2c91-30ae-983f-1922027a62ed | -21.58551 | -48.41925 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ffe993ba-ec6c-34f6-8e43-961eec6a2e57 | -16.49545 | -55.14619 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6861d3c9-21d3-3c79-8ff9-f4a7e55fc9e3 | -17.28761 | -46.10908 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 35612f67-15f1-3fad-a774-a92dbab323eb | -15.10505 | -60.21244 | 2025-09-13 05:01:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11dd0dd8-c490-330a-a421-0206618c065e | -17.28219 | -46.10483 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 49db8915-8c8b-3f4a-8303-c5a22fc76188 | -16.60906 | -49.46352 | 2025-09-13 05:01:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2491ed72-6eda-32a5-bbec-d0c9f45f7101 | -17.43425 | -49.2216 | 2025-09-13 05:01:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d08b2d61-e20e-33ad-99cf-8dae38141e40 | -18.00634 | -46.92187 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 604c54c8-673d-3756-af3f-93600353d1b1 | -22.83327 | -50.99746 | 2025-09-13 05:01:00 | NOAA-21 | PRIMEIRO DE MAIO | PARANÁ | Brasil | 4120507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5b05825a-b0ce-3246-8812-28044b14fe8f | -17.54299 | -44.55619 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a74e9017-c67a-388c-b1b7-8a3a32268ad5 | -17.33524 | -46.66299 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 295525da-e1dc-38c2-9472-b24c45ff4500 | -16.3316 | -51.54176 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1b295f27-564d-3a5f-9a5a-f3d971f1b0c9 | -17.41099 | -49.25661 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f20455f-a88d-3f89-9d62-f1fa84336563 | -19.67296 | -57.00625 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b9d0fa31-638a-3eb8-98ee-d8d520996350 | -18.13693 | -48.4567 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58217b33-f7c7-333b-9faf-1e345d6d558d | -20.45528 | -46.43776 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5273f9e-5ff0-3069-8bc9-b5be5ec8dd45 | -19.33608 | -45.11074 | 2025-09-13 05:01:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38df7a8f-0aaf-301e-8b61-f0ba32572a49 | -23.60408 | -51.05408 | 2025-09-13 05:01:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66f85aa5-f6dd-3d57-aa8b-e654047932b9 | -18.00035 | -46.9255 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a1e2ae7-5cf5-35cc-ad07-881ca33b977f | -20.64948 | -48.69437 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78711503-49d0-395f-be87-93590e512401 | -17.14854 | -53.89463 | 2025-09-13 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b06f1d2-30b0-37b7-ad82-ad264c2c07db | -18.00859 | -48.6535 | 2025-09-13 05:01:00 | NOAA-21 | MARZAGÃO | GOIÁS | Brasil | 5212907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0114fc5e-e919-3a02-8bab-59b75b7eac31 | -17.54521 | -44.55071 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2962cd18-5225-379a-a783-f7b01a5773e0 | -17.33901 | -46.66514 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d5465586-c4e3-35d2-bdd0-536a27bd745a | -17.2872 | -47.25566 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26b9643e-2fd4-344b-9949-c2cfb206d55b | -21.61848 | -46.81093 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 41ef8304-590c-3bee-8497-84e5077e45e7 | -20.55582 | -45.83263 | 2025-09-13 05:01:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 216f4e0a-a866-3104-abfc-9ee71bfd9f95 | -18.04225 | -45.4272 | 2025-09-13 05:01:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9540ed6d-8478-3636-8e20-9d5777c9a247 | -20.09788 | -46.90672 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52c0d821-5a73-3218-b001-8c81b8d84cb6 | -20.65182 | -48.69287 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea7177cf-8c63-3a7e-b2da-a666e8905a9d | -16.49879 | -55.1235 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cc4dcc86-10d7-3781-964f-24357e387219 | -17.27777 | -46.09088 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d9778ae8-8062-3e80-8492-31db6c1f4c95 | -23.80889 | -50.08761 | 2025-09-13 05:01:00 | NOAA-21 | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 36265c8f-d506-3e03-9ef4-e7e33b21ca83 | -19.99452 | -46.90397 | 2025-09-13 05:01:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05445278-2cdd-3d64-8dda-00dce95dc834 | -20.64437 | -48.69371 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 175269a7-1fe2-39c2-925c-db80b71b43b4 | -23.81069 | -50.08759 | 2025-09-13 05:01:00 | NOAA-21 | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c592b15-c658-3068-807d-6603ff33bd0b | -20.4414 | -46.45864 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7516573-ea65-3a33-949a-f1194ec96ccf | -16.53603 | -51.73817 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5aa90d54-8b48-3344-a969-9082ff149d79 | -18.15325 | -49.18881 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 2deaee5c-32e4-3672-a424-3816949739a9 | -19.61946 | -46.69587 | 2025-09-13 05:01:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43241943-16ab-3dc7-861d-19f0c9453390 | -17.28799 | -47.24855 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aa3e6b4e-6ee0-3c8a-aa97-f7fd712492d5 | -20.43603 | -56.95049 | 2025-09-13 05:01:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6cc3dbc-39f4-334a-b43b-6bbcb8c31702 | -21.62391 | -46.81612 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 9754a649-4a48-3844-b5f4-9f361cb34abc | -21.58586 | -48.41578 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16589aa9-a9c2-36fe-9345-093c7a30b92d | -22.66154 | -53.11463 | 2025-09-13 05:01:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c08cf3d9-3f63-37d3-bc24-de3ab24df92d | -18.15353 | -49.18573 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 7aed0afc-440d-3b96-81a4-7e02b5079e8f | -20.44941 | -46.43689 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08a639fa-0f5c-3ce8-be97-7588cb2ed092 | -16.36188 | -51.54182 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67d97bad-3fe7-32b1-9783-7b738a3136c0 | -18.89194 | -47.05639 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4f62845-c277-3b23-b036-be6aa20bfa61 | -16.4949 | -55.14994 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 636b9abb-30f8-3a26-a566-9485f4eaf2fb | -16.49486 | -55.12672 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 573adca0-8da9-3985-b55d-eec16b4e06db | -16.50164 | -55.15105 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 4a662534-90b9-351b-941d-6f14622af813 | -17.31104 | -48.7359 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ce23026f-fc7d-3d6a-8ead-f6a0f062dd8d | -16.49431 | -55.1305 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 2644759c-109b-3534-b05f-6e1c54a31e6a | -16.50109 | -55.15479 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 84453e2d-9a80-3748-b8d4-3c17ee3cd19f | -22.65758 | -53.11405 | 2025-09-13 05:01:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d15f672f-a97f-3ed7-bcea-a136538b407c | -18.39309 | -44.10054 | 2025-09-13 05:01:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 506b8e14-fbcc-31d0-91fc-4144ae04cc9e | -17.54568 | -44.54543 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 9358287e-3dcd-345b-9b92-dc813df70784 | -20.44255 | -46.44653 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c23fe33-8dcc-389b-bd35-9117e685f71b | -16.53005 | -51.75326 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11c24f82-b51a-3b0e-b902-1d05184bb35e | -16.49827 | -55.15049 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 74dbcf64-3376-3f27-b368-fe6f7f027c56 | -17.91459 | -44.45842 | 2025-09-13 05:01:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 84fd109f-7284-3e74-a7eb-97250f1c94d6 | -23.81375 | -50.08815 | 2025-09-13 05:01:00 | NOAA-21 | JAPIRA | PARANÁ | Brasil | 4112306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 69272290-c801-3393-9037-045981822c31 | -21.31472 | -47.3921 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 161cc3c7-91af-3e7e-a18b-7e5200733ace | -22.67272 | -53.12184 | 2025-09-13 05:01:00 | NOAA-21 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f4c15752-7a60-395c-a7a7-a74c5e5e0bd2 | -20.87729 | -49.33616 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab7622e5-bebf-3327-82e5-2a90c21b0da1 | -20.64671 | -48.69221 | 2025-09-13 05:01:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35ba840b-b504-3b8b-97de-256822f70c97 | -17.14499 | -53.89405 | 2025-09-13 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab659cb9-91b8-3f9d-90ba-885b349c0710 | -22.66086 | -53.12009 | 2025-09-13 05:01:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 37e66ccd-3cbf-3b9f-8996-41399236ca69 | -16.53206 | -51.73766 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5bf61e4-5f0b-3693-bd2a-5967eb9a1e6e | -18.14696 | -48.45835 | 2025-09-13 05:01:00 | NOAA-21 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c7ba8da-c379-3b87-8600-508926457ca0 | -17.95996 | -46.93603 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f5ba5f7-0da3-3201-b67e-4f7b6bbe0831 | -21.57988 | -48.42229 | 2025-09-13 05:01:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 18668f5a-5aad-313c-8e66-d8099f86dfd4 | -20.73259 | -56.74101 | 2025-09-13 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08d754b7-24ba-3501-af50-40ac500d345e | -16.3574 | -51.54497 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b93e910e-9a16-3923-a52c-62a0229ee917 | -18.8585 | -46.83402 | 2025-09-13 05:01:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e8728127-6fad-3a2a-8a42-3e333d39487f | -21.06786 | -46.1433 | 2025-09-13 05:01:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 38a13298-1ea0-3c50-a0e1-eacf789ad60a | -20.28779 | -46.59029 | 2025-09-13 05:01:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0014907-1997-3088-b81b-490ce7b14c36 | -17.28143 | -46.11208 | 2025-09-13 05:01:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a1237dd0-62f7-360b-89c6-e16d13492430 | -22.60727 | -46.42409 | 2025-09-13 05:01:00 | NOAA-21 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 3abfa106-4e6b-356a-be23-9ebc2501952f | -17.28373 | -47.23769 | 2025-09-13 05:01:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1fc58d99-b9c4-3af7-a660-e88894572963 | -17.42518 | -49.25831 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 350aa78c-9432-33fa-838f-23602f9cdf3b | -18.15269 | -49.19351 | 2025-09-13 05:01:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 81042f63-00c1-3240-b3b5-878a41027bcd | -16.35838 | -51.50565 | 2025-09-13 05:01:00 | NOAA-21 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb453fc1-7bc9-3981-be8c-0a3bd1bf4972 | -20.08008 | -46.91198 | 2025-09-13 05:01:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9c953e27-1264-3cfb-878d-81256d34fd89 | -17.67793 | -47.8651 | 2025-09-13 05:01:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10a4c271-7c55-325c-973a-7f40be969e33 | -16.50446 | -55.15534 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| de223f1d-39b1-32a5-8fef-4005cfc432ce | -17.14558 | -53.88985 | 2025-09-13 05:01:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9a60751-32d3-3cdf-a6e5-752f6cea2b09 | -19.26042 | -51.43219 | 2025-09-13 05:01:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 057a3707-fac5-3352-83d2-eeca5dc06303 | -17.31531 | -48.74184 | 2025-09-13 05:01:00 | NOAA-21 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 629d406b-63a7-3e6e-b1e0-60ceb1487124 | -17.37364 | -52.90996 | 2025-09-13 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d91dfc6b-cd50-3975-984a-509b4b6ebd7e | -16.49824 | -55.12727 | 2025-09-13 05:01:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7c9ec134-59e4-36c5-baf3-204e0e44038b | -16.52599 | -51.78487 | 2025-09-13 05:01:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 257f3a71-9e28-3de7-bc92-41d8976638bb | -17.42169 | -49.24699 | 2025-09-13 05:01:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fecd6d5-71a4-375c-b1e9-b8ef2575a97e | -19.65395 | -45.86501 | 2025-09-13 05:01:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c32e89a0-483b-34bb-981d-64b4a72af330 | -18.00979 | -46.94295 | 2025-09-13 05:01:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d055cea2-ce4b-3d5d-9523-a398d8b10184 | -22.54382 | -47.36983 | 2025-09-13 05:01:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fafca7b8-ecee-3e29-ade7-5ea4bcd7d6c9 | -21.6181 | -46.81531 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| d28ad74d-4167-30d1-8b1d-f2622502d487 | -17.55157 | -44.55195 | 2025-09-13 05:01:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2fe4448-bb6a-3659-b648-02bb5b33463d | -20.44799 | -46.4395 | 2025-09-13 05:01:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README99.md)
