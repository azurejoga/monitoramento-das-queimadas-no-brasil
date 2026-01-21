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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e88ceb1-2efe-330e-97e2-dde41cc61b3c | -18.8116 | -51.61292 | 2026-01-21 05:16:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a084f41-aab7-3a51-9fb3-41288efbcd14 | 3.34648 | -60.05109 | 2026-01-21 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7ead5f1-cdea-3280-b3b8-d6e062f961c5 | 3.33233 | -60.08742 | 2026-01-21 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2776482-7c62-3ea8-bbc2-267134c383fc | 2.54655 | -60.57111 | 2026-01-21 06:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78ac8925-3149-3efd-ae70-ca7e1ffd923a | 2.54175 | -60.57191 | 2026-01-21 06:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d521e36b-7531-38bd-bafc-9c59133bf130 | 3.34159 | -60.05197 | 2026-01-21 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58bb1636-15fd-3d36-897e-61e35561f470 | 3.33632 | -60.0811 | 2026-01-21 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebf17787-30a9-3acd-bf25-7c28bf2db875 | 3.34249 | -60.05746 | 2026-01-21 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58c6f9c5-a977-3abe-9114-51d1a45cebe2 | 4.42649 | -60.60955 | 2026-01-21 06:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aab5e87a-8532-3a0d-971d-ff573dafc359 | 4.42071 | -60.61742 | 2026-01-21 06:29:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71d027da-0879-34b6-9516-9fb7cc168b7e | -19.4244 | -57.20361 | 2026-01-21 06:41:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 8512b6d2-9864-3530-a3b5-efaa64d8199e | -19.64763 | -56.95499 | 2026-01-21 06:41:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 6ef4466a-4519-3b93-988d-f2c43b581e88 | -20.33335 | -57.89284 | 2026-01-21 06:41:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 31db3e95-63ad-348c-8634-2c876e7cb7f8 | -19.43146 | -57.27954 | 2026-01-21 06:41:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c97aa03d-830b-34ca-9f81-2ffda24287ea | -20.33488 | -57.8831 | 2026-01-21 06:41:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 3fddf7af-376f-3083-a533-ebf00ca90dd9 | -19.66793 | -56.88169 | 2026-01-21 06:41:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| d8a71738-f1b9-3a01-bd0f-d9083ec6c471 | -20.31539 | -57.88968 | 2026-01-21 06:41:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| f8fe7c35-8345-33d3-aa9b-6e43f2fb6b89 | -19.65646 | -56.95649 | 2026-01-21 06:41:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 4adfd794-f598-3d5a-835f-eec54632dd3b | -19.43295 | -57.27007 | 2026-01-21 06:41:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 1937057b-ef6b-36b0-895c-cd230ad39574 | -19.6665 | -56.89103 | 2026-01-21 06:41:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1ecb2f53-55d7-34e5-81c4-907f62d80584 | -19.6579 | -56.94713 | 2026-01-21 06:41:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| dfc0ccb9-0bdb-3dbb-bf3f-da73a6b0a7e1 | -15.9708 | -56.27216 | 2026-01-21 06:41:00 | AQUA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| eb5e6395-afc2-3802-925f-147cc6982b40 | -19.6619 | -56.9541 | 2026-01-21 08:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| c1325d8f-14e7-399b-b350-3a6d45de60e2 | -19.6619 | -56.9541 | 2026-01-21 08:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 146ec900-a514-3c7c-9c89-3407d03b51cb | -19.6619 | -56.9541 | 2026-01-21 08:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 984b9bd3-59e3-3a0f-8d94-be8d02830e9e | -19.6619 | -56.9541 | 2026-01-21 11:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 428346e6-f675-3d8f-8a0e-e94d8e1fff65 | -4.12594 | -38.35847 | 2026-01-21 11:34:00 | TERRA_M-M | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1aaa7b02-0ad4-3a7d-9b34-1fb3e9411eb8 | -6.54462 | -37.42646 | 2026-01-21 11:34:00 | TERRA_M-M | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 17.3 |
| f9ac76f1-144c-376a-bfa3-3dae016df1b4 | -9.0967 | -36.68999 | 2026-01-21 11:34:00 | TERRA_M-M | TEREZINHA | PERNAMBUCO | Brasil | 2615102 | 26 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 53a0e204-1723-3e2a-9323-1dc9738fa6ab | -9.16045 | -37.49464 | 2026-01-21 11:34:00 | TERRA_M-M | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8a49e595-2a43-356d-a63e-dd8ced5c657c | -7.91878 | -37.61405 | 2026-01-21 11:34:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 36ad64bc-73be-3d3b-8b31-4e4a9d5453f8 | -6.40644 | -37.82104 | 2026-01-21 11:34:00 | TERRA_M-M | BREJO DOS SANTOS | PARAÍBA | Brasil | 2502904 | 25 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ef0d9633-7c4f-3406-a137-2fb2213c3565 | -4.03989 | -40.21885 | 2026-01-21 11:34:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 535344e9-219b-3a85-96fb-140514b7de04 | -7.91747 | -37.62343 | 2026-01-21 11:34:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 9203b558-b6dc-3c99-adc4-dfb96d917c10 | -4.03845 | -40.22864 | 2026-01-21 11:34:00 | TERRA_M-M | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 50.9 |
| c5c2048e-c325-3423-abe0-560092f2eb94 | -5.03027 | -38.54682 | 2026-01-21 11:34:00 | TERRA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| d240671b-079b-3572-8c19-d86b656935ca | -19.6619 | -56.9541 | 2026-01-21 11:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 186.2 |
| 30869a3b-1e3f-3bc1-a124-675c0396f1f2 | -19.4357 | -57.2771 | 2026-01-21 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 11b0ce90-6c11-3ccd-b682-b619e1e6f6d0 | -19.4354 | -57.298 | 2026-01-21 11:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 8e32a590-7130-3a23-9001-abf57114a31a | -19.4354 | -57.298 | 2026-01-21 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.8 |
| 6ca442cf-708c-39e7-8f88-4b138a3b1819 | -19.4153 | -57.3007 | 2026-01-21 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 117.4 |
| 85990d06-07f0-3411-bac6-adcfe52c15ed | -19.6619 | -56.9541 | 2026-01-21 11:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 125.5 |
| 4037b630-37b6-3070-9b4d-9bfb4b371b9d | -19.4357 | -57.2771 | 2026-01-21 11:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.7 |
| ed06005e-1e1f-3ba6-b070-49cf56fa4365 | -19.4354 | -57.298 | 2026-01-21 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.5 |
| 762e8516-7c26-3391-8fa7-ecbe184f9360 | -19.4357 | -57.2771 | 2026-01-21 12:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.2 |
| ab8fda75-e585-37f6-a70d-ae7a9d31723f | -19.6619 | -56.9541 | 2026-01-21 12:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 162.2 |
| f87cfa10-07ba-3880-a6f0-007ac478eef5 | -19.6619 | -56.9541 | 2026-01-21 12:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 281.6 |
| 82615357-197c-347f-8ba9-09b06f734220 | -19.6418 | -56.9569 | 2026-01-21 12:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 100.9 |
| c2b1eb40-b15f-30c2-8682-01d6440b43c0 | -19.6418 | -56.9569 | 2026-01-21 12:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 106.5 |
| 45988944-9183-37b3-87b7-a0a41f370414 | -19.6619 | -56.9541 | 2026-01-21 12:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 336.1 |
| ad911487-e732-38ed-a9be-9e2aa16f22c8 | -19.6619 | -56.9541 | 2026-01-21 12:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 476.4 |
| 94007bb2-f1b6-3174-98a1-707ae518cc73 | -19.6418 | -56.9569 | 2026-01-21 12:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 151.1 |
| 93194aab-f9ec-3ea2-a1c9-e228d380ec66 | -19.6418 | -56.9569 | 2026-01-21 12:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 141.7 |
| 84a9135b-0d24-3257-a9b2-3a7f2695a35a | -19.6619 | -56.9541 | 2026-01-21 12:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 470.7 |
| 600d2b80-51c4-38e4-adc6-6eb0f0a70d34 | -20.3481 | -57.9033 | 2026-01-21 12:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.1 |
| 684a4793-9d45-3142-977b-8ae8a4b46188 | -19.6623 | -56.9331 | 2026-01-21 12:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 94.6 |
| 0f77063a-823c-3449-8a28-a05911b125a1 | -19.6418 | -56.9569 | 2026-01-21 12:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 145.6 |
| 20d70d8f-99fc-3d2f-9d62-276ab4bb6133 | -19.6619 | -56.9541 | 2026-01-21 12:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 514.8 |
| 330920a0-5cc6-3af8-b960-109591e3d6e7 | -19.6418 | -56.9569 | 2026-01-21 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 138.5 |
| 08508f57-8f17-3115-b08d-79813fab9f8e | -19.6623 | -56.9331 | 2026-01-21 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| b43e596d-9338-3599-a462-6eb8278c21cd | -19.6619 | -56.9541 | 2026-01-21 13:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 493.3 |
| 4166a351-df00-3dc0-aa56-231e8e8dc5bb | -20.3481 | -57.9033 | 2026-01-21 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| c32a53ea-d478-37ba-84bf-fdf58da51901 | -20.3283 | -57.8851 | 2026-01-21 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.4 |
| 7bc5b5b2-1548-36e8-9999-7cdfac467fc0 | -20.3485 | -57.8824 | 2026-01-21 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 577537ba-0b33-36fe-b1cb-776f003c23e2 | -20.3485 | -57.8824 | 2026-01-21 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 3b349a9a-687e-3481-bb2d-6316440244d3 | -19.6619 | -56.9541 | 2026-01-21 13:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 492.5 |
| cbc528c7-22fd-3318-83c1-9369c7b69f25 | -19.6418 | -56.9569 | 2026-01-21 13:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 120.9 |
| 98950e0b-ddd3-3cbe-b5ac-63bd0c5a3656 | -19.6623 | -56.9331 | 2026-01-21 13:20:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 7be43882-f8a9-3ff9-9377-6031010c772d | -20.3283 | -57.8851 | 2026-01-21 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| ac54d0a5-7d9c-36ae-990e-d47ed69f1ec6 | -20.3283 | -57.8851 | 2026-01-21 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| fa8f651e-f076-3a94-92e4-ad9f793a0f1c | -19.6418 | -56.9569 | 2026-01-21 13:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 6a3cab76-7e48-3762-88bd-04b1fbff70b4 | -19.6623 | -56.9331 | 2026-01-21 13:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 93cfae5e-c520-3710-98fd-b5a71316286f | -19.6619 | -56.9541 | 2026-01-21 13:30:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 369.2 |
| eb60a95e-ae1e-31a8-80dd-fff1b7b34013 | -20.3481 | -57.9033 | 2026-01-21 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 2fe95049-4bb6-3654-8db4-870f05435732 | -20.3485 | -57.8824 | 2026-01-21 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| be9df1de-666f-303c-9ec9-8997493fbe76 | -20.3683 | -57.9005 | 2026-01-21 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 71355cc6-bd5e-34dd-9e2a-3b5dc4f1b982 | -20.3283 | -57.8851 | 2026-01-21 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.4 |
| ab57e0f2-d9b3-3a3a-9af4-df2c2979e0d3 | -19.6418 | -56.9569 | 2026-01-21 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| bb7dbd88-0cc0-3adb-af93-80c102a91e87 | -20.3485 | -57.8824 | 2026-01-21 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.4 |
| 1bda23a3-a221-3766-ab30-75c2eb3cf3aa | -20.3481 | -57.9033 | 2026-01-21 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 197d2c70-4a2f-35d7-8e1f-a21a8b5b9ab9 | -19.6619 | -56.9541 | 2026-01-21 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 352.4 |
| 8ebcfeff-52d6-38b3-a127-630a863832c8 | -19.6623 | -56.9331 | 2026-01-21 13:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 49c79384-6b1d-3d27-88b6-0d4ce26b0864 | -20.3683 | -57.9005 | 2026-01-21 13:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 6d69710f-bd28-363b-9c85-e69c3b6a0957 | -19.6623 | -56.9331 | 2026-01-21 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 85.2 |
| a759b8a9-4d4e-3454-be59-386675cff9f7 | -20.3283 | -57.8851 | 2026-01-21 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| c3967210-60de-3ee1-9951-f4bc6b7df952 | -20.3485 | -57.8824 | 2026-01-21 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 73d453e4-f6ca-34c5-8ea7-2ea09ada8218 | -19.6619 | -56.9541 | 2026-01-21 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 283.3 |
| bb0f24e7-cc11-33c1-a827-b619b8ece089 | -19.6418 | -56.9569 | 2026-01-21 13:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 87.9 |
| e4a96391-e697-3510-b269-17d2b76a7390 | -20.3481 | -57.9033 | 2026-01-21 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 7eb80e6c-3644-3792-8f09-9f394689d468 | -20.3481 | -57.9033 | 2026-01-21 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.4 |
| 3dde5297-64ec-33d1-b4c6-167462a97562 | -19.6623 | -56.9331 | 2026-01-21 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| f437ef96-8616-3893-9316-bb14a5dbab43 | -20.3485 | -57.8824 | 2026-01-21 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| eb5859b1-f7c3-3b28-897e-14b6593b3715 | -19.6619 | -56.9541 | 2026-01-21 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 324.7 |
| 023af2ee-3282-37ba-a710-4dc91f337529 | -19.6418 | -56.9569 | 2026-01-21 14:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.4 |
| 9878604a-894a-385a-8fff-990856ef0798 | -20.3283 | -57.8851 | 2026-01-21 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 0e6b3e2c-f412-3666-b55f-0bd23f1a920a | -20.3279 | -57.906 | 2026-01-21 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.2 |
| c064482a-ab7a-3f25-bd4e-ed12fdbda44d | -20.3485 | -57.8824 | 2026-01-21 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| f5c9e036-bdc7-300d-b20d-b0bc067b5a82 | -19.6627 | -56.9122 | 2026-01-21 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| e88fa0e4-d47d-3b2e-91b9-e4105b22e972 | -19.6623 | -56.9331 | 2026-01-21 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| e4c90751-3f4a-30d2-8d9c-2360b1e49e7a | -20.3683 | -57.9005 | 2026-01-21 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |


[Clique aqui para ver as próximas entradas](README7.md)
