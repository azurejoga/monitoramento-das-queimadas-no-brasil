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
| 4e5ec55a-c166-3072-8645-b5f5a5d443fa | -14.12898 | -45.35214 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d7e9f858-bce0-34d1-86b5-29b8580699bb | -10.55862 | -42.43713 | 2026-05-07 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2d7551ef-2665-351c-81fe-135cf7c45103 | -9.46519 | -47.80274 | 2026-05-07 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec7a1b68-e781-37d4-ad86-18b6b18972c4 | -12.49842 | -58.47992 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 777f7b1e-500a-3eb5-9005-0ef20065f897 | -11.83935 | -57.84746 | 2026-05-07 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c203e3ef-c9a8-3c73-91c8-f0bfffe2f5b9 | -10.92499 | -55.14444 | 2026-05-07 05:08:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04c8bc23-2f78-3d78-abe8-c4a7e9c5da6c | -8.72655 | -47.98095 | 2026-05-07 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95b1de57-dd7e-32c8-b86e-4de23608b227 | -13.95768 | -47.55153 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1931f75c-b9e9-3789-a8be-390e8d53f44f | -8.74888 | -48.92944 | 2026-05-07 05:08:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eba450a-c005-3706-a2b5-854fc331da73 | -11.72562 | -54.8041 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b48577d3-c060-369c-b132-7969fd83db44 | -13.71544 | -56.88201 | 2026-05-07 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caea065a-3dc9-37c5-9e0c-fabd1890843d | -12.4991 | -58.47591 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de5f6a84-5be4-3d42-a73b-ee756fe67047 | -14.12308 | -45.35126 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78aa4bde-d9cc-3d90-8a49-858fc54515cd | -12.50127 | -58.48457 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f86259e-c0c9-34bb-ac70-806638c22377 | -13.18408 | -52.69218 | 2026-05-07 05:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4cf8936-f08c-3d68-858f-aee967549803 | -14.86163 | -48.55302 | 2026-05-07 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eaa74153-4d8b-30e6-a2b1-d294aa158908 | -14.15006 | -52.89875 | 2026-05-07 05:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ada0917-2b0c-39ce-8adc-c0821a19de82 | -8.62976 | -49.54255 | 2026-05-07 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07ecbf38-8654-350b-80b6-05b23b4bcd4e | -12.49978 | -58.4719 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 44fd7452-cf42-37be-90b2-b24cc62beac6 | -11.7429 | -54.80321 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfecbec1-7104-381f-b4eb-7f3f03e2d9b8 | -11.79699 | -56.96476 | 2026-05-07 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ea67518-8b08-3d2c-bfd1-0fa12ffaac8c | -12.49556 | -58.47528 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3200bb2-c359-3e57-aefd-5f94a3dc2783 | -11.61326 | -54.17725 | 2026-05-07 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 825510aa-d7f0-32b9-bc26-b6813826510b | -13.94046 | -54.80505 | 2026-05-07 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49ed0a3c-13e2-398f-8296-50870da7ab55 | -11.57403 | -54.56432 | 2026-05-07 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4e1cf4c-7419-3ea9-82dc-81d47b88484c | -12.75611 | -46.96401 | 2026-05-07 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e68acd8e-7b9a-3efb-a48d-3e0b19f851cc | -11.79759 | -56.96111 | 2026-05-07 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 067ef532-524f-3fa3-9721-1d4551765224 | -11.73287 | -54.80161 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef581bf2-8056-3c9f-8330-698d6639a334 | -8.7272 | -47.97626 | 2026-05-07 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe60755-f9b5-3b9e-a89b-51fcacc6eda2 | -13.88856 | -47.52338 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57fa274c-b497-3775-a255-93a2259cb2cd | -11.72897 | -54.80463 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1caf7314-3eb7-3dca-a2e4-42e5e3043faf | -11.79819 | -56.95746 | 2026-05-07 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3ccddb2-1d77-3e67-aef0-4ac5c0dc59d2 | -12.7783 | -59.00725 | 2026-05-07 05:08:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c69b8b4-43d1-391d-b074-22d67ac0243b | -13.18346 | -52.69648 | 2026-05-07 05:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fae0b10a-57a6-3d61-b656-6bc81f0344a6 | -10.63852 | -48.01158 | 2026-05-07 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c80647d5-596f-37af-9b54-7177e541821a | -9.46689 | -47.80429 | 2026-05-07 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81983675-c004-3c18-8431-3dcb90565b63 | -11.7351 | -54.80927 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71e6ec55-72d2-3b70-a7ee-2610122c0fa3 | -12.49133 | -58.47871 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed77ee25-2df0-3e21-9693-e324fc6b52e1 | -12.49202 | -58.47469 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eba913fc-689c-374b-9b23-ce97c98c111c | -13.62937 | -47.82184 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 90b60a80-4f37-335b-8d2a-0ff763532bea | -14.14705 | -52.89385 | 2026-05-07 05:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb667e62-84bd-3f25-a8a2-9b1cc4e842de | -12.75574 | -46.96709 | 2026-05-07 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a01341d-538e-3a87-b79d-20cc0f5fc76b | -11.73956 | -54.80268 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83a76511-f77f-33d9-8344-63704435bae0 | -12.85123 | -43.75479 | 2026-05-07 05:08:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ddadf64-3bca-36e9-990c-1b9bf64a5391 | -14.31547 | -57.61271 | 2026-05-07 05:08:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5afa2b03-4865-3f7e-96db-bd8ed4ad3545 | -12.49419 | -58.48333 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00d2e303-3250-3a1f-8129-7cd8d1244905 | -14.13583 | -45.34435 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba3b61c3-fb99-34b9-bb6c-7581d88a8c51 | -12.86407 | -43.75648 | 2026-05-07 05:08:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c243dd3f-a73a-3f1a-b802-ae0e8717e631 | -11.73175 | -54.80874 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2075cf8e-a2f8-3810-b810-a3eec3ea24f5 | -14.04215 | -47.60615 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbebafa5-9a55-3569-8a7e-9ae74289eee5 | -8.81031 | -49.94857 | 2026-05-07 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8c3e3105-f647-3612-a470-156e9d8d8c06 | -13.1847 | -52.68786 | 2026-05-07 05:08:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 756f9989-d689-318e-bc40-668329092761 | -14.15068 | -52.89445 | 2026-05-07 05:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dda33501-4f3d-334e-8080-b3124763d535 | -8.63388 | -49.54314 | 2026-05-07 05:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92fb8968-16dd-355e-a768-9887d6d06b00 | -11.72952 | -54.80107 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 200e472a-58ec-3d99-97f0-3c5cffcb3a82 | -13.15341 | -56.80698 | 2026-05-07 05:08:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82353509-3ae7-3c6b-858b-5d8ec56923b1 | -11.80037 | -56.96532 | 2026-05-07 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c3aecb0-7e27-35d4-a245-735a76f91c1c | -11.80097 | -56.96167 | 2026-05-07 05:08:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c099a21b-169a-3e40-9024-b41a9f8370b2 | -14.12945 | -45.34787 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93c7593f-aac5-3c91-b9a7-42def6ff6dd2 | -12.50685 | -58.47315 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17822b54-d5e2-3247-84c9-2405de69620b | -11.43891 | -55.10051 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c40ae14f-5246-3dd1-a3ab-2bef4d08d957 | -11.72841 | -54.8082 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ba95b53-0f77-30f3-97a0-ebf2400b155f | -12.91615 | -49.48637 | 2026-05-07 05:08:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ba3753-236f-36dd-bfba-b8ef997965e0 | -13.88827 | -47.52569 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec52160d-d16f-31aa-892e-a084f3ced31c | -10.23683 | -52.23124 | 2026-05-07 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d830c4e7-a863-35ac-9d52-6d616a917274 | -11.73844 | -54.80981 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c8f76283-eb43-315c-8465-04a3feac539e | -14.12993 | -45.34357 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0709fafa-2347-39aa-91c5-cffb8a86fa0c | -10.4858 | -49.35984 | 2026-05-07 05:08:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3d69321-fb15-34b0-b096-52f2008a2436 | -13.69335 | -52.58939 | 2026-05-07 05:08:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 957ea0c2-4219-36fb-8cdc-65e4c21ed691 | -10.63917 | -48.00674 | 2026-05-07 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 85e5bc5f-9ce9-360b-b712-a1c668d3a3a4 | -12.50264 | -58.47654 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6b2d3d-ec1f-3910-8ee4-d459668cb2e4 | -11.43836 | -55.10404 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dad45d5-2570-352e-8cee-0dbdbec54e5e | -12.41459 | -49.66973 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc697c09-1ff2-3911-9287-aa73e6ba2f44 | -14.12595 | -45.34829 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f53ab10a-7c97-3392-a1b4-dd0fa6d9293e | -12.41265 | -49.67123 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b9363e6-7b8f-3d78-98e8-a69673fee783 | -12.34915 | -50.03222 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53747027-0bff-3291-bb68-13123067650c | -11.73231 | -54.80517 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 017fc3d6-989b-3b5c-9417-703d8af781ff | -11.61889 | -48.05441 | 2026-05-07 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a19da2f-4e08-3434-af79-3a3bfc3cfca2 | -11.61721 | -54.17413 | 2026-05-07 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2dbad33-5f36-37bd-abcc-b98e9b0c4241 | -12.49488 | -58.4793 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba3936ac-483d-3640-b49f-5e23d0433e20 | -12.7552 | -46.96703 | 2026-05-07 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6453962e-85fa-3869-b737-dda74e3593fb | -14.86033 | -48.56348 | 2026-05-07 05:08:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 879f42ce-d79b-3c51-882d-886774559d11 | -12.86467 | -43.75109 | 2026-05-07 05:08:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfa8762a-04fa-34dc-bae4-d310037ce34a | -14.13235 | -45.34482 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c062ffe6-ce30-3df2-a313-b916a05be591 | -11.60392 | -48.05737 | 2026-05-07 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 997a0d70-b67c-3f13-a102-e5dbabe3e657 | -8.68176 | -49.09195 | 2026-05-07 05:08:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a889bf9-3688-3b48-a352-363397748071 | -11.60868 | -48.05811 | 2026-05-07 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6150cc02-486b-385e-9a3b-c6647153db32 | -11.73342 | -54.79805 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9384b479-26d4-3f15-b13a-14dde35770e7 | -10.24043 | -52.23179 | 2026-05-07 05:08:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d47988fc-0e84-35cd-94a3-663f7b9e3a68 | -11.61412 | -48.05368 | 2026-05-07 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd475d3a-c815-38b1-bc4f-f4db565e6a6b | -12.50332 | -58.47253 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8124f293-c290-30a7-8c58-f92a694b20cb | -12.75559 | -46.96396 | 2026-05-07 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21eb54e5-e070-3e2a-adc9-718776459bf5 | -13.95804 | -47.54868 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| edf12eef-07c9-3973-8a38-a8eb62fab48a | -11.73621 | -54.80215 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fa42343-f452-3a0d-9069-d3b8480320ec | -14.12545 | -45.35254 | 2026-05-07 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 819cb006-0151-3fb2-a6ee-cc6744f2684d | -11.73789 | -54.81337 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 630a771b-6cde-376e-b760-dd4baf51c37c | -12.99045 | -54.68224 | 2026-05-07 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21c630d7-f46f-3a3a-97bb-9c6f7549ff69 | -12.50195 | -58.48055 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c41fe6a-dd92-3181-b9a5-9c3af386c4f0 | -12.77468 | -59.00661 | 2026-05-07 05:08:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd4daaa6-7d1f-3fba-8a59-f1d0c13c98b1 | -12.49624 | -58.47127 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README7.md)
