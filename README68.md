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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2042cbb2-2c3f-349f-848f-a872537197f5 | -3.2569 | -54.2226 | 2024-11-23 07:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 202cbcc0-d6c4-3375-90b9-f55c34468f7d | -3.165 | -45.2722 | 2024-11-23 07:20:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c313c4c0-65f8-3ce5-a247-24ab3060b649 | -1.6075 | -52.5977 | 2024-11-23 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 69fb25fa-e952-3468-a5c0-41e1b674d647 | -4.5403 | -42.9066 | 2024-11-23 07:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| bff5f256-b731-36e5-8009-03340bb9b589 | -4.2605 | -48.697 | 2024-11-23 07:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7bcfc837-e640-3d18-a7ff-5cae3af91f91 | -4.5216 | -42.9078 | 2024-11-23 07:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 245acd11-00cd-3480-b615-603d245ad494 | -3.2386 | -54.223 | 2024-11-23 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 16a49b15-050e-318d-a097-6c2506422266 | -1.7359 | -52.7181 | 2024-11-23 07:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 1c0837a4-1359-35a5-982c-05ec592e1f92 | -3.1273 | -45.3861 | 2024-11-23 07:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 32db57a7-cbfe-3473-ac0c-c9fe5a06a1a3 | -4.6085 | -46.5002 | 2024-11-23 07:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 109.6 |
| b51bcfda-bba9-3ccc-945b-2207a4283f75 | -3.2569 | -54.2426 | 2024-11-23 07:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 961a2442-fa38-3242-b143-3f19276251d7 | -3.1459 | -45.3854 | 2024-11-23 07:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fd035810-81e4-3ed5-9fb6-be0c3ab9f660 | -1.7359 | -52.7181 | 2024-11-23 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7b961f40-06cd-3118-989f-df96257f74e4 | -4.6271 | -46.4992 | 2024-11-23 07:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7ae75bb7-420d-3dfc-8c6b-c85bf41535aa | -3.2768 | -53.8199 | 2024-11-23 07:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b57a507e-35e1-32bf-af3d-bfff46d06fda | -4.5216 | -42.9078 | 2024-11-23 07:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d1618de3-b4b0-3ab7-9637-e0e56412a7b5 | -4.5403 | -42.9066 | 2024-11-23 07:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 658363a6-0ce4-3524-ba3f-2b29549dd571 | -1.6075 | -52.5977 | 2024-11-23 07:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4e39b977-3ca9-3c41-8c05-ca1fc3de0de5 | -4.6085 | -46.5002 | 2024-11-23 07:30:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 98f76714-16d7-3a01-b1d1-c83e8255707a | -3.1822 | -45.5636 | 2024-11-23 07:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 194a3fb6-abd6-3031-afc5-5fae7f84af4b | -4.2605 | -48.697 | 2024-11-23 07:30:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| bb839eb1-a15d-3dad-8538-d2182bb9a955 | -3.1822 | -45.5636 | 2024-11-23 07:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8a95e502-2f8c-38f8-bc4d-a2a4ad6ee9a8 | -4.5403 | -42.9066 | 2024-11-23 07:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 75c522a7-e45c-3a5c-8a88-6be80b042ff5 | -1.7359 | -52.7181 | 2024-11-23 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| a5c4d2bd-1c63-3bfe-98c4-455a37291791 | -3.2768 | -53.8199 | 2024-11-23 07:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d137bca0-3b7a-366d-a07e-39b3fb59a4f1 | -4.5216 | -42.9078 | 2024-11-23 07:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 202c0a33-b9c4-333c-b9d4-e8fb18545ff2 | -1.6075 | -52.5977 | 2024-11-23 07:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| da91af2d-351d-3d98-a6a1-93ad1f4a54a6 | -4.5403 | -42.9066 | 2024-11-23 07:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f598e5d5-32f6-332f-aafb-caa1fc1bccc3 | -3.2768 | -53.8199 | 2024-11-23 07:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 729fd70e-36be-3e24-b0b1-49379071b7d2 | -3.1822 | -45.5636 | 2024-11-23 08:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e82c149b-b1be-3b14-bc69-6c170da3fe4d | -3.2768 | -53.8199 | 2024-11-23 08:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c5d90a3a-e732-3289-9665-bd6cb467f6a2 | -1.7359 | -52.7181 | 2024-11-23 08:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d7981692-5bcf-3f69-b579-2be834776483 | -1.7359 | -52.7181 | 2024-11-23 08:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 26ee5b9f-053c-3b09-9fb0-379e304f3c09 | -1.7359 | -52.7181 | 2024-11-23 08:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4e29e3f3-3821-3863-97d4-e5fa8556bb57 | -1.6075 | -52.5977 | 2024-11-23 08:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 8b4e7cfa-0b30-32b5-a575-e5324265321f | -4.5402 | -42.93 | 2024-11-23 10:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 934e08e3-30ec-3292-a26a-08848391b9ab | -2.8675 | -45.2832 | 2024-11-23 10:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| caa54532-d549-3660-a6ab-2d5aeab0b018 | -2.9974 | -45.3235 | 2024-11-23 10:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 2fda0dcd-3955-373a-967b-eb6cf3bcfb9e | -4.5403 | -42.9066 | 2024-11-23 10:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 41a04e3b-9428-31ad-ae75-acad444e6842 | -4.5216 | -42.9078 | 2024-11-23 10:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| fff89798-a749-3b52-ad20-895db023dd82 | -4.5403 | -42.9066 | 2024-11-23 10:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 292.3 |
| 61fe48ff-e1b8-39f5-a317-5679e905a382 | -2.8675 | -45.2832 | 2024-11-23 10:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 185.3 |
| 6fda74d8-7b14-3f4f-96eb-56da635dbe79 | -4.5405 | -42.8831 | 2024-11-23 10:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 497d1810-2fa3-34bc-875f-222faaf867f3 | -4.5402 | -42.93 | 2024-11-23 10:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 7ad23e1d-6e27-3341-abf1-7cf5445409ef | -4.5216 | -42.9078 | 2024-11-23 10:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 223.9 |
| cc785890-2172-3670-8b23-eb89a379eb9d | -4.5403 | -42.9066 | 2024-11-23 11:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 302.5 |
| 528bb5ac-4a69-320f-b72a-8865b13a02c0 | -2.8674 | -45.3057 | 2024-11-23 11:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 747b89ae-b884-3e2c-9698-241d708b448c | -2.8676 | -45.2607 | 2024-11-23 11:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| e4425255-98a2-35d1-800c-1b24a4ecd72b | -4.5216 | -42.9078 | 2024-11-23 11:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 206.3 |
| b739a083-624f-3d83-9f21-9947de33082f | -4.52 | -42.92 | 2024-11-23 11:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e48e11d4-b547-3d38-b220-e363790dfb47 | -4.55 | -42.88 | 2024-11-23 11:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad8e8215-8f16-39e8-bbbf-9fd81cc84732 | -4.52 | -42.88 | 2024-11-23 11:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a9120ff-2b23-39cd-a923-31814a542416 | -2.87 | -45.28 | 2024-11-23 11:00:00 | MSG-03 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a836d9e-3f97-300e-8dfa-de4c78e5cf6b | -4.55 | -42.93 | 2024-11-23 11:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 838a7104-0b1c-3e0c-a407-4770e5c7c8ed | -4.5216 | -42.9078 | 2024-11-23 11:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 0374c150-7451-3384-8c87-d84f9c01d78c | -4.5216 | -42.9078 | 2024-11-23 11:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 268.9 |
| eda92207-7481-3fa1-b0c0-c7e7c6c6fc7b | -4.5215 | -42.9312 | 2024-11-23 11:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 4d672a30-c28a-3aea-8cd9-5e57c8076b01 | -4.5216 | -42.9078 | 2024-11-23 11:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 181b2673-f71b-3b09-ae80-83fbaba32c0c | -4.5216 | -42.9078 | 2024-11-23 11:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 258.3 |
| e95a6a12-cf1d-3960-853d-70c9bcedd98e | -4.2605 | -48.697 | 2024-11-23 11:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 5269ddc6-b932-393c-b5da-5bd154aa5fe5 | -4.5216 | -42.9078 | 2024-11-23 11:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 251.0 |
| 9c921c25-9767-3deb-8281-a7aab4f6e437 | -3.4048 | -42.1436 | 2024-11-23 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 99.8 |
| 89ba0c37-837f-3d0c-b299-f4c4a7be9705 | -3.4237 | -42.119 | 2024-11-23 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 96.6 |
| cc0a7d2d-63d3-344f-905c-ce5f7d22cf64 | -0.9462 | -52.4214 | 2024-11-23 11:50:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 34750e01-091e-31a3-92ad-19312e174f9c | -3.4235 | -42.1427 | 2024-11-23 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| 44f5b8b8-8428-396f-99ae-b23c8d5cb375 | -3.405 | -42.1199 | 2024-11-23 11:50:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| 1ff71640-b2f4-34c6-b9d3-2e0350251e9a | -3.7593 | -42.268 | 2024-11-23 12:00:00 | GOES-16 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 069339e2-f148-3b1d-a7b4-1fb69b42709a | -4.5215 | -42.9312 | 2024-11-23 12:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| f9af05da-1c09-3e62-a639-675baafaaab2 | -0.9462 | -52.4214 | 2024-11-23 12:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 82.5 |
| bccb65c2-d33c-3475-8947-05e99a6fb627 | -4.2605 | -48.697 | 2024-11-23 12:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 145.1 |
| a5bc66bd-9163-3e49-8c0e-b01bedf76f9c | -3.405 | -42.1199 | 2024-11-23 12:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| deefaf8d-a38f-3eab-9386-00200915fe09 | -4.5216 | -42.9078 | 2024-11-23 12:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 323.3 |
| 12eeb916-8d00-307f-a364-69716c496f53 | -4.55 | -42.88 | 2024-11-23 12:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 691f7b76-bdb8-3735-a61d-40297d69a234 | -4.52 | -42.88 | 2024-11-23 12:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e59775c1-17d1-3678-b27a-e0dd11a19cd9 | -4.52 | -42.92 | 2024-11-23 12:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 69130f43-9f95-3167-bbe1-2ac08e33a2d1 | -4.55 | -42.93 | 2024-11-23 12:00:00 | MSG-03 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d558522-c8b2-30f2-8abf-b068646dd2d8 | 1.2428 | -50.7264 | 2024-11-23 12:10:00 | GOES-16 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 56cda078-3e8a-3ea0-a0e6-41825bc286cd | -4.2606 | -48.6755 | 2024-11-23 12:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 389a4e8d-6898-3414-8425-1efc1ac623b4 | -0.9462 | -52.4214 | 2024-11-23 12:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 658eae49-2106-3a54-80e6-ceae45fb42af | -5.0649 | -40.5974 | 2024-11-23 12:10:00 | GOES-16 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 6d6cf341-0479-3780-8852-0402993cbed6 | -4.2605 | -48.697 | 2024-11-23 12:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| 9f1468c8-20d8-363c-8802-25b31b90ba98 | -4.5216 | -42.9078 | 2024-11-23 12:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 75b211a8-bc8d-38a5-b57f-db3018569a22 | -3.5159 | -53.8132 | 2024-11-23 12:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 1b3cdaf6-55d9-3326-b102-5a75d839e8df | -1.7359 | -52.7181 | 2024-11-23 12:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 068e3038-31af-3213-93c4-140db2d812ff | -3.5921 | -42.0869 | 2024-11-23 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 257.6 |
| 073094ff-9c40-3428-a050-39e3e4dd56df | -4.2605 | -48.697 | 2024-11-23 12:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 350.6 |
| 071921d9-85e0-3c1a-9862-c080db5b381a | -4.5216 | -42.9078 | 2024-11-23 12:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| e206bcc0-dbe4-30d4-bd05-c52a322086c7 | -4.2606 | -48.6755 | 2024-11-23 12:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 191.8 |
| 99ee93db-1a2d-3e1f-a92f-fdc8a0c110e0 | -3.5734 | -42.0879 | 2024-11-23 12:20:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 160.1 |
| 27c120a4-cc0c-3479-9567-072d06b88ed5 | -5.10897 | -43.16309 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 6d6bd4da-85f5-3e73-adc4-63c43828cfb9 | -3.6771 | -44.89935 | 2024-11-23 12:29:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 13a3ae08-99c0-319f-9fe1-157b17ee00aa | -3.52491 | -42.04457 | 2024-11-23 12:29:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 43.9 |
| 60298456-487a-37af-b6c4-e43e1648c12d | -2.90343 | -44.95288 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1ea7ddf9-2ee1-3371-b1eb-a04d9ec326c4 | -3.524 | -42.50713 | 2024-11-23 12:29:00 | TERRA_M-T | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| b9a2b1b0-1196-3eae-a7ad-5d36bfea09b0 | -2.78553 | -43.34878 | 2024-11-23 12:29:00 | TERRA_M-T | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 44ef6223-2186-3d40-92db-1e773029dd37 | -2.95996 | -44.94228 | 2024-11-23 12:29:00 | TERRA_M-T | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 875acca8-d75b-31f5-8acf-1e43ca2d67db | -3.37562 | -41.55194 | 2024-11-23 12:29:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ab4ab4d6-96e9-32cf-bf84-7051fffe1ecd | -4.52854 | -42.89929 | 2024-11-23 12:29:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 521.7 |
| bb0043c8-7a0e-380f-a5ea-c8b51d8d8d85 | -3.6505 | -42.39452 | 2024-11-23 12:29:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 3ecaae87-3677-3f00-bfd9-2b769d0f7221 | -4.62136 | -46.50223 | 2024-11-23 12:29:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |


[Clique aqui para ver as próximas entradas](README69.md)
