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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d90aa0c-55a8-3ec1-8f4b-061735cd9606 | -10.9105 | -57.4308 | 2024-09-26 01:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2114f4df-b8ce-337a-a7a9-5b4a58351c8b | -10.9107 | -57.411 | 2024-09-26 01:26:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fd2e7c9c-68ea-3d53-b4ea-b90765593f3f | -11.2123 | -51.1415 | 2024-09-26 01:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a8394057-988e-377e-8abc-fb2ad703ed57 | -11.2034 | -54.7752 | 2024-09-26 01:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 3679b420-754d-3fd3-8ec2-be64c2676361 | -11.2599 | -65.299 | 2024-09-26 01:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 692bb584-662b-3120-9fd5-9026fce8ee80 | -11.26 | -65.2801 | 2024-09-26 01:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.7 |
| c7baf6f8-670a-3f49-8be3-5e7c435397bb | -11.2786 | -65.2982 | 2024-09-26 01:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3392bc88-1261-3457-8da8-919479097cac | -11.955 | -60.363 | 2024-09-26 01:26:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f1d0af94-03ea-3a8a-8376-869e5a444ae4 | -12.2367 | -45.5045 | 2024-09-26 01:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 0546c798-acc9-3e2b-8e0f-66ff5776dbc2 | -12.5085 | -53.498 | 2024-09-26 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| df467949-40c5-3378-b84b-bdbe339ec6f9 | -12.5276 | -53.496 | 2024-09-26 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 3ba01f73-8f80-3cc1-ba8b-08f5693776a8 | -12.822 | -62.7078 | 2024-09-26 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| cc2a59cc-6a7c-3d01-bfa9-8c61370f8e00 | -12.8222 | -62.6886 | 2024-09-26 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 7fc97880-4807-3c20-8591-37726c7102c4 | -12.8408 | -62.7259 | 2024-09-26 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 1538aa15-cbf1-367c-ba31-3b0aceca2ab5 | -12.841 | -62.7067 | 2024-09-26 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 216.2 |
| c5d7000e-4153-3511-b682-528b1f28cec0 | -12.8411 | -62.6874 | 2024-09-26 01:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 5a6610e2-994c-33a4-adb5-804cf144ac70 | -13.2863 | -51.326 | 2024-09-26 01:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 9798dbfc-bc64-3fba-925a-471b7eb681c3 | -14.5705 | -45.6973 | 2024-09-26 01:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c0c8b433-8689-3a23-82e5-140f6872730e | -17.0802 | -56.1321 | 2024-09-26 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 9457bc8e-a845-30e3-aa77-8a1f9cfd36e4 | -17.096 | -56.3576 | 2024-09-26 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 295f121a-3894-36e4-88ed-651ae3976b5a | -17.0963 | -56.3369 | 2024-09-26 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| 93f37574-08cf-3700-8ed0-ca72e52ab5d9 | -17.0991 | -56.1711 | 2024-09-26 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 92.7 |
| cf1a7c06-6118-3435-a663-79343b1c2131 | -17.0995 | -56.1504 | 2024-09-26 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 93.1 |
| 69f490b3-8423-37d1-b95e-fdbec2bd150f | -17.0998 | -56.1296 | 2024-09-26 01:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 97c57c9b-8229-3330-ad7f-5ccfc6dcb564 | -19.929 | -43.7959 | 2024-09-26 01:26:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.8 |
| 22f708a1-3cba-3ce2-8787-feed84bbd878 | -19.9298 | -43.7711 | 2024-09-26 01:26:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.9 |
| 38fddaeb-ab2b-304f-a444-f69ad9694b9c | -19.9496 | -43.7904 | 2024-09-26 01:26:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.3 |
| f8691caf-d7de-3e2c-bb6c-9ae5cc8b7f67 | -19.9503 | -43.7656 | 2024-09-26 01:26:56 | GOES-16 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| 88db40d1-11ff-3f36-bd71-df0499797688 | -20.4197 | -41.8798 | 2024-09-26 01:26:58 | GOES-16 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 88.7 |
| 2f53bfdf-02e3-3b46-9617-e1782deb3cba | -20.4206 | -41.8541 | 2024-09-26 01:26:58 | GOES-16 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.1 |
| 676744df-80c6-3fbb-8f9c-849dcaaf163a | -20.5876 | -51.5026 | 2024-09-26 01:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.0 |
| c182a76e-a238-3fd9-b6ad-b5e5a0c36b82 | -20.6074 | -51.5209 | 2024-09-26 01:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.0 |
| 2b36d170-841c-3227-8bfe-6fc71f5d883d | -20.608 | -51.4986 | 2024-09-26 01:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 406.1 |
| 46ab7cc1-cc1a-3b99-a4ee-4b958dbc0149 | -20.6086 | -51.4762 | 2024-09-26 01:27:00 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.8 |
| 4fb27f95-e00c-3d5e-b2f8-3bb1d499e0cd | -20.6284 | -51.4945 | 2024-09-26 01:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 41e32f35-9b21-3420-aaeb-2b4f23a38831 | -21.9374 | -48.5688 | 2024-09-26 01:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 55c4f47c-a548-3e4f-9d07-c334891d4f3a | -21.9381 | -48.5453 | 2024-09-26 01:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 35c543a6-6d2f-3b06-9dc9-ef322a50b8bf | -2.6601 | -57.5507 | 2024-09-26 01:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 813981f1-ae74-3dd9-936e-e495d3c0af12 | -2.6785 | -57.531 | 2024-09-26 01:35:21 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| ebe0359f-8056-3479-9889-0faa41875db9 | -2.6968 | -57.5307 | 2024-09-26 01:35:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3a45c10f-ca74-3152-a8e0-5d037e2f3d58 | -3.3158 | -53.2122 | 2024-09-26 01:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 66e21d16-f5ab-3b19-9f87-b5ed6d4bb3ef | -3.3159 | -53.192 | 2024-09-26 01:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4d625060-ce33-377a-b674-d465f7615d41 | -3.3342 | -53.2117 | 2024-09-26 01:35:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3a5fce18-f28c-332a-8772-e5bb0556ae4b | -3.3505 | -53.7775 | 2024-09-26 01:35:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 7aa5a80f-0315-37c6-868d-4532f10682a8 | -3.5488 | -50.38 | 2024-09-26 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 26a192e1-b11f-32fb-a868-9b7ca68a67f9 | -3.5673 | -50.3794 | 2024-09-26 01:35:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 73c5405c-064b-38b4-9efc-5866b814b437 | -3.7282 | -47.7266 | 2024-09-26 01:35:27 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| db0d8dcb-8510-3968-89fa-0c4acb5c7014 | -3.8008 | -41.5989 | 2024-09-26 01:35:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 7fae5c4e-51df-3c03-bfaa-a266a697af04 | -3.9208 | -46.4459 | 2024-09-26 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5da45b26-1a8d-3617-a668-6f5138e1d91a | -6.784 | -59.3052 | 2024-09-26 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ee529105-6ebc-3ad8-99fb-f9cb2e39b0dc | -6.8023 | -59.3237 | 2024-09-26 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3e84fd4d-534b-38e4-a51f-0768227b6430 | -6.8024 | -59.3044 | 2024-09-26 01:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.5 |
| c64e3238-e0f4-35f2-a9ec-50dcabd6bbb0 | -6.9306 | -63.1053 | 2024-09-26 01:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| dccfb98f-468c-356b-9412-2d171246a0e3 | -7.2905 | -61.106 | 2024-09-26 01:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 85a900b8-91dc-36b8-babc-10f8063663f6 | -7.3452 | -55.5145 | 2024-09-26 01:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 551266e7-2b89-3c72-97e4-4241bb18cb63 | -7.3636 | -55.5334 | 2024-09-26 01:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b15ea771-1f16-38b5-b0e1-6e6c9a2088f1 | -7.3637 | -55.5134 | 2024-09-26 01:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 213.1 |
| 90c8eac6-1e3f-3701-ad66-f00d58c5b277 | -7.3639 | -55.4935 | 2024-09-26 01:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 13cf8d9d-aa56-3eb7-b02c-00fda7182214 | -7.3823 | -55.5124 | 2024-09-26 01:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 230.9 |
| a694753a-cab0-3e95-b0de-cf536f7d1af5 | -7.3824 | -55.4924 | 2024-09-26 01:35:48 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 180.1 |
| 13ede219-d17a-3f04-8758-eb4c22e854c6 | -8.3155 | -54.9956 | 2024-09-26 01:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| b146e859-7d16-36e7-b2b5-2dfcc66d3607 | -8.7087 | -54.7881 | 2024-09-26 01:35:56 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 43119ae1-0dae-3f16-a6f5-1e6f16308160 | -8.8098 | -58.2172 | 2024-09-26 01:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8e440641-3634-3a0c-a3b4-6c7091505004 | -8.8284 | -58.2161 | 2024-09-26 01:35:57 | GOES-16 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| c9c3027c-397d-37a8-ad9b-295583f621a3 | -9.1046 | -61.1237 | 2024-09-26 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| de86873e-dbc6-35ad-ba7e-300f6837caf0 | -8.9429 | -67.1884 | 2024-09-26 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 3cbbd18b-7489-37cb-a543-6d99ca7c4aa2 | -9.086 | -61.1245 | 2024-09-26 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9956c3de-6721-3000-845e-543e1d6db6be | -8.9244 | -67.1889 | 2024-09-26 01:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 85df5b08-5802-3c35-82dd-a1a26fb95477 | -9.1035 | -61.2769 | 2024-09-26 01:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| be79edb3-cdec-3c71-a808-26887892d89b | -9.1349 | -65.564 | 2024-09-26 01:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 88a1bb99-02c6-3575-96bc-647c45c070de | -9.135 | -65.5453 | 2024-09-26 01:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| c898a695-8d12-3c9d-b789-f512a34fae23 | -9.1535 | -65.5634 | 2024-09-26 01:35:59 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5b86e85d-2041-378b-be65-55bb239ae431 | -9.3571 | -65.6315 | 2024-09-26 01:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f4887b8f-938d-39bb-abd7-b89ce8970a21 | -9.6015 | -50.1566 | 2024-09-26 01:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| bd6afc05-9ddd-3447-ab19-8bc0983768c6 | -9.6018 | -50.1352 | 2024-09-26 01:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 926dcc18-ef25-3af6-a166-ba6bb73ca3c0 | -9.6149 | -57.7568 | 2024-09-26 01:36:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c456f812-9153-3d49-844e-28b80495d997 | -10.3882 | -67.8737 | 2024-09-26 01:36:06 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a3f08e38-7557-360d-a42b-880a27d4ead9 | -11.2034 | -54.7752 | 2024-09-26 01:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |
| 7f5f65e2-350a-33a5-bdd0-37f7e957a727 | -11.2599 | -65.299 | 2024-09-26 01:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 94e6ea09-ce2f-37f0-bf4c-a8821d865759 | -11.26 | -65.2801 | 2024-09-26 01:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 71bbe855-e809-3b11-8a4e-e4ad782d09f1 | -11.2786 | -65.2982 | 2024-09-26 01:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.5 |
| a4a2ad8c-409b-3e37-8d6d-0ac180bc12fa | -11.2788 | -65.2793 | 2024-09-26 01:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 824499b8-9b20-3548-ad09-935c63627cab | -11.7179 | -47.8551 | 2024-09-26 01:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| aaa17734-b9a1-34d3-be2d-5b331725765f | -11.5972 | -60.3475 | 2024-09-26 01:36:12 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 1b142ed0-1171-341d-9a61-7a6ded362e6e | -11.616 | -60.3463 | 2024-09-26 01:36:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 46.4 |
| ca39c0bf-2d6a-3b7f-9e7d-d1fbf67ec36d | -11.955 | -60.363 | 2024-09-26 01:36:14 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 49c626e9-4e99-3130-958e-e9dc0e049508 | -12.2175 | -45.5074 | 2024-09-26 01:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 196e7906-bdd0-33e9-906a-db10005d861c | -12.5085 | -53.498 | 2024-09-26 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| dff483b8-7ee6-3461-b98f-037ae1f1f96e | -12.5276 | -53.496 | 2024-09-26 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 94148bce-4a58-307b-af77-f4aa33780c8c | -12.822 | -62.7078 | 2024-09-26 01:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 67dc025b-d384-3589-adca-c74c13fcc368 | -12.841 | -62.7067 | 2024-09-26 01:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 191.7 |
| 920c5197-ac61-3013-971c-8ff90b4df64b | -12.8411 | -62.6874 | 2024-09-26 01:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 99.2 |
| e4bf5ba5-07cd-3f1b-a438-92bf67922652 | -12.8599 | -62.7056 | 2024-09-26 01:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6ffab517-e101-3143-b562-ad10eac57a71 | -13.0295 | -57.2985 | 2024-09-26 01:36:20 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e7a7404c-cb90-398e-b7c2-e673a3cb07f0 | -13.286 | -51.3473 | 2024-09-26 01:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 253.9 |
| 9ca8f01b-3766-31f6-8637-b7caa79c6b16 | -13.2863 | -51.326 | 2024-09-26 01:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 434.8 |
| fd3081e7-d99c-3280-8a92-142735332604 | -13.3052 | -51.3449 | 2024-09-26 01:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 171.4 |
| b1c20040-fc8a-3577-a0dd-2643eaecab1a | -13.3055 | -51.3235 | 2024-09-26 01:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 7438c127-8982-34bd-85b9-b521f15ccdf7 | -13.4993 | -61.2698 | 2024-09-26 01:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 0bfc8c85-2489-337e-bb79-783eee9daf01 | -14.57 | -45.7205 | 2024-09-26 01:36:28 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |


[Clique aqui para ver as próximas entradas](README34.md)
