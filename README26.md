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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c9f3aa0-5af0-3b6a-9885-03d3c2a41bd0 | -2.56585 | -54.05556 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d30395f5-ddf4-3f2e-93e8-b8083accc494 | -3.20833 | -51.42134 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0ec8f3c6-9988-3122-a4e1-6dd78bf601ef | -3.50527 | -53.81631 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96a439df-8009-3edb-a739-4822d6ae75c2 | -2.55354 | -46.55262 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9911422e-0637-3d71-a632-7bccdb73e999 | -3.89705 | -46.66138 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3668bf8e-d12e-364a-804e-4a199360c3a9 | -2.89112 | -51.58393 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2955536a-09e6-333f-b0ed-2248334d0877 | -1.73814 | -52.73244 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b5728f8c-a1aa-3789-9ea6-616613a2f797 | -4.70408 | -46.05003 | 2024-11-25 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a78c708-ee21-39a5-b5aa-40a2d93d0b04 | -1.62628 | -52.44629 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4d7de595-5a7b-3044-951a-5028777fc8d0 | -2.71109 | -46.2599 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e2127512-2af7-38e3-a71a-649c124ab855 | -3.06509 | -53.22008 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9b2549e6-439c-328e-b8dd-81dd250d9997 | -3.88348 | -50.98544 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed8a1b51-86f6-31cc-96a5-3e349c39788b | -2.59187 | -46.54778 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68d2df75-7551-3977-980f-51781f054d39 | -2.65621 | -46.13236 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b95c1796-829f-3e8a-b057-a0510884cfbb | -4.2597 | -48.6961 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc4aba48-a451-335d-bfe4-82fef63214be | -2.58846 | -46.19777 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c233fdc0-ad2c-3f37-a864-8e61856d012b | -3.26859 | -50.56295 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bce0eeb5-1483-331c-a4cc-90bb4787f7d1 | -3.63824 | -51.45279 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e8205a3-1a1b-30b5-a4ec-f00b70ce254d | -2.55934 | -46.56052 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d17fbd7b-2812-3dda-ab22-37aae18a5da9 | -3.45213 | -47.57429 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f5d360-451b-38b4-9911-5f06fed02ad9 | -4.23799 | -48.70356 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f644566-c1f3-3b27-83a9-1eca84fef872 | -3.52421 | -53.81108 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dda1b6bb-6766-32ad-887f-71befb5d94df | -3.81464 | -51.99522 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c44dce4-de93-3751-8bbb-531f6545b07a | -3.19133 | -46.36613 | 2024-11-25 04:33:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e7a8592-7ce1-3e6a-acab-500bcc2a6786 | -3.24654 | -53.27645 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 610358dc-8535-39d2-b383-5b38e4b67b89 | -5.61759 | -43.48126 | 2024-11-25 04:33:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a850f4f4-d7bd-3f08-853f-8dd72531a14c | -2.71064 | -46.28495 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c4b35e5-be15-3292-a733-7ca34ee8ad8d | -3.83082 | -46.54031 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4e43b0ce-b471-329b-810a-25a357d329a6 | -2.70885 | -46.25547 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 305e0d97-b6c1-3c8d-b4a1-896f3b64be2e | -3.3398 | -46.61454 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfec7859-45ba-3091-a919-9ce6d7009673 | -4.36566 | -48.08469 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cfe992cb-0b3f-3bbd-9a4e-03709cfc5ff8 | -2.79976 | -53.00961 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 289ccd5b-b4d4-32bd-9216-4194636f63af | -3.31903 | -53.288 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 347519e2-0f76-3f32-a56c-3f709e8cfd08 | -2.33552 | -52.18359 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b0c2cf6a-f6d4-3d36-94d7-f8b4b1f3e4cb | -5.8089 | -47.90313 | 2024-11-25 04:33:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18b2e204-bc18-30e6-a658-8e1091b4f57a | -1.61747 | -52.59507 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5e1e8b6a-eb3b-31da-9cae-8687481ac9c8 | -3.9746 | -46.73102 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 054c4146-4eda-3b61-bd7a-6cd40bb0cdef | -4.24238 | -48.63223 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8e7cd415-61e5-3842-bdff-db3042072574 | -3.47758 | -51.98983 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 95658e9e-e44b-3dd1-b50d-f71c58e7c749 | -1.60617 | -52.58553 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21dd2a83-fd4a-39e1-addd-4729daad96c3 | -4.79608 | -49.00169 | 2024-11-25 04:33:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caf96925-1701-335c-ac08-f1f6846b2ef4 | -3.81385 | -52.00007 | 2024-11-25 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6d09f52-94fa-3956-9bbb-98dce1e6a485 | -4.25636 | -48.69558 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 279cc2f6-f61c-3757-a06d-ac5254dbf8be | -1.72379 | -53.24945 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31c533ac-11fe-3271-9de6-a4594d1bcc3d | -1.63327 | -54.46498 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b04d05a-8a50-39c7-bafa-b405db2d8b16 | -1.62388 | -55.1769 | 2024-11-25 04:33:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99822f3a-9fa1-381b-9618-9729f8c53742 | -2.64496 | -46.24927 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 167b1176-6d9c-3a08-bd4c-df4f5f6752e1 | -2.33954 | -52.18423 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1321baef-35a2-3747-94dc-e9f25d64aac8 | -3.39042 | -50.32158 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bb431af-6d20-3712-a18c-c74b054d5041 | -3.26952 | -53.82129 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c289f08f-75d6-3723-af0e-2328b2a385af | -1.62726 | -54.46696 | 2024-11-25 04:33:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8038f1c6-3012-3594-8956-cfea18d84e49 | -2.71614 | -46.27145 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fa1b47b-b158-3e61-8d09-868632e8c5e8 | -4.47656 | -45.65471 | 2024-11-25 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1610bbab-c6fd-3d3f-9027-efab7d7c50e0 | -3.92386 | -46.39954 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd5c723d-8a56-3a86-b87a-9ddd6fc15fdc | -4.47308 | -45.53882 | 2024-11-25 04:33:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2415322d-37b3-38f0-8169-5487fe2bcb27 | -3.94952 | -46.69502 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c846061a-5e7c-33d1-9810-f00c1386f264 | -4.04721 | -48.31553 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40ea8e3d-31e7-3025-b3b5-ec57034858e1 | -4.03326 | -48.0784 | 2024-11-25 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9dff562a-909f-3ed2-9747-166e5b5dc482 | -2.583 | -46.53932 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78a5f6fd-4d6b-34c7-af8a-c38bb4bd1095 | -2.65287 | -46.13184 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a28f8ae-6b4b-36ef-ba74-8da1918bc8f9 | -3.68569 | -47.12527 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fca3f95c-0292-37b6-9310-dbf72a04c481 | -3.33253 | -53.71252 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52329080-e7bf-3e5f-95a3-d469412751a9 | -2.86215 | -53.97066 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e35ffd9-1f3f-3cc6-b02e-0da930c008f4 | -2.69726 | -46.28598 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6730541a-690d-3cb8-a027-4eb9b3834abe | -3.86203 | -46.88725 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| becbeeb1-064e-3446-903c-6e89e9bdce64 | -3.68847 | -47.12922 | 2024-11-25 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f50a411a-4f37-326e-94fa-554b63e16d7d | -1.46889 | -52.6795 | 2024-11-25 04:33:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b45d7025-b56e-34fe-a202-a220cc439857 | -4.43614 | -46.35881 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fe79cb6-6186-30cc-a769-44735010ed77 | -4.23164 | -50.66316 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47a21007-ff1f-3423-b904-e5b362e68b51 | -3.21211 | -51.42194 | 2024-11-25 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 806acc4d-2c1d-309f-8f1f-083f2f8e6c76 | -1.62272 | -52.44192 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff0d6422-19de-303d-a8ea-65367d8711ae | -3.58327 | -52.18287 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33f2aaa1-e81f-39d5-b080-fca6f19f623e | -3.8269 | -52.41431 | 2024-11-25 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76a4ce1f-28c6-36b3-a67a-1ac9dbd944a6 | -2.39854 | -47.91756 | 2024-11-25 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc33023e-5cba-371c-98cc-f794a52ae9ce | -3.94718 | -46.90818 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4772a362-9f1d-3e96-a2e8-be1c9e2f14e8 | -2.79194 | -53.00439 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 583eeb24-46ff-3d3c-9c5e-d19251e2b0aa | -4.2137 | -46.37554 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42c2ae7d-727e-35cb-86d9-81373bcae973 | -3.97648 | -46.6527 | 2024-11-25 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecf4b7a7-fc56-37c5-9ed2-0b4258a866b9 | -2.67387 | -46.26087 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfd238b7-26dd-3964-87ac-3fa3f11b2ded | -2.97037 | -53.85796 | 2024-11-25 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0bc2a45-9912-3ce4-9dfc-dd2398bd2601 | -1.77056 | -53.6264 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c188ac50-5d1a-356f-af0c-e5b60af93b79 | -2.80867 | -46.81524 | 2024-11-25 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24a17bd4-8cd4-30e6-b4ea-29077ed25aa0 | -1.76828 | -52.70543 | 2024-11-25 04:33:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a69ddc2b-baff-3881-8d58-aba1ad19c64d | -4.65144 | -45.35947 | 2024-11-25 04:33:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60dc0433-bb6e-3d03-ab25-78f7d72abc86 | -2.71344 | -46.28896 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f03251b9-e5a1-3d36-9e06-da10bf9c545a | -4.25137 | -48.72734 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d307cb25-a68a-3de1-b96b-630b2e262738 | -3.39398 | -50.32214 | 2024-11-25 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bcac0066-bc7d-3630-ada4-72aa0a213889 | -2.64503 | -46.57722 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ac6b881-d405-3f13-b490-99b546e84bbd | -2.68054 | -46.26189 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34de4684-c64a-38bf-b765-60cd6470b12b | -2.71183 | -46.10481 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59599539-a2c0-3bf3-a994-660428b78005 | -2.79492 | -53.01281 | 2024-11-25 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e71e1b2-ea1e-3447-b473-ce50469b50f7 | -2.62792 | -51.77008 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bc0008c-5308-3632-aa1c-f72a499619c3 | -2.80219 | -54.02623 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 23fbc811-1b6d-3171-9147-6b09135cb8e3 | -3.18811 | -46.56226 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed22f4d1-9af9-3034-9b22-ba8cf30ceb71 | -3.3102 | -46.67401 | 2024-11-25 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b181a82-1ff4-32cc-b2ad-9838036032b3 | -4.23855 | -48.70004 | 2024-11-25 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 381cc39f-9645-3713-9683-7d21eb8825cb | -4.57186 | -46.2953 | 2024-11-25 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8109b7c3-6bd0-32d6-aa51-1104ee062cd7 | -3.35048 | -50.51202 | 2024-11-25 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1669bb4e-9144-3d25-acd9-9216ebf65481 | -4.08735 | -50.36466 | 2024-11-25 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d63ae97e-8664-3d21-a838-af58fbcad1e1 | -2.85837 | -53.96547 | 2024-11-25 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
