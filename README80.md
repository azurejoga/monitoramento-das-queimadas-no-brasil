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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9656e8a-ab34-3504-a37f-659e1f4bd378 | -14.56148 | -41.6278 | 2026-10-06 11:04:00 | TERRA_M-M | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5197e48d-0317-3298-84eb-8f5e80d81f62 | -16.12024 | -43.39433 | 2026-10-06 11:04:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 28.3 |
| e5db5ead-68d4-3faf-ae87-efd123a2486b | -16.12295 | -43.40145 | 2026-10-06 11:04:00 | TERRA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 57860346-b492-387c-9c5a-dfa1cf4f4ca6 | -14.56203 | -41.81614 | 2026-10-06 11:04:00 | TERRA_M-M | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2d3584db-8b93-3468-9fd7-aad65c763d50 | -13.4926 | -42.59711 | 2026-10-06 11:04:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| c2fa6f37-9783-34d1-9fab-a05c35bbd9b3 | -13.16811 | -42.31698 | 2026-10-06 11:04:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 594f4b0f-d74a-3454-aa0d-1401eaaba523 | -14.46565 | -41.84146 | 2026-10-06 11:04:00 | TERRA_M-M | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 3c6ed897-1034-3b51-8f5c-e4ff202737e4 | -11.2607 | -45.5078 | 2026-10-06 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.9 |
| b314f52e-8c66-3905-a131-f481d3e476aa | -11.2603 | -45.5308 | 2026-10-06 11:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 591fdeba-c3df-3ec6-ba90-8a9436c7c948 | -11.2607 | -45.5078 | 2026-10-06 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 206.3 |
| 5d15e978-d771-317c-b084-2c8994fc8378 | -11.2603 | -45.5308 | 2026-10-06 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 15e635f2-5d2b-37af-b13c-7bf25a2b5944 | -11.2798 | -45.5052 | 2026-10-06 11:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 764c982b-163d-3ec0-9955-8ad7e975ef1b | -11.2603 | -45.5308 | 2026-10-06 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 7f4d9331-5409-3def-aeaf-9f7b999ecf2d | -11.2607 | -45.5078 | 2026-10-06 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 141.9 |
| d656a0f8-c2ac-38c1-8c8a-5b8010846d4e | -11.2603 | -45.5308 | 2026-10-06 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| e904a928-9835-3c9c-a38a-fa9a66e71ad5 | -11.2607 | -45.5078 | 2026-10-06 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 7fe94be1-4213-3484-b296-735e4fd5ac3b | -12.7678 | -44.8671 | 2026-10-06 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b6935ad5-66f1-3a1b-8a7c-afbe44071b99 | -11.2603 | -45.5308 | 2026-10-06 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| cbc83b7a-d19d-39a9-a32a-9518e3b6d1d6 | -9.8828 | -44.794 | 2026-10-06 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2435b4c7-97e2-3ada-868c-6ba134574a7c | -10.9762 | -45.4094 | 2026-10-06 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 680c58a8-3cdc-3c9b-b276-570eb681c3c8 | -11.2798 | -45.5052 | 2026-10-06 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| eb0c8dae-0ce2-3eed-99d2-b9e1ea665654 | -11.2607 | -45.5078 | 2026-10-06 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 92b0b547-431e-321f-ab1a-d11b1fba1c2e | -11.2603 | -45.5308 | 2026-10-06 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| d178b51a-0eca-33e4-a09e-8d4f04628e09 | -11.3562 | -46.6522 | 2026-10-06 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| fed3a702-b1ba-3b5b-bc5e-c06005ba230e | -11.2798 | -45.5052 | 2026-10-06 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f78c2bfd-0479-322a-9e0f-f3e55f3ee1b5 | -11.2607 | -45.5078 | 2026-10-06 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.1 |
| c77faec8-3186-3f0a-9cc5-7e1f416760f9 | -11.2798 | -45.5052 | 2026-10-06 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2adfd482-0dab-3a89-a040-985d6fd9fdf7 | -11.2607 | -45.5078 | 2026-10-06 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.5 |
| 86251d5a-394f-3482-9263-acbf07adb688 | 2.4585 | -50.8299 | 2026-10-06 12:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 33b3e7ab-c87d-36c2-a286-0001c0816c1f | -10.9762 | -45.4094 | 2026-10-06 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 03ae100e-bb94-3765-91fb-13b297b240fd | -8.5847 | -45.6502 | 2026-10-06 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0819d92a-55e2-38fc-bca3-84f96ba31061 | -15.5222 | -42.6342 | 2026-10-06 12:20:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.9 |
| 0e0714ee-356d-31f4-84ea-f99f45f21509 | 2.4585 | -50.8299 | 2026-10-06 12:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 3c08b324-302e-37a3-b4cb-99b5ff7bfaee | -10.9762 | -45.4094 | 2026-10-06 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2102ed4d-bc6d-35b4-b7b5-d4f83ff59664 | -11.3562 | -46.6522 | 2026-10-06 12:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 50be5180-64a7-3331-833a-690faaeaf76d | 2.4584 | -50.8507 | 2026-10-06 12:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 80e5b25d-6812-39f2-93ca-03c71eda9635 | -11.2603 | -45.5308 | 2026-10-06 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 60a8c89d-d81b-3155-891b-72fc79942a89 | 1.78724 | -55.58294 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| af281140-7e70-3f8d-9655-e7262b29c362 | 1.60831 | -55.76881 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2bbd84de-262e-35ed-b757-42d1629aafe6 | 1.49281 | -55.68374 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 9f705751-7168-3dc9-b807-e75e5e1a653d | 1.72326 | -55.62565 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 2b05ee43-e454-3a68-babe-e599e965a939 | 1.62271 | -55.79333 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 00fa3c80-78c3-394b-bd22-3c01632368a3 | 3.1258 | -60.58506 | 2026-10-06 12:36:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8169cb81-8293-3ff4-8b57-cc54cb3c0a41 | 1.71446 | -55.64041 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 80922a6d-f642-32d5-95c2-f4d74b872b0d | 2.93018 | -60.1259 | 2026-10-06 12:36:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 4432c24b-7386-303c-ad1c-c61602d0900f | 1.97629 | -55.88268 | 2026-10-06 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 028ea2ef-e866-389d-b249-ab93cd0988eb | 1.98387 | -55.88794 | 2026-10-06 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1add1b16-1431-3cc7-a959-f720b3c3f1e9 | 2.23589 | -55.84057 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d90b5de8-2ad2-3f50-b38d-f38b7d325d3d | 3.50806 | -51.27476 | 2026-10-06 12:36:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 86a19409-c32a-3bef-9749-2044d4bb605e | 3.06025 | -60.58191 | 2026-10-06 12:36:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| b57995d8-4ed8-31a0-9781-98a04cc8d72b | 1.78139 | -55.54264 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cd5ddb5f-02d1-3727-b769-8998b1e95d22 | 3.32028 | -51.34306 | 2026-10-06 12:36:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 096dd2d7-1743-3890-8d52-6a3440024dab | 3.5229 | -51.27935 | 2026-10-06 12:36:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 28.8 |
| def98e5f-63bc-3584-88e3-9c41fa4be661 | 1.62082 | -55.78041 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 70ab220c-7f4c-3e29-9572-313a2be56dc3 | 1.79215 | -55.5411 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| fbf0564b-8232-335d-acfe-0dcd316a0ef9 | 2.01532 | -61.08681 | 2026-10-06 12:36:00 | TERRA_M-T | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 66725753-0e95-39fc-9f72-667cc01ba76e | 3.12453 | -60.57606 | 2026-10-06 12:36:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 664fa62a-2853-3a09-a8fc-d87942818023 | 2.45476 | -50.84582 | 2026-10-06 12:36:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 109.9 |
| bdab1fbf-d4fe-3416-a4f6-4c822a97c664 | 3.50813 | -51.28158 | 2026-10-06 12:36:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d911340e-b128-342c-998b-38c17e6d2dc2 | 1.7853 | -55.56953 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| b5ebf443-4eda-3e53-954a-10262e2ee05b | 2.04473 | -55.86643 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 49a12c5d-114c-35b4-8aa5-071d6280288e | 2.04292 | -55.85375 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6a236841-01c5-3a51-b682-421401c96459 | 3.06152 | -60.5909 | 2026-10-06 12:36:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 26.0 |
| cc6969fc-0444-3565-ab56-40f8e877e2fe | 0.72079 | -51.39993 | 2026-10-06 12:36:00 | TERRA_M-T | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7ad6cd2f-dcca-3051-8285-4c0099021552 | 1.982 | -55.87526 | 2026-10-06 12:36:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 85c5fa9d-6692-336b-a462-01015458b578 | 2.92892 | -60.11711 | 2026-10-06 12:36:00 | TERRA_M-T | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 68a8b8f8-457f-3705-a4d0-2a85add41f97 | 3.05262 | -60.59212 | 2026-10-06 12:36:00 | TERRA_M-T | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 03993f5d-3e20-34d9-bcef-ea339505154e | 2.4504 | -50.84149 | 2026-10-06 12:36:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 91.9 |
| a4ccb052-fec2-3d3a-b03c-53f01493f2ef | 3.52283 | -51.27255 | 2026-10-06 12:36:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 05de7216-5267-309c-a78e-4f2844d79151 | 3.32012 | -51.34995 | 2026-10-06 12:36:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 5edca808-9bf9-3165-9161-877d090ec0b4 | 1.48704 | -55.67694 | 2026-10-06 12:36:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ecaa578d-84f4-3dcb-b7ea-01b3cde42130 | -3.09737 | -54.17725 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a3a26667-c1b9-3531-ad28-cfc85d577bcd | -3.70793 | -58.93272 | 2026-10-06 12:38:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 60a73cb3-d8e5-3a42-b27e-22aed5988005 | -3.01647 | -53.89957 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 983e573b-1294-3db5-8f3f-047a123d3b1c | -3.71721 | -58.93397 | 2026-10-06 12:38:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 30087b82-8799-32cb-a2a6-7db3f1906f9d | -2.32229 | -57.98623 | 2026-10-06 12:38:00 | TERRA_M-T | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 1d9a44c2-5704-3715-b829-dcf00238dc0d | -3.02986 | -53.90132 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 586.9 |
| 472910be-b6cb-372d-a4c2-04775f1aee97 | -2.95667 | -59.16246 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd7e84d7-c9ce-317f-914a-2f92f999dcdb | -3.16842 | -58.63042 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e9bd8a01-1264-37bb-ab2f-0743135d5fcd | -2.99809 | -54.13601 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 076a47b0-0c52-31ff-86f8-41c50dc19879 | -3.33583 | -59.48278 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| ac754dd8-fe75-3764-8572-4c4b1cbb2bae | -2.95845 | -54.14612 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 3213b4af-f944-3d03-98f8-d465f4eff7df | -2.49488 | -56.14296 | 2026-10-06 12:38:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 171fa081-1cfb-31c9-b50a-1954f18bbe84 | -6.68879 | -55.20163 | 2026-10-06 12:38:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| bd18b8a5-42b6-32c8-9308-f32d40d98775 | -3.34485 | -59.48403 | 2026-10-06 12:38:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 34b5240e-55f4-33ca-9a0d-f44714907bb3 | -1.6167 | -55.10812 | 2026-10-06 12:38:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 23ff262f-1878-3c58-b3c4-96a7731b59e4 | -3.49087 | -59.16623 | 2026-10-06 12:38:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3838759e-f986-3472-9739-d378750d89c5 | -3.29478 | -57.85534 | 2026-10-06 12:38:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fdef8573-c712-3a71-b0a8-8f51abafba55 | -3.37958 | -58.1931 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| d38a7f86-f2fd-3abb-9e50-281d8cea2166 | -3.65911 | -58.55277 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 439916fc-bd0a-3b21-90d7-0419a5e1a821 | -3.074 | -54.15272 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| dcda447a-907a-3ce5-98b9-172e9d4b6832 | -3.37808 | -58.20375 | 2026-10-06 12:38:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4b8ae455-da1c-31a0-8476-6f7fef07d750 | -2.1559 | -59.99965 | 2026-10-06 12:38:00 | TERRA_M-T | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 09b1639b-526e-39d5-98a6-b1e45765d080 | 0.44261 | -60.53783 | 2026-10-06 12:38:00 | TERRA_M-T | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 116.2 |
| f23fc900-9630-37e4-8033-7543b0a94370 | -6.45075 | -55.4328 | 2026-10-06 12:38:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| fe1bdea7-ffe4-3483-bc26-328325c1074e | -3.54741 | -59.48636 | 2026-10-06 12:38:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 07cc12e4-d9b7-30dd-8e30-eae5a9f5ae9b | -3.29048 | -53.83601 | 2026-10-06 12:38:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 26a1cea0-3ff2-3398-a374-527eb946f65f | -3.00092 | -54.11512 | 2026-10-06 12:38:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 3b1ba350-f0aa-3b75-bd37-2bdd98b27ed1 | -2.48757 | -58.29264 | 2026-10-06 12:38:00 | TERRA_M-T | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 29d96e05-55ff-3422-a10d-9c841160e7ee | -2.78951 | -57.65888 | 2026-10-06 12:38:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |


[Clique aqui para ver as próximas entradas](README81.md)
