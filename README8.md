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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 767abd7d-2882-388c-88eb-daa13530d028 | -5.7571 | -45.0613 | 2026-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c5f96444-0d11-38cb-8337-f68189bac22a | 0.2667 | -51.4597 | 2026-09-10 00:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 725b1083-88eb-3f66-8068-9794ec8a1cf1 | -5.7758 | -45.0599 | 2026-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 04fd4bb2-3f7a-378b-99c5-04bc52fd9b07 | -10.7582 | -45.9397 | 2026-09-10 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 8ab2457b-7b53-3127-9e02-88fcf55eba6e | -2.7331 | -57.6271 | 2026-09-10 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.4 |
| b218cb42-1b78-3719-8476-9fb15a332590 | -5.7569 | -45.084 | 2026-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 408.3 |
| 6d321968-6538-3f2c-97a2-d02c0ceb179f | -6.5452 | -62.9102 | 2026-09-10 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 200aae41-0c87-3564-8038-8ace1a9403d8 | 0.2667 | -51.4803 | 2026-09-10 00:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 39eec33d-1cf5-37ae-844a-11719f30fc15 | -7.4976 | -45.2814 | 2026-09-10 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 14e7c407-b423-3d45-afcb-0ce149b05102 | -6.5636 | -62.9096 | 2026-09-10 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 459c9ffb-11d5-38d1-9531-06dba0961825 | -4.3772 | -47.7844 | 2026-09-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7514edb3-def3-3b83-a536-42a6fb20aae0 | -4.3587 | -47.7853 | 2026-09-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 98a13ebc-d406-3028-9a98-5895071528bc | -20.5381 | -57.459 | 2026-09-10 00:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.3 |
| 31029037-6c59-395b-ab48-89560f4970d8 | -5.7567 | -45.1067 | 2026-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| e66aac2f-4c01-35f8-8e23-e0c659f3667a | -6.5453 | -62.8914 | 2026-09-10 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 213.0 |
| 2f1ccb54-4be6-33e7-bcdf-b6adc136fdc8 | -5.7756 | -45.0826 | 2026-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 529.4 |
| f01b341a-2c1a-3b86-abb4-4268d3d1b151 | -5.7754 | -45.1053 | 2026-09-10 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 53913062-f43a-39b7-8944-06d2a00064dc | -2.7331 | -57.6271 | 2026-09-10 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 1fadb89a-ec4d-37ef-b2a7-3e2d808ba722 | 0.2667 | -51.4597 | 2026-09-10 00:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| b568cd35-36ad-3f87-b06a-15098be9db7c | -10.7582 | -45.9397 | 2026-09-10 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 18b3b684-006c-3eeb-b96d-05e3d6f7a557 | -5.7758 | -45.0599 | 2026-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 2aaba952-5a5c-3263-9996-96f28f5f9271 | -5.7567 | -45.1067 | 2026-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 3fb64354-43a1-3e65-85b1-66d333b45799 | -6.5453 | -62.8914 | 2026-09-10 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 5aa2392e-aa9a-3f73-ae02-d33c96b2bf1d | -6.5637 | -62.8908 | 2026-09-10 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 1896aaa8-b63f-319a-89d1-893a0e76bfbc | 0.2483 | -51.4597 | 2026-09-10 00:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ea3d2454-38a0-3ce7-a99e-cee843a3de03 | -6.1726 | -44.6432 | 2026-09-10 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1f4700f8-cde2-3553-a209-9bb1d944c4e6 | -5.7756 | -45.0826 | 2026-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 364.1 |
| 82a69426-8b0d-3300-bd62-faa18b58f75a | -6.5452 | -62.9102 | 2026-09-10 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 34256ae4-96e1-307d-98d2-25c8eb3544f0 | -7.4976 | -45.2814 | 2026-09-10 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 2ddd9803-ddb0-3372-a49e-c7210ba63dc0 | -5.7569 | -45.084 | 2026-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 581.9 |
| 3b47cc1b-7ef0-37ab-8f78-24da66179a0e | -2.9391 | -50.4832 | 2026-09-10 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 4214927f-b63f-3119-b1b5-dd9bf8a7a226 | -5.7754 | -45.1053 | 2026-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e303e629-272a-3595-8338-d48e9d306b31 | 0.2483 | -51.4804 | 2026-09-10 00:40:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 8c196f24-9dac-34d4-b061-00cbed0d6fe0 | -4.3587 | -47.7853 | 2026-09-10 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 23e91a0d-b1aa-3e51-a39b-b7de2a68f856 | -20.5381 | -57.459 | 2026-09-10 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 440ee17e-c2db-368b-88e6-a668e62b620e | -5.7571 | -45.0613 | 2026-09-10 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a7e5ec72-ff83-3d1d-a383-0c3011fc5e2e | -13.4453 | -43.8366 | 2026-09-10 00:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| f9d1e75e-adda-3b94-8843-7e610d6593d4 | -4.3588 | -47.7636 | 2026-09-10 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3dce8a54-59c6-3a35-8879-1ee5fa24bec8 | -6.5453 | -62.8914 | 2026-09-10 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7de23e94-6479-32b8-9bbb-931167fe61d1 | -4.3587 | -47.7853 | 2026-09-10 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 7f0b0369-47cf-37a2-95f2-74c04d90c2eb | -7.9837 | -43.9719 | 2026-09-10 00:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a87ececc-5e9c-3c62-9fed-89912d68d84a | 0.2667 | -51.4597 | 2026-09-10 00:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 56.0 |
| eb1c5446-7529-3e31-88d7-9b577d1e0ce4 | -10.7391 | -45.9422 | 2026-09-10 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 70ab4af1-2af5-3421-81c9-c0daa2aa1425 | -5.7569 | -45.084 | 2026-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 420.3 |
| 173e5e01-6492-3ebe-957c-24ee32ecc006 | -5.7754 | -45.1053 | 2026-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| f09934f1-0c52-31b5-b3bb-da4b725f8d5f | -13.4453 | -43.8366 | 2026-09-10 00:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 91e69e8e-19dd-31b9-9705-4b40f079c8d2 | -5.7571 | -45.0613 | 2026-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 7ba6cd4a-e560-3eb2-82f3-740ce195d9ed | -2.7331 | -57.6271 | 2026-09-10 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 0495937e-78e4-3014-be21-6384c32b1995 | -5.7758 | -45.0599 | 2026-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| ad819b9b-7c41-3d26-a4f0-25ceabb20dab | 0.2667 | -51.4803 | 2026-09-10 00:50:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6f9a81b6-7859-3f42-b5ce-f68e976f9a28 | -5.7756 | -45.0826 | 2026-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 426.8 |
| 062e8558-5fc9-339a-a7c2-896ea21c51a2 | -5.7567 | -45.1067 | 2026-09-10 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 3c60f8f0-e8d6-327a-946f-014f645920fa | -2.9391 | -50.4832 | 2026-09-10 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 35fa3e97-570c-314c-9b42-49a2e602068a | -10.7578 | -45.9624 | 2026-09-10 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| aa34f295-621d-3bad-8ac4-8a05dab27b6a | -10.7582 | -45.9397 | 2026-09-10 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 3487cef7-de72-35ba-b233-a6a683506e48 | -5.7758 | -45.0599 | 2026-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| a7341997-77f8-3993-b8d5-7c7c4a99fa71 | -20.5381 | -57.459 | 2026-09-10 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.5 |
| d330b8bf-4fe4-324e-8bec-e1c9fb961930 | 0.2483 | -51.4597 | 2026-09-10 01:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 86dfd3d4-4594-3458-88e2-4175e772167d | -10.7769 | -45.96 | 2026-09-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| d90736d1-04a4-33a0-a7d6-2ace59c8399a | 0.2483 | -51.4804 | 2026-09-10 01:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 77.6 |
| fec9985c-dffe-3b3d-98db-f5e30f113e09 | -6.5453 | -62.8914 | 2026-09-10 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 70321e9f-0238-30d2-a821-2f3a1d0cc2ea | -6.5636 | -62.9096 | 2026-09-10 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 996d6208-04fa-30e6-be12-ce579af508d6 | 0.2667 | -51.4597 | 2026-09-10 01:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 974ceaba-b796-3ceb-9e18-b5487d9be85d | -13.2293 | -61.6772 | 2026-09-10 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 88b90709-680a-33a0-9021-963cd5eadf8d | -7.9837 | -43.9719 | 2026-09-10 01:00:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 841aae4e-6abb-3df8-b934-d7211412c260 | -7.9834 | -43.9951 | 2026-09-10 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1d23b3d1-0e27-336d-a5c8-1268407dbcc4 | 0.2667 | -51.4803 | 2026-09-10 01:00:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dc0512b9-16a0-3edb-b405-67640485f375 | -4.3772 | -47.7844 | 2026-09-10 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fe088757-903d-34c1-beaa-7106f297f95d | -5.7571 | -45.0613 | 2026-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 1380eafe-09d9-3ebc-b1dc-f4d351ed1070 | -13.4453 | -43.8366 | 2026-09-10 01:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b6eae9e2-3b12-3721-b84f-5f6a5b286132 | -6.5452 | -62.9102 | 2026-09-10 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| bc88f4f7-49c5-3684-9142-91576edcda61 | -5.7567 | -45.1067 | 2026-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| e80b2310-1e5d-3201-a37b-41542b24c2e2 | -10.7391 | -45.9422 | 2026-09-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 22afcd9b-d1bf-3e70-bdfc-d7685cd14d75 | -2.7331 | -57.6271 | 2026-09-10 01:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| babebb86-4168-3a51-a256-e67011118d24 | -10.7582 | -45.9397 | 2026-09-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 257.8 |
| 1becf3c4-23d6-3517-ad77-18a83ec981b0 | -5.7569 | -45.084 | 2026-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 342.2 |
| dbf687d4-2136-37d3-a6f9-1ae133123a62 | -13.2297 | -61.6384 | 2026-09-10 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a2183e76-c1e2-3a07-92e7-df0b12e20f4a | -6.5637 | -62.8908 | 2026-09-10 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 73e634ba-aa58-3749-997a-380888233cce | -13.2295 | -61.6578 | 2026-09-10 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 188.2 |
| 1ceba593-285a-3d84-8e81-6d63b2024737 | -10.7578 | -45.9624 | 2026-09-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.2 |
| f1f8d433-e91f-37c0-a168-5e01bf04acfc | -5.7756 | -45.0826 | 2026-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 402.4 |
| d66f98df-cbca-3c04-baad-de97a14aceb0 | -20.5377 | -57.48 | 2026-09-10 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| f4d1f577-288e-3ec4-b067-a91b5be85fe6 | -13.2677 | -61.6358 | 2026-09-10 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 3d9b8b28-aba4-3bd3-9590-aac2a9d1ca7c | -13.2678 | -61.6164 | 2026-09-10 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| e8dc30ac-567f-37e5-b5e0-7b2f6507b683 | -5.7754 | -45.1053 | 2026-09-10 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| deaa3087-75ba-3304-95c7-4fe34728299c | -10.7772 | -45.9372 | 2026-09-10 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 751513c0-2e1d-3e6b-b2ce-20997d0777ce | -4.3587 | -47.7853 | 2026-09-10 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 72ac53f3-ea45-3824-963b-bc0c4b4e0c0a | -7.9837 | -43.9719 | 2026-09-10 01:10:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 5c2d5122-0e25-333e-8904-22b36e0aa26b | -5.7567 | -45.1067 | 2026-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| f6209d02-f6af-3652-bae6-bb9484c98f84 | 0.2483 | -51.4597 | 2026-09-10 01:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 13565c7b-11b5-34c9-82fb-1a0bc77b72d5 | -6.5452 | -62.9102 | 2026-09-10 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d28b0b11-d39a-37ea-bf1c-9c312373700c | -13.2485 | -61.6565 | 2026-09-10 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 942a151a-0c7e-3b8b-b611-51dc47c60010 | -5.7571 | -45.0613 | 2026-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ef050f60-3d6b-388c-b3cf-761a6c8d02f3 | -2.7331 | -57.6271 | 2026-09-10 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| cc750c24-fc97-3846-acae-bc10155b2696 | -13.2293 | -61.6772 | 2026-09-10 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0a50f9b7-e456-3026-adfa-0881040448b6 | 0.2483 | -51.4804 | 2026-09-10 01:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5d84f98b-5174-3237-a702-599d2413e91c | -13.4453 | -43.8366 | 2026-09-10 01:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f18526af-33b7-3b90-b463-3e3476c9dd1b | -5.7758 | -45.0599 | 2026-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 69fc5239-9237-3383-9415-828f5a969424 | -6.5453 | -62.8914 | 2026-09-10 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 318461d7-75a7-32ef-bd78-8bc37249c1cd | -5.7754 | -45.1053 | 2026-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |


[Clique aqui para ver as próximas entradas](README9.md)
