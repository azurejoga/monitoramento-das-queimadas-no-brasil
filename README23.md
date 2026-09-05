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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87747b5f-d416-30d2-bfb1-6ad51576559f | -6.1499 | -59.93976 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39e41bb8-5e85-38d9-bb8d-8eaa24146458 | -6.55375 | -44.77732 | 2026-09-05 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcb279c7-ae8e-363d-bb84-350fb1e3be93 | -5.29834 | -49.5613 | 2026-09-05 05:04:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f07d70dd-e9e0-389d-8b2f-330874fee267 | 0.03203 | -51.65062 | 2026-09-05 05:04:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93f5c63d-343f-3a23-ba81-9d5f26f1b76b | -4.22009 | -59.55844 | 2026-09-05 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 862a0d57-c85e-3fc3-930a-ae8918ee44d0 | -5.34584 | -56.03094 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 10033b65-d97a-3717-9c83-4fdf7a9dbfb8 | -5.59604 | -60.24301 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c5a9eb6-b1f7-36fa-a630-f54ef71e66a7 | -5.16889 | -56.05219 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa0007cc-5c3f-3e9f-be8b-afdafc944017 | -1.81161 | -47.88247 | 2026-09-05 05:04:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 204c85d1-69c9-350b-86c6-f93fe1e565f3 | -5.33538 | -56.03285 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ad88ec9e-f022-3cf4-8510-d08e837af90f | -5.84442 | -60.25589 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5c7f9a39-10a7-3fa6-887e-1941b8015a44 | -4.66585 | -55.63769 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b41e5eab-cf4e-307b-a130-2e1a64d02774 | -3.74699 | -57.34594 | 2026-09-05 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e78e800d-b144-35da-8593-efc9e46a135c | -4.27962 | -54.77516 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 047c77cd-027d-309e-8d89-5cc70061d1fa | -2.82163 | -46.71019 | 2026-09-05 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0b3cf48-4e32-3283-b550-07ccdb8d8a59 | -3.12658 | -54.62355 | 2026-09-05 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 664d5a43-1335-38eb-9151-180232551268 | -5.35077 | -56.02111 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 620259bd-6990-3f58-b855-bab451d13cd6 | -3.63361 | -54.75254 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f4b8bbd-cde4-320e-97c3-74b0aeaa0bee | -3.23002 | -50.57318 | 2026-09-05 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d7ce3e55-6cac-372b-a43e-31dfadf638a4 | -5.342 | -56.03388 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a16e61dc-4a61-3dde-9a8d-574d1cd3ea39 | -4.9157 | -55.79997 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eded5163-4f90-3970-8a1b-442b2d53ea7f | -5.30917 | -56.02503 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7557247f-eef4-3292-b16d-1e86b0ce27b2 | -4.64864 | -55.74785 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b68e1e41-328b-3ad3-b84c-615d5987d01c | -4.66862 | -55.64164 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 559f3471-85b9-3659-870f-bd59fd631c05 | -5.30586 | -56.02452 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3c5f997-6b77-3dcd-bc35-5250be9cbc1a | -4.66639 | -55.63425 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a09512b1-d1dd-3ea6-9d43-81bf0c060a24 | -5.59295 | -60.23746 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0d5d1ff-bd4c-3150-a14a-a99e2eb73a02 | -2.75476 | -54.67527 | 2026-09-05 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3cc096ab-2fc9-3f25-bff3-af5b71982aaa | -3.85455 | -54.20729 | 2026-09-05 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 785ba34c-cb38-3cb2-aab1-d73391cf53a1 | -2.93655 | -57.90302 | 2026-09-05 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1c41273-62c4-3fe3-905d-299829716bb7 | -4.67023 | -55.63132 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 698f201d-ad41-3dc3-8135-9cb27ec25791 | -5.2931 | -55.9978 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58ce495f-237b-3f46-82f7-c7478f8a1f0f | -5.31132 | -56.01123 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39a3aa07-9325-39af-8820-83e6e2549587 | -3.77341 | -61.77585 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a51b965-582a-33a8-b245-a1f3f1f32e8c | -5.30471 | -56.0102 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de3cb3b-302a-3720-8d07-f9b78c52ab57 | -3.76426 | -59.42271 | 2026-09-05 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6002795-be0a-3a5b-afb7-20351a56740d | -3.87309 | -52.25656 | 2026-09-05 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 483cb0a5-31ac-36e9-a8b7-797e69426613 | -3.80799 | -55.88025 | 2026-09-05 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6fa9da2-cd16-3bb5-9987-efc07c4a1cb2 | -5.33261 | -56.02889 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39e30c32-494b-359c-93c6-cec27ef599a6 | -2.5924 | -59.40137 | 2026-09-05 05:04:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20542125-f084-3e4e-8dc6-529cd02c0f59 | -4.67577 | -55.63922 | 2026-09-05 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 39227bff-e3a6-3aee-8e11-b1140723fedd | -5.17936 | -56.05028 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de21f91e-3ae0-3125-ae69-a2bc1934afb3 | -3.69151 | -51.99632 | 2026-09-05 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffdb8cef-6a27-37dc-b84a-9672df4b3f15 | -5.14766 | -55.94983 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60cd8330-4127-3833-bc06-a62d5eac4fd8 | -5.84009 | -42.63129 | 2026-09-05 05:04:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 55d4c237-c65d-3d0a-bcfe-ee347794a2ab | -5.34639 | -56.02749 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b77b692f-2d33-313e-999b-ad98405f7913 | -5.83585 | -60.25152 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab39a33a-c607-3651-a3cf-4f1a6bc1a2a0 | -3.7623 | -61.76071 | 2026-09-05 05:04:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac53c3a0-3c32-321e-b9dc-4dc63ee97371 | -6.20066 | -57.76905 | 2026-09-05 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7206750c-88f8-3567-9ca2-735972b9a898 | -6.35833 | -46.11507 | 2026-09-05 05:04:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7541713d-ee9b-3da7-93fc-c06490eb532f | -5.84362 | -60.25274 | 2026-09-05 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f769575f-6f1c-3d98-be06-444cabfcf33e | -4.64918 | -55.74441 | 2026-09-05 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b703a6d2-4f50-3aaa-891b-2d4e8f3eab6a | -7.24564 | -59.52801 | 2026-09-05 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25fd966e-4dac-3f1e-91da-85b4f1207ffe | -6.58926 | -59.91418 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f28f513-5c0d-34c2-86d6-4a74c01985e1 | -9.04898 | -67.63503 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ee6ae04-b78a-3616-802f-e3272cf8531f | -9.46747 | -67.42126 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5035d29b-5ccc-36e5-a13e-b4f8474141fd | -9.13552 | -67.81337 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b452d40d-7007-32af-a00c-6785bbad33b0 | -13.43015 | -43.82988 | 2026-09-05 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 4db8ddba-257c-3f73-ba20-5f09d016a533 | -9.13638 | -67.80879 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ffdd5b19-957d-32f3-a9cc-80adecec237e | -6.65857 | -59.96299 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe8d945f-7e34-382a-9597-3d27449b1a1f | -9.61489 | -48.55976 | 2026-09-05 05:06:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4467a2d1-fdd0-3827-9e91-05d90bc11ee6 | -6.65324 | -59.94804 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7539c4a2-b073-3f32-a3a2-89a2eb2ae14c | -6.65628 | -59.95319 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 424211e5-e105-3ba3-9d87-db4f7248f44e | -9.80503 | -69.08999 | 2026-09-05 05:06:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1014ec00-161d-3717-a5d3-0d27911d3bba | -6.65104 | -59.96174 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35dcf91f-3b67-30a9-8f5d-e1387053fe41 | -6.68185 | -59.96499 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dcdc5d6f-0449-3f1e-8078-c60442eafcbb | -9.13034 | -67.80771 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29cf6df4-4502-3914-8c02-cdeca741c654 | -13.43601 | -43.82508 | 2026-09-05 05:06:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 92e75a49-912c-3234-9746-afba3e11a3bd | -6.648 | -59.95661 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f60b160-c5aa-3e83-b13d-838f9e9a3897 | -8.97108 | -69.27314 | 2026-09-05 05:06:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10327adf-a6db-3d96-8765-c6d47b0b639c | -9.53304 | -68.63583 | 2026-09-05 05:06:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27b9cacf-ceb7-3ff6-b462-0292b01897dd | -6.64497 | -59.95146 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db754a14-5162-32bc-b27d-50451fa30bd3 | -9.38837 | -56.99403 | 2026-09-05 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 34bcd2dd-7362-346a-959e-a022a4d396eb | -6.65028 | -59.94572 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5fcd5d17-49a7-3a95-a4f1-2d986685be5d | -7.28368 | -61.11621 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e360a2e-4bcf-3780-b0d1-03e9bf43dd24 | -6.65481 | -59.94175 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8249013-d7b5-3e2c-96a1-f6f411611538 | -6.67286 | -59.94931 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b25b95f-63c6-3987-af25-a92dc80ca05a | -6.65021 | -59.94289 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a533fd2-a876-3804-8d6f-93c5407a044e | -6.66152 | -59.94463 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 35de4891-689d-32b0-a101-08e396c3d6a3 | -6.65251 | -59.9526 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a108940a-b866-3786-8007-930904878b47 | -6.65701 | -59.94863 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| d3c9bf6a-a8d5-3870-9a10-3be36895e341 | -6.66687 | -59.93894 | 2026-09-05 05:06:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0e3e9fbc-ac31-33ad-91f4-293e0d4994b3 | -6.65858 | -59.94231 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| eca5b695-e798-349e-a16a-d21fd5c0139e | -9.13725 | -67.80423 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 403a38f8-35ba-3081-b90a-95594200f73b | -9.46631 | -67.42003 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 653e319d-1df6-32dc-b4a7-b6f50acb5134 | -12.43708 | -43.27533 | 2026-09-05 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 716a57fe-f465-3bac-a535-b08abd9046b3 | -6.66004 | -59.95383 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 41b6a8b1-85a8-3ef3-9a3d-f981f0f7186e | -6.66834 | -59.95329 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| afb8a040-97c9-3982-8b8f-078fc1444e0b | -9.46161 | -67.42017 | 2026-09-05 05:06:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0beb10aa-c013-31c8-9eec-5cc051a56741 | -6.53046 | -59.93906 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52e9c5ce-9e79-3f29-a448-e243d1d66c7e | -6.65928 | -59.96121 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 805e1613-ee20-31ef-bdf6-bdc5eadf3d9b | -7.55149 | -61.34021 | 2026-09-05 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fca56535-1659-3678-b8b9-6a0361a6445e | -10.76232 | -60.73677 | 2026-09-05 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7ff08d7-f0bf-3d2c-881a-0ae17acfd670 | -6.56895 | -58.97962 | 2026-09-05 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5842b05f-029f-3051-b3e5-a2a85a35b8d6 | -6.68334 | -59.97937 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7a1e751-2d32-37d1-aca4-0698a04706e3 | -6.65481 | -59.96234 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36e0a235-8f26-30a3-9edb-4bce4598e1ab | -6.66235 | -59.94288 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7e465a5b-11c4-3e83-bf49-ffede520c015 | -6.65328 | -59.95085 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a66254b7-f229-365c-9bfb-a8d966f5d33a | -6.65557 | -59.93718 | 2026-09-05 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 46e729ca-243c-32af-97e1-5c927a21ff17 | -12.44084 | -43.27871 | 2026-09-05 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README24.md)
