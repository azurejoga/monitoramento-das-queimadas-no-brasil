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
| 37710900-9269-30c2-98f9-c864f2208a16 | -11.1447 | -44.4632 | 2026-08-25 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| db0cb0db-d100-332c-867b-68ba6930de2f | -10.3727 | -45.0537 | 2026-08-25 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 618.6 |
| 70f07d45-c7a4-3f97-aea1-6799a4594185 | -11.1443 | -44.4865 | 2026-08-25 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8ab97662-4ecb-3818-9e0b-149ccfa7b64e | -7.6785 | -49.3843 | 2026-08-25 00:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d2d171d2-81e5-3649-a127-0478f18cab5a | 2.58 | -60.6973 | 2026-08-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a9db505d-3d43-3507-bdf9-4f40bd588d65 | -3.5406 | -48.1889 | 2026-08-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| e1c8505e-10d8-3e61-8783-ec88fa7a5ca7 | 2.5983 | -60.697 | 2026-08-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 53156bf0-c353-328f-96a1-51f1e8acd679 | -6.1743 | -53.4834 | 2026-08-25 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| d62206e9-eec5-3814-b845-0fe951857e75 | -6.1477 | -57.702 | 2026-08-25 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| afd6f947-3127-376b-9a1d-bcee6f3aca9a | -6.6409 | -58.5181 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| bc187a6d-6ec3-33be-b5bd-396e0d591c88 | -7.0057 | -59.2575 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| fb222fdd-2aad-3256-99eb-c9e7d61cb32b | -6.8008 | -59.5934 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 236f4379-c1a5-38ed-aac1-bdaadede2a7c | -8.0695 | -44.6552 | 2026-08-25 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 771e7a41-0b86-34ef-8f3d-eaf43149df75 | -7.5475 | -61.3627 | 2026-08-25 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 124.6 |
| beb56337-234e-36bd-bd02-0c205fbfc830 | -6.641 | -58.4987 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 339.2 |
| 94f81e28-632f-3130-807f-4342bdfca58b | -8.5973 | -54.7352 | 2026-08-25 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 1c475c61-e5d2-32fd-bf74-2a2104a66f93 | -11.4498 | -44.512 | 2026-08-25 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 4e134e2a-8693-393a-bf56-de07b70012a5 | -12.7797 | -44.2576 | 2026-08-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| cb04259a-e28e-396f-bccf-eea82f1b24ae | -11.4306 | -44.5148 | 2026-08-25 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 102696b4-bbc0-3471-8b7c-bf1b0b9a8791 | -7.2661 | -45.8443 | 2026-08-25 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 482.1 |
| b71cfcd9-7f89-353e-a0b3-06fa6a999c46 | -6.6227 | -58.4801 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| f58f2a4e-ea79-3549-adf7-9a1b54c8dcc6 | -7.2009 | -60.6132 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| e6196036-71ad-3c17-8006-b11f978e972e | -6.8192 | -59.5927 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| f7689523-095c-3661-955d-44b5c79291ef | -7.2659 | -45.8668 | 2026-08-25 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 175.2 |
| c83796bc-b995-36a9-9808-a71bea830719 | -10.3731 | -45.0306 | 2026-08-25 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 26c4ec00-51b6-31bd-91cd-23c13a3d7528 | -11.4302 | -44.5382 | 2026-08-25 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 135.9 |
| fa686112-23a6-35a3-8423-e842dc5c08fe | -7.2713 | -45.37 | 2026-08-25 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9b8d73e6-84cc-3d13-8df0-bdea64bedfbe | -16.3946 | -49.9191 | 2026-08-25 00:00:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| bdbe72d3-9ab7-36d5-8afc-23baf0142d8b | -12.7792 | -44.2812 | 2026-08-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ffda6bab-28d2-3c91-b4ac-4e6a7c028d27 | 2.5982 | -60.716 | 2026-08-25 00:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 37.4 |
| a2703cc1-aadd-3caf-b8be-2888a74080bb | -7.2858 | -44.0644 | 2026-08-25 00:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7bd9b76c-e907-3a2c-aec5-dc7426c46a49 | -7.0242 | -59.2374 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 3e85f1c2-e57c-35c3-a43d-847038743465 | -6.1928 | -53.4824 | 2026-08-25 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 2211c6ff-2138-3a31-9d37-ea3014a1d9a8 | -7.2194 | -60.6125 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 5f156695-7910-3164-bcf9-12156b861195 | -8.0697 | -44.6322 | 2026-08-25 00:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4bd5ddac-cd48-3e68-a254-347118ca9e0a | -6.8571 | -59.4179 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 4be50c17-650b-3d70-beb7-7d4c0ec7f350 | -7.3103 | -64.7044 | 2026-08-25 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 884c7924-e95e-3242-823a-728957217d15 | -3.5221 | -48.1896 | 2026-08-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 870ecfd4-f62a-33bd-8a01-644381ea2a80 | -10.3723 | -45.0767 | 2026-08-25 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 174.6 |
| f44b6cec-d62e-3a0c-b851-7f37e071c313 | -6.8247 | -58.6461 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 2f04e166-2423-35b0-a03b-7144641db827 | -7.2901 | -45.3683 | 2026-08-25 00:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| f9931ffd-269c-3d14-9a31-0b6f62288f79 | -12.8739 | -48.4957 | 2026-08-25 00:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 5ca21818-9a64-3528-bc95-a907822453aa | -10.3914 | -45.0742 | 2026-08-25 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1de976f9-2a72-356e-a5e6-393b2cc01beb | -10.3918 | -45.0512 | 2026-08-25 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 396f3a19-e177-30d9-a8ec-f0baac866473 | -7.2856 | -44.0875 | 2026-08-25 00:00:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 7ad15df1-65a2-30d0-bdd5-a3282232da7c | -3.5407 | -48.1673 | 2026-08-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| fc2278fc-daf0-3b77-aeba-e4636867fc69 | -10.3536 | -45.0561 | 2026-08-25 00:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 180.5 |
| d5e2b2a7-0253-3c2f-9cd0-dd6a7af70de3 | -7.2474 | -45.846 | 2026-08-25 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 17ee6b09-c0a5-37e8-abf1-85c41b946f99 | -7.3104 | -64.6858 | 2026-08-25 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 3cf10f24-2b91-3d6d-a753-902fbd94844e | -12.799 | -44.2544 | 2026-08-25 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| eafbb328-8071-36b6-a071-091325237933 | -6.6226 | -58.4995 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 204.6 |
| 2355edd4-565a-3953-995e-e4b3db878001 | -6.6411 | -58.4793 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 859e5776-dee1-317d-a380-d2ce84b0221f | -7.2471 | -45.8685 | 2026-08-25 00:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| e7b3b85f-74f7-3e3c-9947-c46f609dfb56 | -7.2525 | -45.3717 | 2026-08-25 00:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 73189f36-108c-3057-8dfd-80bdb525020a | -6.1464 | -57.9359 | 2026-08-25 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 46c482d0-65aa-30ae-90d6-a6ce54dd9ef8 | -6.8246 | -58.6655 | 2026-08-25 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 51951fb0-ec41-372b-b9ad-742cad582101 | -3.5222 | -48.168 | 2026-08-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 8e8bb17f-82eb-332d-8528-a6d24f105f50 | -7.0058 | -59.2382 | 2026-08-25 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 8e1fa220-1ec3-3f24-b8c8-20aca6c65c6a | -11.4494 | -44.5353 | 2026-08-25 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c5e571bf-a21d-39f3-b1b0-557050e30390 | -7.3287 | -64.7039 | 2026-08-25 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 190.5 |
| f06d1875-2502-32aa-b0bc-61ca38375364 | -8.616 | -54.7339 | 2026-08-25 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b5eaa121-529b-3f58-af6e-a1c4f58f2ba2 | -4.0552 | -48.963 | 2026-08-25 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9f7a7e87-4d71-3aa0-9084-28a15d9d262c | -7.3288 | -64.6852 | 2026-08-25 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 319baaa5-41aa-3265-a2c7-cdacb5eba216 | -7.2474 | -45.846 | 2026-08-25 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 237.1 |
| be278b2b-ef7c-3d03-a0a9-549be7906f7e | -7.2659 | -45.8668 | 2026-08-25 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 39ddc8ac-daf6-3955-906c-72f2976e1588 | -7.2664 | -45.8218 | 2026-08-25 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 2a7e1625-28fd-3b8b-adde-fb20064f852e | -10.3918 | -45.0512 | 2026-08-25 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 9775a8fb-c50f-3a12-8185-4fbd44cddcbc | -10.3723 | -45.0767 | 2026-08-25 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 261.3 |
| ad995b0c-a423-38d8-a614-abd640a25858 | -7.4286 | -43.1182 | 2026-08-25 00:10:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| 48d8c347-ea72-3467-8977-51cdaeb14dba | -6.641 | -58.4987 | 2026-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 256.0 |
| d5d4407c-0e11-3665-bca2-034e0a0441d0 | -3.5406 | -48.1889 | 2026-08-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 64175f0a-e62a-3583-b974-1b634265aceb | -8.5973 | -54.7352 | 2026-08-25 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 532920fc-1584-3406-9d65-f386c4071714 | -7.3104 | -64.6858 | 2026-08-25 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 25226be9-75de-39ca-bb7c-524b7c690444 | -7.2858 | -44.0644 | 2026-08-25 00:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b71e5f6c-09aa-3a2f-b8fc-5368add64d71 | -6.8191 | -59.6119 | 2026-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| a4807b52-1807-3a92-9364-334b8755072a | -6.8192 | -59.5927 | 2026-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 4fcd8d4d-5359-30b6-bee6-00bf4814ccef | -6.8008 | -59.5934 | 2026-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 91d52a4e-b2b8-3fda-8e0a-dcd268237482 | 2.5983 | -60.697 | 2026-08-25 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3af0a66f-c03c-37c2-abc0-0c8386f8421f | -11.4302 | -44.5382 | 2026-08-25 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 97429f39-e4ba-3972-ac1f-309816dfd492 | -7.3287 | -64.7039 | 2026-08-25 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 1e878ec3-8b80-3bc4-8e9c-e2f9a164823d | 2.58 | -60.6973 | 2026-08-25 00:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| d9bb3670-8c1d-36d3-9bfe-158b44466899 | -11.4494 | -44.5353 | 2026-08-25 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4e5ef388-266f-322f-96e7-a965a2d7ab0b | -7.2661 | -45.8443 | 2026-08-25 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 181557f8-854d-3bc3-998a-1a001662ad46 | -7.3288 | -64.6852 | 2026-08-25 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| e0300d2f-df87-391f-a110-b75430db8b15 | -7.0058 | -59.2382 | 2026-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 44c720bf-2152-387e-9c88-69f4b3e4f7a7 | -3.5222 | -48.168 | 2026-08-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| eda10d8d-9f78-322e-88b4-018f5b9bf565 | -7.2901 | -45.3683 | 2026-08-25 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2482bb0c-7561-3ff1-ad77-c2ab2853d54d | -10.3731 | -45.0306 | 2026-08-25 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 346fdc60-b52b-3d18-a027-3d1c3146c44c | -7.267 | -44.0662 | 2026-08-25 00:10:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| a97bf502-b1f4-382a-9833-e3f0fe0d84cb | -8.616 | -54.7339 | 2026-08-25 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 425e8a74-3b65-334b-beea-eafa30a327c2 | -3.5221 | -48.1896 | 2026-08-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 013ca5f0-7a8e-3b87-8a9b-a375a30e4032 | -7.2525 | -45.3717 | 2026-08-25 00:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 58b6def6-d080-38ac-a244-0d14f52eb1c7 | -6.1477 | -57.702 | 2026-08-25 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 71206ebe-62d9-3edd-b51e-63405c219054 | -7.2471 | -45.8685 | 2026-08-25 00:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 8077f2da-64e9-3e22-8558-dbddb8e92af4 | -6.6227 | -58.4801 | 2026-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 240614ee-4a63-3944-98cc-81e67d9d58bf | -12.7797 | -44.2576 | 2026-08-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 8886b95d-d588-3141-bc1c-2289ffd42e1b | -10.3727 | -45.0537 | 2026-08-25 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 584.4 |
| 461161f6-694d-3c6c-aa16-9fc99b7d8b33 | -12.7792 | -44.2812 | 2026-08-25 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 4c74f01b-f9ba-34ea-aeb0-69e710662a7c | -8.0695 | -44.6552 | 2026-08-25 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d7b0d9b1-a0dd-3a7e-b13e-632ffc5cf71b | -6.1743 | -53.4834 | 2026-08-25 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |


[Clique aqui para ver as próximas entradas](README2.md)
