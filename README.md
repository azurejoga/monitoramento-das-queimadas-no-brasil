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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d821a82-3246-35c0-aa64-7857c5587664 | -10.6 | -45.1158 | 2025-02-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 6d8d33ee-d500-3d4a-969b-fd3799333bfe | -10.6191 | -45.1132 | 2025-02-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 24b12c5f-777c-3f6d-8228-4d0667807389 | -10.6004 | -45.0928 | 2025-02-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 3e41f762-12d1-3cca-ac25-44edf67c1791 | -10.0042 | -36.4623 | 2025-02-15 00:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 137.4 |
| f3890ea0-448f-3e1f-af3f-1e7158a35299 | -9.9849 | -36.4657 | 2025-02-15 00:00:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.4 |
| f14866d0-5e34-3d72-8cd2-b89b27195594 | -10.6195 | -45.0902 | 2025-02-15 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d77f5440-c5b6-376d-9509-98452daa0463 | -10.0 | -36.47 | 2025-02-15 00:00:00 | MSG-03 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 390b23a8-7548-3f35-9165-23e2efa1ced1 | -19.82818 | -40.1004 | 2025-02-15 00:07:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 6e2df1a5-3dc2-3046-913c-57c672bba6e4 | -19.65218 | -43.35207 | 2025-02-15 00:07:00 | TERRA_M-M | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 2b8aa971-aa33-37d3-83fa-138877aff2e4 | -19.82294 | -40.10682 | 2025-02-15 00:07:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 342fcae7-b254-3c6d-9917-5844e062919c | -14.17964 | -44.37376 | 2025-02-15 00:09:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bb6c816d-c211-3f54-8b46-1ccde914e42d | -11.69032 | -43.91371 | 2025-02-15 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 08cb22ab-cffa-3781-a555-2c6306a1ce55 | -9.99584 | -36.45296 | 2025-02-15 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 263f2672-e584-39d8-936b-0ab8de668c19 | -11.69253 | -43.93257 | 2025-02-15 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 05aef58b-1ab1-3fb0-ad3e-d60a315ed05d | -10.5294 | -44.68148 | 2025-02-15 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d79c80bb-01f8-3c63-86bb-9e85a27a243f | -8.8797 | -38.14082 | 2025-02-15 00:09:00 | TERRA_M-M | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1d392aae-9f97-30dc-85c9-cf0f8eb789a4 | -11.68827 | -43.91964 | 2025-02-15 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 458448b9-7a0b-32ec-836a-3f38a7758fb6 | -9.99861 | -36.47215 | 2025-02-15 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 2dae886e-813e-356d-ba21-3e7eb5062ed2 | -10.67162 | -37.11667 | 2025-02-15 00:09:00 | TERRA_M-M | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 1ddd94e8-4f68-3675-998e-97b0767af7f8 | -11.75268 | -38.52289 | 2025-02-15 00:09:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 17a54e03-73be-3ac1-a508-189339d9ba89 | -10.6159 | -45.10247 | 2025-02-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 002e50a6-50aa-389a-aeee-33c2cde40fcf | -14.17474 | -44.36768 | 2025-02-15 00:09:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| cf1a52f1-84ac-32d9-8bc2-18311eceb00f | -9.24588 | -35.73638 | 2025-02-15 00:09:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 84ac1449-1c37-36c1-a38f-366548757686 | -10.30062 | -36.77559 | 2025-02-15 00:09:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 8658a8cf-bbae-3132-b6eb-ca06e11fa0cc | -12.84833 | -38.25467 | 2025-02-15 00:09:00 | TERRA_M-M | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 3d531422-fa0b-3d85-a561-6f55adb57380 | -7.47542 | -35.12754 | 2025-02-15 00:09:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 4518cd95-b508-39c1-a5da-e1f62f0ee596 | -15.02956 | -43.38029 | 2025-02-15 00:09:00 | TERRA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 14.4 |
| c7ce3928-338c-30a5-887b-86abe8ff9739 | -6.12799 | -35.2231 | 2025-02-15 00:09:00 | TERRA_M-M | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 28.3 |
| 134da21c-29ec-3509-bfaf-b93ed7d27ea2 | -10.62132 | -45.10812 | 2025-02-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6895ba02-a5da-34e7-939c-b069b22202dc | -12.26053 | -43.42974 | 2025-02-15 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d06f3fd9-92e0-3b18-a7ee-adbc3fbac44e | -11.69062 | -43.93847 | 2025-02-15 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eb9fcade-eb42-3034-b0b5-5cc29eb8a803 | -10.60782 | -45.10975 | 2025-02-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 143.6 |
| a710c507-f41b-37d4-9731-1c52edbc797a | -12.26796 | -43.43518 | 2025-02-15 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f208559a-7ed0-3c8c-89de-67417b14fa81 | -10.00637 | -36.46119 | 2025-02-15 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 124.3 |
| e6ad42ca-4ccb-38bb-909d-ddd8c499c05f | -10.29928 | -36.76631 | 2025-02-15 00:09:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 44a761b6-ed48-3271-b6a2-3e6dcb7c1b7b | -10.61845 | -45.12481 | 2025-02-15 00:09:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| dfdbe99a-6189-3ada-b971-eaae1f508478 | -9.09894 | -43.00156 | 2025-02-15 00:09:00 | TERRA_M-M | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c176049b-7700-338c-8cc5-2f0ee39088b2 | -9.99723 | -36.46259 | 2025-02-15 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 491.7 |
| 29034f6f-e716-31d1-8d8e-5219eaf676ec | -10.60513 | -45.08752 | 2025-02-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| de15e8ef-d23a-3b41-af31-0eac50fb9f2e | -10.00776 | -36.47081 | 2025-02-15 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| a6872841-f0cf-323a-8368-1f3dd395960e | -10.2916 | -36.77697 | 2025-02-15 00:09:00 | TERRA_M-M | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 36.5 |
| 04bd23c5-bda9-3aaa-a652-52b8d6c00e94 | -9.24433 | -35.72584 | 2025-02-15 00:09:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 951b7ca9-9e6f-3208-8aa4-1d4416de1a77 | -10.6191 | -45.1132 | 2025-02-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.2 |
| dc10aedf-f870-32e7-a208-4f6d6477c9c7 | -10.6 | -45.1158 | 2025-02-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 25036d2d-6a02-34d0-96aa-d48e226c3798 | -10.6195 | -45.0902 | 2025-02-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d8dc5ea9-f36a-3a2a-823a-cb5b8ce2928f | -10.6004 | -45.0928 | 2025-02-15 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 72684fdc-6ad7-3910-9aad-c12752fccd61 | -12.2638 | -43.431099 | 2025-02-15 00:12:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aa94d97e-9c57-3621-b2bb-61b3219f8a49 | -10.6459 | -44.487099 | 2025-02-15 00:12:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b6a5cbff-23f4-3362-ab74-ca49105ee431 | -11.6916 | -43.911201 | 2025-02-15 00:12:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dba2679-4539-307d-a3b7-49b292bb76fc | -10.5314 | -44.666 | 2025-02-15 00:12:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bfd8e85d-5d71-3cff-ad7f-85941decf748 | -10.5329 | -44.672901 | 2025-02-15 00:12:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac49ec1-9f32-3589-9f7c-67fb226638ab | -10.5506 | -45.215599 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cec7e639-abfe-3f96-9fa2-36ec833ec830 | -10.6189 | -45.105301 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b665029-64dd-3616-9c28-10de55b7758f | -14.4756 | -45.823898 | 2025-02-15 00:12:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94501bff-d76b-314b-be65-c4c16f3c911a | -10.606 | -45.093601 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5e42a88-c15e-3675-9372-d5409c16a7dc | -11.6947 | -43.925201 | 2025-02-15 00:12:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd02e0f-3c3a-31ae-824e-ffcf35cdb95b | -14.4854 | -45.821701 | 2025-02-15 00:12:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac43c152-4799-3fd9-9095-76ac794b4b89 | -13.4862 | -44.013199 | 2025-02-15 00:12:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1909b6e-494f-3ed3-84ff-c309d7139a48 | -11.6931 | -43.918201 | 2025-02-15 00:12:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fe495d5-b9a5-3be1-8dd7-523a5ce56911 | -16.692699 | -43.0051 | 2025-02-15 00:12:00 | METOP-B | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b39836f7-abf5-3b6d-b2f1-408c1a981853 | -10.6091 | -45.107498 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 873a47d9-b7e5-3305-852a-57ba78ab1890 | -10.6075 | -45.100498 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b651b735-8512-31e8-adba-80e6c60d7274 | -14.1811 | -44.363602 | 2025-02-15 00:12:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 007cab61-e4f6-3aa8-a7f8-914e71e0a98c | -15.4666 | -42.135101 | 2025-02-15 00:12:00 | METOP-B | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9021b72f-ab2b-36e7-8e48-ba3529aab716 | -14.1795 | -44.356499 | 2025-02-15 00:12:00 | METOP-B | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 91279b7b-1231-37e6-9375-a0fcd1ee5250 | -10.282 | -36.771099 | 2025-02-15 00:12:00 | METOP-B | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6897e90-6f77-35d7-923a-756e228616f1 | -9.1019 | -42.997398 | 2025-02-15 00:12:00 | METOP-B | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4757f8e1-100b-3af7-a491-daea17d032ef | -21.1262 | -49.165001 | 2025-02-15 00:12:00 | METOP-B | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a51672c-9b30-3edd-8b47-f585251bb131 | -19.657101 | -43.341999 | 2025-02-15 00:12:00 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0dd47c65-837b-3104-b2a7-b9085718a34d | -15.0334 | -43.3731 | 2025-02-15 00:12:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e34d498b-ec23-3fa4-8dab-39cfc630f157 | -15.4683 | -42.142502 | 2025-02-15 00:12:00 | METOP-B | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f157c50e-f24d-3c60-ae47-2d96d3064fd2 | -11.69 | -43.904202 | 2025-02-15 00:12:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 076ed4b0-b160-32d9-90b2-aa2f396141cd | -12.291 | -40.122601 | 2025-02-15 00:12:00 | METOP-B | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| df81d790-f605-3d04-930d-b525a96e2454 | -19.8237 | -40.102402 | 2025-02-15 00:12:00 | METOP-B | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24ddadd0-9244-367d-a2e4-fa845ff35cb6 | -14.4838 | -45.814098 | 2025-02-15 00:12:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9dad21ea-572b-3667-a22d-8ffea4954c62 | -14.474 | -45.816299 | 2025-02-15 00:12:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7ffd38fc-9e6d-39bd-adbc-991fa6b17e39 | -10.5491 | -45.208698 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 595fdb30-bcad-34a7-88d6-e81520d67d47 | -10.6173 | -45.098301 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 11f63888-4f15-3477-8b87-72ac4b1d83f6 | -19.821899 | -40.094398 | 2025-02-15 00:12:00 | METOP-B | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 263b0c5d-469d-35df-a309-0255351b8bb7 | -10.5195 | -44.843498 | 2025-02-15 00:12:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aeb0585a-e8a3-3c3a-ba0e-e06789442d34 | -10.6158 | -45.0914 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd368b14-b64c-36c9-8299-cee9f35dc9c3 | -12.2622 | -43.424 | 2025-02-15 00:12:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9711fcf8-8d5a-30d9-83f5-2b5c48dc7ecc | -15.0318 | -43.366001 | 2025-02-15 00:12:00 | METOP-B | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 025940ff-cd9a-31ac-8e46-b210d677e791 | -8.1345 | -43.141899 | 2025-02-15 00:12:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1fd3a6bc-ed3a-3736-ab90-ec6a8afe517f | -12.2888 | -40.113098 | 2025-02-15 00:12:00 | METOP-B | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 81441e89-65fa-3c56-9c54-4a5c7518456d | -8.1328 | -43.134399 | 2025-02-15 00:12:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69e8ded8-46e3-3273-bde5-6adeaf0bcb94 | -20.782301 | -41.4151 | 2025-02-15 00:12:00 | METOP-B | JERÔNIMO MONTEIRO | ESPÍRITO SANTO | Brasil | 3203106 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 72c11bfb-74f9-3daf-94c9-74cbb65e705d | -10.5522 | -45.222599 | 2025-02-15 00:12:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 92f21ca4-e7ca-3896-b382-2421f062f97e | -19.658701 | -43.3494 | 2025-02-15 00:12:00 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| efca5d45-f35d-36e7-8c1b-10a129528858 | -10.2861 | -36.787601 | 2025-02-15 00:12:00 | METOP-B | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbb7b2e9-260e-39ee-ab7b-38557a0599fd | -10.6191 | -45.1132 | 2025-02-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 1632a37f-cd03-3176-b161-e508c1935fcb | -10.6 | -45.1158 | 2025-02-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| fb35a4d4-7482-3b3c-a422-8b777889d5a5 | -10.6004 | -45.0928 | 2025-02-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| d74017ff-ea39-3cfc-a84b-787acc8fde80 | -10.6195 | -45.0902 | 2025-02-15 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ece5f1b2-520b-376c-b5c9-4afebfbe758e | -10.6195 | -45.0902 | 2025-02-15 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 91ae1b94-cd00-34a3-8ff8-64b322c7978d | -10.6191 | -45.1132 | 2025-02-15 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 150adfb6-3b77-32fa-aa66-1fd4355de711 | -6.8847 | -35.1216 | 2025-02-15 00:30:00 | GOES-16 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 69.7 |
| 994719fd-acbb-3ea4-bdc7-ce0b88752a05 | -10.6191 | -45.1132 | 2025-02-15 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 5b772795-af2e-39ac-8d28-6ec02ec6d231 | -10.6004 | -45.0928 | 2025-02-15 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1f4b72b2-827b-31d1-8a30-0a0546fc3356 | -10.6195 | -45.0902 | 2025-02-15 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |


[Clique aqui para ver as próximas entradas](README2.md)
