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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f801abb0-317d-38ee-a1bd-f6358e6425ca | -6.9156 | -43.5418 | 2024-12-05 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| d22741ea-3f88-31fc-a06b-95d364277472 | -1.4915 | -46.1464 | 2024-12-05 01:20:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bba75a6c-8ddc-35bc-b0a6-cfaf7811a779 | -6.9344 | -43.5401 | 2024-12-05 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 950563cf-bb84-3f03-9099-0c9a03a19d3f | -2.1724 | -54.6263 | 2024-12-05 01:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| f952651f-e4de-3cbb-902c-aa55a5d0a008 | -9.374 | -57.5553 | 2024-12-05 01:20:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 52a32fb1-7b49-318c-bf1b-047ebbfd9b45 | -6.9346 | -43.5168 | 2024-12-05 01:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| dba26d34-4d54-37f3-bcb9-fe040c573d58 | -2.4319 | -53.6584 | 2024-12-05 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 762325c8-d364-3dca-8f30-5d26d75fa715 | -17.3539 | -40.212 | 2024-12-05 01:30:00 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 106.7 |
| 34757b30-2c6c-322c-8e7a-a6d523bad068 | -9.374 | -57.5553 | 2024-12-05 01:30:00 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b09f758b-f07a-3faa-9210-899016e6180d | -17.374 | -40.2065 | 2024-12-05 01:30:00 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.6 |
| 7e6f1e64-14b1-34a8-84e4-e0121c7b1775 | -6.9156 | -43.5418 | 2024-12-05 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 255ebac9-65ce-3c82-9bce-bc5752f74309 | -6.9532 | -43.5384 | 2024-12-05 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 610ade3d-d225-3f28-ac68-5eed984a637a | -2.4319 | -53.6584 | 2024-12-05 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 0dd07d34-8960-30ba-aba3-b25bff074552 | -6.9344 | -43.5401 | 2024-12-05 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 161.0 |
| eb910042-6072-3d42-b302-7fb7a11fbfb9 | -3.9999 | -48.9226 | 2024-12-05 01:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 776042bd-66ee-395c-bd69-c3576a18f99a | -2.1724 | -54.6263 | 2024-12-05 01:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 189cd5dc-1070-3a5c-a103-aafe68f44054 | -6.9346 | -43.5168 | 2024-12-05 01:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 5e108b23-a2dd-3e7e-9599-9829f0910164 | -11.94905 | -55.15347 | 2024-12-05 01:32:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9354c8b6-5365-3061-a498-ddb907a75279 | -9.36467 | -57.56239 | 2024-12-05 01:32:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 8d01ec98-b7eb-3e44-9a39-16710c4c233d | -11.82967 | -57.8144 | 2024-12-05 01:32:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a80652d-3253-33d6-b18b-aff8bc1ac235 | -13.84213 | -59.66387 | 2024-12-05 01:32:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c20dd1d7-180e-31cc-ba63-6a0916fe9f38 | -11.82203 | -57.82475 | 2024-12-05 01:32:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d4c57840-6b09-377e-b390-388bc6137c14 | -11.83092 | -57.82345 | 2024-12-05 01:32:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 70d2e30f-23fc-394d-afcd-e217c324743c | -12.53703 | -57.73668 | 2024-12-05 01:32:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0524e60b-dc3e-33ef-a341-131b59330e3a | -15.07483 | -59.64916 | 2024-12-05 01:32:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 553218dc-9be9-3217-baf4-f93b586c9c2d | -11.82078 | -57.8157 | 2024-12-05 01:32:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8c031a71-da45-398c-ac7b-15f038dd644d | -13.83245 | -59.66512 | 2024-12-05 01:32:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de228476-53c9-39cb-8ab0-bb10ae7362b5 | -9.37354 | -57.56109 | 2024-12-05 01:32:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 0ee5fe16-ee8e-3c70-be73-ac567b023b38 | -11.7697 | -54.6929 | 2024-12-05 01:32:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 516a9389-e81a-39bf-a3bf-4afe6d23e910 | -11.94756 | -55.14326 | 2024-12-05 01:32:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1b3b7adb-70e1-3c4d-bdf1-ffb02d8c0254 | -12.52142 | -54.37289 | 2024-12-05 01:32:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02376cb1-7f65-3739-8290-185d4b097ea2 | -11.89717 | -54.79879 | 2024-12-05 01:32:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 972d2b82-5a82-39bf-8eda-e22a9384122f | -15.09305 | -59.63516 | 2024-12-05 01:32:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 0a307e0e-446c-36ff-a10e-0fd3029f12d1 | -9.37228 | -57.55212 | 2024-12-05 01:32:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9fb0ab36-9d98-3b27-a9bc-f3b0081579a1 | -11.8125 | -57.806 | 2024-12-05 01:34:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80f1902a-7b55-3d2b-b9cf-227c6f1b0403 | 0.75069 | -59.65753 | 2024-12-05 01:34:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0f72d738-0ad0-3dc2-81f0-43e77a993d34 | -2.43534 | -53.6615 | 2024-12-05 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8e338827-d777-3516-b2e2-3ca4dc18df89 | -2.43154 | -53.66751 | 2024-12-05 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 448944e9-0dc4-3f4c-bb8a-a9cb42bd9e66 | -4.00605 | -48.92974 | 2024-12-05 01:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 65085083-3d80-3ff5-a41d-bd8204fb4022 | 0.1702 | -60.5948 | 2024-12-05 01:34:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d96f33cf-1b1e-37ae-8df0-a3c34f24b2a3 | 0.70227 | -59.87538 | 2024-12-05 01:34:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a31ddcbe-7d6e-3589-9d54-3800d101be61 | 1.03357 | -59.48071 | 2024-12-05 01:34:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7842209-dff3-3109-84e4-b2ec6bc77bc0 | -2.42907 | -53.65022 | 2024-12-05 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9e3c772c-1650-311e-a601-27450c57b7c9 | -3.88947 | -50.0871 | 2024-12-05 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| f88ef55c-eb16-33fc-a4d7-6a83aadee51a | -3.99778 | -48.89782 | 2024-12-05 01:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 80ff822c-34c9-396c-b7c0-25c7bb1179e9 | -3.89909 | -50.08018 | 2024-12-05 01:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| d995a2c9-950d-398b-9157-1acd74b4ec2a | 0.17144 | -60.58591 | 2024-12-05 01:34:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 860f8b15-aa8e-34c8-aea0-0c6c6a85ea00 | -1.68166 | -54.45442 | 2024-12-05 01:34:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| dd94229e-001b-32e8-852d-b0d02e728bc4 | 1.03233 | -59.48959 | 2024-12-05 01:34:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cd177c3-c553-31a0-8c5c-3fad74812fb8 | -4.00383 | -48.93725 | 2024-12-05 01:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 910fc5f2-b0a5-3006-ba6b-92b88e24e15a | -1.70501 | -52.6189 | 2024-12-05 01:34:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 957346eb-893b-3996-8b04-4bdd33002ef8 | -2.27041 | -53.53426 | 2024-12-05 01:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 1b9447cd-d8d2-3ed3-8366-3ac368683b67 | 2.4425 | -60.652599 | 2024-12-05 01:35:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f0d1b385-09c8-35c5-9123-660e37a94268 | 2.4328 | -60.650501 | 2024-12-05 01:35:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dce5e960-fc5d-3a5e-b7b0-691fae6c6a57 | -15.0858 | -59.624199 | 2024-12-05 01:35:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7037ac1-e082-3f58-8e84-180b125c74b5 | 2.446 | -60.636902 | 2024-12-05 01:35:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7219391a-aba4-3f12-8019-ea4eca5852cc | 2.4363 | -60.6348 | 2024-12-05 01:35:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6fc9188f-9475-3326-a8d1-c4fbca11064b | 2.57866 | -60.69587 | 2024-12-05 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 3e427a7c-0bbb-3e48-9558-f17646c97d9c | 2.47657 | -60.70206 | 2024-12-05 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27d019fd-4d2e-33e4-8090-d347cdb60911 | 2.4778 | -60.69324 | 2024-12-05 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 20516cf7-d9e2-3f46-8906-af149ec42ba2 | 2.42864 | -60.64448 | 2024-12-05 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.5 |
| ceb9f3e1-fd4d-391d-a079-cc11cf43df5c | 2.42741 | -60.65329 | 2024-12-05 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| cd8fb6a4-4f5e-3961-b31a-d21d87fcecb1 | 2.41856 | -60.65205 | 2024-12-05 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 62b5e482-f390-328e-88db-573db77c9879 | -6.9344 | -43.5401 | 2024-12-05 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 154.8 |
| c24d3182-4a61-3a9b-be04-4b3668d08345 | -2.1724 | -54.6263 | 2024-12-05 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7623fd1b-115f-378f-8c9b-2ec35dccd9ec | -3.9999 | -48.9226 | 2024-12-05 01:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7543c892-c1ea-32e5-88eb-32cac5016794 | -2.4319 | -53.6584 | 2024-12-05 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a0d9dbe0-5bdc-31cc-bd21-9853cca2d916 | -6.9346 | -43.5168 | 2024-12-05 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b266b416-7d05-35da-b09c-50d0e2826149 | -3.9013 | -50.0938 | 2024-12-05 01:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6359fea2-65f3-3a56-8bb6-43202803c43b | -2.1541 | -54.6266 | 2024-12-05 01:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4044dd91-683d-3d3e-92c1-6a63af6b711a | -6.9156 | -43.5418 | 2024-12-05 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d4a86f94-21ff-3bfb-8bd6-fd1bd7212141 | -4.0 | -48.9012 | 2024-12-05 01:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 81b27a05-a60b-3234-9365-9e18b01511d9 | -6.9532 | -43.5384 | 2024-12-05 01:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 6e10a890-3026-35db-80ee-a156d92edec8 | -3.9999 | -48.9226 | 2024-12-05 01:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 41e68014-5aed-3c5a-82da-2c5e7d6b6f5d | -2.1541 | -54.6266 | 2024-12-05 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 91210292-b28b-32ed-9307-2de69cafcfc9 | -6.9344 | -43.5401 | 2024-12-05 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 86397941-749c-35b9-996f-7b5e871ba097 | -2.1724 | -54.6263 | 2024-12-05 01:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 51556bdd-a80e-36e0-957f-63f45672d3d2 | -6.9532 | -43.5384 | 2024-12-05 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f5c1c27e-c802-39b8-92b4-5a6867dc46d0 | -17.8181 | -40.1115 | 2024-12-05 01:50:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| feb3f0a0-a6da-3280-b6d3-9148229cf877 | -6.9346 | -43.5168 | 2024-12-05 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 3a0f4695-2f5f-3406-972d-4b6eab0280a3 | -6.9156 | -43.5418 | 2024-12-05 01:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 0ab2bbdc-30eb-395e-b546-a794239d0160 | -3.8082 | -50.2236 | 2024-12-05 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3293f16e-b680-321d-a8c7-52e153efc3d5 | -2.1541 | -54.6266 | 2024-12-05 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c268ff6d-a366-3976-9470-cd88a6fc9151 | -3.9999 | -48.9226 | 2024-12-05 02:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| ef40a5f3-0130-3e86-b3d4-364aeae71d20 | -3.9013 | -50.0938 | 2024-12-05 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 153b051b-66c6-32e5-9778-ba9c9d792d00 | -2.1724 | -54.6263 | 2024-12-05 02:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0344f22c-f9f4-32ef-b360-f58cf8b41940 | -4.0 | -48.9012 | 2024-12-05 02:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9261f6f9-3d1b-370f-84af-0be1170084df | -6.9156 | -43.5418 | 2024-12-05 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 30f46c02-dafd-372a-bb6a-fea2ca26c212 | -6.9344 | -43.5401 | 2024-12-05 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 1a9c3944-75a3-3021-8e81-ea142edced3e | -6.9346 | -43.5168 | 2024-12-05 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e897a1a3-fdf0-3d55-ac3b-cb144135e5b4 | -6.9532 | -43.5384 | 2024-12-05 02:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8e67e23c-f1ef-33c5-825b-faa591a9560f | -2.1724 | -54.6263 | 2024-12-05 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| f434cdd4-76a5-367a-9742-6b066a400493 | -6.9344 | -43.5401 | 2024-12-05 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b9e0d05b-b833-37ab-8a3a-dba0dd84bef6 | -2.1541 | -54.6266 | 2024-12-05 02:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| d655f6c2-8730-3709-a6ff-2510b34882a5 | -2.2668 | -53.5405 | 2024-12-05 02:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 49be40b5-ee9a-36be-9aef-bd8728614eb6 | -6.9346 | -43.5168 | 2024-12-05 02:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| ff82232c-ccbc-31d2-bdb8-a3d6b9462d14 | -6.9344 | -43.5401 | 2024-12-05 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 38518cdc-9a99-345c-8107-0bd1cc004f6f | -2.1725 | -54.6063 | 2024-12-05 02:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| bc917e3f-f351-3897-a353-9901854c54e9 | -6.9156 | -43.5418 | 2024-12-05 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 314c9996-9d86-3522-ac71-696aa53f89bb | -6.9346 | -43.5168 | 2024-12-05 02:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.8 |


[Clique aqui para ver as próximas entradas](README4.md)
