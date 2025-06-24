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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9da4801-9982-317b-ba9c-73dacce54b1c | -10.58647 | -49.64868 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be3e2b82-4b57-3c3d-af2d-146fcaaf48d5 | -13.27836 | -46.81611 | 2025-06-24 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0701c63-d61f-3666-b313-dfd6530fcc9f | -8.58859 | -51.58489 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 040a0cfb-3c62-3a1e-a333-16f5cb36c012 | -12.24948 | -46.68887 | 2025-06-24 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1265259f-abb0-3029-b7f0-f54f2ac2615c | -10.06186 | -49.66309 | 2025-06-24 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1dd9f745-5902-3ca7-a257-c64ef91d82b8 | -8.56743 | -51.55751 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 0de89cab-8e65-371f-baf6-a5e4d4cf2522 | -11.56636 | -47.91766 | 2025-06-24 04:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 497184cb-1d3d-3ea3-a207-b452b173b563 | -14.51657 | -40.36267 | 2025-06-24 04:04:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dcfd38aa-7f3e-31df-9f8e-0a114e6cb266 | -9.64872 | -48.56771 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9da734b7-d0ff-3294-88d1-c709b6a4aea0 | -11.93945 | -48.42952 | 2025-06-24 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb91fd8e-5523-30d7-b509-b556afcb78f9 | -10.5951 | -49.46017 | 2025-06-24 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d677472-b93c-3cbe-a95b-65fc6c347eb6 | -13.55412 | -44.0956 | 2025-06-24 04:04:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ebbd726-0dca-3658-a46e-e63fe2b80246 | -14.43534 | -48.91534 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| aa2ef73c-c4af-3368-9bf8-5ceee6dc090b | -9.64509 | -48.56975 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8f17a70-4a0a-346b-9fa7-d6718d99ce28 | -8.71573 | -47.85493 | 2025-06-24 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5adc168b-a0f0-38df-ac35-003657825660 | -14.43989 | -48.91634 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c568b558-88d7-3f9c-a859-57c20b38e714 | -12.25182 | -46.68582 | 2025-06-24 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4adb142-893f-30fb-b2f1-9f99c050dad8 | -11.65448 | -46.86402 | 2025-06-24 04:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| baab6289-6745-3cce-9ce0-94f277baa9d4 | -14.6658 | -41.91257 | 2025-06-24 04:04:00 | NPP-375D | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b028e7f2-b9d1-33c7-b932-38b789599334 | -10.58819 | -49.6394 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66d2abc0-7011-3639-9b78-d4b303c2c8a7 | -10.58762 | -49.64249 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b1b75e8-a890-3353-93af-7604904ab209 | -10.25062 | -47.67698 | 2025-06-24 04:04:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b7c42da-046c-3f86-8b02-422df2de94e2 | -13.73431 | -47.74332 | 2025-06-24 04:04:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cc46485-3b59-3cdc-8dea-a97f46fbd96b | -8.58177 | -51.58789 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 234c5aa0-1280-3df6-89c3-a8cfbd83b169 | -13.54661 | -42.47793 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| acb14b08-0400-3a7c-b1db-6465e814953c | -9.39672 | -48.43444 | 2025-06-24 04:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68ba7ecf-339e-364a-a79f-98c9fc6a2661 | -10.28122 | -47.61107 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 117035c0-44e8-302b-bee2-e1550d925c64 | -8.58259 | -51.58358 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aa448785-ce12-3c19-8868-1a2097e4a56b | -12.28881 | -48.80647 | 2025-06-24 04:04:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| be6e63a6-b2bd-37ff-894a-138103ddd2fa | -11.37192 | -43.74943 | 2025-06-24 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1e4d8b5e-1c68-38f8-880d-ac2b9a7f7d90 | -14.38465 | -46.13529 | 2025-06-24 04:04:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe758903-cc5d-326a-b1e9-32c204461e0e | -11.57225 | -47.43241 | 2025-06-24 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 023a9475-3f3e-3ffa-a6ed-5fe03d5571c9 | -11.28226 | -52.46696 | 2025-06-24 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 820b2c14-6e7c-3ed8-a745-1596dcee93b5 | -7.45148 | -45.56652 | 2025-06-24 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7f81a45-b5ce-3cb5-8886-12fd6d81393a | -8.57223 | -51.57237 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 55e9171c-286e-35cd-98ce-beab1ea3d757 | -12.79928 | -48.7332 | 2025-06-24 04:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7bbe477-6c05-3540-afe0-8652e33f2a1e | -7.86067 | -46.66066 | 2025-06-24 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a81cb14-d36f-3abb-a21b-13bbe9b83b94 | -13.27426 | -46.81549 | 2025-06-24 04:04:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61f632ef-4785-395b-9fc5-73c0a61dfe8e | -11.09869 | -46.64655 | 2025-06-24 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a7968ae-e217-3ae5-9dd8-ed7c80f1e78f | -13.07243 | -48.82874 | 2025-06-24 04:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 354489ae-f947-3307-b450-a54887f1ff38 | -8.87078 | -47.27416 | 2025-06-24 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53b8e223-ce18-39ac-a96e-ae0b5dbb167d | -11.33285 | -41.99447 | 2025-06-24 04:04:00 | NPP-375D | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8e0c0d63-dd56-3291-a66f-5b4540835761 | -10.58705 | -49.64558 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8322d875-4f46-37e0-b2bc-b63249476b9b | -8.56058 | -51.56086 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6fa86cf7-6fbf-356a-840b-a97ba65dd4ed | -13.54879 | -42.4857 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 443ccf97-6ec3-37d4-b2ed-1dff0beeaff1 | -10.58133 | -49.6477 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4b4a9a3b-575f-30a5-8e67-dd5cdf50b95e | -12.2903 | -48.80339 | 2025-06-24 04:04:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6d68f520-6510-3e9c-abff-2bdcb1a66cb5 | -12.25016 | -46.68512 | 2025-06-24 04:04:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83f6b0da-b170-3d88-bb7f-1c9e72ed867a | -8.98875 | -49.86911 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5f1d072-4a72-354f-a4c3-bca2f1c7df1f | -10.22817 | -47.45886 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c3c5e0d-0c2f-3e85-8497-8377f7e74b59 | -13.07147 | -48.83381 | 2025-06-24 04:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bc1c7b21-99d0-3a17-8dd9-4226a2d2f06f | -12.2841 | -48.80552 | 2025-06-24 04:04:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f149db80-4514-3a56-9e26-581d313fdcc5 | -12.80394 | -48.73405 | 2025-06-24 04:04:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b7fc782-82ba-31ac-868f-69eaa2356d6f | -7.85622 | -47.11633 | 2025-06-24 04:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f768f1b5-e254-3b1c-b90a-bf905d262267 | -7.48004 | -45.58618 | 2025-06-24 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3565509c-17a7-3731-a3df-df1fa452b752 | -7.47591 | -45.58551 | 2025-06-24 04:04:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d0dbb96-8cdf-3857-9e83-01f9f9a35a2a | -7.43336 | -45.42315 | 2025-06-24 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e0b43e8-1d05-3706-b4eb-b12455da2060 | -12.30595 | -40.37597 | 2025-06-24 04:04:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 51c6dcee-30c3-3867-8408-a5f002c0acac | -14.4354 | -48.91816 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3f12e9a3-7e79-3f9f-a125-f07bd93f6551 | -13.76698 | -44.10099 | 2025-06-24 04:04:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2bd8cb3-e618-35ef-8cda-10ac0b09166d | -12.75612 | -44.4093 | 2025-06-24 04:04:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d7c831a5-a39b-315f-839c-49ce098a597a | -8.06189 | -43.11212 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| a367333b-5ce9-36fd-a0e0-613ba05c4452 | -8.86706 | -47.26878 | 2025-06-24 04:04:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abfefdf3-2901-32b9-9681-9b76049ee08f | -10.95065 | -48.14716 | 2025-06-24 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d566a85-07bd-31a6-923f-e7020d6938e0 | -13.07707 | -48.82973 | 2025-06-24 04:04:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3956c1b5-6ca1-32b8-a646-78e968d84a23 | -10.2804 | -47.61564 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 437adf7d-9af8-307c-aa38-768ce4a86ec1 | -14.5143 | -40.35471 | 2025-06-24 04:04:00 | NPP-375D | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2b843f9-21fb-3087-987c-581dda207721 | -8.2454 | -44.95896 | 2025-06-24 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ed5ab445-6afa-3d13-ac9c-93fa3f7fc4f2 | -13.54938 | -42.4821 | 2025-06-24 04:04:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83432a09-478a-328b-9cbc-8934015f5741 | -7.90814 | -49.64545 | 2025-06-24 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08c0e044-71a8-3781-96d7-985bec0a08a7 | -11.28122 | -52.4704 | 2025-06-24 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43b0a6bd-084d-3afa-b260-82576bccc119 | -13.23942 | -49.83711 | 2025-06-24 04:04:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb1773ce-9814-3388-b979-b85142e82648 | -14.66385 | -46.94376 | 2025-06-24 04:04:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00504423-8d0e-3154-aa78-dda87778b52f | -11.27622 | -52.46554 | 2025-06-24 04:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64e2e097-50bc-3134-b786-49acda6ee173 | -14.19295 | -42.77872 | 2025-06-24 04:04:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6a08931e-e85e-3528-ae53-2fdc93a41e42 | -11.56813 | -47.42963 | 2025-06-24 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38659e4a-5197-3348-aed9-8dead4c721e4 | -8.57574 | -51.58677 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a91a626-c2e4-3abc-b73f-643fde3f2c0b | -8.98811 | -49.87252 | 2025-06-24 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79df823f-1117-3383-8d55-753f9ffef4d0 | -8.06124 | -43.11615 | 2025-06-24 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 572df083-fc3d-3c7b-8901-4ed9a7a50f1a | -8.56275 | -51.55664 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6bb40582-85a9-3522-b407-2e6667c12ccc | -10.59397 | -49.46619 | 2025-06-24 04:04:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2cc3ee16-ae7c-3783-ae94-800657afa928 | -8.56962 | -51.55336 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e039c861-9043-3322-ab15-b5ead3f180c1 | -14.24602 | -43.7552 | 2025-06-24 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57cbf738-a953-38fc-827a-5c3aabe597a0 | -7.87275 | -47.87826 | 2025-06-24 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98a17c37-cfd2-3aee-87e9-5030aeb660b2 | -11.09381 | -46.64983 | 2025-06-24 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c33acc01-0e60-3880-8d3a-6b1dd848bd54 | -11.939 | -48.42169 | 2025-06-24 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7ed314a-8b9a-36d6-a9b2-bc2f9e9ed323 | -8.56877 | -51.55777 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09035ef2-3ff5-35c7-98c9-80660d673a25 | -13.2553 | -41.33075 | 2025-06-24 04:04:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 016b257d-fd91-3d36-9d38-e4886088e4c4 | -10.58248 | -49.64151 | 2025-06-24 04:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2509049a-a50c-38a8-8ec9-506541931ec2 | -8.56968 | -51.58577 | 2025-06-24 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dc97a81-8a69-3613-9afd-5d8afd1b922c | -13.95022 | -45.05058 | 2025-06-24 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35f3280b-968d-3f24-9a86-c4381d8765cc | -14.43896 | -48.92118 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eba8c272-0081-388b-a8ae-f05f461de02b | -9.28924 | -40.46199 | 2025-06-24 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32bb87d9-9c0f-39f1-bd67-38675e60a63c | -10.65143 | -44.4962 | 2025-06-24 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a9353496-ff7b-3c41-bbd6-fc01a21e3706 | -11.60697 | -47.61465 | 2025-06-24 04:04:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3890e90b-db1c-3a9e-bc10-dee5b67c13d9 | -13.25474 | -41.3343 | 2025-06-24 04:04:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 544a3d73-e61e-3713-95da-65de65075eae | -14.43996 | -48.91917 | 2025-06-24 04:04:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f96cd9f5-6270-3282-88c9-d1d151e45dd9 | -7.91353 | -49.64645 | 2025-06-24 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a058c215-8f99-3813-b9f0-00af4a041b98 | -7.3134 | -45.77344 | 2025-06-24 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13c533b7-172b-3e1b-bbea-4ebfd43db014 | -8.24932 | -44.95964 | 2025-06-24 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README9.md)
