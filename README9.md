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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 526081df-9f00-31a5-bf87-542920fb602c | -8.7097 | -62.814301 | 2026-09-16 01:21:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 54a724b2-edf8-37dd-aa88-efda5794ae96 | -7.5502 | -62.319599 | 2026-09-16 01:21:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2af43bba-6551-391f-befe-5c5e25cdc580 | -5.1316 | -55.8899 | 2026-09-16 01:21:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e34c720f-91db-39f1-854b-96cc3b3cd4e9 | -9.1019 | -65.915497 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1826933-ab0e-3f90-a76a-3a2dbe2cee96 | -8.5955 | -64.080902 | 2026-09-16 01:21:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 038319a7-ada3-3fa8-ab47-47007226e6ab | -9.0382 | -65.9077 | 2026-09-16 01:21:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5e1bde4-2926-3b3d-832b-a1047be5e54a | -9.3762 | -60.279701 | 2026-09-16 01:21:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74bf0b5c-3de4-3412-bbc9-dcb9cd9bcb21 | -16.2603 | -39.4136 | 2026-09-16 01:30:00 | GOES-19 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 83.1 |
| fde29c2a-a617-3475-8a9f-61622f36b98d | -10.792 | -46.2071 | 2026-09-16 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 96bd336b-614c-3084-96d4-e691ccb8530b | -9.112 | -45.7294 | 2026-09-16 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| eda09709-472c-3fc5-8f8c-162149c980ed | -8.8588 | -44.8919 | 2026-09-16 01:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 24078d00-076e-3b27-9ab7-3610211bae9e | -9.8012 | -46.4854 | 2026-09-16 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 489dfc29-afe4-35e8-9239-fe49586503d7 | -9.7136 | -64.9074 | 2026-09-16 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 9a5ddd4d-9e00-301d-8475-1a9bab40984e | -5.144 | -55.9345 | 2026-09-16 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 151.7 |
| 1497d435-be46-34a3-be14-3f7fc77a5325 | -5.1215 | -47.6146 | 2026-09-16 01:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 6cff9c34-1a51-31a2-b5c7-8be493b66e04 | -8.8585 | -44.9149 | 2026-09-16 01:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 044144a7-632a-3d6d-9fec-6969e8976a21 | -9.7322 | -64.9067 | 2026-09-16 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| cedc9d2c-fec5-3fd3-9179-8f663fc45f3f | -11.9033 | -43.8112 | 2026-09-16 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 3ed16b0a-9ec1-3b38-86e8-55f96fb28030 | -2.1051 | -52.0575 | 2026-09-16 01:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| af1d9d6b-568d-30b8-8677-119551422a53 | -9.4102 | -62.7113 | 2026-09-16 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 32a676b7-bbdc-39cd-9134-db727d594ffd | -5.1624 | -55.9338 | 2026-09-16 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 128.6 |
| cbf49b3f-1a2d-33ec-98b8-8823799f3fe2 | -7.6511 | -67.164 | 2026-09-16 01:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6776eb7d-00b5-3203-89f4-4cf616bf54cf | -5.1441 | -55.9147 | 2026-09-16 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ba8b0e92-cbac-32ba-b0ff-fdcb1f0797d0 | -5.1217 | -47.5928 | 2026-09-16 01:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c4fa6ee1-b178-37c3-bf5f-a8b03310075a | -11.4849 | -45.7965 | 2026-09-16 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 3831f02c-4a12-3f69-abb5-8837fb76f354 | -9.3893 | -60.3022 | 2026-09-16 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7de31746-cc95-36ff-831f-26481ba5968e | -5.1029 | -47.6157 | 2026-09-16 01:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 87d482ea-d7ba-388a-a851-48324d5bd0eb | -9.3892 | -60.3215 | 2026-09-16 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| be78564e-d821-3260-893c-d2363420e578 | -11.1401 | -40.4748 | 2026-09-16 01:30:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 90a24211-b3d8-3579-b5b4-6b0e1b5fd5ed | -16.2596 | -39.4398 | 2026-09-16 01:30:00 | GOES-19 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.4 |
| f66cf8fc-7712-3ba7-91c7-83b65ac2f388 | -5.1624 | -55.9338 | 2026-09-16 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 20629f29-b338-3b69-a347-07a860207a9b | -11.9033 | -43.8112 | 2026-09-16 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 3572fd0c-a8a7-3eb5-9c55-a4e6f7bacedf | -9.4102 | -62.7113 | 2026-09-16 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| d3836ac6-b34f-3ffc-97fe-861044862f4b | -7.6511 | -67.164 | 2026-09-16 01:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| fc9974d4-fb2f-31f3-82ba-cd28d4309c3f | -9.7136 | -64.9074 | 2026-09-16 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| fda131ef-8080-3d24-ad5f-98ec589e8849 | -5.1215 | -47.6146 | 2026-09-16 01:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 7161b5db-7d82-34ff-a00a-89dc7e705f6f | -2.6966 | -57.6084 | 2026-09-16 01:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d8fcca28-4e71-3cba-9a8d-64e6d7812180 | -5.144 | -55.9345 | 2026-09-16 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| bb6139fd-42fc-374b-abaf-a1a26d45c22a | -11.1401 | -40.4748 | 2026-09-16 01:40:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 49c745fc-15fd-3faa-adfa-2ac1bafcfe0c | -5.1029 | -47.6157 | 2026-09-16 01:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2d9aa367-97e7-3a39-9839-8996bd65cf40 | -3.3806 | -50.8458 | 2026-09-16 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| b1bcb5d6-b16a-3f73-8e72-af9e82b7cc23 | -7.651 | -67.1824 | 2026-09-16 01:40:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| b03af3d8-d395-3c56-93e8-58d362269b4a | -5.1401 | -47.6135 | 2026-09-16 01:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 125e4578-58a6-3f41-bf07-f79a1459c241 | -5.1217 | -47.5928 | 2026-09-16 01:40:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 5b37b680-aebd-3c42-879c-b6a5332e653c | -9.3893 | -60.3022 | 2026-09-16 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 55ad9722-2982-347b-9732-d901649e2712 | -15.2821 | -42.8075 | 2026-09-16 01:40:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a86c2560-2a5b-3835-9011-f4e50908e270 | -9.7322 | -64.9067 | 2026-09-16 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| bbd1f7ed-3e74-3b07-8533-cdc60bf75fac | -8.8378 | -62.477501 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5b3270-e39d-3c04-b02b-df02235272f7 | -9.7243 | -64.903397 | 2026-09-16 01:43:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ed81fb70-8f41-37f6-a2cd-4e8df7dcb8c8 | -9.0992 | -65.927101 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3277ea3-33c9-3aa0-abd9-d873396191bf | -8.8776 | -62.515202 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee987f3-db4d-37bb-90d1-fb703a77a405 | -7.6459 | -67.160896 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98b83d19-7129-3da3-9590-d574d891a1a6 | -9.4096 | -62.716301 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 33d33706-a471-31b3-98fc-68b225ed23aa | -8.7236 | -62.829498 | 2026-09-16 01:43:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1689b204-6bdd-3f3c-b95a-6adeffdf5483 | -6.3314 | -60.000099 | 2026-09-16 01:43:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 91fea297-f9a3-3c5c-8416-fd178de130ee | -9.4176 | -62.706699 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 76ec249f-9bc6-38e0-ab90-b7726eaf7d01 | -2.6918 | -57.6036 | 2026-09-16 01:43:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a286d4a-eadb-358f-823a-021bdce57ac1 | -15.4634 | -53.780899 | 2026-09-16 01:43:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6010f6c5-cb62-38b5-af92-94707b435bda | -7.6493 | -67.176399 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09c3c20b-6f35-3341-a47f-ff67084042d7 | -8.6501 | -66.589401 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d754936-dc37-34f1-9b96-06b1f632227e | -8.6786 | -61.403702 | 2026-09-16 01:43:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64231886-a1e3-3748-8a92-825f09f606ec | -9.4193 | -62.714001 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 12783767-6f14-363a-ac20-ef487142af82 | -8.6015 | -64.089996 | 2026-09-16 01:43:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e204432c-360e-3806-9bdb-f1c7d9ef1d71 | -7.5638 | -62.3274 | 2026-09-16 01:43:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0025e68-ebbf-3e9a-9fc0-a552a1187054 | -9.3862 | -60.297901 | 2026-09-16 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf4b055f-9d46-3e12-98ee-1dcd4207d453 | -9.0552 | -65.914101 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20d066a2-e05e-330a-b776-96f8d90bbead | -7.6123 | -67.241203 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e02cda74-94c3-3653-a609-dc6b4a743425 | 2.7048 | -60.2967 | 2026-09-16 01:43:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c288576e-35f5-30bb-b9db-c080997239e9 | -7.6476 | -67.168602 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d90cfd7-48b2-35e7-bc41-c4690d17ff5f | -9.7259 | -64.9104 | 2026-09-16 01:43:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0065c9b1-7c14-3ad7-9361-8f92fe666c3c | -8.828 | -62.479801 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 45792b7e-01ca-3369-88b1-6e975327e1a1 | -10.6586 | -58.7691 | 2026-09-16 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba0faf47-5940-3ccd-a1cb-2170d56a9799 | -9.1025 | -65.941498 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa7581fe-1554-3569-ba3a-a411782b5eaf | -8.6031 | -64.097 | 2026-09-16 01:43:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 492f2ac7-d1b6-3d81-98ef-e6d88df0e0f1 | -9.7275 | -64.917297 | 2026-09-16 01:43:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 68705607-0f82-30ac-9a69-769a3cf83888 | -8.7138 | -62.831799 | 2026-09-16 01:43:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf33fed4-17b0-3616-a597-cc20e26899b2 | -6.3714 | -55.8298 | 2026-09-16 01:43:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f31b011-ee6e-3fd2-bef3-f9569d1e8cca | -8.6612 | -66.500801 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b66d126-1556-3d08-9213-ddb1dd857a98 | -5.1563 | -55.935902 | 2026-09-16 01:43:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e6af06-56ba-33df-afca-0d7bed32c340 | -5.1467 | -55.938202 | 2026-09-16 01:43:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0df0788-c339-39ec-9c9f-0a985e258ab2 | -5.1416 | -55.917599 | 2026-09-16 01:43:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5dbf4a8-d3aa-3541-aa1f-484c5647af59 | -9.0568 | -65.921402 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 466b20ee-293b-3760-b65c-c662700760de | -9.4062 | -62.701698 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff7f60b3-0890-3e9f-a97f-0ab4492d6d8c | -3.705 | -60.614899 | 2026-09-16 01:43:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6995faa-99b0-33b2-a286-c02a6e5d5fcf | -10.6559 | -58.758202 | 2026-09-16 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7a816759-f006-3d62-9de3-2575b8f9ec68 | -10.0593 | -67.062401 | 2026-09-16 01:43:00 | METOP-C | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 35947e30-1d59-3407-9559-1416d4f5842d | -9.1223 | -65.846397 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea7eeadf-0587-368f-b7e4-c8e3ae91ca41 | -11.8139 | -60.466599 | 2026-09-16 01:43:00 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 90e65831-d532-3efb-85ac-fd61433972cb | -2.7056 | -57.618599 | 2026-09-16 01:43:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82dfd6ad-b421-31d1-903b-df78e379675c | -9.4079 | -62.709 | 2026-09-16 01:43:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9643cf0b-cb00-35a7-a637-a423e4d79c54 | -5.1512 | -55.915199 | 2026-09-16 01:43:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 359e5f7e-465f-385d-b974-c14260c61dfb | -9.3884 | -60.307098 | 2026-09-16 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e469abf1-3de4-3975-a754-d17782a3bf1a | -9.7228 | -64.8964 | 2026-09-16 01:43:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fcc1ba7c-196f-36fe-b4d5-867bf1ee4a5b | -7.6574 | -67.166496 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc8a6a2-2a19-30c2-ba80-1c40a189761b | -7.5522 | -62.321899 | 2026-09-16 01:43:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93c45a86-487b-30ae-bfcf-87d3ddf0d233 | -9.0584 | -65.928596 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a04e4892-a90b-3d80-bf90-3a4d18419ceb | -9.1403 | -65.834801 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 111ad158-e3a2-309f-bbf8-f54e71c28ac7 | -8.7121 | -62.824501 | 2026-09-16 01:43:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d7652d8e-e865-38fd-91a1-33e7aad1213e | -10.1434 | -61.1772 | 2026-09-16 01:43:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a086b42-1217-3713-a5ec-134a7896f336 | -8.6884 | -61.401402 | 2026-09-16 01:43:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README10.md)
