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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdb3b637-d86d-3510-ac2f-6e6cfb5c2260 | -17.6648 | -46.67149 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ba013a58-387a-34ac-8cc1-5def826c30b3 | -17.66351 | -46.67787 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| ef1eaaf2-b3b9-342b-b2b6-5730a7b7a16e | -17.65328 | -46.67565 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6aaddae1-6f70-31e0-a4f6-6648668f1135 | -17.65518 | -46.69262 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6f54ea55-a9a8-3507-92c4-41e2f0d8132e | -19.38878 | -48.89937 | 2025-08-12 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4809ae2-e73b-33b0-9e7c-3efe395dd51e | -19.08046 | -48.14884 | 2025-08-12 03:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d367cd24-e6d7-3da0-a854-102d8f63de3b | -17.63665 | -46.67859 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 12626646-5686-3ece-843d-fc954d9d4fc0 | -18.18214 | -47.00383 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9db7dec8-a35a-3607-b50e-93fee7832319 | -17.66287 | -46.68105 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 738baf8c-4623-3a6a-96c8-e9c44e123a41 | -19.38744 | -48.90198 | 2025-08-12 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 569885f4-7c7a-39fb-8958-246b11d431b6 | -19.3378 | -44.42227 | 2025-08-12 03:49:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75ce2776-1887-3191-8162-1aa804a391bd | -17.66094 | -46.69056 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 388fb27c-ecc4-3342-9d08-2e74a637caa2 | -19.38834 | -48.89784 | 2025-08-12 03:49:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7867161d-d6c0-3bb7-a9e4-0d466e96b486 | -19.33352 | -44.42131 | 2025-08-12 03:49:00 | NPP-375D | CAETANÓPOLIS | MINAS GERAIS | Brasil | 3109907 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0077d1f7-260f-328d-8a1d-a8f37362183f | -17.66862 | -46.67899 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c7452fa4-01e4-3f79-af34-19a7ec711f97 | -17.63794 | -46.67224 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 80a2a1c6-fb32-3cbc-975f-0dcf03388f4a | -17.65454 | -46.69579 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5af919fd-8c2d-3d6a-9692-694ba3311900 | -17.64369 | -46.67025 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f30f7bd7-d6a7-34ea-8bd9-c6d411d0915f | -17.65775 | -46.67992 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 2dfc51b7-b005-35fd-931c-1e358853c0e0 | -17.6373 | -46.67542 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0e191454-f64c-3905-837f-177840b9c51c | -17.6667 | -46.68851 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50fdc3cc-0baf-3b99-a67e-d1cdb0e6f9aa | -17.65199 | -46.68198 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a3091fc9-92d6-3530-b821-c32019f69df7 | -19.29736 | -48.43659 | 2025-08-12 03:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b1eb1276-4d79-39de-8c49-8f445c9a7eb0 | -17.66798 | -46.68216 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1fa8201-2bce-36e3-9ffd-2948ba5a0fb6 | -17.64622 | -46.68406 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 342a2523-f776-3516-9ff4-e883c9074b95 | -17.65647 | -46.68626 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 39.3 |
| c590d5a3-747d-3fa9-9c45-a95d8ddf1a60 | -18.18736 | -47.00471 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a577570e-9372-3943-9f45-a346c2278161 | -19.29821 | -48.43266 | 2025-08-12 03:49:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a27a8996-0db6-3e90-b499-936ab591c9a5 | -17.6424 | -46.67658 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| dd9f4d76-49a2-3196-95e5-9f5919f231e4 | -17.64945 | -46.66822 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 547984fa-a1b6-3cad-9a20-6fb3bb5922e8 | -17.64046 | -46.6861 | 2025-08-12 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5588905f-585a-3086-9ebd-b8b0e1e4aad5 | -8.9401 | -60.7288 | 2025-08-12 03:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 8ab932b7-dc91-3bdd-92fa-c72bbfba5c2e | -12.5742 | -47.0006 | 2025-08-12 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 32570eb3-f0c1-392d-b988-5602ff43c64b | -3.9684 | -47.8901 | 2025-08-12 03:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| e78878fa-b92c-3740-a775-5114ed54feb9 | -3.9686 | -47.8684 | 2025-08-12 03:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d508298f-8453-3f2a-8a40-a811a2fc6a59 | -12.555 | -47.0034 | 2025-08-12 03:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| bed37420-2672-3b99-8553-e4fbf1ab7854 | -7.1483 | -60.1174 | 2025-08-12 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a35fe307-1d62-3f90-b1ec-4b5444901552 | -9.723 | -49.4806 | 2025-08-12 03:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 2c74a158-c389-3841-ac11-9f47a67cb0ec | -9.7041 | -49.4825 | 2025-08-12 03:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 43b7ee92-7bd2-34e0-b134-e0e1d71ae27c | -7.1299 | -60.1182 | 2025-08-12 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f15ecea4-de51-35c7-9079-c7543e28c07c | -7.1482 | -60.1366 | 2025-08-12 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 7f84da2e-7533-3ba9-aaca-af0ffccfe577 | -7.1298 | -60.1374 | 2025-08-12 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| e73deddf-0410-33c3-b2b5-47cd2aed59b3 | -12.555 | -47.0034 | 2025-08-12 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 825e9593-5142-3a07-b94d-e184e7092a87 | -17.6749 | -46.6715 | 2025-08-12 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| f47a76bb-0f4d-3f65-a7e2-5ccc42c41de7 | -16.2961 | -52.9016 | 2025-08-12 04:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 61db6abd-0d39-3c17-999b-bbab471cc0b8 | -16.2957 | -52.923 | 2025-08-12 04:00:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7e8043bd-c728-3e68-8982-165c3bf9f84d | -17.6555 | -46.6523 | 2025-08-12 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 90adb2a4-0723-3009-b856-c7ea65010e52 | -12.5742 | -47.0006 | 2025-08-12 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| d730ef32-4051-3cb9-b4cb-8b313d6ebed6 | -17.6349 | -46.6799 | 2025-08-12 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 0f773279-feb5-35b7-a1bd-848aa55ec5c6 | -3.9686 | -47.8684 | 2025-08-12 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d04a2821-d2cb-3587-9ee1-1575aad1d51e | -7.1299 | -60.1182 | 2025-08-12 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d5b22605-6a4d-300e-86ed-7f9da63710b9 | -17.6549 | -46.6757 | 2025-08-12 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 336.4 |
| bc38584a-90d6-306e-8368-b4520c4788bc | -17.6544 | -46.699 | 2025-08-12 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| b62d7f49-4b90-3327-b6b4-de32d662d1ff | -17.6355 | -46.6565 | 2025-08-12 04:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.5 |
| aa4c7041-a508-3dd2-a64b-044e22a27414 | -9.7041 | -49.4825 | 2025-08-12 04:00:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 957b4c57-91e3-37a8-8170-a63cb4d31d9b | -7.1483 | -60.1174 | 2025-08-12 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 87c7bf9a-68d0-34c0-97c3-80f762adf9f3 | -3.9684 | -47.8901 | 2025-08-12 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 1722032b-f914-394f-bed9-cefd2f6255ac | -8.9401 | -60.7288 | 2025-08-12 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d519d5c0-29e3-3228-b049-520498e5351a | -3.43245 | -49.03848 | 2025-08-12 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8df7a6dc-5324-369a-aec5-17d9a980865f | -6.58387 | -44.55913 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2fe61f39-90e5-3f02-96bd-68a531a6b1bd | -6.58321 | -44.56319 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08cca0d7-9a2a-3a00-b956-593915b96cc6 | -5.51361 | -42.62851 | 2025-08-12 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 33a90c95-6a31-3e98-89e6-680217374ac6 | -6.57832 | -44.57069 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29f16722-dcdc-3156-a4e1-505ed9405e2a | -3.83881 | -47.74533 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| abf94c8b-61e6-3b36-abc4-f9cc05fc1b78 | -4.61149 | -45.61063 | 2025-08-12 04:06:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3efb1af7-1ccd-3ab7-a045-dfed41ac34e3 | -7.06965 | -44.93284 | 2025-08-12 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab89cb41-964c-3817-9771-aa9680958bc3 | -6.57676 | -44.55792 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b0870f50-0473-3471-8f7b-dfc358e7fcfe | -4.30991 | -48.10411 | 2025-08-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 29d32305-8561-3661-9611-ee5133c8fed9 | -6.5761 | -44.56197 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef0626b1-ba5e-3bae-a039-f7374a667bc0 | -4.60081 | -43.31522 | 2025-08-12 04:06:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b682043e-1741-3062-b621-c678c98d562f | -3.83164 | -47.75059 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 27cbae5e-15d7-3898-8338-be18921ec460 | -3.17752 | -48.80827 | 2025-08-12 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38a1874c-99cb-3e4b-9274-9c94df27ffa4 | -6.59969 | -42.78643 | 2025-08-12 04:06:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 155dfcef-0f07-3862-b981-488e5a6be24d | -5.99537 | -39.30883 | 2025-08-12 04:06:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63bf5fbd-61da-3e4d-a495-4ef8cb624e93 | -6.46467 | -44.57781 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99fba570-98cd-3704-8b57-2f8dc4b45b09 | -5.85257 | -41.04424 | 2025-08-12 04:06:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ce5473d2-bd0f-3674-b4fb-33d22192c38f | -6.41516 | -42.42865 | 2025-08-12 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60d4b138-8dbe-34b8-928a-167484182d32 | -7.12728 | -44.62672 | 2025-08-12 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3e323041-255a-34d1-bb69-bc7bdd3f03eb | -5.5387 | -42.66525 | 2025-08-12 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5d722f9c-79a1-3556-89ae-75080576d262 | -7.23128 | -41.91044 | 2025-08-12 04:06:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7727189c-a149-33b1-b4ed-268530b6773c | -3.43016 | -49.04764 | 2025-08-12 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 39631328-7d16-39f4-8aab-0c26a8a366e2 | -6.58543 | -44.57196 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15cc6c20-5f3b-3753-9400-db9962510661 | -5.48203 | -44.38789 | 2025-08-12 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| dd39270e-8960-3493-9b6a-9e08e3566888 | -3.83803 | -47.74995 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ba69a3d-6929-3f4d-b5b3-1ea37c975b1c | -3.10803 | -47.01109 | 2025-08-12 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 218831fd-6ad7-351c-b41f-fdc870f17ef2 | -3.06855 | -40.8182 | 2025-08-12 04:06:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3b6539d3-1612-39ef-b881-41e7560434d6 | -3.96575 | -47.88237 | 2025-08-12 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0a7be1a1-d13e-3205-8425-f3e491433adc | -6.72601 | -43.57912 | 2025-08-12 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2a8c7698-5042-3ee0-8a1a-1b6db63ca6de | -4.31069 | -48.09938 | 2025-08-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 004c97f6-4b71-30e6-aaf6-7669978f963f | -5.48516 | -44.38335 | 2025-08-12 04:06:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 23cfb2c4-cce2-31a0-8aca-2ff3135bacf6 | -6.61293 | -43.88832 | 2025-08-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f3a171b7-9909-3a17-931d-a8caf73af493 | -4.17838 | -48.63601 | 2025-08-12 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d549383-647c-31f7-b07a-ef2dbb62b896 | -3.43107 | -49.04204 | 2025-08-12 04:06:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 539ec874-c5c0-3ccd-acca-3e33ab8dc477 | -7.20993 | -35.596 | 2025-08-12 04:06:00 | NOAA-20 | INGÁ | PARAÍBA | Brasil | 2506806 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1c7c41c3-4015-3c63-a3d0-be8ba15c8159 | -5.93795 | -39.47749 | 2025-08-12 04:06:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb67d325-37bc-33b7-b210-4c03ed752b3c | -6.58676 | -44.56382 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a402181-bf76-3031-8fa3-b041c4e77ae9 | -7.30357 | -39.63937 | 2025-08-12 04:06:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 668735dc-1e4b-3766-a78f-60adaf1ef15b | -6.61355 | -43.88451 | 2025-08-12 04:06:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4cd38950-1fc5-3604-bae8-94cad15ad846 | -6.464 | -44.58189 | 2025-08-12 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb415adc-58b4-3c8d-b34a-15783165b85d | -6.21986 | -43.32477 | 2025-08-12 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |


[Clique aqui para ver as próximas entradas](README13.md)
