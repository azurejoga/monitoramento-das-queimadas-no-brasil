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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b481fee-64dc-3ee7-aa91-a083214d4cc3 | -7.58284 | -46.81653 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18c881f3-5c0d-35c3-bd2e-f12e3f3a3b05 | -7.58229 | -46.81999 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 455176f6-f562-39b2-975e-63c5ebdd3a9d | -7.55583 | -46.79449 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d89b735-9a6f-3361-90a4-9bd29fe08805 | -7.55528 | -46.79795 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e849fb5-284e-3c91-b19a-ae9713fce919 | -7.53379 | -46.78389 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c130a928-bc57-3eff-860a-f7f2b212dc81 | -7.52835 | -46.83982 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 111ede74-9822-3513-a1d4-a564428068e0 | -7.42544 | -46.65323 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc72676e-2784-3e2d-8ac4-eb8f4998e5c6 | -7.40014 | -46.59574 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b770ff4d-a0c4-3992-9f4f-9013da92249d | -7.38319 | -46.74939 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c711d95-7e1e-38fb-8ad6-636d9acb7c9e | -7.35733 | -46.65273 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb5f14a4-aec4-3a37-979c-00076145ed63 | -7.95246 | -45.69228 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4063c115-c199-39e1-b1e6-1e4becd5ddcb | -7.71602 | -45.70577 | 2024-10-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab60af8-ebf9-3e7e-9385-b1bda5408507 | -7.71547 | -45.70927 | 2024-10-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49c883b7-2581-3233-b3bd-cd5dcdf189a9 | -7.71323 | -45.70176 | 2024-10-27 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9e63712-2c95-3f15-8a58-bc61a0355ad2 | -7.39046 | -45.83462 | 2024-10-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 746a6dba-9bed-3b88-bca8-9b0331c14a33 | -7.95356 | -45.6852 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb38fd56-a6d4-3c7b-a974-e3a2a62e8efe | -7.94689 | -45.6842 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87fb4904-ce13-3aff-ab58-1e4e74c728c8 | -7.94357 | -45.68366 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a44af81e-4869-3fe4-84a3-b288cf9efd54 | -7.93969 | -45.68664 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 630790cb-f7f4-3ede-9bb9-9312e832e046 | -7.93914 | -45.69019 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37360a37-f131-3ff8-aa02-69b3f12f74bd | -7.90905 | -45.64204 | 2024-10-27 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2dde1e7-9d73-3028-9704-585eea3a7c25 | -7.58731 | -45.90084 | 2024-10-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed6abecf-fe1b-3591-82d8-4281dfb1a9ec | -7.33341 | -46.19948 | 2024-10-27 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec6eb41b-562d-388b-91ff-641680566409 | -9.10414 | -45.88501 | 2024-10-27 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95dc98dc-5bfd-369e-8394-f0facb203275 | -9.10748 | -45.88555 | 2024-10-27 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 761fd962-cc0b-384e-981f-08e65cb7dd08 | -8.27628 | -45.66259 | 2024-10-27 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3fffee1-3e1a-3ef8-aa8b-a09701f30745 | -12.66561 | -46.58171 | 2024-10-27 04:25:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2d7bb2b-0352-3175-8942-e0a543a9ed4b | -7.70912 | -47.00759 | 2024-10-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 971a7010-e369-3a5e-b9e1-a052101d794a | -7.49433 | -47.33409 | 2024-10-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de42e7d7-fe31-353e-9cbf-0ed1d92f4293 | -7.25487 | -46.84982 | 2024-10-27 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91d3ff15-74ea-3fdb-a5d3-446def014f22 | -10.74352 | -48.18303 | 2024-10-27 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 604ac641-47bd-309a-aff6-442bb18b8028 | -10.72139 | -47.96202 | 2024-10-27 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a754b647-84c4-3c95-97f9-3ea1b7c20efd | -10.71803 | -48.15411 | 2024-10-27 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 62929636-9517-3f39-9bb9-e3b9e66b3387 | -10.53791 | -48.6205 | 2024-10-27 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43dcade6-e24f-3a4f-8c9c-4310b7096f4e | -11.81848 | -48.75226 | 2024-10-27 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b12ed1e1-2d10-3ae8-8fae-fef51900a934 | -11.8179 | -48.75587 | 2024-10-27 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cf4cc86-14a4-348d-a4d8-055edda97aaa | -11.58609 | -48.7589 | 2024-10-27 04:25:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32575967-6feb-3161-95f5-70d4274c4c56 | -13.25589 | -48.24308 | 2024-10-27 04:25:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b42dd8e-61dd-339c-825f-0a40ad35bfeb | -12.69874 | -48.83868 | 2024-10-27 04:25:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 43074464-d6f6-3a22-b5c1-c996030042f4 | -12.69817 | -48.84229 | 2024-10-27 04:25:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be9e6dad-6f43-3fde-a606-a181bc5c9915 | -12.69759 | -48.84589 | 2024-10-27 04:25:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26e629e3-b40e-3998-9747-aed9545d0b9b | -12.69483 | -48.84173 | 2024-10-27 04:25:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b2b24e5e-2862-3419-bad1-fda9bb4cda48 | -12.69425 | -48.84533 | 2024-10-27 04:25:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c7494fd-e0ec-3412-ac80-837c2ef91d71 | -7.73822 | -49.86092 | 2024-10-27 04:25:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e8db19a-96f3-340d-8591-6143878f86b4 | -13.54622 | -49.88976 | 2024-10-27 04:25:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 291ce690-bc8e-3c03-957d-e0f82f250a2b | -14.26464 | -51.12428 | 2024-10-27 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 95ea88e0-cb5c-333f-8ef2-ce7a12293a74 | -14.26106 | -51.12367 | 2024-10-27 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 625ceba5-e5e2-33cd-b14a-fde03d14395f | -6.80329 | -50.88464 | 2024-10-27 04:25:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff401382-38d7-348c-980d-6c57d581c657 | -0.9815 | -53.7192 | 2024-10-27 04:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 1df7f069-d88c-3402-96ba-a0b931525efc | -0.9815 | -53.699 | 2024-10-27 04:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 4a27b744-b053-3461-bbe9-a779d27983bd | -0.9998 | -53.719 | 2024-10-27 04:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 63108db4-4d82-3afb-aaac-eb8b8b55ae86 | -0.9998 | -53.6989 | 2024-10-27 04:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 74ba36cc-0523-325f-9af0-5bb937da50e5 | -1.1831 | -53.8985 | 2024-10-27 04:25:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 2262208a-36f5-3623-8a54-ce0715d96491 | -2.531 | -51.2024 | 2024-10-27 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 5c5a1790-94fa-3e75-870f-908484be963e | -2.5311 | -51.1816 | 2024-10-27 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 218.7 |
| 61bf1d45-4fd8-3dd7-b1b0-2515ed0f574c | -2.5312 | -51.1609 | 2024-10-27 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 0d7c065c-0c28-36aa-905b-3dd39129cd2d | -2.5495 | -51.2019 | 2024-10-27 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| df79e761-5815-3f00-b654-e3e82a4b872f | -2.5495 | -51.1812 | 2024-10-27 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 02baa393-5250-3489-adb9-240249a47732 | -2.5496 | -51.1604 | 2024-10-27 04:25:20 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 9a76d7a0-a867-39d3-8d19-e0107d51998b | -2.7034 | -49.3088 | 2024-10-27 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| be54fc6b-bb76-3de5-a000-2bc29e0974b9 | -2.8329 | -49.2626 | 2024-10-27 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0688b69c-9b75-39db-a7a1-f78283221506 | -2.833 | -49.2413 | 2024-10-27 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 6b786ead-b92f-3b8d-8157-320b5b16410e | -2.8514 | -49.262 | 2024-10-27 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 057c0769-7f80-3338-af6f-1bf093164771 | -2.8515 | -49.2408 | 2024-10-27 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 1c704ccc-bf55-3d63-8931-c0ec9d88fc5a | -2.7033 | -49.33 | 2024-10-27 04:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| fe4511ac-b8c3-3da1-a646-1177e7451c5a | -2.9345 | -51.7505 | 2024-10-27 04:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| fc4dcd0a-14ae-31f4-95f8-8ba0fa227689 | -4.952 | -42.9035 | 2024-10-27 04:25:33 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| f2af788a-7eb0-3b38-b2ff-52120da99b98 | -6.0326 | -39.826 | 2024-10-27 04:25:39 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 191.6 |
| 6ede7834-81e9-3901-9ef3-06f15804914a | -6.0329 | -39.8012 | 2024-10-27 04:25:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 95.8 |
| cbd2d144-5bca-3649-94d4-5b0fb7f2b9c2 | -6.0515 | -39.8243 | 2024-10-27 04:25:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 115.3 |
| 415d0d5d-b2ae-3299-b13b-39466775ea00 | -6.0518 | -39.7994 | 2024-10-27 04:25:39 | GOES-16 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 91764ebf-3ab3-3a78-9391-2b422c393528 | -6.8534 | -45.8794 | 2024-10-27 04:25:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 513e3c20-007b-324f-a36c-b58beb96a0de | -16.28941 | -40.11179 | 2024-10-27 04:27:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50ade733-115b-3a9b-be20-c5390d2030f2 | -17.1548 | -41.08147 | 2024-10-27 04:27:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6007f35a-7c14-3968-8d8a-473ab05f2d9b | -17.15422 | -41.08119 | 2024-10-27 04:27:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6611ce21-e802-3981-827f-a2518bfb4ca4 | -15.55979 | -43.15262 | 2024-10-27 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 5ea9c302-783d-365e-b1e4-102a47f394bd | -15.55929 | -43.15636 | 2024-10-27 04:27:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 57a7d17b-78dd-3261-9558-5f4ee8c4620a | -17.63773 | -43.69711 | 2024-10-27 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1750e289-a91a-3f5b-af20-677d0377f05d | -17.63323 | -43.70021 | 2024-10-27 04:27:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0579cc93-998d-387f-b0dc-1b015a5acb0b | -16.67906 | -43.88523 | 2024-10-27 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 353ce6bc-75fa-30b8-8aff-bb4ebe20b434 | -16.39963 | -46.09606 | 2024-10-27 04:27:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4dac9010-8b28-356c-9d9b-07aad97e4c42 | -16.39614 | -46.09552 | 2024-10-27 04:27:00 | NOAA-20 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02ef799f-f2c9-3d7e-82ad-360eed344c20 | -15.56739 | -49.36296 | 2024-10-27 04:27:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 286427ed-ac96-3ee2-8f48-ffcdba6399f1 | -18.33866 | -48.5755 | 2024-10-27 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2fb884ce-67ef-3a13-aa75-663ef654f049 | -18.33535 | -48.57493 | 2024-10-27 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f706ca7d-d7f1-3c33-bd87-a320f4f2d7a9 | -15.55383 | -49.76301 | 2024-10-27 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 406c64fd-42d3-3907-af3f-930a0d2c8754 | -15.55323 | -49.76669 | 2024-10-27 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5a63c77-67b2-38f3-8b8a-47ab714ccc4b | -15.07782 | -48.94356 | 2024-10-27 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de382632-192d-3f44-8e5e-bf1200e0092d | -16.10149 | -49.19344 | 2024-10-27 04:27:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 72d91af1-d3af-3307-9fb4-9da0790ed44b | -16.01073 | -49.23082 | 2024-10-27 04:27:00 | NOAA-20 | SÃO FRANCISCO DE GOIÁS | GOIÁS | Brasil | 5219902 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f204d8d3-14a3-37e5-8ae4-41e03732dd5f | -15.76652 | -49.24853 | 2024-10-27 04:27:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 999a3848-8f38-3fdf-adda-ad4110f49ef3 | -15.76319 | -49.24797 | 2024-10-27 04:27:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae23aca2-e933-34b5-8b01-b2df3f81ceec | -15.57189 | -49.35631 | 2024-10-27 04:27:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a6faea-84ca-3a7c-8f3c-b3f48d4ede7c | -15.5713 | -49.35993 | 2024-10-27 04:27:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f4faf55-a17f-3a00-bfd8-fc779d815f7d | -15.56798 | -49.35934 | 2024-10-27 04:27:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53960247-0ed6-3e99-92cd-c44790526a58 | -15.55599 | -49.77096 | 2024-10-27 04:27:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9135477a-be2f-3225-b713-5a0b3619dcc1 | -17.79411 | -49.23354 | 2024-10-27 04:27:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 844a429d-e213-36f4-9f28-b3fd9263c7f0 | -17.0065 | -49.78157 | 2024-10-27 04:27:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc9153df-c03f-3572-86ff-5c4c9cfefa0a | -16.79179 | -52.62753 | 2024-10-27 04:27:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997fa4a2-c3b0-31f7-bf8a-02bca314bd3d | -16.78806 | -52.62685 | 2024-10-27 04:27:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README55.md)
