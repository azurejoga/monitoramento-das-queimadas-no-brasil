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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0be30214-4890-3411-adf5-d2aaa8ce341a | 2.42037 | -60.64875 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df6441b7-5740-346d-a89f-88627554a9cf | -2.16846 | -54.62329 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eea6b3d8-3c4b-3948-af48-722b47f120ec | 1.08862 | -59.6478 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fce11a67-b092-3f2f-a802-987c4c75c929 | -2.98153 | -60.9839 | 2024-12-05 05:31:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddefdb01-6bf6-346b-b59f-36797abc92cf | -1.44117 | -53.81489 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e36ca0b2-40b0-3c46-b4a1-4f67c2a40fd3 | 1.0607 | -60.60422 | 2024-12-05 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b19f2b3a-cbf5-3ff8-95e1-72374d7f1b78 | -1.07549 | -62.65751 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83830e03-8041-3a3d-9a28-01fdef08af6b | -1.84395 | -60.27434 | 2024-12-05 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea757c11-c9ac-3605-9a72-fe92a3df59d3 | -1.44164 | -53.81179 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf89374e-1458-3234-a525-fb02c40fab3a | -2.26603 | -53.53814 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e750695d-6be6-35f8-9e63-0e07ac92907c | 3.15534 | -60.71944 | 2024-12-05 05:31:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71b0d46d-f118-3471-8a3d-a1c409a65267 | 0.70307 | -59.87576 | 2024-12-05 05:31:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d7162bd-a8d2-3be6-8ccd-9001f38ecde7 | -1.51735 | -60.32711 | 2024-12-05 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 479f05c7-6ebc-3cf6-b264-5c9d949810c7 | -2.32482 | -54.40472 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49958689-c303-37fe-85ef-18aa17086b87 | 0.89659 | -59.38982 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 894fbc21-f459-3662-821f-d34c02dd9b40 | -2.16966 | -54.62407 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 4eb3d89f-37fa-3acb-a661-f17772b917c9 | 1.08864 | -55.97564 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02b38831-7caf-39b9-8cab-bd1928c701e5 | 1.09656 | -55.97029 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01cedd7e-6926-38b4-ab04-76eb64e05f32 | 1.031 | -59.48459 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0bc64214-344a-328a-bc97-bcbb3402a85c | -2.23641 | -53.69941 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ff469e7-0f85-30a8-9936-afd0f70d8301 | 1.03448 | -59.48402 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afa1fc32-c27c-30ae-b377-6a982eab0138 | -2.16058 | -54.61696 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 72a0f24a-073a-3ab4-babc-b5729466b01a | 2.60306 | -61.31112 | 2024-12-05 05:31:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57d97d81-8f0c-3192-aa80-d77461dcc92a | -2.24169 | -53.70021 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c23fbefb-2e9f-39c7-a03e-97eaa338ed2b | 0.75028 | -59.65934 | 2024-12-05 05:31:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0881079-8b0f-3f57-a028-4ba45e100bf4 | 1.10448 | -55.96492 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5385bc4f-d5dd-38be-881d-7aef4886ba74 | -2.16471 | -54.62331 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| aa8c643f-982e-386d-bdec-7faa4025275c | -1.07603 | -62.65407 | 2024-12-05 05:31:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69693b48-9e6d-349a-b956-ec98a5452302 | 2.47824 | -60.69312 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aee4c9c2-7148-3cd0-b060-d564e8fc41d0 | 0.70367 | -59.87951 | 2024-12-05 05:31:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f6a7e7a-6762-3378-842c-5003442a2a51 | 2.4788 | -60.69661 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ce0ef96-ff6d-39b7-b269-6ca71147f420 | 2.4237 | -60.64824 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cac542bf-ae00-38cc-a057-74ae689c44a0 | 2.42425 | -60.65173 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea73999a-b7ed-36ca-9f9b-bfd73592f9ac | -1.436 | -53.81402 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bc48682-c8bf-3797-baac-f0c8b4d7006a | 1.5271 | -60.67328 | 2024-12-05 05:31:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45b0b68f-5980-3979-92b3-8a489f7ab700 | 0.16821 | -60.59138 | 2024-12-05 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec5d6e13-d171-3bb8-91db-03993358655e | -1.43461 | -53.81237 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e7e4d6c-9d3a-3f38-baad-fb90d0aaca01 | -1.52711 | -60.3325 | 2024-12-05 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab1fe7b2-7c90-3cb8-9bf6-03dbfb73d98a | 2.57772 | -60.69961 | 2024-12-05 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8787c3a-88ef-3b3f-96cf-d9f7d9ae1bb9 | 3.23379 | -59.90888 | 2024-12-05 05:31:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20320815-4877-3839-b461-48cf47d04cb3 | -2.16351 | -54.62255 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9071ced3-eb5a-3b5c-99ff-75203d40195b | 1.41205 | -56.07494 | 2024-12-05 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 108f541d-023a-3ef5-994f-51a0e609aab8 | -1.4393 | -53.81627 | 2024-12-05 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 023f2e3a-3868-3127-8662-eb5a2636dbd1 | -2.16554 | -54.61771 | 2024-12-05 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e6ec9f07-f6e5-37fa-8e43-73853e1a6042 | -11.20459 | -53.82486 | 2024-12-05 05:33:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0c5b07c8-f579-348e-8a7f-3eb595ecf4d1 | -2.1724 | -54.6263 | 2024-12-05 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 997775b2-3432-31f3-a3f3-9eb7bf51d3ea | -2.1725 | -54.6063 | 2024-12-05 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 484db9fe-bcb3-3db3-885c-f33c07fc5e27 | -2.1541 | -54.6266 | 2024-12-05 05:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 1bfe4eae-c602-3710-aeca-330155d3ca45 | -6.9344 | -43.5401 | 2024-12-05 06:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 44d05a96-5734-375b-849c-14601bf577d0 | -1.43517 | -53.80463 | 2024-12-05 06:24:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| bd219b4b-9200-3bcb-bdbb-e7e24dbe1136 | 2.58147 | -60.69517 | 2024-12-05 06:24:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 43f2b9e2-1e80-3168-bf02-d4c92a734aac | 0.17328 | -60.58498 | 2024-12-05 06:24:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 266d30ed-7827-32bd-af76-50dc7cc42534 | 2.42619 | -60.6467 | 2024-12-05 06:24:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8da51624-bdb0-3832-93a3-c4623f6de74b | 2.43514 | -60.6454 | 2024-12-05 06:24:00 | AQUA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1a04b9c4-05a3-3e24-8073-e71fe9260bf6 | 0.75469 | -59.65339 | 2024-12-05 06:24:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a53c701e-c115-3ee0-a3fc-32cb041a2492 | -6.9344 | -43.5401 | 2024-12-05 06:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 6d8eb3b6-0ea9-378c-bebf-e9340cc11c26 | -1.4401 | -53.8153 | 2024-12-05 07:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 56658183-b573-396d-964c-417d171eb40b | -6.9344 | -43.5401 | 2024-12-05 07:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 9585d8aa-444c-30d9-9c8c-d50fe6d9f3ac | -1.4401 | -53.8153 | 2024-12-05 07:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| dabea9a4-b285-344d-ab60-400b2dbc75e0 | -1.4401 | -53.8153 | 2024-12-05 07:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ff982dcc-eabd-315b-8bd5-f1efd127ffa7 | -1.4401 | -53.8153 | 2024-12-05 07:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| e67eab06-0319-32a4-a289-30343b2cf540 | -1.4401 | -53.8153 | 2024-12-05 07:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4c4e543b-d8af-3f4b-8bfe-603a0210cc44 | -1.4401 | -53.8153 | 2024-12-05 08:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9999ea11-b07f-3349-bd08-29547a1d3de7 | -1.4401 | -53.8153 | 2024-12-05 08:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bcc7b27d-1516-330f-b954-e74a6611a924 | -1.4401 | -53.8153 | 2024-12-05 08:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 63bbaf28-aa92-3f44-b11a-3428d6152f35 | -3.99081 | -39.85343 | 2024-12-05 12:16:00 | TERRA_M-T | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9caace52-a7fb-34e6-819b-82c6269d08c0 | -3.41521 | -42.30421 | 2024-12-05 12:16:00 | TERRA_M-T | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 243015fd-e88c-3b71-9141-fe8dc6ccda99 | -3.9895 | -39.86254 | 2024-12-05 12:16:00 | TERRA_M-T | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 9f071725-0382-39bd-a83e-eea7634d7c89 | -4.24121 | -40.17164 | 2024-12-05 12:16:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2717998d-f946-3096-b639-c5e2eae9f555 | -4.57869 | -41.03604 | 2024-12-05 12:18:00 | TERRA_M-T | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 24.9 |
| d28a1db7-aa38-32c1-938b-d32f0736b9b7 | -4.98503 | -40.90257 | 2024-12-05 12:18:00 | TERRA_M-T | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 09e1440e-015f-3b04-8a76-73f2c356c8fb | -4.98629 | -40.89376 | 2024-12-05 12:18:00 | TERRA_M-T | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c0a2b39c-bcb6-3eda-bebd-5ec4f2b836dd | -4.57743 | -41.04482 | 2024-12-05 12:18:00 | TERRA_M-T | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| eeb06d22-7959-3ca0-ac73-8fc524b2b98b | -9.15667 | -37.67529 | 2024-12-05 12:18:00 | TERRA_M-T | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 17.6 |
| fb86a8f6-3878-3973-b10a-1761d4a6aaa8 | -9.30292 | -35.96324 | 2024-12-05 12:18:00 | TERRA_M-T | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 2c2c1e19-6af9-390d-a4fb-255d7430bb01 | -5.88015 | -40.12386 | 2024-12-05 12:18:00 | TERRA_M-T | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| ccd58c2f-ab53-351b-9877-0e9665b78785 | -10.11761 | -39.4767 | 2024-12-05 12:18:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| efd930a8-f16a-3fa0-bc09-fa21ed2476c7 | -9.30407 | -35.96914 | 2024-12-05 12:18:00 | TERRA_M-T | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 57.3 |
| 1d538731-668f-34b4-ab9d-30029bf79345 | -11.18891 | -40.31602 | 2024-12-05 12:18:00 | TERRA_M-T | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 60.3 |
| 9d99d437-0343-36ba-b95a-911c7d4d2a48 | -5.45169 | -35.71125 | 2024-12-05 12:18:00 | TERRA_M-T | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 3ba2a980-a506-38d3-9597-f9bb350df966 | -4.7667 | -40.80862 | 2024-12-05 12:18:00 | TERRA_M-T | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| cdca1a75-1996-3896-b180-b1289c05b2a3 | -10.45436 | -39.10741 | 2024-12-05 12:18:00 | TERRA_M-T | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 1f172e35-d84e-3f87-8278-fe0a3624a69a | -7.43324 | -39.89455 | 2024-12-05 12:18:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 80e52a95-aebb-3b5d-85df-99f5dac17434 | -4.63788 | -40.16895 | 2024-12-05 12:18:00 | TERRA_M-T | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 5e390789-0206-3073-911f-840067eadc0a | -4.63658 | -40.17799 | 2024-12-05 12:18:00 | TERRA_M-T | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 63080e63-4fc7-3ff6-81ee-aaaaaec2ff2a | -4.99269 | -40.78646 | 2024-12-05 12:18:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 32bfc8a9-cfd0-3830-bc51-4474016e621b | -5.60156 | -45.20403 | 2024-12-05 12:18:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4196f45b-1811-3e79-82fa-a232ac439674 | -7.43188 | -39.90427 | 2024-12-05 12:18:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 967a1e3e-8cfc-346e-93d1-67a313b567f2 | -14.05832 | -43.30189 | 2024-12-05 12:21:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9271dfe6-1065-3322-bd7d-15b48d60b527 | -11.34767 | -40.36084 | 2024-12-05 12:21:00 | TERRA_M-T | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 6c3314cd-ec47-3554-b754-b5fc5e354e22 | -12.2375 | -43.25682 | 2024-12-05 12:21:00 | TERRA_M-T | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 26dc8839-c13c-3cfc-a052-c68be1ee3edb | -13.88316 | -42.65717 | 2024-12-05 12:21:00 | TERRA_M-T | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 652830b6-3018-3282-a3f6-24259487d02a | -12.20138 | -38.24621 | 2024-12-05 12:21:00 | TERRA_M-T | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| d2f5a8d1-91b6-38d7-9f6f-d015c42428bb | -13.7405 | -40.74986 | 2024-12-05 12:21:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| cda4f7ac-bc8e-36c8-a199-d119138173d6 | -14.81919 | -43.20593 | 2024-12-05 12:21:00 | TERRA_M-T | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 201d5354-a037-3fca-a6dd-363699fe32ec | -12.19953 | -38.26051 | 2024-12-05 12:21:00 | TERRA_M-T | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 39.1 |
| 8a6fcbc0-4d01-3165-b591-b1bc6b8084ab | -13.90607 | -41.44367 | 2024-12-05 12:21:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 4856fdd7-7acc-3c96-9c9e-f6c40e9aa04a | -14.61435 | -40.54551 | 2024-12-05 12:21:00 | TERRA_M-T | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| f7ab0291-2d29-32c4-9342-d5a2c4404e1c | -12.24467 | -40.14295 | 2024-12-05 12:21:00 | TERRA_M-T | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d170959e-9ab5-3246-a62d-dab9b43a3677 | -15.26108 | -40.28342 | 2024-12-05 12:21:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |


[Clique aqui para ver as próximas entradas](README15.md)
