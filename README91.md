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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 340e6259-5a59-3f99-a4d8-2005bebcae67 | -17.07087 | -56.80153 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 66b52691-3945-3af9-8e5f-521023148817 | -17.06494 | -56.8012 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 68dfd84e-281f-344d-b9ca-205e4ef2245f | -17.06447 | -56.79999 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4adb0dd2-e961-3fa8-a76a-03f281223672 | -17.05855 | -56.79964 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9169573a-e04c-3735-ad1a-e48d4ef500e3 | -17.05809 | -56.7984 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3734ec35-6c1b-361c-ae8a-342a14e64399 | -17.05343 | -56.79255 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a660c973-d360-3a5e-a2ef-426715125db8 | -17.0517 | -56.79683 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 61c37aaa-8924-3813-934c-6f66013e0557 | -17.04703 | -56.79104 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 88b0f610-e1c5-3c17-982d-2994dbdc3a46 | -17.04654 | -56.78974 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 6601ffa2-bc56-3f4c-b896-0b4f996865c1 | -17.04342 | -56.7131 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0c8e55a9-da7f-33d0-9c82-3562ebccd09c | -17.04191 | -56.78397 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2d941732-2545-393d-b0a3-dad266dab5bd | -17.04138 | -56.78263 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b3c8a589-0d8b-3475-b54f-eaf0dd45e93a | -17.04064 | -56.78952 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| d25799cb-41e5-3747-aba8-f310d5dd18d5 | -17.04014 | -56.7882 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e72418b6-ff0c-3dcc-bd58-e93cfe48c60b | -17.0389 | -56.79377 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1828ea9d-9587-3645-83e3-e5a21b0b4301 | -17.03827 | -56.70608 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b92817d6-c9be-33d7-b4ae-50d1dba707a2 | -17.03705 | -56.71157 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0ac6ce7f-cdb4-30c7-87fa-9d2433322f39 | -17.03679 | -56.7769 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7b97b5fe-97b6-3244-9d18-104a0f3cb343 | -17.03623 | -56.77551 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 58956a1b-813e-3d0c-a596-b4d111de0617 | -17.03551 | -56.78246 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e4b84d1a-5c7f-399b-9b02-9088ef1dd23e | -17.03499 | -56.78108 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dc9e593d-4f9f-3d76-9be9-a6b9bdb50022 | -17.03424 | -56.78802 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e9bee3ad-1424-3feb-8278-61008ead6cb1 | -17.03375 | -56.78666 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| baedceab-3428-32f6-8693-950a2dfcdf27 | -17.03294 | -56.76432 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 58a038b6-ba74-3f8d-83de-09476e46b28e | -17.03167 | -56.76985 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a2b13abf-448a-3382-a605-e50444340306 | -17.03039 | -56.77541 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| abb3c38f-ecaf-3624-80aa-bd3cf3b797c2 | -17.02984 | -56.77399 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 90bc12b8-bfe6-3535-97ce-ebfd07cf0610 | -17.02911 | -56.78098 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1fa4a98f-5d37-3e9d-acc4-d31d35174907 | -17.02859 | -56.77958 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 77170aea-5cad-323f-b510-a7d9520c9bb1 | -17.02783 | -56.78653 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e990a00a-2e89-307c-aff0-063a4c5911d0 | -17.02735 | -56.78515 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 2c294071-68b9-33a3-b903-6d8c062e471c | -17.02327 | -56.74319 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d8146c5e-230a-3b45-8016-1374391f22a0 | -17.0222 | -56.77805 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e650043f-8b0a-3edb-b6ad-9926229bf8ee | -17.02096 | -56.7836 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 94042de5-b88c-3f74-88fc-ac7c85a1d528 | -17.0183 | -56.76539 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| c6c4a706-5255-3958-9afe-6692deb2854e | -17.01689 | -56.74166 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.2 |
| a09ebc67-7ad5-3040-9b09-b25f7f270d5b | -17.01581 | -56.7765 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c658ac36-5fb6-3e0d-8946-fa7fe46cfea3 | -17.01565 | -56.7472 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| b7813598-71dc-3944-b177-9de525dfe8aa | -17.01456 | -56.78206 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| fc3b9daf-2f1a-3a77-a830-9c5085d88a1d | -17.01332 | -56.78764 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 5f2a4b55-495c-32d0-8fe2-78e2b7d19015 | -17.01191 | -56.76386 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cb7ab298-b2a8-38cc-8856-eb7ed62af84a | -17.01066 | -56.76942 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 0592748c-f817-3954-91fd-2d416853ffb3 | -17.00941 | -56.77499 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 3c22f4cb-19d3-3bd4-81cb-0600dc388f2a | -17.00926 | -56.74568 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 414182e2-1926-3064-ae00-d98c30c59125 | -17.00817 | -56.78055 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 0ddba80f-6caa-3f82-b67f-e16a2116de32 | -17.00801 | -56.75124 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 266cc87f-0fc0-306e-84db-a4465e2d5efb | -17.00692 | -56.7861 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| 176d3c8a-a1b4-3d2d-ab18-562f9073b785 | -17.00677 | -56.75678 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9b9bf843-d92d-3d14-af58-e1c752a39331 | -17.00552 | -56.76235 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e3eef809-a4ba-3b2a-839c-adb81844d590 | -17.00427 | -56.76789 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 9798921d-893c-39d8-9c56-e07abc9d98b1 | -17.00302 | -56.77345 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 006d7811-5ce1-3b9a-ac4e-aa258bcc8fdd | -17.00288 | -56.74417 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d7bd6d37-1a8a-3dfc-8203-c7b90c2cf7fa | -17.00177 | -56.77902 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.0 |
| ddfa7ecb-bc23-3ff7-90aa-f813d61e10cb | -17.00163 | -56.74972 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| dd72a351-c825-3c63-b713-f7752435d057 | -17.00038 | -56.75526 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 76817cc9-3d00-32a8-ad26-f8af115c6761 | -16.99788 | -56.76635 | 2024-10-04 04:12:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| f767043d-e116-3cd5-ac76-0a651b3499b8 | -29.87259 | -51.15692 | 2024-10-04 04:14:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| ddf8bce1-906d-3c44-b53a-7162b8ef243e | -29.8163 | -51.17585 | 2024-10-04 04:14:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| da1e4778-c228-38e1-b92f-887bdf605873 | -23.2565 | -54.93617 | 2024-10-04 04:14:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5f3f9853-1bcb-3f20-b5a9-495470e4a6ce | -3.2899 | -50.4725 | 2024-10-04 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| a73632b1-c013-32f4-9a4b-824638f8b353 | -3.2899 | -50.4516 | 2024-10-04 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 183.9 |
| 44bf6503-c6f6-3713-8bad-d318dd9c8ee8 | -3.29 | -50.4306 | 2024-10-04 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e2f6db3d-3065-3ca9-b8ac-5ad486600ea9 | -3.3083 | -50.4719 | 2024-10-04 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 87f12042-397b-34c4-b952-d5b133c9b32e | -3.3084 | -50.451 | 2024-10-04 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 227.4 |
| 5360fb49-5da9-3ceb-bba9-ed2bad1c8cd5 | -3.3085 | -50.43 | 2024-10-04 04:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ed2605f5-8796-3c5e-a56b-e1eeb6934a9d | -4.0763 | -48.4902 | 2024-10-04 04:15:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e1263f2d-302d-3be1-8f3c-7522608a0060 | -4.0949 | -48.4894 | 2024-10-04 04:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| baa7c771-bb3b-32c8-91c4-b79aef0bebcc | -4.095 | -48.4679 | 2024-10-04 04:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| eb965646-c2e2-3e3f-b4a3-46e458cd7065 | -4.5375 | -43.304 | 2024-10-04 04:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 199ba1da-120f-3f48-b025-2e479d7a8386 | -4.6684 | -45.8961 | 2024-10-04 04:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 8ffa91cb-551f-3989-89b9-858731e13e48 | -4.6686 | -45.8738 | 2024-10-04 04:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 42e61d59-7b91-3bdf-9e0d-e1a880a82aa0 | -4.687 | -45.8951 | 2024-10-04 04:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| b62e3814-daea-32c2-b962-176656b85763 | -4.6872 | -45.8727 | 2024-10-04 04:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 03577572-780f-3619-81f4-4c2c83862e63 | -6.8961 | -47.2319 | 2024-10-04 04:15:45 | GOES-16 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e9e3e33c-976a-3da0-afcb-afd69d215e1c | -7.0529 | -71.7544 | 2024-10-04 04:15:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 26813fd1-7909-344f-97de-608919199970 | -7.6262 | -45.5413 | 2024-10-04 04:15:49 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 6d7b9c34-bf59-3695-9c3c-8a6f919220d8 | -8.407 | -46.2987 | 2024-10-04 04:15:53 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| c3f63caf-1805-37db-9a10-f8f7897d03be | -8.8771 | -61.8409 | 2024-10-04 04:15:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6edebc74-5654-3062-9e16-da9f76311720 | -8.8772 | -61.8218 | 2024-10-04 04:15:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3d40dcfa-9179-360a-a32e-70fc2fb5f892 | -9.845 | -68.9623 | 2024-10-04 04:16:03 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 54.7 |
| f0909030-7db5-395e-8bcf-a5cceabc0599 | -10.4775 | -48.1829 | 2024-10-04 04:16:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 0837c559-d378-350d-9437-2e8eae6b5a78 | -10.4964 | -48.1807 | 2024-10-04 04:16:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 9534528e-fab6-3a91-9827-d723d2da4b36 | -10.4968 | -48.1587 | 2024-10-04 04:16:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 49b29ec8-7063-3199-874d-9ce3752464d0 | -11.0914 | -46.5294 | 2024-10-04 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 394c2027-cecf-3328-97b8-786e5f0ab63c | -11.0918 | -46.5069 | 2024-10-04 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 9502c7f1-b444-372d-bfa8-ea16945fb5fc | -11.0921 | -46.4843 | 2024-10-04 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ca96747f-b318-31b5-bd6e-d07f846fd501 | -11.1108 | -46.5044 | 2024-10-04 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 7f68ed08-00ff-3336-938b-a42ca4493c05 | -11.1112 | -46.4818 | 2024-10-04 04:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| c6a5453f-fa7c-350c-87c3-c16a512d7f02 | -11.2566 | -60.5825 | 2024-10-04 04:16:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 77f424f6-2e99-3321-8d5a-d2ad3188db91 | -12.5898 | -53.1359 | 2024-10-04 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 9108a8ef-fac2-30b5-88a7-a175157b020d | -12.5901 | -53.115 | 2024-10-04 04:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 128.6 |
| 76900d3e-cb77-3e55-bc19-753bb5592a5e | -13.1166 | -51.1551 | 2024-10-04 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 6ce52460-017f-3557-a1f5-3fb788bbe992 | -13.1447 | -46.3033 | 2024-10-04 04:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 51ff05e9-bc91-3ae1-9e29-4090d59c429d | -13.1451 | -46.2804 | 2024-10-04 04:16:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 0fcdaf0b-f219-36fb-9041-b02ed9569e16 | -13.0598 | -51.1195 | 2024-10-04 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a4c2b539-87f9-3170-a3d8-e2f96aaf57d5 | -13.0786 | -51.1385 | 2024-10-04 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c6f86bd1-a376-318c-ad8b-40bd5578bd07 | -13.079 | -51.1171 | 2024-10-04 04:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3d243cdb-838d-32c7-ab12-2dc327e8c93b | -13.117 | -51.1337 | 2024-10-04 04:16:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| f97cea4b-cb12-3ec8-802d-9f5c7fa1181e | -14.7939 | -48.0275 | 2024-10-04 04:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 0a1e7cab-39b0-32c1-90b4-52d7fa198614 | -16.1094 | -50.4489 | 2024-10-04 04:16:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 49.0 |


[Clique aqui para ver as próximas entradas](README92.md)
