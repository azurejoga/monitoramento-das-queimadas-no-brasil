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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8986dc13-ea79-3a24-a707-e2d6bec015b9 | -6.12896 | -57.83607 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ddabf71-ba19-3926-a312-f7b0546fe210 | -6.12472 | -57.84176 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6304200-f8e7-353e-8594-8bc8aa70f951 | -7.22202 | -60.62643 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4fe5585-e735-3a6a-acee-8573a392a50a | -6.79494 | -59.8134 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6af2e4fe-a827-3225-af76-5d1abb0d3ebd | -6.96681 | -59.07595 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1456701-dae6-3f07-9a25-230d8fe01685 | -6.34073 | -54.75505 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f987a5e4-6e4e-3ebe-b82e-3c1c2cbb35ec | -5.00609 | -56.13485 | 2026-08-24 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02ac3741-1521-34b1-84d9-ccedb394d6eb | -6.34285 | -54.7612 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7904322-35a7-3d26-a26b-03a05b528b76 | -5.78395 | -57.5719 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ebd140b-8531-3da0-a78d-132b71693a25 | -7.57825 | -61.22613 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 51b6b52d-6077-3ee3-b5f3-3d0c3a5372ed | -7.60115 | -61.23108 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a11c230f-1fb0-3677-94f3-b1b61e6d63cd | -6.61431 | -58.38298 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5ecddbf-7720-38f2-a6d8-6d592cdffe42 | -6.12303 | -57.83514 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74c37734-b294-334c-b3b9-3e88e6741967 | -5.77191 | -57.57026 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 048e2fa7-7894-3dc9-9d6f-6f40eb2cbab3 | -6.14971 | -57.94866 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3067137-c7f8-3770-a412-999aa3468619 | -7.67983 | -63.33296 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 59787916-ee78-3eda-9d02-b2c128e2c897 | -6.79432 | -59.80999 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10ef37a2-f541-36b4-8db3-08571ca34208 | -6.13246 | -57.83006 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 035674f3-cfc1-3dd7-bdff-28b1ea010a32 | -6.96631 | -59.07954 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1c795f15-81e0-364f-a1ed-c2acad0e3595 | -6.96581 | -59.08317 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78c1c743-e5e1-3287-be9c-3b1fc9593c77 | -7.57022 | -61.20514 | 2026-08-24 06:05:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72f6affb-75bb-3a9c-950c-562c14fc3d1c | -6.7474 | -59.65327 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a70d9e2-13db-371c-8e02-446d113209bd | -7.6804 | -63.32914 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 84e98f57-2738-316e-899a-6f26e7984cf4 | -6.12533 | -57.83749 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 15bfbe9b-dbb9-3918-88c3-f4f6d6bda061 | -6.85922 | -59.4121 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2ee7792-c84c-3b55-b172-e77e0f4d6ad8 | -4.99878 | -56.13966 | 2026-08-24 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 063a8785-d017-311f-ae2c-e2a1f02455c5 | -7.68877 | -63.33038 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c780b46e-60f4-3b16-ba13-7eddfa49917c | -7.67565 | -63.33235 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7c1afb5-d64b-34f8-af87-f0529b88a22a | -6.67791 | -58.73762 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| efab3b34-ae84-3e39-b82e-f66b8ca28df6 | -6.3479 | -54.75613 | 2026-08-24 06:05:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0ab0e36-be88-3f62-bb76-0f9b4d9305cb | -7.67927 | -63.33678 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31f8e978-7889-3c99-bfe5-6affc4e17275 | -7.67678 | -63.32469 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 3e448414-4074-30a3-863d-37c6e67f98ab | -6.22774 | -55.62025 | 2026-08-24 06:05:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2ab7b128-15a7-3c60-8fbc-d94b6c1c0992 | -6.60856 | -58.38194 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd8a3be5-eb87-31f6-94da-e5fc42e37be1 | -6.55697 | -58.58873 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 288cd008-7506-3c0a-ac87-7bfc581001a8 | -6.79541 | -59.81014 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0bf6d57-0da4-3350-b1a0-bf76c48eff8f | -7.22185 | -60.62722 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8bb610b-4f85-37bb-bf62-9bc1c78e4b1d | -7.69035 | -63.32567 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| df8ed6d6-6162-3eec-9877-5804be63f4ad | -7.68402 | -63.33358 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| daf9da47-cac6-3f3a-a54b-572e30db73dd | -6.56154 | -58.58717 | 2026-08-24 06:05:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2840fa2-0239-3c95-9324-3733132a215a | -5.77917 | -57.56218 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f33acb-043b-3965-b8ce-713200208ba7 | -6.61376 | -58.38694 | 2026-08-24 06:05:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b7d8f6c-48a5-345f-b7c6-5fe949380ada | -7.68927 | -63.33334 | 2026-08-24 06:05:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ef2d67fc-d71d-3f05-8deb-5bb73953a5a6 | -5.00525 | -56.14091 | 2026-08-24 06:05:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5761a3a-48fe-3aae-97bd-511711a14ff9 | -6.96127 | -59.07514 | 2026-08-24 06:05:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 942cf8d4-5e7d-34d4-b193-4b8158bb41e2 | -9.21171 | -60.90526 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef450bc8-1e03-3244-9517-734cfbc8fdff | -8.89954 | -68.88924 | 2026-08-24 06:08:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea68b4f-6a2c-316d-80cc-52bc1be5b458 | -9.86937 | -60.10742 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4f97e27-635e-36f4-bb61-a8d16e8ca3c3 | -9.50967 | -60.49929 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c79b4d3c-28a9-3e18-91e4-a8dbb7085eec | -8.93641 | -62.1418 | 2026-08-24 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2360128b-f0df-358f-89d0-dca692b19a1d | -9.20545 | -59.5718 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf978afa-5973-3dbf-aa34-032450a80b78 | -9.40201 | -60.59068 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2975ed6-3d5e-37b1-8f6c-e4007a26e91c | -7.90474 | -63.68454 | 2026-08-24 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bbeaed6-76e3-3914-b22a-d1d3e195a6f1 | -9.82596 | -57.93665 | 2026-08-24 06:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab802e18-85b0-363b-ad92-d52ba4334adc | -8.8246 | -62.3709 | 2026-08-24 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5d43c3b-acb1-360c-8782-805087ac25dd | -8.93508 | -62.14344 | 2026-08-24 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e36eca9e-6118-33a4-b805-2676d9fbd924 | -9.19895 | -59.57843 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0b6b9a5-d81f-3310-989d-c551c44c1043 | -9.39246 | -60.58311 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ddd3fe4-42db-3bb5-b4dd-7968a2be60c7 | -7.90011 | -63.68759 | 2026-08-24 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5c1155d-fe8e-3989-84f6-2c66a4c9fd26 | -11.91522 | -55.90316 | 2026-08-24 06:08:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f4aa7a3-88f7-30ca-a483-af2516172e0a | -11.91032 | -55.89946 | 2026-08-24 06:08:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cc24847-a66f-3205-bba5-e77715b68765 | -7.90064 | -63.68393 | 2026-08-24 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2002e820-4759-3912-983a-e09f84afe1be | -9.1849 | -58.32049 | 2026-08-24 06:08:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a6895b0-fa55-3de1-81e3-3c7bfa8f377f | -8.82917 | -62.37138 | 2026-08-24 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a3aa10a-a1fd-3852-baf8-7a8f239242f4 | -9.58761 | -60.51328 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b81faa58-3673-3ce9-aaf1-887c03839a2f | -7.90528 | -63.68087 | 2026-08-24 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cccd3cf4-f6b4-3b62-baf0-4cbfecf494bd | -9.50926 | -60.50245 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af505aea-4c91-3fb2-819b-4094b4815fba | -9.00914 | -60.41941 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ab132e6-8fef-3ed3-bba2-ce7de332b301 | -8.82264 | -62.35149 | 2026-08-24 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 09e7e8dd-0ac2-396b-abe3-4444a86666b5 | -8.38242 | -62.69334 | 2026-08-24 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0816b4f-a18f-3b4b-83dd-e475bb4150a8 | -9.50362 | -60.5049 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 424fb1b1-6e8a-3a87-a7d9-0b6ae7408916 | -9.50403 | -60.50171 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28ce758d-504c-32ae-94f9-3bdb9964005d | -9.50884 | -60.50561 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bc8202a-1cd9-3282-9e62-89f8de5b5fc1 | -9.4016 | -60.59378 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 681c1c27-3db0-3a92-b1b2-e1cae4dcc0a0 | -9.86892 | -60.11089 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f50cb4f-30d7-398b-902f-1c329ccb47eb | -9.20497 | -59.5755 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a949daf-7a57-35a7-b4e8-58a141a7ed85 | -9.20449 | -59.5792 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe082a28-a568-37be-8c37-75e32819f049 | -9.58801 | -60.51359 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d53457e4-d914-37c1-b369-87f02f3a0c74 | -9.59327 | -60.5108 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e57bd889-b45d-3d7e-afca-f4354dc0cbdc | -9.38727 | -60.58239 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9cd9f1c-5ab8-3a59-bdd9-6c034d659674 | -8.38304 | -62.689 | 2026-08-24 06:08:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 319f97d7-3de3-3816-9d01-ff8e78e5636c | -9.14999 | -59.40358 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ef71f48-bf5f-39d7-8a09-6b1b676c38d1 | -11.91672 | -55.9077 | 2026-08-24 06:08:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f7d4fa2-3585-3c5c-9158-fa55b9284c04 | -9.19943 | -59.57478 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d3e115f-a33f-3035-b0a4-52643b19bf52 | -9.1999 | -59.57111 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 643d9467-1dd4-3ba1-a796-c760f8938ff9 | -9.59365 | -60.51112 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76e49bd6-f9c9-3f72-9f50-65cdfa9aa1b9 | -8.93179 | -62.14109 | 2026-08-24 06:08:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44647eb6-b926-3bd3-b3a9-4aeeb13322cf | -7.90884 | -63.68515 | 2026-08-24 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b9c9c31-6be4-3aba-8bb9-bc0a37d59812 | -11.90805 | -55.90222 | 2026-08-24 06:08:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c16cb3d8-e1f2-34df-ac76-d005e8b460ec | -7.90421 | -63.6882 | 2026-08-24 06:08:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45087b22-4ec8-393e-897e-666759c6cb0a | -9.86982 | -60.10394 | 2026-08-24 06:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d79f5812-1ba2-369c-bf43-5f668baf4952 | -8.82852 | -62.37606 | 2026-08-24 06:08:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7c29002-7b9c-33ee-ac2d-d8a4706e4d07 | -9.2121 | -60.90235 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 122fb622-4d0d-3a3e-bbf0-4f3143138e0e | -9.15047 | -59.39993 | 2026-08-24 06:08:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5457e3e9-2c13-3440-a2e8-abf362b8b8b9 | -12.0944 | -50.5737 | 2026-08-24 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f8b52f0c-746a-39d4-bdb6-9cd10d6a1ea5 | -14.9388 | -52.6853 | 2026-08-24 06:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 50.0 |
| da3b3654-c5e1-31f9-a074-b5d3f373e550 | -12.1132 | -50.5929 | 2026-08-24 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 0f0852b5-d710-31c3-9826-24f52f420d72 | -14.9396 | -52.6428 | 2026-08-24 06:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f33ca6a4-e09a-3c0c-9d67-9774de2e0ff2 | -12.0753 | -50.5759 | 2026-08-24 06:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4352a855-9a01-3001-b600-96b62ae92ce0 | -14.9392 | -52.664 | 2026-08-24 06:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |


[Clique aqui para ver as próximas entradas](README48.md)
