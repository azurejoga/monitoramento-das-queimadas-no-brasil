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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c065c948-e026-33b0-a425-4fe3670ac1f1 | -5.3641 | -46.430698 | 2024-10-05 01:10:19 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a755ebd-62d1-3b5f-92e9-21eadd507555 | -5.8019 | -49.131802 | 2024-10-05 01:10:23 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4718f2c6-3b8a-385e-ba63-a1fe5d6cfdc6 | -5.8061 | -49.148998 | 2024-10-05 01:10:23 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9043065-13fc-330e-97ba-20d4d3c172d9 | -8.6756 | -62.0784 | 2024-10-05 01:10:24 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dad9731e-802d-3e98-94a1-9a829bfdc233 | -8.6635 | -62.069401 | 2024-10-05 01:10:24 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dac3eaf-7a13-3517-bd6e-c7aa254a35cb | -8.6658 | -62.080502 | 2024-10-05 01:10:24 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f09ec69f-d662-3469-b601-e3f24d96f323 | -8.6682 | -62.091599 | 2024-10-05 01:10:24 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd82cd8c-3284-3005-9b3c-bd91dd01a203 | -8.2218 | -61.192799 | 2024-10-05 01:10:28 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8168e63e-56df-3b3c-9f22-6a4518961a07 | -8.2239 | -61.202499 | 2024-10-05 01:10:28 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3af2313-3388-3280-bcfe-4877b45b4172 | -8.226 | -61.212101 | 2024-10-05 01:10:28 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa1f186b-568a-3c0c-a69b-95fce0220840 | -7.9282 | -61.255501 | 2024-10-05 01:10:33 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd5b4534-a391-3d65-888f-6e2cb347b2b4 | -7.9302 | -61.265099 | 2024-10-05 01:10:33 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f573eff1-4332-3477-b7c4-9102330da352 | -7.8971 | -61.445599 | 2024-10-05 01:10:34 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79988143-0a91-3713-90a7-fb63e6ebb6e8 | -7.8853 | -61.437801 | 2024-10-05 01:10:34 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f6ad969-21da-3cf8-84c6-556020c2f677 | -7.8874 | -61.447701 | 2024-10-05 01:10:34 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 752bdc1d-1734-3725-bb54-51fa82b4e92a | -7.8896 | -61.4576 | 2024-10-05 01:10:34 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8d88462-0804-3a13-8af5-d28bf5ef4366 | -5.8972 | -53.429901 | 2024-10-05 01:10:38 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 958c4f03-eaf3-3b4f-b334-e849b26c9bcc | -5.8993 | -53.4389 | 2024-10-05 01:10:38 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4677e614-851e-385b-84e5-16319f782e53 | -7.1468 | -59.3573 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8da92a7-a1da-3ed4-b09c-7706d5fc6ada | -7.1515 | -59.284698 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28088275-596b-31c8-aae5-ab0ff15733f7 | -7.1532 | -59.292301 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5205bb3b-6c5d-3c4a-a2bb-baf835ff077c | -7.1416 | -59.2868 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f753c6a-c0f0-3cab-aa2d-d5983e43f449 | -7.1433 | -59.294399 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02ac3690-b602-383a-978d-a3de4b05a2cb | -7.1318 | -59.289001 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d611b56-87de-3ae9-95f4-5a33b37b3814 | -7.1335 | -59.2966 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dfb9e821-2315-3a91-96dd-ab00b07b46d3 | -7.1351 | -59.304199 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edaa1d96-132e-38d9-bb4f-556d4b950d65 | -7.1451 | -59.349701 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 062c8e17-c2cc-38d6-8cc4-be5a062cfb51 | -7.2009 | -59.603699 | 2024-10-05 01:10:39 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a17f520-f94e-3cc4-9451-a01b6eb9a242 | -7.063 | -59.256599 | 2024-10-05 01:10:40 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24c38c94-06bc-30a0-ac1d-124e20db7adc | -7.0647 | -59.264099 | 2024-10-05 01:10:40 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95b7a121-5b73-3201-a3a3-e16bc23f777a | -7.0599 | -59.288898 | 2024-10-05 01:10:40 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b7c89557-72e1-33a2-8f4f-49d6b7208e83 | -6.9451 | -59.047699 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8bd0078-c2f7-3b8a-897e-cd5d1037b1a6 | -6.9467 | -59.055099 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 948d4478-cb55-3cca-9841-85cd1c6f05e9 | -6.9483 | -59.0625 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6fb9517-c5c8-302a-9c9b-c4a4163ce582 | -7.0177 | -59.377499 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb2490b-59fa-3984-a78b-289fa0e3d88e | -7.0194 | -59.385101 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a56a5b3c-205a-3e14-97a3-81f2768dfd00 | -7.0211 | -59.392799 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cec55c7d-6384-3180-9dcc-f4543956590b | -7.0228 | -59.400398 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3492e51b-a20f-3afc-9bb5-7c6cf4f10110 | -7.0063 | -59.372002 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad4e4058-56e5-35e6-9037-a1b29fc0107f | -7.0096 | -59.387199 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a59e1ba-a5f1-3104-8b26-83f31a2c9c19 | -7.0113 | -59.394901 | 2024-10-05 01:10:41 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1dfb26d0-65fb-3b7d-977d-75c85a2e4066 | -6.9533 | -59.880299 | 2024-10-05 01:10:44 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c397de38-82ab-33a4-80ec-7f888e882d59 | -4.0536 | -47.919201 | 2024-10-05 01:10:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb22a2be-75a9-31a1-8afa-9270bb8fe013 | -4.059 | -47.941502 | 2024-10-05 01:10:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad162302-022d-37cb-bd18-ae7b592840ee | -4.0493 | -47.943802 | 2024-10-05 01:10:46 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4ac6ec-1d7d-36d2-8f08-d18ff82adb2c | -3.5921 | -47.4879 | 2024-10-05 01:10:52 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dc299d3-13c3-3526-8764-cdfdfff505a6 | -3.598 | -47.512199 | 2024-10-05 01:10:52 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31114522-ae06-3118-9c5a-c34458138d85 | -3.6038 | -47.536301 | 2024-10-05 01:10:52 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14fea091-ad7c-3893-8601-947e2135b055 | -3.5824 | -47.4902 | 2024-10-05 01:10:52 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd3d5f29-b18d-30b4-b45e-63e2afc2b616 | -3.5883 | -47.5145 | 2024-10-05 01:10:52 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8c5d1e-bd25-3299-8dbe-8033662cf172 | -3.5941 | -47.5387 | 2024-10-05 01:10:52 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3158085c-9cc5-30f6-b2cb-fa1b420113ca | -3.2952 | -49.452 | 2024-10-05 01:11:05 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca55bed-8ea0-35d4-afd8-1f3ec68e1775 | -3.2995 | -49.469898 | 2024-10-05 01:11:05 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90cd89b7-dc48-3f43-b4ae-243d9dc89684 | -3.2855 | -49.4543 | 2024-10-05 01:11:05 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95c820a5-e336-3d09-8c85-21ffc9a13ede | -3.2296 | -49.391102 | 2024-10-05 01:11:05 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4141d42e-3e79-3c91-9a80-a082c5574b47 | -3.2339 | -49.409199 | 2024-10-05 01:11:05 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 979b1b49-566c-3bfc-8995-e57b87ed30e8 | -3.8316 | -52.344299 | 2024-10-05 01:11:07 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 222ea7b2-22fb-3ac6-8be1-3f78d1f93c09 | -3.8342 | -52.355499 | 2024-10-05 01:11:07 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 844ffd8c-639b-3a1a-8ee3-f0ef26a1df9a | -3.8102 | -52.384602 | 2024-10-05 01:11:07 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4e20851-7d6f-3111-aff7-ea0333718241 | -3.7979 | -52.375801 | 2024-10-05 01:11:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ece9eaea-8104-3b3a-bf0b-90159b2bf23c | -3.8005 | -52.386902 | 2024-10-05 01:11:08 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03b93a31-7081-3e44-83e3-f6ee34481cf1 | -3.7618 | -52.265202 | 2024-10-05 01:11:08 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60a07d0f-7117-3eef-998b-15735053267f | -3.7644 | -52.2766 | 2024-10-05 01:11:08 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1730f4-34c3-370b-9de0-804ab56f2f67 | -3.2501 | -50.127602 | 2024-10-05 01:11:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc3b269d-e022-3ebc-b21e-f4369fe109e6 | -3.2404 | -50.129902 | 2024-10-05 01:11:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 509bd9a9-14ff-3df1-83e1-b8939a25f3f2 | -3.3048 | -50.4468 | 2024-10-05 01:11:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 110d142a-72ed-3c57-b476-9c17899edc9f | -3.2914 | -50.433701 | 2024-10-05 01:11:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79ca2f8f-7542-335c-be1b-6dc384181b77 | -3.295 | -50.4491 | 2024-10-05 01:11:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f16c1a9-0ad4-38f3-a600-0b70cd8285e5 | -3.2986 | -50.464401 | 2024-10-05 01:11:08 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fd64838-a730-313c-be7d-bc240816e005 | -3.2817 | -50.436001 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49cc3600-2add-3690-b010-c8a366006ae3 | -3.2853 | -50.451401 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a241406a-a155-3248-b64c-25227f3adaf2 | -3.2889 | -50.466702 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96e5144c-c049-3ad5-b113-c80eb99c593e | -3.272 | -50.438301 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e716a8f2-6ee5-30cd-b5be-81ad6223efba | -3.2756 | -50.453602 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff54201-31db-3449-b1f2-e432b0b3a964 | -3.3866 | -50.969501 | 2024-10-05 01:11:09 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95b72c87-3ab7-394d-b700-b596ee517623 | -2.8902 | -48.908699 | 2024-10-05 01:11:09 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 652e41a7-9add-3d62-a0f1-7dcba95efc4d | -3.2307 | -50.349899 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16316f60-606a-3577-b952-c68f9425ae91 | -3.2344 | -50.365501 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1c3850-353a-326b-82e6-f06b32fb8476 | -3.221 | -50.3522 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47d26868-8cc8-30c4-b784-2532c1d5227f | -3.2247 | -50.367802 | 2024-10-05 01:11:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ada4970a-3bd6-39aa-b426-f9767d53dd9e | -3.1254 | -50.207699 | 2024-10-05 01:11:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14b2c4b8-5ab0-3a7d-8bce-2af9e5510220 | -3.1292 | -50.223701 | 2024-10-05 01:11:10 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9709ea05-2f38-3945-a5be-c7ed75c951d6 | -3.2199 | -50.827702 | 2024-10-05 01:11:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9930a3d0-4278-38b9-b4bd-d2ee9c69946e | -3.8656 | -54.223 | 2024-10-05 01:11:13 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab942fed-ddfc-3950-9ab3-c37b154fb1af | -3.4711 | -52.828701 | 2024-10-05 01:11:15 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf47358f-a861-30e3-ac56-e7140fce9f2b | -3.5684 | -53.248501 | 2024-10-05 01:11:15 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9707918e-a79c-3f0c-9082-3371a71da5a1 | -2.5506 | -49.0718 | 2024-10-05 01:11:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10a30b86-7787-35c0-ba8f-998e927902c2 | -2.8798 | -50.689499 | 2024-10-05 01:11:16 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad143dd-9601-33c1-9905-5072659ece36 | -2.8833 | -50.704498 | 2024-10-05 01:11:16 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b43b482-ab8b-3f1b-a95f-4417d0487fad | -2.8868 | -50.719398 | 2024-10-05 01:11:16 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3661aa90-5c61-35cf-8e77-01535eb898fb | -2.87 | -50.6917 | 2024-10-05 01:11:16 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cdf7b7e-9959-3000-a318-324fd1df3bcc | -2.8736 | -50.706699 | 2024-10-05 01:11:16 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5882160-c87a-3d1d-8f7a-e8ddce154f2a | -3.2918 | -53.342999 | 2024-10-05 01:11:19 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a943cb10-0c8f-310b-8802-e4a62a6d56ce | -4.2884 | -60.0061 | 2024-10-05 01:11:28 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 77843098-6690-3160-b0fe-35da167c2ae8 | -4.2901 | -60.013699 | 2024-10-05 01:11:28 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a72508bf-ef79-3e2d-a202-1f051e719deb | -1.1814 | -46.589802 | 2024-10-05 01:11:28 | METOP-B | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2ba2a72-851b-3012-a4cf-649ebe3f76da | -2.7151 | -53.966801 | 2024-10-05 01:11:31 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63c51eb0-9581-3363-a7ff-bded56efe52b | -3.867 | -59.730499 | 2024-10-05 01:11:34 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7d697f3-7916-3f87-a7c2-afa3cbdbeb9e | -1.0337 | -47.908901 | 2024-10-05 01:11:36 | METOP-B | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7c46522-a1af-3f28-819a-1bcdb6836b1d | -1.0396 | -47.933899 | 2024-10-05 01:11:36 | METOP-B | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
