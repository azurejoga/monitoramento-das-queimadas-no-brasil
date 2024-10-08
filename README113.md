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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1604edd-d80c-3d75-be4b-ff4439486c96 | -12.55671 | -53.06713 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574505ec-ecd2-3205-9d13-3391a152a33f | -12.55193 | -53.06316 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac8c9321-6201-3802-8969-a913cd28adaf | -12.55153 | -53.06642 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e064258-6e00-333e-b452-8811409373e4 | -16.49213 | -53.97049 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 466cc1c7-31bf-3e56-a2da-ee347ed6b1bc | -16.49178 | -53.97356 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d50455-93f9-3f97-bfba-57bc19e2ddd2 | -16.47663 | -53.96911 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01460185-7e3f-39e7-878c-5a9f7164e6c8 | -16.47628 | -53.97221 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6d5a3d4-66bf-33c7-861f-593b8dfcd732 | -16.46735 | -53.91189 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7e090116-cf38-39da-a4d3-c22639f1d190 | -16.46563 | -53.90992 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47c2420a-3da6-39e9-8150-bd54941c06d1 | -16.46524 | -53.91317 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2675334-d190-303e-b212-240babb1a3b4 | -16.46455 | -53.91899 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b832074-79d7-3727-960c-c00b5fba5102 | -16.45906 | -53.92117 | 2024-10-08 05:23:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2b50694-4e1c-31a6-836f-bb4dcc18d0ef | -17.77198 | -53.80327 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f189251-37b6-3cbe-b10a-0745aab3d82f | -17.77164 | -53.80645 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f83bf205-365a-3290-8819-d482ba5f137f | -17.76666 | -53.80289 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2aaddfb2-d85b-39b9-9c00-879c9b3e7e69 | -17.76634 | -53.80592 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| edaba84b-83ce-31af-9e83-6191f3b810ed | -17.76599 | -53.80913 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 61ea9195-2d6e-3993-9873-77ac9905b46a | -17.76564 | -53.81239 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0b23a0a3-56b6-3ada-98fd-17d9218ec9f1 | -17.76035 | -53.81184 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a7064d3-eab6-3c25-9c37-f5e210746c7b | -17.75999 | -53.81513 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e67dbbc6-5d04-3712-bfdd-7e4c4eb8106c | -17.16004 | -53.94847 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6604a1c-20bf-3564-be18-07ce00983e29 | -17.15967 | -53.95168 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4057afe3-40cb-3ec8-8970-752b13d7fca6 | -17.15557 | -53.94129 | 2024-10-08 05:23:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca5f8ea8-4325-3ff0-bcab-725f77bcd43b | -17.15521 | -53.94454 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f5c39aa-ac5b-367c-9901-9f641b37a837 | -17.15484 | -53.94782 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb73c024-c338-34d2-84f6-e1d9bd2490e1 | -18.08724 | -54.31936 | 2024-10-08 05:23:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38e6b340-5bc1-3032-a0ef-a2e844bf16c5 | -18.08342 | -54.30697 | 2024-10-08 05:23:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 03442f4b-dc43-37cf-81f5-f451e6378efe | -18.08309 | -54.30997 | 2024-10-08 05:23:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7a3330b-a3cb-3903-8063-ef8f63b13a71 | -18.08208 | -54.31896 | 2024-10-08 05:23:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abe589d4-ddd4-3f50-9eee-c0c01a7a08b9 | -17.33737 | -55.01414 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d4f0405d-ed39-3e68-bdff-5fc5e94fb2da | -17.33673 | -55.01969 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| aaca8782-25a7-3cab-9c72-5a748682df17 | -17.33609 | -55.02521 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2515eaf8-127e-3b33-96c5-4187aa4bad42 | -17.32932 | -55.04112 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0625f7ba-c612-31f6-860d-db9caba09df4 | -17.32831 | -55.00732 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b7e5a937-0bfc-3ad6-b36d-42049783f12c | -17.32767 | -55.01286 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d9c8e5c2-e7b4-3bdf-8d99-38162d0836c3 | -17.32345 | -55.00671 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 461fc24d-cfd9-3773-b3c3-4f0cc0a901e7 | -17.32281 | -55.01224 | 2024-10-08 05:23:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 77d6e37f-099d-397b-90fb-fee467a6524a | -18.90034 | -54.57719 | 2024-10-08 05:23:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3e8a9b54-81fe-3a1f-930e-e3f998ef0e84 | -18.90001 | -54.58022 | 2024-10-08 05:23:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4f5a1fa1-d574-3231-831f-681166bd316c | -18.88409 | -54.58399 | 2024-10-08 05:23:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b82e90bf-d3ef-328b-ae67-4360d8cca3de | -18.87903 | -54.58302 | 2024-10-08 05:23:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09ffaf92-7113-34b1-ad2f-d41d445e3221 | -18.87434 | -54.57862 | 2024-10-08 05:23:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d27a81d-499d-3d90-9358-416539ee44ba | -18.20966 | -54.45509 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a880b29-a5ee-3d9d-85d8-6c02674a8517 | -18.2093 | -54.45824 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4afa7f47-d92f-322a-a229-9f474e2d1411 | -18.20786 | -54.45213 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5757582-aafe-3fa9-8321-911df6c599b6 | -18.20752 | -54.4553 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eec36cc-51fb-3266-864f-865a8a62a18a | -18.20494 | -54.4512 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f27574-89b2-3e2f-80d4-9421c071a18c | -18.20458 | -54.45435 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66bd88d4-154c-3140-80cb-adb694bf2ef3 | -18.20422 | -54.45749 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17e593ee-ef25-3392-9d5a-65a641f79a99 | -18.20276 | -54.45143 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07178bc5-7b5d-3cbf-b3c1-16a850deb9cc | -18.20243 | -54.45457 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a5bd4b-e4ae-31b7-ab32-3c50919debe3 | -18.19948 | -54.45369 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13aaeada-3181-3eac-be3d-2e53d3696edb | -18.19913 | -54.45679 | 2024-10-08 05:23:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7ac30bc-a8bc-3ad7-be92-33df9b97a2f4 | -18.72477 | -57.27634 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| af4bc1c4-5560-31d2-a018-270702859519 | -18.72371 | -57.28464 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 234c1fe5-7bef-32ae-857b-612e541f898f | -12.66434 | -54.71339 | 2024-10-08 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f796781b-4c4f-3387-aa3f-1a39d698c412 | -12.66371 | -54.71825 | 2024-10-08 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ad68a4bf-f8b8-3355-916f-e688aca864a5 | -12.65907 | -54.71758 | 2024-10-08 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2863408a-e373-3ae1-ab68-b2d76ab5623b | -12.65697 | -54.6972 | 2024-10-08 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10aa22a1-8e1a-3309-bced-9bbe5cd57711 | -12.65444 | -54.7169 | 2024-10-08 05:23:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ebb4032a-8dba-3aa3-b051-ccbaa4105bb3 | -16.60279 | -55.90391 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 58dd4e2b-be69-3db8-9134-beb3f6823392 | -16.59432 | -55.89799 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4b7e43e6-bcea-3ecd-963b-8603694f83c7 | -16.58979 | -55.89738 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 48742553-70b4-3478-8bd7-d07cfdb8fe33 | -16.58526 | -55.89678 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d55f8a95-bc81-327a-93f8-7011b1fc1ac7 | -16.58016 | -55.90091 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| fd140f9b-1a64-35f1-977e-f51db25afa64 | -16.566 | -55.90382 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 32829db1-9e3c-3ea5-a64e-4b05dece7126 | -16.56543 | -55.90853 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1dc5f378-cc42-3937-9244-9e4aec012169 | -16.55639 | -55.90732 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1d64c4ba-6789-3e12-88c4-df554d055e7a | -16.55073 | -55.91613 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 2b06908a-c311-3a78-ab06-74107371fa6a | -16.52916 | -55.93017 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 515df92a-c62c-37b4-86c5-a3afd3db3a52 | -16.60337 | -55.89919 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| df1e22c1-5694-33f5-a279-093f300d30fa | -16.59826 | -55.90331 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0c1ed574-1abf-3d32-88b4-6f8c93355b7f | -16.5949 | -55.89327 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 66bd47ec-f096-3525-9016-728b5ec0b011 | -16.58921 | -55.9021 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 31b6ff4d-217a-38b7-adfc-8ea88b8ede92 | -16.58468 | -55.9015 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4aa6d750-6fcb-3879-bb28-99beb6cb1dfd | -16.56091 | -55.90792 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 53f6d541-3362-370a-a1cf-910fb91d48c3 | -16.55582 | -55.91203 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f66a02bf-cf66-3c6f-93f0-bcf084369c12 | -16.54901 | -55.91851 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 85886672-888d-3a0b-9510-808385ac4bae | -16.54564 | -55.92022 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 11421f01-d5b8-3fc8-9df9-fa011bf9da90 | -16.52464 | -55.92957 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 41935087-d266-3750-8785-918a67096fe1 | -16.42593 | -55.94965 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 8a0aed05-113d-3a6f-a7a6-816bd9a40c65 | -16.42537 | -55.9543 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 4318a3f7-f58b-3cfd-ae80-96ca0a08308c | -16.42408 | -55.94781 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 19.7 |
| b401964e-4f4d-3f90-a977-be02816dfe5a | -16.42349 | -55.95245 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 8a8cee95-abc1-317a-beba-1fdd1e6b1bc0 | -16.4229 | -55.95708 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| fdf21312-9a8b-32a4-9166-04fdd012728e | -16.42199 | -55.9444 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b886e032-bad3-3198-b50c-2e8f4c376fd0 | -16.42143 | -55.94907 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 3b2179bc-a5be-3631-96f7-37865cc0cb49 | -16.42087 | -55.9537 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 05bf8179-5978-3bd4-a4ae-e38865b56e58 | -16.41958 | -55.94723 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9e0bd4ed-dbd4-3854-9834-ac2a3e73e5e0 | -16.41899 | -55.95186 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| cba09a92-6fa6-3235-8469-6b29d7f2729a | -16.41508 | -55.94662 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| e81af19e-a322-3f42-bc6d-f46474dfdce5 | -16.41449 | -55.95124 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c621a68a-43eb-3a32-913d-81b5f1dbc178 | -16.16127 | -55.93167 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| b23ab932-abdb-3f99-a459-143b356d0636 | -16.15677 | -55.93113 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6fb8dc80-5512-3f7b-8d65-6c3e6355127c | -16.15622 | -55.93553 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f3423d2e-1ac7-377b-b02f-870bd72a0e55 | -16.13272 | -55.8663 | 2024-10-08 05:23:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 11278348-6dc6-3c90-83c4-74befbfdc838 | -17.16549 | -56.13276 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 358a636f-5173-373a-b43a-ad30b1264e32 | -17.1649 | -56.13741 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 45cde759-e253-38e5-bf7b-3dd156423c26 | -17.16331 | -56.13002 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a1a71026-ed24-33ce-85a4-5977e401089e | -17.16275 | -56.13468 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README114.md)
