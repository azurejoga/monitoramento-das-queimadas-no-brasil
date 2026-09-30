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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26b25254-c680-3ba3-b1b8-33a62cedfd94 | -4.54369 | -50.77711 | 2026-09-30 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c82b6ab-18a3-3913-8fa8-396b140905d2 | -2.64724 | -47.34488 | 2026-09-30 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12051452-33fa-3a97-84e5-920a2fdfa92e | -6.16752 | -44.61903 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8729d1cf-dc80-38cc-b575-5c23dae419ad | -3.22731 | -46.94159 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a83e1a57-d835-3926-a242-ef5a9a21da5c | -4.12374 | -46.87542 | 2026-09-30 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 01d39935-39d6-305d-9460-c77fee0096dc | -1.49467 | -48.91417 | 2026-09-30 04:32:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ffb6bb30-0d1c-3c67-bc61-5ccc25a81ac3 | -9.66286 | -45.12593 | 2026-09-30 04:32:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41c4ad17-a4a6-37e2-bef2-5ab2e19ccad2 | -6.18702 | -44.85705 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3facca32-a1d2-36fd-a4d1-248efc608e70 | -7.4794 | -45.78883 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0c15847-2701-3fe3-8b42-3b3d0dd1e77b | -3.1821 | -51.24285 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d4e0afaa-b446-3198-87ad-e1fe558c7906 | -7.47548 | -45.79183 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f27ad344-c9c8-3cfe-acdc-3264d72f9e5b | -2.82492 | -46.70594 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de5011cb-8d0c-389d-9749-0b3ffb1e483a | -5.73441 | -45.17093 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5c26fdb2-8176-335b-bebe-c8b7e0e2c8f3 | -3.03726 | -48.41076 | 2026-09-30 04:32:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2e7cae7-7d87-3e2e-bf95-4bebb360fc5f | -5.79241 | -43.76451 | 2026-09-30 04:32:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbd30135-124c-3366-8992-e320526b950d | -3.016 | -53.87436 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 657c3f60-55ff-3553-a397-3dc430fbd50f | -5.41062 | -45.90339 | 2026-09-30 04:32:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99075388-404b-3702-b47a-e6ad9dbd56ce | -9.28331 | -46.41238 | 2026-09-30 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78e90ca3-5a38-3b11-bcba-ad74236d5907 | -4.81367 | -46.85122 | 2026-09-30 04:32:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ddf950c-c6ab-3cca-9736-5fdf4c4b7ded | -5.73887 | -45.16444 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ba96323-865b-3aa1-b1d5-d4e057889b1e | -3.18655 | -51.24187 | 2026-09-30 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 24bbc0df-52b8-35b4-bb2f-0ad89979f582 | -5.73831 | -45.16795 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5d8927bc-f8b8-3859-846f-4bbd7357972e | -3.3779 | -50.94537 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 69c0a418-3f45-3075-be33-54686b1127fa | -3.38092 | -50.95578 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a470281d-1866-37d1-9f53-f4300221bb17 | -9.31278 | -46.25224 | 2026-09-30 04:32:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a62a2964-bf0d-364f-84b2-551ef3ed85c9 | -3.25165 | -50.80886 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 85b5a6cb-cf4e-340a-b97a-b1b87466c6ac | -6.20177 | -44.1223 | 2026-09-30 04:32:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29bf91af-7cdf-32b9-8998-ad79ba138967 | -3.23658 | -46.93773 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 3a7f4bd7-2032-39ca-97d9-f0cbe81512b9 | -5.33606 | -46.19154 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e5814cd-e5f9-3434-9228-60353fd659e1 | -3.42887 | -50.43528 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 246a59a5-846f-32f2-924f-55545f0b65dc | -3.23298 | -46.93715 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 8913c5ef-b64e-32f5-ba89-35a42f539688 | -7.51379 | -45.09016 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53cac9e7-3387-3fcc-a442-a050386583e5 | -3.37605 | -50.84318 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 605cc34d-16df-3e2f-aefc-4fce2c50e6d9 | -5.13284 | -56.02053 | 2026-09-30 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ac6a3ae-393e-368a-b661-3b5d9dfa3d9d | -1.68749 | -47.72158 | 2026-09-30 04:32:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e12cc8a9-a1a1-3fe0-9dd0-d2e6098fdfc0 | -6.20864 | -42.51686 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 93ab0f68-8277-3176-9840-0bea94361db2 | -3.23451 | -46.94278 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 29c0ec78-3b75-342f-a12f-994ed298db7b | -7.83757 | -45.81756 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 17904f3c-c3dd-3df3-b785-69656cd4080c | -3.23582 | -46.93457 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9df40b3d-6f5e-3d46-8b50-ef9c0b624288 | -5.33949 | -46.1921 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da22d746-4616-347d-a0e0-8e3789dc21a1 | -2.90288 | -54.08883 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a10e0058-575a-3de1-a111-385fb5c334d0 | -6.7089 | -45.63244 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d200680-d50d-39dc-8d12-696f5e4fc1bc | -3.011 | -54.22354 | 2026-09-30 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc173ed1-c1db-3da1-8e68-02a2dd0b8bdd | -6.65856 | -43.86006 | 2026-09-30 04:32:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4120ee4a-aa86-356d-bf56-1ea56460b2fe | -6.13742 | -53.05953 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bf3ea91-cb0f-3e8f-9489-e5d6d8ebb439 | -7.08044 | -41.7522 | 2026-09-30 04:32:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ace6754a-1689-3bec-8f59-f4032d1b3a8a | -2.64167 | -49.2709 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1e2c491-e802-3db8-a257-e914f012502f | -2.90232 | -54.08984 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2c83016-08db-308f-aac8-bab09b5e6e20 | -8.98471 | -44.17916 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f12ba570-1819-3da2-bebf-dba2f033392f | -4.30487 | -48.61259 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10e97222-2033-3a75-b6f3-7fd93e353c41 | -3.35983 | -50.46441 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf7375dc-1e1f-3710-bd23-255b121dbae8 | -6.38109 | -55.13737 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e74e059-954d-3680-a59d-c49488d6c851 | -7.34033 | -46.08841 | 2026-09-30 04:32:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 84f1bb59-2a86-3e72-bf1d-f45e1364c72b | -3.23456 | -46.95001 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9fd9baad-b2a2-347d-ac00-f03a68aaaa95 | -6.70498 | -45.63544 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb187566-c482-3b9b-bc8b-6640fb70cb74 | -7.82974 | -45.82358 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e3ff3335-39d1-3e0c-800f-e946180ce58d | -2.26894 | -47.86785 | 2026-09-30 04:32:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a158724e-6ba1-3750-b002-da986ab60d56 | -3.25099 | -50.11631 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd6fdaba-d62c-3839-8a8f-1e9b6af37fe0 | -5.73051 | -45.1739 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eab316a4-c7d6-3982-827b-a834ab758953 | -8.84004 | -49.70963 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7daafb01-03fa-39fa-93f3-71890aad4520 | -5.70306 | -44.73017 | 2026-09-30 04:32:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 91bbfdcc-f771-3bf3-aeb7-f317d5e8ddec | -5.03389 | -43.57365 | 2026-09-30 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54a2f258-59c7-3a9b-88d2-309c810dc87f | -7.83644 | -45.82466 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c2997fc2-f117-342c-b9f9-712eb4137c69 | -7.82753 | -45.81596 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 217086dd-c1c0-3680-9d06-626c8381a011 | -5.75779 | -45.17467 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 079377fc-8102-31d4-9061-6f377735e987 | -3.25063 | -50.12152 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf9121b3-3de3-3405-b067-c02354a40307 | -7.82639 | -45.82305 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5dd5acf7-3be3-33f8-980f-e11e4bf3fb15 | -3.565 | -50.25591 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8076bb5e-c706-3f07-a198-ae7480b4a4b2 | -8.55766 | -47.78765 | 2026-09-30 04:32:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63c1038d-b4be-3b1e-b15b-6196bbe9c374 | -4.31416 | -48.62925 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 8aca1788-1d20-3f57-a8e3-80a95c49da95 | -7.92829 | -47.37687 | 2026-09-30 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87513f4a-2ea7-31b4-8fa8-b1498164ebaa | -7.07057 | -44.36241 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cde8ac27-a79b-3b85-b06b-58af9d6254f9 | -4.03048 | -54.19867 | 2026-09-30 04:32:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bf6531d-4e84-3471-95a2-3381ab8a5196 | -3.103 | -50.28318 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21a96ef6-5ba7-3a28-948e-d0bf2beec2e1 | -6.142 | -53.06341 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bef270d-d621-334c-a16c-cedf377d36aa | -6.38037 | -55.14146 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 125d21c8-0d84-37da-9491-896bcdc4d8f9 | -5.74173 | -45.06097 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d60f722-4016-3b61-8681-07683e50d51b | -5.74777 | -45.17307 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 781412f2-5fc5-37c3-b608-fb2799d0894e | -3.24378 | -46.93889 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 04b1b9dd-31f5-338b-a11e-f78d8945e3f4 | -3.25131 | -50.11732 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1cf9f32-aec5-3996-9e7b-a5459a8aae97 | -7.20259 | -40.11975 | 2026-09-30 04:32:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 287e9534-c912-309f-a93e-0e6d5a93afc9 | -9.10322 | -47.17312 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e2f7ea5-70ce-3455-bb5c-c9da7733544d | -5.74499 | -45.16903 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6ae764bc-8b64-3c13-aee6-0b46030e244d | -3.3591 | -50.46878 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0c6ab05-f5ee-32bc-b20e-07cee78ab825 | -6.22848 | -47.44502 | 2026-09-30 04:32:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4a0f1c4-5b2a-3cea-9e36-323edd23b232 | -3.23523 | -46.94593 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b22eb7c5-7c05-3ddf-9eba-9ae50381e50a | -4.29153 | -48.6205 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d9d2e78-fbfa-3b7d-8bb8-b628905ba15a | -4.81241 | -49.46149 | 2026-09-30 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a90fece7-d29a-3b74-8eb2-915e2f87b5c7 | -6.7887 | -55.81725 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3c8d2ca-dd37-33df-9ca2-185735c64f57 | -3.24957 | -50.1247 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d1bfb8d-8d27-3893-8098-d2238ce10d24 | -6.72166 | -45.65992 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9be9f395-6bc0-307a-8666-163a820c2932 | -2.97788 | -51.05399 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 70ca7878-ee23-304c-a035-a88a2c1dfca3 | -7.00859 | -45.30616 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c84c5d1d-0266-3842-88eb-d43d0c3aa6b6 | -4.3267 | -48.62616 | 2026-09-30 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffee3f94-7f68-3fa6-a419-05fe0af79e6a | -7.01637 | -45.30025 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccc784f0-22a9-3f9b-9fed-5d95977db05e | -6.72414 | -45.58052 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b613a26c-dc0f-364b-8576-dbf507762618 | -6.13313 | -53.29634 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dd8bb099-acde-3cfa-93af-44e651db675f | -10.18619 | -39.66452 | 2026-09-30 04:32:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 26be0431-2fbb-35b2-b4a2-b73a60ad4fba | -4.11892 | -48.82415 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 03bffe93-47b4-3914-a896-4e4aa80135f7 | -8.33525 | -44.16147 | 2026-09-30 04:32:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
