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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94b406e9-ea34-3251-9d6a-c3634bddf591 | -6.51492 | -56.19743 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93f57175-6b40-3406-8fce-8a8fbbbba8d8 | -6.6196 | -59.98018 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1be1ea82-edf1-363d-ae0a-2f8a5c6fce1d | -6.81405 | -59.27339 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a7fa49a-c97e-3db4-8c1c-8b6bb71d8ce0 | -6.5089 | -56.21419 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7750323f-aaa1-34d4-a017-f95cccb9879c | -7.08314 | -60.04726 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec15f2c9-fc3b-3a11-908c-b057b8c43b6e | -3.2255 | -49.33577 | 2025-08-01 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c179d84-c66e-3535-95f7-0f62de4db8a8 | -3.39212 | -47.48959 | 2025-08-01 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c5d9c9d-ec9e-3781-b522-61cef0c9379c | -6.55953 | -56.19377 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 954916c2-22df-3a30-8395-daac0e24b547 | -6.82266 | -59.26612 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.7 |
| dc24380a-10a3-3bb7-a43e-3f0d7924ed2a | -6.55676 | -56.1898 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4259b69f-1ca2-36db-b2f0-783fd98f4324 | -6.674 | -56.39591 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66173943-0f95-3435-a2d1-5a2ece431769 | -6.73056 | -59.16318 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b96e42c-3463-390c-8958-cea54a7e623b | -6.55129 | -56.20311 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0a37f3-1250-3939-bee8-7536edc40dd6 | -6.50723 | -56.2033 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4830619-42d2-3ae4-bde4-0eb36a12b813 | -6.82197 | -59.27032 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 138.7 |
| 46d5ba36-bc92-3716-b872-d5aef7a355bf | -8.03585 | -43.1176 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| ab28327b-82db-3d7b-b8cc-68f97634af21 | -6.51606 | -56.21177 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9c19ce6-6800-31b5-b412-06b749ca37d6 | -6.74 | -59.17323 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6386995a-603a-3dbd-985f-ab7adbdbcdb9 | -6.66961 | -56.40232 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d81431ce-a8f0-3fb9-8992-05592dbad375 | -6.56776 | -56.18444 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7771ae00-648f-34e1-90d5-3e41ccb0954f | -6.82989 | -59.26727 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 46e33fe3-585a-39f5-aac2-698d64e5c75f | -6.52706 | -56.2064 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d884faf-f3e9-3001-b951-0d68174b6b6e | -8.04355 | -43.11222 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 2aad73d7-7869-3a19-b8e9-239c68145a5f | -6.83124 | -59.25897 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| f1988557-0c41-3ec9-8d9d-75553b0707e1 | -6.74698 | -59.15304 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77451f6d-600e-3d16-a0d2-f769df5b4761 | -6.74496 | -59.16545 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 5eef8161-6602-3799-a796-21c92efd82cb | -6.83418 | -59.26371 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 06e71b47-1dba-3bb2-a089-fa3feb29fdf3 | -6.50777 | -56.19984 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12cdce9f-eb83-3f76-b654-46ea985b753d | -6.62261 | -59.98542 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23a7a561-70df-3fe2-b980-daf1edefdc4f | -6.64435 | -58.82376 | 2025-08-01 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56f2e6fb-a196-34ec-bc65-ca6f34af0ecf | -4.55725 | -55.75319 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e69f6d35-082c-337c-a792-55f721ad63c3 | -7.07787 | -60.05561 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 883c769c-fc09-3cca-8f57-cbf935d3bffa | -6.81973 | -59.26137 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5dc01ca2-12a8-3e77-b625-f19d2b5fb7be | -6.82041 | -59.25718 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3a3f2352-9d76-3145-b2fd-257a233ebb12 | -6.51769 | -56.2014 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 519fe181-a811-3775-980f-5ba2be352e93 | -8.05889 | -43.10552 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5490c152-d13e-381f-9a41-332e18ea9bf3 | -6.74428 | -59.16962 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 529e1c97-46a6-3946-b890-9e258d5c9f12 | -6.64457 | -59.09114 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 456bd232-d829-319a-9a8b-47fc7179a0b1 | -6.74991 | -59.1577 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61583d95-ba5b-3d22-b7e9-9f6c633583ba | -2.90153 | -48.2495 | 2025-08-01 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0237fad8-86bc-3f44-9a3f-f4bcf72c9e74 | -6.67124 | -56.39194 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62288742-04cd-3f37-88df-dca453452e26 | -6.62712 | -59.98148 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe57a65e-05e9-3abb-b72e-8915729cb010 | -6.72852 | -59.17566 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2dfcd40f-6e48-3a0d-b6c6-c279b0bba93e | -7.07938 | -60.04667 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cca83e58-f3f8-3f96-a0ef-d2dffccc0ca9 | -6.67238 | -56.40629 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18f1b386-c746-3561-87fc-cb5426235841 | -8.05815 | -43.10772 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4890e2e0-46ad-3bb6-8f44-812a4d8e19ba | -6.73415 | -59.16378 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 421acde6-6ff3-300e-a277-ac9b14c30bbd | -8.05126 | -43.10675 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 4cf3f4b2-6394-3f6b-889a-f0af5a22062e | -6.73347 | -59.16793 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 67fe6e72-dddb-304c-80ae-a835c97bc7d7 | -6.51714 | -56.20485 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 341d42b6-c5d4-341b-9102-f2acfb406fde | -6.82402 | -59.25778 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| d26d41dd-5e93-3898-9468-1fe320a1832c | -6.67015 | -56.39886 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c05d07d3-57c9-3a1f-911c-fa24090789a8 | -6.54413 | -56.20554 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94b24900-9def-319a-ba8c-728b3e7ae646 | -6.73504 | -59.18096 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 483267af-7704-3616-9e2d-eea99931e42d | -3.50377 | -43.23778 | 2025-08-01 05:04:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e84dbc83-fbe7-36e3-9157-ff539a09471a | -6.82763 | -59.25837 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 730a4d78-fc47-3098-8639-1c5cc83afc77 | -6.62336 | -59.98082 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7dc32db5-ece6-3478-a563-5238e0e8c8d0 | -5.0594 | -56.92965 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fafdd21-3a0c-368d-aef6-8aec2f475d9c | -6.67069 | -56.3954 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1031143-e62b-3008-a4a7-8caccd9a40a2 | -6.81181 | -59.26445 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a6daa571-9e95-3817-b777-cf4e535fc0ac | -8.04355 | -43.11638 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| fba2470c-a973-3c17-9c19-3e2c042fd60e | -6.54522 | -56.19862 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2e84d13-0184-366d-8895-4db431cc76d2 | -6.56007 | -56.19032 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b93ed7f3-ac0f-338e-aa11-bf841c6da89c | -6.64391 | -59.09521 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 9f7adee0-54e1-37d5-8b6b-b19c2fab4d20 | -8.03667 | -43.11536 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 060295e5-5458-3194-af55-880470d96774 | -6.74293 | -59.17793 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d415af14-612f-322e-8c29-bf6fc2eaaa6a | -7.07838 | -60.04775 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9954ac1b-4946-3045-941e-b35ebf586527 | -6.68166 | -58.86274 | 2025-08-01 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06f7d133-8489-3a4c-a27a-604e70834c78 | -6.82627 | -59.2667 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| f467caff-5c3f-3360-8a4c-7e9c41181e35 | -6.6475 | -59.09579 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 1f2dc0cb-d83e-39cd-ac2c-432e1100656b | -6.81474 | -59.26921 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c5b585c4-e277-360f-8ebc-e975b0a013df | -6.8125 | -59.26025 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b3c4d771-5403-3f13-9e66-1cd6f8dc0e62 | -6.50465 | -56.19566 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8f47b17-e210-3aa8-8104-6fafbe6a4919 | -6.81611 | -59.2608 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| db373096-e186-314e-9d4a-5c13af5fdf51 | -6.5166 | -56.20831 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d476e7ee-bd76-30d0-94fa-8196d073a3e2 | -6.62185 | -59.99005 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c30fe05-568b-322c-a6bc-fd3256b01aa0 | -6.6479 | -58.82431 | 2025-08-01 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79bb347e-80eb-3e47-92c0-13d8d6f72825 | -6.67623 | -56.40334 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3be6732-8b73-3894-b733-aa2e4bbcefa6 | -6.9587 | -56.38107 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4b31ed5-45c3-3b22-8eff-ef08018dcf0f | -3.503 | -43.24318 | 2025-08-01 05:04:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0e28365d-1e98-326c-ac31-5e5aed009eea | -3.3641 | -49.15874 | 2025-08-01 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed2e777e-5ece-3fa6-a015-9b659d863b9f | -6.64855 | -58.82031 | 2025-08-01 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfd8e21b-6c84-3253-82cd-e9f2c17464d1 | -6.56283 | -56.19429 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 630735f6-6f50-38a8-8e7f-0f7a5e738f53 | -6.7463 | -59.15717 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 09d4cbf3-ce70-30f2-8c03-cef864f79609 | -6.62562 | -59.9907 | 2025-08-01 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0be88b3e-53ef-36ef-b8e7-c55e3cb2729c | -3.51021 | -43.23884 | 2025-08-01 05:04:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ca4c68f-a226-333b-bba2-7bcb220f0956 | -6.7364 | -59.17267 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 77429618-f5fd-3c6f-baea-6b60542c39ba | -6.55074 | -56.20657 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d458429b-1c02-3acf-b3e1-19e273bcec8a | -6.51877 | -56.19449 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c91aef78-12f1-3163-bd1b-722641c82484 | -6.73865 | -59.18153 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 19d511f8-0853-35de-b948-bb80d6ddc6b6 | -6.5573 | -56.18635 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df8c7575-fef4-311d-aa58-5a7ba98dcb4b | -6.65746 | -56.39331 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29e5920e-69e3-3abd-897a-898d69484417 | -6.54576 | -56.19516 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef36c75c-30f4-3f58-b144-00a2b891b9fc | -6.55015 | -56.18877 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 605d22f7-7086-30d3-b33e-5102c26dd853 | -5.06332 | -56.92664 | 2025-08-01 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfc760f4-681b-31ce-a2a0-cae742278d89 | -8.04272 | -43.11861 | 2025-08-01 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| b4a264f6-4c1e-3e1a-980d-ae287c83aa02 | -6.73775 | -59.16437 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 76862ef5-cbfe-3e14-a81c-4025ad4435f9 | -6.73977 | -59.15193 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 564fddae-45a1-36ea-9a6b-c1755eb1a08e | -6.82696 | -59.26252 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 76e734d2-1c16-3746-b4e2-df53558b956f | -7.07462 | -60.04713 | 2025-08-01 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README20.md)
