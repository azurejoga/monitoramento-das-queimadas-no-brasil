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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f162927d-859f-3f26-8b35-739cc1bf767e | -14.08419 | -46.24347 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 034fc756-0691-3e57-ad7b-e06016af8400 | -14.07121 | -46.25761 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be283178-5631-3a45-9cf9-8c7da89ee161 | -13.06173 | -52.72935 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e096c0d-eb28-39d6-b7c1-66de3aaddd5f | -12.19731 | -52.86645 | 2026-08-01 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15fef632-a34a-3215-b428-7bb71ef3f4ec | -15.82105 | -48.17338 | 2026-08-01 04:57:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df6696e1-8fd1-3f98-9037-894ba564cc35 | -13.05897 | -52.72526 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8aa56801-e503-3087-a5e9-4f5fc6c8a11e | -11.24004 | -54.85479 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 086a0719-9ebf-36e4-b8a4-6ba52c089c1e | -14.0763 | -46.25381 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 638f81c7-f3f1-3b78-8490-838b6a9fe5b9 | -8.19126 | -55.43467 | 2026-08-01 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7928e282-f40b-3e6b-b206-f6b5eeb6b29d | -14.33664 | -48.0323 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 685fa761-4e11-35d0-b707-8351c8921837 | -14.07744 | -46.26059 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f55edaa1-41f5-3fb0-8f55-f8096aea3c62 | -11.25275 | -54.8652 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0c0e6daa-1c24-3d1a-941c-1cec85f376af | -14.06958 | -46.25036 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0921e2b-1a7d-3b37-9953-8c4dcd3b7adb | -13.01687 | -57.08496 | 2026-08-01 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b33beed0-19c8-30d3-bc60-98ea127a3710 | -14.07801 | -46.2561 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d16eaa05-7846-3078-9fec-11059db0bf04 | -14.08191 | -46.26139 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a64f0d26-eefb-32da-8f49-ebd5f2e20d7c | -8.19425 | -55.43981 | 2026-08-01 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e918971-24c9-321b-a6a7-1b14307cb8f5 | -14.07576 | -46.23767 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68222fd0-ea0e-30aa-88fe-771ae3d92da7 | -14.77206 | -48.29836 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33c2aa85-432a-3509-b779-1481d67ab08b | -11.3206 | -54.4758 | 2026-08-01 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e88e70c9-83a6-3386-bb3c-83f208541952 | -14.34858 | -48.03476 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1875d875-a728-3a6f-9bc5-69b8f16db6bb | -14.08247 | -46.257 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27a01177-c91b-3c35-9c98-4870cb6e398b | -14.07417 | -46.23542 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e48d5034-748c-3005-9cd9-b13a187df386 | -11.13801 | -49.90395 | 2026-08-01 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fb19d1b-1afc-35b8-8f23-d4f424774bea | -14.07139 | -46.29036 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| dbbfb4d0-16ff-3345-bf9a-2e8b8f0f36c4 | -9.87955 | -48.73362 | 2026-08-01 04:57:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26cfd9a8-658a-3107-a640-ae9b00d78683 | -14.0724 | -46.24866 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8147562b-126e-3287-8292-ffe48a2934f4 | -11.24705 | -54.85603 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b9e82183-b59e-3df5-8286-e757bf66425c | -13.06617 | -52.72282 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5084977c-d362-3f45-a29f-1c7e2a0aad43 | -14.08583 | -46.25105 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b3b292ab-e743-3e1e-b5db-fe7a1d1a835a | -15.12521 | -49.27893 | 2026-08-01 04:57:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b71af369-cac2-3e87-8914-f9b7d497628f | -11.23216 | -54.83707 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 556e06db-91de-3b24-9b3f-d1a18826c34d | -14.41719 | -48.04704 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a56762e6-cf31-35cf-ae74-ed55655d727f | -11.24156 | -54.86731 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 806d21b6-2220-39d8-88e2-c02a88883bba | -13.06341 | -52.71874 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ae39a49-891b-3bb0-9a70-b341fa2c8976 | -9.15741 | -48.83165 | 2026-08-01 04:57:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c775a3be-3690-354c-91dd-26c7dba44284 | -14.08408 | -46.28033 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf1e5c9b-bfc4-35ac-87b7-636ed4f14835 | -14.08921 | -46.23999 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1c853b9-0e80-355f-baa4-189bcf34cd99 | -14.33602 | -48.03677 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f048f4b-18c6-3901-bc6e-40d37b0b0190 | -9.82111 | -45.3322 | 2026-08-01 04:57:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 877bd3c4-52e9-3e6c-9c98-248eed7f20ef | -12.24294 | -47.18319 | 2026-08-01 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 368e043b-0acb-3a73-845a-55d17a681893 | -15.57664 | -46.80697 | 2026-08-01 04:57:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ad93153-8824-36b0-8f05-3acd134da618 | -12.24017 | -47.18375 | 2026-08-01 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ff50a73-41fb-31e8-930a-61cc38d5b23d | -13.9563 | -47.82382 | 2026-08-01 04:57:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2334f0f-2735-3f62-a3b5-11eb2a4636eb | -11.23673 | -54.87466 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3d74e450-2462-3dd3-90aa-08982840cd0d | -11.29701 | -47.0312 | 2026-08-01 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8788c0bf-7cfd-3758-b5d2-1be393b14366 | -13.1649 | -53.25532 | 2026-08-01 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bd642da-af67-30f2-b405-ceffc7f7b54c | -15.87856 | -43.60013 | 2026-08-01 04:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be65225d-08d9-3f2c-ad6d-afe6f00ed84d | -8.45094 | -51.5032 | 2026-08-01 04:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 847c69f2-643a-3294-a7c0-0f92a0cd4ca7 | -14.07785 | -46.29343 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 28a54aab-3841-3255-96e5-adab82eb246e | -14.08704 | -46.24204 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a17ef7b9-583f-31be-9fe4-75f340973599 | -14.08684 | -46.29455 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55f732b2-338d-36ce-9aba-680a7e6a7329 | -14.08292 | -46.28947 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92d02821-e665-3cc2-b7a6-9b969598f751 | -14.41065 | -48.06499 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b092bcb6-4540-3f39-9729-4219cccd5d8c | -14.07448 | -46.26736 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 73b82c5d-3e29-35f7-9422-a0aed2aecdcd | -14.07063 | -46.27826 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 19dc50fe-2c95-3916-b960-16093c82d440 | -11.22866 | -54.83646 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afaa6f6a-5dbc-345c-a6dc-fd0c15ef8eaf | -14.07896 | -46.26806 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6723c7c4-556d-35b4-83f5-d908338c3136 | -14.8144 | -48.51862 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dd5981d-7502-360c-b183-5d24e12b0811 | -14.07465 | -46.24641 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 498f1234-6cb7-359c-bbee-b0e86fcf901f | -12.23882 | -47.18259 | 2026-08-01 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 949f5145-5d16-3e21-911b-349ab75c9380 | -13.26246 | -54.36049 | 2026-08-01 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0f8647c-9aa3-3410-b5ea-ad08a2f15b11 | -14.06947 | -46.28745 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 141aef92-5f01-34bf-bc39-724c18c413ac | -11.29192 | -47.03785 | 2026-08-01 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5d2eb2f-b988-33dc-884d-70eff8c69b3d | -14.07685 | -46.22904 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e1fb30-967c-3a2c-b5c8-fcc2ed3eec2e | -14.08526 | -46.27104 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0843baf8-c530-3f04-b95f-15f462119be2 | -9.87892 | -48.73792 | 2026-08-01 04:57:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a04c367e-d16c-3e9d-b93d-ecca9077d723 | -14.34313 | -48.04459 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e95e23d-0c54-302f-8e05-56973ad50f6f | -14.08345 | -46.26875 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0d688ee3-26dc-3f01-a9f1-0a91bde0c9e9 | -15.82415 | -48.18107 | 2026-08-01 04:57:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eeb76f3d-bb0a-3d93-8298-bd818c50bb42 | -11.54557 | -50.13881 | 2026-08-01 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeba8e2f-af7d-3350-b91f-8802f507eb7a | -11.25121 | -54.85269 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| cdf6972c-b3dc-3540-8b8d-357bab9c310c | -14.06731 | -46.26831 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fa3d1b17-a58f-37b5-8903-7ac03732e59c | -11.24639 | -54.85999 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 032a2276-de73-3160-9106-2a0d693f5a78 | -14.07587 | -46.29106 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c7df4ba-2b5c-3d7c-9100-e7b485482b29 | -15.57983 | -50.27108 | 2026-08-01 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60e24d71-265e-3132-a8ce-48f10250555c | -11.24573 | -54.86395 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b732abd5-a76d-3a34-bcd1-1ce7ae327dfb | -11.24924 | -54.86458 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 8553ef3d-f460-3ebd-9792-3883510487a7 | -14.77534 | -48.30412 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15f5aa9a-5ee7-3897-a338-0995f996f27e | -14.07395 | -46.28817 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e33a344-5fb7-3d7f-ab68-194bd24147e4 | -8.51863 | -54.77392 | 2026-08-01 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f4b4ba7-26b9-31ca-9c45-1193440ecb14 | -14.08304 | -46.25254 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56fa967c-2504-36a8-82d6-2320eac27e0b | -14.07957 | -46.26352 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a675c7c1-7300-38f5-96a7-e3650dcf29b4 | -11.14151 | -49.90449 | 2026-08-01 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec600da-70b0-3186-81a0-0250bc6eda01 | -14.08234 | -46.29402 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc4e740f-26cf-3981-b96b-7bc0205a13ed | -11.25056 | -54.85665 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3fe13134-acc9-3d72-80a8-6b3ec07fd08f | -14.08761 | -46.23779 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3bc5d5c-4ffe-3c9c-b527-5b8a74953f56 | -11.1065 | -54.81245 | 2026-08-01 04:57:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5488794-9d8f-3a6b-b785-e7076500a83c | -13.16707 | -53.25602 | 2026-08-01 04:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7150cea-0a02-320e-b6e5-1c258e39f055 | -14.40962 | -48.04241 | 2026-08-01 04:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8564fd1-bd79-32f0-962b-63eb63263be9 | -11.31997 | -54.47963 | 2026-08-01 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb89b03d-f37a-32d6-90ca-730351327f9e | -12.30727 | -43.72545 | 2026-08-01 04:57:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21b3426a-312f-3f0f-9d7e-482a080a0a40 | -12.80986 | -47.17258 | 2026-08-01 04:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97068c8d-2c52-36ab-a700-13aa8d53a3f4 | -14.07981 | -46.22753 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0afd0f19-6de9-30b8-b56e-933a7331bdd0 | -14.07337 | -46.29274 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 613a47eb-eb3d-370b-b51d-53dbbe4edcb6 | -13.06285 | -52.72227 | 2026-08-01 04:57:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f749ca7-96eb-3f57-91ed-c0eed4f5149e | -14.08821 | -46.23333 | 2026-08-01 04:57:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6b41974-84e9-3114-867b-a048efa27a22 | -13.22176 | -54.3956 | 2026-08-01 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0563c17c-55e2-3fb3-9ea9-9d849d6eb323 | -10.47186 | -48.49767 | 2026-08-01 04:57:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9ce7ce3-3330-35cf-8a6d-0f27c4ef19df | -14.07 | -46.26667 | 2026-08-01 04:57:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README19.md)
