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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b40efde0-4b32-381b-898c-0b4c4e0c1409 | -6.94999 | -60.01366 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a9be8ad-cbfd-3d8c-bda6-9e92ca552258 | -7.3913 | -44.88065 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 026d471f-8c15-32d3-a501-e48b91b13ba5 | -6.08196 | -59.9388 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a61549f2-f0d6-3acd-a657-d846d502f43b | -4.60604 | -43.31925 | 2025-08-15 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6865140c-eb43-3a52-8f06-c50804f994ea | -5.85994 | -44.74276 | 2025-08-15 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cdccf0a4-bc56-3150-b3ef-d7441115a058 | -8.30685 | -45.00896 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 828eda07-7454-36ba-bf62-d0c24bdda26d | -7.39658 | -44.87367 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a9808fb-986e-3a9c-ae3b-fea37181c91e | -4.18706 | -42.42546 | 2025-08-15 04:27:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a724817-0b00-31d0-ad0e-fac0d9f083d9 | -6.08595 | -59.94033 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e33e428b-9ebb-3a8b-8a46-d4749105188d | -3.11205 | -47.49797 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0be91994-6393-3ec4-b8aa-384c1209b4ed | -6.54247 | -43.49802 | 2025-08-15 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc78160c-06a3-3cdd-a285-d583699b14db | -6.60868 | -43.89061 | 2025-08-15 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc6e1ac0-d0b8-3b77-a2b0-6d578778f6c8 | -7.48275 | -46.28295 | 2025-08-15 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10479ecc-7603-3210-8fa1-a28add752235 | -6.22362 | -43.34144 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d8bc171-04a7-3d7f-b205-7eb82043d0e3 | -7.39074 | -44.88427 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 230b7d84-6b1c-3dd9-9eab-52ccba014b0f | -4.06553 | -47.9835 | 2025-08-15 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c12e631-9f92-31e7-8923-5b6fad5a13c9 | -7.39075 | -44.86193 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 06ecf50e-82e4-3b27-962a-13ccfdb2fc77 | -3.42955 | -49.04489 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4dd19631-8e18-3efc-ac23-cbd7eba3195c | -3.8268 | -47.74324 | 2025-08-15 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68ed9a56-bc94-34ac-9c49-748e818209d5 | -3.43255 | -49.04988 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 730af885-bcdf-3c48-bfb6-b95859db1236 | -8.31138 | -45.02465 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7a47d5b-bee2-3645-b811-26fd42563e12 | -6.95882 | -43.86285 | 2025-08-15 04:27:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e399990-4918-38a0-8a31-8bf76918a742 | -6.93328 | -59.53486 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| aa407942-249e-3148-bb89-81c40d97f523 | -6.21763 | -43.3419 | 2025-08-15 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d542f73c-780a-3d7a-91ca-0d1398382c76 | -6.72801 | -58.84084 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e35589ac-25ff-3475-89fc-dd0539a6da88 | -4.3102 | -48.10378 | 2025-08-15 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e5fdf34-2306-3d65-88be-01c22b723c31 | -8.31364 | -45.01001 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5b904492-6121-3a17-882a-5aa3d2b698be | -3.37824 | -47.6089 | 2025-08-15 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a062d87-c10d-3eb4-b4a3-1fbf464b504f | -6.06079 | -59.9565 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 83a32b35-fb80-3f59-9977-d96923d3e340 | -6.82429 | -44.48833 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbc3e050-76e1-36cf-b247-cf16cd25875c | -5.76252 | -46.67229 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 10db87ab-615f-397a-9c02-9882d729d962 | -6.65192 | -58.82632 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 701d21a8-b81c-3ac3-a89a-5b673f891e3a | -7.38451 | -44.87964 | 2025-08-15 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3c287a0-2513-31d3-85ac-fd33fc2c4ef2 | -6.95077 | -60.1452 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02cf803b-f767-313d-b1f4-18da6fa2821c | -7.24447 | -57.66543 | 2025-08-15 04:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a02e9d6a-5fb7-3677-b915-8091c464212e | -8.3193 | -45.01836 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4c5d6bd-ff38-308c-ba7b-74533df88831 | -6.94634 | -44.55549 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebe046dc-482e-379d-a06f-8c6133c2a37d | -6.66952 | -58.82341 | 2025-08-15 04:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73d57545-adb2-396a-98f3-41dea2bbe0a6 | -8.30005 | -45.00791 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bf966fe-9dfb-3779-9f80-e14e52b45525 | -5.75641 | -46.66774 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3caadb2d-c384-359d-8fc2-556f7cd95c08 | -5.75919 | -46.67176 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b6482af4-e7a4-342d-87ef-8b5a4726c4e5 | -6.34086 | -42.80566 | 2025-08-15 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c4877b0c-01ae-365e-98f5-49763556d9cf | -6.94142 | -59.52499 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1578cf6-004b-31d7-bc32-99d07b073348 | -6.70385 | -58.86018 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef724f5a-462c-3a26-9947-41e197475169 | -6.08633 | -59.9545 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| cee56338-826e-3723-a02c-9b4e63c5517b | -6.94975 | -44.55603 | 2025-08-15 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c881a188-c066-3461-85b1-3b16abe8b45e | -3.43625 | -49.05048 | 2025-08-15 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 128c67be-023e-3446-8849-6b65f0a71a18 | -5.5981 | -45.37727 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 706632e6-3e23-313c-9c9f-51e019137f78 | -8.31591 | -45.01785 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3549f07-63a4-3bc8-b2ad-64d4d6481b78 | -6.88515 | -59.15485 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be5804a-b9fc-3f7c-bbbb-5f2173d216f2 | -6.93536 | -59.63127 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f2062ff-2ecf-3ff8-bc4e-528fce5fdad6 | -8.32327 | -45.01519 | 2025-08-15 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c261e9ea-1f27-356f-a54f-b467f6782d68 | -6.10419 | -59.92139 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ef31ee1e-532d-3ab7-b12e-96c8122475b7 | -7.32877 | -60.62095 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21ac48a3-69e8-31e1-a187-e0562bdcbcac | -5.37222 | -41.24301 | 2025-08-15 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78545718-a40d-3eee-ad86-fb3ffd24635f | -6.8148 | -43.93272 | 2025-08-15 04:27:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6877f03c-6287-3138-beb8-2e5cdbc92947 | -6.07921 | -59.95309 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| baf6f167-c1f1-3d2b-bfd5-e939b2d4e474 | -6.10604 | -59.92862 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56739ea8-4aee-37a1-86ec-fda5ef0577ef | -6.06657 | -59.96515 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ea548a6d-08bf-3eeb-af42-f915e42ef4fb | -3.95461 | -41.48202 | 2025-08-15 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 786a9203-9be6-396f-896a-044686eb33ae | -6.08335 | -59.95431 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ee5aabf1-c430-3919-8aed-99f731125b06 | -6.1074 | -59.92151 | 2025-08-15 04:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1012c5f8-f1a5-3e0b-ab6c-ab189ff2f7e4 | -4.2269 | -47.21305 | 2025-08-15 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1928bbeb-4785-37c8-8db8-1fa88dee425f | -9.74834 | -48.57034 | 2025-08-15 04:27:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 973e1aaf-8401-3050-9a82-bd173026cdd4 | -7.29232 | -43.82372 | 2025-08-15 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2158ab65-d962-34ac-be17-28722c2b38ce | -6.94291 | -60.01235 | 2025-08-15 04:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a6aa0b3a-67c3-3de2-8eb3-78458aab6886 | -5.27227 | -45.17283 | 2025-08-15 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66d70c87-9bc3-3bea-a442-e672d10237c5 | -9.15844 | -59.66024 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68f777ce-7fd2-3201-b194-c3389c62144e | -9.19437 | -59.66852 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 335b3d30-3b16-3a0e-9d59-d5b1167819ce | -15.17677 | -49.74414 | 2025-08-15 04:29:00 | NPP-375D | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5193fa94-c077-34fa-a397-18f018c9ef54 | -12.50923 | -47.01153 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0eb07ed1-aa07-3c44-8a70-d07607439c2f | -12.58638 | -46.95489 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c2be7590-16ed-3d95-a387-1559e6af6be2 | -16.37928 | -50.90574 | 2025-08-15 04:29:00 | NPP-375D | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e228267-c869-3bc0-aa7d-a7c68642b46b | -12.51089 | -47.43639 | 2025-08-15 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f404b355-dfb0-3405-9fd7-4891285cd190 | -13.47535 | -56.66594 | 2025-08-15 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 255d6642-a93b-3256-b6b6-e71167098412 | -11.77902 | -47.39684 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2f4a78c-7eb0-3162-bb1d-2ff55d595a70 | -12.5973 | -46.96359 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7b0fe6d1-91f8-3dda-98c9-06ea8b20bd9a | -13.47475 | -56.66903 | 2025-08-15 04:29:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2c0af701-a5d3-3ad2-8864-457c80eed6cc | -10.00444 | -59.2177 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fda1e2f-9310-3b9d-8618-1e32f80ad2b9 | -12.75785 | -44.41183 | 2025-08-15 04:29:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 131f49de-26a1-3267-9737-6c420eab1a7e | -13.56851 | -46.95712 | 2025-08-15 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81ff1614-3f65-38a2-8917-a1cbc91b8bb4 | -16.60202 | -47.04611 | 2025-08-15 04:29:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c95f4ef-86f9-3446-9964-eb26be78fbfe | -9.15496 | -59.67833 | 2025-08-15 04:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 404f438a-2982-32e9-98a3-6319f7afd66c | -11.35274 | -55.43414 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0cb0d3a8-b4db-3ec2-849d-aae9c18c24e9 | -14.02174 | -52.03853 | 2025-08-15 04:29:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1e39303-824c-307c-b818-9a6701ae3ad1 | -9.3878 | -60.54813 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e08268ab-24b6-3a64-b0e9-349ce48bc58e | -10.11256 | -57.76476 | 2025-08-15 04:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a8c8742-e68e-3839-a519-88be2e680c07 | -13.32945 | -45.23278 | 2025-08-15 04:29:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ae381c8-96f2-35e3-a696-ac5e1bdbb47a | -14.57174 | -52.04298 | 2025-08-15 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88694dd1-37f1-352d-90c6-6c0bb83ef391 | -13.10856 | -57.16061 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2997a6a-4742-3691-ad60-36a4fcd3bcdf | -15.39205 | -46.58639 | 2025-08-15 04:29:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2aa03a68-b5f2-334a-a104-deb222046fb0 | -11.35258 | -55.43341 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6f73d61c-4ad0-39fc-b547-b813ab72000f | -11.3448 | -55.42004 | 2025-08-15 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1e2b2de8-0136-3f84-90fc-021d1a29ba9b | -12.67912 | -44.95916 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dba2c5f6-c8a0-3f74-acc2-c61a32aedb2c | -13.04613 | -56.84387 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| efdd2a74-0756-3341-83c0-5293ae6ac1f3 | -12.7886 | -45.96156 | 2025-08-15 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef059e8a-f6ae-3335-8909-561afd0b0568 | -10.05006 | -59.35842 | 2025-08-15 04:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bff34017-5508-3dae-abab-a3336c0402a3 | -13.11927 | -57.1628 | 2025-08-15 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 337cba27-9216-3641-b01e-f2fca3083dcd | -11.54296 | -47.26516 | 2025-08-15 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df06ebac-762f-3419-81a5-65b184ca86f8 | -12.57805 | -46.94258 | 2025-08-15 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |


[Clique aqui para ver as próximas entradas](README33.md)
