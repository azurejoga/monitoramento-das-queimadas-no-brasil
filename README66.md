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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1751a0f-fe7b-3682-a161-2f25c6c9ba7f | -3.10818 | -53.7522 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4ddcb23-8ba0-3951-ae56-9945ab38aa6c | -2.41451 | -54.63783 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a65e1877-2150-305c-ac9b-9b76f248025c | -4.0687 | -51.03542 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 506b4103-1d3b-36e9-896c-5c3ac7f86e51 | -2.57354 | -54.08274 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b00f50be-597d-35ea-afad-bcfd7d4010cb | -3.06506 | -51.365 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2091387a-be83-3876-a06a-3a218b6af17f | -3.01174 | -51.43682 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7609a5f-cc73-3ceb-9db9-db1b11d7de19 | -3.66505 | -54.65519 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2504cdc9-f57f-33d7-804c-6f7ca4af44ed | -4.38838 | -47.76114 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 54fb3a99-366c-3778-b73f-e71cfb96afd8 | -3.64393 | -54.21158 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7364225f-573d-3640-9a54-e8d3cbd424fe | -5.94875 | -44.24649 | 2024-11-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eeb9f8e8-c854-303c-b013-f534ca883980 | -3.00717 | -51.4437 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66745367-9edb-385b-be40-327123469974 | -4.38301 | -47.77738 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d23799c5-40a7-3ff4-8d28-abf78e446396 | -6.12349 | -42.51669 | 2024-11-21 04:55:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fa376f8e-421d-379f-ad80-345aaa6295ad | -3.58861 | -53.89466 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18dcd04c-5665-3169-bbab-f93315595c6c | -3.49448 | -48.22506 | 2024-11-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6077e621-0391-37e5-a614-5af86e7340e7 | -3.55384 | -51.53293 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 162cff9b-7cc4-3807-b125-c99ed799d28c | -2.63199 | -54.29183 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb8d9093-1006-36f2-bfb1-5d19e9ca70dd | -2.57464 | -54.07578 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd9c23bb-b5f2-333e-bef2-a74fe54233e1 | -3.87 | -54.3507 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e16c037a-a7b7-3718-a4ed-14f2120ff3d3 | -3.2281 | -53.61608 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89691bab-35e3-3cb3-844b-86d444a58d2f | -4.05141 | -49.07844 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fce1b27-0653-3abc-b24e-4d6fb93b884c | -3.19497 | -53.13574 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebeb5c57-15e3-346b-9ab9-3e6b06b46d35 | -5.66617 | -47.33919 | 2024-11-21 04:55:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86dc1427-4984-352b-8cd9-beb713e3cb6b | -2.58271 | -51.92225 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f1b29f0-8667-3584-a894-52cde16632b5 | -2.95861 | -49.54321 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec249a6f-c661-300a-914b-cbaa67bc95e4 | -3.57712 | -50.41877 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a027c12d-85d7-3043-9273-7675f628be61 | -3.04397 | -49.46335 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0be50b66-d6a7-38af-8275-24da15742ed8 | -2.63144 | -54.27382 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 748fb4cf-b12c-3a5f-bbbd-0f1d58a4e62b | -3.26809 | -50.62075 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de67588a-d440-3bec-b4fb-8f9c4ffe76e5 | -2.76627 | -52.11742 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a2e0d1a-bbcf-3b52-9654-0147a01fcfd6 | -5.62366 | -43.95425 | 2024-11-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19ffef5f-408a-33bd-a4a3-6f582a18900e | -4.95957 | -49.84654 | 2024-11-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2391250b-14b3-3dbf-a78c-755a04397391 | -3.79964 | -52.22561 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36da2b9a-d865-3c5d-8f5a-0fc72d7abcd9 | -3.26454 | -50.6202 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 311ba97e-167a-3e37-b960-fdaa52d792c9 | -2.57238 | -54.00422 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc6ea627-4de1-329d-8b59-9486851a1c70 | -2.57677 | -53.97651 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0522c4a8-ecec-3895-910a-aa8fb0c9a228 | -3.11576 | -53.70405 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbed0093-33f8-3e58-b08c-04a4b38aab64 | -2.945 | -54.2052 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee1c9e7b-37a2-38f2-ac12-e50215611845 | -3.24833 | -50.56009 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c668c76-e9e8-3101-a273-5d864fced1f4 | -2.63311 | -54.28484 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54090bfa-c3dd-3e60-9766-2a8e9c0c70f9 | -4.05756 | -49.28073 | 2024-11-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6ec1b0f-7f8b-3b94-ac3d-316d8c5bd6d7 | -3.55325 | -50.2762 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bfafa03-0c9f-320d-9b85-4b11d3b55f3f | -3.11038 | -53.17557 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 205c7799-0f56-3768-8155-8f86fb801105 | -2.44952 | -53.68451 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d030c12-a5fd-34d1-9bec-a89e1f4fa354 | -3.11479 | -53.75324 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8c4962e3-0d55-345b-a966-ac421987c905 | -3.99506 | -54.57061 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2cad287-0311-3fa8-a423-fb3c26718184 | -4.24787 | -46.11678 | 2024-11-21 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 973219a2-0d1e-3d43-89d7-9592190ffb1e | -3.53466 | -50.44338 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9569f934-ec2d-3d34-be3e-3d3bf1153069 | -3.51731 | -54.17373 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| affaa87f-56ed-3e09-ab70-9b5d8d9cbf74 | -3.27915 | -53.83226 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d6d618d8-9727-315d-8d9a-9e5417a20ad7 | -6.63851 | -47.3486 | 2024-11-21 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99b2ca1e-7b73-34f3-8cda-6b18badcbc92 | -2.92878 | -54.0923 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f59d33dc-12db-3282-ab08-9c3f04d79f5f | -3.34202 | -54.07907 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c3ae570e-655a-3be4-9cfe-d5a90c16eee3 | -2.78996 | -52.55549 | 2024-11-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b67ff6c-93ce-3fd0-9eec-7fa237c85267 | -4.38973 | -47.76202 | 2024-11-21 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ed120cb-2ead-3361-962b-6485a5a17f47 | -3.1016 | -53.98784 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1feb457-f251-35ea-bce6-02608cf218b6 | -3.28192 | -53.83621 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c3a9f5c8-7aa1-3be1-a6b8-1231e29cf625 | -5.10475 | -43.17503 | 2024-11-21 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 98e7c3ae-7077-37a0-aefd-973fd85e6e98 | -2.74639 | -54.02081 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b4e436-c583-337d-8f5b-9da9e9a36549 | -3.64298 | -51.45476 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e11603d3-6d4a-302e-bf95-363fb3050bcb | -4.14429 | -43.87966 | 2024-11-21 04:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9ce43f1-64fa-35db-a6fb-257c7301b80f | -3.71899 | -53.69347 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 830726ff-74c1-3bd9-93f5-b167cab9e7ae | -7.99155 | -55.31595 | 2024-11-21 04:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d43a81d4-149c-3f00-807d-4c546c4137e1 | -5.24281 | -42.6377 | 2024-11-21 04:55:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41516218-2eca-3102-b705-168447512a9b | -2.79442 | -51.79347 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed09ed96-eecf-388f-bad1-33f4351ba83e | -3.39303 | -54.55169 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62b26ca5-bb28-3438-9d26-1e1aac5684f5 | -3.47439 | -53.28188 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ae129c2-3199-344e-8c85-85db680c97c9 | -2.75732 | -52.10877 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c61cc25c-d6de-3b81-bb88-99ed90b42cef | -2.35165 | -53.89521 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9837098-5115-3717-bcf5-1f6c61b92248 | -3.39255 | -53.71614 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9533b6aa-adf7-32f1-b1b5-7e985680cd64 | -2.72624 | -51.74233 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a6bd2f6-a84e-3be3-aca2-db20507687e1 | -3.48458 | -54.70264 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73834c48-4676-3d70-88b4-3f8a863e7af5 | -3.27413 | -53.02111 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a0f5974-aec5-304b-964c-2250f48bd98e | -3.0977 | -53.17008 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 685aaa8d-2d34-3310-a653-205595dc0e1a | -2.62259 | -54.29041 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ccf65642-235f-3212-a655-13f12ad4a18e | -4.14933 | -43.88422 | 2024-11-21 04:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b813d645-d631-35b5-9079-0a8341dc590d | -2.36355 | -53.7979 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d3641f7-4a19-3ae9-a26b-d25e703349ea | -2.80484 | -51.80156 | 2024-11-21 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91e04681-772c-318c-bf4a-549abf857164 | -3.09837 | -53.20893 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da69853-a414-34c1-9d9a-e109d6940633 | -3.28414 | -53.84361 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 116f7cda-c1e5-3cd0-910f-8d9fefd2f714 | -3.03805 | -49.47657 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a054993-df01-3778-bcdd-960208610170 | -2.76248 | -54.04815 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a5e85f8-839b-3650-8648-21bf5d297b4a | -2.40195 | -53.87862 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa52c2fa-5144-3016-9605-d9c502317716 | -3.1508 | -51.51074 | 2024-11-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d882862-a5f0-3b32-833f-5d68eb7cbd27 | -3.51317 | -50.22288 | 2024-11-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06627fe5-7252-3b13-ad17-94d2c576e016 | -2.33903 | -53.9323 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fdd27db1-7263-3fce-9d9b-d1bb498490cd | -3.15181 | -53.23818 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 74e7b0bd-8f74-3f56-923a-78672d74e4be | -3.66008 | -54.3245 | 2024-11-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a8c15cc-c0db-39e9-94f4-7f90f43cfa23 | -2.58285 | -53.98101 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67f3de68-9df0-369f-b354-dc9b2daf22aa | -2.75916 | -54.04763 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45164cb5-e889-3056-94ba-5b82d0b5f3cf | -3.10406 | -49.45208 | 2024-11-21 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed23d106-4d03-37ee-8957-dcdf02891024 | -2.95399 | -53.71777 | 2024-11-21 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8092781-78bd-3186-b36f-1a31e06416c2 | -2.44898 | -53.68796 | 2024-11-21 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| acf63472-0b89-326f-84e3-c2f9066776a4 | -2.61901 | -51.79953 | 2024-11-21 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10a03c01-a878-3385-ad97-e98cd1236c3c | -3.1065 | -53.74137 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aeea7e90-f634-3c09-b7b0-3729f1f3b9c7 | -3.85808 | -54.08255 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d11c2a56-81ec-3470-9ceb-e99931c86ba2 | -2.76402 | -52.1098 | 2024-11-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2a133ea-2655-3dcc-9326-ad4c0766d42f | -3.28409 | -53.82244 | 2024-11-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 35aa645b-6385-392e-a4a0-9e277b9bfe72 | -3.8796 | -52.38645 | 2024-11-21 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9c7891-0c54-3469-8769-8ba6a43091ee | -2.632 | -54.27033 | 2024-11-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README67.md)
