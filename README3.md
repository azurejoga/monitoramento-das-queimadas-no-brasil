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
| 09572030-f814-34e1-8943-cd5182496f50 | -3.66642 | -45.91248 | 2024-10-27 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 1b576170-4c57-3cfb-b6ef-1e25e44a1d71 | -3.66387 | -45.90739 | 2024-10-27 00:09:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 25cc9806-cff5-348a-80b8-87ca499564d1 | -3.46409 | -45.65817 | 2024-10-27 00:09:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 5cc9ee86-4f5c-3772-8e33-efa8b007ab9c | -3.46096 | -45.41258 | 2024-10-27 00:09:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 4b98e149-2dd7-3ca2-afc2-1ee6bcc3d435 | -3.45456 | -46.35738 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f8ba279d-1caa-3fdd-8c56-3c56b980a7a8 | -3.44924 | -46.35116 | 2024-10-27 00:09:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 08765109-abde-382d-8e6a-1f5398c7b964 | -3.37335 | -44.39737 | 2024-10-27 00:09:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 120bbd17-5bdc-3c24-86c4-479defd2a30f | -3.19376 | -45.79581 | 2024-10-27 00:09:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 27.9 |
| f78adcd7-d98c-3b87-b612-f7d2941b18f2 | -3.17973 | -45.80472 | 2024-10-27 00:09:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| de0d5a1d-c041-36f9-bf1a-210d62567d69 | -3.17885 | -45.79794 | 2024-10-27 00:09:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 46.5 |
| acbc1fda-72cb-303c-aebe-1ee3868d0e96 | -3.11516 | -44.99052 | 2024-10-27 00:09:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 90e62f5e-e6ac-3adb-9b57-a1df2e99fa17 | -3.11192 | -44.96662 | 2024-10-27 00:09:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c7f24ba8-da6e-3266-b326-4f53bc9f4e7f | -3.10927 | -45.40392 | 2024-10-27 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c9ed7d7a-c5c0-3319-b71a-7c446162b681 | -3.09692 | -45.39869 | 2024-10-27 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 0bb33923-2269-3667-b184-124598fe42f6 | -3.09481 | -45.40579 | 2024-10-27 00:09:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 1092aa89-462f-312b-a8d0-606256e101fc | -3.08677 | -45.67701 | 2024-10-27 00:09:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| fdb32128-4f58-3dd9-a64f-56e6245fe02f | -3.08315 | -45.64974 | 2024-10-27 00:09:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 186.2 |
| e7c4edff-133f-3ab1-9df9-52dc7f792b5c | -3.0826 | -45.65527 | 2024-10-27 00:09:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 6b304826-75ef-3d1b-a39b-66a22e5fc040 | -17.6231 | -39.918201 | 2024-10-27 00:10:20 | METOP-B | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 42690fd7-53e1-3d63-837b-51b638742672 | -17.5301 | -39.457401 | 2024-10-27 00:10:20 | METOP-B | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 543853d2-34ba-3c34-83d1-1099ac509af6 | -17.5203 | -39.459801 | 2024-10-27 00:10:20 | METOP-B | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 248799d5-2e31-3243-a78c-359fec6278df | -17.594999 | -42.304401 | 2024-10-27 00:10:29 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5009aac8-0ca2-3a8a-b90b-2206aeeae275 | -16.125999 | -40.600201 | 2024-10-27 00:10:47 | METOP-B | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d71dcfc-b72a-321c-912a-38bd6b9777eb | -17.2367 | -46.736599 | 2024-10-27 00:10:49 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a74d52b-9cbb-31f5-aff8-5aac878902f8 | -17.239 | -46.749001 | 2024-10-27 00:10:49 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fcbc1d04-b7ca-3608-a03b-c87950d93fbe | -17.2269 | -46.738602 | 2024-10-27 00:10:49 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9caef837-4733-3adf-8d92-84bf8ea2c1e1 | -17.2292 | -46.750999 | 2024-10-27 00:10:49 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 47f5699f-4ca4-3a8c-96ac-2362f7a945c6 | -2.93015 | -45.40683 | 2024-10-27 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 1451677d-242f-302e-81e6-dc8fd4041f0a | -2.9279 | -45.41356 | 2024-10-27 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7d98fd18-a1f1-3542-b12a-a864b2d15533 | -2.87812 | -45.01012 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9eae6f03-1a56-331d-acca-f656a8c2b3bb | -2.87301 | -45.01735 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 86105ae3-d530-3b6f-aafb-8712b6bafeb9 | -2.8697 | -44.99352 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 278.3 |
| cf1dbeab-6d83-3874-971b-2398d960ba9a | -2.86418 | -45.0121 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 983.5 |
| 79a31b50-aa3c-362b-bc03-2d75afc924a9 | -2.86107 | -44.98826 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 804.4 |
| cec6642a-3a47-3716-ae76-97ad30c87c85 | -2.85928 | -45.44947 | 2024-10-27 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0330ca43-9b11-3de6-9341-1c61610f2bd6 | -2.85906 | -45.01927 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 376.6 |
| 455179ee-32af-3510-83b1-be8d17822669 | -2.85721 | -45.45512 | 2024-10-27 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| cebe3e70-738f-3c01-a76c-8c03b9d53155 | -2.85578 | -44.99545 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1025.6 |
| cb51a962-a583-30c2-a448-e3fcf8fb7777 | -2.85373 | -45.86562 | 2024-10-27 00:11:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 9365dee3-4d13-35fa-bc83-cfd664c14ae6 | -2.49338 | -48.0485 | 2024-10-27 00:11:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| d2f34cc2-ef76-367e-acdf-7c71aa398655 | -2.49271 | -48.05391 | 2024-10-27 00:11:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 209d8ea4-81d7-3f71-a72f-32725e88801a | -2.47275 | -45.86323 | 2024-10-27 00:11:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 768d3b22-0e4c-3af3-b6ec-8ae057f62fdd | -2.47255 | -45.85681 | 2024-10-27 00:11:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2953eaac-d6ec-3d33-b64c-9ec2ea2ef25f | -2.46887 | -45.82937 | 2024-10-27 00:11:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 99a457bc-e54f-386a-8b17-ad694b154a6d | -2.46886 | -45.83587 | 2024-10-27 00:11:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 8a57e444-4d21-3027-ba1b-40bc29bd57cf | -2.36915 | -47.66774 | 2024-10-27 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 1fc1ace6-0c77-377e-a203-285f84f0c6a7 | -2.36561 | -47.67477 | 2024-10-27 00:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 16aa694b-c72a-3096-ae1e-ca64ba07723f | -2.17227 | -47.94416 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 9e9ddd06-6033-3320-bdc3-f101a037c30b | -2.17057 | -47.95146 | 2024-10-27 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 1b688723-5e93-39dd-82d2-c27fb659857b | -1.80466 | -46.40924 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 006544b7-80ea-31e0-987d-ffca2d4c87bc | -1.80139 | -46.40289 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 77738d6f-7a3f-30dc-bfc2-96f744a2c13c | -1.80043 | -46.37955 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 78e264b9-a81d-386e-b28b-2550213aa174 | -1.79739 | -46.37323 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 405a52ab-323c-38b5-8f95-f24c19b26f84 | -1.78934 | -46.41122 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 84fbae8b-b3e2-3ae5-9fed-ca2325acc663 | -1.78607 | -46.40488 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 39d0f72a-c45d-393a-a4f3-d71d7acfdfac | -1.78515 | -46.3816 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 1a60906c-f43c-3093-9b86-f33e5a94eb10 | -1.6714 | -46.55507 | 2024-10-27 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| bf88cbb0-9275-3f8a-a767-264ffe08eca9 | -14.2368 | -43.068298 | 2024-10-27 00:11:26 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3e2d73f4-1c8a-3093-9a3b-6a45c42080ec | -14.2384 | -43.075699 | 2024-10-27 00:11:26 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 04785ae9-c6b5-354a-9db4-72ccfba3466b | -14.272 | -43.232498 | 2024-10-27 00:11:26 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 01a34b0a-49a0-33ce-a91f-d0da9b39925b | -14.2736 | -43.240002 | 2024-10-27 00:11:26 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c13fe14b-579e-3204-a2e6-577eff263c76 | -14.2752 | -43.247501 | 2024-10-27 00:11:26 | METOP-B | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aa447b6f-8406-3e61-9888-98af78b745da | -13.9342 | -42.9505 | 2024-10-27 00:11:30 | METOP-B | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4e89dc94-12f0-3bd9-ba68-323dcbca1e99 | -13.6731 | -41.846699 | 2024-10-27 00:11:31 | METOP-B | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f0874d27-0847-3d2f-8ff5-e53702074c9d | -13.6747 | -41.853802 | 2024-10-27 00:11:31 | METOP-B | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b3f939b0-0d87-3557-855f-4f76928c06cc | -13.8282 | -43.221802 | 2024-10-27 00:11:33 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b0341260-d793-3332-af8f-5d5937c9b842 | -13.4758 | -42.4482 | 2024-10-27 00:11:36 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8cef1800-d03f-3dda-9a59-21803d0aaef6 | -13.4774 | -42.455299 | 2024-10-27 00:11:36 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 251e1c82-6c02-3d90-b831-6b0b2357fe9b | -13.479 | -42.462502 | 2024-10-27 00:11:36 | METOP-B | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0822945b-ace3-3a5b-ac6e-012c05c5a3ae | -12.6733 | -39.297798 | 2024-10-27 00:11:38 | METOP-B | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d8d8845-3bef-3ad9-a24d-e4f012e72c34 | -12.6751 | -39.305599 | 2024-10-27 00:11:38 | METOP-B | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9a325b4d-559b-3adb-83ba-bebb1501c3e6 | -13.4778 | -42.930302 | 2024-10-27 00:11:38 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9d5b1023-9455-3216-a069-fd3593a0158e | -13.4793 | -42.937599 | 2024-10-27 00:11:38 | METOP-B | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 22e5ad01-37ba-3263-b6e1-ec2a221a8430 | -13.3748 | -43.645 | 2024-10-27 00:11:42 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3fe29cb-3622-3adc-a03a-2a8ce945a7ff | -13.064 | -42.118801 | 2024-10-27 00:11:42 | METOP-B | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2cc3e730-2472-311a-aa57-f3b0a80d0368 | -13.0656 | -42.1259 | 2024-10-27 00:11:42 | METOP-B | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 13d5c176-a019-34b6-a76d-54d84f9f9ef9 | -12.9238 | -42.276299 | 2024-10-27 00:11:44 | METOP-B | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b2f4bcf9-3371-366c-a65a-8166c917cbc6 | -12.3097 | -40.1833 | 2024-10-27 00:11:47 | METOP-B | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9f4ce70a-50f2-33a7-9a5a-1bf7fd7e5f26 | -13.3748 | -45.102501 | 2024-10-27 00:11:47 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5af264ac-6125-30b5-ac01-ae1b6c01e268 | -13.3766 | -45.111301 | 2024-10-27 00:11:47 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17be2d68-1536-3d3b-a470-24e72ed2c7e2 | -13.3784 | -45.119999 | 2024-10-27 00:11:47 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0267d339-099c-3b79-ba94-265d94a21b57 | -13.3803 | -45.128799 | 2024-10-27 00:11:47 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00fd7241-b293-382d-beaa-7a834fb6674c | -13.365 | -45.104599 | 2024-10-27 00:11:47 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 014afbf9-9ed8-3340-a645-18c26e25420d | -13.3668 | -45.1134 | 2024-10-27 00:11:47 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3098ff3f-380f-3a38-8a3b-3967ecaabfbe | -12.1212 | -40.351299 | 2024-10-27 00:11:50 | METOP-B | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bf87af0a-a4c5-302f-b768-ed55a4f49e1a | -12.8983 | -44.5881 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3c29a61-2057-35b3-a414-191dca32e295 | -12.9 | -44.596298 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a63fc87f-4dde-339a-98e8-2e34d71c2709 | -12.8885 | -44.590199 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 480ddc40-87c1-36f6-aec4-223d9e3806c8 | -12.8902 | -44.5984 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adad4d50-53bb-3c5b-a4da-abf424317f9e | -12.8919 | -44.606499 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 66a91337-3add-37ac-98c8-a0212b0c241e | -12.8787 | -44.5924 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55039428-f13d-3800-ad54-cd5130539242 | -12.8804 | -44.600498 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0d0ce1-94d3-3c75-a393-e53c4ebe8888 | -12.8821 | -44.6087 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64a15d55-3e5e-3297-a7eb-2fe6682e7642 | -12.874 | -44.618999 | 2024-10-27 00:11:53 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 356a963c-8e67-3f3f-8524-6767a6ddacc5 | -12.3915 | -42.663399 | 2024-10-27 00:11:54 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4c3491c2-4d5a-37f1-a4b7-25fa96f69aa8 | -12.735 | -44.156399 | 2024-10-27 00:11:54 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4697e8a6-3eea-38a9-96ac-d2e97357d57e | -12.7366 | -44.1642 | 2024-10-27 00:11:54 | METOP-B | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3356926d-c5f7-3233-8b19-be25c5b3f33e | -12.2094 | -42.771301 | 2024-10-27 00:11:58 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a42b0ece-882b-3ce6-9410-ff0af7275ce4 | -12.211 | -42.7784 | 2024-10-27 00:11:58 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e8f48ef8-c67c-3d53-950d-8e3987cdf554 | -11.5245 | -40.765202 | 2024-10-27 00:12:02 | METOP-B | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
