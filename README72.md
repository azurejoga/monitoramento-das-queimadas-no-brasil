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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad5647b7-54cd-3ca2-8617-1551b29e7eb5 | -4.08952 | -54.28649 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a48bb37-2db1-3c01-beb2-53c50879c2d8 | -4.08948 | -54.26509 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08824522-7f53-320d-9639-af965b54bc89 | -4.08669 | -54.26112 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2114eb58-e4b8-398e-951f-d081bc796914 | -4.08596 | -53.877 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| daf74dd7-8260-362b-974f-67c133fe9204 | -4.08542 | -53.88046 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2a716bd-6664-3ead-b0df-e0505fd246c0 | -4.05284 | -54.28083 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87aec2e1-be92-3f6a-b53d-1de1861f3a12 | -4.03652 | -53.86927 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5053fcce-7380-32b6-a3a9-8657c3668959 | -4.00901 | -54.38483 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3274a2d4-4dba-3846-bca6-0be185500bc0 | -4.00622 | -54.38081 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79217d79-64a9-3a00-916f-33ac6a49a003 | -4.00567 | -54.3843 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 604e4ff2-6d53-3ba8-a448-638a66aa9a2c | -4.00288 | -54.38028 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb2a0c44-64ea-3de2-826e-8de79b767616 | -3.99287 | -54.46496 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73c3a9a6-6794-3607-ac5e-ac490b771c63 | -3.99231 | -54.46847 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8fae98c8-2bf3-3f9b-ac62-40a21b3989ff | -3.98952 | -54.46445 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd7f0b01-8861-334e-b470-a79086f524cf | -3.98896 | -54.46796 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d14be96-c35d-352d-8823-1e4a8cd268ca | -3.98807 | -53.98219 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad4bbc3a-34e5-39bf-a80a-e3127103d1bf | -3.98062 | -54.34813 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8517fd46-21ae-3623-88ab-d7e1d5f47658 | -3.98006 | -54.35163 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| baee25e3-a773-3dbc-acd6-764f2f831aab | -3.97728 | -54.34762 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bd7daeb-7bda-30c3-9814-863dcd440261 | -3.97672 | -54.35112 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16249925-0fb9-3304-880b-698e139653d7 | -3.97394 | -54.34711 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1242f31-dad4-352c-a179-37be165b5af8 | -3.97388 | -54.09367 | 2024-10-24 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e1c2e02-e727-3381-8d4c-251787e6dcca | -3.96666 | -54.43576 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6a0a440-ec70-3568-ad9c-abfe1b96f48b | -3.9661 | -54.43928 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 962c5d3a-b7bc-3223-8d3a-f7545b602b3d | -3.8504 | -54.76522 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d50a55d-7ee6-3da7-aca4-033e418e7945 | -3.64984 | -54.79567 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fd60213-170f-3aa5-9b63-bbf310e9cd31 | -3.64704 | -54.79154 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e1b3563-fa4a-3539-b06f-0af480ae5a5d | -3.64647 | -54.79512 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3440b10-bec8-3e56-8193-80552023b8fa | -3.63986 | -54.68444 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca827e26-7fbc-320d-bbcd-5d7fd18c9494 | -3.63649 | -54.68391 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 714a0182-1428-3f77-8536-12c394f6749e | -3.62251 | -55.29773 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244ea163-9c17-3e0a-8ef4-f25df838733c | -4.47289 | -55.08949 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5deae74-06e7-32bb-95c9-78a206c318b8 | -4.42538 | -55.43276 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a74fed80-7164-3c13-8133-8bf2584c0deb | -4.42479 | -55.43643 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fd24829-b1e7-39f8-adde-8d18b4cb9210 | -4.42196 | -55.43221 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4692504a-7062-31a8-909d-43d9fb24459f | -4.42138 | -55.43589 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76bc6c11-9927-33fa-9d67-2c7e3fa668f3 | -4.39621 | -55.04468 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8db45c14-ce7d-3deb-ab5b-e16ce4bf2c5a | -4.39564 | -55.04827 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91b78c2d-0881-394a-bf0e-6d1720e64009 | -4.39283 | -55.04414 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5e449ee-69c2-3ce5-802d-4f765c5c53b1 | -4.38781 | -55.18717 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef267392-026e-333a-af8d-16d3d07b9e39 | -4.38442 | -55.18662 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f4a9c2e-231a-3abb-b3dc-dec98d97647b | -4.37743 | -54.79285 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff9cd3de-10d7-38ae-ba27-2abf080c7587 | -4.29967 | -55.08469 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82d1a85-8e8c-3045-af83-406981c0045b | -4.26092 | -54.7566 | 2024-10-24 04:55:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e248967-485b-3812-8036-b1fae0e566ce | -4.23147 | -54.8978 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 08ec90ad-64c4-323c-8aa9-dac7ee7fff92 | -4.14504 | -55.15354 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5e573862-e32b-35b4-8e7f-d0aa86f5001d | -4.14164 | -55.15302 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e2379d1-2796-32a5-a447-766ec4f4fc18 | -4.13349 | -55.02932 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfa28c65-2a75-391b-8172-716b350f40e1 | -4.13067 | -55.02524 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b929ebc-8af7-3207-97fe-c6cb71d7de71 | -4.12728 | -55.02474 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82c782ca-e4c3-3997-b3b2-5e9c40d10257 | -4.12101 | -55.04227 | 2024-10-24 04:55:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ac216b4-52d2-3004-a04f-4dbeb97614c3 | 1.5628 | -55.66081 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3795b146-0931-3e4e-9760-76029550c1fd | 1.5598 | -55.66566 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19697aaf-e26c-304d-998f-e792d0ab0d14 | 1.55614 | -55.66624 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e09786b-6674-3346-8a39-b5a7b7410c31 | -2.02586 | -55.89117 | 2024-10-24 04:55:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bd0f559-f962-3eef-94c4-522e4c467ce0 | -2.00024 | -56.40125 | 2024-10-24 04:55:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46528f14-4aeb-321a-8968-b4402e698fbc | -1.96431 | -56.43886 | 2024-10-24 04:55:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec32e048-b085-3a5d-9ce9-de70dea52dfb | -1.17547 | -55.70433 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d2c76d9-8d85-3a80-82a6-e129db83dfa6 | -1.17483 | -55.70834 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a94b1626-1f2b-3e8e-9dfd-e412df4c190b | -2.02521 | -55.89518 | 2024-10-24 04:55:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 608e1b79-7d01-3356-b25d-243798c88163 | -1.91493 | -55.66073 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a975a83b-4d04-3b87-94a3-c24315cb9619 | -1.87698 | -55.62664 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d09864d-80b9-3c0e-9a40-f756682eb2ed | -1.85599 | -55.29985 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8219c23-3fa2-3c6e-a37a-98397ee9dd4a | -1.72962 | -55.75774 | 2024-10-24 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 493f1324-c91c-3828-8540-65c564cd313c | -1.72258 | -55.64311 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3b47341-3f58-3017-bfab-9c551d878cd4 | -1.71026 | -55.0458 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7aedbc3-f05c-3136-bc69-9fdb58bc2a3f | -1.69319 | -55.10828 | 2024-10-24 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1239ad90-6030-3610-b1d9-2ab41b04815e | -1.68973 | -55.10775 | 2024-10-24 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c5227d0-4345-327a-ba4f-5ac5aba8d007 | -1.61187 | -55.11552 | 2024-10-24 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457b9b0a-d642-3c6e-b892-93e8a6e6cab2 | -1.60404 | -55.8452 | 2024-10-24 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa05530f-d700-3821-9c28-52e108fc63db | -1.60048 | -55.84461 | 2024-10-24 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ba4af07-eeef-328a-86b2-e8a8aa98570e | -1.54631 | -55.89524 | 2024-10-24 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93e06d71-6344-3bd3-8d8d-e0c27930d179 | -1.54567 | -55.8993 | 2024-10-24 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f78c1535-caae-3f8e-9ad7-fa691cd1d603 | -1.54302 | -55.34586 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab3de11d-a0ea-3227-94e9-c7df3ead69bb | -1.5424 | -55.34969 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bc0333e-4e3b-3f2c-9cbf-361310e0fd12 | -1.54222 | -55.34669 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 091eb79c-7572-36ce-9cbe-d390956d449a | -1.5421 | -55.89871 | 2024-10-24 04:55:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 092b46a5-6761-39f1-83ce-36f3f089acfb | -1.54162 | -55.35053 | 2024-10-24 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9a3314a-6cfc-3817-a486-b16d538353e6 | -1.48506 | -55.10007 | 2024-10-24 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 290188d7-f5e0-38ab-a482-9ef7b5880b04 | -1.46952 | -55.33137 | 2024-10-24 04:55:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be07166b-6dd4-3917-b3bc-3c4942493f0b | -3.68362 | -55.44424 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a745d6c9-1fbc-32da-b1f9-baae6541d508 | -3.68018 | -55.44367 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a2d1ce7-126e-3433-821c-80a3b05f5335 | -3.64662 | -55.49954 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ea90679-d0b6-3071-ad7b-817e94f75262 | -3.62917 | -55.43181 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72d50335-619b-3a47-b068-541a9d174d80 | -3.6282 | -55.50422 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 850f3fad-7b00-3be1-9f25-8937b6198605 | -3.6276 | -55.50798 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16ee0560-9abe-3bb4-9509-0a5f1a8ec556 | -3.62475 | -55.50369 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70f82e55-ea80-3ea1-ad77-99d030d124ea | -3.62415 | -55.50745 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34ac60f5-a5c7-3ec5-9852-b8683c9edcd9 | -3.6213 | -55.50315 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d09b57b-4922-3cb0-ac02-bce80ce99120 | -3.6207 | -55.50691 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| caa0c7a2-9409-3ac4-bdfa-329cd98bc191 | -3.61437 | -55.4142 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1af1cc0b-033c-3190-b7ee-b4e285787e1e | -3.60915 | -55.51283 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| d952fcf1-e4ec-304b-ad31-9308e6093e95 | -3.6063 | -55.50854 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b35d751-490d-3b32-90cf-1a61c62b9883 | -3.60569 | -55.51229 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 1f95c25e-821a-39b6-8698-c7499cd47aee | -3.60509 | -55.51605 | 2024-10-24 04:55:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0782d921-1edc-3cda-87c3-d7c3aa5ae003 | -2.48545 | -55.72514 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ff9a72b-3290-359e-81db-b0d338a9c893 | -2.48317 | -55.71687 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d8abb08-c37f-31f6-b232-020b5dc71688 | -2.48193 | -55.7246 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbd5956d-a7e3-3e7e-9c1d-873703a37fd1 | -2.53338 | -56.07683 | 2024-10-24 04:55:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18012d10-8c0b-38cf-b560-b1f058d4a9e5 | -2.48668 | -55.71742 | 2024-10-24 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
