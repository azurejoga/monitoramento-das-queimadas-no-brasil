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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72f1318b-82d0-3969-88f6-271d05695470 | -13.888 | -45.8388 | 2024-10-15 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d5e92e32-98ca-3c55-a9bb-73ef85e998b9 | -13.9075 | -45.8355 | 2024-10-15 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| 7e4d5fa4-f885-362a-87ed-439f6d33c2e6 | -13.9079 | -45.8124 | 2024-10-15 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| ba9df9b0-207d-39c6-a8ff-86b891dd7c30 | -13.9269 | -45.8323 | 2024-10-15 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 3a2d4015-059d-32c0-8352-2a3c323435a7 | -13.9274 | -45.8091 | 2024-10-15 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 17e553cd-cc77-3509-a9c4-c61fe3fd0156 | 1.0016 | -52.2164 | 2024-10-15 02:15:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 77.9 |
| cba7d826-70cc-3546-bb2e-9b4d24a24e40 | -3.1099 | -54.2263 | 2024-10-15 02:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 147cd0ad-5779-3583-9784-ae805ffca297 | -3.11 | -54.2063 | 2024-10-15 02:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 232d743e-e899-3fdd-ba81-45155eea112b | -3.1282 | -54.2459 | 2024-10-15 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| a6fa5805-b8c6-3478-9d43-c5384e49131a | -3.1283 | -54.2259 | 2024-10-15 02:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1e63e387-56fe-35af-93f3-f6864fe0160d | -3.7218 | -48.9979 | 2024-10-15 02:15:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 33d3d7ff-8793-341f-9eb5-b1c09a125e74 | -3.9396 | -46.4229 | 2024-10-15 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2c0b1bbd-415f-3648-8b81-d7898d45f61d | -5.5732 | -49.3995 | 2024-10-15 02:15:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 02ffd795-9d55-34b5-ae36-08826d37854a | -6.6326 | -60.0224 | 2024-10-15 02:15:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 3dfd5ee4-83b7-3e6e-9df1-0933a7c2a99f | -9.3801 | -40.4246 | 2024-10-15 02:15:58 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 3c66e9e2-66bd-3997-8546-c2cd19ef8e89 | -9.9484 | -48.1322 | 2024-10-15 02:16:02 | GOES-16 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 948bb8f6-ffa9-3431-a6fe-6b395dcc6906 | -10.0415 | -54.3442 | 2024-10-15 02:16:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3a0327af-ef37-3470-ab9e-254e4daa060c | -10.3954 | -44.8206 | 2024-10-15 02:16:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| af29562d-9530-39fd-9b6d-c356e56efdf8 | -10.3711 | -61.1935 | 2024-10-15 02:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| baa5c5ac-f0e3-37be-a3d2-fcb5eac4337a | -10.3713 | -61.1743 | 2024-10-15 02:16:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7b6c2e06-4616-39b8-b84d-7cecf6beae9f | -10.822 | -49.256 | 2024-10-15 02:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a619fdcd-232f-34be-bbc0-5c949d6a899d | -10.8224 | -49.2343 | 2024-10-15 02:16:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 47cdcbdd-e680-33f3-af69-f25e7baf6ddf | -11.6915 | -65.2432 | 2024-10-15 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3a326039-6110-3bf0-87ef-bc29f59dec34 | -11.6917 | -65.2243 | 2024-10-15 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| d9b67263-c3e6-33b4-bd8e-db6886f7a969 | -11.7104 | -65.2235 | 2024-10-15 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| dfcfa5e3-a14c-374e-a765-2a500cd06b1c | -12.3983 | -63.7093 | 2024-10-15 02:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e36c867a-a43b-3689-8f61-d74926fa8d04 | -12.4602 | -63.0361 | 2024-10-15 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| e8422e27-39f8-3025-a7f9-96b30cda6fec | -12.4603 | -63.0169 | 2024-10-15 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a6b50626-5628-3d8d-b7c1-3b86f5707eeb | -12.515 | -63.263 | 2024-10-15 02:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 55e4980e-ab7d-3e04-8783-4412e5f17029 | -13.888 | -45.8388 | 2024-10-15 02:16:23 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| aa6f81c4-7cb0-339c-9f23-403f0e7d520d | -13.9075 | -45.8355 | 2024-10-15 02:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 4e122cf4-8ca3-32ef-a221-6948db5dbccc | -13.9079 | -45.8124 | 2024-10-15 02:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 3cc42050-1359-37d7-a528-5a6648e83044 | -13.9269 | -45.8323 | 2024-10-15 02:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 6c3ade3a-789e-30be-926f-a72f3df27ba4 | -13.9274 | -45.8091 | 2024-10-15 02:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| d0bc9a6b-a71c-31a8-8127-69c8eac881e7 | -17.8648 | -57.4171 | 2024-10-15 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| fb1e0a7b-8324-3435-a3fa-61bfb4900636 | -17.8845 | -57.4146 | 2024-10-15 02:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.7 |
| 6dfb5265-b5b1-3441-93c3-36408bca2496 | -17.8644 | -57.4377 | 2024-10-15 02:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 5b749301-dbcb-35ed-813e-0d1043f5a730 | 1.0016 | -52.2164 | 2024-10-15 02:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 390f909c-58e3-32a2-b6dd-01d860c19f49 | -2.501 | -49.0802 | 2024-10-15 02:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b2f9b551-94c5-3c05-97f2-1ac13778fbad | -2.6674 | -49.0544 | 2024-10-15 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| fcf4a666-264d-3706-8105-5a236ad6b658 | -2.6859 | -49.0539 | 2024-10-15 02:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 67bf8d4b-e5c1-3ecc-a3ff-078d62d0478e | -3.1099 | -54.2263 | 2024-10-15 02:25:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| c9a02e89-c544-366f-b4a2-5f9888ff92dd | -3.1282 | -54.2459 | 2024-10-15 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0f84f58f-4580-33ed-a5d9-e192da4433d9 | -3.1283 | -54.2259 | 2024-10-15 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 8a32eaa1-224a-35bb-bfa1-4cbf09acfcde | -4.5334 | -46.5927 | 2024-10-15 02:25:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0f8d1db1-2c95-373d-8b1e-37129a7f6b26 | -5.5732 | -49.3995 | 2024-10-15 02:25:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| e68140dd-0d40-31ce-8acc-863e986a748b | -6.6701 | -49.4586 | 2024-10-15 02:25:44 | GOES-16 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| e0c1170a-a9aa-325b-af4a-d6f889ab4443 | -10.0415 | -54.3442 | 2024-10-15 02:26:03 | GOES-16 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 8318fea1-6a8b-3765-9a4e-e8bd9307dd58 | -10.3954 | -44.8206 | 2024-10-15 02:26:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 154809a4-345a-348a-b443-2d957041a2c1 | -10.3711 | -61.1935 | 2024-10-15 02:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 1a451f39-8c89-3f15-95f4-0430fa9f29b9 | -10.3713 | -61.1743 | 2024-10-15 02:26:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 8057b6e5-0c75-3612-a114-447f3c122d60 | -10.822 | -49.256 | 2024-10-15 02:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 53ceb858-cb90-353a-91b2-941575dc7b11 | -10.8224 | -49.2343 | 2024-10-15 02:26:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 2417e7b5-8840-37aa-8d62-f9539af0818a | -11.6915 | -65.2432 | 2024-10-15 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 882a3564-265c-32fd-a523-0cada74dcaa0 | -11.6917 | -65.2243 | 2024-10-15 02:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| c4399af9-1960-3d6f-9c6d-269598e0c85c | -12.099 | -50.2728 | 2024-10-15 02:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 493d39ab-c365-3287-be09-6938ee45ee39 | -12.1181 | -50.2705 | 2024-10-15 02:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 7147a7ea-09af-342f-96aa-9c77fa40e68c | -12.1185 | -50.2489 | 2024-10-15 02:26:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 05d59bb8-9c52-3dd6-8873-b789e429fee9 | -12.4602 | -63.0361 | 2024-10-15 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7a11f03d-5ca7-33d1-aef0-67decaa2e4c9 | -12.4603 | -63.0169 | 2024-10-15 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 5f82081a-8956-3d5a-925d-4ddb2bc86d31 | -12.515 | -63.263 | 2024-10-15 02:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 224470cf-0942-3992-a96d-3e46c2eb9f31 | -13.9075 | -45.8355 | 2024-10-15 02:26:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 5d370304-b886-391e-899f-84e75b2f8fb3 | -17.8648 | -57.4171 | 2024-10-15 02:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 5c50c0b6-4610-366c-a99d-585758cf8d39 | -17.8447 | -57.4401 | 2024-10-15 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 135.9 |
| f62a389b-991c-3a58-83a0-084c157f7ee6 | -17.845 | -57.4195 | 2024-10-15 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 152.3 |
| 646c231d-1d0c-377a-b9a1-d4694eeb1f1d | -17.8644 | -57.4377 | 2024-10-15 02:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 422be86b-ab59-3a47-9e0b-868f10db9ba0 | -20.3121 | -47.3448 | 2024-10-15 02:26:58 | GOES-16 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 13846c87-00e5-3909-b657-7ce32f03cf6e | -20.3128 | -47.3212 | 2024-10-15 02:26:58 | GOES-16 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 70.6 |
| b2fcb3da-1474-3170-90ed-3884aef63d82 | -20.3326 | -47.34 | 2024-10-15 02:26:58 | GOES-16 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 34c409d7-62f6-370c-a540-821ec5f651b9 | 1.0199 | -52.2162 | 2024-10-15 02:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 8d96747b-7134-3e8c-80ce-03b0a2ebdb32 | 1.0016 | -52.2164 | 2024-10-15 02:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9d2641e0-a5db-37a2-98ce-a549cfb32216 | -3.1099 | -54.2263 | 2024-10-15 02:35:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 0c508112-a6f1-3aad-8db2-e1364d0663bd | -3.1282 | -54.2459 | 2024-10-15 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 207389fa-f01a-395e-8da6-92b3b31f3924 | -3.1283 | -54.2259 | 2024-10-15 02:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 4f2dfd5d-f833-39ab-9758-06bba82f538e | -4.5334 | -46.5927 | 2024-10-15 02:35:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 8aa9c153-b6e2-329c-b1ab-3c44f35815dd | -4.5336 | -46.5706 | 2024-10-15 02:35:31 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 77.6 |
| e08d9071-9006-3121-8795-5378bfa3b647 | -6.6701 | -49.4586 | 2024-10-15 02:35:44 | GOES-16 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ff410b06-406f-3a78-affb-214e34b24b82 | -6.6325 | -60.0416 | 2024-10-15 02:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6c69a8ed-bceb-32c7-a5c0-12d75a8ea0e4 | -10.3954 | -44.8206 | 2024-10-15 02:36:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 62fc7393-b256-3a26-b4cc-84d5336b501f | -10.3711 | -61.1935 | 2024-10-15 02:36:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 136.3 |
| d909cfab-f725-308c-807d-7dd2e05816f2 | -10.822 | -49.256 | 2024-10-15 02:36:07 | GOES-16 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dbb40d80-b2cd-3da4-b57d-dc93b24d6047 | -11.6915 | -65.2432 | 2024-10-15 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 36d6e80a-8a97-3478-9b72-c2c062db4745 | -11.6917 | -65.2243 | 2024-10-15 02:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 2d01bb33-85c9-3f1f-bdfc-6ebf19dd29b8 | -12.099 | -50.2728 | 2024-10-15 02:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f1f1d96e-8c59-349b-bcc6-6fa4fdafb25c | -12.1181 | -50.2705 | 2024-10-15 02:36:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| c7936c6a-9f3b-398d-84ab-e75ea98296c6 | -12.5149 | -63.2822 | 2024-10-15 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 9482dfde-2e28-3202-86bb-6e632b4a9e26 | -12.515 | -63.263 | 2024-10-15 02:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 138cab52-2202-3339-b9e0-418f8616bb32 | -13.9075 | -45.8355 | 2024-10-15 02:36:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 2c87cbf1-9739-3e53-90ab-491fd0d43390 | -7.04274 | -35.12096 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9d6c3e15-7a81-39ec-a093-ba826b241664 | -7.04181 | -35.12366 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 160b493b-4f65-379e-9ede-646ca4100629 | -7.04127 | -35.12857 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| fdd0dc30-e7dc-34b5-8c49-bdcfc5ed5f9b | -7.04043 | -35.13111 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 57de44c8-2713-3cde-9c67-f29b6cf28ee7 | -7.03554 | -35.11932 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b00a429e-15b6-3c1e-85bf-3bdb6fa25567 | -7.03465 | -35.12183 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0619851f-7c21-3a0b-943c-5d7201485a79 | -7.03417 | -35.12644 | 2024-10-15 02:43:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| a0326742-e80a-3408-9d3b-abf1dbddb69e | 1.0016 | -52.2164 | 2024-10-15 02:45:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3446e6f6-6def-307c-99bf-ede4012eee13 | -2.4418 | -50.2447 | 2024-10-15 02:45:20 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 359029f1-a6a6-3b46-8ef9-e60ec59a34f8 | -3.1282 | -54.2459 | 2024-10-15 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 9872d284-0c25-3edb-ad95-e8540f93fdff | -3.1283 | -54.2259 | 2024-10-15 02:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 0f99d3b0-eaba-36a7-95ad-b0f0d772b31f | -3.9396 | -46.4229 | 2024-10-15 02:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.9 |


[Clique aqui para ver as próximas entradas](README21.md)
