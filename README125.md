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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f77318c6-1eac-3d6e-9c3d-81a6b1b5762f | 1.87924 | -55.73153 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b600683b-ca4d-3e80-b19a-014371ba530e | -3.41378 | -50.17083 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83695556-b3fc-38c5-b9e3-d5ef2aef38ce | -2.7541 | -51.66309 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fbdd5ad-c6b8-3543-b127-9ac9df0e0e19 | -3.51126 | -53.78312 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f04b239d-0812-380c-ae96-be007289054e | -3.04933 | -48.96633 | 2024-11-30 05:27:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e999f0d0-dbca-3223-ba88-49707b7757ea | -3.09233 | -50.35511 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e2530ea-838f-397b-9f95-9d168a632197 | 1.18257 | -55.97459 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbec85bb-b2c3-3ebd-bb9e-0c6b7c95f638 | -1.44147 | -55.13247 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 38b31ee3-0aac-3642-a63a-cbe27c28898a | -1.25224 | -54.55177 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e96787c9-62a7-375f-b62d-3ac637106339 | -3.54304 | -50.18502 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89ad8e3e-d547-3830-9654-eaad94447327 | -3.96155 | -48.0922 | 2024-11-30 05:27:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28cf5fcc-a784-3785-8486-b6d4467d1448 | -3.29711 | -53.83892 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97012548-8e9e-3586-a43a-ff2e35c85f0a | -3.12239 | -53.27601 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44977674-40fa-3d9c-9057-8fe50af8d41d | -2.84828 | -54.0327 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb7be6a0-e354-3a6c-ae02-191475a29ddd | -1.87231 | -53.95706 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35edba01-eebc-3e78-8a87-3ab706146b5c | -3.12834 | -51.12147 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f75a75b-2f06-3d6f-91cf-e4387461b2e2 | -2.8415 | -54.02905 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efabd79f-adf0-3885-a70a-b97359d04c93 | -1.34306 | -54.98426 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 891707b5-2d27-3ab4-802c-73bb4ab4d7f6 | -3.24344 | -50.59256 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34270f14-e45d-3138-b5d8-e3f69e7a7f73 | -3.77637 | -53.42041 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3cd39dfc-cfba-3ebf-a24e-511765729dc0 | -3.0938 | -54.02334 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1668858-04ba-3747-b6e3-651dc0c56ef3 | -1.26172 | -54.54871 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b89c81b5-42a2-3a14-afd8-30a737f62075 | -1.41914 | -55.27641 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa91312f-b466-3e89-b4d0-698dfa1ecab3 | 1.10337 | -59.59016 | 2024-11-30 05:27:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| def5d1d4-1fec-30b4-9316-78b835e288a1 | -3.60064 | -54.4268 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75a44897-f2f5-39b2-b176-a95cb49c4110 | -3.34154 | -50.52717 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3219b8e9-9c1c-3f97-a9e7-b01aa0b8a841 | -3.09488 | -54.55164 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3eaeed68-7736-38c0-b41a-37635b4f1cfc | -1.29702 | -55.74087 | 2024-11-30 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e8dd77a-6a5e-35be-8607-e1dce7c5075a | -1.07812 | -53.63871 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94901ae9-cc26-3dfa-abdd-02c06162efce | -2.62876 | -51.74625 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34e0ba57-4cc9-31a2-8bcb-af5540a5f1b2 | -3.59143 | -50.36426 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44b7032b-dd9b-3c96-9bcb-2d99e9c612b4 | -3.46694 | -53.88188 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 923da985-f141-3ae4-a21e-5c7ee407c387 | -2.61205 | -54.20551 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0be223c1-e0d6-3800-81b7-0707072a36ad | -3.09822 | -53.73079 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e7f9d2a-71c4-3d2c-b0c4-62eff5a5e86a | -3.16372 | -53.24384 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9fcf5067-2838-3748-87a2-2cc0574193cb | -1.95312 | -53.34419 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3a9345ae-8461-3d13-88fc-feb168d645e0 | -3.06548 | -50.32795 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 283d4ef4-e9d6-3f8e-ae7b-c00f35049fbc | -2.89672 | -54.77232 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd05b724-a7ad-3713-9597-2718bdd56504 | -2.04502 | -54.69352 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 957c6017-c6ad-3ce3-b1c7-04be600f4746 | -1.76861 | -55.67836 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee961792-b109-31d1-86ee-7c1cb6c065e5 | 0.55255 | -60.36431 | 2024-11-30 05:27:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb6f3d1b-b99a-3bdf-9241-c1b5890f7427 | -3.77143 | -51.67913 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 44e982db-df75-3039-97f9-14a50b122987 | -3.39268 | -50.31858 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fc6ebdf-08d5-3cd3-befb-d56e3ed4f9b9 | -1.75323 | -50.54866 | 2024-11-30 05:27:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f1b7732-2e23-3c5f-bdc5-f46bbb208563 | -1.17541 | -53.91064 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f679763-7cc7-3f20-a0bb-2564c602902a | -1.47245 | -55.12896 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f275707-5569-38fe-b109-04bfcae3cc31 | -1.58506 | -52.28204 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cee9fd26-4207-366f-b5f6-3ace82883d6c | -2.86158 | -54.03982 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 182de919-707d-315e-bc3a-2c8e2136d06e | -2.84542 | -54.03468 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| daaae3fa-a72e-31b2-a34a-33bae4ad5fd9 | -2.89193 | -55.22528 | 2024-11-30 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fecc46d-a734-3946-b76a-d997595649d8 | -2.65604 | -51.71421 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d3d40d1-5546-3d73-9d5e-5a43bd296384 | -0.96284 | -51.7197 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0340080-d545-3825-9a2c-ee01a8d800a5 | -0.87716 | -51.72167 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de1cd15d-b521-3796-bf9d-d4f18acd0f24 | -1.06687 | -53.63355 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e39fa773-d86a-3518-b64c-1d7632c4fc60 | -3.38953 | -53.27333 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07772ceb-060d-39c6-bab0-926c888efa72 | -3.39173 | -50.31514 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c6d684f1-4e0f-3d7a-9b6b-125e047b6635 | -1.63754 | -53.86525 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3fc2a4c0-7d62-3b19-a44b-25523cd32eac | -3.15113 | -53.83455 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e6c411d2-2181-3f5b-82ec-3dc3918c8370 | -3.75364 | -49.9479 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 016ba3a8-d228-3055-9e60-27663911231b | -1.71992 | -52.63047 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bbe6dc9b-3d42-3832-abe0-8039cf0f1b9b | -3.12776 | -51.12538 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81306b14-cef9-3e33-80e2-ddb61c5b8a9a | -3.7912 | -58.97977 | 2024-11-30 05:27:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd7cd7c4-e9d9-33d4-8f30-088f3cb374dd | 0.94475 | -50.73301 | 2024-11-30 05:27:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf01b892-c0bf-303e-943d-044fb0795c6a | -1.36273 | -55.19279 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 705fff61-1f36-3698-9747-8cf638c6ff0e | -2.65057 | -51.71341 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ee22a8d-df23-398f-96d5-ec84bfbd8425 | -3.27632 | -50.59774 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ab56e6b-acf4-3b9c-a2c2-0fe5cddcf782 | -1.34528 | -52.13295 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3aa9bbb-d274-33f7-aaeb-675e658ab0a0 | 1.19028 | -55.99816 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51639d90-ce07-3944-8387-67336cebe6b9 | -2.23245 | -53.62773 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63b246e3-9f11-398c-90c7-ee3edc720b1c | -4.19197 | -50.6896 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2417a31-da5f-3f80-92ab-e320e7dd0311 | -3.3608 | -49.10174 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9232469-5801-3150-bf06-0a0b8528ae3c | -3.25295 | -54.21974 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb1e0ace-e666-368b-87c4-ac210cf4e0c9 | -1.59531 | -60.57719 | 2024-11-30 05:27:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adcee051-6e90-3b31-ab21-e0efffc37166 | -1.58927 | -52.28904 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af9a636d-ad51-3c13-a79b-a2f21288ff1b | -2.96219 | -53.72445 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21ceda93-e1fc-34ed-8310-728b60e98af0 | -3.53724 | -50.18158 | 2024-11-30 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be684f67-25a8-3b32-92ce-fe3870e588cd | -1.53373 | -56.06442 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c0cd66b-2ce1-3d25-9257-b301403cb314 | -3.24448 | -53.92897 | 2024-11-30 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4ff8ec70-90d7-36ec-b811-b2f06255ce20 | -3.75206 | -49.94443 | 2024-11-30 05:27:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85832f86-72fa-38fc-a8a5-c556992e69bd | -1.53162 | -51.61714 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eef632f4-1789-360b-98ce-4b72adb9d06c | -0.25036 | -53.76276 | 2024-11-30 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9cb83c1-ebfa-3b7f-b2fd-ad2426cb3de5 | -2.11593 | -56.15698 | 2024-11-30 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce4a3c19-644b-3f61-bb9d-e6bed924028b | -1.04051 | -51.73616 | 2024-11-30 05:27:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c547eb47-c845-35d1-beb5-d12603d13428 | -2.04436 | -54.69783 | 2024-11-30 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4178a3f-6ea1-37ef-a114-5dffa61ba80d | -1.702 | -52.64587 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59fdd2ad-87b0-3798-8141-780939b0a688 | -3.63915 | -54.44995 | 2024-11-30 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 553d1f71-4de7-3e1f-bde8-71258019ec55 | -1.26161 | -54.5498 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 79b5f4a8-47f1-3288-8144-c4c1a5d46592 | -1.26547 | -54.55368 | 2024-11-30 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f79a2cb-9972-3a25-bd78-ed63a6c3d11b | -1.47493 | -56.10134 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c3424cb-cd42-3985-bb9e-ab3fbb43af4a | -3.04028 | -51.78614 | 2024-11-30 05:27:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 189fabe6-6658-3069-8f5b-899a4f533cff | -3.23147 | -54.73072 | 2024-11-30 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c9eb20a-0feb-3bbd-a899-9f4d1c971687 | -1.91251 | -52.91014 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5a96138-f41b-38f8-89a3-97581d517fa3 | -2.31624 | -49.07419 | 2024-11-30 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3222c8b-0367-3299-840c-8dc434a99c56 | -2.83405 | -54.10794 | 2024-11-30 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44e8b565-e316-35d3-8a56-d6af5c5de281 | -3.43827 | -59.29054 | 2024-11-30 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6cef05f4-81f6-36aa-bfb4-c0787da6f338 | 1.18794 | -56.00832 | 2024-11-30 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 968db2ff-d040-346b-814e-683a95b979b3 | -1.19321 | -51.75976 | 2024-11-30 05:27:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ebb6e74-af0a-37d3-bee0-26ab13fb35fc | -3.15813 | -53.24096 | 2024-11-30 05:27:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6b53b776-91f8-3710-979a-808b0512e849 | -2.65124 | -51.71326 | 2024-11-30 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6c90a39-bd8b-3d51-9645-73d0c7a03720 | -1.61751 | -52.35804 | 2024-11-30 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README126.md)
