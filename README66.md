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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9dca27e-fdcc-347f-a311-e8f4d7597b38 | -6.583 | -58.9658 | 2026-09-12 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 0f10df02-0878-309e-8c4a-08367f0dfd26 | -6.2029 | -57.7193 | 2026-09-12 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 72644218-88ec-3cc9-964c-cc3a84b9c47d | -2.7331 | -57.6465 | 2026-09-12 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 67633a68-d371-3a9b-bfba-fcc7916206d8 | -6.1662 | -57.7013 | 2026-09-12 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b9d67cd5-61f4-3dea-a65b-10d5db1e2f2b | -10.2171 | -45.2799 | 2026-09-12 16:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 78a35e31-f514-3925-9697-42f546076142 | -9.6755 | -46.0047 | 2026-09-12 16:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 6ef98615-ebd4-3c51-8ae1-427fc2e25a0c | -3.3688 | -59.4079 | 2026-09-12 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| d37cb335-5f44-377e-a4e6-8b5d2ee45f69 | -8.8132 | -46.9495 | 2026-09-12 16:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 3f4489f2-f9c1-3c74-ac17-f363b90539b4 | -11.0839 | -50.8368 | 2026-09-12 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| ada125e1-e028-37f0-a52f-65c16a071522 | -3.3504 | -59.4274 | 2026-09-12 16:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 31f3f091-fac5-3cc0-8ce4-f262362d423e | -4.4654 | -55.4435 | 2026-09-12 16:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| cc8d769b-13a8-303b-be80-8d186dc81bdf | -9.1339 | -51.5927 | 2026-09-12 16:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 714.0 |
| d511b6e0-7ffb-3f2e-9133-781652b1b0fb | -6.166 | -57.7208 | 2026-09-12 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 149.4 |
| 4becb34c-bbc3-399d-8cc4-c8cef01191ae | -10.5161 | -57.4395 | 2026-09-12 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| c06c0dd9-7194-37b4-869c-499d70f24cbc | -3.3322 | -59.4086 | 2026-09-12 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 4690e475-e8dc-3593-8135-f4c90b6cc582 | -10.2171 | -45.2799 | 2026-09-12 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c4a79703-59aa-3f01-97e1-25967e366eec | -3.3504 | -59.4274 | 2026-09-12 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 20cb0faa-aabe-3d24-b81d-ab64791b4052 | -6.1993 | -55.2739 | 2026-09-12 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 4197115c-7e35-3599-8cab-7d69ce2414ec | -6.1846 | -57.7005 | 2026-09-12 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 676c9e53-017e-36e6-8335-7b463a389ca3 | -3.4059 | -59.2155 | 2026-09-12 16:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 98bc313c-71cc-39c2-860d-8f1d5e99853e | -9.5319 | -45.4546 | 2026-09-12 16:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 156.1 |
| e8f70eac-893d-355e-9006-6912ce255a40 | -10.2933 | -45.2702 | 2026-09-12 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2c1a1006-5060-3dc9-9b8a-31847b9363e6 | -3.3687 | -59.427 | 2026-09-12 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 2ab40f0f-2e28-3793-a52a-a7f49083af05 | -13.3953 | -51.6956 | 2026-09-12 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 58d86286-7ff3-3df8-94ee-217c83203a30 | -3.8278 | -58.9182 | 2026-09-12 16:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| ce3505ad-802f-3942-b93d-35395d65654e | -10.5161 | -57.4395 | 2026-09-12 16:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 4c6d0131-809a-3d7a-8e37-79c570a56d52 | -11.2488 | -54.1378 | 2026-09-12 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 255f3d3e-7eac-3fb5-a976-4f8ce584f43a | -8.8132 | -46.9495 | 2026-09-12 16:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 425b5f0f-583e-36b9-86e2-9a7c56e9cabe | -10.2206 | -50.373 | 2026-09-12 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 203.3 |
| da3a6387-3e69-3b7d-b3ad-a701a4b45b63 | -9.1358 | -70.8171 | 2026-09-12 16:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 747f91f4-78da-3fc6-8710-9d257adc0e0d | -3.3504 | -59.4465 | 2026-09-12 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e51fb71d-68d3-3b8e-8d39-b3c5171560f2 | -2.6602 | -57.5119 | 2026-09-12 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 8bcff589-8625-33d8-a5a9-d9d40ea35e15 | -2.6785 | -57.5115 | 2026-09-12 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 997cacd7-35b8-3dbf-ba54-74f982b558f2 | -12.66 | -54.58 | 2026-09-12 16:15:00 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5c386cd-f97c-3323-aa7f-046c200b292b | -12.7 | -54.65 | 2026-09-12 16:15:00 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4e93f6-ed67-3e69-918d-69c4749ae07c | -12.67 | -54.64 | 2026-09-12 16:15:00 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 865c0733-7124-314d-a1e7-04321210a89b | -12.67 | -54.71 | 2026-09-12 16:15:00 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae56bae-8ecc-3b5f-8449-ffaefd475b1e | -8.07 | -54.78 | 2026-09-12 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c75111ac-b858-36e8-98ff-8536db790f68 | -9.13 | -51.57 | 2026-09-12 16:15:00 | MSG-03 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9b506df-8540-335a-8371-0b7a461dc4aa | -8.01 | -54.76 | 2026-09-12 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1bd08a-0e3e-3ce3-b7a2-4009ef4b10d6 | -12.7 | -54.72 | 2026-09-12 16:15:00 | MSG-03 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51bca82e-36b0-3742-b157-9b567dc95a7d | -9.13 | -51.51 | 2026-09-12 16:15:00 | MSG-03 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e62658-5c02-37e3-b418-0e9bcd5e25b8 | -8.04 | -54.77 | 2026-09-12 16:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdf09a1a-9a03-340d-9d84-24a9076f8faa | -11.0839 | -50.8368 | 2026-09-12 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.9 |
| ed4af0eb-bc63-3cac-86eb-78a476de4dba | -11.2488 | -54.1378 | 2026-09-12 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 3cf936ca-25b5-3d70-a4b8-a457d131bd36 | -10.7274 | -50.6192 | 2026-09-12 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 0c5e881b-8f0f-3791-9465-62301c7c0d78 | -2.7149 | -57.608 | 2026-09-12 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 0a174890-4f99-32c8-b2ad-cede7f3bfe3e | -3.5345 | -59.0401 | 2026-09-12 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 65a70b52-c1ca-3e8b-940a-f726d3d71b70 | -9.6854 | -48.0288 | 2026-09-12 16:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| a35c94ba-b693-3f7b-862b-3dcc5e07fdad | -6.1846 | -57.7005 | 2026-09-12 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 956ecfee-9af8-3c5f-924a-d5138156b3de | -9.6755 | -46.0047 | 2026-09-12 16:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| e3c7174a-19bd-39ef-97d6-a52bd456c053 | -8.8132 | -46.9495 | 2026-09-12 16:20:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 318.0 |
| 07f9353e-f2f3-3fe3-a3d6-e2e63b62e835 | -8.8132 | -46.9495 | 2026-09-12 16:30:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 42e2e725-8b61-3462-9e14-5a746c61c29f | -2.6602 | -57.5119 | 2026-09-12 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 507b466b-f339-35b5-822d-626d92c9b297 | -10.6621 | -45.9974 | 2026-09-12 16:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 2424b2ce-0dbe-34df-aa76-66a8855ca267 | -11.0839 | -50.8368 | 2026-09-12 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 882975ce-8b9d-316d-9b43-53206fe970a2 | -11.0839 | -50.8368 | 2026-09-12 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.4 |
| fb38697c-cc9c-3816-8717-d6d49bcc51d1 | -10.2933 | -45.2702 | 2026-09-12 16:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 152.2 |
| e283cbe3-cb45-3008-89f3-0448fb7b876c | -9.6854 | -48.0288 | 2026-09-12 16:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 8e1ad657-5176-33e7-b595-88e0e94e129f | -3.2954 | -59.4667 | 2026-09-12 16:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 42b7fc79-c488-39fd-aefe-46df0f9fe860 | -13.3387 | -51.6389 | 2026-09-12 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 223.7 |
| c8af7e5c-73a1-32b8-9229-5809b310041f | -2.6602 | -57.5119 | 2026-09-12 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d1e241ec-6f1e-3d3f-9ec8-5e28a809f84f | -9.6755 | -46.0047 | 2026-09-12 16:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |


