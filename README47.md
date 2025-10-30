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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20e4feb7-3acb-329c-916d-1d31fff3a29b | -7.62178 | -47.80542 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c525286-dbda-35cd-8920-31a537dbfd0e | -4.76354 | -46.85157 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f43abc7f-1ba6-3518-9e4c-62f930cf58e9 | -6.97277 | -47.31855 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea1a1608-76f2-3aee-ab74-69ab96e5b67d | -7.95963 | -46.73209 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00caa1fe-e0f9-3c99-8f42-04ea0868280d | -7.62669 | -43.58961 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b7dcb86-4b66-3330-8790-1d257453840f | -7.38992 | -43.64992 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa6592ec-292f-36a9-af8f-2c8f02b1f9ab | -6.13442 | -41.68172 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5dd03991-a3d2-34ac-b718-0f1de901cd26 | -9.90944 | -47.91148 | 2025-10-30 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab51070d-33cc-3424-95c0-bc938baf7e20 | -6.14839 | -41.85518 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e2a45bd9-b086-37a4-a111-6dfb24e7aa5f | -5.59558 | -42.77729 | 2025-10-30 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b369ab5c-e01e-351b-bf9e-49b20e56ab1b | -10.88053 | -50.08961 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef1c3a80-6dc2-3acf-8ca2-aa1c2d8442f1 | -7.61483 | -43.59602 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ff7eccbe-548a-3c9a-8709-d58ce034365a | -7.95797 | -46.72116 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46db9bbd-d5ad-3a82-949e-ed63ae67715a | -7.79701 | -48.30426 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5147f6bc-4d5f-3b92-aeec-25c078c33807 | -7.51069 | -46.26324 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f10fcbc1-bb95-39cb-8582-86e1038cd488 | -8.65051 | -44.802 | 2025-10-30 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 607f7d7e-38ea-359a-b81d-4a4c794da56e | -7.81039 | -46.41013 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b3ae948-de24-3719-a4d2-3cabff1b7865 | -6.13868 | -41.70686 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2c090894-d5b2-3ac6-b2f8-ac7702e25089 | -8.02265 | -42.51213 | 2025-10-30 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c924472e-92eb-3fbe-a15e-14663f13ddb0 | -7.92773 | -46.8052 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db3bd31a-c804-3df4-b23b-3ab33fbbf45a | -4.98807 | -45.51783 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75dc9fc3-4cef-3440-943f-c019d975bed4 | -7.12307 | -47.01548 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95f7ed27-fcac-36a6-954c-e33e1f73734b | -6.14007 | -41.71419 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b18c084-46f3-3671-a7e3-047121dabc5b | -11.84477 | -47.92308 | 2025-10-30 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 115008d2-051a-39f0-813f-abab94f0f5c0 | -6.15436 | -41.59922 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 98d070af-d091-33bb-abc5-527dbb2be945 | -10.85367 | -47.87305 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09bfbea1-201c-351c-9136-a7a444277d4b | -5.69972 | -43.15956 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 06aeeeca-cde0-351e-881d-f0dccfae51ee | -7.33777 | -45.28113 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bf41e3a-8b51-3b8d-89a8-5608787b3f83 | -7.39783 | -45.98588 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7beb81e2-efb4-3729-943a-06722cfeb21f | -9.93418 | -47.15977 | 2025-10-30 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0a97fc3-6eb6-3ef8-a5e2-1f5164dca7f1 | -8.32858 | -47.92997 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| fafdfc97-0e9b-3323-9687-be029d35c6b9 | -7.29514 | -44.9637 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3f3dd19-8d39-386f-b280-806e3ed4f111 | -6.81104 | -48.64719 | 2025-10-30 04:25:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e95a1a02-c475-3c38-a131-61c5b7687d5e | -5.58954 | -46.5498 | 2025-10-30 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3263ee1d-e722-3c12-859a-5fb033f9ce26 | -6.13842 | -41.5946 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| c81f83eb-cc31-3173-afaa-6974cf81e1e7 | -5.30477 | -44.32388 | 2025-10-30 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43ffa94e-66a0-33b9-b36c-d95f1bf3cddb | -9.87855 | -44.87795 | 2025-10-30 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 602f4d5c-355a-3298-bed4-29e33330395b | -6.18927 | -41.57875 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b83b0c50-23fc-3360-a12d-5318702a761e | -6.74997 | -44.60999 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2853afd7-014c-35c0-b01a-cf1359dc7ac4 | -11.07026 | -47.53725 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 82a8362f-5692-3acf-9757-d87522c70541 | -7.10105 | -39.57819 | 2025-10-30 04:25:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 513dec0c-f7b0-3c21-9564-3ed29f28d2b7 | -5.26422 | -42.49665 | 2025-10-30 04:25:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9dbf2282-d8cc-3a58-a4f0-e417f285fe6b | -5.58955 | -51.12799 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5c09ff7-bc65-353c-94bd-79cb580ee40e | -6.98878 | -46.23369 | 2025-10-30 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c75623d-d9ad-3146-b72b-3dbc6dea0d41 | -6.13362 | -41.57364 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 07cdd494-d30b-3165-8a37-1035e71e258f | -4.56321 | -46.33693 | 2025-10-30 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dfe47247-dcfa-3fbc-bc2b-b9cc072fc157 | -5.7231 | -44.40595 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7950498-fc52-330f-9eb0-ad622001885a | -6.17709 | -41.60725 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 30baed82-38b6-343e-bd5a-21c787b28b31 | -7.37361 | -42.4569 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d06081e2-22ab-3118-a750-2856d9337562 | -9.23714 | -45.56005 | 2025-10-30 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed06d23f-f2c1-31a5-8fbc-ee826ca9425f | -8.07117 | -45.15247 | 2025-10-30 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 754f0475-22f2-348f-a531-9b76f9f4b8ed | -5.2173 | -44.01078 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98b641b0-c9c2-3bba-ab9c-2a07322c86f1 | -7.59188 | -45.37465 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4381ed1-449e-330f-abd5-40a79827a502 | -5.59984 | -42.77362 | 2025-10-30 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecfead39-6ccd-3b17-a693-0a1713fa626a | -6.33136 | -46.4371 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fca2be1-33b2-3bfa-a8eb-fa5912e314d8 | -9.93347 | -47.86815 | 2025-10-30 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 099256ce-7f24-33ac-afa9-84517ec4927a | -7.95633 | -46.73156 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d25ccab6-5f2c-3d46-9b31-1bbaaa871874 | -4.35623 | -48.19926 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b687123-3d9d-3a6b-a7c8-4c0322eb5814 | -10.25148 | -43.95905 | 2025-10-30 04:25:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bdd49851-88a7-3a07-86ff-03a19c7c2226 | -9.49858 | -40.37691 | 2025-10-30 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 5e99bf49-2686-3d9f-86b9-041c14a573ee | -7.08298 | -44.93098 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b3905170-1bf0-3f1b-853b-5d433402db79 | -8.81406 | -47.91645 | 2025-10-30 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbb60046-9aeb-341e-b0ef-93a3dec2a37d | -7.08243 | -44.93457 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e7c3c3c7-6fe6-3d9f-8ad7-de72bfe7547a | -6.13687 | -41.69208 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 7b2d4a92-eb1d-3b62-af33-e99db5a2c221 | -7.31794 | -44.12702 | 2025-10-30 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30a8a41a-cef8-3514-a079-8bbd05107529 | -5.63656 | -41.09337 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e242fa96-9637-30f9-b3f1-736a544f6b56 | -4.84651 | -45.42456 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ad430c6c-f828-3c69-9baf-cbaa42819894 | -7.33915 | -46.89626 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2506872c-73d7-3770-a1fc-22e9570c7aa6 | -5.48612 | -44.10739 | 2025-10-30 04:25:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5792858-714b-3952-9adb-1eeb3df83f7b | -7.59882 | -43.60591 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52e6a8d7-c933-34e5-a869-09a61b361add | -10.64643 | -47.89381 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 011e7f0b-b947-31cc-a8bf-0efe2d30ae23 | -5.51467 | -41.23844 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 476555c4-8fe0-32ab-9320-ac8be8a8a54a | -10.88868 | -47.59042 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad7aa5e6-44c7-3cb6-ba36-6d3e066f3989 | -5.27672 | -47.23748 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45c43a87-c233-3696-8ac0-028ccb2e85ee | -7.29163 | -45.66668 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff50f8e7-f3d4-3dc5-a74f-7152739f4f78 | -10.95986 | -47.56968 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 882895a0-e4cc-3fbf-b1b3-464e7883def9 | -7.27996 | -46.8829 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c5f1373-7dff-3fb1-ae14-ec96873b08ad | -9.74986 | -45.00864 | 2025-10-30 04:25:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aeb859f0-bbe7-378c-8bf0-242795d41bb8 | -11.8442 | -47.92661 | 2025-10-30 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4415ae1b-29a9-3346-8aea-849397228348 | -6.63601 | -44.60032 | 2025-10-30 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f03596-a271-37ac-8677-0371c39ee8e2 | -5.66075 | -42.79334 | 2025-10-30 04:25:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 92627efc-3bfc-3731-9972-57fa077f3880 | -5.13636 | -46.19394 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d341bb9f-8e7d-3030-9823-626a99c10d14 | -5.51785 | -41.24417 | 2025-10-30 04:25:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e5c7224-18a8-38e9-9572-93dc12febd95 | -7.11975 | -47.01497 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a23bbb35-0908-37d0-83e0-42e51fddb9cd | -10.76805 | -44.7374 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5cce174-c668-3304-8229-71a2698bddcf | -5.80718 | -40.84061 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 42dde56c-9bad-39d7-aa5c-a6249c35ee22 | -8.17949 | -44.47159 | 2025-10-30 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 653a96d6-27ea-3cd6-ac92-93b3cf6ea40c | -7.30777 | -47.81419 | 2025-10-30 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9fd94392-2531-3c75-a2d5-e0faaacdd140 | -7.92828 | -46.80174 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a98fa87-1674-39b7-96c0-107e923179e9 | -4.40956 | -48.94931 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b7150bf-0aa6-3ce0-8bf0-84b7e308a14a | -9.86347 | -47.69027 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04a9e970-3351-34be-99ca-9d52616e3a38 | -7.29495 | -45.66721 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a9382105-f571-31e9-aa16-a18f6f659d81 | -7.35173 | -47.62626 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2ef1e11-4d86-36fc-95d3-2a0d959941e2 | -4.60529 | -48.75063 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e442e5-ba98-3361-b9fa-b95b558316a9 | -4.81734 | -45.65305 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bac021e-a8ba-3fba-aae2-ef8c89080bee | -5.62316 | -47.11036 | 2025-10-30 04:25:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a12bd81-4699-3018-93ff-c18d02e318f3 | -6.87102 | -45.07462 | 2025-10-30 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07f12b90-aef5-3e80-a942-f11aeb81b68e | -4.88842 | -45.43817 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d151d803-a87c-3183-a3bb-724b9772c3ff | -5.77568 | -44.38797 | 2025-10-30 04:25:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5efae084-7aca-369b-9eab-42d67e1f157b | -6.10689 | -41.72428 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |


[Clique aqui para ver as próximas entradas](README48.md)
