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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ca86736-3e92-3f61-a36d-a329921d1496 | -5.50487 | -38.93691 | 2025-01-22 03:29:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7e530a5e-5edd-3a0e-8b72-0a2c98355601 | -6.15988 | -39.43444 | 2025-01-22 03:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0baf9abe-c8e7-3170-aa1a-05c6fe2390eb | -4.51109 | -38.27361 | 2025-01-22 03:29:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f44c608e-df0f-3c5c-8c3b-14529319a0cf | -9.01622 | -35.44276 | 2025-01-22 03:29:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| ff083c5f-5d1a-3751-920f-018ae426d279 | -4.51556 | -38.27438 | 2025-01-22 03:29:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c6e2d340-c0e5-36e6-829a-fa5a6137f113 | -9.01688 | -35.43877 | 2025-01-22 03:29:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b4dd5cdc-724c-3c61-b24e-4021c9ddd6cb | -5.9505 | -39.68438 | 2025-01-22 03:29:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56103f2d-c926-37f3-a710-b0b8194281cf | -6.15519 | -39.43351 | 2025-01-22 03:29:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4d3a47d3-d8b6-3d5a-9ced-d4122158ae85 | -9.02042 | -35.43934 | 2025-01-22 03:29:00 | NPP-375D | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4ce83cb9-3999-39ae-89ba-2820c439d76f | -5.9113 | -35.72928 | 2025-01-22 03:29:00 | NPP-375D | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 70363f31-da2a-3223-ba4a-1a046174699f | -12.75353 | -42.36854 | 2025-01-22 03:32:00 | NPP-375D | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df1b422a-c045-3b7b-9feb-5e2a7345fd59 | -13.81882 | -41.73221 | 2025-01-22 03:32:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 02702cc6-37cd-3f48-8b25-726c7912b66b | -12.94965 | -41.18163 | 2025-01-22 03:32:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 004e94e8-de7a-3db6-babb-43f5d1ee4855 | -11.03395 | -45.05051 | 2025-01-22 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a61022d9-19ac-3264-935a-11dcf38961cd | -11.02358 | -45.05502 | 2025-01-22 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4318bedc-85c2-38a7-829f-504fe4d56ef6 | -11.23046 | -40.37657 | 2025-01-22 03:32:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d775c62c-4b69-36d5-853e-4d6a9b241e73 | -11.0642 | -38.43806 | 2025-01-22 03:32:00 | NPP-375D | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4639fcb2-0653-3f34-ae0b-08f22e340f2b | -11.13867 | -40.61736 | 2025-01-22 03:32:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a6e6330-336b-3f31-9d6c-9c786772cd46 | -11.02678 | -45.0539 | 2025-01-22 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05eae164-6181-3a41-90a4-40c041b372e9 | -12.34761 | -38.19615 | 2025-01-22 03:32:00 | NPP-375D | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ec703354-a0cf-35f0-bd07-ee39e37a2286 | -11.03171 | -45.04662 | 2025-01-22 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d1e97a56-1b50-3c75-aa2d-b5e36f247567 | -10.69635 | -37.04942 | 2025-01-22 03:32:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ff90c995-01c9-3cda-8c97-b697ff823652 | -15.55712 | -42.64595 | 2025-01-22 03:32:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 06a14c4f-7cc1-3494-9309-8f95a9425d07 | -11.03074 | -45.05161 | 2025-01-22 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97efbf58-bc3d-353c-b699-de9b9ecfe13f | -10.71099 | -36.98611 | 2025-01-22 03:32:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c791b7e2-68c1-32b9-993c-6f64add2bfbc | -11.23601 | -40.37214 | 2025-01-22 03:32:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5522564a-d3ea-3a5f-b1c8-d144edd07a35 | -11.88612 | -40.95656 | 2025-01-22 03:32:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dade4f7e-e2a9-3cb1-ab80-87761f58a976 | -9.6359 | -37.9883 | 2025-01-22 03:32:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| acfb42a4-0a49-30a3-8693-cca8ecb9d8ca | -12.95012 | -41.18357 | 2025-01-22 03:32:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4c107461-ffdd-331c-a613-204df6cb9ac5 | -12.02901 | -41.32854 | 2025-01-22 03:32:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45e56f22-c08c-3322-afef-0c00d3ce5f0e | -16.75954 | -41.0535 | 2025-01-22 03:32:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 25e2d7f0-dd6b-3079-bed0-9a85dc51b150 | -12.02418 | -41.32756 | 2025-01-22 03:32:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9575ed2d-97bb-3429-bc2a-5fec09269cb1 | -10.71177 | -36.98153 | 2025-01-22 03:32:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c0040fe2-fdcc-3f9a-993d-b3b43cb63675 | -11.23508 | -40.37736 | 2025-01-22 03:32:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 04910d1e-1be0-3d17-a6bd-01fa7e12327c | -11.03495 | -45.04557 | 2025-01-22 03:32:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 92529edb-b1d1-3385-9238-1077efe1f9e3 | -15.87647 | -38.98835 | 2025-01-22 03:32:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 82440bbe-f552-3b1c-a1a8-0ed011ebfc48 | -18.57455 | -42.29151 | 2025-01-22 03:34:00 | NPP-375D | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 237e3716-6fa8-3f10-949c-116ff0acd56c | -16.34982 | -43.69661 | 2025-01-22 03:34:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 420a8c91-8da5-3004-b587-629888aa03ca | -18.60802 | -40.2562 | 2025-01-22 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b93c6e1a-6a46-351a-a25e-fa86f976c1e5 | -18.92797 | -41.93526 | 2025-01-22 03:34:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fd22453b-c671-3291-9832-c04a38cad9ce | -21.10762 | -47.76781 | 2025-01-22 03:34:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6447ef6-8ac7-3e19-abf9-1b92dc1fcf1f | -21.11365 | -47.76954 | 2025-01-22 03:34:00 | NPP-375D | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f5f8d63-4928-3ef3-93a3-59c4572e12b6 | -18.61204 | -40.25702 | 2025-01-22 03:34:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ca73eca8-007f-341c-880a-0113af0b8c6b | -23.4719 | -46.2835 | 2025-01-22 03:34:00 | NPP-375D | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9db3e476-e5c4-3687-8475-5dad9148977c | -27.87867 | -51.15381 | 2025-01-22 03:36:00 | NPP-375D | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0ab8bf00-90e5-314f-9ecd-8e0889ac79c8 | -27.7333 | -49.93875 | 2025-01-22 03:36:00 | NPP-375D | BOCAINA DO SUL | SANTA CATARINA | Brasil | 4202438 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 60b19f48-72b6-3f9e-b00b-ecfc1218d6ad | -27.8723 | -51.15215 | 2025-01-22 03:36:00 | NPP-375D | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 591cb95b-5288-3ad6-aee9-c5caa8eaa07e | -27.46649 | -50.7695 | 2025-01-22 03:36:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c30960ae-a2d4-35ba-a1f7-ccb7bab459a4 | -27.73962 | -50.56461 | 2025-01-22 03:36:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 57caac8a-b55d-379f-a3c2-b3d51560b664 | -27.74582 | -50.56622 | 2025-01-22 03:36:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8fefb36-52b7-3d62-8071-29b9ad214e45 | -27.8728 | -51.15347 | 2025-01-22 03:36:00 | NPP-375D | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8d1de098-1a65-369e-b663-b618d3266a21 | -27.47276 | -50.77129 | 2025-01-22 03:36:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e8fda9cd-df3f-3191-81ae-ecdcfcadbd9c | -27.87917 | -51.15518 | 2025-01-22 03:36:00 | NPP-375D | PINHAL DA SERRA | RIO GRANDE DO SUL | Brasil | 4314464 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5f86328a-f127-3ebb-ab56-390bf94bab39 | -5.3599 | -45.17842 | 2025-01-22 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d7dc74f8-20ee-3f9b-a95f-67f9162834cb | -12.18671 | -41.3583 | 2025-01-22 03:53:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c2925332-95a2-3919-a06b-c9e6c0fa4dc0 | -11.02555 | -45.05437 | 2025-01-22 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f3309d3-ae3d-3384-8209-d4dd7c70f362 | -5.84228 | -37.48019 | 2025-01-22 03:53:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c0380b29-14d4-3625-9812-afbafc688d70 | -11.23768 | -40.37323 | 2025-01-22 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd8f453e-6b5e-3d3a-b809-981175d9ff3b | -11.13768 | -40.61777 | 2025-01-22 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4b9183d7-48fa-3d1c-8906-37459f23d7ba | -10.70924 | -36.98424 | 2025-01-22 03:53:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 669984e8-ff33-39b2-a96b-420df1f26812 | -5.91146 | -48.08086 | 2025-01-22 03:53:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 165122c9-fb7e-33e6-a1f1-3ef8e40298bc | -11.21178 | -37.73122 | 2025-01-22 03:53:00 | NOAA-20 | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a383b688-c292-3e08-9425-987ecb214ffe | -11.0393 | -45.04919 | 2025-01-22 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 019f032a-604e-3986-bc96-6c6da3f55e78 | -11.942 | -39.65977 | 2025-01-22 03:53:00 | NOAA-20 | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47dcf97e-4ac5-3e58-965d-7ccc121783e0 | -13.04625 | -41.44415 | 2025-01-22 03:53:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 16330c36-df18-36d3-97f7-92e5aa3bb9b3 | -11.0345 | -45.0522 | 2025-01-22 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9ae9af9-ca8f-3bd9-b208-8235c325c614 | -2.93017 | -39.93522 | 2025-01-22 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 32961990-fb66-3587-8cec-301700f5351d | -7.22217 | -35.7839 | 2025-01-22 03:53:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c08c6f1-fff0-3bb2-8e9d-f2223d74c48d | -11.54803 | -37.79713 | 2025-01-22 03:53:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fe3d5e1-d039-3e42-98ed-8ee33bea3780 | -11.03516 | -45.04837 | 2025-01-22 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 68a9a7bd-8c21-3617-bbd9-87b055e285e6 | -5.20688 | -43.30358 | 2025-01-22 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8622dfd4-dcc8-3763-89db-15ec92c41e50 | -6.80248 | -35.18686 | 2025-01-22 03:53:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a769b94-dee4-3086-bb52-f044035e3aee | -4.51134 | -38.27721 | 2025-01-22 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 860a3488-c877-3dd2-9e79-de80ef20fb7c | -5.50064 | -38.93832 | 2025-01-22 03:53:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3b948514-ea7e-31f9-ae2e-19d41f57a627 | -11.03036 | -45.05136 | 2025-01-22 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db599940-fa58-38b6-aed5-c42210d18a33 | -12.75344 | -42.36845 | 2025-01-22 03:53:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 391ad20c-1056-33a2-a1f8-bace97838f05 | -4.51188 | -38.27377 | 2025-01-22 03:53:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ca3fb7e1-e947-3c38-b9f8-dd46ee67e037 | -11.2983 | -38.057 | 2025-01-22 03:53:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 720febbb-e4f2-3b9f-91d0-e4762fa16fc4 | -7.53494 | -37.55236 | 2025-01-22 03:53:00 | NOAA-20 | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e8a541fd-95a6-3192-acc7-9837b676cb6d | -5.38145 | -36.81949 | 2025-01-22 03:53:00 | NOAA-20 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23aab26c-51f6-3805-ab78-02b483692d48 | -5.70505 | -45.84645 | 2025-01-22 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b652e5b0-7d9f-32e8-bacf-bf4182bd1524 | -3.24364 | -48.07843 | 2025-01-22 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6597e6ac-1842-38eb-a233-ab9af1eea84d | -6.07691 | -35.40358 | 2025-01-22 03:53:00 | NOAA-20 | MONTE ALEGRE | RIO GRANDE DO NORTE | Brasil | 2407807 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9dd8b153-44a8-3831-83f1-aeb05c3c1163 | -5.91086 | -35.73036 | 2025-01-22 03:53:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 87c962f7-f158-3686-958c-b92f59def674 | -11.59738 | -38.09521 | 2025-01-22 03:53:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7f19afbd-5ba7-334f-840f-954b217fb831 | -11.23377 | -40.37629 | 2025-01-22 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 37fa24f7-f6d8-3aa6-ada8-c8289a5d07ba | -5.50397 | -38.93885 | 2025-01-22 03:53:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc9c2db2-9226-3edf-be64-7472af45dbc5 | -7.22246 | -35.78503 | 2025-01-22 03:53:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d2f0327-fd20-3877-8eba-02c85d725443 | -5.70517 | -45.84344 | 2025-01-22 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c3b0a70-4f2a-3737-9d7c-7d1b19edf272 | -11.03103 | -45.0475 | 2025-01-22 03:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 338239a8-f787-3071-be60-137a3d6f850a | -11.2371 | -40.37683 | 2025-01-22 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6cb580b3-25ef-3ca5-bed4-d8e075e85f01 | -5.70426 | -45.84864 | 2025-01-22 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0a4bd66-17f6-3210-aab0-8ed37a31d8ca | -11.22986 | -40.37933 | 2025-01-22 03:53:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 10f6be7b-ba33-3e4c-b505-73dce72a427c | -12.02717 | -41.3275 | 2025-01-22 03:53:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6be373f0-a095-325e-805e-35c5d79d6186 | -12.34855 | -38.19506 | 2025-01-22 03:53:00 | NOAA-20 | POJUCA | BAHIA | Brasil | 2925204 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8733dba7-9ab4-337d-a767-bb24e614fe85 | -12.13951 | -40.34313 | 2025-01-22 03:53:00 | NOAA-20 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e73ed00-8cd0-380f-ad6c-ee02d9163bda | -3.24431 | -48.07438 | 2025-01-22 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1dfea12a-4fb9-3734-a18e-ce7030382133 | -12.94858 | -41.18385 | 2025-01-22 03:53:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a74ff93e-9b59-30ae-b33e-e3f29010abe6 | -2.92669 | -39.93467 | 2025-01-22 03:53:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ae2463a8-5507-3a3a-b065-17c3c28e83e2 | -12.94917 | -41.18021 | 2025-01-22 03:53:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
