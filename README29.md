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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e6ae902-4cd3-337d-8026-efa23796cec9 | -9.3808 | -61.5124 | 2025-08-10 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 01787ff4-ba6c-31f1-8870-b03df092a2dc | -8.9399 | -60.7481 | 2025-08-10 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 5ea6b46c-55f1-316f-b7eb-992ed4e8ccd2 | -8.9401 | -60.7288 | 2025-08-10 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 5631360f-a582-3f2e-80a5-b9c74cc49a46 | -8.9213 | -60.7489 | 2025-08-10 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 0d3569eb-cf14-3aac-8510-8c03e62b6bfb | -9.3808 | -61.5124 | 2025-08-10 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 7835feba-9951-3dad-b5e0-e5b263a790f9 | -9.3806 | -61.5315 | 2025-08-10 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ada9aefa-f423-3abb-835d-c758def5178e | -9.362 | -61.5324 | 2025-08-10 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 034a981c-e7e8-3b89-9802-5207bd8f1ca8 | -9.362 | -61.5324 | 2025-08-10 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 41ad2f9f-263f-35fc-b61d-cce39c74271f | -8.9213 | -60.7489 | 2025-08-10 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 923f79ad-3c49-317b-b13a-842ac18cead1 | -9.3806 | -61.5315 | 2025-08-10 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 2aee2f25-3ea2-3de5-9dc4-2ab0dfacc395 | -8.9399 | -60.7481 | 2025-08-10 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4dcb524c-f60b-3ade-9e05-3ebdb0d876cd | -9.3808 | -61.5124 | 2025-08-10 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| d88f7726-84da-3eb4-b88d-922b9dde7f8c | -8.9215 | -60.7297 | 2025-08-10 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 80c091f1-56db-3421-9696-48d4c5916711 | -8.9401 | -60.7288 | 2025-08-10 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 177a52ca-259c-3c24-a7c6-45f349baf77e | -8.9399 | -60.7481 | 2025-08-10 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 9b6705aa-23e3-31d5-8bdc-e76e6ca1d427 | -7.4185 | -43.9823 | 2025-08-10 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3acf8ca2-3ba7-34bd-a69d-ea61867f812f | -9.3806 | -61.5315 | 2025-08-10 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e6673b3e-a3a6-33bf-89be-f2f9257b58dc | -7.4182 | -44.0055 | 2025-08-10 06:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c05e11cd-c7ba-37a0-85a6-cf2af35a8e2a | -8.9213 | -60.7489 | 2025-08-10 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a409e980-9a81-3546-8424-70649990893a | -7.0614 | -59.1972 | 2025-08-10 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| a320f61c-6642-3067-84aa-a22cf46ee70b | -7.0799 | -59.1964 | 2025-08-10 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6161d4e7-5531-3b20-8847-96977b369a21 | -8.9399 | -60.7481 | 2025-08-10 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5239eba9-0b6e-3bee-9e10-83c56e2323ed | -8.9401 | -60.7288 | 2025-08-10 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 49218ad3-3629-3dc2-b520-2a7042541a62 | -9.3806 | -61.5315 | 2025-08-10 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 1b539a7c-14bb-3bfb-939e-075eb5e0174e | -8.9215 | -60.7297 | 2025-08-10 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| ebcd98bf-e7d9-32e4-86d3-358dff0e00c6 | -8.9213 | -60.7489 | 2025-08-10 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 25dd5d02-f4a2-33ef-bf17-9c5052108c0d | -7.08 | -59.1771 | 2025-08-10 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3abaa6ce-ff65-3820-ab75-67730ebe1c8b | -7.0614 | -59.1972 | 2025-08-10 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f6778672-7f51-384c-bccb-6f500e82c9c3 | -8.9213 | -60.7489 | 2025-08-10 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e0f5f9aa-1bf2-371d-836a-b9e679c16bad | -9.3806 | -61.5315 | 2025-08-10 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 23d0896c-d459-3f76-937d-d9269f2c6d53 | -7.4182 | -44.0055 | 2025-08-10 07:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 47.8 |
| f71e6473-c13e-37d4-9108-57f70e9da536 | -8.9399 | -60.7481 | 2025-08-10 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 798b6a1b-20b7-39ba-b620-ee79d40e28cd | -8.9215 | -60.7297 | 2025-08-10 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9f593620-cb9d-3b4b-9b1a-3f84e45abcfe | -8.9401 | -60.7288 | 2025-08-10 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 3ac92b6c-14c3-3bcd-93c9-0af4938b0a4d | -7.0799 | -59.1964 | 2025-08-10 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 4d252ea9-b4e7-3c2f-83ec-26a8c38723d6 | -7.0615 | -59.1779 | 2025-08-10 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 96c88f92-4791-3305-9add-3e1444bce0b5 | -8.9213 | -60.7489 | 2025-08-10 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 1e7684c0-89af-3ac8-a198-cfd195dd5313 | -7.0799 | -59.1964 | 2025-08-10 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1b20cfe6-9154-3b21-8d4d-1dbc4d6f1623 | -7.0614 | -59.1972 | 2025-08-10 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0f14da88-256c-3128-95ad-4eeab9b0678f | -9.5012 | -46.295 | 2025-08-10 07:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b009050d-1b2c-3577-94b4-60886b72da92 | -7.0615 | -59.1779 | 2025-08-10 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9dde96f9-be29-3a34-a5c9-d392276ef553 | -7.08 | -59.1771 | 2025-08-10 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 79acbd71-9ec2-3217-a278-dd1f3153e49e | -8.9401 | -60.7288 | 2025-08-10 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 825bfe13-fe8a-3245-bfb1-0deb8f94f7b3 | -8.9399 | -60.7481 | 2025-08-10 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e1a08bc8-77c3-3aff-9a6f-f30bc9a5d8f3 | -9.5015 | -46.2725 | 2025-08-10 07:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 951dddfd-2934-384d-9918-c73ebf240c71 | -8.9399 | -60.7481 | 2025-08-10 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 916d4623-3e81-3185-8b41-fda5ef59098e | -8.9401 | -60.7288 | 2025-08-10 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e45d9793-ed54-389e-8390-65ec7d151cbe | -8.9215 | -60.7297 | 2025-08-10 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 219da671-b7fe-385a-8445-03ed96e7ec6f | -8.9213 | -60.7489 | 2025-08-10 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a61178ef-7e09-3d9b-8b8f-19767f0f81a2 | -8.9215 | -60.7297 | 2025-08-10 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 7ccc0ad5-73f1-33fe-b6f5-4baa98e2614a | -8.9213 | -60.7489 | 2025-08-10 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a97f7ed0-f4b8-3a33-b0e2-6458d0a3a65b | -8.9401 | -60.7288 | 2025-08-10 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b2cfd819-4a32-3e4f-8f10-b3ed53d13589 | -8.9399 | -60.7481 | 2025-08-10 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| be029689-590f-34b4-b82a-7becf4b06c5e | -8.9215 | -60.7297 | 2025-08-10 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 4b587922-aa48-3a7e-8bf7-4ac7cf21bc4a | -8.9213 | -60.7489 | 2025-08-10 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 85f2bc1e-cfeb-30e0-a74e-00d375cffabc | -8.9399 | -60.7481 | 2025-08-10 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fa73ef34-e177-34b8-a5c3-56c008d6d37f | -8.9401 | -60.7288 | 2025-08-10 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 3a1eefbe-a174-3a4b-8cb8-dce0720a78ff | -8.9399 | -60.7481 | 2025-08-10 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| eaf99548-4b9b-3494-be9c-f43d8143b34e | -8.9213 | -60.7489 | 2025-08-10 08:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 04338838-3b9d-3908-a3e8-96fbf42d05da | -8.9399 | -60.7481 | 2025-08-10 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| a2a9288b-1428-3265-8c1c-d5ec9654a2a0 | -8.9399 | -60.7481 | 2025-08-10 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| d16e1d4e-859e-3664-b779-f930b1ca9a24 | -9.3806 | -61.5315 | 2025-08-10 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 14b158fe-9b29-3464-b2d1-e7f3a4e094b3 | -9.362 | -61.5324 | 2025-08-10 08:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 60103b32-361d-30ae-a28d-81e06f1c78d2 | -9.3806 | -61.5315 | 2025-08-10 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| ca1053c5-c4f2-39a6-bfdf-160c208c0663 | -9.362 | -61.5324 | 2025-08-10 09:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| acf47c96-fa30-34d2-b981-f14e0d682201 | -9.362 | -61.5324 | 2025-08-10 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 79f7559d-9ea0-33ed-88ef-edeef55d3659 | -9.3806 | -61.5315 | 2025-08-10 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a3dfc1f5-8d40-37f9-96e0-98da5c175755 | -8.9399 | -60.7481 | 2025-08-10 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| bea11ade-11d7-32aa-ad1a-8af58063f5c6 | -8.9399 | -60.7481 | 2025-08-10 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7e6b01c3-2227-30f8-a906-ab6d756a7d7d | -8.9213 | -60.7489 | 2025-08-10 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a88d3e68-4fcf-308c-9de6-b7b48e0c4ed5 | -7.4373 | -43.9804 | 2025-08-10 11:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a172e07f-f314-3e3a-ac88-cf339157ab34 | -14.1108 | -45.3844 | 2025-08-10 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 98ab6131-b5eb-3113-8642-333f42c0056e | -14.1103 | -45.4077 | 2025-08-10 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 8a1c5fda-a4bb-3a26-97b3-2028ae599112 | -14.1103 | -45.4077 | 2025-08-10 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| e75c28f1-8945-32a5-8863-dc85979c3560 | -14.1108 | -45.3844 | 2025-08-10 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 9efe1487-81e0-34c0-91c4-f5b6d95881fe | -14.1103 | -45.4077 | 2025-08-10 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 1a419c27-5a37-30c5-9034-8e27d5cce402 | -14.1108 | -45.3844 | 2025-08-10 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 148.7 |
| a1624873-99d8-38be-9f4b-7bc806c1aa7b | -7.4373 | -43.9804 | 2025-08-10 11:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b85f6488-9adb-3964-8295-61d010b14269 | -14.1103 | -45.4077 | 2025-08-10 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| ff270910-1f31-32b2-b82f-62541f470c3a | -14.1108 | -45.3844 | 2025-08-10 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 166.8 |
| 071a52bf-8774-301d-8dd7-073e2c9bcf1e | -11.747 | -45.0246 | 2025-08-10 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| f50948e8-8dbb-3add-9ac9-f68288d5d2a3 | -14.1103 | -45.4077 | 2025-08-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 1c78c1d9-d5c4-3ebd-819d-d58e8d89732f | -14.1108 | -45.3844 | 2025-08-10 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| a712426f-f434-3457-b341-f12b52aafa5d | -11.7278 | -45.0274 | 2025-08-10 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 73c87200-f882-3277-9546-fd6a29cc7d81 | -11.7466 | -45.0478 | 2025-08-10 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| d83d405a-25a5-3532-bc37-bf7b538aefbb | -9.5015 | -46.2725 | 2025-08-10 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6034c6be-3ec3-32e3-9678-38be15d73a19 | -14.1108 | -45.3844 | 2025-08-10 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| cfc227ad-f080-33a2-9899-13107ba6991b | -14.1103 | -45.4077 | 2025-08-10 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 75eea535-5ce2-368c-8520-51ddf0046d44 | -7.437 | -44.0036 | 2025-08-10 12:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| f0deffc4-9f58-3ab7-a4ed-d403ba24c98b | -7.4373 | -43.9804 | 2025-08-10 12:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 173.3 |
| b523cfdc-d960-39b8-b95d-98bd901e14c1 | -11.7466 | -45.0478 | 2025-08-10 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 7687ff1a-3b1f-31c3-b4e2-8cf73810c3ea | -11.747 | -45.0246 | 2025-08-10 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 61898a30-bd4a-37cc-a8fe-1011ecec8631 | -14.1108 | -45.3844 | 2025-08-10 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 64b446cb-cf48-31f6-8ea8-8736d9150167 | -7.437 | -44.0036 | 2025-08-10 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 4b57d21b-0e44-3839-9d8a-20a68a032d02 | -7.4373 | -43.9804 | 2025-08-10 12:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 286.6 |
| 2e22ba9a-2746-3488-a47c-c8a3cfc260a6 | -7.3012 | -39.6453 | 2025-08-10 12:10:00 | GOES-19 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 135.1 |
| e54c2a6e-2803-32b9-828a-abc086de80e3 | -14.1103 | -45.4077 | 2025-08-10 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 385b6e33-77c4-3979-b8a4-7436d804cccd | -6.83544 | -42.90723 | 2025-08-10 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 1b0a0bcc-f6fc-31af-b0c1-8f929db7d907 | -4.58786 | -43.34816 | 2025-08-10 12:12:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ea1cc21-d253-394c-8727-da00da0f4661 | -6.5681 | -42.84206 | 2025-08-10 12:12:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 29.8 |


[Clique aqui para ver as próximas entradas](README30.md)
