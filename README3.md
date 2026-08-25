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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e403f073-3c09-3be5-85dc-f5d806fa753c | -16.3946 | -49.9191 | 2026-08-25 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 30939cb3-3a07-3c9e-a10d-f3b530bee2c9 | -7.2474 | -45.846 | 2026-08-25 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 74cf9aed-fd9f-374f-bd00-848b81db27a2 | -7.3103 | -64.7044 | 2026-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| df46c4b3-0135-31cb-baba-a5a62bde33de | -7.2856 | -44.0875 | 2026-08-25 00:30:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ee34e5e6-20ff-38e0-9929-65faf77b446c | -10.3536 | -45.0561 | 2026-08-25 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| ddeb5c2d-1ffc-39f7-a87f-06176027b359 | -6.6409 | -58.5181 | 2026-08-25 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| d3051617-7ec7-3c52-96aa-fa82b0e475c9 | -7.2659 | -45.8668 | 2026-08-25 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 4b7c10c1-113e-3a24-9447-eff4f03356e9 | -6.8008 | -59.5934 | 2026-08-25 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 1b72c73a-be31-3edf-bc9a-5c1eccf120da | -6.6411 | -58.4793 | 2026-08-25 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 434c8bb2-4440-3060-ae50-55c92033330f | -8.5973 | -54.7352 | 2026-08-25 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f6fddc21-ffdc-310f-8040-e9039dce957f | -3.5222 | -48.168 | 2026-08-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 847e4e6c-2325-3b14-8a91-d573af27c53f | -7.0057 | -59.2575 | 2026-08-25 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 0dee11a9-d936-3dea-948c-7959f331ddd2 | -7.529 | -61.3635 | 2026-08-25 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 8854541e-8633-32b7-ab23-75f0580b81b8 | -7.2525 | -45.3717 | 2026-08-25 00:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 07b4918b-8fa8-39c2-96be-1e8137875cc8 | -4.0552 | -48.963 | 2026-08-25 00:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 28f2ea53-a40f-3fcd-8649-7e33c72e6d7f | -11.4302 | -44.5382 | 2026-08-25 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 20108f82-8e18-33b0-a4cd-2da5730c9d00 | -11.1447 | -44.4632 | 2026-08-25 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 7561a3f4-5b60-37d0-a677-c990a4018843 | -8.0695 | -44.6552 | 2026-08-25 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| a294431c-492c-3fe9-bc70-d39bde0d57e2 | -11.1443 | -44.4865 | 2026-08-25 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 72b227b4-6aaf-3c88-b2b8-936b0b42314d | -7.4286 | -43.1182 | 2026-08-25 00:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 175.8 |
| 29e781c9-99b2-3c02-820c-c9d63cf375e0 | -7.2661 | -45.8443 | 2026-08-25 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 235.6 |
| c9f39f69-f20a-3374-a2ea-e7e3aa2fa353 | -3.5407 | -48.1673 | 2026-08-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| fc21b29f-3045-3c74-b149-0c7646a07679 | -3.5221 | -48.1896 | 2026-08-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| df14d33e-050f-34d2-85cd-128fbb670dc9 | -12.7797 | -44.2576 | 2026-08-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 5c5e3bf4-3519-3899-977f-5d6b099f47ea | -8.616 | -54.7339 | 2026-08-25 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5ab04957-5a04-3ac5-8e34-e86e3a051a5c | -10.3723 | -45.0767 | 2026-08-25 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 194.5 |
| d6b6ba5c-966f-3aac-aa24-f7e06a60129b | -6.1743 | -53.4834 | 2026-08-25 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 5b9f8655-be63-319c-9c1d-b0124220c233 | -7.2713 | -45.37 | 2026-08-25 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 72942ccb-579e-3bff-8a73-b10c05f25a8b | -7.2858 | -44.0644 | 2026-08-25 00:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ccbb3c45-3fe8-383f-b07e-a7ce0cbcafc3 | -7.3287 | -64.7039 | 2026-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 7a5cfd84-c6f8-339d-a25e-3e46f1769600 | -10.7687 | -50.926701 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3880afb8-8b0d-3dce-a22f-a57b08a453a9 | -6.7052 | -56.329498 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51a2d495-8a88-35ee-8f16-05f7602c3a00 | -7.0174 | -59.221901 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6e4d64a-d0b4-3c72-b3f7-58c637557ffc | -17.5975 | -50.882801 | 2026-08-25 00:32:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f018d625-aa0e-3a55-819e-c50333aec890 | -12.744 | -44.231701 | 2026-08-25 00:32:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dadc4f50-be5a-36b9-8460-631912208151 | -6.2587 | -55.402 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3becfb-31cb-3b82-8e6e-1f275479e5ea | -10.902 | -51.052601 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 148ea8ff-12b0-33f0-b263-d7888768c2bc | -7.2378 | -44.019501 | 2026-08-25 00:32:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6275624e-892e-3ff2-bdea-5d3473d7f73a | -6.1461 | -57.694801 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98b5b48b-26e3-3a42-8fe6-045b71335c92 | -6.2006 | -53.4832 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee50342b-26ad-32cd-b188-b85fadd252eb | -13.8781 | -54.016102 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb548047-ea55-3731-8017-568dc0c1792d | -6.9597 | -59.052101 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dba006ce-9ad9-392d-ac05-8e5eaf83fa62 | -4.1083 | -49.432999 | 2026-08-25 00:32:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4b8185-d646-3b48-83e5-d8944985c296 | -8.6016 | -54.7384 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76b7a450-74ee-396c-9e31-462869737364 | -6.1294 | -57.804401 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51678052-0ac1-30f0-aa5b-a866036e53b1 | -10.7958 | -50.910198 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5e5acc4f-d257-33c9-882d-19288c16f3f4 | -7.4934 | -55.349098 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 961eb8b9-7849-3c07-936f-4f83ae641a9f | -6.8272 | -58.635601 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| efc33791-01bd-30a1-9e29-30d0c7efc7e6 | -6.1738 | -53.4561 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eba3a7f-c1bc-3898-913e-8e9049d42a38 | -11.3977 | -44.4762 | 2026-08-25 00:32:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1ba727ae-5996-3d69-99dd-25b700d9e342 | -8.0536 | -44.605499 | 2026-08-25 00:32:00 | METOP-B | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e971a895-14ea-3335-b453-e2d2759c8ef8 | -7.0112 | -59.240799 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81a09f27-a4d6-3530-bfea-458d9b70bcf8 | -6.6023 | -58.361 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53b89474-c85a-3f96-ba57-9179985d1b43 | -5.0096 | -56.117699 | 2026-08-25 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14bd1d7c-5264-3d90-b435-b359fdad6cf3 | -5.7701 | -57.530899 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84fe2ca4-76b4-36cd-9a87-e0b8522c5b11 | -6.221 | -57.753899 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2c18b6-25d5-3b6b-a378-adf538d0d02d | -7.5124 | -55.569901 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73b025ff-04a9-3f08-9a06-8f2d873dd5d2 | -8.5748 | -54.847698 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eef6d37d-d159-3a67-b3c8-fd8afe19d331 | -6.6121 | -58.358898 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7eacb8c-5531-3fd3-bade-c5cdc7bcf6e8 | -9.1926 | -50.077702 | 2026-08-25 00:32:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01704e88-a126-3bc7-b499-bcd13c100c00 | -6.7334 | -59.424801 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fdf98570-8cfb-35aa-8df0-00fe2856c592 | -6.3546 | -54.737 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20e5f943-a764-35f3-bd9b-a55223886a57 | -16.392799 | -49.901798 | 2026-08-25 00:32:00 | METOP-B | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 273133e3-80af-3942-948b-ce40bff9a396 | -6.2207 | -55.4617 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e557c6ec-c2a2-32e4-b0aa-03521cd16679 | -7.3209 | -64.622498 | 2026-08-25 00:32:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2545fce-764b-32b8-bb2d-f76b2f1266cd | -6.6095 | -45.1213 | 2026-08-25 00:32:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4d11af1-311b-324c-86c1-af92a9116521 | -6.1658 | -53.466202 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be424db-7e44-3697-b6e4-4909d523a290 | -10.4593 | -50.4104 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 70de1cca-5a30-3278-a1b7-51f5b916fcbe | -4.4711 | -54.792198 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c1a0b01-91ce-3e4a-88f3-12ad540551a1 | -6.1852 | -57.731499 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 052f7aba-3966-338f-8107-ed4b9fec42b9 | -14.3966 | -52.9352 | 2026-08-25 00:32:00 | METOP-B | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 94c7959b-194a-3642-811a-081d0ce7c47f | -6.1278 | -57.797199 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1d8daf-3f36-3cf8-a748-9a3486ad928d | -7.2386 | -45.343102 | 2026-08-25 00:32:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47d05b7c-bd2b-3d77-bb8a-481e84984ef9 | -6.7491 | -59.637901 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c070128-cee4-3398-b0bf-847f2a8bcb85 | -4.1181 | -49.430698 | 2026-08-25 00:32:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ce593f0-858e-3421-8765-e927813e03d4 | -6.7104 | -55.576698 | 2026-08-25 00:32:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24c27d59-51a4-30e6-b3bc-eeaca97e8274 | -11.5432 | -46.943901 | 2026-08-25 00:32:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e49bfeef-eda6-3c0f-8d68-5f3b8fd369e9 | -7.5723 | -61.174801 | 2026-08-25 00:32:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9abccdfc-a081-3ae6-8857-bb5d6c76c9eb | -6.8589 | -59.388802 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 977d74a6-0afe-32b1-9b8a-8e6d62b09cc9 | -5.8697 | -52.1036 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50f7a58a-581c-3f2e-ac8a-265b9c62d0fc | -6.3448 | -54.739201 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fd701ec-0c1f-364b-b738-7d58a2efd9de | -6.1793 | -53.479801 | 2026-08-25 00:32:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d64e65c2-46e7-35d2-ba91-10a5ec51c5ec | -11.8595 | -43.7761 | 2026-08-25 00:32:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 076f857f-e802-377a-9f0b-dc9d18110823 | -4.6009 | -55.723999 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2acbeee7-165c-33a4-9981-daa9fe62a97d | -5.7831 | -57.5429 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33aeb16e-12a3-3c88-84f5-2d0f9a56a3e7 | -6.2239 | -55.475601 | 2026-08-25 00:32:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f338f465-ba2a-3bd5-bd57-25ec731f820f | -6.947 | -52.7896 | 2026-08-25 00:32:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a169c5eb-0b8d-3d53-87ac-e2d700278b1f | -6.6357 | -58.4659 | 2026-08-25 00:32:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4715fbe4-287d-302d-bf64-ae0ba011e640 | -10.4715 | -50.418201 | 2026-08-25 00:32:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 978d45e5-fdda-311d-ab09-8fba7491460b | -16.497 | -54.6483 | 2026-08-25 00:32:00 | METOP-B | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c4e37162-384d-38e4-850e-61000ad60b0f | -10.9042 | -51.061901 | 2026-08-25 00:32:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c71378c4-c4bc-348c-9b1d-9b8d99e8851b | -6.1457 | -57.8312 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb731bde-4404-31cf-89ad-8edc00ee065f | -8.087 | -47.455502 | 2026-08-25 00:32:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20bb7b04-d857-3969-b3be-01fb3b9d91a0 | -6.8082 | -59.579498 | 2026-08-25 00:32:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 145abcd8-e007-38e9-81e9-2f1ee1945ca5 | -4.1349 | -56.349201 | 2026-08-25 00:32:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2740dbf-ca00-35ae-b51f-ec64d2688498 | -13.8699 | -54.025398 | 2026-08-25 00:32:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e5607680-a665-38a0-bce5-7bc8ed011bf7 | -9.5178 | -49.249802 | 2026-08-25 00:32:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4092ef5-2752-3d93-86dd-cca2b8bdf657 | -6.6138 | -58.366501 | 2026-08-25 00:32:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d21743a2-f6db-3189-bb26-3bdb26d00f64 | -4.93 | -55.766602 | 2026-08-25 00:32:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c307f8a4-febc-3d65-9c95-20942a91bc1f | -12.7056 | -48.361401 | 2026-08-25 00:32:00 | METOP-B | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
