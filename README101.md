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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 961f3210-ed5e-3a8c-9af2-2e66a3ae3b81 | 4.36719 | -60.00042 | 2025-10-17 05:06:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e03ae3c-90e1-331e-8195-7b0b3124ad0c | 1.38736 | -50.85273 | 2025-10-17 05:06:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14527238-f50f-379a-aac4-0beafd62414f | 3.96123 | -59.82169 | 2025-10-17 05:06:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71195b63-09df-3443-9272-04ad73318ab9 | 3.96068 | -59.81811 | 2025-10-17 05:06:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10ba6347-73cf-3e89-903c-f94b088a3dd1 | 4.37886 | -59.77512 | 2025-10-17 05:06:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8280fba-94b2-3724-95e1-04fdb0eb93a4 | 4.37128 | -59.99977 | 2025-10-17 05:06:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d0716ca-60dd-3ee7-a85b-bdab9766a490 | -4.38609 | -43.39643 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 588b9fff-0e26-3d45-a312-89f45079e710 | 1.81219 | -55.73714 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebc09b3f-5c62-3cfa-b64b-be0af188e368 | -3.4072 | -52.88279 | 2025-10-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0892fce9-8a67-309a-aa8b-b5ed1c719e97 | -5.28912 | -47.92606 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 471f46e4-41dd-3c08-98c4-13bbde27b7b7 | -4.25724 | -48.55183 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43677205-ada1-3c99-b6d5-cb372a1dbefb | -3.64967 | -51.75151 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65394e7c-cd3f-3984-a516-adea981cc6e1 | -5.28865 | -47.92934 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d248c6aa-ffdb-3410-9939-d0b211e1a2e7 | 0.87665 | -51.12429 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 778ba91d-2612-3306-9795-a711a45a906a | 1.85837 | -55.66298 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb4b8c8-957d-3b93-9e44-9861bc1f53c7 | -2.86618 | -50.73728 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e286139b-2ea4-39cb-b5b5-2daa7c7e8f8b | 1.8078 | -55.73077 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5377762-a94b-337e-99c7-e2bf593c9031 | -2.8663 | -50.74043 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be547dcb-e011-34ad-9162-0f06f1dbe5b7 | -1.62741 | -47.05349 | 2025-10-17 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91447f2e-6c1a-3020-b856-4b049b266587 | -4.71899 | -46.44669 | 2025-10-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a45798de-fac8-3914-8baa-2b1f11ff6693 | -4.8682 | -45.78575 | 2025-10-17 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c144926-1146-325b-8560-45926c02553c | -7.32665 | -44.16142 | 2025-10-17 05:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b114f768-17de-3660-9f7b-21c165bc9f1b | -5.84586 | -43.87682 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45d2d41c-d8eb-39c2-9da0-119c52a087a5 | 1.8484 | -55.68566 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f59c19c2-c3da-3b56-8a72-979d79c4c174 | 1.73827 | -55.7839 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b2201704-05e2-3a81-8fe6-f956d9db8f41 | -4.40821 | -48.94609 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59e6799c-9ca7-3870-b90c-2559562c89d8 | -5.46291 | -44.64602 | 2025-10-17 05:08:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3943c90c-625c-328b-a787-75903bcb77cf | 1.73496 | -55.78442 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a55d5bd6-9eaf-353b-97b2-0f7b38e98f69 | -4.56203 | -46.622 | 2025-10-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e93473-384d-3179-a8f9-a4fc7ebce42b | -2.86558 | -50.74113 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd35eefd-5cb8-3d0f-8472-4c518d6ce985 | -3.65583 | -51.32943 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b890be80-036f-3a4f-a2df-6b5ed9f54543 | -5.91119 | -44.74993 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f54dc05-b0f3-3cc2-8aa3-a12d0be5cd21 | -2.87527 | -50.73785 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a4a884b-ad16-3760-8b81-b7a135d564d2 | -4.36633 | -48.70882 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4739d13-20dd-3f3a-b401-7199bb262fe7 | -4.8155 | -43.19902 | 2025-10-17 05:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79ccfdf0-b473-33e4-b7fd-3d98d143bd3d | 0.33075 | -51.36105 | 2025-10-17 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cb7e60e-b59c-3617-bc2f-8df232adb711 | -5.8791 | -44.83979 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3cbacdf0-2fa4-3d4a-826b-5f3a419cb410 | 1.01861 | -51.15882 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 601daac6-5293-3baa-a6a7-39899700aa43 | -6.42517 | -44.72523 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6faea22-0567-3f29-b492-b7f9dc8c034b | -6.59193 | -47.07606 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a871484c-92d5-3bfd-b5a7-2da418ba863c | -0.8975 | -47.54253 | 2025-10-17 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb30756e-4eee-3652-8a08-9c4ef357035f | 1.72997 | -55.79577 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42ff9d97-9c81-3186-bec6-ae1404de9d52 | -3.81259 | -51.8639 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0eb71f05-ab10-3e16-8149-f598fe3e9959 | -3.40897 | -52.88041 | 2025-10-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e08a836d-443a-3613-9af3-9580edf8a7a4 | 1.7968 | -55.72543 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4272c118-90e2-3fbb-8326-4eb26ae756b7 | -4.31161 | -48.08353 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bb9ef9e-2457-37a8-9d91-2e8540272da9 | -2.87098 | -50.73405 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1eb75cd-ef65-3385-a7fc-a4c86727ba6f | -1.30193 | -55.74774 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bda02e6-0a27-3c24-877b-83473b9ac42f | 1.2922 | -54.70292 | 2025-10-17 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d12f189-44db-3f05-a72b-83d6bcdaaeb9 | -5.89133 | -43.90332 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 754c9f47-2475-3e32-a273-1ff170540b86 | 1.85285 | -55.67088 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9232e381-98f9-39a4-a895-155dc1cd0714 | -5.85182 | -43.88457 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71219bf4-ae7a-3061-bf25-c1ce2adb5dc8 | -2.92769 | -48.30459 | 2025-10-17 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| feff658c-c3cf-39c8-bd87-a564a9ffb821 | 1.73442 | -55.78097 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a28285f9-4cda-3864-b9ed-59924d248b23 | -5.29294 | -43.55225 | 2025-10-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| db3993a7-1889-382d-8914-1cf6541283eb | -6.5857 | -47.07905 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8935f08-903e-36d1-a361-0a4c54ddc323 | -6.29663 | -45.53596 | 2025-10-17 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 014e9e23-f054-3ff6-95a9-7918bf8f6cb6 | 1.8705 | -55.65404 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 479657b3-1f01-3a24-be9a-0c22eb657c82 | -4.21366 | -48.36037 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8536df52-9cce-3a7a-9ec3-203227ed8e91 | -5.24046 | -50.95364 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4107bb42-e7b1-3cf7-adac-fd4d034ef885 | -4.40606 | -43.4055 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 16fb84ee-ce8e-3a31-80a9-484ec315c016 | -3.52749 | -50.31263 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1771aa9d-4220-3380-94fa-7cb1b4d7c407 | -2.8705 | -50.74108 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a3ce5d7-d5ee-38e2-8cf8-c20245efb51c | -2.8747 | -50.74171 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fbc507b-87c3-3026-8ccd-badd152ff9fd | 1.74987 | -55.77151 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e352d77-2b0c-342c-b997-8e549a180114 | -2.94492 | -47.31116 | 2025-10-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0877d30-6acb-3e75-80a8-0c183888c594 | -3.12888 | -50.21082 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86664a69-c8b2-3000-9ca4-c6146a6c0b0c | 1.79347 | -55.96254 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 567e2fcb-0c9d-3fc8-b467-86ca27547f29 | -1.51452 | -51.6248 | 2025-10-17 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 775e0aa1-13bc-3641-a2d6-1c405db24f2f | -2.96076 | -48.58642 | 2025-10-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62e4db66-d8c2-3262-a544-00d9abe9375d | 1.78315 | -55.8969 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ebca4de-53b3-37b6-831d-7c318bd56768 | -2.68746 | -48.70613 | 2025-10-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d265f402-14b3-3cb8-ad44-e2abfdfcbb3b | 1.82467 | -55.70696 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4e0fb895-c959-34c8-9fb9-617c0f511e4c | -4.40314 | -43.41918 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 21b39026-8ed7-3409-a03b-e04c73e52498 | -2.87338 | -50.72174 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c27adf71-43aa-3cb9-8d7b-92b322a2c926 | -1.73351 | -54.43498 | 2025-10-17 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24e89e9f-5408-37a6-8677-dd6e101d2484 | 1.88426 | -55.65542 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d4646d4-ffb0-3615-a9a3-40c8261b5654 | 1.8451 | -55.68618 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 649d726b-b869-3932-8333-1a2a398f87e6 | 1.792 | -55.88847 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 015daa07-713a-39e1-aa7b-2f3f28060d8a | -1.66516 | -55.14584 | 2025-10-17 05:08:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f851baac-74f8-30e0-a042-b7715e145f93 | -4.73825 | -44.94255 | 2025-10-17 05:08:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2b38a68-2ea3-3b10-8a33-74f8f5842957 | -4.54563 | -59.92551 | 2025-10-17 05:08:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dc86e56-1d15-348a-8f96-c9bae189abde | -3.51339 | -52.48596 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a178fa7-3715-3eac-8661-4127a858393c | -2.68798 | -48.47087 | 2025-10-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 094464c7-f659-38c1-8a2a-10578e8e9a5a | -2.86679 | -50.73342 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4a1fb41-533f-3c5a-aa69-cae12b7eb1ad | -5.39396 | -50.48553 | 2025-10-17 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3ba0e9a-fb6b-3f0c-9752-59618432f1a7 | 1.82521 | -55.71039 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 46554a67-00c3-3a11-aac5-83ff2f52393c | 1.7637 | -55.75173 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b99beb-a36a-32e0-9c49-d24ed7e56dd4 | 1.88382 | -55.60972 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d51ddb7f-eba4-3d4b-bae3-af214061735e | -1.93968 | -56.85263 | 2025-10-17 05:08:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85a16c64-6dd9-334c-884c-64d2140f0763 | -3.26823 | -53.25684 | 2025-10-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bf85370-7bde-3b55-85e1-414ed36049b3 | -2.86745 | -50.7327 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 451fbf02-4526-3c30-803c-f5d7586c24c2 | -3.48937 | -50.08953 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0440d622-70ca-3fd9-b5d5-d3c090c2e6ed | -3.65207 | -53.6552 | 2025-10-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee4db86d-0f1d-3ca2-be84-b6d43494869c | -3.33299 | -53.24534 | 2025-10-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13c60dc2-0a61-3d7a-91aa-69f393fdb51c | -2.87701 | -50.72624 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1dfaf49b-545a-391a-a0b7-7c6ce00b8934 | 0.87278 | -51.12489 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb708316-0d39-3789-a6b8-8e71af44930c | 1.76646 | -55.74777 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 739ab97d-25a4-37f1-a5fd-fd8ce2871043 | -5.25736 | -44.21585 | 2025-10-17 05:08:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 799cb844-7e7d-3b9f-a515-2a5bef76a544 | -2.4463 | -52.25087 | 2025-10-17 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README102.md)
