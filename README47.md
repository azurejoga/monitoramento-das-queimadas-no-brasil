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
| fdd16c56-9099-3607-b526-bd71fe31a5f3 | -3.2501 | -50.33969 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7569ddf-6483-3f82-b107-f5c12566bdca | -3.24956 | -50.04138 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9876a9a8-ad9e-3705-9b2c-5ba1b3f60173 | -3.24868 | -50.04665 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6871aa2f-5eb0-3bb6-998d-72a4c05f3a55 | -3.2461 | -50.33336 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4d4605f-abf1-38a7-8e47-330b9bca9e5e | -3.2452 | -50.33887 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35abad9f-2238-3ec2-a952-5d1b62598476 | -3.21052 | -50.30484 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57af2b80-b47f-30cf-af29-19eba31b2f68 | -3.07392 | -50.2363 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6149173f-83ad-390e-83dd-cbc900473ae6 | -3.07173 | -50.23365 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f38ebc0-c2fa-3f41-b24d-214fbf2f76d9 | -3.07037 | -49.57433 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 147a44e6-bd78-3025-ab50-f8215e688378 | -3.06957 | -49.57926 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb4761d6-5b67-39cf-896c-2143d2197870 | -3.06594 | -50.2384 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ea35c80-a04b-3900-a1fb-9ee780b468d3 | -3.06569 | -49.5736 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 448fb83a-1385-39e4-be62-7e44687c6835 | -2.98739 | -49.52545 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14afeb41-9c39-31de-b447-0542ed67438e | -2.98497 | -49.52239 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 167253ea-0cd6-35e4-a45e-dbcf5d5a9fd3 | -2.9842 | -49.52724 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6082622-2ea9-33bd-922a-3605f7828999 | -2.98272 | -49.52472 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f882dae5-5242-3a63-8c7f-a6556114b4b3 | -2.93254 | -49.43389 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9706c6a4-2133-3bf7-b7fa-918ff724db76 | -2.92949 | -49.42354 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6db0d8c7-6b28-3f12-88e9-1f3383b27f1d | -2.9287 | -49.42836 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f51d06aa-f762-3d80-a4bc-5d4fbb36b68a | -2.90801 | -49.03857 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7449672b-49c0-362c-8532-20bd5232a1e9 | -2.90111 | -49.50846 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7358c1b3-d643-3f52-b8c6-83033ad7cc86 | -2.89261 | -49.50203 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 510b7078-4b09-3cb7-9bc2-7231bf7dc528 | -2.89258 | -49.42538 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e25bf4fc-6896-3595-8fbc-5b46a45b19c8 | -2.89164 | -49.42224 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f261c3d3-19d8-319a-aaff-a1ceb5dd95a0 | -2.89081 | -49.42718 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ac24b140-61b9-3470-a437-3e4e84ba3e4b | -2.887 | -49.42154 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dbf09f24-5702-3ee9-a385-ad46dfb82cb2 | -2.87953 | -49.27125 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c65ec645-a7aa-3085-9f05-7f3a32190387 | -2.87495 | -49.27047 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 696aded9-3598-3e6a-9c1d-063773b6ec43 | -2.86021 | -49.39027 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e0ac48fe-881e-34fa-a827-efd1171995fc | -2.8516 | -49.44327 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7307f346-06be-3a4d-95e5-6cde35191eb6 | -2.82112 | -49.22506 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de3c7fc4-8364-354f-b5ce-81a179f1a3de | -2.82081 | -49.22779 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ab5137b-e5c7-37b1-b881-d73798391270 | -2.81883 | -49.76503 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d4b0db1-0684-370d-a69f-c9e7186a3979 | -2.81803 | -49.76999 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9ab3e9e-6526-389b-9cea-ed52b4eab302 | -2.81346 | -49.32848 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0080562b-3ff5-3f9b-98fe-f75dec6d201a | -2.81328 | -49.76919 | 2024-11-02 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e3eebfc-e312-3c50-8f12-10a9312ded37 | -2.80457 | -49.32913 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7015c444-2561-349f-9d0b-9ce5c49eef64 | -2.8038 | -49.33394 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a099a00-60dc-399b-b8dd-ef09b7ca1d9c | -2.80345 | -49.33172 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00e016a0-40d8-3140-9bd5-5ee004cc3cd7 | -2.79919 | -49.33316 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ffee740-7d88-3c28-91a9-bd8da5eb188f | -2.79884 | -49.33097 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0d62824-01bf-3ba8-bed8-b22feef50bff | -3.50638 | -49.94443 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32741471-c583-3c55-813a-e10a58750118 | -3.45949 | -50.16724 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b56b6ae2-4192-3891-8556-20479df84235 | -3.45071 | -50.16037 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5f93cca-db5c-3318-94b7-b907fd5ef2c3 | -3.44718 | -50.18148 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| edeed771-54a8-352a-9a86-acef54519def | -3.44674 | -50.15443 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ffb81a1-898b-3cab-88d8-5ce78e1f49e7 | -3.44234 | -50.18066 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dcf506b4-096b-3f0c-aab3-a1941752a005 | -3.37493 | -50.2676 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77a00c43-9e81-3d37-9375-8b84fcd1ab37 | -3.371 | -50.26102 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e4c87185-b887-3966-b8c8-46e0b302ec7b | -3.37008 | -50.26667 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fb58e787-50be-3c85-933f-18ce173982ab | -3.352 | -49.23135 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad1d3dc8-2408-3514-8574-679d5e8d5d5e | -3.35078 | -49.2336 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf009d39-842e-3b6b-885a-94e0990eeb07 | -3.34174 | -50.25636 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bd171628-cf42-39c3-bc7b-9c25eb92c7b6 | -3.29711 | -50.02243 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad2c754c-4fbf-3208-9bb5-c2a14069e604 | -3.29232 | -50.02162 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ba43dcff-179b-3797-b3b1-20796cdb5583 | -3.29228 | -50.23492 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59769b97-aba4-340d-95a0-525a7c3873ce | -3.28739 | -50.23423 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff765ac9-28af-33f5-bf06-79f0df446a69 | -3.28251 | -50.23346 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a4b271ee-b584-3d50-b1ec-0ada9cca051a | -3.28167 | -50.23868 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5f649a1b-f984-3d4c-af7f-cf87cc0abf18 | -3.24779 | -50.052 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9216eb11-44a5-371c-a601-00b8d91a6f25 | -3.24388 | -50.04583 | 2024-11-02 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66660b40-071d-33ab-948e-5b44aa66825d | -2.63036 | -49.35758 | 2024-11-02 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a112698b-b9e0-342c-b86a-9b62bd981de9 | -2.62573 | -49.35683 | 2024-11-02 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f27883-bf34-33c2-b0a4-684804fb28d0 | -2.60648 | -49.15895 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e64a7952-f432-36ae-894f-679aa9d5d4d2 | -2.60646 | -49.15725 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 746580d9-adab-303e-9c43-9027973a279b | -2.60571 | -49.16192 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f31f555-a6fd-35dd-b986-839763056681 | -2.60388 | -49.82032 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8055391d-186b-39f7-8d0a-407b8d43a95e | -2.6034 | -49.82188 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6cab9c9-5c0b-35bf-b9f4-8fc5ab4a0e8b | -2.60303 | -49.8256 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c5eaf17-3f9a-3bb9-8296-1ac3fdbbbafe | -2.60051 | -49.19458 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8218af5e-261a-3b78-aa7d-c56bd053ca31 | -2.59976 | -49.1993 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4983a016-449e-3863-973a-228ecb2412e6 | -2.5991 | -49.81948 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 299401ee-a503-32d2-83c1-f4de7e3480c4 | -2.59825 | -49.82478 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d794b67b-f5e1-31a3-ae87-14ff7dcaa0ab | -2.59607 | -49.25214 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df89bc4e-00ff-3482-9cf3-abfc5ef7facd | -2.59431 | -49.81868 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65dd3e5b-fd19-3f44-a718-62bb039d58d2 | -2.59347 | -49.82391 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 20545d00-7b7c-3e1a-ac26-4fde856b22cd | -2.5853 | -49.23086 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f6cf5de-339a-32a9-9879-0ccc1e368f1d | -2.58456 | -49.94101 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 749f53fe-0b01-3637-931a-0202fb11c48d | -2.57825 | -49.1285 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8210cbcd-8466-3f66-85fe-312f1c4453d7 | -2.57542 | -50.06046 | 2024-11-02 04:12:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65550986-4e1e-31eb-b1eb-e85aebe72000 | -2.57445 | -49.12308 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75bd2a1c-36d0-3fb7-b545-9479dd000e61 | -2.57402 | -50.05602 | 2024-11-02 04:12:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dad54451-a23d-31ba-9dbe-ab8b7268a0c6 | -2.57312 | -50.06141 | 2024-11-02 04:12:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16bf1b7c-0cdb-3d0e-a88f-3d214f84e78b | -2.56386 | -49.2468 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22e0228d-325b-3df6-b10d-370f18865d66 | -2.5585 | -49.22157 | 2024-11-02 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77f12f74-617e-3d42-ad47-64130cf775df | -2.55137 | -49.63306 | 2024-11-02 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d01c6f5-1da6-3a1d-b488-97c3226a6876 | -2.55028 | -49.63169 | 2024-11-02 04:12:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64b7c81a-286b-3c10-a568-afb897b33abd | -2.50982 | -49.736 | 2024-11-02 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 100536bf-1da1-3cec-8202-5a22affcf4e2 | -2.50953 | -49.73484 | 2024-11-02 04:12:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edd73413-d603-3132-8dd1-5174a32799c1 | -2.46897 | -49.8345 | 2024-11-02 04:12:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c373302-6bea-362a-b641-f85766598c09 | -2.39656 | -50.31371 | 2024-11-02 04:12:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76d4a59a-9757-308c-8969-aa4ed29c6ff3 | -2.39565 | -50.31936 | 2024-11-02 04:12:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33353a38-342c-36b4-b158-14e81e754b86 | -3.91653 | -50.43871 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdc86172-0e8c-3c99-af1e-6e8c41d82a20 | -3.91379 | -50.44042 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ba8d8ed-30ee-3867-a0b7-493617ffa0a5 | -3.86839 | -50.48663 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba5ad6f4-358b-3351-9436-8523436af3b4 | -3.86349 | -50.48576 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af761e54-47b0-33fa-9cb1-57a428e847ba | -3.76122 | -50.00566 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905056a4-3ca7-3440-8957-8860dec72dd6 | -3.70944 | -50.54993 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77afd883-42d9-34b8-920d-fca5a866ec95 | -3.70451 | -50.549 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b5dd2bf-7183-39e8-8fd7-5c9d50b4307d | -3.70215 | -50.15604 | 2024-11-02 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README48.md)
