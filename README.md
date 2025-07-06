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
| 14b9ba87-958c-3851-ae91-0ada4fab5ae9 | -11.3407 | -51.4452 | 2025-07-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 37.9 |
| da47c2fe-750c-3244-9dc8-93ae6e39b8c4 | -11.3218 | -51.4473 | 2025-07-06 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 5921e1a2-2154-3f6a-8a22-c13abf1b62c5 | -10.5776 | -49.1316 | 2025-07-06 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a5a12b1a-2a9e-3aed-bd2c-85a3a0f430d4 | -11.4588 | -45.0895 | 2025-07-06 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ae40a745-9e4e-3b2c-9cc9-d72a60fa316d | -10.5586 | -49.1337 | 2025-07-06 00:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 183eaff2-4523-35e2-ab07-6de5c6fe9b81 | -7.2023 | -43.1406 | 2025-07-06 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.1 |
| a7a85523-b625-36d6-9673-1e8ee4e2c28d | -7.2025 | -43.1171 | 2025-07-06 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 2dd1ad17-de02-3a54-8e32-79e057510133 | -5.6065 | -45.1852 | 2025-07-06 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| f2fc12d6-9dc0-3184-99ed-b6a9659033ad | -11.4584 | -45.1126 | 2025-07-06 00:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 10651f2a-e00f-36da-8c25-4a675e85a55d | -7.2023 | -43.1406 | 2025-07-06 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| cf4cf354-29c2-350e-9a09-e3eb879d1ef6 | -7.2025 | -43.1171 | 2025-07-06 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| e2bd7898-d005-3fc2-8759-fe8c00ac8bbc | -10.5586 | -49.1337 | 2025-07-06 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| a3ba12f1-7a35-3f47-a731-05ceb5a63945 | -5.6065 | -45.1852 | 2025-07-06 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ffdb83fc-67c5-3d90-bc84-643824ce34e1 | -10.5776 | -49.1316 | 2025-07-06 00:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 8cc8af9f-2aa9-3f59-ba39-e8bd48a16a95 | -10.5776 | -49.1316 | 2025-07-06 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 488510e5-f6b0-32a5-ad02-8b6ed01cc455 | -5.6065 | -45.1852 | 2025-07-06 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6403e421-e5dd-3e4d-8c68-ff6e9b55cfc2 | -11.4588 | -45.0895 | 2025-07-06 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| db2fef2d-0afc-3b57-be2d-065b839e382e | -5.6065 | -45.1852 | 2025-07-06 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 9b770d7c-d9bc-3b4c-8367-550edcc8a23a | -11.3218 | -51.4473 | 2025-07-06 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c3993e88-3b62-3ec5-a73a-e4cb01851fbe | -7.2025 | -43.1171 | 2025-07-06 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.2 |
| 219ca1ee-8726-3917-ab15-c34d86dc676e | -10.5776 | -49.1316 | 2025-07-06 00:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| cdf40889-5034-3003-9da4-654110f21a54 | -12.0266 | -57.0845 | 2025-07-06 00:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 4b359ab2-1029-3cd0-abad-284b213c474a | -10.5776 | -49.1316 | 2025-07-06 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 6395c9fe-da85-315c-9e44-dae6f8bd3d38 | -5.6065 | -45.1852 | 2025-07-06 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| bf69e861-2f0e-3a70-87d6-f9da01731e98 | -7.2023 | -43.1406 | 2025-07-06 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.3 |
| 5e3694f5-8652-3cef-bbc7-75061cb399b8 | -11.4397 | -45.0923 | 2025-07-06 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| bf997777-52cd-3188-a64d-252c92d06ae3 | -10.5776 | -49.1316 | 2025-07-06 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 5aa2d116-7663-3f02-b805-06ea9d8a0ac0 | -11.4393 | -45.1154 | 2025-07-06 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 08417ef7-10f2-33b9-a45a-950dad229509 | -11.3218 | -51.4473 | 2025-07-06 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.9 |
| f9272c91-8d86-388b-80e2-6f0e833a56b2 | -11.4588 | -45.0895 | 2025-07-06 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| eaacbeb9-82f8-3cd6-8917-fcb8d4794fcc | -11.4584 | -45.1126 | 2025-07-06 00:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b3304567-2ff0-3a87-8697-ed08d8093ca0 | -11.4393 | -45.1154 | 2025-07-06 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 28f4310e-dcfd-3167-adf6-3c12e68c4da5 | -11.4588 | -45.0895 | 2025-07-06 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8d021228-6cd2-33e2-8708-d3752a21640c | -11.9694 | -55.5194 | 2025-07-06 01:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1ec89fa3-bc6e-30a0-af5d-9597c127e9a4 | -11.4397 | -45.0923 | 2025-07-06 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 0a470434-c5fe-3a1b-a83e-5620cf3c309b | -11.4584 | -45.1126 | 2025-07-06 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 46400a8e-4a55-3dd2-89e9-51770b4e9a10 | -11.9884 | -55.5176 | 2025-07-06 01:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 106.5 |
| cb27ca72-ef42-3cc8-b4a3-d4e1c5c3d50a | -11.9881 | -55.5379 | 2025-07-06 01:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1a728ad2-574b-38b5-bfaf-0da113f0c050 | -7.2025 | -43.1171 | 2025-07-06 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.0 |
| 36742ae1-dd9d-361a-be0a-38e8679bfc88 | -11.9881 | -55.5379 | 2025-07-06 01:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 0a4983fc-13c8-3a9d-a50a-4b61866bcb7b | -11.4584 | -45.1126 | 2025-07-06 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7e5f03f7-2a14-3b9a-bb64-7c31daf8e317 | -7.2023 | -43.1406 | 2025-07-06 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| c8d63803-077c-3496-a119-bd17c75f4ba0 | -11.4397 | -45.0923 | 2025-07-06 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| f5f270e8-ac7f-318b-a7cd-f9f14fbb645a | -11.9884 | -55.5176 | 2025-07-06 01:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| c4e91648-9fbd-3d17-8d8e-aae010137490 | -11.9694 | -55.5194 | 2025-07-06 01:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 121.7 |
| a6e9f270-8253-383e-a52d-81156dfd806c | -11.4588 | -45.0895 | 2025-07-06 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7d25a91d-34d6-3212-8f1f-d46760bcaa90 | -11.9692 | -55.5397 | 2025-07-06 01:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 52dec85b-921f-37fd-a08e-c1b72ff48c58 | -11.9694 | -55.5194 | 2025-07-06 01:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 3c661077-a27a-384d-94ea-604b61b8fd1a | -11.9884 | -55.5176 | 2025-07-06 01:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 2228d5c3-54af-34e0-b5d0-d9c4102dcb2a | -11.9881 | -55.5379 | 2025-07-06 01:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1f2d0db8-9037-3ad6-8f4c-6cbc28c2f82b | -12.0266 | -57.0845 | 2025-07-06 01:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 119f0008-246a-3789-93a6-3b3298811a76 | -11.98326 | -55.53453 | 2025-07-06 01:22:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2e72c389-2342-3b6f-8261-e81fc9d6ac4e | -12.03157 | -57.09183 | 2025-07-06 01:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3d006568-3d4e-3bd0-a828-278d3c71a811 | -13.00177 | -55.97329 | 2025-07-06 01:22:00 | TERRA_M-M | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 51185369-175b-33bd-9f77-8e5a75abece3 | -9.3506 | -58.84298 | 2025-07-06 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 28bbea97-7199-3694-a9b2-07edfe312f62 | -11.87995 | -58.74117 | 2025-07-06 01:22:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 80079fa7-b19e-3c60-aebe-619107be52fc | -12.57796 | -56.981 | 2025-07-06 01:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09fb2cc2-d83d-3669-a3ef-fb5db5c96ebd | -11.33001 | -51.44217 | 2025-07-06 01:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 456ca24a-f07e-3acf-904a-802aae7b65a6 | -12.03015 | -57.08212 | 2025-07-06 01:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ea029ae1-bec4-3c83-a9c4-06ed84ad9530 | -11.98149 | -55.52293 | 2025-07-06 01:22:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| b92eb748-1e56-3235-8664-594c2036b98f | -14.84263 | -56.38225 | 2025-07-06 01:22:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5cbe030f-d88d-303e-89cd-58509c827adc | -11.33388 | -51.46615 | 2025-07-06 01:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 831deeb4-c497-36b6-86f2-628904889dd2 | -9.35186 | -58.85194 | 2025-07-06 01:22:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cdb97388-a5af-386c-a338-99fe7b2cddee | -12.57937 | -56.99071 | 2025-07-06 01:22:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e7580bd7-f926-3627-bff6-e0819a805bd9 | -12.01956 | -57.07381 | 2025-07-06 01:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 32eb1d93-5b62-35e6-adf4-26b1f3c2a1d3 | -12.02099 | -57.08352 | 2025-07-06 01:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ac2b07bf-bf2c-3ec7-9f70-fd6a9570c687 | -11.32553 | -51.46205 | 2025-07-06 01:22:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 531d430e-42a3-3cb1-8f81-41cbbc519272 | -12.02873 | -57.07238 | 2025-07-06 01:22:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1d0e9666-e128-3cf2-87f0-4aa915f344b0 | -10.56445 | -49.12806 | 2025-07-06 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 00a99bed-dfad-3eac-b8cb-c5575708915a | -7.18137 | -56.71398 | 2025-07-06 01:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| fd3b72f6-908f-3ce9-a812-535433a6bbbf | -12.0266 | -57.0845 | 2025-07-06 01:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 7ea06153-ce2d-304b-bd81-95e2eb1cc280 | -11.4588 | -45.0895 | 2025-07-06 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 1d706bbf-e319-388d-b599-13769b41569a | -11.4584 | -45.1126 | 2025-07-06 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d8e4866a-6d6d-3ad9-8efd-2c8c7f6d7208 | -11.4588 | -45.0895 | 2025-07-06 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 324dbe91-c414-3dc5-8367-eb93f4287273 | -12.0266 | -57.0845 | 2025-07-06 01:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b1a68953-c657-362a-b807-0e45ff19dd1e | -11.4397 | -45.0923 | 2025-07-06 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6ffcbb7a-9ad9-39cb-a010-5d8d055c8bde | -11.4584 | -45.1126 | 2025-07-06 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ec7674c0-25bd-332a-8295-44eead66baef | -12.0266 | -57.0845 | 2025-07-06 01:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1215b51c-b5e7-32ae-9f1b-eedba1ae9f8f | -11.4393 | -45.1154 | 2025-07-06 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 47a645b4-65a9-3cb2-ae97-bdd148562ea2 | -11.4588 | -45.0895 | 2025-07-06 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| febae2cc-3c74-383a-b2cc-7320258c0c41 | -11.4397 | -45.0923 | 2025-07-06 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| db9f6e58-f918-3d53-a42e-fa2a5e51237e | -11.4588 | -45.0895 | 2025-07-06 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c243737e-36bd-35f7-8fb5-80976684c829 | -11.4584 | -45.1126 | 2025-07-06 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 38800403-d952-338d-8875-cae06f00ec2d | -12.0266 | -57.0845 | 2025-07-06 02:00:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 07f06b52-14f0-3e83-b498-de409fc3ed10 | -11.4588 | -45.0895 | 2025-07-06 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c75e3818-d2d0-3cc1-9638-87b816dc4ea9 | -11.4397 | -45.0923 | 2025-07-06 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b2380311-bb32-3bc6-8607-d3609cd3c03d | -12.0266 | -57.0845 | 2025-07-06 02:10:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 09c349e6-6e5a-331e-91b5-a7d7e91c155e | -11.4584 | -45.1126 | 2025-07-06 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| e45fc66b-7c6d-3a2a-a2cf-1cffc7a5a909 | -11.4584 | -45.1126 | 2025-07-06 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| b4fb8edd-92b3-3e08-b78c-1c9e37b4c4a1 | -11.4588 | -45.0895 | 2025-07-06 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f4ebf902-f159-3bc9-8aa6-e93d718791d1 | -12.0266 | -57.0845 | 2025-07-06 02:20:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| b7bb6402-ab30-3f0c-a70c-47ffe5a90895 | -12.0266 | -57.0845 | 2025-07-06 02:30:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2e53c77d-cbf9-3f6f-8915-35989a9911d4 | -11.4397 | -45.0923 | 2025-07-06 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 940d8f0a-7ce5-3686-9ed8-087193fb6916 | -11.4584 | -45.1126 | 2025-07-06 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 8fea7331-f6bf-3777-adab-7e82c2b74ee7 | -11.4588 | -45.0895 | 2025-07-06 02:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9d8ccbdb-5cd5-3693-aca2-bc112700d288 | -12.0266 | -57.0845 | 2025-07-06 02:40:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b1b293e3-29d9-3e87-a3c1-05cd45df1e19 | -12.0266 | -57.0845 | 2025-07-06 02:50:00 | GOES-19 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 10c1c8cb-3fbb-3bd2-aab8-6afba1f729d3 | -11.4584 | -45.1126 | 2025-07-06 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 480457dd-c600-380a-8b59-efe040fe251b | -11.4588 | -45.0895 | 2025-07-06 02:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 183ff91a-b90f-3c50-a5e7-b2c148472243 | -11.4584 | -45.1126 | 2025-07-06 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |


[Clique aqui para ver as próximas entradas](README2.md)
