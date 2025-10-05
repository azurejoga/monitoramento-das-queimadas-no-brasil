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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1fd46fd-2595-3e2d-a80e-4f3ae063801d | -11.81635 | -45.06755 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d50fa7fd-33e7-3910-938e-dcd8c491e5cd | -8.58058 | -46.32523 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 6eeda4f7-0f88-375a-804c-c43110ab9037 | -13.95543 | -43.0728 | 2025-10-05 03:34:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4799a948-acec-3a7b-97b1-e58c037ecddf | -7.61039 | -45.4683 | 2025-10-05 03:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82115f0f-4866-3388-8274-77a44b39ac42 | -9.25117 | -46.778 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 577117ac-1e30-3ccf-a6ea-f3ee1bcc8226 | -9.95596 | -43.77645 | 2025-10-05 03:34:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8eba8e66-fccf-309a-b95b-03cc2d5e190f | -7.11543 | -44.1776 | 2025-10-05 03:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6405ff95-3eb3-34ce-aa2c-333bb2f990e4 | -9.05847 | -47.02448 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2e98ff2-2acb-3eb9-a232-3983dc2a6fa3 | -11.76091 | -44.74269 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| de1aafa2-267c-3401-844c-16ce38ed0072 | -13.12328 | -43.84278 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 25ff33a4-e04d-3540-9e1a-4b4f1319aa50 | -13.33709 | -47.1909 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bf2608cf-acef-37c6-8341-fb2a7db2d6c1 | -13.68051 | -43.18685 | 2025-10-05 03:34:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 490f97bb-c4a2-38f6-8598-6eaf28a9579d | -11.79895 | -46.8434 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4215ca8e-188a-32c2-96b4-9a37cd263735 | -18.32868 | -45.88268 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 053b5c92-d890-3477-9247-0f9f498816dd | -15.21034 | -46.38714 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7e05d6e-404a-318f-9695-b2a50f5478f1 | -19.94037 | -44.39037 | 2025-10-05 03:36:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 303979ab-001c-3e3d-b67c-4e19d35156d5 | -15.91165 | -48.82565 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 2bcb7f2f-eb49-3d2c-9c2b-a929dd527614 | -14.92833 | -46.84758 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18f4826c-aeea-3315-b12c-babd3d83eb81 | -15.96463 | -43.32637 | 2025-10-05 03:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31ba9307-da17-355d-8925-7c3d3151aa60 | -15.50422 | -46.85691 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19df5cea-a410-3fca-8cf0-f447ae837e27 | -13.9168 | -48.1987 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39e82562-e991-3971-8b2b-90989289b020 | -17.02277 | -43.44912 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 697d48dc-7217-360c-8fa3-8221cf253435 | -18.33373 | -45.88253 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5c172b5d-db0f-3e80-ab18-d503c09f02c7 | -14.67082 | -48.35431 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c7db3760-01b9-3a80-a26a-c5747b6b8bb9 | -15.31963 | -46.37088 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2efd14fe-35d2-35de-858b-a8b1adb7adf4 | -13.90949 | -48.19785 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a4e2783-4f3a-37b5-86a4-9bf1a5838d1a | -14.68301 | -48.26796 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55100ef3-4f91-3950-a67f-8b03f0544a0a | -15.17197 | -43.63801 | 2025-10-05 03:36:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0cacd8f8-35d7-3326-b8cf-e6397e35b53c | -15.3587 | -47.9757 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6431719a-a4b4-3875-b84f-88d56c23fa27 | -15.51199 | -46.85025 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d491aec2-6d63-3356-9b93-fb862ad2a310 | -15.209 | -46.39326 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd971e0d-e002-326c-bd9e-adcc12b3fd3d | -15.39626 | -47.96272 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30e9aca2-7093-359e-91f6-1ee76c2f1ab0 | -14.31832 | -47.70326 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 91ced1c1-07ca-3014-92c0-58a284042ec8 | -17.01768 | -43.44794 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5957bedb-cf29-3cbf-a6d5-73556980dd48 | -15.3164 | -47.32294 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1ce022e-c70a-3d76-a185-1e71b294c2fa | -14.88673 | -48.2691 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ca530e71-f8ca-3f52-adc8-88c1f7eb9cea | -15.54564 | -46.8207 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f5fe75d-a830-38e9-9feb-1fd1dd9165a2 | -15.35584 | -47.98114 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 89d3f7d8-51d0-3ced-9b0c-5e3aa583b901 | -14.68364 | -48.29791 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 58f6bc40-0de4-386b-a4df-61f4ebc62fdb | -14.67936 | -48.34963 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6b3a77d2-59a6-37f4-ad23-7c639e22d8c6 | -16.35447 | -47.05894 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa84c270-9349-32d0-bfe0-0cc6bfeb9212 | -15.82413 | -42.61867 | 2025-10-05 03:36:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d59d81ed-e767-3270-8c5c-1d2056dea9e3 | -15.38116 | -47.93976 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0c94cccf-6b33-3e06-93ea-90ccd39f5bd5 | -14.94911 | -46.84629 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29a515d5-c803-3843-88ae-94ff44c03cc3 | -15.39214 | -47.95537 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c574a99-6462-3fe9-88ba-3d6b0c266b71 | -15.17268 | -43.63449 | 2025-10-05 03:36:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91d2a8d0-1394-396a-b80d-7f5c22b09932 | -15.75618 | -46.26434 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46beb0b6-e7c9-3281-bce6-4c5fc3fd5e41 | -14.94157 | -46.84953 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15720e19-3e16-3c39-b14c-d89549d1e477 | -14.67156 | -48.3085 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ef9c440-3c12-34c8-9a37-e74b9dc8e30e | -15.13935 | -45.75081 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d078eadf-9e39-339c-9d69-a3ac2ecd5e6b | -15.7622 | -46.26658 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14bb74ed-767d-3294-885d-8f6dc64caac9 | -19.94801 | -44.39827 | 2025-10-05 03:36:00 | NPP-375D | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4269206c-7ff9-3191-bb37-b7352870e680 | -14.685 | -48.349 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7abaeba3-9ded-350a-9a64-af23158ff6ea | -15.35717 | -47.98259 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 788ad8ba-56b7-3d3a-be94-d61debb562fe | -15.3078 | -47.33043 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e36e8fc9-dbb3-36b2-bc1b-14f9ae88dadb | -15.32723 | -46.37425 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe289b8c-4bc1-3ba3-8b89-4234fc8f508d | -14.33212 | -47.70646 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 107e6bcb-ae35-3f2d-b376-8809b887a97a | -15.91629 | -48.828 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d57e9ff4-f802-3dcc-92d9-896b0fb6e07d | -14.41343 | -46.1829 | 2025-10-05 03:36:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0add030c-f758-33e8-a130-dea632ae5c29 | -15.29819 | -47.95506 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3bc19fd-4a1b-35c0-9b4f-4d06a0586e43 | -16.26806 | -47.11354 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66d0a16e-1cbe-3196-9cb0-d9313d8f6527 | -16.59839 | -49.3871 | 2025-10-05 03:36:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab0d3850-4cd9-3ec4-971c-81251ffcf7f7 | -15.72173 | -46.25809 | 2025-10-05 03:36:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b11f92d2-6daf-30f3-9b56-573177bb326d | -15.29852 | -46.32465 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f60acd8-bda1-346c-8673-1b4e34277c25 | -14.67625 | -48.36334 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 42238829-f829-3b73-9545-2d463aa3f965 | -14.32512 | -47.67238 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 56bdc5d4-1743-30d0-bc17-da05890f33dd | -13.91171 | -48.1987 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a7625f1f-d0fa-337a-93d1-31c8b693b598 | -15.20629 | -46.39704 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7be6bad5-abb3-35c9-86cb-994424b57567 | -17.02331 | -43.44649 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00945c4d-e618-3417-8e5c-942c8449ea2e | -15.51312 | -46.84522 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68a0775e-4a68-34de-9b21-baa98f9ae6fd | -18.33285 | -45.88649 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| e56505da-3b69-3e82-ac55-fd56426b6152 | -14.0073 | -48.21564 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c77a0cf-0ed8-380f-85ad-325be7657fe9 | -17.20244 | -44.44622 | 2025-10-05 03:36:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78b77efd-0d9f-3e01-b4fe-93268d72b8c0 | -15.1228 | -45.74065 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ef7c483-1fd7-3d9f-9ee8-47bf1e0698a4 | -14.32354 | -47.67957 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9956562d-f5b5-3dd9-ae2e-e71e1b96c46c | -18.32785 | -45.88655 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6e526593-eb78-38d8-bc71-8389aa3802e5 | -14.92133 | -46.84836 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7db7b4ea-92e1-3cc7-b7da-09fc5a3c4b62 | -16.60013 | -49.3798 | 2025-10-05 03:36:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5b4e4ad-77ff-3ecb-bfaf-c5c56400420e | -15.52763 | -46.87395 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c010c3fc-7bdd-31d8-a1d6-f2ecadea1fd3 | -15.73236 | -46.26924 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09b3ef56-1f22-373e-a08a-089469f09d30 | -17.01543 | -43.45884 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbf83c0b-2403-32c6-bb78-365c01a94698 | -14.69553 | -48.34423 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54eba3c2-1934-3fe2-9bf1-4ad78394ddf2 | -14.95313 | -46.8593 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b93990f7-fe99-31b4-a5e5-f67f61e29da6 | -17.97493 | -45.00262 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6c8243b-7c01-3f07-9333-c88270427a27 | -15.52612 | -46.87811 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75e9a11e-a5b6-3da8-9ebc-f13e8a7ece89 | -15.87186 | -46.25986 | 2025-10-05 03:36:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0c06fb4-8eea-388f-8e76-38df172b1170 | -14.66441 | -48.28415 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14381684-1eb0-3441-9c34-525765cbeb66 | -19.94659 | -44.63891 | 2025-10-05 03:36:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| d3cc4240-57e0-3bdc-b826-fb6c049dfb81 | -15.51953 | -46.84683 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6df6a45-d80f-393b-99fd-fb0f21e0dc37 | -15.35746 | -47.97407 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3e9d76db-fc0e-3316-9ad8-2a18e974a701 | -14.68639 | -48.35161 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 802b4ef2-e398-363d-adbc-e5650d45a34a | -14.6846 | -48.3595 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cb626efa-650e-37ce-85e0-7b7c9fdfc5c4 | -16.26271 | -47.1071 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5717b65c-dc7a-35dc-98cd-5843cae40b38 | -14.29798 | -45.86728 | 2025-10-05 03:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c30c5834-54d5-3b84-a6ec-9f6eae3b8dd4 | -19.95014 | -44.64786 | 2025-10-05 03:36:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5125eba9-d6c8-32bc-bf0f-20cc55d05403 | -14.68874 | -45.17829 | 2025-10-05 03:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 82e7428e-a667-3f09-8b73-bf054c303ec0 | -19.94505 | -44.64617 | 2025-10-05 03:36:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 569e67c7-6ae8-3f98-9ce8-52e7de4d9d89 | -15.54348 | -46.8317 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f584d3ab-aee2-3252-bb93-385fb4ea47e2 | -15.51212 | -46.85169 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fadd52c-49e5-3e6a-8319-1d087e4f8059 | -15.91002 | -48.83258 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |


[Clique aqui para ver as próximas entradas](README34.md)
