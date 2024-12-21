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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b0c79ca-b9ee-340d-8e9f-06d3e6042a30 | -2.84617 | -54.54726 | 2024-12-21 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6d0f7ac-7b33-3b86-8f86-6908332347ce | -4.02284 | -46.54457 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5f448a5-b29d-3663-9f36-be2d51992620 | -2.65214 | -46.10288 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 647b6c17-ad4f-3bae-96be-6df6776f72b3 | -2.70426 | -45.56862 | 2024-12-21 04:46:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 667b2aa4-c547-346b-b5de-1be3597c14a7 | -4.0335 | -47.03943 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f2061c6d-00d1-3a55-96ea-cf0df6f63f3f | -1.70853 | -52.5828 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d58ff85d-8b7f-3475-bc96-75374ba3efcb | -2.44641 | -48.57117 | 2024-12-21 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbfb6a08-06b9-325e-bd5a-cd8515d5cc51 | -3.08616 | -46.56588 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6285d55-663c-3d85-af40-73fc7816ed92 | -2.8081 | -46.73128 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc750b34-4326-397b-9a19-2e20fce6b99c | -2.7705 | -47.39594 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c5a625d1-9dea-3961-b353-674653c8ed4d | -1.51144 | -47.27005 | 2024-12-21 04:46:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da7eab18-b45b-3306-9735-4303d655ad06 | -2.70461 | -46.14497 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4196bb3-43f4-3f57-9294-f13bf0aa144b | -3.83511 | -41.56842 | 2024-12-21 04:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b356b6b3-9f41-39ff-a923-e448b3e86585 | -5.98603 | -46.15844 | 2024-12-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7d95bfe1-ce77-3364-8909-7485b2a5a3be | -3.47676 | -51.44802 | 2024-12-21 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f943e721-0b69-3572-810d-b49683591366 | -4.01617 | -46.90092 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c883e38-f78c-3703-88ff-73656b4476c8 | -1.96339 | -46.64785 | 2024-12-21 04:46:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efba724c-818e-3e7a-b777-3028f6d4d1f1 | -5.23257 | -37.73201 | 2024-12-21 04:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60664038-9cc7-39a7-80a8-ec93b1913226 | -2.70918 | -46.14084 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78a4b8f4-3d96-3fec-b674-f3eb4ea43342 | -0.96318 | -50.64187 | 2024-12-21 04:46:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c93cba11-6060-31e3-ab5b-7d8f0775810c | -3.06891 | -47.47975 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71d6c3a2-b4bd-3690-b106-be006c539e07 | -6.01636 | -45.88977 | 2024-12-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3853ae39-04bb-3dbf-a38a-45c7b558ad58 | -2.63308 | -48.04967 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7842347b-47e7-378f-8d8a-6c5e8b4caa6a | -1.2594 | -53.52182 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53b801a6-3795-322e-92a0-1538323b1cc6 | -1.9422 | -48.13624 | 2024-12-21 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1288ffd-43af-369f-a449-8e28b19bbcde | -3.91806 | -46.67255 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 368eb3d0-238a-3031-8b8f-431b8beec376 | -3.76405 | -47.18814 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 975431a1-bce4-39ab-93a1-70a58bc1ff47 | -4.02652 | -46.79898 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6aaf4c35-9e49-38b2-aace-f46bd27c352f | -4.10847 | -46.72043 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a86ed68-67ec-3d13-8329-dfdb04b3c100 | -1.56594 | -46.77193 | 2024-12-21 04:46:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 236449d8-c436-3a3c-9d82-f2e54557a433 | -3.80772 | -46.70986 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77359a92-aabc-36a9-bea1-11a4cf81a97a | -1.88916 | -52.07581 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a85df251-27e3-3e9e-b45c-2753b5947c0c | -3.93858 | -47.0001 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ee799dd-8f37-3ec7-8572-62ed79fd0405 | -1.25844 | -53.69402 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35da748d-845c-359f-a0fa-f7011acca337 | -3.9248 | -46.88923 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 351e1c33-f04f-336b-a6ec-bfadf1523911 | -2.06052 | -45.47963 | 2024-12-21 04:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff29fc0c-f71b-36d2-9925-3624b75c4d98 | -2.06152 | -52.053 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d65fff64-f3f0-3cfd-b01a-dc52474bf7f8 | -4.06561 | -46.7231 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dee738bd-b38f-3dfb-a36c-4627d79db0d5 | -3.75672 | -47.18708 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 218142b4-8366-3626-83b2-de9f4a5f36c3 | -2.4418 | -47.48557 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0290bb9-4302-35f1-a136-cea5d609f3bd | -2.00024 | -44.53714 | 2024-12-21 04:46:00 | NOAA-21 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f4db931-2ffe-3bb4-bbd2-16fdfec9a385 | -1.50515 | -52.63908 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57bf0141-fa72-372f-bf4c-cde277d90c98 | -1.25523 | -53.47751 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d26249fd-5908-3beb-a30a-94466a3e2901 | -1.29045 | -53.12899 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59be37f3-1d60-39de-920f-c73ca0295fee | -5.60539 | -42.82186 | 2024-12-21 04:46:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b10bf31-e442-38e3-a1b8-23b61c42b93a | -3.90825 | -47.00016 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ccb7d8d-412b-3d89-ba8b-e40051026af1 | -3.83605 | -46.67891 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4dbfffb5-ea4a-3999-9655-4d91b51acbd0 | -3.11943 | -44.15762 | 2024-12-21 04:46:00 | NOAA-21 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dadd562-eb55-3af0-9f1b-cf0ae7aed19a | -3.94679 | -42.86347 | 2024-12-21 04:46:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 178d1ea8-e405-3ab7-afe1-8ba46e2e38bc | -4.11156 | -46.72551 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba84d728-4fac-384a-868d-022d7684ce8e | -2.61896 | -47.4668 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e65d5cd5-5694-362f-9dd1-f82a55af6091 | -3.30974 | -42.26651 | 2024-12-21 04:46:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcfd613c-e2f0-349c-83d3-549e4ae10fa7 | -1.87989 | -45.55401 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48c4d669-5234-3be6-bcda-a59af1ae1e15 | -3.88456 | -47.0321 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70301a02-8f3f-3f58-b9e5-3d1f8ac21d2c | -3.46563 | -44.98347 | 2024-12-21 04:46:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a573f3e0-cd90-3a82-afbe-143ffdaa8e0e | -4.10399 | -46.72454 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d363100-6cb5-33d1-9b22-1739ef209672 | -5.69065 | -46.53255 | 2024-12-21 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48c85282-5e75-3d7c-845e-b62ec0201ab8 | -3.74667 | -51.52637 | 2024-12-21 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11d6df7a-52b3-353f-a39c-02bf5faaa743 | -9.22352 | -60.33621 | 2024-12-21 04:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 99d342b4-a6b0-3309-a4be-ae65b6602388 | -9.22423 | -60.33803 | 2024-12-21 04:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6f3925eb-864f-3866-83be-493545b6d0b8 | -10.50549 | -49.1245 | 2024-12-21 04:48:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 393f7177-890d-3004-b0eb-4f3e243092f8 | -12.78828 | -61.50494 | 2024-12-21 04:48:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0f45cf-7e09-3466-839e-0ecd9f574f9e | -12.79396 | -61.50292 | 2024-12-21 04:48:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 576fe249-47e7-3f48-bef1-734c63f15340 | -11.85887 | -46.95208 | 2024-12-21 04:48:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 737aaa28-054f-333b-ab2a-f1b3496bf610 | -11.863 | -46.95271 | 2024-12-21 04:48:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24c6dacc-a78a-3d27-b2af-74b8c540fecb | -9.21867 | -60.34006 | 2024-12-21 04:48:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1fb4704a-4730-39f7-89d1-f36f4a1f3f56 | -12.45995 | -43.56007 | 2024-12-21 04:48:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fad155d5-63be-31ed-b3f6-54f2b25f0c36 | -18.51929 | -53.40026 | 2024-12-21 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f86709d-b9a7-32a7-84b9-94956eed1e4c | -14.84504 | -56.75217 | 2024-12-21 04:50:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf87c2f4-9ec6-37bb-94c5-63ec889ee12f | -15.16779 | -56.47003 | 2024-12-21 04:50:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 755519fc-7e12-37e2-b1d7-d3161ec5634b | -18.1242 | -51.93882 | 2024-12-21 04:50:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b35b671-f3e6-3f23-a26e-c0f5ee6fe3fa | -16.33503 | -56.832 | 2024-12-21 04:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d5f2a731-b54c-3105-8547-3e8c79bef305 | -19.08299 | -57.71132 | 2024-12-21 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 706e843f-e5c3-3496-a18d-59b789a1471c | -18.60389 | -51.78849 | 2024-12-21 04:50:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25ce94c2-10bf-330f-b9fd-b131eff4b009 | -19.76179 | -53.42436 | 2024-12-21 04:50:00 | NOAA-21 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce13dc77-7404-35f5-9694-d6cddf648a79 | -18.51984 | -53.39661 | 2024-12-21 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07962d4d-1fb2-39e0-9690-df27663d210c | -19.06393 | -52.85354 | 2024-12-21 04:50:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16d7dae3-2e0f-36b0-82b7-9ad91f3c07c5 | -17.29993 | -53.76856 | 2024-12-21 04:50:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc9ce07e-562f-35d2-a61f-3933059b90db | -15.78317 | -54.51206 | 2024-12-21 04:50:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28441b68-79f7-3d44-a05e-8811f32b0a3f | -19.06729 | -52.85409 | 2024-12-21 04:50:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e6f1290-5d6f-304b-9b30-88a7d325f938 | -20.47626 | -55.84231 | 2024-12-21 04:50:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a266191b-27d2-3066-bf07-e205567d54fe | -18.50933 | -53.39863 | 2024-12-21 04:50:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0842b32e-5f26-370b-a589-b689948f5186 | -19.08662 | -57.71204 | 2024-12-21 04:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ddd96d01-b90d-3d3c-8741-cb66f83ac00e | -17.29331 | -53.76744 | 2024-12-21 04:50:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba691593-3a92-396a-88db-8fcf2fcc68f1 | -18.60735 | -51.78904 | 2024-12-21 04:50:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c0626e4-3f44-39d4-8fd4-55621bcec4e5 | -20.29572 | -54.78936 | 2024-12-21 04:50:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 911ad40c-37a7-3f8b-ba25-5e31d9fb10a0 | -17.29662 | -53.76801 | 2024-12-21 04:50:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e3d9c47-6150-3779-9baf-46e9a1b39b26 | -20.29514 | -54.79303 | 2024-12-21 04:50:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e996cd9-b16b-38ca-9b54-316b84580f08 | -29.77815 | -51.17773 | 2024-12-21 04:53:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| b3336ad6-62b4-32d0-8a21-20352d90e38a | -29.77853 | -51.17611 | 2024-12-21 04:53:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 0bd65039-5499-3f24-ba80-bae92bca2b0f | -1.87883 | -45.55898 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1370ce5-e0a1-3920-bc63-209bcd881d17 | 4.45301 | -61.02555 | 2024-12-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df25d71f-0bae-32b4-b244-39fbe5bb1647 | 4.45791 | -61.02875 | 2024-12-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5a97f6aa-e699-39b0-ba04-ac15ae89e28d | -1.88104 | -45.55654 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 003e6324-e018-36e8-b949-d14b8bceaa4a | 0.74452 | -51.98275 | 2024-12-21 05:08:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 33d3ea7f-d325-358e-b8f8-3baf452cd55b | -1.87951 | -45.5546 | 2024-12-21 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2273e580-7a98-3539-a0c9-bf71853db72d | -0.35646 | -50.07954 | 2024-12-21 05:08:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 100b0cbf-0a55-3d0b-b116-6d40a750c5fc | -0.96297 | -50.64347 | 2024-12-21 05:08:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dca02dc-b6ea-31b2-b23f-07f49f9a88a0 | -1.30168 | -47.75348 | 2024-12-21 05:08:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a0b2481-91c5-39fc-a887-0e60464f6923 | 4.45359 | -61.02945 | 2024-12-21 05:08:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README9.md)
