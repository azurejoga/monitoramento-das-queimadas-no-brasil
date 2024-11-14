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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78864a85-1799-32f9-9302-918c8fbb0714 | -2.35772 | -51.98116 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd83e686-54ab-3ff6-a2b2-35001dd47f7b | -3.14899 | -45.2808 | 2024-11-14 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75c01317-4450-3efc-af34-08c8286b8f9d | -2.51371 | -46.38922 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dbfe2f7b-9ea8-36fc-b7fa-27ba00ec4f5a | -1.85538 | -47.82759 | 2024-11-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38fe501e-a082-310e-af53-1338279c8ec1 | -5.56663 | -45.365 | 2024-11-14 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8efa226d-e298-3fa6-a76b-412954628132 | -1.33501 | -48.32918 | 2024-11-14 04:40:00 | NOAA-21 | MARITUBA | PARÁ | Brasil | 1504422 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ae2192e-d9fd-3d9b-ae1f-92b6935c3047 | -6.96046 | -39.82821 | 2024-11-14 04:40:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0b5d021-2edd-3e04-9d3e-a69e2a9ada5f | -4.46976 | -46.53333 | 2024-11-14 04:40:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b50f3a7d-2f91-3e2d-8dd5-59a3aed5eb18 | -5.02865 | -46.83777 | 2024-11-14 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 808c1a9f-2f09-3f6b-8a02-38230a2b683e | -6.95996 | -39.83186 | 2024-11-14 04:40:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1470ff73-df59-3d20-8a8e-2cfb33cbebd0 | -3.56301 | -51.45095 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53e08b55-b00e-331c-9f41-186af0a99478 | -3.02238 | -48.04435 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a1c8ba-20f6-3e7c-831a-036b7dac9377 | -1.37087 | -47.09028 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e156a76-7810-3b70-bd1a-bb00561e3c48 | -2.1578 | -53.63181 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 279bd498-d1b9-33b7-b534-8e1826d18038 | -3.23348 | -50.67209 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a369a86e-8226-360b-9658-5907760f950f | -2.53551 | -47.47617 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94bb86bb-a090-3ddf-8292-9b00088ad11d | -4.05119 | -48.31778 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e84dd2b2-7bf2-3840-a58c-4aeea8134e49 | -2.67143 | -46.82139 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39b2ccdb-1c20-3111-b90d-ae0c5adf6ad1 | -2.23498 | -46.44126 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc070119-572d-309b-affc-5eae6706ce18 | -3.25641 | -50.79189 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4b72054-83f8-3c87-a4b3-14e4a0bcf863 | -4.00487 | -48.85569 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1af893d1-0678-3197-a36d-828bcedb4d16 | -1.62009 | -52.51282 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe033fe9-48fa-3316-9eee-5f195a9e8ccf | -1.44836 | -52.25063 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c273ac4-dbdc-3585-8e0a-d041ffc1d68d | -2.66003 | -46.80439 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb9e8982-f3f6-363c-86c6-1ffa0dd56764 | -1.39813 | -51.12957 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b44eb961-8c54-37d6-bc0e-425f1f6d04a1 | -4.21286 | -50.49995 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9af4bb7-7e73-37a9-8cc7-620f7e983c12 | -3.42738 | -50.30753 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74b8a36a-352d-38f8-ac0c-9b6d831381ca | -2.41033 | -48.47963 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 320975ae-4f0d-344a-9374-de34212b4ee5 | -2.95195 | -48.01583 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f2c1182-4e01-378c-8fd4-d1035efbcdb4 | -4.29409 | -46.87679 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bedc2e7-9391-3ae4-9845-d8673991dfcf | -2.1199 | -50.697 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad66b139-5d0b-30b9-a191-6ac4587ff78e | -3.40665 | -50.37372 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9580196d-a34a-3923-9d6b-a2bacee774bb | -2.30082 | -49.1164 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8f6b21b-cc0b-3b5e-89f2-7a017abba8eb | -2.50251 | -47.46748 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5da6ec28-f8f5-3e98-b94d-e04ef69b5f15 | -2.37423 | -46.49674 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 704a3fe5-788a-315b-98bb-5be4312ad923 | -2.24426 | -53.74538 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7223846f-f1df-3884-b02f-8a7b4cfd0e2e | -2.59415 | -48.19464 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af9ac334-f9fb-3097-8c71-cbeca0c795f4 | -1.21525 | -51.78177 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4e13631-b6a7-3165-9c75-c421c41436dd | -1.34953 | -51.43516 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e1d408-34b1-3f02-a9cd-b5a5777fd8b0 | -5.02923 | -46.83395 | 2024-11-14 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e31acad4-52c8-3eb7-a1c8-647abfa371f1 | -4.93075 | -45.44811 | 2024-11-14 04:40:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc31b137-c1d6-37e6-bf9c-af82cc05d4c4 | -2.64263 | -46.16551 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7c1ff3f-a37e-3fd2-96ef-9b03231e9b10 | -2.17239 | -50.51995 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6fd4e23-8a84-3009-89a3-d6282284de17 | -2.64345 | -46.82094 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07acd08c-721a-3ab8-9baa-e158d8bbdd09 | -3.80077 | -44.76691 | 2024-11-14 04:40:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e170e84c-3f5e-320d-b44b-ff12e02948ff | -3.77349 | -51.03012 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ba24bd95-6d6c-3b1e-8e47-52fae1e8626b | -3.74842 | -50.45258 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 983503e0-fb09-3a19-ac2c-55904ca6f7f1 | -1.66876 | -47.80257 | 2024-11-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 911f4620-88f1-31c5-b679-8948a18e310c | -3.17326 | -50.45163 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbfc3589-1d93-36f1-a22f-74282394640a | -3.86487 | -47.09018 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ae78841-9d96-3839-8995-acc65dcbc72b | -1.51676 | -51.55124 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e555235c-fcec-3dd4-9a14-53705df1ba10 | -1.21263 | -51.75129 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db54782d-2c42-3f21-9d90-44d0ff9df548 | -4.04401 | -45.71975 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ebd06701-8348-39e8-836b-58735e57bd8d | -2.6381 | -49.52695 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85468769-6cad-3fc9-8c82-c6e64ba58c01 | -5.15606 | -48.18602 | 2024-11-14 04:40:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e8e71b6-aaa2-34ae-95b9-2ea044560478 | -2.02578 | -46.50308 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc39b00f-354c-3dee-b6ff-0f1afbaead02 | -2.34484 | -48.59608 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6112c87e-5cc2-3eef-9751-33579f47308a | -4.37585 | -50.80087 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a50284b7-b871-3291-9b0c-d8d640145ed6 | -1.23043 | -51.77983 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2621c300-5bc8-348d-ba8f-c2aac1fa5e3e | -2.63473 | -49.50513 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d7b33b77-312b-362e-827e-6348a42534d4 | -3.04817 | -50.33617 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c95d6368-571d-383d-b625-a2f42527b219 | -4.00313 | -45.56823 | 2024-11-14 04:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f107fb8b-491b-389e-b7e7-7d8f79d0d1d4 | -1.63554 | -53.27019 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 9291f14f-4807-3e45-8231-333aab462247 | -1.32951 | -52.45921 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06d22b43-d8ce-371c-8722-1a7bb29928bd | -2.67292 | -46.99173 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f2e49a8d-5b46-3bb6-a4ba-df04fe2a45de | -1.25352 | -51.77477 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c3f6ac-caf6-3437-a2ec-ffb06b7fc58d | -1.39586 | -51.12122 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beac35ed-815f-38fa-8ac2-d645bd232e47 | -4.41529 | -48.60173 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7d50afb-34e1-3392-b475-c3f0d84dc3de | -4.26467 | -48.19014 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99c9974b-99aa-36c7-b4c6-c1383213813a | -4.05387 | -47.22913 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e29ebcf8-c43e-34ec-86b1-8b57cd22be65 | -1.38263 | -51.57338 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9b01948-9a33-327f-9c11-07f044f16b9e | -4.26039 | -47.07323 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dc3ba49-bc32-38e6-b738-f763825ff7ba | -2.14596 | -48.80046 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bed2046-7313-3d08-b4ea-449c085490b3 | -11.78785 | -47.06862 | 2024-11-14 04:42:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35851fc8-9a8a-392b-977b-1877c2f9b156 | -10.56098 | -47.59094 | 2024-11-14 04:42:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 978b6889-3f7f-3d53-bb57-b1bcbed56535 | -9.16346 | -50.54259 | 2024-11-14 04:42:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8697a838-e07b-3bf0-90c3-2ffbdb876053 | -11.78555 | -47.07026 | 2024-11-14 04:42:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fd4606fa-46e6-389e-9b27-40935fd099ef | -10.55741 | -47.59036 | 2024-11-14 04:42:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acb7088c-47a3-39b2-8457-4f525f1629ba | -9.16401 | -50.53911 | 2024-11-14 04:42:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9b60d842-7dcc-3002-9a13-75f750f7629d | -11.78618 | -47.06569 | 2024-11-14 04:42:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6b07d428-daae-3a84-9221-4d3ca190ff18 | -15.93434 | -59.27498 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9105144-60cc-3d78-8ce8-c52c3a70fc46 | -17.61714 | -57.54307 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 325629ec-86e8-33be-b29c-4766f973ce6f | -17.61703 | -57.54773 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| eabeffb0-30d6-3213-91dc-4c290a83b387 | -17.27311 | -57.4749 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1571bcf3-0808-3c4b-88d3-f2f69123a0e4 | -16.01024 | -59.39677 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d6b9d78-88ee-3d50-b359-fc5fd8d1ad51 | -17.25299 | -57.47095 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| ff5a9d61-c147-3fca-a0d6-a9c2af933a17 | -17.7081 | -57.5505 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ac885981-9adc-3083-a3a7-709b76929f9a | -17.25231 | -57.47462 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 00c15144-5091-32ec-92b9-8c893be20410 | -17.5909 | -57.41314 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c09f8a90-389c-35c0-87c0-1cdf5e5dad4f | -15.89458 | -59.28196 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5be88d4-342a-347e-901a-f0083e1fd2a3 | -18.01957 | -54.22198 | 2024-11-14 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8112c31f-e9d6-3fd2-b69d-292477cdd8f7 | -17.59166 | -57.49999 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 0a383107-944f-3e34-aa7b-c4ead42fd2e1 | -17.26037 | -57.4762 | 2024-11-14 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 523cf69b-aef4-3f5b-ae20-acc72688ed55 | -16.241 | -58.93156 | 2024-11-14 04:44:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a145f6bd-a6d4-3030-89ba-8b78d433dd55 | -20.47883 | -53.67494 | 2024-11-14 04:44:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 537e92f1-d515-3c28-b3cd-c72196b8ea67 | -17.61301 | -57.54694 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| dfb23a00-9a2d-3878-b287-c98e530444ba | -17.21244 | -57.23011 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aef14417-22a4-3951-baa7-38d15df79433 | -15.87309 | -59.29355 | 2024-11-14 04:44:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 4b1c03a7-65cd-3432-b0b4-d163404923b4 | -17.6331 | -57.5509 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 33bb507c-5156-361b-80e3-43c0214d7a6d | -17.59571 | -57.54644 | 2024-11-14 04:44:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |


[Clique aqui para ver as próximas entradas](README38.md)
