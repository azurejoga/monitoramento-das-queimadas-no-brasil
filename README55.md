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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24f77cd6-47ef-37dd-9a5b-5c3d07f038f3 | -21.9374 | -48.5688 | 2024-09-26 03:47:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 120.3 |
| c6aa1719-5455-3aca-9d8e-c8608040967c | -22.2162 | -47.5603 | 2024-09-26 03:47:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.2 |
| 4edcf162-818d-30e4-aff0-ffd95211b0e1 | -2.6785 | -57.531 | 2024-09-26 03:55:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| bc136dc6-c0bc-3e83-9778-078cd07babd1 | -2.6968 | -57.5307 | 2024-09-26 03:55:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 0f84cef3-6cc2-3335-a25d-c1da96081f54 | -3.5673 | -50.3794 | 2024-09-26 03:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| be909b1d-f066-3c72-bcf0-b0cceaf98af0 | -3.9208 | -46.4459 | 2024-09-26 03:55:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d9f54a6b-588c-3019-bd12-bcddce4529a7 | -6.949 | -63.1048 | 2024-09-26 03:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.0 |
| a565e173-0e93-3530-b4cb-068a187ac7c3 | -6.9489 | -63.1236 | 2024-09-26 03:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| a7d5a026-a981-30bf-b005-c23620c7c5ff | -6.9306 | -63.1053 | 2024-09-26 03:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 5de1fadc-1487-3230-9d6a-bfbf36bab31f | -6.9305 | -63.1241 | 2024-09-26 03:55:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| b10d1307-ef31-372d-a2e1-0333e053e13a | -7.3824 | -55.4924 | 2024-09-26 03:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 79682e20-2447-3daa-b83e-5e4ffadae24c | -7.3823 | -55.5124 | 2024-09-26 03:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 70000ad2-99f2-32fd-861a-01099ebd216f | -7.3639 | -55.4935 | 2024-09-26 03:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| aec82262-c5e7-301d-9921-673d0a785b73 | -7.3637 | -55.5134 | 2024-09-26 03:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 296.6 |
| 903bde28-957f-396f-8c90-56c84603be4c | -7.3636 | -55.5334 | 2024-09-26 03:55:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| a3fa3bee-aefb-311e-a957-9cf6d51c2da9 | -7.2905 | -61.106 | 2024-09-26 03:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| c659173a-c1f3-3fb7-859d-e0fc9c9d35b4 | -7.8156 | -54.7252 | 2024-09-26 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.9 |
| f4d32e81-fc45-35b0-bfc7-79683477a620 | -7.8154 | -54.7453 | 2024-09-26 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| c8834f7b-dd2b-3024-8808-55cd39fa1fda | -7.797 | -54.7263 | 2024-09-26 03:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| fe1e147e-1fd0-36d8-8324-09fa83f74f83 | -8.1394 | -61.2817 | 2024-09-26 03:55:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 05e93249-adf9-34a0-9fd8-c8af9e3f12a0 | -8.3155 | -54.9956 | 2024-09-26 03:55:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 4aa818d0-6a2d-3c86-b788-719282471af9 | -8.8098 | -58.2172 | 2024-09-26 03:55:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d322c2cd-83e3-3b91-8abb-80285d8e366d | -9.1046 | -61.1237 | 2024-09-26 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e49a1174-17a8-356b-ac61-628abd88f815 | -9.086 | -61.1245 | 2024-09-26 03:55:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b85d5af0-8958-3e19-b93c-cb625913f877 | -10.0515 | -53.4432 | 2024-09-26 03:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 90ebefde-7668-3c17-ac33-93b3d54d927e | -10.0513 | -53.4638 | 2024-09-26 03:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 6dff5692-fda1-3857-a317-8eef39aedb9e | -10.051 | -53.4844 | 2024-09-26 03:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 00624b6f-c9e1-383f-81bc-57be9e30eb87 | -10.0327 | -53.4448 | 2024-09-26 03:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 8b04dc79-60ca-3752-bfdc-f14fa8c07711 | -10.0324 | -53.4654 | 2024-09-26 03:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 427.2 |
| 0deac1e7-7ded-389f-96d1-158214ea6d86 | -10.0322 | -53.4859 | 2024-09-26 03:56:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 200.9 |
| 46b9dcd8-425b-384c-801a-d39c5baff041 | -11.222 | -45.536 | 2024-09-26 03:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| c0b3b921-7627-31c3-8889-59864129d24e | -11.2029 | -45.5387 | 2024-09-26 03:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 74f1da0f-f58c-3d70-a656-4d716bf2178f | -11.212 | -51.1627 | 2024-09-26 03:56:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f7a8775b-7f86-3dd0-9e6c-520e487f37fb | -12.2367 | -45.5045 | 2024-09-26 03:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.4 |
| a576c9f6-abaf-3f4c-a135-49e2aebcf29b | -12.2175 | -45.5074 | 2024-09-26 03:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 7be6797f-462b-3d6a-839d-0fb61c362be0 | -12.217 | -45.5305 | 2024-09-26 03:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| fb993af3-797e-3e02-98fa-edfdd69d62cf | -12.5467 | -53.494 | 2024-09-26 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| e6db9025-a260-3497-8a4c-46e705678bae | -12.5276 | -53.496 | 2024-09-26 03:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0850e706-d977-3fcf-ba3d-a4ad394665cf | -12.5026 | -48.9198 | 2024-09-26 03:56:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2e8843ae-be30-313d-9146-83955068a72f | -14.9022 | -51.4749 | 2024-09-26 03:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| fde312e1-70e3-32c3-8356-3fe915abde45 | -14.9018 | -51.4965 | 2024-09-26 03:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 78259096-d37b-3e02-90a7-85b6a8fb9c76 | -14.8828 | -51.4777 | 2024-09-26 03:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 202.4 |
| d115aaf9-5c08-3f07-88b1-b436265efb8f | -14.8824 | -51.4992 | 2024-09-26 03:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 280.8 |
| 572a083c-8cc4-37b0-a751-4b8cc7c727d3 | -14.8634 | -51.4804 | 2024-09-26 03:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 46d7078b-0e96-3c5b-8859-67a632aeb791 | -14.863 | -51.5019 | 2024-09-26 03:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 3c9154b0-f2e4-34e3-9fc4-dc80cc2dcd99 | -16.1185 | -51.9651 | 2024-09-26 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4c91ca0e-0c4d-3a6a-8511-96a022334fc7 | -16.118 | -51.9867 | 2024-09-26 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 265.9 |
| 157f5a24-c71e-36ef-a0f6-ce52e9fa02d9 | -16.1176 | -52.0082 | 2024-09-26 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b64d375a-4b51-33ae-9b71-22da6cfea3c5 | -16.0989 | -51.968 | 2024-09-26 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a882100f-e315-3102-9f6b-92120972d334 | -16.0985 | -51.9896 | 2024-09-26 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 208.3 |
| 6ac3adea-5a6e-3b9e-a330-a72d0102cf1c | -16.098 | -52.0111 | 2024-09-26 03:56:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 31c41e1a-d780-3473-aa09-f23e4c6a0021 | -17.0995 | -56.1504 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| c6d077a6-31c2-3877-899a-30823bd376d3 | -17.0991 | -56.1711 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 44.8 |
| d3df74e7-b5d9-3ee5-a242-1986ba024741 | -17.0798 | -56.1529 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| d6125726-0271-3e77-be0c-7f3dcbcecca8 | -17.0795 | -56.1736 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 815b1df4-cab2-3257-b9db-5445f430b12b | -17.0402 | -56.1785 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.3 |
| e9a99557-a101-302f-b8aa-b315d35e650d | -17.0398 | -56.1993 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.4 |
| 3e21215b-55a7-351f-8852-a755de9b73e9 | -17.0205 | -56.181 | 2024-09-26 03:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| ab0889c2-d2d3-3773-8598-956b9e8099ab | -20.608 | -51.4986 | 2024-09-26 03:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| 10ebce47-0f0b-33e9-be9d-2f80989ede7d | -20.6074 | -51.5209 | 2024-09-26 03:57:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.0 |
| 8d803220-3e52-3a79-afbd-a3b8618d569d | -21.9381 | -48.5453 | 2024-09-26 03:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0e075402-7658-36bf-b2ba-b4bbfe819c9b | -21.9374 | -48.5688 | 2024-09-26 03:57:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 712344d4-75b0-3165-bfb5-d8b48e3e923c | -22.2162 | -47.5603 | 2024-09-26 03:57:08 | GOES-16 | CORUMBATAÍ | SÃO PAULO | Brasil | 3512704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| b2b2fb1d-4bc0-3acf-ac64-acc76e659642 | -3.36413 | -41.21363 | 2024-09-26 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 219d9182-489b-3d87-8270-eb9153ac8fd1 | -3.03241 | -40.7099 | 2024-09-26 04:04:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 03703eb3-1cf0-3a80-9af2-0392b28aaff2 | -3.51482 | -42.00175 | 2024-09-26 04:04:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ab0ed002-fafa-328d-be35-aedda708991d | -3.95106 | -41.69067 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92c440a7-feae-3b5b-9644-8a14dcdca28f | -3.94773 | -41.69015 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1794f7f-7dcc-392a-8cc7-2eb85251a62b | -3.92393 | -41.71513 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45a0c17a-91ed-325c-8705-7062510867ad | -3.79764 | -41.58809 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f04802c3-6f42-3636-90b0-c0412b99e53e | -3.79709 | -41.59157 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1b517783-7089-3ec4-80b8-dd4830261915 | -3.79653 | -41.59505 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c28f8c6f-6042-3bfa-9977-bc2f21069ae8 | -3.79598 | -41.59855 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 42d23d13-6c0b-3071-b71b-135aec849c63 | -3.79431 | -41.58755 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| a0b17558-4d18-3b33-9c75-2220fbad0e88 | -3.79376 | -41.59104 | 2024-09-26 04:04:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| eb4e5e18-a95c-3a07-9e48-0e0508bf0c17 | -4.84789 | -43.03366 | 2024-09-26 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd2506b6-dd0e-3d66-9574-84366b2a0bef | -4.84729 | -43.0374 | 2024-09-26 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6c67e75-7781-3ca7-9b0c-dd07b26f7b5d | -4.84446 | -43.03311 | 2024-09-26 04:04:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62462985-4aa8-347b-b764-f5fdbe96d639 | -4.36188 | -43.02813 | 2024-09-26 04:04:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04b50e82-e277-3825-868d-a21ee6b63916 | -5.95297 | -42.56711 | 2024-09-26 04:04:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 80a65467-1efd-3e01-9b18-43294524104a | -5.94961 | -42.56657 | 2024-09-26 04:04:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a27e3193-9a85-3ad0-88a6-6af87be4ecd8 | -5.94904 | -42.57014 | 2024-09-26 04:04:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1701d40c-dc33-3016-962d-e4cea2fb7d9f | -5.75236 | -42.62355 | 2024-09-26 04:04:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1e6e20d-d5ec-3a3f-8042-ab7798985f30 | -5.74899 | -42.62306 | 2024-09-26 04:04:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67f6f32c-edbd-31a9-99b0-871a2e04b3db | -5.54518 | -42.97132 | 2024-09-26 04:04:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b902100-b238-3225-a686-5fc968d2ac8f | -5.54459 | -42.97501 | 2024-09-26 04:04:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d62e0ef0-1f34-34e3-a9bb-3f0991bd1180 | -5.52589 | -42.76553 | 2024-09-26 04:04:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 82edf28f-9933-3e24-a65c-d60b7585cf9b | -5.52029 | -42.75718 | 2024-09-26 04:04:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9803b8b5-7d03-3440-a50a-7d2c35447f39 | -5.3554 | -42.77621 | 2024-09-26 04:04:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18d8e5fe-ef94-34b7-b3ed-93c7530f3fc5 | -5.35259 | -42.77203 | 2024-09-26 04:04:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e474ad86-46d6-39b2-b081-ef95cd59b7e8 | -5.352 | -42.77568 | 2024-09-26 04:04:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99e6b2ca-acff-32b4-8946-fe377421abc9 | -5.26165 | -42.94636 | 2024-09-26 04:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a16dabc-5964-35c9-a377-8ed42d101b06 | -5.26138 | -42.94897 | 2024-09-26 04:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3ec7dd14-4aee-30c3-9ed6-b794c9bc7c57 | -5.64876 | -43.24669 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bab7d0b2-5d8d-3dce-af71-27197e59f13d | -5.64819 | -43.24602 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fae8efb3-559a-3d00-9b88-ae7638d7912d | -5.64532 | -43.24614 | 2024-09-26 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54f75b77-78a2-3f43-bfe4-99e05c62db58 | -5.30101 | -43.0731 | 2024-09-26 04:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0fab375-994f-3868-bf56-75248aa1d26c | -6.33164 | -42.50965 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2b8012f8-cecb-3951-8b3d-ce5f98cc1324 | -6.32828 | -42.50914 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60be08d9-b10d-37c2-8015-80cf731eb9fd | -6.32493 | -42.50863 | 2024-09-26 04:04:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README56.md)
