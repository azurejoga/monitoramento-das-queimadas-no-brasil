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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96d3cd01-e695-3c4e-b2ed-27b9afd63810 | -10.85704 | -69.40065 | 2025-11-08 05:50:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 342655e7-5d27-384e-af38-8d6d6a262475 | -14.8587 | -56.56586 | 2025-11-08 05:50:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9146bd40-b59f-39eb-80d9-76db53ddb8c7 | -12.44001 | -63.15967 | 2025-11-08 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4759f23-005a-3131-97ab-5d91bfba7742 | -9.5905 | -68.70882 | 2025-11-08 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2b1bd72-964d-383c-b2c1-1e6743894f94 | -11.04369 | -68.70818 | 2025-11-08 05:50:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd75c8e3-ee41-3a2c-affa-9a1ca54bd60d | -11.76037 | -61.07616 | 2025-11-08 05:50:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfc04460-30c0-3d31-9781-0d91226d12f9 | -11.26495 | -60.8943 | 2025-11-08 05:50:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78962eb0-abe4-3457-b0f3-c72a24ddd1c9 | -11.72513 | -59.31798 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85fad1b9-93ab-31e6-becb-3a64f22ea06d | -11.73144 | -59.30941 | 2025-11-08 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 143e30ea-f587-3666-9cb6-d5e797e8da49 | -11.71512 | -61.42098 | 2025-11-08 05:50:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 123be70e-548b-3803-ad6d-ab74c47a39ba | -3.6633 | -45.9686 | 2025-11-08 06:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f2b03cbe-00c4-39d8-8ef9-8f14cc4a406d | -3.9292 | -45.0128 | 2025-11-08 06:00:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 1282f8a6-75fe-3d7c-a20d-3b6dc05dfd31 | -3.6634 | -45.9463 | 2025-11-08 06:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 173.0 |
| ece54c47-e45a-3dad-8495-0c4b6c942fbf | -3.9292 | -45.0128 | 2025-11-08 06:10:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 197.4 |
| c0fd4a35-0db4-3173-bbd6-ba29d52a6fab | -3.6634 | -45.9463 | 2025-11-08 06:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 105.1 |
| b4ffe7b5-6473-324c-8b75-2ef7e35fe4d4 | -3.682 | -45.9455 | 2025-11-08 06:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f13abd12-6733-3310-8e92-1eb2cdb3bdb0 | -10.28284 | -67.27837 | 2025-11-08 06:18:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cf52c49b-f6a7-3b77-b60e-5bf95fa86b8c | -10.28806 | -67.27438 | 2025-11-08 06:18:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e13d5460-d351-3baf-94e5-e23c0fb0f322 | -8.62372 | -66.81843 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6446e221-03e3-35ba-a845-73a7e76752f1 | -9.92596 | -63.64198 | 2025-11-08 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dfd8724-0842-3ed5-8e51-91159e989b7f | -9.86533 | -64.88096 | 2025-11-08 06:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43cb5ccd-a3a3-3d48-9784-0ea9859e67e8 | -11.86601 | -62.89069 | 2025-11-08 06:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5da732f-ce80-3fe6-b30f-67b18a8f1354 | -8.64555 | -67.03214 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 085265e1-261e-3e7d-b7d8-180aa229c024 | -11.04353 | -68.7097 | 2025-11-08 06:18:00 | NPP-375D | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 032400aa-37a5-3313-b631-6d9a046b50a1 | -9.8649 | -64.88438 | 2025-11-08 06:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c58bfb61-00e1-393d-bb3f-d69fad019681 | -9.55537 | -66.74541 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8eb4741-bd96-39dc-b559-ccc4c4d490b4 | -9.56073 | -66.74114 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d0a190c-3306-3a2a-8b22-95dad4a85efd | -11.86658 | -62.88583 | 2025-11-08 06:18:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0963313a-3d83-3ec3-adc5-a74f41d42475 | -7.01164 | -71.63178 | 2025-11-08 06:18:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f350672-17d1-3bb9-8985-7d4651d3f188 | -9.77892 | -62.50624 | 2025-11-08 06:18:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4b7eb6c-6951-3ddd-b992-74b018447cf7 | -11.79693 | -62.74852 | 2025-11-08 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9ccca3f-0412-3cc9-8baf-70bd381b66c2 | -8.63068 | -67.03934 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97e6293b-8a36-3392-a7b6-ba82bbb70a18 | -8.25773 | -71.11658 | 2025-11-08 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 520effe1-d6be-3860-9caa-1a3c83abc35a | -9.77953 | -62.50127 | 2025-11-08 06:18:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65bcee0b-3c89-3e8f-af76-f59c1548da8a | -9.50672 | -66.77051 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63f6848d-8879-3861-b528-9e24a3b86a0d | -9.30826 | -65.82325 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b3134ce-cb0b-3f75-9bbf-c865709b5d7a | -8.62439 | -66.81368 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a0e38c1-9138-3c80-ae5c-33ae50559e47 | -10.0012 | -63.65357 | 2025-11-08 06:18:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b65f9ac-5733-30ee-9e71-cc6678c7d819 | -9.62838 | -68.60075 | 2025-11-08 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77ba238c-7baf-32dc-9cc7-fbf21d828021 | -9.54197 | -66.7384 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e69a336-9f04-3f2b-ba5e-d1bf752f3edc | -11.79062 | -62.7478 | 2025-11-08 06:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bad8ced-b4ea-39ae-86c3-50b26a592cf0 | -10.85558 | -69.39938 | 2025-11-08 06:18:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0553b4dc-876d-3019-b39d-f00aa6bf731d | -9.77602 | -62.50003 | 2025-11-08 06:18:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ac7f197-3413-37d8-8b92-3a4dc0f5d6d0 | -8.65009 | -67.03279 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03dbfc68-fe8d-354d-b6bd-b9a0338a08ce | -9.87025 | -64.88516 | 2025-11-08 06:18:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe0be6bb-dd52-304d-8bc6-c6ebec31e478 | -9.59204 | -68.70915 | 2025-11-08 06:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc77a09c-4bad-377b-8c78-08ded603cb24 | -10.28349 | -67.27371 | 2025-11-08 06:18:00 | NPP-375D | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4967c43d-d077-37fe-a054-d5dcf56a30de | -10.8581 | -69.39832 | 2025-11-08 06:18:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 716101e0-99dc-3f2c-a62f-b45c2a305441 | -8.62187 | -66.76483 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11cc4149-89a9-3ba7-a605-72a850a1686c | -9.77537 | -62.505 | 2025-11-08 06:18:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be7d70fd-3ce5-304e-adf9-e0be9de6ac75 | -9.62424 | -68.6001 | 2025-11-08 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eed16ed2-4f63-341b-adc7-948ed2bf85cc | -9.50923 | -66.76891 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f8123ab-50ea-3bea-9fdf-0ddf0fc1140e | -9.50455 | -66.76823 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fef56b24-2ed0-3331-81b3-dd16cf54295f | -8.63522 | -67.03999 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97c7dd77-dc3b-3db1-a890-7638f527ceba | -8.56349 | -67.01443 | 2025-11-08 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 774cced5-8e38-3f0e-9c2b-a6af19252045 | -3.9106 | -45.0138 | 2025-11-08 06:20:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6e149e69-f2ba-358a-b88d-893531044139 | -3.6634 | -45.9463 | 2025-11-08 06:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| f120f9f4-bd55-3b8a-832f-5e9674a26086 | -3.9292 | -45.0128 | 2025-11-08 06:20:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| fc6b6948-290b-3b47-97a9-7113c8373589 | -12.45453 | -63.15365 | 2025-11-08 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98f6db82-c4e4-3915-ae67-7bd185ae6aad | -12.44833 | -63.15289 | 2025-11-08 06:20:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 725c5e90-4415-312f-816d-b6065094b0c6 | -3.6634 | -45.9463 | 2025-11-08 06:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 150.2 |
| a32f6139-8c40-3d12-99af-564777ea247f | -3.9106 | -45.0138 | 2025-11-08 06:30:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0c3ca24a-d2a4-3901-b284-5420edb737af | -3.9292 | -45.0128 | 2025-11-08 06:30:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 822fd9fc-4869-3dec-b6f5-3f20e9c9a14b | -3.6633 | -45.9686 | 2025-11-08 06:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7921409a-f3ef-3e46-91ba-7b85c2a0df6e | -10.28378 | -67.2761 | 2025-11-08 06:39:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ec18ae74-c5ec-3d98-9751-141219762999 | -10.28269 | -67.27895 | 2025-11-08 06:39:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e9902d2-6e33-35ee-8d6d-44724a4b28dc | -3.9292 | -45.0128 | 2025-11-08 06:40:00 | GOES-19 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 136.4 |
| e3bc1f15-cc9c-34db-a33a-c2fc25982629 | -3.682 | -45.9455 | 2025-11-08 06:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ca9072a0-ce58-3a0b-bfb5-6aeda486a668 | -3.6633 | -45.9686 | 2025-11-08 06:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| c57598a8-8f63-3ed4-8960-8f12600b5399 | -3.6634 | -45.9463 | 2025-11-08 06:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 142.1 |
| d861feb7-146e-39a2-961e-ecc6248f5a89 | -2.46507 | -49.3732 | 2025-11-08 06:44:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a1d50092-41a9-30b6-a7d6-9b1f0db563c2 | -2.70867 | -49.53898 | 2025-11-08 06:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| fd71875b-3cf3-39f7-a6ab-c49d08654232 | -2.45987 | -49.36536 | 2025-11-08 06:44:00 | AQUA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 9a8550e6-c182-32a7-8607-e184d3ab2a87 | -3.92329 | -51.00745 | 2025-11-08 06:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d1764448-91c8-3426-9465-6eade2f6ed2a | -3.32773 | -53.35888 | 2025-11-08 06:44:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f6b40286-fa3b-36b0-a654-4f8bffa563c1 | -3.64954 | -50.26149 | 2025-11-08 06:44:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 489ca2eb-b333-31b1-a586-b11388fe7286 | -2.71597 | -49.54548 | 2025-11-08 06:44:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f6723b3e-df87-379a-aee4-cf8b8f0e0ae4 | -11.869 | -62.88534 | 2025-11-08 06:46:00 | AQUA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b76a55c9-910c-3f9d-8225-027ccc0289a7 | -9.44663 | -59.20697 | 2025-11-08 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4eb845ec-d889-3074-b061-1b81101c5049 | -9.44803 | -59.19789 | 2025-11-08 06:46:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| da1fbac2-f83a-34de-b64e-53e51ea40169 | -11.73281 | -59.30849 | 2025-11-08 06:46:00 | AQUA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 82156676-57f2-3ec8-a656-9e7f7cefe13f | -12.45671 | -63.14611 | 2025-11-08 06:46:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b1ae3ae2-b9ae-34d9-a6ec-0f53412bf8fc | -3.5713 | -42.4431 | 2025-11-08 11:50:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 135.1 |
| 7a1c9c6a-28fe-3841-84cd-d180f93b6081 | -2.4631 | -49.3789 | 2025-11-08 12:00:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 4a486401-40cb-360a-a457-d3f2f3617b2a | -2.4631 | -49.3789 | 2025-11-08 12:10:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| e5081951-fa81-3dcf-ac9c-7978da66353e | 1.19364 | -50.79434 | 2025-11-08 12:14:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 17.7 |
| e827eb37-493e-35eb-abb5-21b6b10b8d46 | -4.23075 | -46.89083 | 2025-11-08 12:16:00 | TERRA_M-T | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 4ea4d23a-8e79-3322-a2b9-bdefe86ab7e2 | -3.44898 | -43.15391 | 2025-11-08 12:16:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8478518c-0cb6-3106-9812-669d51a868fb | -7.44795 | -47.81483 | 2025-11-08 12:16:00 | TERRA_M-T | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1c2abfbf-4db7-32ee-9615-d4fd335897a2 | -5.39317 | -47.65315 | 2025-11-08 12:16:00 | TERRA_M-T | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a1868218-4cf4-3972-8720-114b46a400fd | -3.34492 | -50.20611 | 2025-11-08 12:16:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| ebb1767d-aebd-3d2b-bebe-4f4b9e2619df | -2.83943 | -49.41022 | 2025-11-08 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5e982345-89be-3a44-9259-605b61f2aef1 | -1.4275 | -47.06514 | 2025-11-08 12:16:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 917f493f-ce30-38f3-83da-9265507d9116 | -3.02001 | -49.43784 | 2025-11-08 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0fbc8846-aecb-3acf-8f5f-b77c74fddc6b | -3.14826 | -50.29044 | 2025-11-08 12:16:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| e11376f2-5b03-3f11-b761-194757ebd739 | -4.82781 | -48.06248 | 2025-11-08 12:16:00 | TERRA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3c38860a-8621-3644-8702-8a6da40aa318 | -2.97995 | -48.70865 | 2025-11-08 12:16:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| bdd1303e-26d2-3002-a83e-d64f0b9774c6 | -2.61814 | -49.22739 | 2025-11-08 12:16:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 65f3d26c-be7c-37c4-b11e-8b47d58eda8b | -3.56706 | -42.44473 | 2025-11-08 12:16:00 | TERRA_M-T | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 297.8 |
| 94b7aa34-344a-35bd-b445-b49f90cef508 | -3.8607 | -44.99918 | 2025-11-08 12:16:00 | TERRA_M-T | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |


[Clique aqui para ver as próximas entradas](README40.md)
