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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6856f8f-8967-369c-94b6-3b9a29116033 | -4.81817 | -44.35522 | 2025-06-19 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f9197d-e0bc-3c53-b0e2-e158d7aaf333 | -7.23443 | -43.10446 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4e638c41-bb99-34fb-bce1-69ed2eccd9d1 | -7.53916 | -43.80835 | 2025-06-19 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4419a5d-5be4-33e9-8e14-028fca463bca | -6.68403 | -43.21856 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| deb91459-457f-3de6-ad16-3d3476e6f7bf | -6.68121 | -43.21444 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34d6a23c-8567-3ee6-83c0-80244ef16b0b | -8.12381 | -43.12828 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 79ba8798-754e-3b74-ba93-d66993d29ba5 | -5.13395 | -37.8484 | 2025-06-19 04:17:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 561da8a0-3a00-3078-849d-c3a261052555 | -8.12609 | -43.13574 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 56bdbc12-c8d1-31cb-b253-dcc78767fd14 | -6.6722 | -43.20567 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d20e2aa5-b172-325d-9a1e-d1e4cd7f1c97 | -7.24408 | -43.08709 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6303c83a-ec43-372f-a263-e3fad390b910 | -7.20444 | -43.20856 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e36074a3-2dfe-37a4-9b7e-839881adfba0 | -6.68571 | -43.20774 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 658fcdd8-5085-387c-b4e0-087dcc069123 | -7.14418 | -43.28493 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef55dcb7-3916-329d-b222-8f1fc566f2f3 | -7.54306 | -43.80534 | 2025-06-19 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d8f0076-488f-3347-9d8b-180572de03d7 | -4.59433 | -47.89092 | 2025-06-19 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e451609f-c22e-3425-b82c-9952891156e6 | -7.43982 | -43.04486 | 2025-06-19 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| de044c9f-b4eb-3c22-953c-c7702e424189 | -7.14983 | -43.29322 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1342e0d-cba5-3c6d-93af-4d7c55e566b5 | -7.34941 | -43.87344 | 2025-06-19 04:17:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5fa5ae8-cbb2-3726-8f55-d217fce81be3 | -7.23841 | -43.07868 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 65280318-e90a-3e5d-b3c5-e61888e7b916 | -6.70748 | -43.25571 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff0d06ab-2c97-36a9-8148-3ed0f9c7ba5a | -6.53792 | -47.80963 | 2025-06-19 04:17:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b9307e4-e27c-3001-822c-3d5f7756f44c | -5.29113 | -44.71601 | 2025-06-19 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ebdb390-9955-3808-a2ff-b141ebcfa52b | -6.67502 | -43.2098 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff9c3ab8-df90-3ceb-918b-01f1e6fe87f4 | -7.23671 | -43.08971 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| e5206343-0ec8-3725-a498-09d460eda07a | -6.85752 | -45.55212 | 2025-06-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53a67844-a8d9-3491-85ce-722ee87e744e | -6.67558 | -43.20619 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 99b517f0-2fe0-3f9b-8711-0f1be59a2f36 | -6.68683 | -43.20054 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| be4d1f17-d122-3ee3-bc70-61cbcd60bd79 | -5.84669 | -43.49203 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ade07cc-d1cf-3af1-a9bf-938f3aacac40 | -4.77379 | -47.57042 | 2025-06-19 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0a004196-a94e-3c34-a3c1-8bcaff41e543 | -4.84215 | -43.18568 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 476f0b09-391c-3b75-948a-3656a83b9032 | -5.77325 | -43.46298 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8258cb6d-45bc-395b-ba4d-e2d181b8fdea | -7.24068 | -43.08656 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 4beedfcc-f96d-31b2-9fdd-86dae3afd002 | -8.0742 | -43.10922 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| 2d19727c-6b06-3244-8002-6ce5dee1851c | -7.24125 | -43.08288 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| a4fe71e8-e3ee-36bf-a142-03169ee0cf0a | -4.82148 | -44.35574 | 2025-06-19 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37c730c6-e779-3c6b-aec6-93dfb96a3105 | -4.28301 | -48.18314 | 2025-06-19 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e24d97bd-0ae5-3c21-8442-511e6d3fb186 | -4.8427 | -43.18214 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f67b90b-9c43-35af-af89-7aefd718fe58 | -4.01547 | -47.85315 | 2025-06-19 04:17:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 846221ca-45fd-3338-97c7-50302c3e2295 | -7.41022 | -48.13169 | 2025-06-19 04:17:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddec3132-482a-3631-8a47-484c177348ef | -7.26016 | -43.54995 | 2025-06-19 04:17:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1ea2980-2a65-35d2-90d1-38aeabc00c8e | -7.43641 | -43.04431 | 2025-06-19 04:17:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7be92377-9f90-33ab-83da-ceeea731d1f1 | -4.27923 | -48.18252 | 2025-06-19 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e41c7c5-5459-3291-a18c-8eaef358c589 | -6.32138 | -43.7566 | 2025-06-19 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e71f408-5688-3c16-b92a-7b3811bf57cf | -6.66803 | -42.48463 | 2025-06-19 04:17:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bc949c67-6ae7-3d6d-85fd-5f41f1ec2536 | -6.67951 | -43.2031 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bdfd622a-262e-3892-aa72-91c9d72e5b83 | -7.16942 | -43.21064 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e7983c50-7c58-3efd-bd2f-1a33b91df555 | -6.68515 | -43.21135 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6d6f8fa3-8fe2-3915-b2f3-56169b2b2ef2 | -6.68797 | -43.21547 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 942791ab-0ef1-3db7-8b22-ab0c0729de4c | -6.3711 | -43.65638 | 2025-06-19 04:17:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45e9cda1-d61c-3d6d-b68e-96db1bf06322 | -6.69022 | -43.20104 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 200f7510-a4d3-31e2-a4bd-964794856995 | -4.41076 | -47.66051 | 2025-06-19 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0af2a74c-100a-34d5-9563-055401b81114 | -8.07078 | -43.1087 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| 0f57bd60-b425-394d-ae31-385af97cf918 | -7.23217 | -43.07394 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 44ac924e-1a49-3ed0-8748-14ed9453bea1 | -7.24465 | -43.08341 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| ebf05832-e315-3089-a94d-f0e7dbdcfd2f | -8.12665 | -43.13198 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 539e2264-1446-3773-94de-1484deda612e | -6.88063 | -46.35855 | 2025-06-19 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2d5fe15-de87-3d78-987e-e761bb16e160 | -8.12722 | -43.12823 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| be0d130d-189e-3bef-8d62-c82a0540d38c | -6.68965 | -43.20464 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 89738dd9-8199-3928-9f14-dde3586891fa | -6.84307 | -42.80364 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 067b5c58-b076-3a87-8f28-c972731e43d3 | -4.83601 | -43.1811 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ecafcd1c-0a2b-3c25-b22d-4f1f99872c2a | -8.12723 | -43.12878 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c9efd74b-cbd0-3409-8110-fca7fe93080f | -8.12665 | -43.13253 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 34cdc197-e018-37df-90d4-64f6a21955b7 | -5.1225 | -45.02983 | 2025-06-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc97fbd3-799f-3a7d-8a30-bce09538f20b | -4.83546 | -43.18464 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dac5b22e-edb9-3519-bc4f-996823947073 | -7.53971 | -43.80481 | 2025-06-19 04:17:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9e9223b-75b6-3336-8b05-f994c5b12da8 | -7.23954 | -43.09392 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| eec3cc45-fc69-3a74-b279-f95b367953d0 | -4.84549 | -43.1862 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d67b0158-e9e9-360d-ae2f-a70ccce0abcf | -7.21913 | -43.2258 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 44237865-cbbe-3062-ac20-f5ac7d04bc12 | -7.24351 | -43.09077 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bf5d8eae-e3fc-3320-9474-7aa9d2a183bb | -8.07477 | -43.10548 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| fb525c83-7c42-3a71-97bf-1caee1b98916 | -6.67149 | -42.48513 | 2025-06-19 04:17:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 65065d61-a2d7-3839-a2ef-d012b9f4e201 | -4.77742 | -47.571 | 2025-06-19 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ac0a893-a799-3b48-ade2-2c872d39b256 | -7.1499 | -44.06189 | 2025-06-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9afd586-87d5-3ee4-ae39-0b64e7fac480 | -6.67613 | -43.20259 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 410aa022-40c0-39b3-a834-9996803b85b7 | -7.21856 | -43.22944 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 850d7e0c-29ef-3455-8dd9-4d04f9181d6c | -7.23784 | -43.08236 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| eeeaa75e-b0f6-359e-a1b7-9e387510b11e | -7.00754 | -43.68948 | 2025-06-19 04:17:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a052bbc-a897-3ee9-8857-ebec8e8e6ec7 | -6.85309 | -45.5586 | 2025-06-19 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b9f88d48-417d-39a8-91cd-732c0999b258 | -5.13459 | -37.84397 | 2025-06-19 04:17:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5e85bdb-3cf9-3783-943f-3227693d069c | -7.23501 | -43.07815 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 05dcd244-14a7-3087-adcf-5b5fdfa58728 | -4.83936 | -43.18162 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| baf1ff40-8947-3b70-ad70-5aa55d52e731 | -8.06793 | -43.10444 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 339991c3-f1a9-3296-b0fd-1eee048b7114 | -6.70759 | -43.89238 | 2025-06-19 04:17:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ad45749-1ea0-32b6-963c-d250c9776d62 | -7.29559 | -43.04925 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0ed55591-bd82-399b-97c5-0ea1740e7272 | -5.77381 | -43.45945 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5b74a61-b811-366d-b9a2-d71cfbf72689 | -7.16998 | -43.207 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 69048cee-1c4d-3626-ac48-ebc6f1b10464 | -8.12607 | -43.13628 | 2025-06-19 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 70ae95a8-c2be-38e5-8606-dfeff516ab2e | -4.83825 | -43.18869 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a54fd282-9df1-3af1-b253-3c11e12ad5b0 | -6.17775 | -42.48209 | 2025-06-19 04:17:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4698c206-ce6d-33a9-a1fb-b1f1b6002207 | -5.77436 | -43.45591 | 2025-06-19 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 266a04c9-09f5-30f6-b6fe-f88688c7fe73 | -6.53088 | -44.45973 | 2025-06-19 04:17:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e14f85f-b20f-3d52-a16a-d39e30f51338 | -6.28774 | -44.23295 | 2025-06-19 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 70a9e4bb-d0c6-338f-8d90-e3b468a6d0d0 | -4.8388 | -43.18515 | 2025-06-19 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f4bf40f-c7e0-305c-8113-0fca09c5f3dc | -6.29767 | -44.23449 | 2025-06-19 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 270e789b-93d6-34d6-bba5-5560a286ef25 | -6.70466 | -43.25157 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e1fc56b-898b-33f7-817b-7d9904f3e1c6 | -6.97421 | -43.72782 | 2025-06-19 04:17:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b387a153-07aa-39a4-af4f-aa57a6076af5 | -7.15377 | -44.0589 | 2025-06-19 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96cd0327-8818-3de7-b6c3-9f28c6ba4cbc | -7.17393 | -43.20388 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d31f9a6b-ffe3-3a3c-9a8d-10b1bb782cc2 | -6.68401 | -43.19643 | 2025-06-19 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d8f6b9d-e012-3d02-a420-fe94180e8906 | -7.14756 | -43.28546 | 2025-06-19 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README14.md)
