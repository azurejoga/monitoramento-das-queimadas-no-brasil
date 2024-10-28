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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8c0f770-ba34-37ee-8065-19546ca6be2d | -5.26709 | -46.2095 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8e870e3-1d69-3b5b-a5b3-8d0d5db017ca | -5.2641 | -46.25188 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27f5ab2f-d49c-38a4-8752-a10e84dceaa0 | -5.2595 | -46.25475 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82a64119-c2f2-3580-87d4-6e32017aa71f | -5.22483 | -46.23077 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 594af528-ea82-3dea-9acc-f3bf4bd4a9da | -5.18478 | -46.19933 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e1185e7-dd77-33f9-b104-64f812468408 | -5.18418 | -46.20294 | 2024-10-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3a656da-9bdf-34e0-a56b-48d6fa945ea3 | -6.38296 | -46.44711 | 2024-10-28 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b421b10-85af-3ac1-9e56-8eb54e6a17c0 | -6.33675 | -46.33196 | 2024-10-28 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3197da25-bdf4-36b8-b827-0e21afa35a9a | -6.18679 | -46.57591 | 2024-10-28 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8c19a78-05a5-3ba3-a9f6-b3283531e3a9 | -6.18619 | -46.57943 | 2024-10-28 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9615997b-b0d7-374a-b110-103a78311744 | -6.18215 | -46.57877 | 2024-10-28 04:06:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a57cccca-359a-3a33-8f1d-67e2dbe48f37 | -6.11819 | -46.36387 | 2024-10-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4195e35d-0d52-3520-842f-2a74a4b78837 | -7.89537 | -45.42312 | 2024-10-28 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92e2714e-8d18-3255-bc68-617e44a5afa4 | -7.80499 | -45.58656 | 2024-10-28 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25643bbf-39db-3ea5-beac-a45f98c8a26d | -7.18478 | -45.48586 | 2024-10-28 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42a83eb1-32d9-3c41-b6fb-11be7d68cce6 | -7.12774 | -46.03514 | 2024-10-28 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e2c904-ba0c-353e-a8a7-289363726d60 | -7.09593 | -45.29514 | 2024-10-28 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 368b73f4-9833-329d-b554-daeec0a07dee | -6.53675 | -46.00208 | 2024-10-28 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 026e87bd-a38f-3947-b5e6-8ffd09d1f37b | -7.589 | -46.85427 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e540a9c-815d-39d1-8f29-3582f38a0e30 | -7.51374 | -46.63154 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b66be89-4d07-35f8-97b0-0c5bb7d6e2dd | -7.51287 | -46.63667 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8814da1-c234-3d7c-945a-6352dc569b62 | -7.46708 | -46.71349 | 2024-10-28 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c74b729e-9322-35f5-bed8-82a1f90fc724 | -6.95553 | -46.31454 | 2024-10-28 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 832d1d74-bc16-376a-9a4d-2fc215af9cc8 | -6.95161 | -46.31386 | 2024-10-28 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139ef66b-0dc2-3858-acb5-629c8f88cd3f | -6.93997 | -46.21424 | 2024-10-28 04:06:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 787dae13-3f84-36ab-ad0b-e911c2551587 | -6.72242 | -46.31351 | 2024-10-28 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 504519ba-d1d1-35f5-a635-3b8cdedeead0 | -8.99774 | -46.75656 | 2024-10-28 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da291173-30ca-3eb7-9d66-502869e53e58 | -8.99689 | -46.76151 | 2024-10-28 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df96e540-48aa-3f23-b14a-9e78a3b789b9 | -8.99383 | -46.75587 | 2024-10-28 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47df548a-a346-3478-871e-ed8e6f122214 | -8.99298 | -46.76083 | 2024-10-28 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9b99d15-3a34-3e53-8645-273aa7937796 | -8.98992 | -46.7552 | 2024-10-28 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9ad12c5-c9d8-3c77-a5a3-d4d7573029e8 | -7.95534 | -46.542 | 2024-10-28 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 702e71ab-bc7c-3849-955a-c8def2637507 | -7.95141 | -46.54133 | 2024-10-28 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49c6f5d2-5e96-370d-a3c5-332ee97d7ad3 | -9.73988 | -46.27633 | 2024-10-28 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da74ce22-5ddb-32eb-9b25-d6daefa7176d | -9.73535 | -46.28026 | 2024-10-28 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1687e577-5933-3ceb-8f12-d93793cc9536 | -9.73236 | -46.27503 | 2024-10-28 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0570b8c0-2cb7-3c10-8745-5edaa28c4423 | -9.67379 | -46.2533 | 2024-10-28 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e169a995-ff88-3999-a23f-4bf0134eaa64 | -9.67303 | -46.25785 | 2024-10-28 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c9506cd0-1761-357f-9c74-078f1a211b8c | -4.77281 | -46.39413 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b4aabb3d-fef0-3c2d-a3a5-44c6c180103e | -4.77221 | -46.39786 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ee6d51e-3930-3552-b675-de6b95281ada | -4.7716 | -46.40165 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08633945-77c8-3d07-aaa3-e46663556935 | -4.76872 | -46.39357 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7e42f088-28f2-3966-bc6f-7c7af8ae0289 | -4.76812 | -46.39726 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| feb11111-cf0b-3d62-a278-59eaf1510259 | -4.76751 | -46.40102 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8d97be82-e3f2-3e96-bbb1-e5071d23adce | -4.76462 | -46.39301 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| da68ce7d-0058-3402-b5bc-37f3dfecbe34 | -4.76403 | -46.39667 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ab55bf4d-d741-3cda-846e-3f8c0c24086b | -4.76342 | -46.40041 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 9ff35fa7-9063-38df-bca8-d5e0433a1976 | -4.53501 | -46.39396 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c061c86-5c1f-3abb-915c-95f0557fde7f | -4.53441 | -46.39765 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5846b84d-77d5-3eeb-8592-c89dccfa370c | -4.51949 | -46.46318 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f35e043-57ba-3cb3-a2ed-cf21542f09b7 | -4.51539 | -46.46243 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c32e013-80e6-3729-81d0-fffda5a106e0 | -4.40446 | -46.32457 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16e8476d-0d9d-3fa2-b2b0-1f5ee164795e | -4.18162 | -46.38572 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c1a169c5-d189-36dc-a5f4-5d367b2265df | -4.18101 | -46.38944 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4caa2a8f-385c-3e71-a13a-feaf2fe52340 | -4.17752 | -46.38499 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec228a36-ce7a-39be-9680-4e69155d5362 | -4.13279 | -46.40879 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6829706b-35b6-3353-9271-891c5fe55c09 | -4.05648 | -46.26162 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 043dd026-fce2-340c-8973-e1da11ab202e | -4.05599 | -46.26013 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cca60929-987a-3319-a463-ac4cf8cd08a7 | -4.05538 | -46.26382 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5a97413-8e21-3bab-a0aa-2894129c42f5 | -4.0524 | -46.26095 | 2024-10-28 04:06:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29a1a04f-da43-32d3-8da5-8fc3373590fd | -3.99137 | -46.48287 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 81f29717-d720-32e6-8f27-7a01805d8a79 | -3.99076 | -46.48663 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dd36a9b1-23da-35da-a893-2fbbf28a296b | -3.98781 | -46.47852 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcacdc59-b925-33ee-b0c7-500ace035000 | -3.9872 | -46.48227 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8a68479c-76e5-3ead-9bd8-aee938aee29a | -3.98659 | -46.48605 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 146352ed-0ef6-3240-82ee-1dc793e8ec6d | -5.06529 | -46.78851 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0356fbe7-a2e4-36da-9628-f74b6de5dfa0 | -5.01251 | -46.48241 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 621bdd1f-ce8c-35c4-b49f-382a3b70a2f8 | -5.00844 | -46.48171 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57040e15-38a2-3b83-af90-3aa1f1f7e1db | -5.00781 | -46.48544 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26d9cc70-3a65-3eba-9ed8-9d63f81b247f | -4.96458 | -46.4967 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa601bcb-bc55-32b4-b4a0-2b0ac412f496 | -4.9605 | -46.49592 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb753d6-b795-3752-b63b-0335547f707f | -4.90076 | -46.86123 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7184418b-c2a3-3178-9641-bf939762c06b | -4.90011 | -46.8652 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ceb9e32-8a75-30f8-a2f7-5ac7d5ced70d | -4.88394 | -46.85867 | 2024-10-28 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea97b449-e1e8-34a5-9898-cd1c50a7ae3e | -4.74161 | -46.8039 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5018c678-6dd2-3ef7-8d5f-7f0269637dd8 | -4.73807 | -46.79932 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e960fce6-b26b-3c27-97dc-1db194590c9d | -4.73741 | -46.80327 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c772688e-bb28-374c-aa49-bafb02b34004 | -4.73677 | -46.80705 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e19f5be2-46d0-3923-abcd-21a928d7f33f | -4.73321 | -46.80259 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b82e41ec-3de9-36de-8a5a-bfc208dda6b8 | -4.67784 | -46.66396 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c135bef8-63a9-3bb4-9c6a-7f3b9764345f | -4.67493 | -46.65578 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 88c6d4e3-0fbf-35d7-9c26-9cacf6098ff3 | -4.67431 | -46.6595 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 313f9360-8101-30c2-971f-cbf4a55d81c9 | -4.67369 | -46.66325 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ae5ccc08-13c6-3926-8ad8-7822350297a3 | -4.65699 | -46.66094 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c701b252-db7a-36c2-a47d-3199767eef57 | -4.61533 | -46.69748 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92d17a6-aea3-3695-b35f-d554ba8dabd2 | -4.61115 | -46.69687 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79e4b90e-09ab-33d4-a578-92925f97f2ca | -4.54472 | -46.6076 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bc2b09ba-6698-39aa-a80b-b29a3496068c | -4.54407 | -46.61145 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4233de03-4a08-3cb1-880e-daebb1fea735 | -4.54259 | -46.60852 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6c45a96a-7060-3d89-9e50-4d95b99ae1ca | -4.54197 | -46.61238 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ea829111-0cab-3b14-85bb-3c64c927de61 | -4.54055 | -46.60704 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 07411fa1-8436-3efb-b3d4-b8d80961158a | -4.5399 | -46.6109 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f42a5516-1bd9-3b32-8ffc-01daf657c338 | -4.4298 | -46.61032 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1949c675-3204-3391-988e-950cd4fcb5f2 | -4.4273 | -46.60915 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0abfa5ec-cc4b-335a-912c-3236b3dce008 | -4.42668 | -46.61285 | 2024-10-28 04:06:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f55528f-43a6-30d8-873a-cea1c85e693c | -4.23857 | -46.88172 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59ea5423-fedb-3dce-b1df-2884df86c96c | -4.23566 | -46.87283 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 10eac727-422c-362b-b964-7c034ca0c0ef | -4.23499 | -46.87695 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3ec12be6-ade0-3f7a-be9b-6b7ef9cabc57 | -4.23433 | -46.881 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 503726d2-b639-3d64-98fb-8713b0002e81 | -4.23141 | -46.87221 | 2024-10-28 04:06:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README42.md)
