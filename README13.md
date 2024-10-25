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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eaa5ee39-3ee9-37e2-a8ab-273723b1f48b | -3.1949 | -46.807 | 2024-10-25 01:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 03e0c3cb-6b98-3bb6-b029-587c90646df1 | -3.2135 | -46.8063 | 2024-10-25 01:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 5f5274bb-68c7-3fb4-aa1c-4ca3a5fd92ea | -3.2136 | -46.7843 | 2024-10-25 01:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 05585318-e21a-34e1-8fb5-bd7958eec267 | -3.958 | -46.4442 | 2024-10-25 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5ad86afe-0f94-3e8c-aea1-cafc6b50fa87 | -3.9581 | -46.422 | 2024-10-25 01:35:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 72db97dd-d46b-3447-9240-c829d83a5048 | -4.2429 | -48.5474 | 2024-10-25 01:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| a5814831-2c60-3286-8da5-b033141f996d | -4.2441 | -48.332 | 2024-10-25 01:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 22de8d7a-b193-300c-80c7-b2e5cc63f210 | -4.4271 | -45.7751 | 2024-10-25 01:35:30 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 02ff04f5-99b6-3fef-aed1-07c4352b524a | -4.5045 | -48.2117 | 2024-10-25 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b9e7e944-585d-3c48-bd5f-7663ad4e154f | -4.5231 | -48.2108 | 2024-10-25 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b7848bd2-2da0-3083-9b0e-a08bfdac65b5 | -4.58 | -48.0132 | 2024-10-25 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| e9e4c998-1fa9-3f52-ba19-21922dfcac4a | -5.9788 | -45.3621 | 2024-10-25 01:35:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| b0e5c5cf-3a41-39ec-abd9-02d6a1289d82 | -6.5219 | -60.0457 | 2024-10-25 01:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a2e2d1fc-6cce-3d56-9a2e-028977644f53 | -6.522 | -60.0266 | 2024-10-25 01:35:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| f1520188-19ff-3625-a8ae-9bdb4f0fd55c | -6.6472 | -47.8642 | 2024-10-25 01:35:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 9360ea9d-a944-32ae-aa00-37c0a7e1a09b | -9.6691 | -35.8459 | 2024-10-25 01:35:59 | GOES-16 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 5b1ee2cf-73b7-339c-a4a9-0f830c5b7cd0 | -11.883 | -56.4152 | 2024-10-25 01:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 0da2f0d9-02eb-3f61-80a5-e48aa0b4b5de | -11.902 | -56.4135 | 2024-10-25 01:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 122bfd8c-2f1e-35c5-9c27-dd6501d69d59 | -11.9822 | -63.9213 | 2024-10-25 01:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| a8fa9981-7725-3132-a039-21f319e5573e | -11.9824 | -63.9022 | 2024-10-25 01:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 125.2 |
| fb715ddc-92c6-3e2e-ae85-c81f486ff5ad | -12.0011 | -63.9203 | 2024-10-25 01:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 2807d614-4a65-31cc-980d-16cea4f8ab80 | -12.0012 | -63.9013 | 2024-10-25 01:36:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 202.4 |
| 66679e07-6d9e-3769-8326-03a767f30654 | -12.0444 | -63.1547 | 2024-10-25 01:36:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| bee8aa0f-f9bb-32c9-83b4-742b4d422f34 | -12.0445 | -63.1356 | 2024-10-25 01:36:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6d2d43bd-9f30-3845-b6a6-a6139e44f7a8 | -12.0632 | -63.1537 | 2024-10-25 01:36:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| de673897-109a-3536-9e5b-d26247a2c3a1 | -12.0634 | -63.1346 | 2024-10-25 01:36:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| b3614f03-9ba1-3f40-bb1f-adafe46173f8 | -12.3782 | -63.8821 | 2024-10-25 01:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 860c549a-0d4f-365e-90dd-885527d15d73 | -12.3783 | -63.863 | 2024-10-25 01:36:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 1506a263-4178-369a-9a76-785a790d3574 | -12.4589 | -63.1895 | 2024-10-25 01:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| de0d1873-55de-3a97-9e5a-fb2ff4bb64cc | -12.4591 | -63.1704 | 2024-10-25 01:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 30c75008-90c0-35a6-8e87-84c14add032c | -12.478 | -63.1693 | 2024-10-25 01:36:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a1b7da2e-6a4e-3151-a8ed-d104f437addd | -12.5356 | -63.051 | 2024-10-25 01:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8a11039e-68a7-3e5f-b724-0b969531abf0 | -16.94 | -57.5268 | 2024-10-25 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 6448d9df-3df1-34b2-bb47-b9619bd3e59c | -16.9792 | -57.5223 | 2024-10-25 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 5b6d91ab-2bc5-3b29-85a9-2fa8b08ae391 | -17.0381 | -57.5155 | 2024-10-25 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.4 |
| 3408f8a3-98ab-3a9a-9238-2d7e1324de12 | -17.215 | -57.4744 | 2024-10-25 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 05a16577-956c-3fbf-9b4e-b9eb869e4d38 | -17.2337 | -57.5336 | 2024-10-25 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.5 |
| cbafbe67-7e5a-32e3-8e81-35c7c0c8bd7b | -17.2537 | -57.5108 | 2024-10-25 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 79.3 |
| eff10f2a-91ab-366d-a7c4-97af7a8fb6c0 | -17.2147 | -57.4949 | 2024-10-25 01:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.2 |
| 43d5c04f-378c-3d9a-9a35-b8eaeb5ad6dc | -17.7453 | -57.4933 | 2024-10-25 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.7 |
| e1ea5f61-9d26-38de-be3e-beb31b6f4125 | -17.7671 | -57.3673 | 2024-10-25 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 62438066-7eea-3395-af11-21e5360b3d32 | -17.8042 | -57.5067 | 2024-10-25 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 116.1 |
| 49f11cff-5bd6-3408-83f9-bfdda2764ef3 | -17.8239 | -57.5043 | 2024-10-25 01:36:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 92.9 |
| d49eb1b6-500b-3375-9f06-28f224b864a6 | -17.9473 | -57.2009 | 2024-10-25 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.3 |
| bee3c3d9-cc9b-3265-a1cb-4ab582bc2ec8 | -17.9268 | -57.2447 | 2024-10-25 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.9 |
| ef135bfe-b583-3461-a60f-1c6d22d800d8 | -17.9272 | -57.224 | 2024-10-25 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.3 |
| 6cd0efb2-6ef7-3121-a29e-3b9bae3510fb | -17.9275 | -57.2034 | 2024-10-25 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 36b21efe-fce8-377a-bdaf-7e9767ff52ac | -18.0056 | -57.2555 | 2024-10-25 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| d7eac528-f5a8-3d72-8e18-91e3420f023a | -18.0254 | -57.253 | 2024-10-25 01:36:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 9a8159cd-6205-349f-8cd9-36960de933a4 | -18.0431 | -57.3745 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| bb0217ff-efec-3acf-8d61-aa5b34c92c90 | -18.0434 | -57.3539 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.0 |
| f888bcaf-8184-3117-9c8e-bd0cc64f3344 | -18.0438 | -57.3332 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| f1374402-71a4-3ed6-99d7-fd699b89efcd | -18.0441 | -57.3126 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.3 |
| f95943b7-e3e0-30f9-96bd-b1eda9948d33 | -18.0445 | -57.2919 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.9 |
| b1af8228-95b7-3203-b022-49bfb166aa1e | -18.0844 | -57.2663 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.7 |
| dda70099-4363-3b8d-9b82-a75495e9545a | -18.0847 | -57.2456 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.0 |
| ea7f2193-4b82-3c35-9eae-c20bbfb8f068 | -18.1042 | -57.2638 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.3 |
| 616bb7f8-0223-3a37-8a9a-3379fba400c3 | -18.1223 | -57.3647 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 119.5 |
| acee63b6-fc18-358e-8614-6c1e85d0fcbb | -18.1226 | -57.344 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.9 |
| 860625fa-389b-3e5d-a3e1-33f36b057c8f | -18.1421 | -57.3622 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.1 |
| 92714358-d818-365a-ac68-7295ddfff98f | -18.1424 | -57.3415 | 2024-10-25 01:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 8fbd94bd-2721-3015-9d06-1650301802a5 | -18.3012 | -56.1804 | 2024-10-25 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| f4029ca8-7090-3023-9776-8ef246500f09 | -18.3199 | -56.2404 | 2024-10-25 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 563aa274-ce52-341f-8a10-02a0f885e592 | -18.3203 | -56.2195 | 2024-10-25 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 6262d2a7-3bb8-3b68-9d4e-c023d278846c | -18.3207 | -56.1986 | 2024-10-25 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 53.5 |
| 78731d14-0f6e-39dd-8b22-3c946bbc65af | -18.3398 | -56.2377 | 2024-10-25 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 61cd3ed6-6be3-3963-ab28-497a3b3347aa | -18.3401 | -56.2168 | 2024-10-25 01:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.0 |
| 623a24a2-86ff-3c20-a01a-462bfe72e922 | -1.0445 | -47.6237 | 2024-10-25 01:45:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| e2282015-cbcf-3e14-9db4-5eef171ee9b3 | -1.0446 | -47.602 | 2024-10-25 01:45:11 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1c092f01-eecd-3a40-a742-e5a123499fab | -1.063 | -47.6235 | 2024-10-25 01:45:11 | GOES-16 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 23ff92ad-dd87-3c1e-90f6-37d4e014f708 | -1.1834 | -53.6569 | 2024-10-25 01:45:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| ec68ffe6-1b7e-3cdc-8d2d-d0e8c2de49ef | -1.1924 | -47.6219 | 2024-10-25 01:45:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a544749a-a7f6-3032-b930-830a7ec319a0 | -1.1925 | -47.6002 | 2024-10-25 01:45:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 136.6 |
| b0db989d-3aff-3baf-aac5-daa1789483dc | -1.211 | -47.5999 | 2024-10-25 01:45:12 | GOES-16 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 6bc1480a-8182-3a21-9570-31ab1a48bd40 | -2.6192 | -52.4564 | 2024-10-25 01:45:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 012453ff-ee33-3fee-9a4f-f4201d4693f0 | -2.6193 | -52.4359 | 2024-10-25 01:45:20 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 4a5ec08c-6831-3567-a548-c3e4b77ca583 | -2.6297 | -49.247 | 2024-10-25 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c92714bf-4d3c-3985-bbbb-f2d1a73ef79b | -2.6482 | -49.2465 | 2024-10-25 01:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 409910bd-4051-33e5-b7a3-79c172e81dd8 | -2.796 | -49.2424 | 2024-10-25 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f5f67b0d-4019-3335-b855-10fb74daaf8b | -2.8144 | -49.2631 | 2024-10-25 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 45cd7c02-4f92-3e47-a0b9-fc9e31d26eff | -2.8145 | -49.2418 | 2024-10-25 01:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 0a2aacf8-f098-3d85-a754-37e3e9136dbe | -2.9578 | -50.4198 | 2024-10-25 01:45:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 81959044-d51d-3dfd-a037-24eeae14e226 | -3.2135 | -46.8063 | 2024-10-25 01:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 440261b6-ef23-32cb-aa88-ac922c77e521 | -3.2136 | -46.7843 | 2024-10-25 01:45:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 01fde096-ad6a-3851-9f07-60246eb95354 | -3.9396 | -46.4229 | 2024-10-25 01:45:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4e070d2f-0540-3054-b59b-37fe2b0621fe | -3.9581 | -46.422 | 2024-10-25 01:45:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ea4a0850-a1ba-38cc-a5bf-5eba7d89e56d | -4.2429 | -48.5474 | 2024-10-25 01:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 33a12b93-a2a3-31db-92e8-44aa3b720412 | -4.5045 | -48.2117 | 2024-10-25 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| c6cbc88a-50ae-3c9c-a932-40f4a01c9353 | -4.58 | -48.0132 | 2024-10-25 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 7bc0d9cb-c82a-35e4-abca-5198d9543bb3 | -4.5986 | -48.0123 | 2024-10-25 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 22a59e5a-f629-3ab4-ad2b-0fae189f9d7a | -6.5219 | -60.0457 | 2024-10-25 01:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5cc3d1a2-6fc3-398e-8b81-baaa0f8cf2e9 | -6.522 | -60.0266 | 2024-10-25 01:45:43 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9a87fa36-13ae-34b5-aef0-e6212427af48 | -6.6472 | -47.8642 | 2024-10-25 01:45:43 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 49.1 |
| cd6c5fd6-8e11-3f67-a8e1-e7b4b5721dc2 | -8.9064 | -48.544 | 2024-10-25 01:45:56 | GOES-16 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 75024874-da01-3316-8319-4b47ae8cbeef | -11.902 | -56.4135 | 2024-10-25 01:46:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 2a72be01-5059-311a-8bc0-4c54e71aeb06 | -11.9822 | -63.9213 | 2024-10-25 01:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 1c70297f-ffaa-361a-b5ee-8da42e880813 | -11.9824 | -63.9022 | 2024-10-25 01:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 123.7 |
| d2bd0ed3-2b22-3b6d-a989-efe4d660083a | -12.0011 | -63.9203 | 2024-10-25 01:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 9b6c0c6d-71fb-3d1e-9cf8-abb42489b006 | -12.0012 | -63.9013 | 2024-10-25 01:46:14 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 175.9 |
| a5266e96-e226-3336-904f-286df180e5a9 | -12.0444 | -63.1547 | 2024-10-25 01:46:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |


[Clique aqui para ver as próximas entradas](README14.md)
