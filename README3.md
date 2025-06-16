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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92963080-0c01-3130-b8c0-a8883f033041 | -11.0115 | -55.0561 | 2025-06-16 01:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| f5f511c8-7649-3155-9670-a527352f9df1 | -7.1167 | -44.0571 | 2025-06-16 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 32bb2575-87f9-330e-9782-c10dba6bfd3b | -7.1169 | -44.0339 | 2025-06-16 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 5b64eedf-8c18-3ecf-b1bc-18247a18443c | -11.1379 | -53.9429 | 2025-06-16 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| df43a23d-c678-3ab9-9df0-47c0c9280137 | -11.1568 | -53.9411 | 2025-06-16 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 08bc11a4-0bb0-3b57-a891-2c2835062a9f | -7.0981 | -44.0357 | 2025-06-16 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4159a947-8653-38aa-8ac9-a6922010ae28 | -11.0115 | -55.0561 | 2025-06-16 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 627753ce-26d8-32cb-ad2f-8fa0794239f6 | -7.1357 | -44.0322 | 2025-06-16 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 09d0e17e-e66a-30f2-b672-52778249021b | -10.9926 | -55.0577 | 2025-06-16 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 471e4b88-75cf-31a7-89c5-f31ca9362331 | -11.1382 | -53.9223 | 2025-06-16 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c317cc02-766c-3fa0-8c36-7a8fa9d602a3 | -11.0113 | -55.0764 | 2025-06-16 01:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5fe4263e-0651-3c70-a569-754e1494d544 | -7.1355 | -44.0553 | 2025-06-16 01:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 7a3d2337-d510-3dbc-a52f-f1117d68fa3a | -11.13655 | -53.931 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 9fe2ac29-37ba-39c8-9d61-a9b86f19c4bd | -10.09689 | -52.74654 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6b630cc3-1974-36c9-bbde-5f18734e984c | -12.02774 | -57.09204 | 2025-06-16 01:20:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ca1d111b-e45c-398f-8d9f-107589a848dd | -10.99778 | -55.05085 | 2025-06-16 01:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 271d1abe-c3bf-3e4c-86e5-214e532deb5a | -10.09431 | -52.73053 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| fd21b998-1292-3054-ac9c-cd1034e659ad | -10.23103 | -54.29786 | 2025-06-16 01:20:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 655e8e1d-59ff-38ed-b1bb-9f426e99557d | -11.00907 | -55.06041 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 9c5f3a78-ea0e-3b05-8947-1fe2b1aab25b | -11.01112 | -55.05409 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 75cb5960-41b6-3685-bcae-cb900253cd4a | -11.98735 | -57.19022 | 2025-06-16 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 73d263f9-f4bd-33bf-9b56-f01196e4169e | -11.00747 | -55.04939 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| dbc41822-61e6-3e58-9f71-1f2a63b7df2a | -10.09844 | -52.73545 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 4ee0d6e5-131a-3d91-9d1f-ca528c54511f | -10.08681 | -52.7374 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 3fbd7ccc-6e5f-338e-bef8-e8bb702e76b8 | -11.14893 | -53.94211 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 7c340315-4dbd-393d-8409-0906d02fe115 | -11.01278 | -55.06503 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| e2e29e50-bca7-30f6-b4dd-d46747304e5f | -11.14698 | -53.92939 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 3f87543e-d53a-3e8d-8c69-7be2955cd22e | -7.72332 | -55.14267 | 2025-06-16 01:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a080e1b9-1acb-3d35-8d86-83007c0262a4 | -10.85826 | -53.78132 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 55db0c42-48bb-3d50-b6b1-c9e2f46f3878 | -13.92153 | -54.63974 | 2025-06-16 01:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 81380d1f-d7fc-340f-904f-0ef623df43d2 | -14.03195 | -55.12178 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9a7b4ac8-c398-34d9-ac92-c8ce602a944b | -11.14048 | -53.95642 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0ff64530-735f-3930-b9b3-15119c5e2956 | -13.91992 | -54.62906 | 2025-06-16 01:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 00c17fff-cbe7-3777-9b48-319466b9ae8e | -11.00946 | -55.0431 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f409e3b7-d15f-3faa-9f1f-a5499a5354be | -11.01442 | -55.0759 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| effd4c10-5972-3843-a133-d543d4c41eb2 | -10.10091 | -52.75154 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| eef98329-c8da-3cb8-acef-8249a2e60472 | -10.07517 | -52.73925 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| e114a358-42b5-3f3e-a1da-22082100c18c | -14.54393 | -59.87132 | 2025-06-16 01:20:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4352d7fd-4add-3a4c-9c71-f04358254d3e | -10.99939 | -55.06188 | 2025-06-16 01:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 74ca65f9-6582-3528-ba40-bc6b2aa23f7b | -11.98861 | -57.19923 | 2025-06-16 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e89b7c4d-8e55-37db-8575-a2ae4173f652 | -10.07766 | -52.75533 | 2025-06-16 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 71ad0bb9-7f3d-3114-93a3-23ac9dcce81b | -11.001 | -55.07285 | 2025-06-16 01:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 233f6c31-93ae-338f-a06c-20cf40e24866 | -13.9183 | -54.61837 | 2025-06-16 01:20:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8fbb989-1b74-31ba-b4ab-9697a330f4b3 | -11.13851 | -53.94369 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 203.9 |
| d4582ce8-06d5-3b2e-8393-2d167cf7b469 | -13.28885 | -57.07671 | 2025-06-16 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6b37cb8b-0410-3af1-86f8-b1c899fb98be | -11.01066 | -55.07132 | 2025-06-16 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| b5f00e76-fa48-3a92-af22-3def8bf5773b | -10.84768 | -53.78307 | 2025-06-16 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c540bcc0-f30a-3da5-90c3-b48694e0bd78 | -7.1167 | -44.0571 | 2025-06-16 01:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 5565da23-2871-3a3a-af2e-f2ba95cbc78e | -7.0981 | -44.0357 | 2025-06-16 01:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| eb1283c0-edda-32e5-b88d-020d881d9225 | -10.9926 | -55.0577 | 2025-06-16 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| ed614e4e-d4d7-363b-9225-2945aada5d00 | -11.1379 | -53.9429 | 2025-06-16 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.1 |
| e84c1f73-fd88-37e8-bc00-f074300d3ab6 | -11.0113 | -55.0764 | 2025-06-16 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 4edc8594-3374-3a3a-a88d-e7cbf001ea07 | -7.1169 | -44.0339 | 2025-06-16 01:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 358.3 |
| 8d5d39d5-4c64-38b9-b368-6b19922da364 | -11.0117 | -55.0358 | 2025-06-16 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6f43f017-4ca9-3b58-8796-7c828626a6ee | -11.1568 | -53.9411 | 2025-06-16 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| c32fa0c9-3527-3885-b4bd-24ea22eba3f5 | -7.1357 | -44.0322 | 2025-06-16 01:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 5a8d192e-5a7a-31d1-9514-525ce0fad6b4 | -11.0115 | -55.0561 | 2025-06-16 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 149.2 |
| 3b120548-b431-3cc2-9f2f-0f0729db4386 | -11.1382 | -53.9223 | 2025-06-16 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 98dc6e86-7f39-31c3-9fe5-ef5baa4aea6a | -7.1169 | -44.0339 | 2025-06-16 01:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 333.8 |
| 7e8242bf-c322-33c1-925e-8a1acf1d4436 | -11.0113 | -55.0764 | 2025-06-16 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5e7d15fd-8cbc-36dc-a37c-868e2bd32dd6 | -11.1379 | -53.9429 | 2025-06-16 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| cfdad259-e1a5-389e-ab68-1efbec83035c | -7.1172 | -44.0108 | 2025-06-16 01:40:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 31e347a0-e50d-30af-ba35-4a8a6336aae2 | -11.0115 | -55.0561 | 2025-06-16 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 76d98992-fb0c-3033-b299-65c4f7b95091 | -7.0981 | -44.0357 | 2025-06-16 01:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 405f2029-db5a-3c0b-a33a-84e74d3df44f | -11.1382 | -53.9223 | 2025-06-16 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| bc4ac594-bf4d-3b95-8ebb-3493cf1f6a64 | -7.1357 | -44.0322 | 2025-06-16 01:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c7cbb2aa-6fd1-3893-8db8-80c6a568a429 | -10.9926 | -55.0577 | 2025-06-16 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3091e18b-fc86-3178-a662-6832405e3ae6 | -11.1568 | -53.9411 | 2025-06-16 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 852566c9-178f-3a75-ab0a-e16095a3a9fc | -7.1167 | -44.0571 | 2025-06-16 01:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 4baf37a2-98c4-3e8b-8312-7124106c9f2e | -11.0115 | -55.0561 | 2025-06-16 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| e69aa06b-4ed8-35d1-88bb-28b6c99cdc9e | -10.0972 | -52.7376 | 2025-06-16 01:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8c9d7d7e-fee2-33e5-a9ee-2550049ee4de | -11.1568 | -53.9411 | 2025-06-16 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 50075a67-1aef-39ef-bce2-50b5ac4adf34 | -7.1357 | -44.0322 | 2025-06-16 01:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 191ac491-584f-3181-9071-9ef008ec4a0c | -11.0113 | -55.0764 | 2025-06-16 01:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 975a0e11-3ed4-37c8-a59f-facae1ba8d51 | -7.1169 | -44.0339 | 2025-06-16 01:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 294.8 |
| b3ddf923-74ff-3ef2-824e-e8675618a31b | -7.1172 | -44.0108 | 2025-06-16 01:50:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 27cbf70a-f7cf-32fc-a862-81e8c1039152 | -11.1379 | -53.9429 | 2025-06-16 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 82b5e8a6-0f61-3ba7-b37a-d05eadcacfee | -11.1382 | -53.9223 | 2025-06-16 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| d2fa2649-dccc-3363-8bfc-41c12a8620de | -7.1167 | -44.0571 | 2025-06-16 01:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 130.6 |
| e19cb207-2633-35da-9d79-da72c2543989 | -7.1167 | -44.0571 | 2025-06-16 02:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 7038048a-cec3-38bf-b797-c8bc9d435fcc | -11.0115 | -55.0561 | 2025-06-16 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 26146e92-db83-3f87-a3d0-0c4132e88a21 | -7.1169 | -44.0339 | 2025-06-16 02:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 281.9 |
| 6d4ebb83-7b8e-3338-a1c7-9702385dd55c | -11.1382 | -53.9223 | 2025-06-16 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| adde39bb-0b33-3e2c-a8cc-0839cc9b7ea5 | -10.0972 | -52.7376 | 2025-06-16 02:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 492fa348-9e5d-3e67-b93c-e527dfcac3c6 | -11.1568 | -53.9411 | 2025-06-16 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| be25f9c3-9cb9-383a-b7c5-48995566b943 | -11.0113 | -55.0764 | 2025-06-16 02:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 8b05b19b-5a00-3ac7-a131-2dccebb9f9f4 | -11.1379 | -53.9429 | 2025-06-16 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 0dd37b74-9cda-3a69-aaca-7a43af53f829 | -11.0113 | -55.0764 | 2025-06-16 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 37.4 |
| e39991c7-fb43-38c3-8140-eca9435e6cac | -7.1167 | -44.0571 | 2025-06-16 02:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| a9f59323-26f1-3c23-8c41-ec7e5a2ffd7c | -11.0115 | -55.0561 | 2025-06-16 02:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 5285df4b-c795-3c86-af07-9b7161e5e2df | -7.1169 | -44.0339 | 2025-06-16 02:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 257.2 |
| d609771d-64ed-31d8-8f28-8e7ac486186e | -10.9926 | -55.0577 | 2025-06-16 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| ecdf0579-8709-3150-8be2-ef2e178ae619 | -7.1357 | -44.0322 | 2025-06-16 02:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 03d9d110-45d2-331d-8f64-2812f0a9340d | -11.1379 | -53.9429 | 2025-06-16 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7a15ebe6-d1c4-3767-a921-cb9a7c499c83 | -7.1167 | -44.0571 | 2025-06-16 02:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| ab4ac3bd-e018-3770-96f2-c7695a46c9c4 | -11.0115 | -55.0561 | 2025-06-16 02:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 111.5 |
| db9fcb68-8a5b-38de-84ac-e55201bf6c6c | -7.1169 | -44.0339 | 2025-06-16 02:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 244.6 |
| 7f844f53-9b34-3fe3-807e-e065223240b9 | -7.1172 | -44.0108 | 2025-06-16 02:20:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 71d26fed-3511-3ebf-999b-6a7e6795d41f | -7.1167 | -44.0571 | 2025-06-16 02:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 745a6654-fc70-3c5f-84e7-340d209b77e2 | -7.1357 | -44.0322 | 2025-06-16 02:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README4.md)
