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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29befcf4-7d47-370e-9dc6-0bbcc1381d3a | -10.1309 | -50.019 | 2024-09-27 01:26:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 265c7992-6ffb-39d5-98fe-c402d6fabc84 | -10.3672 | -53.7858 | 2024-09-27 01:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 588ed8f0-02f5-3a9b-8d87-dbb8f860a243 | -10.6643 | -45.861 | 2024-09-27 01:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ec56d689-6751-3375-87af-bb06fb669915 | -10.6452 | -45.8635 | 2024-09-27 01:26:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 311358d9-73cf-339b-a969-507c098f04b7 | -10.9264 | -54.2692 | 2024-09-27 01:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 230.4 |
| 37373f24-f054-3270-82e2-2f580f614026 | -10.9267 | -54.2488 | 2024-09-27 01:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 251.4 |
| 32b34a86-042c-3ef6-ba8a-708793fe872a | -10.9453 | -54.2676 | 2024-09-27 01:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.5 |
| fd3ab430-a6aa-3a96-8375-3d36adff9a90 | -10.9456 | -54.2471 | 2024-09-27 01:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| c39b5df4-adea-321c-ab81-d292f6656e67 | -11.1219 | -50.8328 | 2024-09-27 01:26:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 72d60a7f-de51-3c1c-a920-702bc3ea20e5 | -11.2034 | -54.7752 | 2024-09-27 01:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 505f34cb-9ddf-30de-aa4b-4f48af5cf195 | -11.5872 | -63.9596 | 2024-09-27 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 1135a9c2-dfd9-3d61-b834-2f0c8f413bfd | -12.1863 | -50.7981 | 2024-09-27 01:26:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 84ea6659-f387-3e72-b870-ec4f4906dae1 | -18.3997 | -51.961601 | 2024-09-27 01:26:17 | METOP-C | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 09accb02-eefa-3f60-9043-25ae2cab4dc8 | -12.6636 | -54.6782 | 2024-09-27 01:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e790de64-4a9a-3030-89e4-1550c8f91076 | -12.6824 | -54.6968 | 2024-09-27 01:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| b0f05106-06ff-3e1b-8b3a-b00982054cb7 | -12.6826 | -54.6763 | 2024-09-27 01:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 1a2f2fcc-0a2f-3cff-b76b-7cd40776e0e1 | -12.8437 | -54.0422 | 2024-09-27 01:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| ba9dc469-55e6-37e0-88e4-f52479ecc768 | -12.844 | -54.0215 | 2024-09-27 01:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 1a70ce97-0479-3514-ad93-dd5043d59365 | -12.8628 | -54.0402 | 2024-09-27 01:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c4050ea8-ec72-37dd-8f60-05fe90320687 | -12.8631 | -54.0195 | 2024-09-27 01:26:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| e52f1231-9640-3e90-8df3-0499ba31af28 | -13.4413 | -44.0267 | 2024-09-27 01:26:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| f7cd4a36-37ce-3d36-b801-16ae5c0e36b3 | -13.2105 | -51.2714 | 2024-09-27 01:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 71761aea-eac9-3243-af31-2a114bd7b324 | -13.2297 | -51.269 | 2024-09-27 01:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d4f2f154-d151-3207-a748-35aefaf89d86 | -16.840799 | -47.703899 | 2024-09-27 01:26:25 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 53b47618-502f-36e6-b223-edb7a746f92d | -16.836201 | -47.725201 | 2024-09-27 01:26:25 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a5225374-a5e6-322f-9b33-8611da92442c | -16.841101 | -47.7435 | 2024-09-27 01:26:25 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0265391e-bb7c-3fa1-8a2d-4e19547dfb30 | -16.8461 | -47.761799 | 2024-09-27 01:26:25 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b7a273f-b0b1-3208-8c92-2d5125cbee5c | -16.831499 | -47.7463 | 2024-09-27 01:26:25 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bfb625b3-c91b-3bc5-ac9e-ca271b2f9e96 | -16.8365 | -47.764599 | 2024-09-27 01:26:25 | METOP-C | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2d77dd-b8f3-363c-84d4-b8b9fef3dcf5 | -14.7104 | -45.533 | 2024-09-27 01:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 12c82ba7-580f-343b-a2b9-39e25c1eac82 | -14.7109 | -45.5096 | 2024-09-27 01:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 655.0 |
| 5b0b1f9c-a99e-3f54-a0af-788c6fcc5de0 | -14.7114 | -45.4863 | 2024-09-27 01:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 397.1 |
| 69f8b540-f68d-3f30-b01e-8c487090b849 | -14.73 | -45.5294 | 2024-09-27 01:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 08c6050d-d0a8-3d5a-8b95-287fb738a2de | -14.7305 | -45.5061 | 2024-09-27 01:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 389.3 |
| d288f2d6-9c4f-35d6-9900-eee38cce3d77 | -14.731 | -45.4827 | 2024-09-27 01:26:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 227.9 |
| e20c64b5-9f9b-3495-8d40-2a5dcff0bc14 | -15.6056 | -56.9626 | 2024-09-27 01:26:34 | GOES-16 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| a96f3c14-f335-35c2-acdf-db3f5079a28f | -16.3685 | -49.915901 | 2024-09-27 01:26:42 | METOP-C | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 00947360-3819-3911-b970-8cbb457d2218 | -18.7044 | -42.0865 | 2024-09-27 01:26:49 | GOES-16 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.1 |
| 1b31303c-a402-349b-82dc-4e5e2751900c | -14.7275 | -45.499401 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 264b3d68-34bf-34e7-acfb-5a5d6580ac08 | -14.7354 | -45.527302 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 150c84c9-574e-3dfa-a88c-3baac53e722d | -14.7196 | -45.471298 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 260c6efe-1b2e-3563-918c-4668783bea32 | -14.71 | -45.474201 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7eeb3a93-dd88-3d58-9ffc-d3de95189bad | -14.7179 | -45.502201 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2eec52e2-40fb-3787-8e77-4f402ce57d67 | -14.7258 | -45.530201 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5d7b08c6-43b9-373b-9dfe-e55eeb4bfdd0 | -14.7084 | -45.5051 | 2024-09-27 01:26:49 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6a1cb23-08cb-3129-ac6e-02623d26909b | -19.5272 | -47.872 | 2024-09-27 01:26:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 741d7463-81a2-3796-a242-22110e816fc9 | -19.6136 | -42.8159 | 2024-09-27 01:26:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.5 |
| 73b4137c-c90c-366d-aa36-fe96cc4d3c49 | -19.5266 | -47.8952 | 2024-09-27 01:26:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| fb841953-e13e-34e8-852a-e4d3920558e3 | -19.5476 | -47.8675 | 2024-09-27 01:26:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 3f722956-2ce2-3639-8fe9-6f9948b2103b | -16.133101 | -51.974201 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a2aef318-5941-3c1d-b703-3c490dfc250b | -16.115801 | -51.946098 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a965e077-4443-3e94-b6a3-c53ccf549b5a | -16.1234 | -51.976799 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c40c9f6-5ce7-38a0-87d2-c19e1ee71b82 | -16.131001 | -52.007301 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 236c8332-6b70-330a-ae20-a9ff09f95534 | -16.1035 | -51.9384 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7df7534e-8418-3eae-83de-d569467e0cd0 | -16.106001 | -51.948601 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ed9fc8ca-3d87-395c-a978-c008a6b0e156 | -16.108601 | -51.9589 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 664ba873-d348-3beb-863e-544610cef60f | -16.111099 | -51.969101 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cfae9701-3ec4-3d35-8c76-8324eb606ccd | -16.121201 | -52.0098 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 75b6254b-f471-353a-aa98-958d7a44d502 | -16.0989 | -51.961498 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 82b22f5e-bca1-3a43-97d7-8b1fbae7139b | -16.1014 | -51.971699 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a7dce1b2-d4f0-311f-984b-af3186acc708 | -16.0917 | -51.974201 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8be45704-9a22-3693-931d-eaa5258b0f5a | -16.0942 | -51.984402 | 2024-09-27 01:26:54 | METOP-C | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ef28038-96fc-31ea-9fad-bc9f252f7ef0 | -17.114201 | -56.163601 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5fb0d42e-7cfa-36fa-ba3f-d83e5efd2268 | -17.115801 | -56.1707 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 350debc6-fa53-3731-b51a-a1b5cdc735c9 | -17.117399 | -56.177898 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9421c117-113b-3fb8-9032-0f73e634510a | -17.119101 | -56.185101 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a390dec-de6b-3fde-8afa-25e5df624048 | -17.120701 | -56.1922 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ea3e1921-3b3a-3923-ad73-adb9135389e3 | -17.104401 | -56.165901 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e6cecc4-de38-392d-9657-8ab01e74efab | -17.106001 | -56.173 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0c4449d5-388a-34f3-b936-900b81bc72a5 | -17.107599 | -56.180199 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ff470769-8486-3c90-a778-bb6c5ca37181 | -17.109301 | -56.187401 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6feccb42-7c09-39a6-a64b-f0892c3697a8 | -17.110901 | -56.1945 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 676376d6-a111-362d-b57a-ce82c3eebb52 | -17.112499 | -56.201698 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37e04010-0aee-3f0f-ac7c-9ea9ea4c7088 | -16.614401 | -54.088501 | 2024-09-27 01:26:54 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c65672d3-4292-3d13-a54c-a3a26db67a6e | -16.616301 | -54.0965 | 2024-09-27 01:26:54 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e1ef9de-8867-37aa-a194-301978a34491 | -17.0882 | -56.139599 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41ef9d10-1d88-3cfb-8f3b-fee07b97912e | -17.0898 | -56.146801 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c9309dcf-bde1-32d8-9dd7-66b65846268b | -17.0914 | -56.153999 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8db339d1-c081-3c4e-8db8-326b428e5497 | -17.093 | -56.161098 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8dd454f-8f3a-3f5a-ae45-698c0b96758c | -17.094601 | -56.168301 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1449642f-b438-397d-bd3e-7e80d9586fbf | -17.096201 | -56.1754 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 621628b8-a5ed-3cad-8893-b5e3e73dc559 | -17.097799 | -56.182598 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 823f959c-55b9-34d6-838b-6eea8271f412 | -17.099501 | -56.1898 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8353d9a5-6c2b-305a-bd7c-01fe2657c994 | -17.101101 | -56.196899 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc751beb-61cc-34e7-a4c2-6f2f9f497350 | -17.0784 | -56.141899 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| de54d36c-e19d-33da-96a9-f5f2b68d53a4 | -17.08 | -56.149101 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bc29d8cb-70c2-3a00-b1cb-055f43b98e87 | -17.0816 | -56.1563 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d7f70eb-66a0-3683-b3de-ad37b4865f51 | -17.0832 | -56.163399 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2fb3e6cc-272e-3fa8-862b-303492bfd40e | -17.084801 | -56.170601 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a181acad-b500-3676-adba-e3a5b667fdf2 | -17.086399 | -56.1777 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 185fc8b7-1766-3e22-b2d0-a2e7592a69cb | -17.087999 | -56.184898 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 787fc97b-ebeb-3ef4-80bc-22e55a5cc770 | -17.089701 | -56.192101 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d790114-160a-3e37-8913-424c514eccf8 | -17.102501 | -56.249298 | 2024-09-27 01:26:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8d178760-7884-33fa-942f-ce233295a883 | -17.0669 | -56.137199 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93b1c6b3-f172-34d7-a12c-436168a3e46b | -17.0686 | -56.144299 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05d686da-3da9-3a9a-9571-f43f38009a3f | -17.0702 | -56.151501 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a5752ccf-0bc2-36c8-8e04-17aca02101c2 | -17.0718 | -56.158699 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4dc0e936-752d-35be-b149-e0c787b11144 | -17.0734 | -56.165798 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8c315e81-aa85-37a8-979d-211a3a27899e | -17.075001 | -56.173 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0e2a62c-b478-332d-b663-53fb1894c128 | -17.076599 | -56.180099 | 2024-09-27 01:26:55 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README32.md)
