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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8576839c-435f-3339-a512-9ed16548b926 | -17.45161 | -49.39811 | 2026-08-25 04:10:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bfde561-e87c-3af5-8e43-5760a8a35c9f | -15.26793 | -52.80154 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3d78181-93eb-3a51-b659-393e6751e67e | -13.8774 | -54.03081 | 2026-08-25 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f080bdb-3a23-3e05-a28c-d2134a65c16b | -16.39532 | -49.93206 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93dd9c46-db3f-3fc1-85b7-5c057f133ffb | -16.40249 | -49.92327 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f3346e3-0cfd-3ea8-8e31-5855903f5c53 | -16.39981 | -49.93667 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75c0d645-2f5c-3d47-ab7a-80180bcbbecc | -16.41798 | -49.92693 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9cf53df-0a84-3b9f-bffe-6f5c82c2de2e | -14.3855 | -51.96514 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ffe365a2-4faa-3778-b547-70e012c20122 | -16.40793 | -49.92476 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a3ae816-ca4d-33c4-9909-5bf1f63f1af9 | -14.37842 | -51.96854 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2d1d73d4-69e8-3866-b83d-8c6ed8f3a789 | -23.16713 | -47.09848 | 2026-08-25 04:12:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 14001e10-387d-3ca9-82c6-606190c91a78 | -23.16604 | -47.10141 | 2026-08-25 04:12:00 | NPP-375D | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 75890e50-774f-38cf-8ad7-b6f21643a9bf | -11.15 | -44.47 | 2026-08-25 04:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9789e107-9ce3-36cb-9715-fddc32149a98 | -3.5221 | -48.1896 | 2026-08-25 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b4d4d560-dbab-3aca-a11f-8d7dd537549b | -11.1252 | -44.4892 | 2026-08-25 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 964ecbed-60c7-398b-a1a9-63394b53ebae | -10.7801 | -50.9113 | 2026-08-25 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 46d73fc7-29bd-334b-96e4-0dbf2cd0125c | -7.0057 | -59.2575 | 2026-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 97b636f6-596b-3076-9d41-b88d9453146b | -11.1256 | -44.4659 | 2026-08-25 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7b59bdf0-ad2c-3628-b318-0c04b6ed130b | -7.0059 | -59.2189 | 2026-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 39018a97-2131-3d7c-a8a8-309bc6a883f2 | -11.1447 | -44.4632 | 2026-08-25 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 208.1 |
| e3f6c56b-29a2-3e4c-bf87-f2145f5de12d | -10.7988 | -50.9305 | 2026-08-25 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 625b8086-0998-35f1-8535-2eccebaaa9a4 | -7.2903 | -45.3456 | 2026-08-25 04:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 5a6ca0f8-ae9d-318a-8738-6664548cd1a0 | -11.1443 | -44.4865 | 2026-08-25 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 0e16acc7-f56b-3e44-871f-5cba2248a844 | -7.0058 | -59.2382 | 2026-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 321.5 |
| 647d950e-8f15-39a3-8c11-59788ca0ba80 | -3.5406 | -48.1889 | 2026-08-25 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 074fa726-f2e9-3c4a-a705-ef135293b2ff | -3.5222 | -48.168 | 2026-08-25 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 5dd32939-4ce5-39df-bc4a-994b9de46433 | -6.9872 | -59.2582 | 2026-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 261.5 |
| f360eae6-10b6-3ea4-a3f6-72534de2c11e | -6.9873 | -59.2389 | 2026-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 354.0 |
| c94ca66d-5e51-30fe-bcd3-1aaceb75074c | -3.5407 | -48.1673 | 2026-08-25 04:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 9c8e947e-bc3e-3d6c-91ec-d21c7e739eef | -10.7991 | -50.9093 | 2026-08-25 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 5b4e7ec5-9a59-3c87-84ae-1bdec0b9c6dd | -10.3727 | -45.0537 | 2026-08-25 04:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| eb02ad31-4f1a-32d4-b2db-924837d1844b | -6.6226 | -58.4995 | 2026-08-25 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4eb98ecc-f0e5-3803-98ac-808e8d160802 | -6.641 | -58.4987 | 2026-08-25 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e832f5f3-4cc3-3303-b8ff-8705e0693ef9 | -10.7799 | -50.9325 | 2026-08-25 04:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 134.7 |
| affcf670-3fbb-3af4-b35d-1628a5ed7709 | -6.9688 | -59.2397 | 2026-08-25 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7f4f0af1-7c04-303b-87ef-45417e3c2db7 | -7.2901 | -45.3683 | 2026-08-25 04:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| fbdb8f1f-2ac1-3c0e-9f97-e3b713683e29 | -3.36298 | -42.16093 | 2026-08-25 04:23:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd14a780-7f46-3a2c-a7e5-741528750a65 | -1.41999 | -55.72991 | 2026-08-25 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41f7e5e0-69a1-3696-9f32-b261a138bccd | -2.47594 | -49.35374 | 2026-08-25 04:23:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 484da6b7-a331-30ce-87f4-c57a9584ca8e | -2.60602 | -47.3564 | 2026-08-25 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9ccb197c-7d85-33c8-b1e2-8666e1ffc39f | -1.86795 | -47.98249 | 2026-08-25 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d95f74c-c5f4-3889-a74f-ea7c95394992 | -2.8089 | -48.67315 | 2026-08-25 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 430456e6-373f-3a12-a765-27a71070d4bb | -1.59458 | -47.3611 | 2026-08-25 04:23:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6e68f48-4ab6-327d-9c29-afe57cd41658 | -2.71921 | -48.8033 | 2026-08-25 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d272333-66db-3dfb-9631-6a0e2b1554e6 | -1.41858 | -55.73104 | 2026-08-25 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af9f43b5-2ac5-3e74-9a00-19bd31765ec6 | -2.11648 | -47.11768 | 2026-08-25 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2bd8fdb-9ab1-300d-8689-c6c641f6db4f | -2.80577 | -48.66753 | 2026-08-25 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72b32a10-d1a2-3e22-912e-884ae0a6d8ae | -1.21021 | -47.88574 | 2026-08-25 04:23:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1941b4c-74b3-309d-af43-c77d8c4bf66c | -3.30515 | -42.77269 | 2026-08-25 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f05c911e-597f-380d-8930-216286db7738 | -1.87176 | -47.98309 | 2026-08-25 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3830f7b-1f58-3d26-8b2c-6274cf05139a | -1.59089 | -47.3605 | 2026-08-25 04:23:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efd37dd6-59e7-3076-baf7-e71080824fcf | -2.47535 | -49.35744 | 2026-08-25 04:23:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| be434cb5-3a7e-342f-8b8a-31f3f9ffa981 | -2.80969 | -48.66816 | 2026-08-25 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cace3fa0-cf40-307b-9c52-8ba89315b5fa | -3.36356 | -42.1572 | 2026-08-25 04:23:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a2a8be88-f969-30dc-a3f3-4742afbb1cad | -1.41945 | -55.72572 | 2026-08-25 04:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8840150-2061-381b-97b7-818b94bcf577 | -2.11286 | -47.11713 | 2026-08-25 04:23:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 615214f5-3c84-33aa-be0d-f8cdf4cddb87 | -2.60967 | -47.35699 | 2026-08-25 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2619025-1866-36ef-8987-4d9d9742e8b3 | -2.04588 | -48.0378 | 2026-08-25 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe959615-2886-3352-b6e6-e5f45acaea1d | -2.1835 | -48.14207 | 2026-08-25 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4043bf22-b3ce-3ba7-90c5-c605726f226c | -5.77467 | -46.11503 | 2026-08-25 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7b68d16-1b15-313a-bc33-b3885b2e6008 | -3.8036 | -42.94789 | 2026-08-25 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9e582f31-7a68-3265-b7f2-40c08b2bddb6 | -10.04407 | -46.42392 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7df516c0-dc08-30ff-8d02-c32d8b8672bc | -8.09467 | -47.47208 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68b5541a-54ba-3156-a755-77642b195221 | -3.52984 | -48.18259 | 2026-08-25 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 963db335-65a4-3774-801a-b812177ff68d | -7.13113 | -42.79043 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1724208-bd78-38a9-9aa7-3e684d37e69e | -7.44802 | -43.12351 | 2026-08-25 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cde42551-1ac5-3205-9df5-a264f3c71ca1 | -7.64633 | -42.7244 | 2026-08-25 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 086cbe92-d110-3567-bfb2-016d2fd67bc3 | -6.35343 | -54.75802 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8879cf1d-e01a-342d-9719-4df55137b19f | -8.59752 | -54.73988 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 300b030c-e7d1-3c5b-93af-b682566e79ae | -5.01103 | -56.1397 | 2026-08-25 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8b294cc-1edc-3777-8eea-996eb4c2046c | -11.14405 | -44.47756 | 2026-08-25 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 32.8 |
| f62f0c5e-e04b-34ab-9b03-d41714ccce42 | -6.65437 | -43.90786 | 2026-08-25 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d49cc746-4f19-33d2-8d7b-eb4f554cd12b | -6.81787 | -58.6582 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8dd5a77e-48c2-36e5-9eac-0bb8790c650e | -6.18021 | -53.48856 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6776768e-ad22-3d1e-b84a-e20c86464b2a | -5.95317 | -53.58355 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ee55b1e-e4c4-3b95-8c2b-8c1d52eb3228 | -10.37211 | -45.05836 | 2026-08-25 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 100c7dbc-8b12-3709-b6f3-9ba5ec5eca85 | -7.1826 | -42.77865 | 2026-08-25 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13a640e1-a317-327a-96e1-97c17f3d6850 | -7.86744 | -46.11869 | 2026-08-25 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee501157-528a-3d29-b2a0-0591c6abc816 | -7.48411 | -44.94037 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f119c49-e7f7-3d09-9813-4a928e363eab | -8.13003 | -47.50888 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d887afe6-5d83-377c-85bc-ea6f345ee101 | -9.60231 | -45.37823 | 2026-08-25 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c59df53-f759-3edf-919a-75619a650942 | -6.62909 | -58.48755 | 2026-08-25 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| bd91f2ca-6daa-3775-ad34-830bedde26d7 | -6.21838 | -55.92478 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9978f852-4b6b-3a92-8378-cc388f460937 | -6.50785 | -55.22588 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4d942ab-f724-3b4a-94fd-8ed76118ff42 | -7.28577 | -45.35589 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8e24376d-1005-3da0-b1c5-bffd9494acd9 | -9.69335 | -46.0468 | 2026-08-25 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b8627e8-0f78-3f4a-8bbc-fa651d562bed | -8.09813 | -47.47261 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 68418353-12a9-3252-a22d-e1e7b25a9343 | -5.94285 | -57.73809 | 2026-08-25 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d8b497a-7956-361c-a539-1219b05add52 | -8.08661 | -47.52177 | 2026-08-25 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9803d1c-80c4-3db8-af28-23d2f1a196b3 | -8.1607 | -46.69954 | 2026-08-25 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7944198c-f11a-32d1-942d-34aec55ecaa3 | -7.48851 | -44.93398 | 2026-08-25 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35ebb1c3-416c-39ad-bc68-dac6844469e8 | -7.29073 | -45.36735 | 2026-08-25 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d3059f8-26c9-3dcb-9403-cd214c46bf4f | -3.9481 | -47.64931 | 2026-08-25 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 672970ed-b8d9-3b56-b648-252425279260 | -6.61774 | -53.1912 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2023c8de-6436-3fd7-a903-cf4c2d6eaecf | -8.76156 | -45.79593 | 2026-08-25 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d95ac517-9e8e-37aa-ac2e-55bb977d09d8 | -6.96837 | -42.09882 | 2026-08-25 04:25:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7960165c-83e8-31dd-8b41-aca4c635a03e | -6.08052 | -55.54895 | 2026-08-25 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a0bbf72-9880-3301-8e01-27e19473cc73 | -6.19048 | -53.49041 | 2026-08-25 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 354d4167-fc0a-39ce-8ed6-6905d2132aeb | -10.05767 | -48.45569 | 2026-08-25 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a0d41b2b-29e3-3ea1-8d42-e23ce5fe3afe | -6.60512 | -52.45585 | 2026-08-25 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README28.md)
