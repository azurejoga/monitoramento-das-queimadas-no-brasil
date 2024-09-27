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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a455cc3b-9cb6-31c3-a4a2-a320e14b703f | -7.32021 | -61.17898 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb0c06f6-032a-3f2a-af57-3660dea3eb27 | -7.31932 | -61.1838 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 28bd3721-d7c4-343b-9479-c520a0d7830b | -7.30546 | -61.08654 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60639306-532a-332e-b617-fff385186deb | -7.30457 | -61.0913 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 120cfe7f-db9a-31df-8a1b-0683c15f28a7 | -7.30369 | -61.09605 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 558d93d1-2481-391a-9dae-7d5d2e3d553c | -7.29841 | -61.09023 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45cf5358-a118-384c-b5cb-61911e0acfac | -7.29663 | -61.09979 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8018a1e2-88dc-3a21-b159-fabb0d447318 | -8.98221 | -62.41265 | 2024-09-27 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 186102fd-e689-3e69-9494-6a0302acb52d | -8.22756 | -61.50497 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ff4d3a8-0589-3d4b-be60-b8b6d7a9bb76 | -8.22225 | -61.49904 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8a8e7607-1185-3e0a-b357-750c3544a7f8 | -8.22133 | -61.50397 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 010667cd-5ad1-3f3a-91ac-2eb56b2c3caf | -8.17099 | -61.3979 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be996c55-7ff9-3849-9aa9-74c50df4de82 | -8.16605 | -61.39499 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8c6bbcf5-ce93-3ac8-961d-7c5fe1bb08ef | -8.1648 | -61.39683 | 2024-09-27 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0985ffe4-f42d-39e0-90a2-d2811ff57aeb | -8.14894 | -61.28186 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99715980-34cd-38cd-a4b9-afea18ccd4f7 | -8.1428 | -61.28074 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ae6b3ae-8713-371d-b647-71d61125af3d | -8.13664 | -61.27975 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 798a6c89-f44b-3064-8026-2dbf5279f4b6 | -7.99407 | -61.43174 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79affba9-4610-363f-be1c-89eeb1b7946e | -7.99313 | -61.43674 | 2024-09-27 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e91b75c3-56bf-3d53-a97d-98aaae2f1141 | -8.97785 | -62.4006 | 2024-09-27 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 537f24f5-e174-3140-8518-0ed339b33567 | -8.97679 | -62.40603 | 2024-09-27 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7dcbbd7b-824a-3a22-8558-6b1ed50f5986 | -8.97572 | -62.41148 | 2024-09-27 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 71a4dd5f-5ebd-362a-9b91-f86e8cfa87ec | -8.51954 | -62.06131 | 2024-09-27 04:40:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85bc5f6a-115a-362c-8a08-31aa4c5af43a | -8.52053 | -62.05613 | 2024-09-27 04:40:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 450afeed-62e7-3389-9736-0d6ed0a2dbdb | -9.37125 | -62.44972 | 2024-09-27 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9222af52-83d6-324e-bc2d-f018724b7a01 | -9.37021 | -62.45514 | 2024-09-27 04:40:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e89dfc13-f01a-3e9f-a0e5-6434affc95df | -8.47141 | -62.65281 | 2024-09-27 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ae42cd4-8643-37c8-9112-123c75535602 | -8.4648 | -62.65154 | 2024-09-27 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f43fa007-8cf4-3576-b9b4-e4ecce3fae52 | -8.46364 | -62.65739 | 2024-09-27 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db664b38-3c0d-3813-82ab-4f83ad6225d2 | -8.46753 | -62.65058 | 2024-09-27 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a9049a0-653a-30e6-8736-673e46ec5ed6 | -8.46641 | -62.65644 | 2024-09-27 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c5c2c77-d362-3c24-b907-472c6a9734d7 | -8.40846 | -63.40462 | 2024-09-27 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 641b1f38-f104-3a70-a9af-a5d7614399e0 | -9.16778 | -40.53683 | 2024-09-27 04:40:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4694b142-a943-3118-aa79-3376f3aef142 | -9.60681 | -40.61913 | 2024-09-27 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 424b7f00-eb47-34d3-a262-bb595be15647 | -9.60635 | -40.62264 | 2024-09-27 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a55d2aa7-61a5-3eb1-beae-653d7d640506 | -9.60589 | -40.62614 | 2024-09-27 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c6e2a7c9-4bd8-3035-8f06-53679a43f06e | -9.49982 | -40.86725 | 2024-09-27 04:40:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f271e6d9-fa99-3236-922b-46b5a012a68e | -9.49829 | -40.86544 | 2024-09-27 04:40:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0d43ebad-fce4-3af4-9b69-5ce73f7a3dd6 | -9.49783 | -40.86904 | 2024-09-27 04:40:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f1554ee3-7567-379b-87c7-9472f943f8a2 | -9.49446 | -40.86655 | 2024-09-27 04:40:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a60a00b3-402e-3c91-be9f-74cfee6df65f | -12.15576 | -40.85974 | 2024-09-27 04:40:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 45449342-63a9-38f5-8e4c-a1dfb8686f4f | -12.15527 | -40.86372 | 2024-09-27 04:40:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5d6961d9-1616-30b2-a0b8-de0fdf21db09 | -12.15518 | -40.85963 | 2024-09-27 04:40:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e333c549-8c52-30b8-a556-f38f88b266c4 | -13.40745 | -41.32663 | 2024-09-27 04:40:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ae81fe58-745f-3a76-a1b6-299b5ea26c31 | -13.40703 | -41.33031 | 2024-09-27 04:40:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d40a957f-4b3d-31be-bafd-a2fc823c1a1b | -13.2648 | -41.49663 | 2024-09-27 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fdce35d9-c308-36f0-8cad-034a974603e4 | -13.26202 | -41.4979 | 2024-09-27 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c6c8b33-462a-39d4-9d0f-a867814b9512 | -13.25941 | -41.49586 | 2024-09-27 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1a032c6e-83f9-3b35-adae-f4aa1f5804d0 | -13.259 | -41.49941 | 2024-09-27 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82e0fa1a-7145-38ca-a540-7794458729fd | -13.25859 | -41.50296 | 2024-09-27 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3fae356-7513-3102-87f4-cd49b00f5d09 | -13.2562 | -41.50062 | 2024-09-27 04:40:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e6663282-04bb-3043-a37e-8c17a2af38e1 | -6.85992 | -41.70345 | 2024-09-27 04:40:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c7cf6b28-11f1-3f4f-941f-14f7e74dfb4f | -7.05498 | -42.05546 | 2024-09-27 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cccd1c92-a75d-3294-92e9-959c5cabc66d | -7.05424 | -42.06066 | 2024-09-27 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b81350af-9627-3bd7-bbb8-30cdac81776d | -8.30375 | -41.43401 | 2024-09-27 04:40:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e8970f67-f40e-3f6b-84de-741105d287b0 | -8.30334 | -41.43702 | 2024-09-27 04:40:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 93138502-abb9-3392-8f04-f502d2ff848a | -8.29869 | -41.43331 | 2024-09-27 04:40:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25cef6ac-ba53-3264-89f1-0b63668abf57 | -8.29828 | -41.43633 | 2024-09-27 04:40:00 | NOAA-21 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c0562b3-3bc4-3848-88aa-00e44751ef04 | -8.29445 | -41.42653 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c630d8a7-7f89-3f40-9869-a2494df9dac7 | -8.29404 | -41.42956 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 65cfa0cc-9d3e-36dc-ad97-ca38eff06e54 | -13.53716 | -42.56171 | 2024-09-27 04:40:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10eed627-4515-347d-9738-056713c78d8c | -13.53678 | -42.56479 | 2024-09-27 04:40:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b1eb8a8-66e2-3dcc-846d-31c963688beb | -13.01365 | -42.2174 | 2024-09-27 04:40:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69c49352-f686-349c-815d-e623d0ecc363 | -11.69776 | -44.52427 | 2024-09-27 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd929ee5-17eb-3b70-a4b2-b864c45d5ed7 | -7.96816 | -42.8527 | 2024-09-27 04:40:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8c76ffe2-23c6-38bc-9647-79a264bc0a83 | -7.96361 | -42.85188 | 2024-09-27 04:40:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| b63257cf-ec5e-3f8d-8819-709d1e0f685e | -7.87329 | -42.69043 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7fa523d9-4b4a-3222-99eb-9a1277497240 | -7.86804 | -42.69442 | 2024-09-27 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d2d43b29-f38e-3c51-838e-134eccf347c2 | -7.86739 | -42.6992 | 2024-09-27 04:40:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d1a7d46-b95d-3288-ba62-fa793466028f | -6.88232 | -42.84544 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 968d4bcc-b9b0-3711-beea-d0ae6589a8fc | -6.87781 | -42.84495 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 66442cd0-cf09-3460-a958-dd7a03bb5e2a | -6.87718 | -42.84949 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 2fb3e99f-ead3-3d03-a3b9-363aa7b09743 | -6.84902 | -43.11522 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89dcfce6-f472-3f9b-a4cb-2ec56990d151 | -6.81464 | -43.13605 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ece63b0-85e8-3ecb-9596-a8540f53c7a8 | -6.81404 | -43.14038 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0da14ad2-c7da-31fe-8f26-171d13b6d100 | -6.81404 | -43.13857 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2eac44bd-943f-3c09-bdd9-3aa7aa22669d | -6.68861 | -43.51649 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b78c2c60-4db7-337d-ab77-18643f48d6ee | -6.68433 | -43.51587 | 2024-09-27 04:40:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b871baa-2027-32b4-b500-f00dbbc43a6c | -7.58869 | -42.29154 | 2024-09-27 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 03cb5ddb-d9d2-3c8c-984f-b180e4a48786 | -7.58638 | -42.28691 | 2024-09-27 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2869e536-1f72-3db5-8ed2-dd6e7508ed64 | -7.58568 | -42.29206 | 2024-09-27 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6cd4308e-2c5a-3bbc-a914-7b3789d8173a | -7.58469 | -42.28587 | 2024-09-27 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd607f6c-6d08-33fe-ad0f-eb3b36da1a33 | -7.58395 | -42.291 | 2024-09-27 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3e2c83b7-aa37-384f-99ce-b3486c7d9af9 | -7.48677 | -43.71124 | 2024-09-27 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fa4ce761-bd25-31c0-ac08-88f8a0eda009 | -7.2777 | -42.28893 | 2024-09-27 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9a893b2c-4f78-3476-8b5e-0c150888308f | -7.27573 | -42.28746 | 2024-09-27 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0c773ac1-0084-3f86-a4d4-6878487dbef2 | -7.13373 | -43.19988 | 2024-09-27 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1a7877c-4415-35e3-ad72-159e62b8c435 | -7.13029 | -42.51347 | 2024-09-27 04:40:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 474079c5-4a7a-3815-b5af-e49904ee8436 | -7.38312 | -43.34317 | 2024-09-27 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca3a9782-7343-35ee-86f2-c86659f0ecbb | -7.37181 | -43.32841 | 2024-09-27 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf8dd95e-33c0-3376-a0de-51964b948dcb | -7.30008 | -43.3876 | 2024-09-27 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ceaf7f5-714d-3beb-b867-421e024ed11c | -7.29674 | -43.3179 | 2024-09-27 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc5b54f6-0785-36ef-8bc5-fbbf4cdd6a1c | -7.29297 | -43.31305 | 2024-09-27 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6300899f-331f-36c9-9b9b-bc3a0e084951 | -8.07526 | -42.89019 | 2024-09-27 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 769401c8-d7b3-3e64-937d-49f366fee603 | -8.07461 | -42.89495 | 2024-09-27 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ff38ed0c-2b67-3443-9f3f-bc1d6c09dd62 | -8.07397 | -42.89959 | 2024-09-27 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 716c4982-9d4b-31fc-a198-33ae8da01a32 | -8.07133 | -42.88494 | 2024-09-27 04:40:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| dceff6bd-d6f5-344a-9e31-7483282a8e72 | -8.06487 | -42.89816 | 2024-09-27 04:40:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a083544-21bc-3b05-8a6f-205dacc9af94 | -8.50603 | -43.92424 | 2024-09-27 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83c49e5d-4ecc-39cc-9870-cc514cf69fec | -10.60111 | -44.28578 | 2024-09-27 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README85.md)
