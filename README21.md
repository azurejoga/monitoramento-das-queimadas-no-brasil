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
| 23a1bcce-ca36-3a74-9e3c-b317f81b7f67 | -12.8561 | -51.94208 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6099fe67-c0e9-3243-bd35-689f2859cca8 | -3.2107 | -46.80387 | 2024-12-10 04:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3903d86e-c2a0-3a78-a242-07618aef46cc | -2.99451 | -53.02174 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 496e9b39-6a51-34d9-b6a6-f5b1052a4ded | -2.81398 | -53.04393 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f867c1d0-4339-3160-a0d0-939b4a38b8e6 | -2.03878 | -54.43224 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7530611-7720-37d2-86a5-13f1813f0ba5 | -2.8379 | -53.06558 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2e68939-f656-31bf-8579-3bd499d9c34a | -3.07495 | -54.07893 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe571175-1212-3922-9bc3-bac58102519c | -4.54794 | -49.37097 | 2024-12-10 04:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dc53dc6-57eb-3c47-a6e5-9c1321338ea9 | -3.10102 | -53.25095 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8651ef8f-4509-34da-854f-d3a6f7ffd48a | -2.78387 | -52.86765 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8320c9bd-8a50-333c-a29f-d32f0dbad6cd | -2.80733 | -53.06446 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6c4dcb8-47f8-3ad6-a4b3-c9e0baee90e9 | -3.18267 | -53.8619 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| feded424-1c9c-3cf0-8dc7-642b2cfb5bf7 | -2.6331 | -48.05744 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9275628-21b4-3b3b-a25a-b2f707d2b876 | -4.39109 | -47.77073 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3420514d-74c7-3c31-af41-d03c29fc7d0c | -3.8368 | -54.29995 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45560277-54e8-30e7-a331-95b67e5d0b25 | -3.09728 | -54.07091 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ccbda9c-7d0b-3f2f-9887-f40e76cdfccc | -10.50431 | -44.93119 | 2024-12-10 04:53:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb4f02af-7889-3f4d-8fa5-14f961e8e24f | -2.30755 | -54.0042 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 506a93ca-30bc-3166-a5f0-e6795f45639f | -3.08582 | -54.07678 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35cab9c6-b487-3144-94fe-96dc067e0253 | -3.75358 | -52.10476 | 2024-12-10 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a33dd565-43e6-3856-aaad-3d51f1f22a3b | -3.47403 | -49.85147 | 2024-12-10 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2200c355-bbec-3b50-a1ea-40901e47be57 | -2.99686 | -52.85435 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e0390198-3f6b-31f9-8aa4-2a27dfb37282 | -1.54161 | -52.67698 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afb68c5d-4e4b-3649-bc88-18450615895a | -5.51137 | -46.25941 | 2024-12-10 04:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19fcee26-1109-3820-b8e4-4bf4c25ff164 | -11.83133 | -57.82129 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f22a00a-6cf6-3f61-ae4f-994c7bbaad00 | -1.39458 | -52.33429 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b66a6bec-9765-3ca6-abc2-fcc2a8b0a905 | -1.73803 | -54.16918 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1505fb4-176f-3d51-81da-dd39ee608021 | -1.52937 | -54.02089 | 2024-12-10 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed01a56c-985f-365e-9823-e6a5d45516f8 | -2.44847 | -49.02796 | 2024-12-10 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecb534dd-f7ff-38fb-8c1d-a03f35d5dbeb | -2.99456 | -53.04324 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d8d2dd7-b35a-33bf-8f84-5438ac0bbadb | -6.91751 | -43.51382 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6bf47ad7-573e-3aa6-971c-40b1a03018ba | -3.63539 | -54.68024 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b69bb516-464a-398d-8162-8df694a01468 | -11.82763 | -57.82067 | 2024-12-10 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d08ba2fc-a620-32d5-9542-e1d6ce73f243 | -2.41686 | -53.68777 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48fffce7-3f49-3767-bff7-9fe212b2f8e7 | -2.45148 | -57.92822 | 2024-12-10 04:53:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 233b18ee-1e8e-31be-9c61-cd0ac6a80616 | -3.26634 | -45.37489 | 2024-12-10 04:53:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58ec8fb7-8a90-3851-ad37-c104bf802732 | -2.36723 | -53.91377 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f139a92c-b893-36c0-9a17-652870e40d8d | -12.37242 | -54.16733 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4de0d241-9867-37fb-bae1-c8850bc788f8 | -13.94427 | -44.35847 | 2024-12-10 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 942573f5-c005-3eab-b696-8f5f6363330f | -12.56451 | -51.30609 | 2024-12-10 04:53:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaeba3fc-11a9-3b19-8f79-a35c0c6cdb76 | -2.82622 | -53.053 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c958ad20-8a9c-3605-81f2-719405640c75 | -2.41346 | -53.68726 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43fa9fcc-4b5a-39de-93e1-084d786e8e02 | -3.611 | -54.30687 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 083b88f2-8abf-3f56-af1c-cc686cc90d17 | -3.33906 | -53.25229 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8931403-365c-3548-b218-9230a1bfa824 | -1.32124 | -54.95304 | 2024-12-10 04:53:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae9fee8-0934-3a65-832e-2115162592ab | -4.19071 | -50.57368 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 039796ad-87c6-3e76-a574-a6dd5eeba25e | -2.77834 | -44.9982 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1d89604-ff3a-3526-adcc-6c33c50b7816 | -4.89505 | -48.05365 | 2024-12-10 04:53:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ea98fc0-b402-3973-90d8-191133bd4353 | -5.68177 | -46.48129 | 2024-12-10 04:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7965740f-da73-36c3-8724-904a87bb40cc | -12.36525 | -54.16978 | 2024-12-10 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2d5e308-9dbe-3ce1-b1af-b81ebf39e650 | -3.31025 | -52.74376 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac9a02b5-c06c-3f02-930b-bd1e68169a39 | -12.23606 | -52.4431 | 2024-12-10 04:53:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 819c9a26-c71e-38de-b55d-194fdd9a42d1 | -6.92135 | -43.51571 | 2024-12-10 04:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4fa5fba-7404-3097-8230-c073ac7009b2 | -3.30354 | -42.48145 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14f0d5c2-6ba1-38fa-9ff6-ef60528ebdd7 | -4.38936 | -47.75525 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 1596447a-5c5a-3564-b801-4561a691a7e4 | -2.17651 | -53.65495 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cf4e28b-2a83-31d5-aaac-417124c4227e | -3.81569 | -52.36132 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd1c517a-6ee1-310e-861a-d1d668f33615 | -3.59831 | -53.74466 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f07a4336-d049-30db-abf9-580fad998d09 | -6.73492 | -46.29115 | 2024-12-10 04:53:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bfe01ef-ab6b-34be-b138-9d5a37f466b3 | -3.69111 | -53.69299 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c78a0f75-89d5-32ae-a374-834a335479da | -3.53788 | -54.58699 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab62ed66-15fe-3274-9361-aa15c1f7cfba | -2.46163 | -53.66844 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a347f763-3b1e-3ad2-b622-84d90d8a81d5 | -0.84871 | -47.56005 | 2024-12-10 04:53:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2b4937e-09f9-3e03-a1dc-10948d78ac6e | -5.62567 | -43.95725 | 2024-12-10 04:53:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74138e13-fcf5-3213-a76d-a6c74a84c767 | -2.82664 | -52.96357 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a741853c-def7-3064-965d-301d623b7bd3 | -6.97197 | -42.98891 | 2024-12-10 04:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e2477e6c-dcb1-3a5d-a44a-db0dacaa87c2 | -1.42325 | -53.49002 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4777daaa-2278-3e47-a105-5579af068609 | -2.78231 | -53.24466 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 347a7f74-0e92-3b62-b041-c5cf34f311c2 | -3.51113 | -54.67809 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f31d586-3894-3dfc-9b9e-771267975b28 | -3.87094 | -54.35113 | 2024-12-10 04:53:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc605def-2d50-375d-a997-6e58ed4d82de | -2.86597 | -54.22348 | 2024-12-10 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea2cc47f-5714-3181-ba43-baf221b7a3e8 | -2.45032 | -53.65185 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64e0f841-f1fd-373d-96dc-511cca2eab1b | -4.54719 | -48.01993 | 2024-12-10 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0a875fe2-8a02-3509-9cd3-85a10f2d494f | -2.95916 | -53.11672 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5ed31482-8fea-30ba-8c69-88643bd00cd3 | -13.94092 | -44.36085 | 2024-12-10 04:53:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62b685d0-8d12-3c22-bcb7-edfc4982e3ba | -3.08371 | -54.04603 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84d9a61f-67fb-37d5-9344-37df90518366 | -2.44976 | -53.65546 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2495837c-3ada-3a93-8d93-321184294574 | -4.38216 | -50.81138 | 2024-12-10 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f82f6c4-e9e5-395b-ad3f-ba87011fa2d4 | -1.42836 | -53.47971 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97745762-4fce-3105-ac44-d1b4405e3c9a | -2.34467 | -53.85712 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f48a853d-1af3-372d-a4f1-57b17339c9e8 | -9.71654 | -54.89242 | 2024-12-10 04:53:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a3e2d05-26d3-36ce-997f-79a99a5588b5 | -3.53279 | -53.93888 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e74e8e2e-c8ab-3839-b4d2-43ab516eb9dc | -3.3968 | -52.66938 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 976d4628-b79b-3fb7-a160-8cd4b6fddb14 | -3.83382 | -52.35356 | 2024-12-10 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 519129dd-a5dc-3c8e-bdc9-18dc103fd90f | -1.50203 | -53.43139 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af0fdc0e-e7c9-306d-82bb-26075058f096 | -2.40891 | -53.69403 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fcb96590-916a-36e9-86f3-dbd8729970ec | -3.10492 | -53.24794 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d8bc8a9-7c18-397f-8a06-b3b0e82e3787 | -1.74572 | -52.8057 | 2024-12-10 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72b459ea-cfb3-3501-bb70-188d7353bf98 | -2.99408 | -52.85036 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d97955f7-3f80-3a18-913f-fd72931a34c2 | -2.81333 | -52.98307 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c493af8a-a68a-39de-947c-23045a8b21c1 | -3.12644 | -54.06396 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4202e902-d49f-3bb3-9a6e-5918f1b3b78c | -4.38543 | -47.75464 | 2024-12-10 04:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6d3a6473-a710-37d1-a984-333413e981cc | -3.39218 | -52.80672 | 2024-12-10 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f18d6a97-1386-3745-a690-b97232c572af | -2.98967 | -52.85681 | 2024-12-10 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45711e64-4c7f-310c-8d0d-7f09864e3622 | -1.52615 | -52.96942 | 2024-12-10 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 807ff88e-de1a-381b-8b86-6b474a13c4df | -3.07019 | -53.79628 | 2024-12-10 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8497a327-201b-3c5b-81ea-0a28c8438041 | -2.35863 | -53.79133 | 2024-12-10 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfe8afe0-49eb-3742-b668-ae91f5cac722 | -11.78507 | -55.13039 | 2024-12-10 04:53:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa60b949-f35f-3006-8a10-5144090c0cb7 | -2.82252 | -48.08674 | 2024-12-10 04:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176736ab-5bd2-3b86-a1a9-a2c5c4f6a30e | -3.23187 | -42.43121 | 2024-12-10 04:53:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
