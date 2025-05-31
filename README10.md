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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a29ead7-077a-3b61-911a-a4e62d8fbcbc | -10.65196 | -49.42767 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a7076c2-7863-3aa1-bbe8-787588678d3b | -15.88849 | -43.45719 | 2025-05-31 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 373dca46-70ac-3b39-ab3d-5c19a35f8103 | -11.83709 | -51.27423 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 98f687e2-70c4-368f-b3c8-de295de6ffc5 | -10.66793 | -46.39458 | 2025-05-31 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51c598c1-85b7-3ee9-bcad-899ff911649d | -9.53092 | -54.76549 | 2025-05-31 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea6cec73-9fc3-3869-bdee-dbd842f6e07d | -12.10676 | -54.66734 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ee00a27-ace0-3e4d-b8ae-2005cecd3a46 | -11.91404 | -54.42737 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cefb4165-ae56-3289-8ee4-74e221ca7bbe | -11.03918 | -54.00137 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87ca58c2-c8cb-3c13-9b9e-97fb34313bb3 | -14.03213 | -55.13702 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e5d33dd-628a-357a-a752-3b94740ded2f | -16.12353 | -46.82545 | 2025-05-31 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 682e1dc6-1fb7-301f-8a87-8baad73b6ab9 | -13.10391 | -52.29328 | 2025-05-31 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3940b965-098b-3f79-af0c-f349d5d6d7da | -14.49247 | -46.50917 | 2025-05-31 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cd3ecfa-6719-332b-b4c6-7b3b87072e0d | -12.18199 | -54.2509 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cbb58e2b-b16f-31aa-8c37-ac52c54b990a | -8.97189 | -50.20589 | 2025-05-31 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1deb0023-a312-3cbf-8c00-8ba97cfeaa42 | -9.12252 | -48.75697 | 2025-05-31 04:27:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4534bf0-5d78-336b-b51a-798992942fb2 | -12.27243 | -44.58822 | 2025-05-31 04:27:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ca985c7-d99d-3bed-aca5-482219ab329b | -9.52999 | -54.77063 | 2025-05-31 04:27:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64af2f63-3710-320a-9648-4abf3a0507dd | -9.31316 | -49.4934 | 2025-05-31 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e47765c-e860-324f-a257-73bd56049fa0 | -10.82814 | -56.94707 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3041ecd6-6d3b-379f-81e2-1baf712cea34 | -14.83684 | -48.09307 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 733ee947-a149-36c0-a3b4-f8a0f4c323f3 | -13.10451 | -45.27802 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13edceeb-8c24-3a26-8c6d-1833cd75ab8e | -10.68951 | -57.65152 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2adcdd87-7972-38d5-b2b6-d0f80c4621dc | -9.13184 | -49.65067 | 2025-05-31 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c4f4434-552a-3892-a2fa-e09dc9488cbb | -12.16208 | -46.29059 | 2025-05-31 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f7eb5a92-d6a6-3020-834b-7d2526af90a4 | -14.83299 | -48.09607 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b607784-c854-3978-8a37-c4c9a9f42a7b | -9.31443 | -49.48558 | 2025-05-31 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7bc28b2-dfae-3498-afcd-9d1b4874ff45 | -10.64124 | -49.43037 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3e632041-686f-3b02-b79f-989031f46e34 | -9.39424 | -48.41914 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9edb77e-0ca0-37e5-8cdc-06ceae54cd4e | -11.14476 | -53.94191 | 2025-05-31 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5b68d07-4f4a-3a69-aaab-7b155db5d831 | -12.03815 | -54.96519 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c507ec4-f674-3df1-a67c-4dccfef81d0d | -12.37502 | -54.16194 | 2025-05-31 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28dc5ea1-359d-39e1-bb25-31323c2c4a55 | -10.33091 | -57.49271 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c82538a-2113-35aa-a14f-5909f59d5fcd | -14.0203 | -55.12517 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeea6c3c-7a37-3bff-acac-f7ebc8e8efd4 | -14.61473 | -47.96915 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3a2bed7-c1c2-364b-b69b-f2faebdcdf7b | -9.40244 | -48.42407 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 296b5d99-99cc-33d6-9a09-bd23a20ca789 | -10.46111 | -47.93915 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7a3d21e4-bde8-3634-9e95-31d547ee1e23 | -12.01402 | -49.52691 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| acd8ccbd-a40e-39d4-8dd7-56bc811c7655 | -10.65415 | -49.43581 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 43862f0a-e5cd-3c1e-9d14-e73c260fd144 | -13.99538 | -52.71806 | 2025-05-31 04:27:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26abcce1-58c5-3315-abee-b6b6a7ae73bd | -11.84153 | -51.27044 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f7dd88b1-e2e3-3b3b-b182-853f4acf54d6 | -10.64812 | -49.43148 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 312080df-d09f-3fe2-a2aa-33b15313c4c1 | -13.04812 | -53.71942 | 2025-05-31 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44b0884d-5320-3ce9-a5ab-2d2aa4c35302 | -9.67792 | -48.60262 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7de53f6-df9f-302e-b499-84a88ad7c4e8 | -12.01463 | -49.52316 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| abd69ca4-c1db-336f-bd51-89659736c4df | -9.1143 | -48.63455 | 2025-05-31 04:27:00 | NOAA-21 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d42290-9a31-36ca-958e-0a52027aaae1 | -12.03288 | -49.51854 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 96255952-deb9-3302-914e-4480f93e4a79 | -12.02145 | -49.52431 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6dec71a0-f9b6-33fa-963e-63f9466a303f | -11.84078 | -51.27488 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5746cae8-1252-3c1e-877e-6e547f5a364f | -10.82271 | -56.94614 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8efb221-5f2a-346e-aa37-753e86484f91 | -13.62827 | -47.44237 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a54328ac-6f3f-3877-bcb8-313cb003e93c | -14.0707 | -47.65901 | 2025-05-31 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8049a006-9c83-3264-ab73-3b4f8cab090c | -11.83784 | -51.26978 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 8dc5cf85-aef2-3d9b-95f6-bd5a8981ebc1 | -12.15873 | -46.29006 | 2025-05-31 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46250bee-1d17-37fb-a8ae-5eb238b90d9b | -11.90775 | -54.8279 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b5628e8-c499-3473-a477-e9c22a71804f | -12.02084 | -49.52805 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 81d6f2ed-d3d6-3b04-a5bf-7808d18a00c5 | -11.92017 | -54.41912 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d324d0f-9a07-39ee-8fae-5a368c287d61 | -11.00001 | -50.7555 | 2025-05-31 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bcfebb03-60f9-368b-96d2-cde4ea5863e9 | -14.61803 | -47.9697 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 152a37a0-0392-34a7-9ff7-32fd952a3313 | -9.31379 | -49.48949 | 2025-05-31 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3857f6-2c4d-31dd-b9c7-7e1c8b60614b | -10.45314 | -47.94461 | 2025-05-31 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afbffa4a-2d6e-31fc-84de-943ac5b6d167 | -12.02546 | -49.52114 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3440db8e-f4db-30bb-92bd-69ff38637b3e | -14.61913 | -47.96262 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75ef1451-fcb1-353a-8acd-c637fb2c5f1c | -12.45371 | -54.91657 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6620609-3fe2-36cf-ab9b-1f17e3478166 | -14.01577 | -55.12432 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7b42236-782c-3af6-900a-22d2bd1544c1 | -9.56242 | -55.00525 | 2025-05-31 04:27:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ab0c474-2b79-37f3-899b-34b15c108ae5 | -8.81312 | -49.84483 | 2025-05-31 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42d34c4c-ccdb-3ffc-a855-9622e55126b3 | -13.09926 | -45.28945 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 823e2e15-127d-32d1-b192-956867a31d47 | -16.59018 | -45.87875 | 2025-05-31 04:27:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 00c1ef54-3da8-3a6f-91f4-8bbcafa265a0 | -14.02078 | -55.14217 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4726725f-f32f-3d98-a639-ada6c2642067 | -13.6481 | -47.4456 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b0cb2ae-372b-382e-b8d3-82f812a45040 | -13.99498 | -52.69738 | 2025-05-31 04:27:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7903d3fd-c341-3e27-98ce-a153c7349a1a | -13.10393 | -45.28201 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1fdc7a7-5f9d-3c80-89ca-9cd3dd558352 | -12.4629 | -54.91828 | 2025-05-31 04:27:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a163334d-291a-32ad-bb6d-1a5795b7aa51 | -11.68609 | -48.26224 | 2025-05-31 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c5e7e4a-0103-36dd-89b2-cd1900016c41 | -11.8297 | -51.27301 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d48e107e-ae44-3bd1-aa78-39e27599e416 | -13.30595 | -44.26826 | 2025-05-31 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 98e7aae7-7e7c-3aa4-b3e3-e48cc280c073 | -12.37572 | -47.31599 | 2025-05-31 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 359e3286-88fb-351c-beec-21b14c98e24f | -15.57056 | -47.85556 | 2025-05-31 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6062bcd3-76bd-371c-84e8-231ea2f900a9 | -11.83859 | -51.26535 | 2025-05-31 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b47d5fc3-848d-342d-8c82-29d407f672f1 | -11.90445 | -54.79019 | 2025-05-31 04:27:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8c55cdbe-9f1a-3789-a227-b424ed6baf64 | -11.78045 | -47.31723 | 2025-05-31 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8a650c3-399d-3141-9bc1-2be66064c20e | -10.82338 | -56.94259 | 2025-05-31 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c445cad-c050-3c91-9669-8c17415f64f4 | -9.9664 | -49.81155 | 2025-05-31 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fe9e21ce-52be-366a-9e40-d0236b2ba9d8 | -14.20431 | -47.69914 | 2025-05-31 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da615382-0375-393e-a46d-f56f0d789b2c | -12.02887 | -49.52171 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e894f6c8-0ffc-3e2c-8367-476328981328 | -10.73557 | -49.28241 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6d1e0f67-aff9-3820-94f2-95c025d2de0a | -9.58806 | -48.73042 | 2025-05-31 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8de6df83-8687-3956-a10c-8eb772128e42 | -11.10771 | -50.8742 | 2025-05-31 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be016765-2e83-34dd-a76f-5bf923dac734 | -14.01881 | -55.12729 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d787fbd-1ab9-3a46-9ac9-8dff73796f64 | -13.63103 | -47.44645 | 2025-05-31 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bc7ae03-4f28-3d9d-aa23-371378ae019b | -12.01804 | -49.52374 | 2025-05-31 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2e1a6362-239b-3a63-a1f7-9cc9e2bc19e4 | -9.31673 | -48.45109 | 2025-05-31 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67b44741-8745-3b00-90fd-09ba91e319fa | -16.1207 | -46.8211 | 2025-05-31 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 796ce6ef-3999-384a-9031-657cfd8bb0f5 | -14.01966 | -55.12264 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b861db53-824b-3228-bd08-e6ee8c644931 | -10.64063 | -49.43417 | 2025-05-31 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2c694a16-4e4a-3ac8-932e-381733be9878 | -14.62518 | -47.96725 | 2025-05-31 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d288ec3-0e65-3e5b-862c-ca277b4dbc2e | -14.03124 | -55.14172 | 2025-05-31 04:27:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8510a238-892c-3596-b55a-5a723d10360e | -13.10975 | -45.29104 | 2025-05-31 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82a747a0-a2f6-33cc-9430-4af5f4104121 | -11.89728 | -47.44033 | 2025-05-31 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e33e0d57-0897-3222-9ff2-21236ff44f00 | -9.84923 | -48.14742 | 2025-05-31 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
