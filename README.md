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
| 0b898d34-f6d4-37ff-af23-3214860b3173 | -13.40479 | -43.02461 | 2025-02-25 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 28.9 |
| 37e67a7f-59bd-3d16-8c6e-99449d4d98f1 | -12.99961 | -45.01011 | 2025-02-25 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 70eb31be-2bd4-3e93-8e4e-e5f43343fef5 | -13.04587 | -40.34007 | 2025-02-25 00:11:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| dd8ed51b-6843-3939-bd5f-03affca927c4 | -13.40652 | -43.03887 | 2025-02-25 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7ff85eed-fa91-3638-ade3-191f360fca9d | -6.7664 | -35.22019 | 2025-02-25 00:13:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| f25d15d3-4845-3f7e-9de3-f15063bb50e2 | -8.06465 | -34.97723 | 2025-02-25 00:13:00 | TERRA_M-M | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| dee040f1-62bc-3d94-b5a7-a65e44a8591a | -8.94196 | -44.24971 | 2025-02-25 00:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| cc7182e8-faf1-3687-afd4-eb59429c0478 | -6.76866 | -35.23483 | 2025-02-25 00:13:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 4e8142b9-f7c5-384f-b7a5-93c00b147f79 | -6.77984 | -35.23315 | 2025-02-25 00:13:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 6d0652fc-002a-31a0-b4b8-3a3faae53b88 | -8.94003 | -44.23499 | 2025-02-25 00:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 96749ce0-d64d-3b1b-af70-cf91ac64f95a | -6.16728 | -35.21823 | 2025-02-25 00:13:00 | TERRA_M-M | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 05168efe-9939-36d3-b03a-761eb061c6fb | -6.77756 | -35.21833 | 2025-02-25 00:13:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| f920ca65-6a98-3c47-8434-81fc1271c59e | -6.77783 | -35.22487 | 2025-02-25 00:13:00 | TERRA_M-M | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 43b29205-fbc2-3bca-b660-017b05624fb9 | -10.87455 | -44.79411 | 2025-02-25 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 471d4bac-893f-3267-b332-0312d1e475e3 | -8.94207 | -44.24335 | 2025-02-25 00:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8019b654-c223-3268-a168-a7c2aca8c00a | -6.76666 | -35.22665 | 2025-02-25 00:13:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 22.2 |
| cad38831-106e-32bf-8760-f7fb87392c58 | 2.7431 | -61.2813 | 2025-02-25 00:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 1f298f2f-1c41-3014-a524-c9621c630ec7 | 2.7431 | -61.2813 | 2025-02-25 00:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 92c9a493-0ed3-3a70-a849-1e796d585f3b | 2.7431 | -61.2813 | 2025-02-25 00:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 9662ca0b-b45b-3b8d-b5c2-1602d5434390 | 2.7431 | -61.2813 | 2025-02-25 01:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 24ddbc72-fe62-3be0-94db-fa5ae7b56088 | 2.7249 | -61.2627 | 2025-02-25 01:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| dafa6c2f-e2a6-3d59-a867-90e185b2c40f | 2.7249 | -61.2816 | 2025-02-25 01:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| fa97532c-9b6d-3e3f-9153-98f1f701d144 | 2.7249 | -61.2627 | 2025-02-25 01:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cabc4148-9fe6-30f5-9661-3e01712ee583 | 2.7431 | -61.2813 | 2025-02-25 01:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2872b2e9-ef67-3aee-b27c-a478ff21884e | 2.7249 | -61.2816 | 2025-02-25 01:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b4b3f55e-3dcd-3b4e-bd67-46f903f09b49 | 2.7432 | -61.2624 | 2025-02-25 01:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| a915d908-69c3-3f3e-af73-2b3aa0cf768f | 2.7249 | -61.2627 | 2025-02-25 02:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 6efc863d-49f0-3d20-9323-f96a12074d8f | 2.7431 | -61.2813 | 2025-02-25 02:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 80b37a24-29a2-35c2-80ce-57219204aead | 2.7432 | -61.2624 | 2025-02-25 02:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4d9220e3-a30b-3fbf-922e-f8122022eca9 | 2.7249 | -61.2816 | 2025-02-25 02:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c865c79a-43fc-3dd2-bc5c-7bf811dd6a49 | 2.7431 | -61.2813 | 2025-02-25 02:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 976b093b-4ecf-370f-ad64-b3565ae7e494 | 2.7249 | -61.2816 | 2025-02-25 02:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 140.2 |
| fe1d1bc4-0a17-3bda-9ff8-35ad36640c18 | 2.7432 | -61.2624 | 2025-02-25 02:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 116.8 |
| ffa78a94-6404-3a31-931f-ee30d777aea8 | 2.7249 | -61.2627 | 2025-02-25 02:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 58371611-976f-37cf-b162-01f479baacd9 | 2.7431 | -61.2813 | 2025-02-25 02:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 64d26ba2-d657-3b8b-99c2-5afaeeb22d51 | 2.7432 | -61.2624 | 2025-02-25 02:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8e2ced9f-d498-3d8c-a676-4aa7dd4ba37a | 2.7249 | -61.2627 | 2025-02-25 02:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 145.1 |
| d63b0d25-e345-3528-b38c-47536e6959d0 | 2.7249 | -61.2816 | 2025-02-25 02:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 969cfc47-d9a9-38a6-a9b0-181d380255b9 | 2.7249 | -61.2627 | 2025-02-25 02:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 130.8 |
| d1f96d36-1234-344c-b0ce-3c0306d70aff | 2.7431 | -61.2813 | 2025-02-25 02:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 6ec1e8b5-a46a-31db-8a63-71a090007e35 | 2.7432 | -61.2624 | 2025-02-25 02:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 323a3b43-a154-3e2b-b31e-02f727d3a297 | 2.7249 | -61.2816 | 2025-02-25 02:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 173.3 |
| 3359e953-0f94-3703-bc11-e9150a733a39 | 2.7432 | -61.2624 | 2025-02-25 02:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 25510b9b-7d1d-3dfe-8fa0-c5400caf2a70 | 2.7249 | -61.2627 | 2025-02-25 02:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 383a61b2-4c26-3124-9fa9-297f4b5b808a | 2.7249 | -61.2816 | 2025-02-25 02:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 109.7 |
| fd3f4e91-cf5d-32d2-ae0c-81459ee5e94a | 2.7431 | -61.2813 | 2025-02-25 02:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 171.7 |
| 6e56d635-1698-308c-bde0-5f3c65bb8c7f | -15.8955 | -43.4523 | 2025-02-25 02:40:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| d32f52a8-5ffb-33a0-8dca-9fd4f681cdb1 | 2.7249 | -61.2627 | 2025-02-25 02:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| ef290568-0014-3d14-87d4-4ff2440c0670 | -15.8955 | -43.4523 | 2025-02-25 02:50:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 30054039-f3c1-3d5e-9cf3-ae0d29db717d | 2.7431 | -61.2813 | 2025-02-25 02:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 128.6 |
| c2b6f2ff-b669-383c-8682-59ca9250623c | 2.7432 | -61.2624 | 2025-02-25 02:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 82.1 |
| a1d07614-f9c5-3e66-a161-be798c0f82cb | 2.7249 | -61.2816 | 2025-02-25 02:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 143.3 |
| ae7884e6-6af6-3d5d-8bf7-2b087db7d0cf | -7.47509 | -35.1545 | 2025-02-25 02:51:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| f437daea-1a23-352f-9132-36e7b2a32b82 | -7.46914 | -35.15486 | 2025-02-25 02:51:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 41634f6a-8677-3ffe-9e41-8efcc246898a | -8.06903 | -34.97813 | 2025-02-25 02:51:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 12746eba-ccb1-304f-b566-e2ba1cdea758 | -7.47564 | -35.15615 | 2025-02-25 02:51:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 43b19f3b-5fff-352f-8164-3c5544a7694d | -15.8955 | -43.4523 | 2025-02-25 03:00:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0bd8bc48-bd4f-3047-9ca2-766a5347c642 | 2.7431 | -61.2813 | 2025-02-25 03:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 116.9 |
| fab0ab92-fa84-3c65-a5f7-4bc091adc5a8 | 2.7249 | -61.2816 | 2025-02-25 03:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 10fc633e-bd80-3376-afb1-799a1198f51b | 2.7432 | -61.2624 | 2025-02-25 03:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 06a2100b-ebbc-338a-9e5d-6f9526d0f8f2 | 2.7249 | -61.2627 | 2025-02-25 03:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0c1b3247-89aa-345b-8714-4a79d712544a | 2.7249 | -61.2627 | 2025-02-25 03:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| fee282ef-110a-3ef9-8115-fecf431e0582 | 2.7432 | -61.2624 | 2025-02-25 03:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b1755e1c-2a3f-3f03-80eb-9260ed27f29a | 2.7431 | -61.2813 | 2025-02-25 03:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 16d7ac44-de6e-3d67-8334-bac7fa476422 | -15.8955 | -43.4523 | 2025-02-25 03:10:00 | GOES-16 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 138.6 |
| e53ae638-300d-3724-84a5-9149332e948c | 2.7249 | -61.2816 | 2025-02-25 03:10:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 0024f4d0-cbc9-3cba-be90-ad40732f762d | -5.24984 | -36.31656 | 2025-02-25 03:14:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 556bcfa9-8c25-3c3e-85f3-e13768f8307f | -5.18964 | -35.76207 | 2025-02-25 03:14:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d88a9113-760e-3d94-89d8-407563c6cc3d | -5.18814 | -35.75868 | 2025-02-25 03:14:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45ee6cdb-bcf2-3649-a4a9-2188e685c8c7 | -6.46889 | -35.00433 | 2025-02-25 03:14:00 | NOAA-20 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 41896458-4b67-33db-be38-3369c1465a79 | -5.18729 | -35.7636 | 2025-02-25 03:14:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| da508d80-62e5-31d1-9532-5f2df72deb0d | -18.11534 | -39.68877 | 2025-02-25 03:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ba662477-e0d7-3ca6-81e5-357dc9896a96 | -7.46989 | -35.15582 | 2025-02-25 03:17:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 51d71c03-1e77-374b-b663-b6107fa3f6d4 | -8.11557 | -43.1387 | 2025-02-25 03:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9e7e6320-1ddb-3c5c-90c1-464847880f3f | -9.40845 | -40.3166 | 2025-02-25 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e0d740ac-3aa7-3947-b023-13817d487cbe | -8.1117 | -43.1386 | 2025-02-25 03:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 835f7089-7855-3a04-85f1-557dc965862a | -7.07794 | -35.09186 | 2025-02-25 03:17:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f52359ac-c6df-3d95-99e0-47c67bc70ad8 | -7.17225 | -35.59322 | 2025-02-25 03:17:00 | NOAA-20 | JUAREZ TÁVORA | PARAÍBA | Brasil | 2507606 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89043911-b8f8-30d9-8aef-1c9d60fce29f | -8.11417 | -43.14569 | 2025-02-25 03:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 419c8fa4-cce6-33ee-a6f1-fbe326ee1129 | -7.47607 | -34.84442 | 2025-02-25 03:17:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8996ef88-d3fb-3d10-ba4e-d3342686f710 | -9.40259 | -40.31546 | 2025-02-25 03:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8b5091c4-b55d-3568-827e-89fa6bc916bb | -8.39424 | -35.48345 | 2025-02-25 03:17:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0416113f-b785-35be-a41b-c73831a2ee33 | -8.06952 | -34.97922 | 2025-02-25 03:17:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| bc9badfb-1428-3343-9c5c-15b80beb4ce4 | -10.5313 | -42.4372 | 2025-02-25 03:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4eb8d569-8ae1-3980-b074-8e7084410455 | -8.39496 | -35.47934 | 2025-02-25 03:17:00 | NOAA-20 | AMARAJI | PERNAMBUCO | Brasil | 2600906 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc552366-a948-3b62-a500-e3e3fbe983eb | -8.11035 | -43.14557 | 2025-02-25 03:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0fc05f7e-d809-39ff-b25c-dafd4268dcc9 | -18.11695 | -39.68785 | 2025-02-25 03:17:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 47911869-2e4a-39f6-bceb-b9d35fd8948b | -16.6807 | -43.88466 | 2025-02-25 03:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47867e36-f6bd-315a-be81-94aac1a0c688 | -10.52962 | -42.43943 | 2025-02-25 03:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 934fa003-1342-31b5-9e1e-29235ce1cfaa | -13.04015 | -40.34472 | 2025-02-25 03:17:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67d895ad-d2cb-388c-9eca-aa5b9e598753 | -15.88625 | -43.4639 | 2025-02-25 03:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 76b2c42f-d536-323d-84be-f7dd8d679d68 | -8.38559 | -34.95959 | 2025-02-25 03:17:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7f05beb9-a75d-3fee-aecc-f10de0c9fdea | -7.47061 | -35.15167 | 2025-02-25 03:17:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2c5ca47a-44f0-3646-81e0-f40ea79c9a1a | -13.04086 | -40.34115 | 2025-02-25 03:17:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 96ee8a17-ee05-310c-9bdb-c65eebf8f774 | -15.88742 | -43.45851 | 2025-02-25 03:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 4d6e98ed-f3a8-36bc-a278-8af4c6cdf8fd | -10.07728 | -38.03782 | 2025-02-25 03:17:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5397bac0-73a9-30bd-ae39-c45ff32062fe | -15.89255 | -43.46539 | 2025-02-25 03:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 393a42f5-5d5d-3a62-ae1e-41f35bea3e08 | -15.89372 | -43.45997 | 2025-02-25 03:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 622d239b-44f1-3245-83cf-3857efd736a9 | -10.53024 | -42.44255 | 2025-02-25 03:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2a5d4efe-c0b4-36f4-8fc6-8444caa29016 | -7.07294 | -35.09518 | 2025-02-25 03:17:00 | NOAA-20 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
