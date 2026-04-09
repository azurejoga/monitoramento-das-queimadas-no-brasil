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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e898ee1-c51e-3a85-9de3-b10f70b8fe22 | -12.307 | -57.4008 | 2026-04-09 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 24e7dab6-5044-3cde-a6ee-23ca8140d308 | -14.1216 | -43.4217 | 2026-04-09 00:17:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21c13f9e-b6bc-3c8a-a26b-14081374de84 | -11.8692 | -43.872002 | 2026-04-09 00:17:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7ba28a0-62e3-3163-a08e-f9ed53f81b29 | -12.0168 | -45.235298 | 2026-04-09 00:17:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b425fa64-1fbf-3c68-886b-7274094a9b45 | -19.597 | -40.076801 | 2026-04-09 00:17:00 | METOP-C | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b5d9fb73-2794-3dc8-8ba2-a82ab4cb533d | -12.0266 | -45.2332 | 2026-04-09 00:17:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2582126c-bf19-3597-ad56-867274515249 | -11.8675 | -43.863998 | 2026-04-09 00:17:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 93c70a06-847b-3680-aad3-915478515ebe | -14.1314 | -43.419498 | 2026-04-09 00:17:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8069f62e-5ebe-354b-adad-6a6ddf7f6da9 | -11.8658 | -43.855999 | 2026-04-09 00:17:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4f42ab08-90f0-3cd0-ab00-602d8e468e2b | -14.9012 | -41.9856 | 2026-04-09 00:17:00 | METOP-C | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4a5c0e45-d789-38fa-9497-ca0102f71efc | -14.1297 | -43.4114 | 2026-04-09 00:17:00 | METOP-C | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52e012be-bd91-3e09-9916-29e1bcfd6d73 | -29.79842 | -56.9588 | 2026-04-09 00:54:00 | TERRA_M-M | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 14.2 |
| cead0d88-5633-324e-afe6-16caf610e575 | -18.50764 | -55.52197 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.6 |
| f50c9f6b-b4c3-36a8-96ed-dc398378af8b | -18.49538 | -55.50318 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.8 |
| 035cc36b-eece-33e8-97cf-61f10dceff02 | -18.49386 | -55.49299 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.6 |
| a6042e2c-299b-395d-a497-b9f3b54ac036 | -18.50461 | -55.50163 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 269d8339-fef5-3ef1-af7a-609d6edcd7de | -14.9242 | -55.97784 | 2026-04-09 00:56:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 69335d5f-e2cb-3885-9a99-7bbd260bea87 | -20.09729 | -57.22281 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 26452b18-02c8-3939-84cb-64990b2af029 | -18.50613 | -55.5118 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.0 |
| 94721dca-7194-3d6c-bf79-3adf84b1f63d | -18.71403 | -57.54593 | 2026-04-09 00:56:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 4f607062-68a6-3e38-880b-d73da85cbd5b | -11.93572 | -58.08224 | 2026-04-09 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 78ef7054-ebb5-3c50-ab5a-7971b17e436d | -12.29908 | -57.39998 | 2026-04-09 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| d7ef2415-4a4b-3d44-9127-f3ed629a8bcd | -12.28866 | -57.3919 | 2026-04-09 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0769984a-0613-3c44-a640-ad05004c4d00 | -12.29003 | -57.40134 | 2026-04-09 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5ca9c4b6-3649-35a4-abf1-ed1abdf5cea2 | -11.93443 | -58.07312 | 2026-04-09 00:58:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cd7aa93e-c846-3c90-b17b-622524d32a03 | -12.30044 | -57.40942 | 2026-04-09 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d564d1d6-a005-387d-8386-5636abce9817 | -12.29598 | -57.18565 | 2026-04-09 00:58:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4021dde9-ed13-30f7-a5c5-492e9cf27716 | -18.496 | -55.498501 | 2026-04-09 01:22:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2569883b-6145-39e9-ae15-8001663132bb | -18.4907 | -55.479301 | 2026-04-09 01:22:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 345a78c9-c617-3db9-bfdb-6e66a3737dc4 | -18.4995 | -55.486401 | 2026-04-09 01:55:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 142335bb-c6ed-35fe-be57-42c84b740e9b | -18.504999 | -55.506302 | 2026-04-09 01:55:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8b379534-9cea-3e40-8fbc-7eca6a7c7a3e | -18.514601 | -55.503399 | 2026-04-09 01:55:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7c7cb3ab-594e-3ff6-b614-ea7a4c4e6500 | -14.12339 | -43.41935 | 2026-04-09 03:19:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 85d2fa34-47cb-365f-8163-9e8e104deba5 | -11.86306 | -43.86352 | 2026-04-09 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c31a4b3-7200-3fa6-b434-e946abfb0680 | -12.43253 | -40.91816 | 2026-04-09 03:19:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4a3d1975-918f-3bf6-8cef-12b2f69df471 | -11.87002 | -43.86494 | 2026-04-09 03:19:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8cb73b87-7cba-3b7e-814f-846a2e251ef3 | -14.12287 | -43.41512 | 2026-04-09 03:19:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58a49aa8-b75a-35f9-a754-d97adfd92f33 | -14.12941 | -43.41647 | 2026-04-09 03:19:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 480e5935-251e-3833-89f0-ce827699912a | -11.95839 | -43.37962 | 2026-04-09 03:19:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ca235db-cdca-30a4-aa62-4a41ed32dc5a | -11.7022 | -37.66788 | 2026-04-09 03:19:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b9333bad-12de-330f-83b1-5e80c240757e | -11.7014 | -37.67123 | 2026-04-09 03:19:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 23079588-305b-34da-9438-afeef80f4be7 | -11.70121 | -37.67313 | 2026-04-09 03:19:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c2739791-6420-3a6c-aa1a-c5cb8879bc95 | -14.12162 | -43.42078 | 2026-04-09 03:19:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46483bcd-6b0d-3ad5-89d9-e9262ba8481d | -19.5893 | -40.07586 | 2026-04-09 03:21:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 35e6f296-a384-352e-9c53-4c2c9b2219a3 | -18.90716 | -41.94384 | 2026-04-09 03:21:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fa922899-2095-3f6b-921e-92d95bbe1548 | -18.9075 | -41.94255 | 2026-04-09 03:21:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 60c05b45-e446-33f3-81c3-757d8fcd1fd9 | -18.90806 | -41.93973 | 2026-04-09 03:21:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 17b4cc98-87c3-30e0-adf3-92f1947d6c45 | -10.95678 | -37.7498 | 2026-04-09 03:49:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b3bb6481-7da7-320c-8c3c-22927fa6af10 | -10.58663 | -37.62129 | 2026-04-09 03:49:00 | NPP-375D | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 24983a30-0380-36b3-829d-d62bf9a23680 | -11.7038 | -37.67116 | 2026-04-09 03:49:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9049313d-7d92-3e5d-8742-6ab148cefb92 | -10.58325 | -37.62074 | 2026-04-09 03:49:00 | NPP-375D | FREI PAULO | SERGIPE | Brasil | 2802304 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32ca4838-e9b8-3d59-9574-18609cce9542 | -11.70043 | -37.67058 | 2026-04-09 03:49:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1a1f9186-7b09-3ce3-8e9a-ff19eea18ea0 | -9.45364 | -47.82425 | 2026-04-09 03:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d264662e-7a95-3580-864f-bc102209b3c6 | -9.45661 | -47.80901 | 2026-04-09 03:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a041724-e417-36ff-9bb5-43992c702b14 | -9.46289 | -47.81031 | 2026-04-09 03:49:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09279186-f092-3eed-a463-418077744599 | -11.82327 | -38.26479 | 2026-04-09 03:49:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 33434091-69f5-3f81-9a3d-166944ffccbf | -11.87197 | -43.86551 | 2026-04-09 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8641f440-9b0c-3103-ba5a-e0f026f6585a | -18.90714 | -41.94328 | 2026-04-09 03:51:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 43a3a025-b4e0-3867-babb-6eb8da370499 | -12.0193 | -45.23459 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f8d6f6d-57a1-3846-bfdf-c1bb00e23e71 | -12.02441 | -45.23563 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c64a9caf-2749-3fbd-a3e5-75974cc5a53c | -11.8682 | -43.85962 | 2026-04-09 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7698ef1-77d3-3969-8eec-3d24129ee10a | -12.03126 | -45.22741 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c39673a5-26f4-3cb4-a647-fd629d658473 | -11.86869 | -43.86302 | 2026-04-09 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cbfd6ef0-0b83-3064-9b77-0c6f35ab2b69 | -14.13057 | -43.41529 | 2026-04-09 03:51:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b12fad6d-53df-3a8e-acef-f8704c2ac63a | -11.96011 | -43.37812 | 2026-04-09 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb8d4560-b201-36b8-8c3e-39ed92aa8683 | -12.84101 | -45.9585 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55c94171-2775-3102-99c1-0a7c36951070 | -12.01872 | -45.23768 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 640d47f8-1f4c-3307-9823-fa752e029f67 | -19.5983 | -40.07762 | 2026-04-09 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 25a9d408-7838-3e55-9ad5-14d1990500dd | -19.5949 | -40.07698 | 2026-04-09 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 90f0e26d-28b6-3605-999e-12161741d2c4 | -12.02952 | -45.23665 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01d9fcc4-ed07-3258-ab3c-3a32ff9a7421 | -11.87337 | -43.86391 | 2026-04-09 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 143ff2b9-6589-35d7-a663-6b1ac2dc864c | -19.00969 | -42.14959 | 2026-04-09 03:51:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8e14b234-79fd-3771-9938-ac38fdc4fda7 | -12.83703 | -45.95076 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43808655-6314-383e-9125-2c66b3f93fa0 | -19.59084 | -40.08021 | 2026-04-09 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c6fbf52-2df1-3c98-b567-7ae7def95ae3 | -16.92238 | -43.60083 | 2026-04-09 03:51:00 | NPP-375D | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51df4b7f-2419-3ae6-af00-3b2689aba8d0 | -12.0085 | -45.23563 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73f5df51-ba71-34b6-93eb-38ec32c93e4b | -12.02499 | -45.23254 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05da2158-4fcb-317b-a1f9-0143896584f9 | -12.02557 | -45.22946 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e51fb22-c84e-3e67-b1ae-f5f91eb06a2f | -12.84166 | -45.95516 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11ff98d4-ba10-3747-a5f5-5eb1877d15c1 | -12.43309 | -40.92155 | 2026-04-09 03:51:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ea43f554-a20c-3a89-8db5-2fd3380ce935 | -11.95958 | -43.38165 | 2026-04-09 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 06b2193f-f5e4-328a-bc5d-f30fd4d06b1b | -19.00886 | -42.15426 | 2026-04-09 03:51:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ccae93b4-61cf-3885-9d61-19594287ad40 | -14.13056 | -43.41742 | 2026-04-09 03:51:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0455bbd9-2d06-3321-8068-4e67efb5234a | -11.96045 | -43.37698 | 2026-04-09 03:51:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9758d4e9-ed6b-3051-ab52-e3e0f6e9aacc | -12.01989 | -45.23151 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44a8f41e-e42e-3a8c-9033-23650c1dc269 | -12.83574 | -45.95741 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 303713d8-dbac-3e26-a5c9-8f678327b403 | -12.03068 | -45.23049 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb05c6ef-b97d-329d-b111-60935438ec1f | -11.86729 | -43.86462 | 2026-04-09 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 167255e2-a412-3215-9b61-66e21fddd101 | -14.1262 | -43.41658 | 2026-04-09 03:51:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f4adc0c-3e7d-3d9f-a589-507ea1168560 | -12.43394 | -40.91672 | 2026-04-09 03:51:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a4541b1-2cb1-3b9e-be72-ce20dc3142ec | -12.83638 | -45.95408 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e8fdbba-f605-3ab3-b6ba-70e3e031135f | -13.2652 | -43.54992 | 2026-04-09 03:51:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 250a2aab-0691-370e-8c17-5d8be7c1d0ba | -19.59149 | -40.07634 | 2026-04-09 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c33b754-7604-3ba9-bb73-e80967dc144b | -12.01419 | -45.23357 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03f63bab-6877-3cac-a325-6892bce72415 | -12.0301 | -45.23357 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9e5d91c-83ed-310f-8aa5-88b3bca6c44e | -14.12539 | -43.41874 | 2026-04-09 03:51:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dce84918-84ad-3db1-bce5-6f4e7bf254d7 | -12.84036 | -45.96184 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99c4bbc3-2cb9-304e-9bb8-dfae09d98c0d | -11.87287 | -43.86052 | 2026-04-09 03:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 777e9643-9c3b-3caa-b334-241b497860a5 | -12.01361 | -45.23665 | 2026-04-09 03:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88e2e59f-e75d-3d6a-a42f-504d52b94a48 | -12.83768 | -45.94744 | 2026-04-09 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README2.md)
