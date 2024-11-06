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
| d6d21505-80e4-3fd0-a543-d2bab7c7fd0a | -2.1007 | -46.475498 | 2024-11-06 00:54:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b360d48b-650f-3539-90e7-865e30697b9c | -2.5567 | -54.001499 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bcea725-9eb7-3fba-9c94-680a3db2154c | -2.0359 | -53.573002 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dce93f98-4ecc-3f5f-8f58-523af40c0cea | -2.7218 | -51.708199 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf50459-e3de-3f29-b387-3932cccc1492 | -4.6833 | -46.3909 | 2024-11-06 00:54:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c4d8b24-41de-3ce3-bf8b-386642384bc9 | -12.1558 | -44.617901 | 2024-11-06 00:54:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7a74e58-3e3f-3d21-a6e6-6fb1116182a3 | -1.8669 | -54.682899 | 2024-11-06 00:54:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da0b158d-cad0-313a-844c-d11a5b72cd80 | -3.7051 | -41.6922 | 2024-11-06 00:54:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5feded2a-9a20-3dc8-9c9b-647e33336e00 | -2.8238 | -52.960098 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f234327-dd77-320e-aae2-7058f464f84e | 3.6147 | -51.318298 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ed382a51-1828-36c0-b7fa-b0a11aac4ff8 | -2.8438 | -52.912601 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82f1a65e-5340-3f8b-a87f-1bdb8d593589 | -2.9311 | -51.049702 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfc7ff21-1cee-305d-8e0f-7fc5256e8a94 | -4.6567 | -43.815899 | 2024-11-06 00:54:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b9fba971-863c-35c3-b9ff-43bd8a0159d9 | -2.8761 | -51.3032 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de026ad0-099a-3fbc-a4bd-bb898ad40b28 | -3.0133 | -53.427299 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db36a19-4d7a-3431-be62-8c129127e515 | -23.9306 | -54.0564 | 2024-11-06 01:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 86.8 |
| 968d0b62-db69-35b9-9ceb-2b51a096e82f | -4.1247 | -43.5601 | 2024-11-06 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 91583d92-bb53-3dae-9b5f-35465ce8581d | -3.0213 | -53.2607 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 38abcc89-3178-337b-9db0-6279a90d4215 | -2.6131 | -54.5381 | 2024-11-06 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a0764479-c78c-3cc9-bcb6-f8ff77044ffa | -2.1746 | -53.7036 | 2024-11-06 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| f7c95473-c7d7-313f-b90e-8fdeff448dae | -3.1397 | -51.103 | 2024-11-06 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| d7c20227-2ad0-3aef-995d-0ade2a0a9e1d | -3.0397 | -53.2603 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| efddc652-9fd2-3622-ba2b-ba7e26f18155 | -6.5014 | -47.4813 | 2024-11-06 01:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 267.8 |
| 0951ceed-cbca-33b9-a9b7-81ad426d4e05 | -3.0212 | -53.281 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 072a00a0-45de-31e2-a363-63f46abb6844 | -2.6764 | -51.8395 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| b04108c5-7d92-308b-b373-25b2b5b27647 | -0.8539 | -52.8298 | 2024-11-06 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 24f155cb-e260-3a73-89ab-f473d227ec56 | -3.967 | -48.15 | 2024-11-06 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 1457b0ec-5f32-3292-91f1-86ff976e1bdf | -3.2415 | -53.3967 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 3cb1bb83-c068-316a-8773-3de1588e7bd1 | -2.8423 | -51.7735 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 86c777b1-6656-3464-ada1-1f60d68b15b8 | -6.1041 | -43.9593 | 2024-11-06 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 8b2ffa37-611c-3aef-ac19-97e56d2716a7 | -6.1416 | -43.9563 | 2024-11-06 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 40a31a59-6021-3878-8666-f787890a5f26 | -3.2349 | -50.3695 | 2024-11-06 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| fc1ec254-aad1-36c2-bafd-4a87589ca825 | -6.4906 | -44.6862 | 2024-11-06 01:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 040457de-2ff2-3855-8de8-fd1d90722251 | -5.5632 | -43.6998 | 2024-11-06 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7401a0e2-d1f1-3042-8535-a115e36da127 | -6.5094 | -44.6847 | 2024-11-06 01:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 7eb1bdd2-f22d-39d2-895d-e0a10c447ff1 | -4.5616 | -47.9925 | 2024-11-06 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6cee5082-ddf5-31ff-bb49-7fdaf96d1032 | -3.1393 | -51.2069 | 2024-11-06 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b87a0de3-3f27-31c5-902a-641e7d105ee7 | -3.0023 | -53.4434 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 6171c687-94c4-31bb-9d44-ea7b23d260e7 | 3.6184 | -51.3162 | 2024-11-06 01:00:00 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 80.5 |
| d24314f0-1437-365a-b996-edcce7eb36c3 | -6.5012 | -47.5033 | 2024-11-06 01:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 5d957f55-7376-3d10-944e-6028a3000de3 | -6.5096 | -44.6618 | 2024-11-06 01:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e1a37a36-90ae-32eb-85ee-6e1321f4766f | -6.4909 | -44.6633 | 2024-11-06 01:00:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 12821a7d-5c34-3df3-a9dc-655efc0f100b | -2.8662 | -45.5977 | 2024-11-06 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 36.0 |
| d46e2edf-6e1d-300d-991b-22b86ee41ff2 | -6.1226 | -43.9809 | 2024-11-06 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 2626efef-85ab-3ab0-a5bd-0db8c737f06b | -2.7244 | -54.1351 | 2024-11-06 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 0aecf47c-08f9-3e17-9cb2-259ef34668aa | -3.0207 | -53.443 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 89bfcd8d-46c8-30f1-afd1-99ffba356316 | -3.0396 | -53.2805 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| d01ebab6-4f01-32f7-a65b-dc45ce41b049 | -3.1213 | -51.1036 | 2024-11-06 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 96cfc87f-eb53-38c8-a215-fff76a577cf5 | -3.0607 | -52.5066 | 2024-11-06 01:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| cd3c8316-0993-3027-b21b-77d6bc36170f | -3.1212 | -51.1244 | 2024-11-06 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| ccc9d72e-1d05-356c-806e-08fa798820fd | -3.2348 | -50.3904 | 2024-11-06 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| cd6a1075-ce58-360a-90bd-6daf146e7c78 | -2.8661 | -45.6201 | 2024-11-06 01:00:00 | GOES-16 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a0fa7e10-d0b1-3e97-bb4c-96e69ab71a1b | -23.93 | -54.0787 | 2024-11-06 01:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 111.6 |
| 3b38b9ae-b600-34f8-9c29-6f61512bd6ec | -6.1229 | -43.9578 | 2024-11-06 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| d7bfcb26-75e6-31bf-a0c7-45ad1ace2b43 | -2.4185 | -46.1693 | 2024-11-06 01:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 831fabd0-a574-3d27-b561-978eb73b8ab5 | -23.9512 | -54.0744 | 2024-11-06 01:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| e83a6609-07e3-3328-a194-976cf7fe8ddb | -2.1563 | -53.6636 | 2024-11-06 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ba0c60de-9361-3bf2-9318-06ae074602d9 | -3.9669 | -48.1716 | 2024-11-06 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d9515af8-05bb-36ae-9c9a-22f9104cfa8d | -3.0207 | -53.4227 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 71597bbe-b502-3347-ad04-eabfb96c36b3 | -3.6788 | -50.2284 | 2024-11-06 01:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 4376b9ae-a790-3bb6-aaf6-1ad2a860ef22 | -2.7243 | -54.1552 | 2024-11-06 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| d6fe4dff-d404-3091-ace3-fe334c726e1d | -6.1039 | -43.9824 | 2024-11-06 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 939774dc-d260-319a-aca5-7363c3ae438b | -6.1414 | -43.9794 | 2024-11-06 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| fa9e28a4-5506-36e4-a479-4978d8eaaf79 | -2.8424 | -51.7529 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 37c99f5c-1ba6-328a-8eaf-dd4f9e93221b | -2.1563 | -53.6838 | 2024-11-06 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| eb02a9ee-f275-3ce6-bd9a-47a683daeb61 | -2.2505 | -46.484 | 2024-11-06 01:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| a47b787e-2004-390e-a7f2-1dc862330464 | -2.8608 | -51.7731 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 264.6 |
| d65ec61c-6af3-31c2-b4a8-8621d3cd2053 | -6.4827 | -47.4827 | 2024-11-06 01:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 851971ae-f31e-3d56-a8c6-3631c95912df | -2.1746 | -53.6834 | 2024-11-06 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 30a8779c-cd8b-310f-9046-1662946246eb | -4.1246 | -43.5833 | 2024-11-06 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 357.4 |
| ee331948-abc4-31da-89f1-c886edbead19 | -2.8607 | -51.7937 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| f4cc5c3f-96ff-357f-a6ad-a6567b932618 | -5.675 | -45.9232 | 2024-11-06 01:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 6eedede6-5eb0-3c63-abd2-019bbfbb2c81 | -2.3999 | -46.1699 | 2024-11-06 01:00:00 | GOES-16 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4dcd3e90-58fd-34dd-b880-37410a8440d7 | -4.0859 | -53.9365 | 2024-11-06 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| a515a557-70e5-3b02-a62b-2cc2a34a745b | -3.5262 | -51.3193 | 2024-11-06 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| c12a7dfd-effd-39f4-ad9a-7406c1ccdbda | -4.1432 | -43.5822 | 2024-11-06 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 183.1 |
| c1b28ef7-297a-3628-8a8a-810685170cc1 | -2.6764 | -51.8189 | 2024-11-06 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 15676fbd-b61b-33ea-855a-02ac7d5a9432 | -6.4825 | -47.5046 | 2024-11-06 01:00:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e785d684-7cfd-325e-9ca8-a3d5669d0fee | -3.1759 | -51.2681 | 2024-11-06 01:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 0dc5a8cd-c1e1-32d2-adfd-eb282837d74b | -4.1434 | -43.5591 | 2024-11-06 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c1f6d165-535a-3125-b80d-32c093a40add | -3.0023 | -53.4232 | 2024-11-06 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8a0bc901-f70b-3504-9864-42476e55d478 | -1.2922 | -54.5585 | 2024-11-06 01:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| ab64ba9b-fb3e-3a25-b6bf-3f25e36be7f1 | -2.8608 | -51.7524 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 7dd5fbc6-0f18-3360-a6f1-8f2df75f4398 | -4.2165 | -53.5686 | 2024-11-06 01:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 112b84c3-d356-34d5-995d-8c26f590b707 | -4.1244 | -43.6064 | 2024-11-06 01:00:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 73132238-c650-33b6-86c9-4aafc28931c3 | -2.8423 | -51.7942 | 2024-11-06 01:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 25ab273a-6bc6-3fc5-a007-8eea9703cfe4 | -4.5614 | -48.0141 | 2024-11-06 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c8853553-86a2-3beb-9b6b-950eac6fc1dc | -2.84 | -52.94 | 2024-11-06 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a09bcd4d-e50b-31eb-bcd1-94a03840308b | -2.81 | -52.94 | 2024-11-06 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e4c95c5-da94-3a8c-b4d3-91fcefa9351a | -2.81 | -52.88 | 2024-11-06 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4931fa2c-fd68-3550-be08-a6cf430676ea | -6.12 | -43.99 | 2024-11-06 01:00:00 | MSG-03 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87ad3f18-60f6-316e-8a5a-6f63b88ce6ad | -4.13 | -43.55 | 2024-11-06 01:00:00 | MSG-03 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d556ba1-167a-34cc-a613-6938a45e668a | -4.13 | -43.6 | 2024-11-06 01:00:00 | MSG-03 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b03189e6-3be6-3c8d-b5f4-6b3d880580b2 | -6.49 | -47.51 | 2024-11-06 01:00:00 | MSG-03 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35062b9b-8fdc-3bcd-a9db-e807c72ce7bd | -3.0396 | -53.2805 | 2024-11-06 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 853f6302-add0-3c6f-81f0-ded2384cb96c | -2.1746 | -53.7036 | 2024-11-06 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 891473e2-66c7-35b2-9230-0b43b0d883b6 | -2.082 | -47.0383 | 2024-11-06 01:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 8a41ee0a-6472-3f25-a3af-6531efcd1ad4 | -2.8608 | -51.7524 | 2024-11-06 01:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 926393da-1cc2-36ff-a588-fbe53d245b62 | -6.5012 | -47.5033 | 2024-11-06 01:10:00 | GOES-16 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 60da390c-ad6a-33a8-8216-0bb01377a33f | -3.1213 | -51.1036 | 2024-11-06 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |


[Clique aqui para ver as próximas entradas](README13.md)
