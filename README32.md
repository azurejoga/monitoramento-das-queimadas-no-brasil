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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7fc16a4-8d65-3d5b-8627-069b4aa8e39b | -1.24664 | -54.5292 | 2026-09-04 05:57:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f355ee1-d7c8-3e54-9691-fc88fc41ca45 | -1.24683 | -54.53244 | 2026-09-04 05:57:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1618dbb9-89d7-3068-9e09-9878fba228c7 | -2.40989 | -57.90102 | 2026-09-04 05:57:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0af8a0b5-4b8d-308c-9a16-1a6a2ecf75cb | -6.35513 | -65.48711 | 2026-09-04 05:59:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8637e231-6c97-3250-8ea9-083e4c7cc5f6 | -7.09415 | -56.51287 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd2048ab-f6dd-3ad8-abc9-71811210d593 | -6.68531 | -59.9383 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a42b6b1f-07b7-322f-be7e-a7a19368c408 | -3.01708 | -61.48739 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97bff5b0-6977-3edb-8d78-0c453f9db387 | -3.08078 | -61.18137 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d15f30ca-0857-316c-8b11-849d9c80372d | -4.10383 | -60.66187 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 066d203d-22c5-314f-8352-bf2cc81901af | -7.79843 | -62.34918 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2f7c771-071c-30b7-a1bc-76c7c6627616 | -6.95648 | -59.74375 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a5ae339-a17c-3d9d-afd4-991869644701 | -7.093 | -56.52112 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 600b1054-83c1-3ae4-9a2a-3ed4049d9d0e | -3.36727 | -59.50309 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05ffeeed-02e3-3a5b-8ef1-5535ee12bee3 | -3.2934 | -57.88318 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53540e62-fb75-3b77-885c-cdea84034f55 | -6.67599 | -59.93694 | 2026-09-04 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5c0a246-acdc-37ea-bfb1-d687a18cc96d | -6.6878 | -62.85235 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2e5ee13-a199-3301-9fc1-5c6af4ce6b97 | -7.47086 | -63.75064 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6233b193-b0e2-3ea1-855d-c13b9c2c84de | -8.10826 | -54.78748 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a5e88ce-0a6f-39f7-8561-2ac415bd979a | -3.29555 | -57.88301 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7c39480-90af-3a31-ad3e-a1b8cfe5e78c | -8.20402 | -62.79982 | 2026-09-04 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c7ed0ec-e43b-32a7-9dd7-c647dd9a13e7 | -3.28874 | -57.87943 | 2026-09-04 05:59:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dbdcfb1d-ed41-395e-aa85-77aaae699997 | -7.58516 | -57.68967 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fb58602-5f1a-30c3-b89b-dd4e12184fdd | -4.29441 | -59.957 | 2026-09-04 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e79dfce-003e-34b6-a26c-39e9b50d5a7d | -3.07121 | -61.08148 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 514e76f6-2dfa-3e3d-b21c-aea26678ecda | -6.71085 | -63.18478 | 2026-09-04 05:59:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 081147d9-489b-39b5-9b25-5e9d59717148 | -4.10442 | -60.65792 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89c914a3-146d-3a3e-8a26-c488f5c9b2a3 | -5.56429 | -60.17513 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c74eb92e-1efb-3b99-8276-29919d0bd9f5 | -3.77513 | -61.75492 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 987984cd-790f-3e59-afa1-90c9445b8ffe | -6.68325 | -59.95263 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 31d9db2c-9036-3934-9d11-0692463a5eca | -4.09897 | -60.66519 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbfa8c7e-d4e9-3319-a130-dce797eb1738 | -6.68771 | -59.98748 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| bf8506cd-fcff-3938-9b81-3f093333efa9 | -6.75762 | -59.43345 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fce847f5-92d7-32bd-9462-26b98213f51e | -5.17353 | -60.28342 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb225e69-3248-39c3-99e1-17afc97eb548 | -8.1915 | -62.80305 | 2026-09-04 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b3ac1dd-27ef-3a22-9668-6b8dac1fdd0d | -4.23937 | -62.24002 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd584173-fb76-3e75-be5f-28f3c540a99d | -5.85361 | -61.16343 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca3fc3fc-046c-34a4-9542-fd95c2835b0a | -6.52838 | -59.93525 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eda2653d-b908-399c-95d2-3e25fc41156b | -8.1669 | -62.77877 | 2026-09-04 05:59:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b31c56f0-0925-3945-bc47-3193f1f0d0c4 | -6.13422 | -57.68831 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e54791-1417-3956-a3c9-3a97be973742 | -6.67651 | -59.96643 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 50a88562-7bf5-3687-a60b-8e2e87ea2b09 | -6.66926 | -59.95077 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 305683c5-60d8-3904-8821-ba460fe08860 | -7.4395 | -64.61601 | 2026-09-04 05:59:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07a49c50-2839-39d0-81b3-485e0533eb3f | -3.61926 | -60.56982 | 2026-09-04 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1699e602-e44f-34de-a92b-2d08c98a478e | -7.73485 | -61.65035 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0f4dd18-9487-3ee9-a6b7-87c43210244c | -5.56045 | -60.16995 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0279667b-0eb7-3e4d-aac6-920bf1a4e58c | -6.69374 | -59.9786 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ebb10044-4ec4-3181-882b-37b4790600b5 | -7.42555 | -61.73184 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74853863-a615-3d3d-ab8a-309852a48158 | -3.14287 | -60.64069 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f1d0d6e-c199-3f12-aaeb-36c98c8eb824 | -7.55689 | -61.33567 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6aa7123e-9cbf-315f-bba0-05ed88e225c9 | -7.08181 | -56.51502 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfd2b32c-ee16-34e7-ab70-2ef45cc88773 | -6.14846 | -59.94227 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 263a84e8-8b0f-3b58-9397-019c7f30a669 | -6.31054 | -56.0456 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fca611ba-8f86-3261-9cd9-badcab1710fc | -6.68184 | -58.75292 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f02a450-cccd-39d1-89c1-b0cc4640ecdf | -4.24012 | -62.24272 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 346ece44-4d0a-3393-8745-da74c50fd341 | -3.61501 | -60.56918 | 2026-09-04 05:59:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e6b7cf9-260d-3b2d-a94e-68592232e214 | -6.9415 | -56.46025 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15a79bb4-d4d6-324c-b357-f1e8bae7d966 | -4.12423 | -56.34731 | 2026-09-04 05:59:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41618dd6-5150-3569-93a1-4cb68b2211ca | -7.73065 | -61.64969 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ea05be0-caa9-32a6-a4c7-84d7b23ee5d1 | -3.16085 | -61.11653 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b755c86a-169a-36e7-a731-d2a1bfa69baf | -6.1574 | -57.7573 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 106518cc-4977-3f5f-88f8-83c42263e2fc | -7.08713 | -56.52011 | 2026-09-04 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88ae8ec5-dcfb-37c1-8320-2b951344e45d | -3.67941 | -53.74737 | 2026-09-04 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af73d4b1-9e1d-33bb-8408-74aef8f2f572 | -7.37214 | -60.60309 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbc8f0dd-ef4e-32d5-b7fa-8a3cb15689bc | -8.1098 | -54.77599 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b7436f54-9870-3b98-a24d-0b2a3f03af1f | -7.5418 | -60.72388 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fe2ec7c-4ed7-34ac-a5ee-528d3c1e15d8 | -7.00001 | -62.97773 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a6d2820-619c-3c93-872d-a6746edee796 | -3.12388 | -61.2235 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e02b0ba-24df-3e93-9336-9156a56047b7 | -8.43642 | -54.69119 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 780507f0-8bb7-3dcd-8638-300c64fd04d1 | -6.76244 | -59.43425 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24203096-0be1-37dc-8f4f-0bd301b1228f | -7.55181 | -61.31013 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6613621-d71c-35e9-af19-2bb83e70ded1 | -7.56001 | -61.34433 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51dab27d-3ee6-3061-843a-b7df165300ba | -3.40013 | -61.34034 | 2026-09-04 05:59:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66fb38c6-2e59-3682-83c6-7a322f8f8989 | -3.77907 | -61.75552 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b158a72-ad0e-3c2e-bfbe-795b03b8eb29 | -6.77958 | -58.95493 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3aa867a-72e9-3fe7-9915-cf549881eb92 | -7.46603 | -63.74328 | 2026-09-04 05:59:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 93629e42-5354-31f9-bda1-0ecc11be67e8 | -3.18034 | -61.15244 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27489cfa-a5a1-343a-af52-27616f37d533 | -6.67972 | -58.76757 | 2026-09-04 05:59:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 853715aa-b811-3c22-87cf-6d8571f9d84a | -4.81396 | -62.78439 | 2026-09-04 05:59:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d46eb1de-8f54-3d42-a4f2-2349dc05ee30 | -3.10204 | -60.20089 | 2026-09-04 05:59:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b045d0bd-add2-375a-a31a-be8ddb89575c | -3.21876 | -61.17286 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e16a8b1a-f00b-3699-bbc7-8f00939b5ef6 | -6.15643 | -57.76413 | 2026-09-04 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a25210c3-0004-3ade-9a2b-a8af0eb82577 | -7.01461 | -62.98473 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc01ee0b-437f-388f-b1bb-027188e3e978 | -3.07584 | -61.07849 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2dfbac6-4a67-3d99-84c5-7a2f9b270f35 | -7.37277 | -60.59879 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9933ce02-5186-3502-a63d-ad351de2e7f3 | -3.07673 | -61.18078 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9afa578c-d00e-3ed4-ac89-604996475ec3 | -5.99729 | -62.50309 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdb6b564-f70c-3f24-b5cc-334f540f9fbc | -6.52577 | -59.93753 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dd28720-0fdd-362a-90b4-c1399d141559 | -4.14704 | -60.69258 | 2026-09-04 05:59:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7da0dda3-5c8b-36ca-a302-3c90eed38585 | -3.67487 | -53.75428 | 2026-09-04 05:59:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728a7ba8-80a4-3b0a-95ae-19de0d93360a | -6.6772 | -59.96162 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 535f56de-8a96-3e8d-a5ed-edd331af5165 | -8.11796 | -54.78901 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dd1fbbeb-fa00-39da-a990-30b68508370a | -7.01914 | -62.9806 | 2026-09-04 05:59:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f6ff7c4-d2e8-3b88-aad9-344d87e69e5b | -6.68997 | -59.9389 | 2026-09-04 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15d8971c-be8c-3603-a4ff-79c78fbf037f | -8.11131 | -54.78802 | 2026-09-04 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1a8f37c9-23ac-3888-8239-f379b381dd5e | -7.55514 | -61.34776 | 2026-09-04 05:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 045bb3d7-32b4-3563-a6bb-385a082f4884 | -4.24249 | -62.24536 | 2026-09-04 05:59:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 304d3011-a329-3edd-af36-2bb5182fa65a | -6.6386 | -59.44661 | 2026-09-04 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c2c481a-376a-3be9-ad8e-3e8d8655c0e6 | -6.68065 | -59.93763 | 2026-09-04 05:59:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bacf1ff8-8b24-3cd4-9f3b-7b3a482342eb | -3.29091 | -57.87927 | 2026-09-04 05:59:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee8d1b41-c408-3116-a0ae-2abf03433ab1 | -3.16437 | -61.12074 | 2026-09-04 05:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README33.md)
