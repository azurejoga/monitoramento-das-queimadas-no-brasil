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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f6854e-69a6-3b16-9959-3cda9bfb8437 | -4.40199 | -49.66786 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c7ff02c3-4b86-3487-a19b-0c2a1c03350e | -3.74133 | -52.42741 | 2025-11-09 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dd56a04a-a265-3048-b43f-9e7a8e27878d | -6.12803 | -52.64379 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86636aea-b30e-3705-a683-ab41f269799f | -3.4963 | -46.30336 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e4e981d5-ee1e-3587-885e-8a12dd4f2c5d | -6.88735 | -49.25171 | 2025-11-09 00:34:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| e524f1f8-efa9-3925-bec3-21bdcf9cdc79 | -3.98261 | -51.03298 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5349acb2-1275-367f-8f6b-1d7e7bcc63e3 | -3.5361 | -50.85955 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2501e197-74c7-3e71-aae0-c224f5ad34af | -3.15054 | -50.60642 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0ebaaae9-6103-3caa-8a99-a1b7e8c1a288 | -9.50831 | -47.27445 | 2025-11-09 00:34:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e2ce37f8-ed9d-3b6f-b2c0-acd71af33769 | -5.25539 | -47.17097 | 2025-11-09 00:34:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f2c0426-e8df-32f8-a2f1-16b2f51abad3 | -4.49152 | -50.50587 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8fb2f971-ac13-31af-be80-e25bf87e9782 | -4.37666 | -48.69702 | 2025-11-09 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1ef9282d-46ea-3627-aade-958e53ed311d | -3.83963 | -51.12244 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 682237a5-3a43-3ad9-9664-dd663944a95f | -4.97205 | -49.5959 | 2025-11-09 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7df546fa-f9ee-311d-a93a-b003aea7fe7b | -9.5177 | -47.27304 | 2025-11-09 00:34:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9e97bf46-102d-35f0-9017-bd10c454c071 | -3.31387 | -50.12938 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| a21454fb-db98-3b4a-a063-7376923611cb | -3.33495 | -50.07498 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3f31224a-90c1-3c71-90cd-aa24df86a3ba | -3.31264 | -50.12048 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c190b331-5830-3c55-9c8c-4189f45af2ce | -3.45948 | -49.85004 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 262a75f7-d63b-3670-94df-b70d0cb5cb4d | -3.95234 | -49.02301 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 2e706ac1-a002-3eb2-8ddf-8295d9e6f13b | -1.59248 | -54.30186 | 2025-11-09 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 75092584-d4cb-397f-a15f-a321b2b2e7dd | -3.09363 | -50.32652 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 75a64444-6c79-3db8-802c-c524ae3be6fe | -3.33553 | -44.3556 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1000e4a6-188c-3ecd-b005-56da6d2781d7 | -3.10249 | -50.32527 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 0b7eb054-d7db-3726-8a9f-82a2080331af | -3.15009 | -45.07557 | 2025-11-09 00:34:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a5d0f3a8-7238-3afb-b1c2-8cfc91a17140 | -3.95366 | -49.03248 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 240caa0d-1fc5-3352-a5e7-874e471e99da | -3.74968 | -45.98571 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 13a69dad-10bb-3578-9280-a9dcadd47e02 | -3.86354 | -49.37516 | 2025-11-09 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| fec45ad9-8532-3845-8201-a1864dae927e | -3.75233 | -52.09979 | 2025-11-09 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b2db3201-164f-31ae-aabc-1c393a373cf1 | -2.7454 | -45.1596 | 2025-11-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 4d8f51f0-9bb5-376d-8208-236f3ace1c80 | -4.60762 | -45.5639 | 2025-11-09 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| dd3d102a-7259-317a-99e3-53ed930c4de1 | -3.84084 | -51.13125 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 6a335b0d-4e26-339e-874e-bdd1dd092de6 | -5.30303 | -47.29142 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d7a0df1c-2f99-3178-ab4c-2657b1ebe1f3 | -3.32091 | -50.10423 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d74f2279-9387-3ac7-8f53-2fffb287c7ef | -3.06165 | -49.37397 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83505cd8-8913-3269-92b9-f337cbb40eb2 | -3.44892 | -45.65648 | 2025-11-09 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 92ef0f05-8600-3cb5-9198-a6c940eb212a | -4.14546 | -46.26488 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c49be771-b88d-3d62-91c1-0c3af2126d69 | -4.27714 | -49.89884 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b371596c-82f3-359b-b200-1971e9c20eb8 | -3.0924 | -50.31767 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f0a3248f-38b0-33e7-800d-29047afc25a0 | -4.41074 | -45.94302 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 11f0217e-d9c6-32be-8866-8684c14771fe | -4.52347 | -48.83033 | 2025-11-09 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cd44e450-f15f-33bb-88d2-fb991f923137 | -3.27484 | -50.04393 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dd0baa72-b310-3430-ae6c-febac2c7aaee | -3.45387 | -48.82049 | 2025-11-09 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 234fd2b5-cc05-3485-b5dc-c2418ccaec77 | -4.39024 | -45.96689 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 35587dc5-6209-3414-93e2-89a028389d25 | -3.14066 | -50.27472 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d889577b-d32f-3e20-80b6-f700a4e702d7 | -7.55069 | -45.86319 | 2025-11-09 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 89b2b6ec-da1c-31e7-8510-bb10dd28aed3 | -4.06607 | -50.43452 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c57cd177-4bc4-3f27-a326-eebe93f21201 | -3.77117 | -44.28606 | 2025-11-09 00:34:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 10ba8ae1-6d07-33e8-b4d0-0ce0f520e061 | -4.51712 | -45.72776 | 2025-11-09 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 40121276-6ea3-326b-9f6e-58d848f67a60 | -2.73323 | -45.16138 | 2025-11-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 24.5 |
| e309a1a7-8d49-3627-a6da-4d3b66d5fa0d | -6.05163 | -58.0496 | 2025-11-09 00:34:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fcd92c1d-4e6a-3ce4-a2fa-3be806470279 | -4.37905 | -45.48946 | 2025-11-09 00:34:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 17268f4b-a3f6-3e7f-8233-c5e3d45d2d8c | -3.06105 | -50.22255 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 90cc3e99-ebb9-3fd0-a7ce-02a11c4da219 | -3.30869 | -50.15734 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8d48e1aa-e2e5-307c-8e8a-48c39a75770e | -9.50684 | -47.26433 | 2025-11-09 00:34:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 661dba84-5396-314e-9631-e7d638afd172 | -6.3421 | -46.76434 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| fee44682-dd14-37a9-9606-5546266ff480 | -2.60994 | -49.2376 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d8f51785-5c42-3382-888b-4846537ba83c | -4.64256 | -49.54138 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9c00a465-42a2-3cca-bfbb-4c21b18da413 | -3.43283 | -50.24524 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1b3f63f2-4a9e-3422-bdfd-b47b5043f22f | -3.32777 | -49.89336 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9388c270-10fb-37e0-b1a0-fb31d1bd1224 | -4.62799 | -46.39108 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ae555960-52cd-31ed-a10d-9c7da18cef26 | -4.45494 | -44.63702 | 2025-11-09 00:34:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 49cf846a-6d4a-3048-9c32-cc2501778fda | -3.44891 | -49.97056 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 2e80ad94-8a9b-393c-85a0-85e248a8631f | -4.91003 | -44.6358 | 2025-11-09 00:34:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1584cbe3-289c-3ac6-b5fc-b18b9b0d5eed | -5.37198 | -44.61999 | 2025-11-09 00:34:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9cb8068c-e540-3e96-9fe6-32f5de770457 | -7.56321 | -45.87468 | 2025-11-09 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 80ab9310-fb50-30dc-bdeb-893611583caf | -7.17408 | -44.95457 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 8ed22ac3-e899-3c95-8d34-c2915e2d3113 | -3.73484 | -50.03965 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 07d56817-1ee3-3c4f-a2f6-cc8d88615393 | -8.35502 | -49.94594 | 2025-11-09 00:34:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6200c7d-c426-306e-ad94-2082b6bfa2d5 | -7.4092 | -40.09863 | 2025-11-09 00:34:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 44.8 |
| 63984b92-d38e-3f8a-9f19-3fe884e8ef7e | -3.3385 | -44.37541 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 312.0 |
| cb1de8f3-7a58-3e7a-8425-b036c6d46994 | -5.49275 | -45.86798 | 2025-11-09 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| f253235a-8eb9-3ef2-ad47-cf639cc1e9e3 | -7.40304 | -40.06223 | 2025-11-09 00:34:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 86732d9d-4777-392e-a01f-7b2b85722331 | -5.28818 | -44.9579 | 2025-11-09 00:34:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7318f171-2843-36f9-a60b-df8ec2390318 | -3.66722 | -51.74737 | 2025-11-09 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ae9c0bd2-e46f-343a-8edd-e7e465e7e37c | -3.77006 | -44.28057 | 2025-11-09 00:34:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 6330d7c3-4534-3fa1-95b5-237c4e16b861 | -4.64064 | -46.40291 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 96634320-cfa8-39eb-9426-7f6b15a77927 | -3.66612 | -50.8085 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 50eaacaf-e407-35f3-8886-8baca2f55e41 | -6.34384 | -46.77602 | 2025-11-09 00:34:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 72b3b797-886f-3e22-8e6d-e1ac9f24a9de | -2.73875 | -45.49778 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5e2ffdde-ba50-3864-af64-73f41f2a05ff | -3.65596 | -50.26485 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| be4aa535-72a8-3b4c-aa31-ff4b6f2a4557 | -5.4024 | -47.26409 | 2025-11-09 00:34:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 740615c1-0874-369a-b6dc-fa2b9eb8521f | -3.29222 | -49.76945 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55fd8f76-f618-3182-9dbe-9f61313bb88a | -2.59677 | -49.21027 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d77dd88c-1c25-35ef-bfb7-7d5696b2a01f | -2.4427 | -49.22493 | 2025-11-09 00:34:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6009c7bf-ed44-36e9-92b1-ca07f4a5b563 | -3.58136 | -41.65542 | 2025-11-09 00:34:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| fe2c2889-1632-329a-840b-0dc3d6cf1151 | -3.48547 | -50.36408 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cb30d7c9-89b5-321e-aa04-86bd80d8f65a | -5.4907 | -45.85421 | 2025-11-09 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 24098a82-5469-39e9-a2ee-9307bb14eefd | -3.31756 | -50.15608 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6ce6f675-f2db-3e56-8f28-7d711472439d | -3.43035 | -51.1019 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ca1d36df-868a-3c80-aac3-7a3c17494250 | -5.22781 | -49.57767 | 2025-11-09 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 338cbbc8-e6f9-3d78-b975-cebb84ea60a6 | -4.40395 | -45.97369 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2ec3b26e-b9c9-3cdc-b2be-18c65fc797b8 | -4.13189 | -49.25282 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7bbe2566-67bf-3b0f-aa8d-be46418d2063 | -3.67059 | -51.16723 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 323a8f3a-6236-3fed-a693-e2f717765cab | -4.68518 | -46.40976 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| bdd76439-5f58-33e9-a331-b0a7a67cd5ab | -2.96871 | -49.83042 | 2025-11-09 00:34:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 2866735b-dc69-3b2b-898a-e8a702bef662 | -3.07204 | -49.38202 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 7bc2997c-1ffd-3832-82d8-e981ee5bc1a2 | -3.80598 | -48.90378 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 598bed48-2465-3e78-b997-5a58e8a41197 | -6.01386 | -43.76527 | 2025-11-09 00:34:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b18d4dba-96e4-3626-9d2a-c8193cd69ab9 | -1.59399 | -54.3131 | 2025-11-09 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |


[Clique aqui para ver as próximas entradas](README5.md)
