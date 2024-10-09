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
| 11a6f645-3af3-356f-9c0c-fff2aa778cf2 | -22.15 | -48.16 | 2024-10-09 00:03:17 | MSG-03 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a11417e2-21e2-3fbe-b7cd-e0dc873a215d | -21.62 | -47.75 | 2024-10-09 00:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b4707592-71b1-32f7-ae10-1ee662ee6e66 | -21.62 | -47.7 | 2024-10-09 00:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6920fac5-21be-3917-9ca8-2f9cbc8a5fec | -21.65 | -47.77 | 2024-10-09 00:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bbc5d434-23e6-3216-b51f-70068fe3a41d | -21.65 | -47.72 | 2024-10-09 00:03:20 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9253d302-9766-3da2-a9f5-e9d27766bef1 | -21.82 | -49.17 | 2024-10-09 00:03:20 | MSG-03 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| df2268cb-e43b-3334-bea4-623ef7098800 | -20.33 | -48.73 | 2024-10-09 00:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 99479da6-edc3-3c64-9b7f-e72991f648e3 | -20.37 | -48.8 | 2024-10-09 00:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4e13d921-cbdf-33b6-a8d3-5d3ae3636dfb | -20.37 | -48.74 | 2024-10-09 00:03:28 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| be6f5e49-3edd-3893-acaa-741db83190ab | -17.12 | -57.49 | 2024-10-09 00:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6777c9a8-708e-3c50-a50c-ded066803bf0 | -17.12 | -57.42 | 2024-10-09 00:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 482a1850-98ec-3e58-bb61-87e6ab4dc65d | -17.12 | -57.34 | 2024-10-09 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31636851-ea57-3d5e-85dc-25036db62f0e | -17.15 | -57.44 | 2024-10-09 00:03:49 | MSG-03 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 92a1283d-b56e-3bb5-a60f-cf37b727ccca | -17.15 | -57.36 | 2024-10-09 00:03:49 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 375591e7-7c4a-33cc-8215-8d4aa267dc4d | -12.01 | -51.08 | 2024-10-09 00:04:15 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f49320b-6893-3e36-8c72-191b75545c77 | -10.65 | -55.93 | 2024-10-09 00:04:26 | MSG-03 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c819fc7-8028-3a43-938a-be81d8c4f9f9 | -1.11 | -53.6173 | 2024-10-09 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| c97c6e9b-db91-3064-98b6-8d8d9b3e4695 | -1.1101 | -53.5972 | 2024-10-09 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| d648fba0-be9a-30ae-8362-e8c952499927 | -1.1284 | -53.6171 | 2024-10-09 00:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 011bacf9-cecd-3f64-b79a-2eb3ad4bc0c5 | -1.9609 | -50.8404 | 2024-10-09 00:05:17 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 5b55e9bc-826d-3a74-b16d-84b31ef087ed | -2.4787 | -50.2438 | 2024-10-09 00:05:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e38095b7-6163-3c2b-939d-845d931401be | -2.9829 | -53.7267 | 2024-10-09 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9b5a5338-3cf2-3e50-b4c4-2458171998c2 | -2.983 | -53.7065 | 2024-10-09 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d7acea34-411d-3457-bd1a-51e927e7ee29 | -3.8007 | -41.6229 | 2024-10-09 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.9 |
| 1e075842-174a-3863-bdb6-58d2ef787612 | -3.8008 | -41.5989 | 2024-10-09 00:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| dba2336e-aa34-39ec-8937-0234599667ed | -3.6978 | -50.1225 | 2024-10-09 00:05:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b896421b-25dd-36ac-9d65-d014c68278d6 | -3.8194 | -41.6219 | 2024-10-09 00:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| a0fe383d-2ac9-308a-b326-4d7b13d18e89 | -3.8196 | -41.5979 | 2024-10-09 00:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 981899f3-9d2c-3731-9313-4145d25f67d1 | -3.8119 | -49.4841 | 2024-10-09 00:05:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 29a2bf9a-16f0-310f-b751-88cef1e11cf3 | -3.9021 | -46.4689 | 2024-10-09 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 49a42b75-2c93-3bf1-b91d-cb16ebd61398 | -3.9023 | -46.4467 | 2024-10-09 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 7481269a-dae5-3762-9203-ee68cfb225ca | -3.9207 | -46.468 | 2024-10-09 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 774271a2-188c-3b4f-b520-63a2a13b5ce0 | -3.9208 | -46.4459 | 2024-10-09 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| a3861db6-93d3-3c80-b119-c95e90b3dc1f | -3.9394 | -46.445 | 2024-10-09 00:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 847416a0-ef3b-35e7-b2ca-5d75661b497c | -3.9495 | -47.9559 | 2024-10-09 00:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 886e0677-5607-3888-8ac2-df6423a58e66 | -5.2253 | -43.8164 | 2024-10-09 00:05:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 3e7d8418-1ba7-3523-a272-cc6905eadc19 | -5.2441 | -43.8151 | 2024-10-09 00:05:36 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 93e2379e-86b5-3016-9123-3ae9cd11c3d6 | -5.8216 | -44.1196 | 2024-10-09 00:05:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 73741c0c-5bc3-3b86-b0af-9cc38bca03ef | -5.8617 | -48.1571 | 2024-10-09 00:05:39 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d3310c83-94d5-36fe-a16a-7deb0052561e | -6.0041 | -44.6333 | 2024-10-09 00:05:40 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 0b50b7a6-33a5-3c71-8613-b2caacb76073 | -6.1599 | -44.001 | 2024-10-09 00:05:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| a15326e8-7d0c-330a-93f5-438695c87195 | -6.48 | -49.918 | 2024-10-09 00:05:43 | GOES-16 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 761dd51a-af9e-3d29-b744-43445c066b01 | -6.4986 | -49.9168 | 2024-10-09 00:05:43 | GOES-16 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| d592142e-f5a5-3e30-98d3-21d9c6f141f4 | -6.5308 | -58.4257 | 2024-10-09 00:05:44 | GOES-16 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| afac8753-ed33-3ab0-9e20-7a089f2051e5 | -6.5309 | -58.4063 | 2024-10-09 00:05:44 | GOES-16 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| f6e2c6f7-a3cb-3176-a412-9bb21e89f1db | -7.0231 | -59.4303 | 2024-10-09 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 7880e230-99ba-33ef-9e1e-b15382d5fdb8 | -7.0232 | -59.4111 | 2024-10-09 00:05:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4992897d-404e-348b-bdf2-857f952140ea | -7.0417 | -59.4103 | 2024-10-09 00:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.0 |
| de5f74be-64e9-38b0-881a-cace46998251 | -7.2435 | -59.633 | 2024-10-09 00:05:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 5936f79e-69e6-3e4e-a3c6-bbe54f566c32 | -7.3473 | -64.6661 | 2024-10-09 00:05:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 75a953cd-4974-3a74-9739-16dee1af8669 | -8.4919 | -48.6476 | 2024-10-09 00:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 211.4 |
| a595b8ca-b653-3b8b-bb34-634487d4ff86 | -8.4921 | -48.6259 | 2024-10-09 00:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 7f239bc0-a7b5-3586-8bf2-2575d8caec7a | -8.5107 | -48.6459 | 2024-10-09 00:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9b11900e-e51c-39f0-a061-ff946785af57 | -9.0543 | -63.2375 | 2024-10-09 00:05:58 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| fe4d81c2-21ae-3747-b41c-108d708166e3 | -9.1044 | -61.1428 | 2024-10-09 00:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 090a42e6-bf5a-3f1c-8fc7-6ec360edd159 | -9.1573 | -61.5803 | 2024-10-09 00:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d0c6ab1a-7019-3538-bbc9-f68b26c15ac3 | -10.3656 | -64.8262 | 2024-10-09 00:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 82d2d87d-bfc6-3e71-90c3-9e2d5e88a734 | -10.3894 | -61.2502 | 2024-10-09 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 6061f6fc-a8f5-3329-9fb3-ae11f7280292 | -10.3895 | -61.231 | 2024-10-09 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| d83d3661-92c5-3fa4-84e7-26ac456025ed | -10.3842 | -64.8443 | 2024-10-09 00:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2f859fe7-af96-3715-b828-53f4502a61c4 | -10.3843 | -64.8255 | 2024-10-09 00:06:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 811c121d-c5cf-33d3-80f6-46f0548edc1c | -10.5351 | -49.4607 | 2024-10-09 00:06:06 | GOES-16 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f5efd1c2-1c4b-3e35-81cd-833148908793 | -10.4287 | -60.9979 | 2024-10-09 00:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7ea6223f-9bef-3ce4-9704-2f797722dc42 | -10.5902 | -57.5333 | 2024-10-09 00:06:07 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 34c68c99-5754-3a19-9b8b-4ff182d214b5 | -10.6666 | -50.923 | 2024-10-09 00:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ab614122-afb7-3e5d-9670-94a81a114731 | -10.6669 | -50.9017 | 2024-10-09 00:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a9b313c2-d173-3d7e-8b4e-e45fc90f425c | -10.609 | -57.5319 | 2024-10-09 00:06:07 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a4c31227-05ad-3d76-9700-3eca6e328617 | -10.5943 | -64.024 | 2024-10-09 00:06:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 19d34e6d-7075-35b4-b2b1-bbdcde863286 | -10.7056 | -64.1516 | 2024-10-09 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 484d202b-abb0-35c8-9fc8-cdceda222dfc | -10.8567 | -63.9177 | 2024-10-09 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 6b4c8e17-d035-3c87-bad1-97b7bbfe31c4 | -10.8568 | -63.8988 | 2024-10-09 00:06:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 951e97eb-7d08-331d-b0c7-d7d1cb43c3c1 | -10.8754 | -63.9169 | 2024-10-09 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 138.4 |
| e03e2b54-b2a5-3381-b447-ef4c512d66eb | -10.8755 | -63.8979 | 2024-10-09 00:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 1bf7320d-e540-3dc6-8991-8587b17d5000 | -10.8925 | -64.1623 | 2024-10-09 00:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d252f4d2-e04e-3859-93b7-32a0c23e66ca | -10.8941 | -63.916 | 2024-10-09 00:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 02878a4f-ddee-33ce-b1f7-4dc324471fa5 | -10.9112 | -64.1615 | 2024-10-09 00:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 154.0 |
| ba142344-414a-3f67-8e76-76cc76d06d18 | -10.9113 | -64.1426 | 2024-10-09 00:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 0a577322-fed2-3313-8dd9-2925ed82e904 | -10.9082 | -68.3988 | 2024-10-09 00:06:09 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d2f48d0a-f537-3a4a-a07a-23a51731211f | -10.9301 | -64.1417 | 2024-10-09 00:06:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 9839cce6-5622-3bf3-b424-6705358522f5 | -11.5233 | -65.137 | 2024-10-09 00:06:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 55999b0d-b1fa-3eec-a9fe-d3ea46c1a025 | -11.5726 | -58.9619 | 2024-10-09 00:06:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 466ee95b-e578-30e0-b437-6802477797db | -11.5728 | -58.9423 | 2024-10-09 00:06:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 6bb8fa7d-ecd2-3cbc-bb06-345b2344f6f9 | -11.6806 | -64.0312 | 2024-10-09 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 29d39b46-ba1d-35f3-b8a6-6ea81a222605 | -11.6808 | -64.0121 | 2024-10-09 00:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 27d82143-8eac-388a-9d57-ebfc0f0fb7bf | -11.9917 | -51.0766 | 2024-10-09 00:06:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f4f37b4f-cbd2-3da3-b923-954c7ab90705 | -11.992 | -51.0553 | 2024-10-09 00:06:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| f7e527ea-e200-3a8d-bc61-793ce9b6fbde | -12.0107 | -51.0744 | 2024-10-09 00:06:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 4e574807-da1b-3b13-a92e-2dd7cd05ce9b | -12.011 | -51.0531 | 2024-10-09 00:06:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 221.3 |
| b86ecdea-2032-3f08-87e6-4afbf94ec8d9 | -12.7673 | -44.8904 | 2024-10-09 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 274.6 |
| eb23635a-4f36-31e3-8760-2815fe4c4b60 | -12.7678 | -44.8671 | 2024-10-09 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 78b78d63-9a43-30c4-a049-31f1f672c920 | -12.7866 | -44.8873 | 2024-10-09 00:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 955cd395-e454-3f38-8ccb-cf49742149cb | -12.6676 | -63.0819 | 2024-10-09 00:06:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 3de21276-e81f-385f-ba12-2a88e5dce632 | -12.6875 | -62.9656 | 2024-10-09 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6648019f-6b4b-3bee-9113-b9b5d2381152 | -12.6876 | -62.9464 | 2024-10-09 00:06:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c5db89b9-8170-3dd7-935c-2605091d269f | -12.7501 | -62.269 | 2024-10-09 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 466d53f1-f9b6-3e1a-be26-f019da284cfd | -12.769 | -62.2678 | 2024-10-09 00:06:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 8e08ac8d-32ed-3470-b8ff-1a12b70b2347 | -12.9166 | -62.7214 | 2024-10-09 00:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 36432ba1-044a-32dd-bdf2-62fe8b935930 | -12.9565 | -62.4878 | 2024-10-09 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| a1666fc0-0304-3c03-a210-c9369f30cd19 | -12.9566 | -62.4685 | 2024-10-09 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ae63ade0-5f7a-39d3-944a-790378da9275 | -12.9754 | -62.4866 | 2024-10-09 00:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 61.0 |


[Clique aqui para ver as próximas entradas](README2.md)
