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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b216c937-f580-3731-a6a5-74069fd6ab9f | -5.22649 | -44.91995 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df33addd-dab3-3a1e-ae0b-49d6219ed727 | -1.2593 | -51.59013 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51b4015e-ca6e-35df-b263-1c7a82bdb74c | -2.02194 | -51.1953 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 22f85de7-054c-30c0-be9a-e4b6a1bd5415 | -3.21095 | -53.84217 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75d87c6e-f638-3068-9451-c629b7c5a49a | -2.96873 | -53.93427 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea2998c3-a206-39da-a046-76592ac6801b | -2.79899 | -54.04184 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 608c004b-ad86-3308-a825-8261bba8e976 | 0.98423 | -50.26406 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67ecc8a3-3f50-305b-8b45-fa69bfdd723d | -5.63035 | -46.95925 | 2024-11-29 04:57:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d8729166-3ee5-30e4-ab1e-c7063c9fe395 | -2.23429 | -53.6926 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0fb9bab8-970f-3737-8a3f-22ffe4bb1c58 | -1.69384 | -52.62138 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e072c242-6479-338b-aa5a-77da9b3863cc | -3.78299 | -49.36385 | 2024-11-29 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0a39135-811b-30f5-9a46-e0b4a3ca9ea5 | -3.46556 | -50.53748 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4671d487-3a92-3e58-9151-5a05bbd1ce44 | -1.33569 | -52.54039 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd7afdd-7394-311d-b81a-8769842db8e3 | -2.5046 | -54.16159 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e5f2c59-9eae-3ee1-94d2-a3ba697d7fde | -1.62123 | -52.69477 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6b7539d-6eec-3a82-99d7-646ab3a38efc | -2.3359 | -46.87154 | 2024-11-29 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 841b40e9-710c-3bce-9296-a8a99af41e04 | -2.46121 | -48.57491 | 2024-11-29 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e0c1f4a-8c6e-30fb-bee7-5bb8abf36a39 | -1.18566 | -51.77469 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bbd3018-d730-313b-acad-441ac3aa553e | -2.64535 | -53.97857 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 208c0e1b-73a1-37ed-bad7-71060ab22768 | -3.00421 | -53.72869 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60d1ea41-e68a-3a86-8928-687d705b572c | -2.86398 | -54.03775 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d0c67121-c44c-32c7-b165-126d24458a5e | -2.86051 | -53.99494 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8279c25-3a7c-3e1a-b3cb-c25b534ccd70 | -3.25024 | -53.63372 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a0a74e1a-2469-30d7-9923-5cd49b203075 | -2.83491 | -54.07206 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd671206-2b8f-3d4d-9d02-df291e2281ea | -2.52217 | -54.13598 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33624cd5-4fb7-35c2-b902-bc6bd88f5f4c | -3.69623 | -50.22348 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a5fa823c-b62c-34cc-ba83-fe700caacab0 | -2.06359 | -53.39152 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aa0e4a9-eadb-3e7d-9b2a-1056051ae764 | -1.38015 | -52.84495 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da28001f-46bc-3dbf-8362-85ea2eae47a1 | -2.57073 | -49.99585 | 2024-11-29 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71b4266b-9f04-3d6a-b824-a744850a0858 | -2.83846 | -51.84 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eae3ab15-99d3-3993-b7a9-73650d04e7e8 | -1.62324 | -53.88187 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3ecd089-f6cc-390d-ac57-08cb959c97ea | -2.86935 | -54.00335 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 22e87b86-2a84-3d23-9455-be54c13f1f4c | -3.69254 | -50.22293 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d07e8c00-0776-3344-a7d3-60eb8e4b2be5 | -2.72463 | -48.67244 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70279a4d-e25b-35c7-bf6f-ece38e0bf694 | -3.1417 | -55.00311 | 2024-11-29 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df7914aa-750c-3d92-91b0-13e8b0cac544 | -2.43796 | -53.97763 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46fc4e75-3c09-3125-ba65-91d86cfed18b | -1.66278 | -52.73304 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d104ff6e-5d74-3de6-a65f-ef1cbf5e275b | -3.19907 | -46.59863 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a09b0418-db6f-3f7a-9945-9b619ce27334 | -3.43358 | -54.11687 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e79bd91e-0942-3de9-bc7b-5be13277d4ba | -2.57373 | -54.32836 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50e8c952-4f10-3bdb-b599-1e0c73ee091f | -3.41637 | -53.2225 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9abe88e1-fe10-3024-a0c2-7c2df8d055d2 | -1.10171 | -53.60617 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1de5174d-ad8c-36f1-ae17-1e722285a77e | -2.25491 | -53.62548 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edf209e1-cdc8-3727-a3fc-e324d7fd09de | -1.04279 | -51.73804 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d99680d-7a45-3b32-839d-718bc19ffbf1 | -2.02187 | -55.20592 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2de40851-ece4-3595-95a3-35fb77ff1e66 | -5.38847 | -46.10972 | 2024-11-29 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2660487e-6d3c-39a4-b536-95e1ee83075b | -1.26482 | -52.64666 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 734f0639-5d7d-3db8-9923-d3ca526fb4bb | -2.32578 | -50.6737 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f391c38-9464-3703-960e-811aec6f715a | -5.22319 | -44.92383 | 2024-11-29 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 210be1a5-8caa-336e-a55e-28e3f63d6151 | -1.65453 | -52.74239 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 992ae08b-d9b3-3d06-b8f7-336c3b0ee436 | -2.21574 | -52.48057 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4f4ced6f-5196-3983-9af7-9144e61278b6 | -3.09834 | -54.04298 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4c14a8-8b5e-32dd-8cd3-f6b36d698101 | 1.67778 | -50.66394 | 2024-11-29 04:57:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1326dadc-0eb6-3168-940a-8f44ad2e5def | -4.44048 | -46.58342 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 48d60b85-54c3-3418-822e-39163312ceb1 | -3.22035 | -54.17484 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e54acf01-6c2b-3075-a595-f93c12e6b9d0 | -2.3643 | -55.70961 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 934f339b-edef-3642-bcc3-fc562f0c6b30 | -3.11565 | -54.47398 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0de322c9-6f61-3b0f-9c31-3e730c0aac07 | -3.21557 | -53.37854 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 982e8842-ae1f-3240-9299-b5c9f883a20d | -3.31395 | -53.74922 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 888eed1c-9a7f-3e71-b522-d4cd61ebd654 | -1.38572 | -53.63662 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b400ff8a-0d50-30b7-8c8e-2ac7b513204a | -2.9144 | -51.71168 | 2024-11-29 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24a44e43-c03e-3c4b-8eac-7f56442948ed | -2.26579 | -53.46908 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8287d1b2-9167-37f3-b8f7-ac55a0736b58 | -3.49952 | -53.80325 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da32858f-29ec-3d39-9abd-650624716e6c | -1.26713 | -55.74702 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc75c29c-57a1-3b8d-a5f6-dcee46bedbcb | -2.96128 | -53.72207 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8ac5de1-d243-30d0-8c56-cc9cb0b265c3 | -3.36511 | -51.62981 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 00fd72b2-6c26-3cd2-a7a4-afee543dac62 | -1.20546 | -53.68255 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5af89b1-8995-3151-9d54-d31561cc42c6 | -3.78129 | -50.13738 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35bc9ce-7ed1-3847-a42b-4fad67ce6883 | -2.25652 | -53.74523 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5deaa39-c36a-3b9d-8d84-45319ce4c630 | -3.17395 | -46.31067 | 2024-11-29 04:57:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 701cf9f0-cb1a-3b20-9dca-e4a94854d20d | -2.0213 | -55.20957 | 2024-11-29 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75d4b817-312a-3639-a53e-bb52aadfc2a5 | -2.88859 | -54.16516 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1ef1aeb-9635-30f3-8ec7-6af7b7ce58a9 | -2.00274 | -51.16603 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38be029c-95e4-3d16-88ef-ea194438e59f | -3.96772 | -47.23807 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa4e0769-a193-3165-be5a-97af3d703cfc | -3.11714 | -53.26765 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02cd9d58-b3a9-3547-8837-6f530716ac13 | -1.55203 | -54.77434 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44b2e6b2-49a0-333c-9d53-a597f9a8b387 | -3.58162 | -51.31917 | 2024-11-29 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9970e5bc-95cb-3bf4-a94c-17aeb5c82568 | -1.54077 | -52.66471 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f1b602e8-74c6-3ab0-b3d5-c18022d95d3a | -2.85153 | -54.0958 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f224f5e4-1d6e-3362-be4f-2e8f719d2ff4 | -4.06637 | -46.82554 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9afa80c2-bcc2-3736-a847-eba6740c72b0 | -1.20566 | -51.62273 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfe592e8-b8b7-37d3-8fa4-1a0b1d7841e7 | -2.8371 | -48.09429 | 2024-11-29 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a46b5237-beb4-3365-a618-7e88f7c1eb08 | -3.9804 | -46.64643 | 2024-11-29 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e443696f-977c-3728-a0d8-4c963a7563a5 | -2.45998 | -53.70648 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5857e3a-5b72-3394-8c50-10ec9ce5c3a0 | 0.27624 | -49.80648 | 2024-11-29 04:57:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cae4896-ca09-3264-ac87-f2023282fac4 | -1.44486 | -54.52116 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 183ee468-2747-3d88-8985-0f8c8fcf4a08 | -2.80237 | -54.06351 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4f4c916-0a29-3d26-b2db-3c542ebd9935 | -3.0811 | -53.30082 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ec4be48-dc7b-3b8f-b468-9f631cae9865 | -2.83699 | -54.03712 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78cd0754-d117-3537-9946-9606a0d8b370 | 1.20797 | -55.97501 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 817027f5-580a-3b76-bff3-5eccae2c0a26 | -3.24917 | -53.64059 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 690fdbae-8486-3faa-bc6b-fec6a9894aea | -1.18959 | -51.77163 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9719abf-2e06-3994-a756-565d15d60f4d | -2.87658 | -46.83865 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4f8fa8e-b560-36ad-921c-2860c99947fe | -3.15758 | -49.42941 | 2024-11-29 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 59d8822e-92b4-3f26-89be-612bc1f307e4 | -1.09033 | -53.37244 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50b21838-f97c-33d3-8c60-feb97a5c9f14 | -4.48279 | -55.78892 | 2024-11-29 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1b8c286-b79e-3c41-8925-4137f1e444e4 | -1.08488 | -53.38564 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d22e811f-5f44-30fe-98a0-b62624239797 | -2.82899 | -54.10998 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7531fef6-9cfe-3523-b4d1-c04d33312256 | -3.49568 | -53.80617 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3df0610-1671-31c0-82d7-5b8224778d5e | -1.99061 | -54.89765 | 2024-11-29 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |


[Clique aqui para ver as próximas entradas](README51.md)
