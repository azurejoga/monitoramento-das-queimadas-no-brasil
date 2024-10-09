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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 013e9389-73bc-319f-8cae-6afaba5ede66 | -6.7798 | -60.0552 | 2024-10-09 01:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 3c649dfd-d206-3f7d-8d29-0fa37edcfea3 | -6.7799 | -60.036 | 2024-10-09 01:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d0df901c-2f52-3121-91f8-f35f65675cc9 | -7.1873 | -59.7701 | 2024-10-09 01:55:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 42925259-d837-308b-815b-67b6781c417b | -8.3403 | -44.1195 | 2024-10-09 01:55:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b1b273ae-f2da-3376-b850-f4f854422e13 | -8.3406 | -44.0963 | 2024-10-09 01:55:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ae3b9268-8022-3083-9cb8-cc82b388e292 | -8.4919 | -48.6476 | 2024-10-09 01:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 3543c8bf-29be-3186-bf4c-23f266946c6f | -8.4921 | -48.6259 | 2024-10-09 01:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ad39e970-41db-3c36-9285-10cd7624bbaf | -8.5107 | -48.6459 | 2024-10-09 01:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 45a26506-01b6-341a-b482-3476cad66ac8 | -10.3894 | -61.2502 | 2024-10-09 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 33dc55c2-7fa6-38aa-ac75-c6785eff8f4c | -10.3895 | -61.231 | 2024-10-09 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d723e186-d864-3343-96db-09e856207458 | -10.4287 | -60.9979 | 2024-10-09 01:56:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| eb4cb57a-674d-3028-9d83-90a32ebf88d5 | -10.6068 | -55.9169 | 2024-10-09 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8a67df6e-b129-3e32-a739-a756ec3b2bf3 | -10.6253 | -55.9355 | 2024-10-09 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b89b3271-b892-3309-99b1-e05bfd403a82 | -10.6256 | -55.9154 | 2024-10-09 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 122.6 |
| e38276da-3b06-31ae-84cf-21b30f113f92 | -10.6258 | -55.8953 | 2024-10-09 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| b7b49d9b-4870-3222-b3e6-07fdb53cf117 | -10.6444 | -55.914 | 2024-10-09 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 26197c38-0c65-3efe-9d62-4df640bb9f4e | -10.6446 | -55.8938 | 2024-10-09 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 4e9009e0-a9ac-3174-82ff-ce5760a7b9f1 | -10.8567 | -63.9177 | 2024-10-09 01:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 99e68bb5-4bc1-35ce-848e-7930c12addaf | -10.8754 | -63.9169 | 2024-10-09 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 988f5374-6078-3f36-8d44-e3b8cd806eb7 | -10.8755 | -63.8979 | 2024-10-09 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 6ca9d230-925e-36a5-8aea-72f6116880c8 | -10.8941 | -63.916 | 2024-10-09 01:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| b512f680-e805-3131-9f4b-12a5c78ca8fd | -10.9112 | -64.1615 | 2024-10-09 01:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 3faba191-8a3b-3890-a95a-35974f9baaba | -10.9113 | -64.1426 | 2024-10-09 01:56:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0cfcce35-9d53-3d68-95be-cf344c3e9e8d | -11.6806 | -64.0312 | 2024-10-09 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c8439d46-dea4-3440-9199-0404a9c6c1f4 | -11.693 | -65.0163 | 2024-10-09 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 63ca7c88-ba08-3301-90ac-35a535e34a35 | -11.7117 | -65.0155 | 2024-10-09 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ca03c416-9140-30d4-bc59-4a34d9a69509 | -11.7119 | -64.9966 | 2024-10-09 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0cc55534-5d91-3303-9910-19c094823294 | -12.6676 | -63.0819 | 2024-10-09 01:56:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 61649717-d999-3308-967c-3d7a9161f6ab | -12.8591 | -62.8018 | 2024-10-09 01:56:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 08bb0387-cac6-32fb-8adf-a0f5cd54c184 | -12.8779 | -62.82 | 2024-10-09 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 9112e325-1b8c-31c3-a47b-9ecd6311c586 | -12.878 | -62.8007 | 2024-10-09 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| f9e3d498-2664-372f-b097-37faaf74e37f | -12.9566 | -62.4685 | 2024-10-09 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ba9fc845-c140-3247-a747-7b6e9f90b588 | -12.9756 | -62.4673 | 2024-10-09 01:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 73e1f994-c762-38f7-bcf8-347188789ec6 | -13.1931 | -51.1669 | 2024-10-09 01:56:21 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 16ea6de5-14c5-3290-bb14-f16cdb13c895 | -13.8369 | -44.5691 | 2024-10-09 01:56:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 1940be1b-e30a-364e-892d-4e6eb882fd60 | -13.8564 | -44.5657 | 2024-10-09 01:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 855b2fab-cb6f-3fcb-b2ab-c13ca2d368a6 | -14.1197 | -44.9637 | 2024-10-09 01:56:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| ff669585-f102-3b86-aec4-12ea4ab71c87 | -14.1392 | -44.9603 | 2024-10-09 01:56:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 121.5 |
| dc42ba7e-54bd-3c3e-a831-775c4cff53da | -15.5996 | -57.3699 | 2024-10-09 01:56:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 97307f2e-9230-303c-ab9a-c5857c6816b3 | -16.4184 | -55.9455 | 2024-10-09 01:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 31aa1fd8-00d6-3bc8-9f12-dd9e0480404f | -16.4187 | -55.9248 | 2024-10-09 01:56:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| c12b05f4-4040-3629-ab03-a679ea8e429f | -16.6871 | -57.4536 | 2024-10-09 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| b65250c3-e846-32b0-9c60-26620ddaa17f | -16.7067 | -57.4514 | 2024-10-09 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 5bbe19b6-4fda-3532-822b-9a3adfe410d6 | -16.8743 | -56.7352 | 2024-10-09 01:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.1 |
| 6371fc76-4b1e-3962-b41b-9e235d3a01ad | -16.8747 | -56.7146 | 2024-10-09 01:56:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 0061dd74-e441-3728-9cbc-054b6a505211 | -16.9211 | -57.4881 | 2024-10-09 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 54bb6f18-496b-30f2-88bb-29ffa5e7f191 | -16.9403 | -57.5063 | 2024-10-09 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| 17d8c19d-b533-34a7-9e5b-f6ba44912ae3 | -16.9407 | -57.4859 | 2024-10-09 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.6 |
| 7af4e5bb-91ce-3b9e-8c19-a641a1ee1b26 | -16.9603 | -57.4836 | 2024-10-09 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.5 |
| 8f1d0793-e824-3a7e-8e5a-0e24a71a791b | -16.9606 | -57.4631 | 2024-10-09 01:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.9 |
| e9bf5652-1292-368e-b05c-18730f813f59 | -17.1188 | -57.3628 | 2024-10-09 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 696f19df-16c1-3426-83af-b41d8c957d69 | -17.1271 | -56.8486 | 2024-10-09 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.3 |
| 27a76e99-18c3-345d-96ed-c45eefe80b5e | -17.1467 | -56.8463 | 2024-10-09 01:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| f13311fe-b2ef-3fb3-909a-c9d52852c29d | -17.1588 | -56.1222 | 2024-10-09 01:56:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 6ca31556-e75e-395d-a487-b007211e9266 | -17.335 | -55.0366 | 2024-10-09 01:56:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 48673744-f6b7-3322-907b-445e0527e1b2 | -17.3353 | -55.0156 | 2024-10-09 01:56:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 118.6 |
| a7a9c77e-be48-3859-a63c-7f6aee3050da | -17.3547 | -55.0339 | 2024-10-09 01:56:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 131.0 |
| c7fac737-5c09-317f-bbb5-e6224705858e | -17.3551 | -55.0129 | 2024-10-09 01:56:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 136.7 |
| 5d1b60b3-c850-307a-8e4b-78b62030932c | -18.1193 | -56.3921 | 2024-10-09 01:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| a7e3e926-eed2-38d9-ba96-e44b808c4246 | -18.6597 | -57.2137 | 2024-10-09 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 8f45f6fe-f3c7-34f7-bbc0-b2dd06c8ea71 | -20.2915 | -43.9444 | 2024-10-09 01:56:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.8 |
| 62f80e35-ecd6-33b4-961a-83998bf61f85 | -20.3121 | -43.9388 | 2024-10-09 01:56:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 121.7 |
| b9bb1444-5a64-3436-84e8-a3c406b35af3 | -20.3352 | -48.7076 | 2024-10-09 01:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 483.0 |
| 6784b701-fc5d-3cc7-a8be-4c4985a31057 | -20.3346 | -48.7307 | 2024-10-09 01:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 329.4 |
| 2dbc6561-936f-3967-90aa-a7d119898743 | -20.3551 | -48.7262 | 2024-10-09 01:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 364.8 |
| d7060dc4-38b0-3ae5-a52f-aeb9e1fd85e7 | -20.3557 | -48.7031 | 2024-10-09 01:56:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 341.7 |
| 7c2a106c-06c7-3064-a8f0-d28557a2984c | -20.3755 | -48.7217 | 2024-10-09 01:56:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 1bd5be8e-8782-3814-b2c5-1132388befb7 | -20.3761 | -48.6986 | 2024-10-09 01:56:59 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 761aea24-c8bd-3a6b-832e-5a00adb4c0e2 | -20.7839 | -47.2559 | 2024-10-09 01:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 96.7 |
| eb933323-3850-349d-8239-1f6b4084edf9 | -20.7846 | -47.2323 | 2024-10-09 01:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 221f34f9-f048-3d04-ba49-2256fc9f6792 | -20.8045 | -47.251 | 2024-10-09 01:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5531318f-8660-3bbb-86c3-7edcc460e6e1 | -20.8052 | -47.2273 | 2024-10-09 01:57:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 7ee89ec6-0c32-333e-8bbb-17452fc16b8e | -21.0919 | -47.228 | 2024-10-09 01:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8d06ec37-ba28-3832-8100-472594e48843 | -21.0926 | -47.2043 | 2024-10-09 01:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 882a94c8-7cd5-3681-97f2-b34a03617342 | -21.1126 | -47.2229 | 2024-10-09 01:57:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 87.9 |
| cec33e16-b36c-319f-8aff-1921f8b9b4b6 | -21.5727 | -46.9659 | 2024-10-09 01:57:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 105.7 |
| e095e895-b731-39c9-99fb-f9303a024eb3 | -21.5864 | -47.8827 | 2024-10-09 01:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 189c906f-ced9-3385-8efa-1f3b65dff5b8 | -22.8137 | -48.4225 | 2024-10-09 01:57:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 1514cb3b-32ae-33f2-8084-9c64b46c94d1 | -21.59 | -47.73 | 2024-10-09 02:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 273df048-5725-3122-a772-35e245d9a174 | -21.58 | -47.68 | 2024-10-09 02:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4436d5eb-81e9-3991-a073-c9e8b581f91f | -21.62 | -47.7 | 2024-10-09 02:03:21 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ef7ff4a3-4ccd-340f-891d-9aee5e23ba5d | -13.91 | -44.52 | 2024-10-09 02:04:03 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc6b9bdf-da0f-3caf-a9aa-6135467a4531 | -13.94 | -44.53 | 2024-10-09 02:04:03 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 84d4ab4b-9611-3efd-bb98-a6d32795851c | -12.01 | -51.08 | 2024-10-09 02:04:16 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee8b6a84-a335-3cbe-b8be-ebee404fdcef | -1.11 | -53.6173 | 2024-10-09 02:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 3c5f7b1a-74af-3df0-a123-9286290d29e2 | -1.1284 | -53.6171 | 2024-10-09 02:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c1c2baee-ab70-3b0d-b951-2bb153e4e8e0 | -3.8008 | -41.5989 | 2024-10-09 02:05:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| 92ffd368-7835-3334-87ad-601e3c09f88b | -3.8196 | -41.5979 | 2024-10-09 02:05:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 1825ea71-806d-3964-9a01-72b71814108e | -3.9021 | -46.4689 | 2024-10-09 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 4a209b2f-47b2-3861-aecc-8a59c128e1b5 | -3.9023 | -46.4467 | 2024-10-09 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1744c4c3-3e14-340a-a120-b7a3350caf34 | -3.9207 | -46.468 | 2024-10-09 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| c785196e-ee02-32b2-ae1a-c44230ba0c18 | -3.9208 | -46.4459 | 2024-10-09 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| aedaf9b2-6f67-3b22-82ff-c39b3bc963c8 | -3.9393 | -46.4672 | 2024-10-09 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9d5ee01e-7c76-3bd3-8b5a-f8a0d734be2e | -3.9394 | -46.445 | 2024-10-09 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 103.8 |
| e91615f9-0771-39fb-8907-7b9755debd01 | -6.7614 | -60.0559 | 2024-10-09 02:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 152.1 |
| 650ea9c4-6cfb-3057-bb1d-d7b29b6b6994 | -6.7615 | -60.0367 | 2024-10-09 02:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 77e3a284-2095-3e17-aab2-73031b603ccb | -6.7798 | -60.0552 | 2024-10-09 02:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 252.7 |
| aa1ca6a5-426b-3c4b-a17c-7691ed8b868a | -6.7799 | -60.036 | 2024-10-09 02:05:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 7233c7e2-9e35-30ac-9882-8ac764bef9e6 | -7.1873 | -59.7701 | 2024-10-09 02:05:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 236614d1-7fe3-3036-8165-13ec50b826a5 | -8.4919 | -48.6476 | 2024-10-09 02:05:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 113.5 |


[Clique aqui para ver as próximas entradas](README50.md)
