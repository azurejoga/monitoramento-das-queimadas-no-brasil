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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee97416a-f0f0-3da2-a112-5674a1596745 | -6.74122 | -42.94823 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 28fae74c-90cd-3352-bbb6-0d97f038e02f | -7.97456 | -42.27686 | 2025-11-17 03:46:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 29a07a23-3a73-3a2a-b708-532da054ee2c | -4.09944 | -48.02777 | 2025-11-17 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f06d85dd-37d7-35d4-b557-f430ae3639c6 | -4.4073 | -45.83854 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e9ab6f3-01cf-3651-abe9-4421299356ba | -6.90578 | -46.46437 | 2025-11-17 03:46:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54a5b6cd-14b8-3a07-b6a6-826f6a1cda05 | -4.65342 | -46.90118 | 2025-11-17 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ee863f8-0137-3608-8254-e72cbb665619 | -4.05704 | -47.49968 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7e5f90aa-0386-31e5-bd75-54bd47acc47e | -7.00962 | -39.19297 | 2025-11-17 03:46:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 64b5d371-b8df-39e3-97e7-bba566155891 | -4.01665 | -48.81946 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| add782b3-110f-3126-8aa8-fc96c9635854 | -3.30391 | -50.08265 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc9cbef2-0322-30a4-b19b-52c35cf72525 | -8.11743 | -43.53888 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2684b91c-3cc7-3e51-b141-784df1fe7e54 | -5.76141 | -42.51125 | 2025-11-17 03:46:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 302139ca-4280-3e43-923d-1cd63d21ecf3 | -7.36852 | -45.83238 | 2025-11-17 03:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b163c711-0d9e-3cca-a8e8-2a406235a7a8 | -6.35803 | -46.15589 | 2025-11-17 03:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e5eee4e-5043-3740-87fa-6db8e906615a | -6.94031 | -41.53453 | 2025-11-17 03:46:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8fc62ec-e3b2-3a4b-b104-49b5ef1038b1 | -7.21545 | -47.98729 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 51dc2f53-2bf8-352f-9d56-12a97028fbac | -6.85574 | -42.86059 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 98c23b69-a423-3382-9f58-3733c9a30636 | -3.77469 | -47.74992 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a3c8201-d2c8-3205-adc9-bc53b2b1b3d4 | -4.69569 | -46.306 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d88d8e58-c1ec-3bf7-9353-ac6b111ce701 | -6.34378 | -44.22726 | 2025-11-17 03:46:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9122e0d6-2ded-337c-a08e-de54b3a57ebd | -4.40789 | -45.83511 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f79b494-102e-3f19-89aa-f285cf32f7ec | -7.2541 | -48.01248 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20f68265-4b7e-39a5-8401-a0829afded02 | -6.67582 | -42.05478 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 134328de-89b3-38d7-9e84-6ef5bd60e2d8 | -4.65439 | -46.54845 | 2025-11-17 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| baf68459-8c49-365b-a917-41d7482284d5 | -6.35154 | -41.75174 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6898fb86-be4b-386c-b409-721fff2dda6c | -7.37015 | -43.31167 | 2025-11-17 03:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d111b0c-e8c2-3903-88ec-d03fc69a5858 | -4.25334 | -46.41466 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b6989bb-6d21-358c-881f-b01308022a10 | -6.33924 | -41.79351 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0fb0a8d6-c073-3281-8df2-6f4152d770eb | -7.09982 | -42.72807 | 2025-11-17 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d8d02567-d262-3b56-b454-dad1bfb3844e | -6.14135 | -41.70211 | 2025-11-17 03:46:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2a844586-5815-3739-80d1-3ce041c14a58 | -5.54253 | -41.76703 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4bb9ab0-3533-3052-b28e-a635bf765573 | -6.78841 | -39.56663 | 2025-11-17 03:46:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 44851340-3d96-33cd-a61b-543c09674dc4 | -8.24395 | -40.86733 | 2025-11-17 03:46:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fbd43342-9037-381e-ba9d-c8cb7660ade8 | -8.80749 | -40.40483 | 2025-11-17 03:46:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e69a2fd5-d425-394c-b558-11a53632447d | -7.13287 | -47.1335 | 2025-11-17 03:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cfa1ea0-54d1-37a0-8b07-301d77680b23 | -4.25595 | -46.41182 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b2ef501-5098-3a14-ace2-0183b8f76cf4 | -6.39805 | -42.28779 | 2025-11-17 03:46:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1dd6b335-6990-3612-802d-5e64bfbe1b56 | -4.40242 | -45.83426 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8edea135-7421-3515-880e-bd74872af46f | -5.34315 | -43.04358 | 2025-11-17 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f449efd2-b5d9-377c-85fa-abad50918d86 | -4.65572 | -46.55149 | 2025-11-17 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c96a6adc-7f97-341f-9cb6-06b22e644dcd | -7.13513 | -47.13273 | 2025-11-17 03:46:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22bf5e52-3b61-3f43-b3a3-7ec59ca25606 | -6.6226 | -41.46249 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39e892ef-90ea-389c-98c0-6c004c556214 | -6.71173 | -42.93907 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 09027ecb-e0d6-3e88-acb3-2e3dbc9df733 | -4.25896 | -46.41595 | 2025-11-17 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75ffb38e-6103-3922-83f0-ac48a3f27cc2 | -4.07201 | -46.20115 | 2025-11-17 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a838ad99-08a4-34c6-90a8-73c3597ff7fd | -6.81721 | -39.14777 | 2025-11-17 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 36b0f6d9-60b8-3e33-97ec-91d22fba5347 | -4.86655 | -44.62661 | 2025-11-17 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ff34ec7-230c-3f18-88f8-3c14c2ec4dce | -7.62168 | -42.57664 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ce1cd71d-5e3a-3347-971c-bf2b45fbd267 | -7.70864 | -42.94954 | 2025-11-17 03:46:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 50c0e69f-c8ef-34fd-b85b-b4efc8719ba2 | -3.29674 | -50.08126 | 2025-11-17 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fce1835b-9ad9-3057-b9d5-4f86d778ab72 | -7.2184 | -47.99289 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e3ef8d22-ab83-3534-b1d0-f8f956413e83 | -6.34288 | -44.23258 | 2025-11-17 03:46:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d97dc02b-8cd6-366e-a0d7-6dad0a658fdd | -4.99426 | -44.36013 | 2025-11-17 03:46:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 914068da-01e4-3840-9872-3bac23c5bb88 | -6.65698 | -39.28801 | 2025-11-17 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 67572f73-a474-3def-b513-b2cc4630effc | -7.21413 | -35.77767 | 2025-11-17 03:46:00 | NOAA-20 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4bd721a2-6ce7-393e-8db0-1fec1074c8a6 | -5.97677 | -37.83138 | 2025-11-17 03:46:00 | NOAA-20 | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ba5948f-dd17-3796-bac4-4960cfb1eadf | -4.40123 | -45.84118 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26425dc4-6b73-3b01-9738-1677d08777b1 | -7.49032 | -45.87498 | 2025-11-17 03:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df9b7a87-4cbc-347f-a69e-875a86e80331 | -4.01107 | -48.81236 | 2025-11-17 03:46:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3afe56f-41cc-31a8-8e2b-6f81392545c1 | -6.77541 | -39.99722 | 2025-11-17 03:46:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 16f4ffd6-45c6-30f2-bb6e-7d73d018b03d | -4.4067 | -45.84202 | 2025-11-17 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c25346f1-cfc4-3845-8662-2f03382a3419 | -5.88644 | -43.97433 | 2025-11-17 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8abe8b8-6dd5-3fd2-865a-6620dd2e3b72 | -4.99914 | -42.42677 | 2025-11-17 03:46:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c97d412c-8da1-3f1c-b584-c677e0cbe0cb | -4.0932 | -48.02627 | 2025-11-17 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bff778c-b76a-3259-8cfe-596189d8df10 | -4.42002 | -45.55494 | 2025-11-17 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7389df49-9124-35fe-a526-36de1bc13201 | -6.91126 | -46.46516 | 2025-11-17 03:46:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1adc585e-3fb6-3fa6-a6b6-07d4f9843116 | -3.83467 | -49.81652 | 2025-11-17 03:46:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b2fcd21-4c56-32a8-bc5e-2002462f9ef0 | -6.36128 | -46.15026 | 2025-11-17 03:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62c6e9d4-1304-33a1-bf9c-03279276bf2f | -6.70461 | -40.79231 | 2025-11-17 03:46:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a8128b7a-6a1d-3440-b6ad-a08bf2603222 | -7.54863 | -42.51836 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0101c96e-c28b-3e61-8ec8-e97c105525c2 | -4.42056 | -45.55168 | 2025-11-17 03:46:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5bb4cd25-c726-324f-b81a-4b8e38f62b44 | -7.71083 | -42.18373 | 2025-11-17 03:46:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7bfc9045-e37e-3449-9df7-24dad24d5817 | -6.67644 | -42.05107 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7012aa0d-976f-3b23-86a6-f7a8a83fb115 | -5.41587 | -41.02709 | 2025-11-17 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3f449134-d4e3-3345-8f9d-dd568668725c | -3.77275 | -47.65002 | 2025-11-17 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a3950c2-9ec3-3486-bfaa-dba01466e1c4 | -5.6206 | -37.80433 | 2025-11-17 03:46:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| a111c765-b01f-3574-8bba-695d451c5b4a | -6.68174 | -42.04441 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1fb0066e-9bc2-3159-9b66-244269add5da | -6.93257 | -39.61667 | 2025-11-17 03:46:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 11812a3b-a10a-3216-876a-e44f0db51c12 | -8.121 | -43.54422 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9a2e087e-8f2d-3e54-b61b-3f4ad4014f98 | -8.11932 | -43.52688 | 2025-11-17 03:46:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b386638-6f47-3585-a2ff-83b9a542fc88 | -4.70969 | -45.10785 | 2025-11-17 03:46:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 546aae11-94f1-31ad-be4d-41e1a47a6b1d | -6.41642 | -41.46661 | 2025-11-17 03:46:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0debce35-58b8-3348-8740-ba39f81cfcfc | -4.93831 | -44.53931 | 2025-11-17 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a736ad83-c547-3d4a-a4ab-7415039db303 | -6.9332 | -39.6129 | 2025-11-17 03:46:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0e6a64e7-808f-394b-b218-30d8d5cce782 | -6.36016 | -41.74953 | 2025-11-17 03:46:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28f93dbc-4328-3668-a2cf-c4de0099dc5f | -5.93059 | -38.1204 | 2025-11-17 03:46:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b9daefb-f6c6-3f20-92bf-b212453a4be3 | -4.09571 | -48.03005 | 2025-11-17 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fdefbe9e-08cd-3dcd-9e54-f5512cfa7564 | -6.67768 | -42.04375 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 60c45f32-b6d6-34b7-a9d6-c6f389ae9c1c | -6.8472 | -42.85904 | 2025-11-17 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 004023d8-1107-3f2b-ad88-e3c30bafbd67 | -3.52715 | -49.10225 | 2025-11-17 03:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11225f0-f66d-35af-b230-86e124aa1740 | -6.41559 | -41.47147 | 2025-11-17 03:46:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b07f0d4-e2e5-39b5-98f9-adbb0e75ac90 | -4.86606 | -44.62956 | 2025-11-17 03:46:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3c92f94-320a-3bb4-a169-ee71191a62f2 | -6.36068 | -46.15359 | 2025-11-17 03:46:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bb75bc4-055b-30cb-8e87-883156a0e270 | -6.68235 | -42.04079 | 2025-11-17 03:46:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 16f20344-7784-39c6-a265-ebb7f07962df | -6.40764 | -42.33194 | 2025-11-17 03:46:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 788e7ba9-dc16-34ff-a852-b611af175600 | -7.54798 | -42.52209 | 2025-11-17 03:46:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 49a3d4e0-d637-31a7-b5e4-fcf371d93466 | -6.00205 | -39.88355 | 2025-11-17 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5a9516c9-3068-3d10-8252-6b107ab8cca2 | -7.21323 | -47.98722 | 2025-11-17 03:46:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47c04785-0d0d-392a-925e-8a99ed4051f8 | -6.4835 | -47.19196 | 2025-11-17 03:46:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7518395-3cd2-3485-bcf1-1de276f24a62 | -4.65642 | -46.54753 | 2025-11-17 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
