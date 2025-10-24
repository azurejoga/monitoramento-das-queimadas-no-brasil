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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5511d0ba-0e30-384c-98d0-0cc62a18f963 | -10.1918 | -36.7236 | 2025-10-24 00:00:00 | GOES-19 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 82.0 |
| b583bf76-d84b-322f-91c9-8b3a8de4d185 | -5.6561 | -45.9468 | 2025-10-24 00:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 52caac81-f722-30bb-aecf-ae44abc4554d | -12.7786 | -47.3752 | 2025-10-24 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1b5a0525-0dae-31a7-b870-5155bb7914d1 | -6.3127 | -41.8727 | 2025-10-24 00:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 76.4 |
| 01b14a28-70e1-37c0-a7cc-04301294bdbb | -14.4282 | -50.9389 | 2025-10-24 00:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5348f727-9ff5-348f-af2c-7e4b3ab53868 | -10.3411 | -44.643 | 2025-10-24 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ea5c76a2-939c-37c0-836a-2d130d6b525d | -10.6636 | -44.7156 | 2025-10-24 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 1a6798cd-e4ed-3422-a57a-2ee51927d0f5 | -10.3415 | -44.6199 | 2025-10-24 00:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c030b7d3-511a-351f-973a-66d06fc9b244 | -7.5497 | -47.3766 | 2025-10-24 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e5a94b89-9ead-34a3-b5fd-48c381fa21d8 | -3.7867 | -43.9011 | 2025-10-24 00:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 58b5571c-69f9-3064-8473-ac105f55bdbd | -17.6555 | -46.6523 | 2025-10-24 00:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.5 |
| f1dbde0e-5075-319a-be82-278df5440cd9 | -7.5687 | -47.353 | 2025-10-24 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 87f48737-df9b-34d0-8b04-b675d6499113 | -5.564 | -43.607 | 2025-10-24 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 61db154f-667a-3c31-b8c9-f77af8c5fae4 | -4.2754 | -40.7012 | 2025-10-24 00:00:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 75.6 |
| a3369216-9dce-3270-adb4-e7ce3ee77192 | -4.2942 | -40.7 | 2025-10-24 00:00:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 144.5 |
| 84d1260d-5936-3742-a730-19405726d535 | -11.0526 | -45.399 | 2025-10-24 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ee2520e5-984f-3ed1-a37e-b6f71aee40bc | -7.5499 | -47.3546 | 2025-10-24 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| a6a100ba-afec-3990-b465-f7529a5e82ee | -6.7842 | -38.5673 | 2025-10-24 00:00:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 4ef6b88b-fa66-3f18-9d48-bc8fb053f638 | -7.5684 | -47.375 | 2025-10-24 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c452c081-5482-3019-a007-eba1eea4155f | -14.4472 | -50.9578 | 2025-10-24 00:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8660c152-41ee-3fe8-a30b-a4a91408118e | -14.4278 | -50.9605 | 2025-10-24 00:00:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 89e88ac3-446d-331f-b4f1-1374bfc7a202 | -3.2617 | -52.909 | 2025-10-24 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9b10dc44-f90c-3c20-b71a-be6f795c9282 | -5.6561 | -45.9468 | 2025-10-24 00:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| fd928c9d-879f-37b7-ae61-90e9142a533c | -10.3606 | -44.6173 | 2025-10-24 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 144cd73f-76c8-3574-b860-69b897f992f1 | -16.9559 | -53.2318 | 2025-10-24 00:10:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 74102c48-e7ea-38b7-af26-902da80a88fc | -10.0198 | -47.086 | 2025-10-24 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 8695e69a-4732-34b6-b6c0-ab927c99fa33 | -7.5499 | -47.3546 | 2025-10-24 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 150262ca-2713-3c1a-a545-45c8f01ace61 | -3.2617 | -52.909 | 2025-10-24 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 418b5f78-937e-3dc7-bb82-251790db565d | -3.2433 | -52.9095 | 2025-10-24 00:10:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 9e932d8c-7965-3e48-8e5f-3794472f4ed3 | -11.0526 | -45.399 | 2025-10-24 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8103a466-5e6c-38f6-9c17-2911073d865f | -6.7842 | -38.5673 | 2025-10-24 00:10:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 103.0 |
| a9c795bb-3b4d-3d00-b3f2-bc04230c9c70 | -4.2754 | -40.7012 | 2025-10-24 00:10:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 9e18a42e-0899-320c-ac4b-9ee436e1f366 | -17.5967 | -46.6182 | 2025-10-24 00:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 137909dc-eeff-34bf-8c0e-27958a388a83 | -7.5497 | -47.3766 | 2025-10-24 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c33df774-84da-3ab5-9dc9-c4d58286db0a | -10.3411 | -44.643 | 2025-10-24 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 89.1 |
| d18c93de-4bfd-3557-b134-e70c2d69159b | -4.2942 | -40.7 | 2025-10-24 00:10:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 4657dc9d-260d-39a8-978a-c709f9019f13 | -10.3415 | -44.6199 | 2025-10-24 00:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 55f0152f-361e-36c4-9815-23e70c82a600 | -14.4278 | -50.9605 | 2025-10-24 00:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 112.0 |
| d867ea97-fe3a-3523-b3c5-5dd707066b9b | -14.4476 | -50.9362 | 2025-10-24 00:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1c25e5e0-5aa9-3992-803e-3418351eed6c | -10.0194 | -47.1083 | 2025-10-24 00:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| cb565ff4-1248-3002-b27c-7c5a2b6e1480 | -6.7652 | -38.5694 | 2025-10-24 00:10:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 70.2 |
| 426b996c-5c72-3cb2-afbc-c4315625ce77 | -14.4472 | -50.9578 | 2025-10-24 00:10:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1c7332df-e6b7-3c0a-8c8f-491469cc8813 | -6.3127 | -41.8727 | 2025-10-24 00:10:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 68039b41-e122-3ad1-8cc4-6b61ae4d3412 | -17.3156 | -55.0183 | 2025-10-24 00:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| 958c8aed-0741-3534-862a-2696057c8c96 | -6.3127 | -41.8727 | 2025-10-24 00:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 4d6b6ac3-9b95-35f0-bade-2615ca8a3294 | -3.2433 | -52.9095 | 2025-10-24 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| a6db0bbd-b08c-33f7-af61-108420963570 | -17.3353 | -55.0156 | 2025-10-24 00:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 8b45e4fd-d65b-3c38-9fba-b4d15c62353e | -3.2617 | -52.909 | 2025-10-24 00:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 01684e5b-bee0-3f68-bf68-1ca008d0121d | -17.5967 | -46.6182 | 2025-10-24 00:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d6389e2c-75f6-3a30-81f7-acbf8b05a414 | -14.4278 | -50.9605 | 2025-10-24 00:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 6ba492c9-a34e-31b1-8a78-0c96610073c5 | -11.0526 | -45.399 | 2025-10-24 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5b17680c-a34c-38f3-8528-ce37a94e4bfd | -7.5497 | -47.3766 | 2025-10-24 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 97518b63-d429-3bb1-a888-81377f902e6d | -6.7842 | -38.5673 | 2025-10-24 00:20:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 143.2 |
| 7a7f9b97-d644-3516-b501-ffce3cf28025 | -4.2754 | -40.7012 | 2025-10-24 00:20:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 68.2 |
| bcaae469-35d2-333c-80db-7035c5e51a98 | -5.6561 | -45.9468 | 2025-10-24 00:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 52768078-c6b3-3a7f-80e3-5a2066aa1e6e | -4.2942 | -40.7 | 2025-10-24 00:20:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 0a5a3fa7-e224-356f-9e3b-e6f6e634cb55 | -16.9563 | -53.2104 | 2025-10-24 00:20:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 6db19102-528a-3677-b344-a21481c98ae5 | -17.335 | -55.0366 | 2025-10-24 00:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| b9715915-41d7-3ee0-9b26-79c5ced70b9a | -17.3153 | -55.0393 | 2025-10-24 00:20:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| 5f08c7c3-d1b9-3eac-854b-53a660a72b84 | -3.7867 | -43.9011 | 2025-10-24 00:20:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 9e970d81-2cf0-3b42-83e9-8dc15be16f3f | -7.5687 | -47.353 | 2025-10-24 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 68c180ee-7d23-3e19-a8ae-f408e64b992a | -14.4282 | -50.9389 | 2025-10-24 00:20:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| dda34134-940b-3f4c-a119-5dc21fa388f2 | -7.5499 | -47.3546 | 2025-10-24 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| a4a0a5b9-0476-35af-b873-4c2fd615dae1 | -14.4472 | -50.9578 | 2025-10-24 00:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 59d66e79-0352-3af6-81b5-f965576746d7 | -17.6555 | -46.6523 | 2025-10-24 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 03e8865c-7528-3d13-80a0-905cedebb145 | -7.5497 | -47.3766 | 2025-10-24 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 45da5b33-cb7f-3ac4-a4ef-3f6bfc464af7 | -7.5499 | -47.3546 | 2025-10-24 00:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 8dbc450c-5a22-3def-8a92-004bab0e660e | -17.335 | -55.0366 | 2025-10-24 00:30:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 5254ac69-3be3-3f76-97fc-6d44b8536067 | -4.2942 | -40.7 | 2025-10-24 00:30:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 144.1 |
| d015e9f9-69ed-331a-b8c6-9ab94f507af4 | -6.7842 | -38.5673 | 2025-10-24 00:30:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 15eb1b4c-c6d6-30ae-bb71-46bef631c642 | -17.5967 | -46.6182 | 2025-10-24 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 250c7a99-d5b7-3250-9de3-c0eaf79237ba | -6.7825 | -45.4799 | 2025-10-24 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| c1a1737b-f1a9-319b-8a88-3e69ad7bc79d | -4.2754 | -40.7012 | 2025-10-24 00:30:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 0cc02690-f7ac-3a15-a50e-a7616dda4747 | -11.0526 | -45.399 | 2025-10-24 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c4aa41f4-10c4-3a94-a2f6-73008e22e64e | -2.2647 | -47.84 | 2025-10-24 00:30:00 | GOES-19 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| fa98495d-2341-3c44-a304-b865b34c44bf | -14.4278 | -50.9605 | 2025-10-24 00:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c87fd513-908e-356c-9d21-82f1d304ec64 | -3.2617 | -52.909 | 2025-10-24 00:30:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| dd5dbf39-7bdd-3de5-8978-3170542df8d2 | -17.6549 | -46.6757 | 2025-10-24 00:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 72bd5be6-ea51-3ca0-9bc0-fed6995578d4 | -5.6561 | -45.9468 | 2025-10-24 00:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 238dd7ae-19bb-33d6-8b22-2b09939eb3aa | -16.9559 | -53.2318 | 2025-10-24 00:40:00 | GOES-19 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 8064d6d2-61bc-3953-b957-4604d41f2209 | -4.2754 | -40.7012 | 2025-10-24 00:40:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 67.7 |
| c0ff1ef2-4f56-3ad6-af80-2ed65917de25 | -17.5967 | -46.6182 | 2025-10-24 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 39bf0271-3c5d-3e0a-a5c0-77c18d956e29 | -14.3079 | -49.082 | 2025-10-24 00:40:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| b247f4e5-b3de-35af-9f1c-d07183bfd556 | -7.5499 | -47.3546 | 2025-10-24 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2625eb6d-f6ab-3b7e-b44e-7171f98d530f | -6.3127 | -41.8727 | 2025-10-24 00:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 1203df35-e562-3fda-ae5d-ee52c4af2e73 | -17.335 | -55.0366 | 2025-10-24 00:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 95250c26-e9a8-35c6-9e96-94b35237bfcf | -17.3153 | -55.0393 | 2025-10-24 00:40:00 | GOES-19 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 79.7 |
| d79d80ba-1358-3b8f-9b95-3ff15437704b | -15.1939 | -49.4083 | 2025-10-24 00:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a036d1f7-52c5-30e5-b764-65cb5d316ce5 | -14.4472 | -50.9578 | 2025-10-24 00:40:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| ce86acf4-075a-333a-915b-1678cdec832a | -15.1744 | -49.4114 | 2025-10-24 00:40:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 70001ccc-2cdf-3335-a8dc-65aed19ef13a | -7.5497 | -47.3766 | 2025-10-24 00:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 326bb3a3-9981-3993-978f-7d6603f3adae | -17.6555 | -46.6523 | 2025-10-24 00:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2d815f01-f7dd-3931-b2aa-d4ef8e2c0fdd | -14.4278 | -50.9605 | 2025-10-24 00:40:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 89c4532c-2685-3c86-9854-da4d570e51e5 | -2.482 | -49.2297 | 2025-10-24 00:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| fd3e54f6-963a-3f62-8790-7fed14798419 | -14.3083 | -49.0599 | 2025-10-24 00:40:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 154.0 |
| b2a70622-5c5f-3f43-94cf-f6c36888bf05 | -6.7842 | -38.5673 | 2025-10-24 00:40:00 | GOES-19 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 536b6504-0c86-39d3-ad61-7b525ed5dfd7 | -4.2942 | -40.7 | 2025-10-24 00:40:00 | GOES-19 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 66.1 |
| 1e425104-67bc-3199-8d19-f6b7888ca7c1 | -3.2617 | -52.909 | 2025-10-24 00:40:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8c550ff7-0950-35fc-b7d8-959867f443eb | -11.0526 | -45.399 | 2025-10-24 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 1600358a-4ca2-306b-b379-a8a06e4ff730 | -17.6555 | -46.6523 | 2025-10-24 00:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |


[Clique aqui para ver as próximas entradas](README2.md)
