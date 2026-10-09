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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f00c659a-345c-3fb5-8829-5a8d0b806112 | -6.91585 | -45.88182 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d89fc44-0581-3f0c-bb1d-e23b13090f0d | -3.11287 | -53.7955 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 89c222aa-256b-3d06-87b6-10bc49b3f81d | -3.09893 | -54.28051 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ddc5cbe-8761-3055-9c7e-3d8567ff2b41 | -6.52541 | -46.51446 | 2026-10-09 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0f01f06-aa9a-38ee-943a-cec6e9c13de3 | -3.90199 | -55.89683 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 884b1e40-1cbc-3ece-927a-1d72ad807df3 | -6.16212 | -44.13941 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c81c5c10-3f8b-3189-8166-bf33c54e6ab0 | -2.75405 | -54.10218 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8fac0b5-fe69-3cc2-9f31-03d0cdc5af68 | -2.93808 | -53.92073 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b80a786-eb4f-3967-9f5f-0460497cd4f0 | -5.00041 | -45.26961 | 2026-10-09 04:25:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37d5cae0-1fac-34c6-8991-973d578b3175 | -3.00597 | -53.91364 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2b345c41-07a5-338f-9839-3962ea509482 | -3.55782 | -54.69257 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a588fe6d-906a-35a1-ac1b-1fcb47c95995 | -5.71897 | -41.76807 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 0af4cf1c-18f4-38ee-a9ab-74603e1d521b | 0.92403 | -50.25915 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 752fd976-a1e9-3359-8b20-71c77efbb7ba | -3.11348 | -54.16312 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 9597778f-7fd9-320d-ae6e-0af2486c0e2c | -3.67811 | -55.94522 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96708891-560d-3517-bd9e-62b8e68c744a | -6.8187 | -39.55035 | 2026-10-09 04:25:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0bd80e30-6b62-35cc-bad0-12d14a2ca241 | -3.69928 | -53.66969 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5d17b19f-cf9b-3b22-9fcd-7627aebac1b9 | 0.94444 | -50.19896 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 924a68a7-1e57-35de-bba3-fa7d52033c9a | -3.10252 | -54.29039 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9753304-be0e-3fef-b0db-19aa21e64a60 | -5.7073 | -53.47522 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa7f52bb-56e0-3e19-8997-33b85cb188da | -3.01024 | -54.0722 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 010468c6-a980-364f-b5cc-e03565cc066d | -2.82254 | -57.13742 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e60c990-bdd9-3e41-bbab-c012e11659c7 | -0.39586 | -51.77349 | 2026-10-09 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d27dd047-a38e-38d9-bdfd-6a983546a860 | -3.30879 | -54.69965 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b76acc15-6dcb-3249-95cb-acc063c85e3d | -3.17755 | -54.74294 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed0ab04a-c605-3de8-9b28-dab5d7de7333 | -3.54996 | -54.67513 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8fc7f974-7d3e-3d32-af07-40b34d77c1cc | -4.64311 | -50.95553 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7c893c7-518e-3242-b510-c666a9c34851 | -3.08306 | -54.28113 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f1647d8-2c2e-3f48-a133-0b0687f313ab | -4.15524 | -47.98702 | 2026-10-09 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27f85c36-c2b3-321e-9b20-3c9a23cd5d25 | -5.3789 | -46.18571 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b80cb8e-3663-3371-a536-c9024552489e | -3.67239 | -49.52526 | 2026-10-09 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 37f175a1-6470-382d-8ef4-bdb39ab8a380 | -3.54563 | -55.52877 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4addddce-ea3c-3470-9596-d3b3089c989c | -5.08899 | -46.21023 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c745d22-c71e-3551-880a-7ac3fdc798b1 | -7.02792 | -44.79198 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b8455ca-1462-35ff-bc6e-eefec29b0cd6 | -3.2257 | -54.29368 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84a575e7-bc57-3bef-b758-ecd0436cf715 | -3.0142 | -54.04874 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ed4b34e-128b-32e2-a7a1-0c2a7accce53 | -3.02527 | -54.04453 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f2f86a6-9742-320d-aa0a-3efcc642cf78 | -3.43243 | -54.53898 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a30da844-97a1-33a8-b1d7-a609d566016c | -5.49286 | -44.29788 | 2026-10-09 04:25:00 | NOAA-21 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ec4e3f4-2c19-370f-8ee4-c026f93764d6 | -3.19172 | -50.54952 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 71d98aa6-d45d-33ad-9627-52b9a131761f | -4.79762 | -45.76677 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a175afa0-fa01-385f-acc3-4037e543a865 | -3.55834 | -54.68941 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fdb4b3aa-cfde-3f92-b8ba-01b54ad32fab | -3.08078 | -54.27659 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58e4e56d-580e-30d5-a0af-1305223d9b11 | -3.17818 | -58.8451 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e40fcf4-3683-3670-9ad3-87462f9bcec6 | -0.08173 | -49.48867 | 2026-10-09 04:25:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8cf18f92-f7d4-356c-858b-c1dadab31d48 | -2.98853 | -54.0841 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0676c863-a5bc-31ed-a12d-24ff52576ed5 | -3.43532 | -56.94259 | 2026-10-09 04:25:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f5594dbd-488a-3e4a-a6a9-8a872acbc0f9 | -6.01539 | -40.98088 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7ce929a-bdf8-3ad7-848f-c1706c7bda9d | -6.1391 | -44.15129 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c0b1475-cbce-397e-97de-4d9c68070226 | -6.90484 | -45.88726 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc8e7540-7c9d-3ddb-9ca2-0bd1534a1361 | -6.0874 | -44.26413 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c76e0e-d90d-3f9c-8cd4-b3a42c08b717 | -4.94254 | -45.66553 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b383537-b74d-3404-baf5-2d97a4ba8e2f | -3.50304 | -59.27148 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bae41381-49f9-348e-87df-3495629ff73c | -3.27424 | -51.0726 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aeb5e072-4167-39f5-8f10-03c0c27b3f2a | 1.69826 | -55.60551 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da6bbeba-eb8e-31d0-9bf2-36d5fcba22da | -3.85549 | -51.93885 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79754bdc-e092-35e9-a040-1cdd08647540 | -6.11538 | -44.81177 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1965b47-1a96-31ae-9c94-3798e127d999 | -0.8813 | -48.08397 | 2026-10-09 04:25:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0d588c2-b9f2-3330-95bf-9f8eeac785ad | -6.88262 | -43.70557 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69240823-0b36-34f2-ab63-ce99fbded373 | -4.29377 | -54.80875 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f86357b1-e8e2-36f5-b375-df8c2572aef4 | -2.83473 | -49.51161 | 2026-10-09 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e581f1ab-063d-3cc7-94a3-92fb0f3442d3 | -6.14646 | -47.92407 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40b4f4a5-f1e0-36db-b9cf-768e9c09608b | -4.07891 | -44.11652 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40c4f800-fb1d-359b-a3cd-f0bb818c0e00 | -2.93057 | -54.12041 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b6c4a17-9c81-33c4-8c23-d798104dd5e8 | -3.01493 | -54.049 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69f87630-f732-3151-99f7-eac9e9a76e4d | -4.12133 | -55.03574 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63b959a5-dfd8-3ff3-8307-3b6678341297 | -6.79786 | -39.33687 | 2026-10-09 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a0eed4cb-86b9-3f67-ac4c-c5fccb6101ae | -2.94594 | -54.15354 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0caa5c90-e441-37ee-8ff0-b8094f7085dc | -6.01234 | -40.97294 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 0a6ebf76-27e4-3dbc-a945-d2c3dfefffec | -5.99852 | -40.95216 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 46789d6c-f1ea-38c1-a123-8ddd0976dc0c | 0.54037 | -50.89564 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 19a68462-ca60-318d-86fc-f65327e8ca69 | -5.10548 | -46.21279 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0118590f-32cf-31e8-bb33-5761f84332e8 | -3.55431 | -54.68511 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 41ea2b6b-47cf-3c5a-a3c9-a54116ee3047 | -6.94264 | -43.66914 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef0167a7-2788-3992-a141-aa8392462937 | -7.22371 | -44.16333 | 2026-10-09 04:25:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd915cbd-54ca-34e2-97cb-ffa57ed5b344 | -3.17901 | -50.55276 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6df7fe81-70b6-3b1c-8ba4-730fc9ef9d28 | -3.78222 | -58.58918 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69f84416-d417-3000-9a10-f0c6ab38c212 | -3.5669 | -54.6742 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1b882987-fba5-33bc-b886-b9f7f38f3b15 | -3.93233 | -56.0247 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ceb1d1d5-fb5d-396e-a7c6-c090bbdd816e | -6.00157 | -40.96018 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| fb3539cb-d38e-3e08-8e0f-333ab18a83cb | -7.1319 | -41.81123 | 2026-10-09 04:25:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6c60f5a7-5c0e-37f9-8423-ee0adbe61744 | -4.91833 | -55.86053 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf97c0b8-aab1-3a75-849f-2a56ad9229c4 | -6.912 | -45.88479 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f63a6c62-9448-3cc8-911e-619d4e87527a | -3.07474 | -50.96197 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44b98dfd-3715-3b5a-8252-6ad940c54396 | -5.70183 | -53.47923 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 78885e46-42d8-302e-acbc-433095daec11 | -6.87995 | -44.81528 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d70aa05-fcf6-3333-ad05-ae6c667fdade | -5.70811 | -53.47789 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f3eefcda-ff32-3580-8b6d-59728c425c13 | -4.08515 | -44.12122 | 2026-10-09 04:25:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bcc26bf5-0893-3250-91f2-de095919c5fe | -3.17866 | -58.63678 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7c1653f-7852-3555-81f9-cde97a01ff6f | -5.39692 | -45.91367 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08e2d228-221e-3ef6-9aa3-bf80c796e7eb | -6.82467 | -39.3163 | 2026-10-09 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2cd51874-8704-3cca-9a6d-86c48ca9459f | -6.01016 | -42.26992 | 2026-10-09 04:25:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| afc3e288-2914-3483-ac79-aca613503ed8 | -3.1733 | -50.58773 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5bad42e8-3a97-33b4-903c-1b258173df1e | -1.54316 | -54.5606 | 2026-10-09 04:25:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95b6273c-916f-3d3f-a40c-395224981e81 | -3.008 | -54.05992 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f399eff-51fe-3df6-b2f0-14f4bb96ab43 | -2.7475 | -54.11033 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a8264805-5f69-38ae-a24a-0ad0c5f956e4 | -1.15374 | -54.22975 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 664d48fa-45e1-36f6-9745-147ec11fa852 | -5.70285 | -53.45221 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5eb32491-a6bb-3233-a24c-2dcb313d2a5e | -3.26581 | -54.0228 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f6f3c77-8d9b-3c32-9b4e-658dffd461fb | -5.68819 | -53.45451 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README75.md)
