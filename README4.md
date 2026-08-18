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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83a15d9a-678c-3c8a-892f-18051d769436 | -6.85964 | -59.02317 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| b5a383e8-21e3-3987-ab29-e33df083ccf8 | -9.12645 | -61.60453 | 2026-08-18 01:09:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 29e9fe95-f156-3313-bae9-c75a33777b9a | -6.95509 | -59.04507 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 35f745b3-0768-3099-9e22-4fb8dbc58bd6 | -10.13456 | -62.39768 | 2026-08-18 01:09:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 57917058-43a6-3671-8aaa-2a2bc8444aad | -8.75341 | -62.91231 | 2026-08-18 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 31f0e7b1-56c7-30f1-92a7-28c23eb41c3e | -8.73282 | -62.90467 | 2026-08-18 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 1b8c1d9d-c1e9-30e2-bcfa-f05ecd78ce41 | -8.95235 | -60.58579 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 542ecd23-8f72-3d1e-b2e7-91eb1a3f0ad9 | -10.40785 | -61.20866 | 2026-08-18 01:09:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6fdba9eb-01de-3e8d-a01e-3f7d70d3d2ee | -6.73816 | -59.17818 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 07f95415-1c28-32ed-8a32-dfe3597f6af0 | -6.75461 | -59.19751 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.7 |
| fed8c50a-86b6-3f7e-aad9-5d3d42b61cb1 | -6.75095 | -59.16154 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 158.8 |
| dd6aaa8f-4d51-35f0-af00-ea13fb815730 | -7.60694 | -60.82633 | 2026-08-18 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| fd328a0e-8fb9-370c-9c6d-2ee84a7e7304 | -8.89864 | -60.60955 | 2026-08-18 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 14dec95f-c504-3ba2-a731-bdc6faf6b560 | -9.35349 | -62.37571 | 2026-08-18 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 46d2aa24-56dc-3b14-aa71-7dfa78c369e6 | -6.90832 | -62.90349 | 2026-08-18 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d489435b-ed55-33cf-add4-a6f614361904 | -8.19004 | -55.01091 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| de3a780a-8e66-3d8f-8738-6827debccea2 | -10.13617 | -62.40859 | 2026-08-18 01:09:00 | TERRA_M-M | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 561567b3-fb76-35b7-836a-679b23050d8c | -8.25417 | -62.98515 | 2026-08-18 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 88ea2efe-bd2f-372e-b8df-8c520e52d2f8 | -9.42357 | -60.42805 | 2026-08-18 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 621b1a4b-312d-32cc-93db-d0689cda0932 | -6.77741 | -59.76679 | 2026-08-18 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| f3d9e87b-019a-34b2-8d43-19fc630e2549 | -8.21411 | -55.04802 | 2026-08-18 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 30b018af-73e1-3149-a2cd-2e26460e0cbd | -8.2222 | -55.0216 | 2026-08-18 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 17711e8d-8ae0-31a7-a6ca-7f35f922184c | -6.7663 | -59.1708 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b1c532d5-1b03-366f-8ce3-b3da2b902ba0 | -9.4256 | -60.4353 | 2026-08-18 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 5747ed58-9fd2-39fc-b0f0-e543b56e745a | -9.4257 | -60.416 | 2026-08-18 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| f9bcf7ec-2ed6-3260-88d7-f3683ab3b219 | -10.8691 | -44.9646 | 2026-08-18 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 207.2 |
| eebd73fc-e228-3b1e-a8b4-aecb109402aa | -14.1631 | -52.9113 | 2026-08-18 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d7beb2ca-d527-3204-884a-0b5c8537a32e | -10.8688 | -44.9877 | 2026-08-18 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 363505a7-acfd-376b-9732-61cc72a8230a | -6.748 | -59.1523 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 48ede342-4fff-3ac3-aa39-db224ca64002 | -6.7478 | -59.1716 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 172.3 |
| bee4c93e-23ef-3928-bf98-21aaf4d4ae34 | -14.8033 | -46.6453 | 2026-08-18 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0a9c0ba3-1948-3c5e-8889-db4907306c04 | -14.1821 | -52.93 | 2026-08-18 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 1ca7312f-a776-3627-8346-0bb1a1ed4e61 | -14.8228 | -46.6419 | 2026-08-18 01:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2ce1a42a-aa9f-35cb-b234-e02e8f8caa41 | -17.1021 | -46.5575 | 2026-08-18 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 4dc8eacc-5936-39fc-801e-8cdba4bc28af | -14.1628 | -52.9323 | 2026-08-18 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 35e4c05a-91f8-34d0-aaee-ed41ab065b27 | -6.8594 | -59.0125 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 76b85c1b-eb86-31e5-8352-661bd7a34595 | -6.7664 | -59.1515 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| cdac78fb-471e-3e76-8e1d-9fd4b321b51b | -6.7477 | -59.1909 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1b79cab1-e93e-35ce-b68e-5db604f9955f | -17.1016 | -46.5808 | 2026-08-18 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 8f850bbb-9778-371d-9fcb-211f6c510346 | -22.0762 | -55.9924 | 2026-08-18 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 44acadaa-0dcc-32b6-896d-b364e29a3f13 | -6.8411 | -58.9939 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a56b105a-2236-3684-b9bb-88d1afd23111 | -6.8596 | -58.9931 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 22f0c6d2-1c5c-374e-b1d5-3495b2f6058c | -8.222 | -55.0418 | 2026-08-18 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c26afa88-6e79-3bf3-9384-b9e74fbbc43c | -8.604 | -50.3527 | 2026-08-18 01:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3cbff971-4d62-3110-a035-fa5c7cde901f | -14.1824 | -52.9089 | 2026-08-18 01:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 121.0 |
| c5e4600c-a809-3ad9-bef5-a32bbc4c88ef | -6.841 | -59.0132 | 2026-08-18 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| d5ca6206-387d-37ab-b5ca-bdbd60e6efc1 | -9.4254 | -60.4545 | 2026-08-18 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 69d233c4-d634-3183-bef4-b4b9c1c95f96 | -8.185 | -55.024 | 2026-08-18 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c70d3ff9-84c6-3319-8601-3f552c145af7 | -10.85 | -44.9672 | 2026-08-18 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 35d267a1-0b2b-3e3a-b202-8a541108d4f3 | -17.1215 | -46.5767 | 2026-08-18 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 6d4ab4a8-8bcb-3951-b2a8-763a435d8bad | -8.2036 | -55.0228 | 2026-08-18 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 6613a596-81b4-3ad9-bb5e-0998bb04cf70 | -8.6 | -54.74 | 2026-08-18 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51b9fb8e-d109-3c82-8912-607e88acc500 | -8.54 | -54.72 | 2026-08-18 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9f6f2d-f421-3b77-a6bd-13599da6dc56 | -8.58 | -54.79 | 2026-08-18 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72ca55f0-b8c7-3fc6-b4df-8c24c6be0c79 | -8.57 | -54.73 | 2026-08-18 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0797f6d-ffe9-393a-9fb7-82d1c0844285 | -17.1 | -46.58 | 2026-08-18 01:15:00 | MSG-03 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 63588f4c-baef-3e89-831a-696d8da99800 | -8.57 | -54.66 | 2026-08-18 01:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 471a8961-70ae-31ad-adcb-6af96543bd7c | -8.604 | -50.3527 | 2026-08-18 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 1b289f02-25ac-3960-8955-cffda6333571 | -14.2562 | -51.9472 | 2026-08-18 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 180.5 |
| c85eac42-0527-3c35-854e-b011ec46d15f | -6.9516 | -59.028 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| bf8772ff-e6f5-303d-9485-8af42a7965d0 | -17.1016 | -46.5808 | 2026-08-18 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 9adbd1ba-0389-33f9-9107-5fd0a2183ea9 | -22.0762 | -55.9924 | 2026-08-18 01:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3ce20e4d-5b9b-3e0f-92ad-03a50384fef4 | -14.0355 | -53.6808 | 2026-08-18 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d0cffce6-785c-3d04-beaa-f2281e3adce9 | -6.841 | -59.0132 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 966c3172-79b4-3cb0-a764-e0fad52031c0 | -10.8691 | -44.9646 | 2026-08-18 01:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 263.4 |
| e5d25879-b100-3688-9f50-b8c410011767 | -14.2755 | -51.9447 | 2026-08-18 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 192.9 |
| b428efb7-a7de-374a-a391-bd9fffb3e283 | -8.6042 | -50.3315 | 2026-08-18 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 9ec35169-c618-3ec4-95df-00a9e463ee5a | -10.85 | -44.9672 | 2026-08-18 01:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 216.6 |
| f7b2a56f-7842-3770-8845-185455bc3b93 | -14.1824 | -52.9089 | 2026-08-18 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 93fa5c93-cfce-3430-b13f-0b360165f843 | -6.7477 | -59.1909 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b45e2f57-e535-3d2f-830a-ac1a3c149f7f | -8.185 | -55.024 | 2026-08-18 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| f58ff31d-1d01-338b-bcce-dca1a689fe4e | -14.2759 | -51.9234 | 2026-08-18 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 96f7295b-cf9e-3938-a79c-1638f1585769 | -6.7294 | -59.1723 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 6f5ef73e-0312-322b-85d8-174800d726f4 | -14.1631 | -52.9113 | 2026-08-18 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 066d0919-c253-3619-b71f-f5be8c1ce4b0 | -9.016 | -60.4945 | 2026-08-18 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 51c173ae-dbfa-37d0-a2d3-44906cd308ca | -14.1821 | -52.93 | 2026-08-18 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 08491bd6-8795-3009-bdbd-6f8eb5b8b7c8 | -9.4256 | -60.4353 | 2026-08-18 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a082c698-65fb-3acc-912a-fd3c9af18e19 | -9.0158 | -60.5138 | 2026-08-18 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 80d7d180-5c47-32ec-958f-9e9f1abf8cf8 | -14.2566 | -51.9259 | 2026-08-18 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 253.6 |
| cb97e517-a653-327a-92f5-ea2c214331aa | -17.1215 | -46.5767 | 2026-08-18 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 376b77ac-c16d-3348-bc35-3e01b0363c22 | -9.4254 | -60.4545 | 2026-08-18 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 0015996b-66ed-3b35-978f-9e08e5edba32 | -6.7478 | -59.1716 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 3f49900e-346e-38da-8005-2df86b3e4b3a | -8.2036 | -55.0228 | 2026-08-18 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 7d5cf727-a5b8-38b1-82bd-92ffb17b07ce | -6.8594 | -59.0125 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| f289c826-6e89-349c-b126-73d62f63a467 | -6.748 | -59.1523 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8753d70a-f209-3cd9-a562-159c726878dc | -6.7663 | -59.1708 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 77bfd25d-4b70-377b-afc0-a1083f815eb3 | -6.8411 | -58.9939 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 7454bf44-5f5d-387e-98a4-4509ec958091 | -17.1021 | -46.5575 | 2026-08-18 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 77.8 |
| d342bacc-2066-3d3f-ba80-27ce91127804 | -6.8596 | -58.9931 | 2026-08-18 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 03a3ab7a-33bd-3ca0-9293-fa4e9e8a0557 | -8.9974 | -60.4955 | 2026-08-18 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d5db0336-8906-3050-b5ba-f3b2865101d9 | -8.2222 | -55.0216 | 2026-08-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b3ca8969-08e4-355e-9e61-48d68aed7265 | -14.1824 | -52.9089 | 2026-08-18 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 415b82ba-1b61-3d05-9bc6-1a9c76ec7c03 | -6.7664 | -59.1515 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| aaaab0fb-d552-3dd2-92a3-6c9d9e1570d0 | -14.1821 | -52.93 | 2026-08-18 01:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 56af8283-caee-31bf-a9c1-1f74c15f4a7f | -6.7478 | -59.1716 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 687b9ad4-9f03-3d38-800b-d9468df2b821 | -10.85 | -44.9672 | 2026-08-18 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| fee74397-ca01-3051-b3aa-9f9b3913d26e | -9.0158 | -60.5138 | 2026-08-18 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| ff13a4a5-8bcf-3af2-829a-fbab1f68b4cb | -6.7477 | -59.1909 | 2026-08-18 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| fb3e1e8c-a960-3b35-820c-d1fe4a81e01e | -8.604 | -50.3527 | 2026-08-18 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1330d3b8-7b13-3747-8ec9-ab80fcc2ada4 | -8.6042 | -50.3315 | 2026-08-18 01:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |


[Clique aqui para ver as próximas entradas](README5.md)
