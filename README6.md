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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cedffd2-f382-3d2c-ab8b-121dc84135ff | -11.7666 | -44.9986 | 2025-08-01 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 6cca24f7-6de1-388e-a989-f8105d4ed2de | -23.5446 | -47.8293 | 2025-08-01 01:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.4 |
| 13dc655c-f216-337c-96f7-22a884961eea | -11.7662 | -45.0218 | 2025-08-01 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 27e34181-bda2-3cea-aca4-04c888243ad9 | -8.3396 | -50.5652 | 2025-08-01 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| ae778b06-2d31-3c9a-8ba7-dde6dda2dbba | -6.7477 | -59.1909 | 2025-08-01 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 553368ba-d436-368c-8fb1-42e688cdcb24 | -8.0513 | -43.1001 | 2025-08-01 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 81.5 |
| 0b202a09-1c58-3da5-b8a7-d6e0acb6eb98 | -23.5234 | -47.835 | 2025-08-01 01:20:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 404.6 |
| 11d54e85-b198-3ba1-a38e-9f296e32675c | -9.3989 | -45.4928 | 2025-08-01 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 2135a85d-659e-359f-a92e-433f8b433448 | -6.7294 | -59.1723 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 407.1 |
| d276794a-d12f-379b-9761-f2d54a23d7f9 | -7.7255 | -45.078 | 2025-08-01 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 140.3 |
| def5155e-bc72-3576-97b9-5196fa42dee2 | -8.0324 | -43.1022 | 2025-08-01 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.6 |
| 4fb724cc-ba04-33e6-952f-b226cd4b3e4c | -23.5234 | -47.835 | 2025-08-01 01:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 434.5 |
| c3c3eeca-2b1a-364f-9183-836866826c46 | -23.5022 | -47.8407 | 2025-08-01 01:30:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.8 |
| bff5635a-208e-3680-8dd9-6e9cc19334b0 | -7.7446 | -45.0534 | 2025-08-01 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| f8314a6d-9b96-3e3d-ac21-9fe7b0e4f332 | -6.7478 | -59.1716 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 214.3 |
| 1c0ce9dc-653c-3298-8afd-556d569bc7e6 | -6.6143 | -59.9848 | 2025-08-01 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| d601a80c-dd44-3a9d-809c-ffff77ba33cd | -23.5446 | -47.8293 | 2025-08-01 01:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| df35c2eb-648e-3e6b-94bf-f8a7f7e8d43f | -20.7109 | -44.2727 | 2025-08-01 01:30:00 | GOES-19 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.3 |
| e23b12b0-f2e4-3607-bf29-10b42096e14e | -9.3989 | -45.4928 | 2025-08-01 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 3e1a8e37-1bf7-360c-aee0-30051197e327 | -9.3439 | -40.3058 | 2025-08-01 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 152.2 |
| 16f8adf6-759b-3e69-9105-768dba48004a | -6.7295 | -59.153 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 63daf6c8-46e2-3503-a533-bd3b39a24ba9 | -6.748 | -59.1523 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 5c305ac1-92a3-34b2-8aaa-8d8cb5a65a8e | -7.7253 | -45.1008 | 2025-08-01 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c6ddfb01-7837-3c6c-835d-01a5d31b8818 | -9.4178 | -45.4906 | 2025-08-01 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 089cd4ab-24e3-3a17-a9c0-c28c418d2c4d | -9.363 | -40.3031 | 2025-08-01 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 123.2 |
| 55459de5-81be-3f10-a020-b91789357548 | -7.7444 | -45.0762 | 2025-08-01 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 314.9 |
| a0a8eede-944b-326a-8b1e-4966c653e332 | -8.051 | -43.1237 | 2025-08-01 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 8309d4de-2afa-3c5b-8df5-2d5aeac297ab | -8.0513 | -43.1001 | 2025-08-01 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 697002b5-07ff-3a3d-874b-19a8bf1703a1 | -8.3396 | -50.5652 | 2025-08-01 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| f11dae4a-286c-3b36-a3b2-08b21a47f3ad | -23.5226 | -47.859 | 2025-08-01 01:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 52f913fe-6292-3919-a5fd-58e55f1d92db | -23.5242 | -47.8109 | 2025-08-01 01:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.6 |
| 4912ae59-57ab-3a86-85f7-692bdeca3011 | -6.7477 | -59.1909 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| bc41ac9f-f6a6-3dda-abff-c0eaafb8d47a | -9.3435 | -40.3307 | 2025-08-01 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 160.2 |
| f5a6f109-167d-385e-9f8c-bb2110da2b49 | -8.0321 | -43.1257 | 2025-08-01 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| b79f4636-ea83-30b3-94be-a983f99b7f8b | -7.7441 | -45.099 | 2025-08-01 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 130.2 |
| f6937c6d-c873-3da3-a092-fa35de6ea70f | -9.3626 | -40.328 | 2025-08-01 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 119.6 |
| e2471435-8f84-338e-884b-17ec9d3e83b1 | -6.7293 | -59.1916 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 1f1c174a-18a8-37fd-be89-e3fdd8115211 | -6.6376 | -59.0988 | 2025-08-01 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 48c37624-cde2-33c9-9e08-63391ddf8998 | -7.7255 | -45.078 | 2025-08-01 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e407516d-84c4-3704-95f7-a084269b87f4 | -6.7294 | -59.1723 | 2025-08-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 376.4 |
| ef41e1c6-47f4-334c-8d89-f9431b9833a5 | -23.5242 | -47.8109 | 2025-08-01 01:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 128.0 |
| 830f050e-b7d2-3426-b119-a57e59b28bb7 | -8.0321 | -43.1257 | 2025-08-01 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| b58a6be2-9391-30de-8842-6eb035986a86 | -6.526 | -56.1923 | 2025-08-01 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 37e7f271-fec7-36d0-94e0-f83b22ba589f | -7.7444 | -45.0762 | 2025-08-01 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 093871cf-5250-3375-adc4-6748ebfd8ab9 | -6.6143 | -59.9848 | 2025-08-01 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8d8c546f-b211-3a45-90b2-555591b8024f | -9.3435 | -40.3307 | 2025-08-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 160.1 |
| f00a3ed6-2114-32ba-afed-c543fd3b74a2 | -23.5446 | -47.8293 | 2025-08-01 01:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| cce67afb-4fc3-33e3-8e2e-116e2687025f | -9.3989 | -45.4928 | 2025-08-01 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8788fb35-cf0b-3355-b9cd-e158f26b141e | -9.3626 | -40.328 | 2025-08-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 178.9 |
| cf61bb5b-e579-3bf0-b06f-b4a8ab4d0167 | -9.4178 | -45.4906 | 2025-08-01 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 73b4c92c-d3c9-3854-b4a7-1725ba2831c5 | -6.7478 | -59.1716 | 2025-08-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 216.2 |
| e767b6c8-456f-3dd8-9cbb-cec632400ef0 | -6.5258 | -56.2121 | 2025-08-01 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| aa3924f9-9bce-3546-bba4-cc73af99f09a | -7.7253 | -45.1008 | 2025-08-01 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 58dc1ef4-d1c4-3b60-956b-8e2de06a53ac | -6.5443 | -56.2113 | 2025-08-01 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 6d55b4bf-7f72-34ee-a93a-32fe8fde9757 | -23.5226 | -47.859 | 2025-08-01 01:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.6 |
| 20780889-6b98-3c3a-890d-89716e5792e6 | -6.5445 | -56.1915 | 2025-08-01 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| eb2e3347-1286-398b-88d6-169e06154127 | -6.5629 | -56.1906 | 2025-08-01 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| df990791-d967-37c7-9f1c-42071b040f0c | -6.7295 | -59.153 | 2025-08-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| ab89d78a-2f0d-3a6b-ad73-ecb3ec85a748 | -23.5022 | -47.8407 | 2025-08-01 01:40:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.0 |
| 5a49fc0e-6b7f-30a8-82ec-7858a29c61b4 | -7.7441 | -45.099 | 2025-08-01 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| e76e12bb-e38b-3321-aaff-07adf875965c | -8.051 | -43.1237 | 2025-08-01 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 57660d02-38d7-3a63-a8d5-6080b32b7217 | -23.5234 | -47.835 | 2025-08-01 01:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 418.9 |
| 1ef078dd-674c-3ff6-81ff-6de6d1b29c76 | -8.0513 | -43.1001 | 2025-08-01 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.5 |
| bb790ba9-1239-354e-a5eb-d7b5ecafd979 | -6.5074 | -56.213 | 2025-08-01 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 923697e0-a2c0-35c6-9a48-82c12d959de5 | -6.7293 | -59.1916 | 2025-08-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 4dd82569-319b-31d2-a491-a710c74b503c | -6.748 | -59.1523 | 2025-08-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 88b24e19-e462-3754-a477-9821f7478d95 | -9.3439 | -40.3058 | 2025-08-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 122.2 |
| 20b38f5c-4114-3c74-bbea-55f088b667ef | -9.363 | -40.3031 | 2025-08-01 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.9 |
| fa4b08b0-485f-34cb-804a-992689b55919 | -6.7477 | -59.1909 | 2025-08-01 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6106e5a2-fdc9-37e9-aaf8-8fefa1c6595a | -8.0324 | -43.1022 | 2025-08-01 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 3f42213a-408c-3b70-a603-25280f985dbc | -23.5242 | -47.8109 | 2025-08-01 01:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.8 |
| b93d30cd-79a5-3093-b6c0-5ad568714413 | -20.7109 | -44.2727 | 2025-08-01 01:50:00 | GOES-19 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| b931e361-ab67-37e7-a912-aaa08f6c2bc9 | -6.7478 | -59.1716 | 2025-08-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 213.1 |
| b78cdf17-072a-3699-821d-98b23df34e02 | -6.7293 | -59.1916 | 2025-08-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.6 |
| ddc4aed3-9c19-31cd-81ed-499985bc8643 | -7.7255 | -45.078 | 2025-08-01 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 54a11d66-b9c1-31d2-aa73-c6705a4eef1a | -6.7295 | -59.153 | 2025-08-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 4fb76bb3-5c9c-3245-9c98-cf2ec1fac843 | -6.7294 | -59.1723 | 2025-08-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 327.8 |
| 1cf51b36-5ffd-3372-875b-e28130f15313 | -6.748 | -59.1523 | 2025-08-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 6b575c59-c0ac-3846-81f5-ff6a254358bd | -8.0513 | -43.1001 | 2025-08-01 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.3 |
| 27020f4e-3021-3c75-97d1-60b8e78f34a3 | -23.5234 | -47.835 | 2025-08-01 01:50:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 389.5 |
| c17430cd-7a18-31c2-878a-f80acb2147f7 | -7.7441 | -45.099 | 2025-08-01 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| be33c775-e888-3e69-a2de-6ac5f625e324 | -23.5022 | -47.8407 | 2025-08-01 01:50:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.1 |
| 483c334d-198d-3979-8314-7e2db6795df4 | -8.3396 | -50.5652 | 2025-08-01 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a8489728-8f74-3547-93de-064cfd1cd0ac | -9.363 | -40.3031 | 2025-08-01 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 17f72790-d602-3feb-97ff-4fcdfb22831f | -9.4178 | -45.4906 | 2025-08-01 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| f339725b-b4a4-398b-bf5c-fbdd90f7513e | -7.7444 | -45.0762 | 2025-08-01 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 3700b6f7-ac0c-3398-b7a4-3d3d95a3b524 | -9.3989 | -45.4928 | 2025-08-01 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 108.9 |
| bd066495-55c2-33f0-91d5-50b9e4eef943 | -6.7477 | -59.1909 | 2025-08-01 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 2876f932-669c-3784-8d8b-53742b8ec7db | -9.3626 | -40.328 | 2025-08-01 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 105.6 |
| 239fdea7-5208-316e-a97f-5147cd172115 | -8.051 | -43.1237 | 2025-08-01 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 133.6 |
| 3677f72c-5a8f-36cd-a335-21a5d01fadca | -8.3394 | -50.5863 | 2025-08-01 01:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| be589e87-5255-30cf-8df7-40116e4557a6 | -7.7253 | -45.1008 | 2025-08-01 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0cc52c86-98a0-3388-bd75-3652355e4036 | -8.0324 | -43.1022 | 2025-08-01 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| fb2f694b-0896-3e70-9ace-0bde3e9d94ef | -8.0321 | -43.1257 | 2025-08-01 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| 868f5f53-e01a-34b7-b94f-9d2319201d60 | -6.6143 | -59.9848 | 2025-08-01 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d8d73701-062c-3f86-a786-73727e7a8501 | -23.5234 | -47.835 | 2025-08-01 02:00:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 283.2 |
| 1b479156-1c01-3af5-a026-c730c31d9742 | -6.7478 | -59.1716 | 2025-08-01 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 205.1 |
| 84f83f29-03d7-3967-8cb3-79968d5ed186 | -8.051 | -43.1237 | 2025-08-01 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| bf467c92-6a54-3e91-834b-741bbabec7b1 | -6.5629 | -56.1906 | 2025-08-01 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ef246621-576a-3b3f-bd85-0a708825121b | -6.7293 | -59.1916 | 2025-08-01 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.0 |


[Clique aqui para ver as próximas entradas](README7.md)
