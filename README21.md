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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3687521-f2ec-37c0-9216-a4cba3a78c70 | -10.3088 | -53.7015 | 2024-10-10 01:05:33 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b413722-4b4c-3fd8-96c9-af92d810065e | -10.7907 | -55.837601 | 2024-10-10 01:05:33 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 931814fd-d3ed-34cd-8cd2-328f2bc92527 | -10.384 | -54.165699 | 2024-10-10 01:05:33 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82406a56-ffd1-38dc-8f0e-9dcea62bfae5 | -10.5876 | -55.0662 | 2024-10-10 01:05:33 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b418115e-f0d0-3fa9-91b9-acad493ecb76 | -4.9513 | -42.9973 | 2024-10-10 01:05:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 13fb4ef7-5536-3f01-a5f5-8ba014736aa7 | -4.9515 | -42.9739 | 2024-10-10 01:05:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 1c3f60e1-bb35-3c11-b569-cf100a90d86e | -10.3742 | -54.1679 | 2024-10-10 01:05:34 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c62ee1a-52bc-3b3e-88ae-f59906474dd3 | -10.3758 | -54.175098 | 2024-10-10 01:05:34 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc56820-1623-3e85-8833-9287bdba16fa | -11.0483 | -57.199699 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7e041bb-4f44-377a-b3f0-2c745f359bd9 | -11.0353 | -57.187 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d77f427b-6884-3767-8632-22f1e203d04a | -11.0369 | -57.194401 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9092b85e-3d79-3ac2-a55b-1b914cdcc0b2 | -11.0385 | -57.2019 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6588f3ad-3327-3b76-833a-f460b744b96a | -11.0401 | -57.209301 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 838c18c9-8826-3d38-b114-4d85aa933671 | -11.0417 | -57.216801 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3ad7f37-42f9-34b2-b89b-b8f602ea2f47 | -11.0255 | -57.189098 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d15d0ec-f580-3169-baf6-6ca7535b9ef2 | -11.0271 | -57.196602 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5852292-c875-331b-9aa8-4b69c0cc4f04 | -11.0287 | -57.203999 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b887f7f-578b-32a0-8726-47ce9147a9c5 | -11.0319 | -57.218899 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 581d2991-16b2-3ed5-a4a2-7c1e794f2318 | -11.0189 | -57.2062 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2425cf76-b646-3c87-b15c-a39fe656a6cd | -11.0205 | -57.2136 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a32b16e8-0890-3cf4-b308-ecc32845cfd9 | -11.0221 | -57.2211 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 236d6c95-6d84-3197-87f7-55956fe04c97 | -11.0237 | -57.2285 | 2024-10-10 01:05:34 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6128a510-29df-3eb3-b688-ac09559ebee9 | -5.2361 | -44.8018 | 2024-10-10 01:05:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| ce2bfa88-af69-33b8-9e12-8ed7a77a10ea | -10.6225 | -55.868099 | 2024-10-10 01:05:36 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 056534ec-c05b-334f-bf20-82976721d11a | -10.624 | -55.875099 | 2024-10-10 01:05:36 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dccbaeae-caa1-340e-b397-78fb777c67eb | -10.6256 | -55.882099 | 2024-10-10 01:05:36 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3098c465-be4e-35e1-bc21-8e175f4c8512 | -10.6271 | -55.889 | 2024-10-10 01:05:36 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b36c22f-c0e7-32d0-9c30-b29a4f1fffb0 | -9.4843 | -50.970699 | 2024-10-10 01:05:36 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1599fc26-ce67-367a-9d17-91b436942744 | -10.622 | -55.912201 | 2024-10-10 01:05:36 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1fbcaacb-0dbc-3690-83bd-bfade77734fd | -10.6235 | -55.919201 | 2024-10-10 01:05:36 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a73f7179-f2e3-3b2a-93df-34f2e9db139f | -9.6464 | -51.785301 | 2024-10-10 01:05:36 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007baa01-c975-3166-8822-37ec9bbd9b44 | -10.2158 | -54.2873 | 2024-10-10 01:05:37 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7157184-fd6b-3398-9902-efc39f45c8cb | -10.2174 | -54.294399 | 2024-10-10 01:05:37 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4e8c515-6576-3637-80c1-9a583f8a3efe | -10.9108 | -57.466 | 2024-10-10 01:05:37 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ac2d95d-abe5-3966-99f8-0a6868e14806 | -10.4822 | -55.607899 | 2024-10-10 01:05:37 | METOP-B | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 423c514f-de18-30b1-a6bb-785d016e5e8f | -9.2426 | -50.349499 | 2024-10-10 01:05:37 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81a9cc12-8f0f-33b9-91fa-808f78272942 | -11.1212 | -59.075699 | 2024-10-10 01:05:39 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee24b258-5383-39d4-b15d-0f7e50b6d34a | -11.3931 | -60.3815 | 2024-10-10 01:05:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cb8bfc4e-8666-3848-a00e-3ece25ef9e9c | -11.3954 | -60.3923 | 2024-10-10 01:05:39 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 24495cec-349d-37f7-978b-f387fd14c9e9 | -9.7141 | -52.823799 | 2024-10-10 01:05:39 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 924585f9-3bf4-3a4a-99a0-f8d78ea5e5ab | -5.9036 | -45.4127 | 2024-10-10 01:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 088eeb50-e939-3c14-944c-ebfde144d84f | -5.9223 | -45.4114 | 2024-10-10 01:05:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 5aec1eb5-a164-341a-807b-19f66e986612 | -9.7713 | -53.159199 | 2024-10-10 01:05:40 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e340ca1b-8b47-3003-a6dc-2708cfebde9c | -9.7731 | -53.166901 | 2024-10-10 01:05:40 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ded3fc52-d478-3191-9484-b698393a015a | -9.7463 | -53.1404 | 2024-10-10 01:05:40 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 309a3e41-85f9-3fc9-bc42-fd3231f7f33c | -11.3463 | -60.550701 | 2024-10-10 01:05:40 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 20b86e24-fd6c-3c74-b5d3-07e2099c711f | -11.2691 | -60.373699 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 730ed09a-d836-3c71-8b51-99a6a104ca84 | -11.2713 | -60.384499 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 103f4ced-ad12-36e3-917a-c159e658dd14 | -11.2593 | -60.375702 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4f7e45-9fca-39dd-b9aa-270cf0b6c467 | -11.2615 | -60.386501 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d958223c-51a5-3b03-ad36-b21e84eeb0e8 | -11.2674 | -60.464298 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9e1300bb-0bc4-3370-a92c-f4efa459d6ac | -11.2696 | -60.475201 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ea933c54-057d-39fc-901c-bf4e1ede7d0f | -11.2576 | -60.466301 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2dac41e1-f962-3449-8d57-18c0639949f2 | -11.2598 | -60.4772 | 2024-10-10 01:05:41 | METOP-B | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7c547f97-6284-3b93-95c3-39c9e0853a07 | -10.1059 | -55.1688 | 2024-10-10 01:05:42 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1229bd34-8bf7-3bf8-b31c-c82905774e05 | -8.7861 | -49.654598 | 2024-10-10 01:05:42 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c74de2c0-09be-3cea-97c3-3a290fb47baa | -10.5776 | -57.5392 | 2024-10-10 01:05:42 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbc16f08-1ab8-37c3-b4b1-b94746cc7b82 | -8.4934 | -48.6236 | 2024-10-10 01:05:43 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 406dbd03-33d8-395c-a0d4-23f062fe00a0 | -8.7711 | -49.762901 | 2024-10-10 01:05:43 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8ac2cb-86db-3409-8554-dc0684b4ffd9 | -8.7741 | -49.775101 | 2024-10-10 01:05:43 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dfc3beb-54d6-34d0-bb25-2d17ce73d3e0 | -8.777 | -49.787399 | 2024-10-10 01:05:43 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6be5618a-eaf7-32e2-8671-e38470a80f93 | -8.48 | -48.611301 | 2024-10-10 01:05:43 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 67837201-ab26-37ec-aaf8-adc84dc656d0 | -8.4837 | -48.625999 | 2024-10-10 01:05:43 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| e3bc2d5b-528f-3521-85f8-b1a1e0e83b99 | -8.4873 | -48.640701 | 2024-10-10 01:05:43 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| dae9fbdd-bbbf-327e-856e-a0108f98e6f6 | -8.7389 | -49.7579 | 2024-10-10 01:05:43 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aec9f44-4092-3187-a116-ee04a878d3c5 | -8.7419 | -49.7701 | 2024-10-10 01:05:43 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0630e959-43a9-3977-a45b-8adf6612adb2 | -11.1605 | -60.5895 | 2024-10-10 01:05:43 | METOP-B | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7662a8b7-63d3-3d36-aa91-9fdf5a161f2d | -6.5218 | -60.0649 | 2024-10-10 01:05:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 46783223-a2d8-3385-b3f2-01f850ab510b | -9.1327 | -51.488701 | 2024-10-10 01:05:44 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b20bcf15-5695-3001-a47c-016b501a0cd4 | -8.5596 | -49.189301 | 2024-10-10 01:05:44 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1dca06e-f202-3705-9a31-51fb59057383 | -8.5629 | -49.202801 | 2024-10-10 01:05:44 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf817768-ab38-3ac6-9987-44e9d227cc35 | -6.747 | -59.3259 | 2024-10-10 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ccb7b40e-7919-3594-98c9-d0c40e874a96 | -6.7654 | -59.3252 | 2024-10-10 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.3 |
| cd1f41fb-bd57-3b4f-a30d-b923d079065b | -6.7655 | -59.3059 | 2024-10-10 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d94f9964-b40d-3dae-a5d4-5938e3378a3f | -6.7798 | -60.0552 | 2024-10-10 01:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 381806a7-fc6b-3cbf-b666-0317ccf19ffb | -6.7839 | -59.3245 | 2024-10-10 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.4 |
| bca5a5d9-a6a1-3a0a-820b-f7041c6e86f7 | -6.784 | -59.3052 | 2024-10-10 01:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 55be3d2a-982f-35f9-b2d3-0afc5b06b3da | -9.9543 | -55.319801 | 2024-10-10 01:05:45 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77f4ec32-0e84-39ae-a576-4b850a367a1b | -9.9559 | -55.326698 | 2024-10-10 01:05:45 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44be6bbb-a1d6-3960-a31f-15ec25dc5249 | -9.0215 | -51.455002 | 2024-10-10 01:05:45 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb6ca9e6-e19a-3487-9a56-860a60b70b31 | -9.0237 | -51.4646 | 2024-10-10 01:05:45 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 516ccb35-1f20-38f2-9102-a0c0aeeb7178 | -10.3292 | -57.4832 | 2024-10-10 01:05:46 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6d1e692-156f-3da5-8394-1f41c4de14d6 | -10.3308 | -57.4907 | 2024-10-10 01:05:46 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 936170e3-011b-3e9f-9f06-c9ffce3f198a | -10.3325 | -57.498199 | 2024-10-10 01:05:46 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6547bf-cb80-3296-b37a-f17b5c87a6fc | -7.1346 | -59.3099 | 2024-10-10 01:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ffb8266a-1a4c-39cd-8096-0fcd83422b19 | -8.7611 | -50.707699 | 2024-10-10 01:05:47 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcbe99d4-0cf3-31d9-abdf-72ce948b6e52 | -7.2965 | -44.949902 | 2024-10-10 01:05:47 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e7cae4d-b496-39a9-ab59-03ec230aad65 | -7.2799 | -44.9249 | 2024-10-10 01:05:47 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15b1dbf4-2765-3eb1-a657-132e81c38d23 | -7.2869 | -44.9524 | 2024-10-10 01:05:47 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2f84985-a2eb-30ab-817e-5512252b6263 | -7.2773 | -44.9548 | 2024-10-10 01:05:48 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abffb02a-0aee-3c5c-a7f2-85c37609cf3d | -10.2804 | -57.683899 | 2024-10-10 01:05:48 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e5306e95-5c64-3e4c-a604-c29c14bccb92 | -10.282 | -57.691502 | 2024-10-10 01:05:48 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a77c93cc-abf2-33fd-8149-8d7d2b8fed84 | -10.2755 | -57.7089 | 2024-10-10 01:05:48 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5f86ca-66f4-3334-84ed-7988170d2d3b | -8.3899 | -49.551201 | 2024-10-10 01:05:48 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15ee8a97-8d69-30e1-a6b3-990c9c695356 | -8.5603 | -50.515202 | 2024-10-10 01:05:49 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40a53035-8264-3d8a-80e1-187711bd596c | -10.2217 | -57.792702 | 2024-10-10 01:05:49 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0680aae5-560b-396f-87a5-efe80e335f0f | -10.2234 | -57.8004 | 2024-10-10 01:05:49 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7c7d39-df72-38bc-b12e-41e5043544ef | -10.2534 | -57.939499 | 2024-10-10 01:05:49 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a050fec3-c8cd-37eb-ad45-e805cbff4375 | -8.5505 | -50.517502 | 2024-10-10 01:05:49 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e10d02d8-2ae3-3df4-a815-0b4706c0642f | -8.3305 | -49.646599 | 2024-10-10 01:05:49 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README22.md)
