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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ede6fddc-97c0-378b-bea9-77dde6a92111 | -16.0933 | -50.20681 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c60c2e1b-9e4d-3d5c-a73c-f82087840d89 | -16.09075 | -50.21823 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 74831134-2c62-3afb-a70a-6e5ef08314cd | -16.09065 | -50.18822 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c35ce89e-ef03-3b25-bdc2-057ca6c76e37 | -16.09023 | -50.19246 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 60e18609-b9da-3e9a-b886-9e720395f5b2 | -16.08965 | -50.1927 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8384ba7c-1cad-327f-a3e3-9a38aefb100c | -16.08794 | -50.20304 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b67128f2-96b9-3fa7-b530-49da27b4b899 | -16.08727 | -50.20337 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e46e8635-0969-34b3-ba35-2d2587036d37 | -16.08671 | -50.20874 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef684f56-4e59-3f04-8144-4d38fb6c429b | -16.08601 | -50.20903 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73adec7f-e1ff-3d35-b6c6-64b0b2d80a0e | -16.07532 | -50.19867 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c02525ac-dcbb-38c9-a58a-b86e06d687ac | -16.07008 | -50.1916 | 2024-10-08 03:45:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d2c84c02-c683-33cd-b963-05a34abac55a | -16.06933 | -50.19258 | 2024-10-08 03:45:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0197fa49-d9fb-319f-a023-2e534b649726 | -16.06822 | -50.2002 | 2024-10-08 03:45:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8e508f8-99e5-37f5-9dd9-e90e3ec2e584 | -16.06727 | -50.20178 | 2024-10-08 03:45:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d7acc89-bbe4-3097-b4c4-30bbd4dbf7b7 | -17.58322 | -50.47084 | 2024-10-08 03:45:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| de2cc2ed-8969-3365-be1b-0e188c1d2eea | -17.58202 | -50.47617 | 2024-10-08 03:45:00 | NOAA-20 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dcd7bb4b-2406-3b9a-9235-516682bff0bf | -19.7165 | -50.38388 | 2024-10-08 03:45:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 00cad55e-5c91-39cb-910d-a6914c723102 | -19.70938 | -50.38694 | 2024-10-08 03:45:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d0cd7699-ac65-3e05-8fd2-a0f99c095eae | -19.71541 | -50.38869 | 2024-10-08 03:45:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0d48822b-15a4-354e-94da-be23f6e58f35 | -20.988 | -50.10321 | 2024-10-08 03:45:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e119f297-3bec-352d-960b-3ea1c781897b | -20.98627 | -50.10128 | 2024-10-08 03:45:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ffbe5c9b-d9d4-35f4-a84f-a392d291324b | -20.98521 | -50.10583 | 2024-10-08 03:45:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 470480b5-3e17-3ba5-92c6-a2a039b67cd8 | -20.98223 | -50.10136 | 2024-10-08 03:45:00 | NOAA-20 | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eece92c3-65ea-3ccd-af9a-2aabc80048f5 | -19.71487 | -50.38755 | 2024-10-08 03:45:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ebca6657-0eb1-30b6-863c-9e6370528e85 | -19.71599 | -50.38274 | 2024-10-08 03:45:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| df9c2c8c-401d-389a-8f62-aac8486f1974 | -19.71044 | -50.38224 | 2024-10-08 03:45:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2bab75ce-fa3f-3101-aaf1-8306ef2c28e8 | -16.64584 | -50.60581 | 2024-10-08 03:45:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3db43a28-59e4-3c12-b42c-8626de5bea66 | -16.64457 | -50.61142 | 2024-10-08 03:45:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d537edc-5d60-3789-8240-eb934761d2de | -16.64139 | -50.60425 | 2024-10-08 03:45:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea809145-5967-35fe-a423-00241fc5f7f2 | -16.64012 | -50.61003 | 2024-10-08 03:45:00 | NOAA-20 | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 969357b5-50ad-33cb-80d7-5e8ff5fd613f | -17.36131 | -52.00601 | 2024-10-08 03:45:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 87105bae-31e5-31a7-9bd9-938ce343bfda | -17.35976 | -52.01266 | 2024-10-08 03:45:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9afcbfed-3eba-3a6a-be7a-652ea285f2a1 | -17.35921 | -52.00463 | 2024-10-08 03:45:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0cd7729-8f1f-34fe-a00c-f623bccd92d8 | -17.35765 | -52.01114 | 2024-10-08 03:45:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 58bdc0b8-371c-3f14-8543-08b5a0bdc29d | -16.81267 | -51.2586 | 2024-10-08 03:45:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb236c6b-241a-3333-955c-07a0ba9662e8 | -16.80587 | -51.25722 | 2024-10-08 03:45:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5797a79-06c6-3692-a88f-c9f98d257f90 | -18.54911 | -52.65549 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a10d1a9-ef15-33c3-ac85-3f4e7243db55 | -18.5491 | -52.63905 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 01fcfe71-64ea-33f3-b4e9-453bf97bec0d | -18.54734 | -52.64625 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dbd84e98-59bf-3a2c-9cf2-537208d62684 | -18.54564 | -52.65326 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0de6d874-8af5-399b-9458-fc70a8d1af8d | -18.54551 | -52.63922 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d8953f47-5f75-3c6f-aea2-6ac0731fae7f | -18.54384 | -52.64626 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5bb88f0d-5bfb-31c0-8765-dfd9ef5900b6 | -18.54215 | -52.63691 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 935d5caf-9ac4-394c-8e92-dfd065eb53eb | -18.54043 | -52.64396 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 75676a7c-0b58-3d0f-852e-0c1eef47adbe | -18.53865 | -52.63667 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f9f60dcb-b0e9-3180-9dea-94ac73e365b5 | -18.53696 | -52.6438 | 2024-10-08 03:45:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ccce6565-67c4-37b9-8d3e-4195659484c4 | -20.4277 | -47.66286 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 81667ada-4a9b-3880-9d2a-aaf4721a4d56 | -20.42699 | -47.66616 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1e4b799-1d95-33af-81b0-b21f206ac78d | -20.42629 | -47.66941 | 2024-10-08 03:45:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 94fa8d93-d908-3185-b178-b55c60168aaa | -20.42628 | -47.64455 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f187944-c7f5-333b-8ef3-132fd06bfed6 | -20.42612 | -47.66131 | 2024-10-08 03:45:00 | NOAA-20 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce5fdb0a-b4bb-3751-ae70-ed351c7a7542 | -19.82644 | -43.79766 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f91d5996-9a9f-339e-9a74-92b511cbcd24 | -19.82413 | -43.85481 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 869807d0-1b49-3f90-b534-f8e7a140f284 | -19.8287 | -43.78571 | 2024-10-08 03:45:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04c8fefd-c801-3708-b77f-900ed705fe0f | -17.66521 | -41.14293 | 2024-10-08 03:45:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9893dbaa-ffa4-3d4a-805d-7b0e6cc2d31b | -17.666 | -41.13844 | 2024-10-08 03:45:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2aeeeaca-6833-3aa4-b22c-2fad1e7f87fd | -19.42896 | -41.15659 | 2024-10-08 03:45:00 | NOAA-20 | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c6d84761-1757-3ec0-aa99-9d7d9b6916b3 | -19.4254 | -41.15596 | 2024-10-08 03:45:00 | NOAA-20 | ITUETA | MINAS GERAIS | Brasil | 3134103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d64469ff-bef4-3e8c-8be2-b85bb69b439c | -19.10973 | -41.30385 | 2024-10-08 03:45:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| acc4102b-f524-3bc8-8e52-59fae727ac77 | -20.31795 | -41.98076 | 2024-10-08 03:45:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ab7cdbc2-48eb-362e-890d-5b05a769817e | -20.46141 | -41.97649 | 2024-10-08 03:45:00 | NOAA-20 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 605f8028-9b56-39bc-b146-946898f8166e | -22.3048 | -41.88084 | 2024-10-08 03:45:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9e3dc27e-c522-34c0-b433-7640c99be307 | -22.30333 | -41.8832 | 2024-10-08 03:45:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d3101a1-6b33-3abd-a408-3ae683f9e68f | -21.96439 | -41.51733 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c44f4314-e7b7-3227-ad38-ec0cde6457be | -21.93247 | -41.55443 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 70456085-961d-3e1b-9936-b077d7126353 | -21.90228 | -42.35419 | 2024-10-08 03:45:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24f20498-c114-3e33-8bfe-90a37b66da46 | -21.31609 | -41.40009 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| aa535967-67cd-356d-b843-2ca201334c7c | -21.31329 | -41.39531 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1bfd5cc5-0b25-361a-aa68-8b5cff11f1be | -21.31255 | -41.39953 | 2024-10-08 03:45:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2f37b155-2952-389d-93ae-0f0370c7d2bf | -21.16313 | -42.198 | 2024-10-08 03:45:00 | NOAA-20 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 21e1bb1e-6280-37dd-bbab-b4dc2d564c24 | -21.16305 | -42.19571 | 2024-10-08 03:45:00 | NOAA-20 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| eeb34b09-f2db-3806-ad17-f84111909ce0 | -21.16223 | -42.20026 | 2024-10-08 03:45:00 | NOAA-20 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 0ecda98f-0248-36a0-9fa7-b641d03534f4 | -22.59744 | -42.21412 | 2024-10-08 03:45:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79256990-c28c-34e6-a408-d876f0448db5 | -16.30055 | -42.04837 | 2024-10-08 03:45:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f79f64fa-4a08-33d2-b7c7-0d983eec93ca | -18.06112 | -42.11064 | 2024-10-08 03:45:00 | NOAA-20 | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 873c3db5-6b68-3aa3-96b7-779e1660cfb7 | -18.81001 | -42.98976 | 2024-10-08 03:45:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 39e3217e-5a7f-3999-b880-758bc2d8bf45 | -18.56364 | -42.41169 | 2024-10-08 03:45:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b0de884c-e181-3902-a425-e91168480941 | -18.56072 | -42.40594 | 2024-10-08 03:45:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 9a615395-6fc7-333d-82fa-d7653e7b1082 | -18.81099 | -42.98438 | 2024-10-08 03:45:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e9d6f7f7-76c7-36ea-9075-f0ee513727a9 | -19.1342 | -42.71843 | 2024-10-08 03:45:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 09882943-27f3-32c0-8b7d-12e172a68607 | -18.9374 | -43.14816 | 2024-10-08 03:45:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0dbe570d-f4c2-3c63-b9eb-5b1ced95a18b | -18.55983 | -42.41089 | 2024-10-08 03:45:00 | NOAA-20 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cb7fa5f1-b1d0-3800-bfae-90e5e1bb6065 | -19.13721 | -42.72383 | 2024-10-08 03:45:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9c8ca440-2862-33da-86c7-8024e40c117a | -19.13331 | -42.72327 | 2024-10-08 03:45:00 | NOAA-20 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c4813103-8d68-31cf-b5c2-8dd40568b8e9 | -18.63497 | -42.77559 | 2024-10-08 03:45:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bbcbbbf1-8f6b-3f80-99e8-373a88dff9a6 | -20.41768 | -43.55555 | 2024-10-08 03:45:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eb80c787-1125-3303-83a7-de274bee0fb2 | -20.41374 | -43.55464 | 2024-10-08 03:45:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d09060b-b33c-3c35-a6e7-4244aee2b109 | -19.76322 | -41.99286 | 2024-10-08 03:45:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a43fcf2f-f249-3a61-8295-ac326bcbd592 | -20.21914 | -42.903 | 2024-10-08 03:45:00 | NOAA-20 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b48f70f9-af1e-32ab-a464-8ae0cab63dba | -19.88981 | -42.63433 | 2024-10-08 03:45:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 73643382-0157-3629-80dc-4040174e2627 | -20.6918 | -43.29948 | 2024-10-08 03:45:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 988d9eed-fd09-3c9e-92fb-2566de84def9 | -19.89651 | -42.64072 | 2024-10-08 03:45:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85368046-82c0-3a56-b781-137bed4b313f | -19.89271 | -42.63995 | 2024-10-08 03:45:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c33d94f2-63c7-3ea4-bfdf-da87b5ff64a8 | -19.83094 | -42.38143 | 2024-10-08 03:45:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5735338f-f85a-381e-b8c2-6589bdef18cc | -19.8974 | -42.63588 | 2024-10-08 03:45:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f324c649-c2e3-3c10-b801-74e36bc67b88 | -19.8496 | -42.38558 | 2024-10-08 03:45:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 349047dc-98a2-34b6-9308-a8769aae9359 | -19.82247 | -42.36182 | 2024-10-08 03:45:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e32e45b5-95dc-3af9-824e-45778635efb7 | -19.97353 | -42.45433 | 2024-10-08 03:45:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c26db2ce-feed-33c9-9086-df947646250e | -19.96977 | -42.45358 | 2024-10-08 03:45:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 9a4a0003-5292-3f93-b1c4-e7a7202ba34c | -19.77273 | -42.00356 | 2024-10-08 03:45:00 | NOAA-20 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |


[Clique aqui para ver as próximas entradas](README39.md)
