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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 649eb1af-75ff-34e2-8512-89fac84a8fb3 | -18.7172 | -57.3305 | 2024-10-01 06:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| e68c4e06-82c6-3052-89e0-47dc6f9978b6 | -19.1329 | -57.4628 | 2024-10-01 06:16:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| 4b586218-d62f-3d3a-a5b0-90f9e91227cf | -11.6555 | -64.9991 | 2024-10-01 06:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ef8b8439-a2a5-3799-a839-e4b320a74807 | -16.6525 | -55.958 | 2024-10-01 06:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| b3e84e91-fb6f-33ff-ae7c-566dc8f4f257 | -16.6515 | -57.233 | 2024-10-01 06:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 118e8fea-8630-3a4a-b55e-b49fb76d8e25 | -16.7528 | -55.8005 | 2024-10-01 06:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| 3ae0bb67-5add-3fc7-9454-b3703ceefef6 | -16.7724 | -55.798 | 2024-10-01 06:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| bfc95bc6-c1ad-3e1d-a52f-fce48077cbfd | -16.7728 | -55.7773 | 2024-10-01 06:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| d75d8143-373a-3479-9b5f-1e50b540b38a | -16.8787 | -57.6971 | 2024-10-01 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 7ee2368e-aaf3-362c-bb69-58148d20332a | -16.898 | -57.7153 | 2024-10-01 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 41.4 |
| b36f3934-7859-36db-8ab8-98728df49a81 | -16.8292 | -55.9152 | 2024-10-01 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.9 |
| ea42cce7-8643-39cf-a331-92f7b8512b0f | -16.8488 | -55.9128 | 2024-10-01 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.3 |
| 82b22924-fa8b-3a11-888b-8530513561fb | -16.8491 | -55.892 | 2024-10-01 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.0 |
| f62949e1-c4a3-307a-89b7-7b43855fb145 | -16.8983 | -57.6949 | 2024-10-01 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.0 |
| d51aff51-3463-3f71-a473-e562973a68ed | -16.8684 | -55.9103 | 2024-10-01 06:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| c795e268-8ba8-3a10-84fd-50c1d6ca5be4 | -17.0895 | -56.7503 | 2024-10-01 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| bf028b44-d757-34e5-9b52-14d8ab964d5e | -17.0898 | -56.7297 | 2024-10-01 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| c7056cb2-a10d-330c-b96a-a513f08fb087 | -17.0902 | -56.709 | 2024-10-01 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.0 |
| cd3ec8f4-5894-34af-84f7-56099d517eb3 | -17.1095 | -56.7273 | 2024-10-01 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 58.7 |
| 7fa43f4b-395a-3dd0-8c11-75f9dd914448 | -17.0702 | -56.7321 | 2024-10-01 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| c200b4ed-a172-3d3a-98fe-f0fdaf6120ee | -17.0705 | -56.7114 | 2024-10-01 06:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| a90e2e3e-11be-30a7-bd73-2d58df63f951 | -18.6973 | -57.333 | 2024-10-01 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.8 |
| 5568b9cf-4ba7-3ea0-8b59-bc337ee54a51 | -18.7172 | -57.3305 | 2024-10-01 06:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.3 |
| b4f35fc5-6916-34c3-a3f3-7b6416867274 | -19.1329 | -57.4628 | 2024-10-01 06:26:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 6e3700a4-5db1-33fa-9161-f37e6c7f5e0a | -11.6555 | -64.9991 | 2024-10-01 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e5560e7d-29e1-355f-8aec-979c1bd6c5f2 | -11.6743 | -64.9983 | 2024-10-01 06:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 030ba2c9-5615-31fb-89db-7ef053ab9ea8 | -16.7728 | -55.7773 | 2024-10-01 06:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.4 |
| ed46fd24-5cfe-3231-9795-467b80748035 | -16.7528 | -55.8005 | 2024-10-01 06:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| 49163e85-b7a3-3d86-b117-3ebb48afeae7 | -16.7724 | -55.798 | 2024-10-01 06:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 8cef9b77-4008-3004-8e3c-f0cab1a7a156 | -16.8292 | -55.9152 | 2024-10-01 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.2 |
| 99cc25da-1dd6-3604-9f8b-6319725867e8 | -16.8488 | -55.9128 | 2024-10-01 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.8 |
| af5413ef-e2a3-312b-8b9e-a9d9672b1079 | -16.8491 | -55.892 | 2024-10-01 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 2e890b8d-d7c3-3175-bc7f-14ff00204f8c | -16.8684 | -55.9103 | 2024-10-01 06:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.1 |
| 7c5807cb-6ac2-3b54-a745-c83894884f6e | -17.0705 | -56.7114 | 2024-10-01 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 1d0ebbf9-867d-3943-8814-6dd08631ce34 | -17.0895 | -56.7503 | 2024-10-01 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| d5ea99e7-5bdb-38b9-875f-eb6996c6afb1 | -17.0898 | -56.7297 | 2024-10-01 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.4 |
| d0c466b0-7958-308f-ad5b-3ff2af207393 | -17.0902 | -56.709 | 2024-10-01 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.8 |
| 0a40ba88-ece1-3719-9366-6ff114afedfa | -17.1095 | -56.7273 | 2024-10-01 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| 9a8931ca-64a5-39a8-a96e-c7f52af56f9a | -17.0702 | -56.7321 | 2024-10-01 06:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 62908292-dcdb-3a58-9120-5627b54cef8c | -17.705 | -53.2046 | 2024-10-01 06:36:45 | GOES-16 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6f4f6428-b6d1-3b79-8335-6715a58f70f7 | -22.3707 | -49.3244 | 2024-10-01 06:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 199.5 |
| 526f6d7e-9faa-31dd-805d-eec92aa36c95 | -22.3713 | -49.3011 | 2024-10-01 06:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.9 |
| 49869a92-05cf-3026-bf45-e02c784e6fc1 | -9.35035 | -68.84061 | 2024-10-01 06:46:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21efd937-2da7-3053-9303-2e9ba8b81d6c | -10.71168 | -69.42104 | 2024-10-01 06:46:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afea63d0-b650-39b1-8686-c2bf43b9ea05 | -10.71103 | -69.42674 | 2024-10-01 06:46:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f706bea-b032-3e98-9869-337f7a2bd9f2 | -10.70893 | -69.40946 | 2024-10-01 06:46:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4161f47d-6864-39fa-bc62-b6ae3ef427df | -10.70822 | -69.41537 | 2024-10-01 06:46:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be9dee89-91e6-37a0-b0f8-74f1e1c17ee2 | -10.70752 | -69.42119 | 2024-10-01 06:46:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 49db4c60-23b8-39db-a3fb-62cab7bb03b0 | -10.70506 | -69.41987 | 2024-10-01 06:46:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 186d6300-0840-394b-aaee-aafbc12d5568 | -11.6555 | -64.9991 | 2024-10-01 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 7963428c-aa45-39cc-8638-ffa70867115a | -11.6556 | -64.9802 | 2024-10-01 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 58549b14-705e-3fb0-9111-422570e94581 | -11.6743 | -64.9983 | 2024-10-01 06:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 0d11b4dd-2fa5-3643-8ffc-0f6bb9c0ece4 | -16.7724 | -55.798 | 2024-10-01 06:46:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 3eb825e6-ee28-3c9d-b708-c2d5570ac52f | -16.8488 | -55.9128 | 2024-10-01 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.4 |
| 44fdd474-3827-3120-9d20-8dbd02907a21 | -16.8292 | -55.9152 | 2024-10-01 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| 3b8fd44a-805c-3e6d-ae8d-6f156751f680 | -16.8491 | -55.892 | 2024-10-01 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 43.1 |
| 832c63cd-c825-3364-859f-69ec665536f1 | -16.8295 | -55.8945 | 2024-10-01 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 40.9 |
| 5878e806-5be0-3da6-93ed-b21ec25ac574 | -16.8684 | -55.9103 | 2024-10-01 06:46:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 286f2a9e-9014-3fe0-aa0b-e1c57ed5d1b5 | -18.6973 | -57.333 | 2024-10-01 06:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.9 |
| 53a817b1-1056-303b-893e-46f32aef5d2c | -21.6078 | -47.854 | 2024-10-01 06:47:05 | GOES-16 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 387efb2e-b12c-35ae-a5fd-5a1f69f8b8c7 | -22.37 | -49.3477 | 2024-10-01 06:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| 20d754d3-de6a-3114-9ccf-07e44d1007b3 | -22.3707 | -49.3244 | 2024-10-01 06:47:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 197.6 |
| 2b471b15-b87b-3a1e-994a-b4c63b41eda3 | -22.3713 | -49.3011 | 2024-10-01 06:47:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 127.4 |
| aa8b1436-aa47-3e5a-b68a-62c88a1b5548 | -11.6555 | -64.9991 | 2024-10-01 06:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d904bbd3-c3e3-391e-9a11-c9c0deb16132 | -16.8684 | -55.9103 | 2024-10-01 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 237731bc-ad13-3037-88ea-16e78361c077 | -16.8488 | -55.9128 | 2024-10-01 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 31df01a2-73bd-31d9-9c70-f223900c75fa | -16.8292 | -55.9152 | 2024-10-01 06:56:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 48.9 |
| f0b09581-e609-38a3-b200-a0b1f6c6f98a | -17.0702 | -56.7321 | 2024-10-01 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.3 |
| 97057412-c8b6-30f7-b409-398b7f3267fb | -17.1095 | -56.7273 | 2024-10-01 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 47e0efd3-7538-363c-bfd0-30e8d5ebef56 | -17.0902 | -56.709 | 2024-10-01 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 2417976c-d5c9-3a0b-bf69-83ea432d64ce | -17.0898 | -56.7297 | 2024-10-01 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 1a0dd4f6-c7c8-3b12-9aba-aa12c382032a | -17.0895 | -56.7503 | 2024-10-01 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.7 |
| ecc1e4ee-2372-347c-b04d-08d707e2bd3a | -17.0705 | -56.7114 | 2024-10-01 06:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.8 |
| d6fe766b-46be-350c-9836-877ce97e9a2f | -18.7176 | -57.3097 | 2024-10-01 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 3528e7c7-57cf-3940-aa84-503a6a7328b1 | -18.7172 | -57.3305 | 2024-10-01 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| b9f0e26d-abc1-31e4-bd4e-a6c94014f982 | -18.6977 | -57.3123 | 2024-10-01 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 30b148d6-128d-3513-87e7-841a2e139856 | -18.6973 | -57.333 | 2024-10-01 06:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 60e6817d-adcf-3f58-9c39-be30ac2f143c | -22.3713 | -49.3011 | 2024-10-01 06:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.8 |
| c2c6ee75-344b-35f6-b8e0-8321ab987268 | -22.3707 | -49.3244 | 2024-10-01 06:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 161.1 |
| c5b89941-01fa-30e0-89c0-806d9c037821 | -11.6555 | -64.9991 | 2024-10-01 07:06:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| afb3fe95-1111-35b0-abdf-abaad4489b52 | -16.474 | -57.3553 | 2024-10-01 07:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.7 |
| 08393938-d044-3550-a466-150300329f38 | -16.4939 | -57.3327 | 2024-10-01 07:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 75db932f-4937-368a-bde2-1644d02de1dd | -16.4935 | -57.3531 | 2024-10-01 07:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.3 |
| af1b7100-1a3c-3f16-84d4-0dab86595bd6 | -16.4743 | -57.3349 | 2024-10-01 07:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 2ebc2054-dcc5-3778-997d-013a671e4588 | -16.7724 | -55.798 | 2024-10-01 07:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| 6edadc33-fa60-3008-967c-2601f8d3caba | -16.8684 | -55.9103 | 2024-10-01 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 6df2f8d7-be92-36a4-8203-daa89ce5e9c3 | -16.8488 | -55.9128 | 2024-10-01 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 6a76de02-a088-301d-aa8b-f7a0ca8e717b | -16.8292 | -55.9152 | 2024-10-01 07:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 6f386f6a-aa6d-36a4-9dc3-548d48d311b0 | -18.7172 | -57.3305 | 2024-10-01 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| af966bcb-0c10-3499-a740-d42568c734e3 | -18.6973 | -57.333 | 2024-10-01 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.1 |
| a07decb0-ddf9-38b4-b986-ac4e588aa70f | -18.6977 | -57.3123 | 2024-10-01 07:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| f0336496-9ec2-3c39-a9c7-399683cacfb5 | -22.3922 | -49.2961 | 2024-10-01 07:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.1 |
| 88cf22b9-74fb-3a7b-bcde-1073de9ebb1c | -22.3713 | -49.3011 | 2024-10-01 07:07:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| 1c259b2b-7f14-3602-918b-d89798b97329 | -22.3707 | -49.3244 | 2024-10-01 07:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 163.6 |
| a12374d4-297e-3e52-ada0-1e21dbfb9b1c | -22.37 | -49.3477 | 2024-10-01 07:07:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| d8bc0e7c-1e31-3a1c-981d-4208e5e7f8a8 | -16.474 | -57.3553 | 2024-10-01 07:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| bf3978ba-457a-3145-a680-126f30fcd798 | -16.4935 | -57.3531 | 2024-10-01 07:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| df83f1f6-43dc-3fa0-90d3-0b7ffd9e9c5c | -16.4939 | -57.3327 | 2024-10-01 07:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| c3fa4b06-8c3b-312e-88cf-6ba3c1010e64 | -16.7724 | -55.798 | 2024-10-01 07:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| e136eca1-6b98-3bd3-a8dc-75b9b1697cf2 | -16.7728 | -55.7773 | 2024-10-01 07:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |


[Clique aqui para ver as próximas entradas](README158.md)
