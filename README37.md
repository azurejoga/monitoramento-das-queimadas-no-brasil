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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66cddb29-fafb-349e-a111-beedfe2e9a70 | -1.79197 | -48.07084 | 2025-10-19 04:29:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 39020304-b0c2-33dd-8cc6-73cb7788ac89 | -2.87334 | -50.71986 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da866394-9f3f-3da8-84a5-8d1e7401fd5a | -4.42489 | -47.75412 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b9bf7e3b-47ec-3ba2-a995-50874c05ff2b | -4.14735 | -47.66064 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 283786be-af4c-3205-b259-3bab6069ea04 | -2.92482 | -49.08092 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf2abffb-6d57-3647-ac59-b5882566981d | -3.15688 | -49.16652 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12feb4e0-d1c9-3565-9299-ec6d2f379544 | -4.91917 | -45.98841 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63750950-8563-3cf2-8c11-a2ad3ca8922a | -4.52123 | -48.83619 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4db7858b-975e-3582-83f6-7106ef3b5795 | -2.79002 | -49.64886 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61e01fd8-460b-38f4-8590-23d6afa5955f | -3.48526 | -51.47887 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d195bafd-36c7-3097-a239-66e3e36f7714 | -3.97845 | -48.08311 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70b3a981-a0eb-331c-b11c-c5ec427f3e70 | -4.33563 | -43.60554 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 241b5403-52c2-302f-873a-027ee47765df | -3.80394 | -51.64306 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15bb2b1b-ff9e-36bb-9f73-9c7b032347e5 | -4.83021 | -43.01692 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8882e041-f6c5-3261-b84d-84089efb5066 | -4.52993 | -48.41573 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dcbdf62b-3650-3cfa-b68d-624c9c23a093 | -3.80704 | -51.64864 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24da007a-8a7a-37f0-99dd-c0caaadd8df7 | -2.90877 | -52.72659 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a72e2e5-95c2-3995-a28c-22e02e950043 | -4.46591 | -44.97543 | 2025-10-19 04:29:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1147481d-cd59-3660-ab64-5a490eb22bdc | -3.46147 | -50.09369 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e40f0bb-d2d3-3c31-96a6-d2007e6bac31 | -3.13891 | -50.25964 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a7ceb55-6500-35db-be35-edf6701d7ba0 | -3.01895 | -51.35322 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fbdcf68f-354e-3909-ae95-146da76c57a2 | -2.57164 | -49.11568 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb7eb57c-602d-3dce-93b8-d8217748760b | -4.42009 | -43.959 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11f201d9-9095-3ce1-95dd-b6e0e999c808 | -2.70404 | -49.86731 | 2025-10-19 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27492ed4-8b17-39e7-8081-2c4798338cc2 | -4.23075 | -44.68996 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02224dc4-6dd0-31c9-83ab-b9c8eda901f8 | -3.1496 | -50.24283 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09ff3125-4647-3e2b-9f61-68e4c550717c | -2.65445 | -49.52243 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f5af224-d807-37da-967a-020320b1ef79 | -5.33537 | -42.55232 | 2025-10-19 04:29:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 52300a1f-4061-3fb3-a99f-e096a8ee4c38 | 1.7906 | -55.71921 | 2025-10-19 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3126780a-43cc-34cd-9892-a036e01b638b | -3.89412 | -52.4076 | 2025-10-19 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 633d04e5-9443-388a-987b-b51f48bf1592 | -4.13213 | -46.22478 | 2025-10-19 04:29:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40f0a53b-22d1-3f0b-8863-4121be68ecd3 | -3.39644 | -54.06285 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3dd5d494-44dd-3fc4-829d-5700e0524953 | -3.52246 | -49.93394 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e27c4bbc-d982-3988-9d6f-29c08c2f9003 | -4.41814 | -43.97169 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00450092-8957-3840-b0ef-4f4ed95868d2 | -3.6438 | -49.96919 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50631898-34b5-320a-8c8b-d8d5e5c99b31 | -4.96502 | -45.9149 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bbd3fa13-2f05-389b-9750-90b998b1bef4 | -2.74017 | -49.39112 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca3df4de-f32b-3ac7-bc1a-8c7d4e05bfa1 | -3.09109 | -49.22228 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5523c975-78a2-39ce-baa8-2c0400d6cd2f | -5.08972 | -45.42639 | 2025-10-19 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f9e9322-1baa-3e50-a9a5-e5a02549a1a0 | -0.35175 | -50.36721 | 2025-10-19 04:29:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f57f63c6-094e-3112-ad97-0a09637023d5 | -5.10723 | -44.2113 | 2025-10-19 04:29:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b45d0d-291a-3b9d-a2df-d26c4ab1deaf | -3.29282 | -50.00858 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75d43349-8542-378a-bff2-582c7ccb3d1d | -3.8641 | -49.81778 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd89eccc-88d9-3b5d-a71e-9009048276c7 | -3.86475 | -49.81382 | 2025-10-19 04:29:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cbcb93f-756c-3daa-80e4-3395e0f0557f | -3.22414 | -53.14197 | 2025-10-19 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5efcbb7-4a01-3d4a-9458-0a22fd89b67f | -3.14456 | -50.24752 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0abe3f53-7a69-3985-9d27-6ea12a43db60 | -1.49276 | -48.98884 | 2025-10-19 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b5dbf1-43cd-3902-87ab-b6a81ef80558 | -3.14527 | -50.24647 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 016e7596-a7b0-3599-88a9-2fd06b1ac5be | -4.26038 | -48.55555 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 084ba1a2-b104-3f6f-b87e-f2c19122da60 | -3.97322 | -47.57983 | 2025-10-19 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88f6a40f-11fd-3f4d-a579-0a2652731a6d | -3.14886 | -50.24387 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3353f168-9adc-37f9-92c2-4bfc472d9405 | -2.44285 | -49.37402 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 65cfe0dd-7153-3263-8051-a29077153c2b | -4.23873 | -43.09713 | 2025-10-19 04:29:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63190fa3-378c-3e26-a6ac-944f6419cfac | -2.9648 | -47.89865 | 2025-10-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acd0ec91-7721-34dd-b164-c5c5e0decff8 | -3.972 | -48.91452 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 682f04b4-baf6-395e-b43d-0b03a6cd0720 | -2.69979 | -49.87084 | 2025-10-19 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9dd2643a-db21-38d5-ab9a-06f4b56e6899 | -4.21554 | -48.36236 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e4d3289-3cbb-3482-aa9e-4e858cb6a51a | -5.42956 | -42.73055 | 2025-10-19 04:29:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5aed977e-9221-358f-b5c5-df45533c36d9 | -4.77191 | -45.89247 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11dd3c3c-a74e-3828-987d-250189d25153 | -0.43243 | -51.964 | 2025-10-19 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a9f96de-1800-3104-b020-4b2d8054062a | -3.26891 | -50.12455 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 145e4313-db2c-3d94-bf7d-948d98c4c05d | -4.25759 | -48.55142 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1cfdcf27-4a7c-39f1-99e8-a63ef0542dc2 | -3.75966 | -44.99082 | 2025-10-19 04:29:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| afa6fb5d-738c-32ab-b823-9f5c5dbbbf08 | -5.21541 | -43.74619 | 2025-10-19 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49e92654-1069-36e1-95f1-40657b80851b | -3.824 | -48.6526 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03674848-db6c-3e74-854e-e2e5edf71abf | -2.79293 | -49.65342 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c166903-5244-30af-9b6d-e78c92e369a2 | -3.81762 | -52.13998 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 429ad404-3a84-379a-b30b-b810f8a9baf2 | -2.2531 | -51.9109 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 14d7a385-0f31-3f69-8369-4de1e655225b | -3.60578 | -42.85796 | 2025-10-19 04:29:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57d26bf6-c408-3571-9b87-7cb6333aa8ed | -3.33046 | -45.62399 | 2025-10-19 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7c9eb13-28a6-3144-9bbd-54146afd38ac | -3.13728 | -50.24636 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b51e8084-98ac-3979-a6b1-5dd85c468850 | -2.44825 | -49.36284 | 2025-10-19 04:29:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 185d0ed5-eb98-386e-b257-68d6fdeabb36 | -3.46955 | -47.69195 | 2025-10-19 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beedd8e3-04e6-3b67-b11c-a34be276dfd5 | -3.5189 | -49.93335 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac6bd5e1-ea18-3dd3-87c1-9bbd2a081da3 | -4.57365 | -45.88074 | 2025-10-19 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a42cfbc-df51-3232-8ce0-9b2908ff4257 | -4.14459 | -47.65668 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a085312e-f74e-3aac-b4cc-34e8f4c6aee2 | -3.64023 | -49.96863 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bf529531-84e4-35b2-84d0-70f74539e57d | -2.9094 | -52.72269 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d0212b2-0938-3be2-bf0f-552a1bf3daff | -5.37181 | -42.7965 | 2025-10-19 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f10c4acb-8bfd-3fe6-8756-8d32b87f5aef | -4.77624 | -46.88463 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4980d3d4-cedf-3a43-8ce1-41fe618390b6 | -4.92129 | -45.67496 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20df2ef4-3e1a-3a1d-b3d4-f716e7945343 | -4.44455 | -43.21857 | 2025-10-19 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2936e18-f02d-3aa2-b393-027c7856e440 | -3.54931 | -54.69462 | 2025-10-19 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b00f56b0-7147-3fb7-915f-16bcaaa308cc | -4.1479 | -47.6572 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43192881-e1e2-33a1-9403-f8ae1adb767d | -3.89065 | -52.40314 | 2025-10-19 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac51d513-7abf-3880-a6cc-64564f36162a | -3.82457 | -48.64898 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8290814c-2f1b-3dc1-8fe2-d02882e8e9ae | -2.87489 | -50.73397 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d262d7c-8197-31b4-a6f5-0774ca4b93ce | -5.28106 | -42.54779 | 2025-10-19 04:29:00 | NOAA-20 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 82541b62-15a5-3cc4-a443-78b97a47a088 | -3.11702 | -49.10592 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96e561dd-f943-3056-8dbd-2c91f1bef4be | -3.51189 | -49.93828 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0a9aa52-0d8f-3b61-8752-f7beee15a912 | -4.52403 | -48.84033 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92ffa065-78f2-38fa-91e3-293fd62fedf2 | -3.39567 | -54.06765 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 031f0703-ef6a-3ce8-973d-44eb16babeb7 | -1.10542 | -48.90186 | 2025-10-19 04:29:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bbf7534-f5a7-35c2-8fe7-1f9476765996 | -3.14522 | -50.24329 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b38f29c9-a339-3329-8b52-db3e031c9d15 | -2.79671 | -48.94185 | 2025-10-19 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd61b004-86d7-37b3-bab8-f6b40d366c34 | -0.43182 | -51.96786 | 2025-10-19 04:29:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ad99d2-0409-35bf-8453-953bb5040246 | -2.70045 | -49.86674 | 2025-10-19 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6180a81f-37ca-3ce9-a436-f1bd2e846104 | -2.70196 | -49.54217 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d0661b8-39c6-331e-98de-13caa5d3f706 | -2.91367 | -52.72327 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb788b62-407e-3770-abb1-c6e64ea32903 | -3.65256 | -50.25725 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README38.md)
