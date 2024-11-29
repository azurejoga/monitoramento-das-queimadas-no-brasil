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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fab5577-cedd-3e81-8c44-203fa15c1059 | -3.26675 | -50.10013 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| facd6604-bd1e-3f87-9401-ca49330c7a69 | -4.09771 | -53.9817 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b2f02e-f90f-33fa-ad13-1676a3535e13 | -1.13517 | -54.21763 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4730c5bb-5cfe-37b9-a730-cdc848461b0f | -1.35629 | -54.63342 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df0eb3c-1ec5-3c36-bacc-c7912870d201 | -3.22237 | -53.42184 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a08e020-715f-3825-868a-68c466bb3cca | -3.94876 | -46.91994 | 2024-11-29 04:57:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02017506-ec32-337e-9f9f-4e6fd021eefc | -2.65428 | -48.78494 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e6a60f5d-865c-39a5-a54e-4df7124148e5 | -1.33112 | -54.61858 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a475cc-2094-3838-ba65-9886530d1b10 | -1.11823 | -53.21529 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c539da2-3a80-36ea-a2d5-0d5694d226ec | -3.86093 | -50.15181 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d767cf6-606b-315d-95d9-d74bb2d42e9e | -2.75733 | -54.02406 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaa3dd50-92a9-35a9-9026-d46ddf06593c | -1.95281 | -53.33921 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e1dde9cb-8903-3b4b-9cd8-bfbd04fbe46c | -3.37343 | -50.1799 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5a16b135-e3a7-35ae-a37c-1863daf882ce | -3.70936 | -47.13741 | 2024-11-29 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4822f6d6-8219-32eb-8ea1-9a6d8351638d | -3.09524 | -53.25361 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ace117e-18ec-3504-b36d-148b82eb8a4b | -2.60008 | -54.2685 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45a94865-79cd-30d9-bc75-64700e2b5e5b | -3.24849 | -50.77661 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa255b92-ff13-3939-9c5d-00b1bc09be56 | -1.31844 | -51.75427 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bb29311-1251-3eeb-9c3d-997b7fa808ac | -1.49989 | -51.98735 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0056f543-de3f-3c92-96da-db3493788390 | -3.96776 | -50.18856 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e1e4fc2-d168-3458-9987-a261510303f2 | -3.02731 | -54.01731 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f4450cb4-0b82-38f5-8fcf-9d368dbd826c | -2.62574 | -54.27959 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb0d2cad-b7ab-3a53-990c-481655dc21f4 | -2.64178 | -54.28561 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfcd29a5-6adf-3b74-83c0-4de608db9494 | -1.44151 | -52.58202 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96458b0b-1e42-3540-a2d9-4b78caaef644 | -2.90079 | -49.79068 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1df2c42-49ac-3044-8fe1-819e1fb8c7be | -3.49354 | -53.81991 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 695eda45-5dd6-30d5-8951-133483eed368 | -5.73676 | -46.6283 | 2024-11-29 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 17d2d0a5-cc58-3b73-a503-9fefee5e95f6 | -0.95164 | -52.99582 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f03306d4-e5b0-326f-9b51-256a1261385a | -1.07275 | -53.37675 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8ac19c8-50e7-3aee-af9f-d3cc69878e1f | -4.43177 | -46.57677 | 2024-11-29 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 24445266-83f7-3b9d-9cbe-2410fef1a6df | -3.06791 | -54.4097 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c908bc15-0075-3c1a-84ec-05051abb800c | -3.17052 | -53.64605 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20301820-ec0d-3bed-843f-4e209ca0d37d | -3.04636 | -54.41704 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 307c41c9-145f-343c-a333-030fa2aba7ae | -2.52548 | -54.1365 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c500830e-5128-385d-a6e9-b7b0568033a5 | -2.56214 | -54.33725 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffcd0906-0b7a-3e3d-ba94-016723c2dc7c | -1.68052 | -55.1682 | 2024-11-29 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70ba46f7-06ae-3060-b0d3-a2b1131b1ad4 | -1.31776 | -51.66919 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94d36fc6-ceba-3f8e-a8b5-340c0d2f59c2 | -1.36216 | -55.18322 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5683384d-4250-33cb-a20a-040fb7624619 | -1.12483 | -53.21631 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b04ef570-3265-3358-b5fc-fe9305042277 | -2.90052 | -51.36825 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1641bb2f-65ea-338c-ae16-93c4da111b40 | -1.87056 | -53.95267 | 2024-11-29 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fa6a17e-904f-3eb4-b3a3-abff9f086ca5 | -2.79568 | -54.2145 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 534363d5-bf94-37d0-919f-cf5bd91811fc | -1.39633 | -54.94183 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91cf6bb2-2be7-334a-91b4-97a942d9b2f1 | -3.32999 | -50.2234 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3e82f8f-05d9-3eba-b922-1754edaee7de | -2.85004 | -53.03847 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2059bfff-f370-3a1c-b8ac-a7f8c985e325 | -3.59714 | -50.36066 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcd5a8b5-ddc5-3ff3-b39a-e2099d695cf2 | -2.62082 | -54.20087 | 2024-11-29 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5f6ad03-835d-3fc3-9c1d-843ec88fc77e | -2.27176 | -50.45861 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7def5c93-13fe-3060-9219-49e87b3762f0 | -3.01565 | -47.79702 | 2024-11-29 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac76f94d-3c48-3664-a4c2-95fb76078f63 | -2.58999 | -54.22438 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ef31be7-2671-3821-bfb4-7148759708aa | -1.08863 | -53.36165 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 705fd3a1-73a1-3328-b6dc-849dc6edb28f | -1.45077 | -52.54446 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5e34114-e169-356a-8fb6-a3a31330d939 | -1.30433 | -51.73366 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59da2626-7e19-36aa-bde7-88f933eed049 | -3.65737 | -50.70455 | 2024-11-29 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89f5610b-7794-3e5d-939d-922e1dc3d693 | -0.00203 | -51.1678 | 2024-11-29 04:57:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d86253a-fa44-3563-8c7c-8b0638478722 | -2.96927 | -53.93083 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0419e76b-43d1-3a6c-87a3-a4d8267f38f5 | -2.66567 | -48.79022 | 2024-11-29 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| ce07767b-8c05-35cb-9038-21ee12602442 | -3.30481 | -50.75957 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 589c16f7-6e94-370f-babd-859afdc43ebc | -0.99162 | -51.71179 | 2024-11-29 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60d36f82-cad5-30a0-8ce9-901726515731 | -3.73331 | -54.22393 | 2024-11-29 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1618824a-b3d4-3324-8ae8-c3b1460b12e0 | -1.28102 | -52.69514 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00826b46-89a9-312d-91f3-df70885f3d04 | -1.6523 | -52.73497 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88f9ea92-900c-3ecd-9764-a875545fd740 | -3.50505 | -53.81114 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94ecd7a9-9247-32f5-b4db-190809da3485 | 1.20602 | -55.96253 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ffac07c-582c-3d5c-9c8a-f55cd0b2a95b | -2.91585 | -53.07335 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 123f45d8-7241-335b-ae6f-b6c4c5466175 | -1.72699 | -52.47326 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e6207ff-f262-3bb0-b7b2-3b8209d49c85 | -2.62078 | -51.75074 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f4d1df2-b769-3236-aa32-90df7c06f91b | -2.95973 | -53.88361 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4484671-5334-3e73-a70b-c2c3ab60f3eb | 1.21853 | -55.94784 | 2024-11-29 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80c9ca3f-940a-3023-9155-d7a16550ace7 | -1.40614 | -53.3974 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c0cee2d-38b1-32c9-af46-b0c25b8d451d | -1.34719 | -51.98175 | 2024-11-29 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c8cf21d-cf39-3210-9180-71558163f658 | -3.28624 | -50.62746 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4d99007b-0b39-3042-8377-a32dd064de43 | -2.38226 | -53.65921 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| add85ba2-47b7-323b-929e-15f2d4d6d7a7 | -2.64853 | -54.08847 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 13a6a30c-c3c3-3503-9227-1d44c85fd28b | -2.01362 | -51.18716 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 29190125-63de-3153-bdd6-b7ecb2db0710 | -1.65778 | -52.72165 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e1614e7-42ad-3fee-b1b9-85563b4c95e3 | -1.60951 | -52.28995 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 849cfc28-2474-3013-9264-7f3cebad7c3b | -1.58724 | -52.27933 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc7a8ccf-972f-36de-8856-39ad1c705324 | -3.0734 | -50.94823 | 2024-11-29 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c50eade9-867e-38e8-8849-5cafa6be9e09 | -3.33689 | -53.21029 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 600f4b36-030c-331c-b930-0ef4cdb69a23 | -3.86444 | -52.39611 | 2024-11-29 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1217d9a3-dbcd-3313-9174-a65be45ba728 | -1.25986 | -51.63108 | 2024-11-29 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed48b42c-8103-3aec-a9b3-cecb2fbca91e | 0.98833 | -50.26739 | 2024-11-29 04:57:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43a77eab-6393-3767-bb60-259421a9d02d | -1.34994 | -55.01642 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 225433ca-fc60-3153-b521-03619ce2e503 | -1.67484 | -52.52534 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff091add-c428-3db5-9d73-da7696cad9d8 | -2.9803 | -53.29232 | 2024-11-29 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| aae2348e-69bd-3ce7-856c-884470c2f641 | -2.45095 | -52.97997 | 2024-11-29 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc75917f-1992-3c72-ac0e-ab20bed7fb1e | -3.28566 | -53.6921 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4fe15d0-11e0-3988-886a-ccce5ea46419 | -3.08432 | -54.56542 | 2024-11-29 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55057917-e78a-3ff3-8e1c-9e5b8ad364eb | -2.81161 | -54.02616 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fb8ee0d-a116-3aa6-9cc5-a6d0332e240c | -2.97294 | -53.88564 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe7fe762-896b-3a0e-acbe-98626d08541a | -0.6103 | -51.71969 | 2024-11-29 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d296081f-4224-3ece-ab10-9522a2d52ba9 | -3.2415 | -53.9315 | 2024-11-29 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67a91be8-c24a-37b2-b69d-947ff6ebc200 | -1.89039 | -54.5438 | 2024-11-29 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 190ed9ed-d80e-30f8-818d-bdb85c5a4854 | -1.3958 | -53.55032 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6817f0ce-4563-36ba-bcdf-59ff630af550 | -2.16332 | -53.27686 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecb6b94f-6272-3d6c-8dc3-4c4383c7eb93 | -4.36516 | -47.25121 | 2024-11-29 04:57:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b52f7129-af55-34c3-92b7-672c048e1898 | -2.53894 | -54.05022 | 2024-11-29 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a428a52b-8347-30a1-b430-9044e964f0eb | -4.67174 | -42.38607 | 2024-11-29 04:57:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| bc4fa400-c783-3043-b48b-784cbeac969d | -3.40925 | -49.52726 | 2024-11-29 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README49.md)
