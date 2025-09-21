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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 809a3120-4454-3db2-9299-d20e68b46c0c | 4.32759 | -60.73845 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5a21089c-256a-3cd9-ac64-c1dbfd39ba81 | 4.32806 | -60.74166 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| baf6812d-a36c-3d88-b413-aecaf9811e9d | 4.33381 | -60.74405 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c27ce87-67e0-3d87-83f5-a1fd1d754c95 | 4.33235 | -60.73392 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0804658e-4c2f-3ef5-b207-33fbf81cd345 | 4.32901 | -60.74831 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31b59272-5650-3e26-b3fd-0c0e25265993 | 4.33333 | -60.74069 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 516bd2a9-7a4b-3bac-bc89-3fc138923561 | 4.32713 | -60.73524 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b68a86ed-ba40-388c-b2b0-7f4daf95ba4f | 4.33431 | -60.74748 | 2025-09-21 04:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74043aea-28a2-35c9-911d-ef5045d628cd | -3.3701 | -50.39434 | 2025-09-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ff220ed-63db-3942-b0ea-d272d1fded5b | -6.17056 | -43.69134 | 2025-09-21 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0c04f508-f47e-357d-9524-c21f459a37ac | -3.35131 | -48.39409 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e96b47a7-410a-3cbd-b288-876e7f745f37 | -3.83492 | -50.77533 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d98ea6c-cdc1-3105-a82f-a85d748ebfcb | -2.73362 | -49.54896 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecaef223-c1f4-3725-9853-27c5e56dedd1 | -7.92556 | -44.10263 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24f3c851-56c2-34e8-a469-900f21ce309e | -6.19083 | -44.05684 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d9cf9a0-169f-3c87-817e-24bc313d58d5 | -3.30737 | -48.71621 | 2025-09-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07eef587-00f3-342d-b591-d4548b2db906 | -2.62427 | -46.83878 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a3b73b0-ef9b-3f6c-8b48-2fd564bf4b7c | -2.14367 | -53.64852 | 2025-09-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aaeaa1c-6af8-3496-8713-301f3da655bd | -2.74331 | -49.55246 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c043e04d-0b3f-318a-bacd-b03a1e54e73e | -6.31688 | -42.37403 | 2025-09-21 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3776fec6-d69c-3b25-954d-4e91acb0974e | -2.30682 | -48.14938 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dbe71b96-8b77-3c7a-a4da-8913993ea4cb | -5.56633 | -42.14882 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d44d1c06-6fd8-3761-9b23-711170accc59 | -5.69168 | -51.75411 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57d70e6e-fa32-3fda-a89e-2f6c157f1ef5 | -6.31122 | -42.36824 | 2025-09-21 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e7d59a0d-8543-34ae-9bb9-61b04abaf96c | -3.29879 | -51.60413 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a75d7b2c-af68-395b-bf80-e421c7d54ef9 | -2.8323 | -48.65522 | 2025-09-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12e55595-82f1-3942-895b-99101db8d5c2 | -2.7321 | -49.55074 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46701443-6a15-3b9e-87e7-d68fb20b20a9 | -3.49123 | -53.26786 | 2025-09-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4b79f880-f41f-3cdb-b701-a3015fdadb4e | -5.63586 | -45.9544 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5b009270-6e6d-3d5a-b516-58d1de5277cc | -1.12461 | -54.14508 | 2025-09-21 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a015d7e-1320-3725-a61a-8f662b7562f5 | -3.3559 | -48.39108 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6e7eaf1-f4d1-3dff-bd37-f143b73395c1 | -5.5704 | -42.1502 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bd4d3639-bd2d-3082-8e06-7156c6db90b5 | -6.94178 | -44.76059 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1cd1841-d7f6-340f-976d-2d26a6e5b7b9 | -2.74483 | -49.55068 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dc0fbb5-564b-3e75-8f9d-03eff5888caf | -5.27574 | -44.81438 | 2025-09-21 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b9a77d9-31d0-3df5-b417-c85f7d5bfe47 | -3.35536 | -48.39471 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 340ebb21-afe7-3278-a0df-d0936ddaa243 | -3.65243 | -58.16564 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 408cfc0f-6ac4-3ab3-afff-3ef8454b895b | -5.52241 | -43.87059 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 66196620-23b2-3c4b-abc3-90a760215fef | -4.46421 | -44.13736 | 2025-09-21 04:55:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4db28c94-5618-35ec-85ae-f1332503f14f | -5.51995 | -43.86095 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e1f8a07-4897-3f17-895e-05fb413d270a | -2.80797 | -58.34579 | 2025-09-21 04:55:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4745dddd-e5f8-3bd2-a476-032de78b934d | -2.74415 | -49.55515 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eeb12071-05b5-35dc-ba24-f243367d77bf | -3.59539 | -43.91687 | 2025-09-21 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 637d4c61-a33a-3522-aa5a-24588a0393e8 | -2.60778 | -48.13956 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a38e57f7-ec40-3394-b205-21e5f16dd99a | -3.8057 | -47.57114 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edb5688f-c3e4-322e-98e5-86ff16ee6293 | -1.40017 | -50.58949 | 2025-09-21 04:55:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d5e2454-7628-356f-af59-aab3f200bd1d | -3.20303 | -51.58977 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66beec05-441b-388a-9fe2-cfcf9a35b641 | -7.38406 | -47.04049 | 2025-09-21 04:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b7ca9534-1828-3f40-ac90-5695d128a815 | -5.69113 | -51.73454 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 717307bf-337d-3e1d-bf4c-65589c6adaf0 | -5.52506 | -43.86597 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6678ab76-bdd9-3438-b767-8bb1bceff835 | -5.75577 | -44.1953 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b7dba3a-718d-383c-9755-c0b10a842a05 | -7.48018 | -46.66381 | 2025-09-21 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa285cd1-c63d-3e8c-91a5-92a19535a01d | -5.57977 | -42.14531 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 1c93cee1-137f-308d-aa53-70eedc7db499 | -7.41533 | -44.54597 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09e836cd-1db5-3d04-8319-4f6d639310f1 | -3.36186 | -48.40663 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c243d1f0-470a-381a-8382-a16fd0e96235 | -2.69435 | -59.42855 | 2025-09-21 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a45dc152-265f-3753-aaf4-79ef6adff9aa | -2.61429 | -46.85163 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2edba2cb-169e-3aef-9a65-60ffd6102129 | -5.47414 | -45.37817 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74045724-5c27-310f-8189-89bb7cfa05a3 | -5.8263 | -49.91805 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40a9a2c4-712e-3780-bcdc-70cfc92b7bc0 | -5.79534 | -50.20193 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d734383a-6fd6-31c9-9ee7-1618993a5ab5 | -5.63669 | -45.95578 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 450b35b5-eeef-328a-ac0c-9033ac883790 | -3.34727 | -48.39346 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8a9e0a5-c894-32a4-9e28-030c294c3b2f | -5.69226 | -51.75032 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28b3c2e5-5b51-3ef6-8845-6357ea42e3dc | -7.91284 | -44.10934 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c96c63a8-7296-3ccf-9942-06761ecc0775 | -3.33001 | -52.54384 | 2025-09-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fdddb22-1def-3161-875b-91ae215be778 | -7.59992 | -45.49649 | 2025-09-21 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d716799-7190-3c7e-9761-f80429f88db4 | -3.3478 | -48.3899 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ce45fc9-1081-32f5-bf71-3dce1c104229 | -5.75522 | -44.19915 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 939359e5-c9b5-35a2-b542-38951cb498f9 | -4.79678 | -47.28376 | 2025-09-21 04:55:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01a11b62-1358-3909-a1a3-c84cc08716cf | -6.01747 | -44.33105 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4ae83cc-a708-398a-a60f-f14310c2d5dc | -2.61788 | -46.85111 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d69418c5-f93c-3194-a575-c9b9384da097 | -2.61983 | -46.83804 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b75c847-9e68-377a-b02d-76b9bb485445 | -3.35078 | -48.39766 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd54f1af-1f36-3e35-be52-3096e278c12a | -3.9825 | -51.05954 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3254caa3-561d-3968-a125-34ea7ef6e271 | -2.80684 | -58.35272 | 2025-09-21 04:55:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1acb77e5-6fb3-33e1-bf1b-f3f1c73f1a91 | -1.75388 | -47.1763 | 2025-09-21 04:55:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 453d1ab3-4030-31f1-a401-a251ca15db5f | -3.53828 | -49.9853 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aadcb273-6746-3093-83d9-ff5d9dde2b3b | -5.01241 | -45.20354 | 2025-09-21 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e820e96-5e86-3ac4-8739-67932a019e9f | -5.99937 | -43.94156 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1693046c-1387-3d7d-87db-2d57388c8483 | -3.64515 | -58.16286 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 74e148b8-b1fc-3e5b-b9f8-0552cfc23e37 | -3.59558 | -43.91727 | 2025-09-21 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0061e1-9e5e-36d5-a387-32f41103fe5b | -5.5194 | -43.86495 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0ef190f1-f06b-35c4-aecd-cf9f6d225eb5 | -5.82979 | -49.91649 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7b5ed36-9f79-3abc-b377-7d1b1f39a314 | -5.51674 | -43.86963 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9f93d5bc-2b2f-3289-8d74-fcc2ec959355 | -5.52476 | -51.44995 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 733e31ea-9136-38c3-b06f-4ba4b298be85 | -3.34685 | -48.39354 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff44a22b-137e-3077-bb6f-b50895d78218 | -4.70979 | -46.47216 | 2025-09-21 04:55:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5645fa86-359f-351f-8e95-ce9d20122c68 | -3.59527 | -47.5188 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91f19ba7-de07-37bd-ba6f-fe0b5b9056ed | -5.62734 | -51.69815 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 707b9c63-2cbd-3a4b-a207-6bf9b5afe43f | -0.95174 | -47.35628 | 2025-09-21 04:55:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa0d35aa-740a-3382-bbed-906efd769974 | -6.733 | -46.53602 | 2025-09-21 04:55:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c632ab79-9a71-3955-84a9-8a2b4b8323dd | -3.30289 | -52.58614 | 2025-09-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6922c1f2-64bf-3932-a75a-33c2721ef216 | -5.60228 | -51.48925 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef11114-1f15-32cf-b147-f6be8ea46688 | -6.30499 | -42.36657 | 2025-09-21 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 198fd6d1-6d97-33fc-9c16-ced7560e5f2f | -5.63173 | -45.94809 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 201d2c75-bc5a-331f-bcb7-8e526f8079dc | -5.58928 | -51.19335 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc1a2610-9244-3dad-aea6-f716e726b669 | -6.01188 | -44.33046 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2fbfa860-970b-34de-828d-8feb9ae0ea09 | -4.32905 | -48.38749 | 2025-09-21 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38161d76-605c-3882-b037-43099700824e | -7.59506 | -45.49279 | 2025-09-21 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13f0f011-a5a5-3595-8743-a5a26cb310d7 | -2.74177 | -49.54563 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README34.md)
