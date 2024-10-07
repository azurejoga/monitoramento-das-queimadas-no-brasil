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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0cb1c68-a64c-3b00-8073-1a07640eed1b | -16.9741 | -56.6202 | 2024-10-07 08:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.7 |
| 0173cc2a-9d60-38b7-951c-0e9d440b583f | -17.0123 | -56.6773 | 2024-10-07 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 171.1 |
| 254055d9-49ee-3312-96c0-96b1cfdeea55 | -17.0316 | -56.6956 | 2024-10-07 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.8 |
| 4a7db757-5fa4-3546-a8f6-d1abe0f101d8 | -17.0319 | -56.6749 | 2024-10-07 08:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.0 |
| dfd11f05-7526-3cc2-bb21-15ec35ff0270 | -17.178 | -57.3354 | 2024-10-07 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.2 |
| 7be4907e-69ae-3430-85d8-cc1465ee6fbc | -17.1777 | -57.3559 | 2024-10-07 08:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| bb10833e-076e-3619-a7fa-58bcc47782a6 | -17.1584 | -57.3377 | 2024-10-07 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.3 |
| 9b2cafe9-f109-3519-9b36-56cf6bec91a6 | -17.1274 | -56.828 | 2024-10-07 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| b6b9a895-5a79-3a20-a6ee-ce638a9b4b1f | -17.1278 | -56.8074 | 2024-10-07 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| 5b41ad4e-9d72-366f-bd2c-16e17c2c5b77 | -17.1581 | -57.3582 | 2024-10-07 08:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 4da056d8-3da0-3d97-9844-4fc5f34995c7 | -17.6675 | -53.1033 | 2024-10-07 08:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 1fb5618c-938a-3806-9487-f7c2d8d1777f | -17.6679 | -53.0819 | 2024-10-07 08:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 111.3 |
| dec55cf2-8a60-3f3b-ae5b-b36056ab90a2 | -17.6873 | -53.1003 | 2024-10-07 08:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 51ebb098-fe5b-3360-8263-5c01647c384c | -17.6877 | -53.0788 | 2024-10-07 08:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 6fe926bd-d95c-32c7-8111-eca058fea140 | -17.7662 | -53.1095 | 2024-10-07 08:36:46 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 49c0adbf-0154-332a-8820-d9c552b616ee | -17.786 | -53.1064 | 2024-10-07 08:36:46 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 5960b1b9-1ee3-33a2-9cf3-2bd6e737f92e | -16.5072 | -57.7387 | 2024-10-07 08:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| bb5cac40-908c-3eb4-871e-b6405a5db1fd | -16.5267 | -57.7365 | 2024-10-07 08:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| f9ea886d-e2e5-3126-b763-1aa4cbc8ab58 | -16.9741 | -56.6202 | 2024-10-07 08:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 140.5 |
| 13b645df-c7aa-3e14-a6f6-5e9dfa345355 | -16.9744 | -56.5996 | 2024-10-07 08:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 180.3 |
| 9846c9db-49bc-34ca-94ed-55451dc96b19 | -16.994 | -56.5972 | 2024-10-07 08:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| eaacff0b-dcf1-3c80-ae18-43dfdb7820a1 | -17.012 | -56.698 | 2024-10-07 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| 0cafcac4-4d1b-3fae-ae09-05075ad4e5d1 | -17.0123 | -56.6773 | 2024-10-07 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 143.8 |
| f3b2e6da-a14e-3e78-91db-05e6c0f7d78d | -17.0316 | -56.6956 | 2024-10-07 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 3357dd8f-114c-307c-a7e0-6928376fe0b6 | -17.0319 | -56.6749 | 2024-10-07 08:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.0 |
| a28ea9b0-529a-3fba-8480-8f030c0aadcc | -17.178 | -57.3354 | 2024-10-07 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 8b81069d-96ed-345e-a2e4-5768b977f092 | -17.0982 | -57.4267 | 2024-10-07 08:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.3 |
| bdde62b2-bcbf-3b70-afb2-763897910528 | -17.1274 | -56.828 | 2024-10-07 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 6e72a1ea-5632-38fc-a5dd-e8959f2b45cb | -17.1278 | -56.8074 | 2024-10-07 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 4bade95d-e5c0-31a5-a16a-9834abc80c4c | -17.1581 | -57.3582 | 2024-10-07 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.0 |
| 568c8af5-3c24-3bc2-9ce9-b84b7566c0cb | -17.1584 | -57.3377 | 2024-10-07 08:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 07e83179-7ae4-3cc3-86ae-1903669a568a | -16.8048 | -57.4197 | 2024-10-07 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.0 |
| 62b2e311-49be-3947-9995-59481ee14a8b | -16.8241 | -57.438 | 2024-10-07 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 74.1 |
| 1f9d5dd8-4d73-35ac-91c5-6c802481ae47 | -18.63 | -57.28 | 2024-10-07 09:03:41 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5f0a8e34-3e24-3adc-b21a-2b945fa5b173 | -10.8755 | -63.8979 | 2024-10-07 09:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 34d5e7ab-1ef3-3ffd-a579-f5956f1fa701 | -17.7922 | -53.7889 | 2024-10-07 09:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 1f226c0f-47ed-32ea-bd81-67b873826e67 | -16.9741 | -56.6202 | 2024-10-07 09:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 146.4 |
| df6b7413-7c11-34a5-bea5-435811cb6429 | -16.9744 | -56.5996 | 2024-10-07 09:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 227.2 |
| 1d9d082c-acc6-3e8c-8c19-74d7b97daa47 | -16.9937 | -56.6178 | 2024-10-07 09:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.2 |
| 87eb323c-16bf-378b-b74a-d649ad3e9d75 | -16.994 | -56.5972 | 2024-10-07 09:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 208.2 |
| 13e2cef5-4b1b-338b-b366-20236d907296 | -17.0123 | -56.6773 | 2024-10-07 09:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 140.3 |
| 13c9fb74-6e94-3b33-92dc-e31f7411ec6d | -17.0319 | -56.6749 | 2024-10-07 09:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 146.0 |
| 85d47fd1-9511-35e0-b479-f78927df150f | -17.1278 | -56.8074 | 2024-10-07 09:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| d5dd82ad-19fa-3149-bc62-91a36fd04ff5 | -17.7922 | -53.7889 | 2024-10-07 09:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 1b57e71c-d3d1-367d-aefd-04c21a7c2686 | -17.7918 | -53.8102 | 2024-10-07 09:36:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 54348fb6-37e3-3fa9-ae23-c191db5d2551 | -18.6192 | -57.2603 | 2024-10-07 09:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 163.1 |
| 5a2e3987-6535-3127-a60d-28945e43fa63 | -18.6391 | -57.2578 | 2024-10-07 09:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 143.6 |
| 122c96ae-c5b6-3673-8b1b-92584ededf79 | -16.9741 | -56.6202 | 2024-10-07 09:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 155.8 |
| 771214e1-e833-3c2c-bd4a-238398bab24e | -16.9744 | -56.5996 | 2024-10-07 09:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 197.4 |
| 76cfcbec-7d5d-33fc-9984-2f61c39ae8b8 | -16.9937 | -56.6178 | 2024-10-07 09:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 159.0 |
| 600b6025-d732-3039-90e3-36477d1a7e47 | -16.994 | -56.5972 | 2024-10-07 09:46:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 249.5 |
| 36590d5a-b852-3329-839d-dae18961e773 | -17.0123 | -56.6773 | 2024-10-07 09:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.8 |
| ac2ee61d-37b6-301b-aae1-57d98f1fafa1 | -17.0319 | -56.6749 | 2024-10-07 09:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 168.3 |
| 55d47ba2-5f2d-32e6-ad4b-a8df8bd70b36 | -17.7922 | -53.7889 | 2024-10-07 09:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 99ed0197-8166-32d2-ae72-d98845573d73 | -17.7918 | -53.8102 | 2024-10-07 09:46:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 69b6a6e5-a976-34fe-9cf9-9d52ca68d59d | -18.6192 | -57.2603 | 2024-10-07 09:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.7 |
| a43a8ca0-21c0-3e39-a6ff-c9006db0fa87 | -18.6391 | -57.2578 | 2024-10-07 09:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.3 |
| 0023ff2f-2f65-3668-be49-00f3a5336e33 | -20.486 | -47.6779 | 2024-10-07 09:46:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 2d955d4e-e5f2-3e95-9638-b8c179b7171f | -17.0319 | -56.6749 | 2024-10-07 09:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 153.5 |
| 3d51bd17-288f-3c05-99da-7eda7057f517 | -17.0123 | -56.6773 | 2024-10-07 09:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.7 |
| a3f112f4-c27a-3ff9-94f3-32e3ad56331e | -16.994 | -56.5972 | 2024-10-07 09:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 157.0 |
| 6b74ee93-153f-35e8-a483-24c153a57154 | -16.9937 | -56.6178 | 2024-10-07 09:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.8 |
| e837b3af-ce7a-397e-a088-4e6b43c11163 | -16.9744 | -56.5996 | 2024-10-07 09:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 174.4 |
| 4be4585e-6553-304c-9513-9e2e1daba740 | -16.9741 | -56.6202 | 2024-10-07 09:56:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 157.4 |
| 38af3044-399a-3653-89f0-c4b502b073e4 | -17.7922 | -53.7889 | 2024-10-07 09:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| d92b30e4-2df6-33dd-b7a6-920ef6104214 | -17.7918 | -53.8102 | 2024-10-07 09:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 156.0 |
| c66f9598-13e3-3556-b200-d88e877eacef | -18.6192 | -57.2603 | 2024-10-07 09:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 794a72ec-ab60-3348-b652-506570ce43fd | -20.486 | -47.6779 | 2024-10-07 09:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 172.5 |
| 706b0f22-9844-3f42-b983-901fc0a0be5b | -20.4853 | -47.7014 | 2024-10-07 09:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 32d162c6-ef04-35f7-ae90-02b9059666c5 | -20.4655 | -47.6827 | 2024-10-07 09:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 117.5 |
| c6775395-db98-3a46-b9a6-371fe35cb3f6 | -20.4648 | -47.7062 | 2024-10-07 09:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 125.4 |
| c9d58ad4-bbd3-32a3-87ac-e88623e9dd82 | -17.0319 | -56.6749 | 2024-10-07 10:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 158.8 |
| e5644f2f-ae2e-39c8-bb6f-caef50c52daa | -16.9744 | -56.5996 | 2024-10-07 10:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 150.4 |
| d18ac5a6-ec3d-3af4-a61d-2b0d87809da0 | -16.9741 | -56.6202 | 2024-10-07 10:06:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 145.0 |
| 9f1f4b9d-b5c5-3f99-a8b7-23b9c0789519 | -17.1274 | -56.828 | 2024-10-07 10:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 1f254ba7-3547-38e8-8f01-4b7ae5ae6327 | -18.6391 | -57.2578 | 2024-10-07 10:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.8 |
| 667cd1e8-2391-333b-a881-6c441ca18396 | -18.6192 | -57.2603 | 2024-10-07 10:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 1f16647e-b0a6-3d19-9bbd-47ef3fbf49c2 | -20.486 | -47.6779 | 2024-10-07 10:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 4311d986-b34d-3261-888c-3f5a4885c1e5 | -20.4853 | -47.7014 | 2024-10-07 10:06:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 0e0c4d17-ac59-3711-b201-0ec918b09e72 | -17.0319 | -56.6749 | 2024-10-07 10:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 145.0 |
| a9ec9f1a-b51f-3312-89f2-f41bb095a5c5 | -16.9744 | -56.5996 | 2024-10-07 10:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 133.4 |
| 6d99f111-e3f4-35d9-a780-48e7e0dfef37 | -16.9741 | -56.6202 | 2024-10-07 10:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 3fa0f91b-aabe-3c67-a3ae-cd6c646ffa80 | -17.1274 | -56.828 | 2024-10-07 10:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 7f6a8baa-692a-3768-bc1a-c0fc866eaba1 | -17.8314 | -53.8043 | 2024-10-07 10:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| f209bbb4-ac7d-303d-94f0-c42181e32435 | -17.7918 | -53.8102 | 2024-10-07 10:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| b6242bf5-612c-37c9-8798-6889fe7e29ce | -20.486 | -47.6779 | 2024-10-07 10:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 51795197-be6c-3d9a-8135-dcbc70583e8d | -20.4853 | -47.7014 | 2024-10-07 10:16:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 34822e21-2b78-361e-98c0-956c76a84e36 | -17.0123 | -56.6773 | 2024-10-07 10:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| a3449d70-b7db-3be5-b60a-b0c7ee93ec36 | -16.994 | -56.5972 | 2024-10-07 10:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 110.5 |
| 76ae931c-a4b5-34a5-b45e-3994774d9c76 | -17.0319 | -56.6749 | 2024-10-07 10:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 77762615-48f9-37a3-beea-65d3143552c9 | -17.1274 | -56.828 | 2024-10-07 10:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.9 |
| 5d6003c2-7682-3666-ad2d-4a117c50381c | -16.9744 | -56.5996 | 2024-10-07 10:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| a7bac73b-2c39-3500-9a54-c5dcbb1a6390 | -20.4853 | -47.7014 | 2024-10-07 10:36:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ab3385b0-4788-3cd0-b4eb-817b29c2b2ff | -17.1274 | -56.828 | 2024-10-07 10:46:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 132.5 |
| 9ed3584b-a247-3c22-b76d-1ebe40924711 | -21.3267 | -47.6176 | 2024-10-07 10:47:04 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 04a551fc-f690-3032-8b0d-9d06a777d310 | -17.8314 | -53.8043 | 2024-10-07 10:56:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| cc7d98ba-5a06-3231-b4d7-032f32eaacfa | -20.4648 | -47.7062 | 2024-10-07 10:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 122.6 |
| c082b985-6170-33bb-85c5-b9e9ce7bc8cf | -20.486 | -47.6779 | 2024-10-07 10:56:59 | GOES-16 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 26605a8b-ba10-3246-9f5e-bbc107858ec1 | -21.3267 | -47.6176 | 2024-10-07 10:57:04 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 143.6 |
| fdf4bae7-0d8a-3760-b8db-7195d6f04573 | -21.33 | -47.65 | 2024-10-07 11:03:21 | MSG-03 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README147.md)
