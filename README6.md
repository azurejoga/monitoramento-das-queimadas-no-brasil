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
| 47068a1b-24d7-318a-a191-0684e2284ece | -10.4996 | -64.486198 | 2026-08-28 01:13:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88633323-26e3-389f-8769-68df153a7a27 | -8.5651 | -54.7668 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424a446d-234f-3d3b-969b-6b423827f9ed | -10.7343 | -54.0271 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8016dd82-588b-3d8c-a65f-ba59e7dd3c83 | 4.1465 | -61.257099 | 2026-08-28 01:13:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9e23d43d-e31c-325f-8aea-06d3a8853265 | -7.5041 | -61.380901 | 2026-08-28 01:13:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b0304c6-9a1e-34ef-b315-219db4686479 | -9.2052 | -65.786201 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32b57be3-8c58-3cbd-abcc-d7692a673e5b | -11.2117 | -54.004299 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d107625-86ec-38a5-8cb1-4d440e77e696 | -8.5747 | -54.764301 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b1388eb-7431-3e63-be03-f6cea36f6b1e | -6.1561 | -57.7756 | 2026-08-28 01:13:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81129238-59aa-3b00-8141-656d11146917 | -9.6006 | -55.119701 | 2026-08-28 01:13:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98d01bcc-e732-3d10-92a3-fd75f92dd1be | -9.1636 | -66.015701 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f0a0719-109a-38db-b7cd-445d28ffc274 | -9.1652 | -66.022697 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38b6016a-94ce-3914-bf10-78a13d6a5ac8 | -11.2051 | -53.979301 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2ff7e8b-7b18-394d-944f-2a2a5c629363 | -6.1505 | -57.794701 | 2026-08-28 01:13:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6368eb2e-b5a4-301f-a01a-666b91845b6e | -9.9497 | -53.934799 | 2026-08-28 01:13:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca9480c0-cabd-32b2-859d-30418eecc736 | -8.872 | -66.882202 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac917411-377d-303b-b97a-9ee3d7a7b41c | -8.5906 | -54.786301 | 2026-08-28 01:13:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a234dc05-e4cb-3ef9-b0c0-f10789364959 | -11.7106 | -54.528702 | 2026-08-28 01:13:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4eb82442-2f9f-360f-971a-7b5be56b962c | -11.2501 | -53.993801 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61ae21b4-8ef9-3bec-aeea-cc4326ff1999 | -10.7439 | -54.024399 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91704f4c-be08-3d41-b11f-02faa706ebae | -8.9941 | -65.439796 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ccbef32a-b550-3e2e-86fd-17912cf8e0ab | -8.9827 | -65.435097 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4434e4ca-b76f-31a6-9f79-df6d59d89d34 | -10.7276 | -54.001701 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df016c35-e9f4-348d-9a2d-189c3c08d207 | 2.026 | -61.4603 | 2026-08-28 01:13:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 23c6960c-8dec-3fcb-a919-045a69a27d80 | -10.5043 | -64.507103 | 2026-08-28 01:13:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4fe46067-a377-316b-b852-85ef7381a7fa | 4.1495 | -61.243099 | 2026-08-28 01:13:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d5ffec12-97bc-3866-92ee-9df8c1c7e464 | -8.885 | -66.8946 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae4db2a7-bc3b-3a01-a3c8-8d1eb81a1e62 | -10.378 | -61.231899 | 2026-08-28 01:13:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e9f7577-745c-360f-be41-ac36d1b87444 | -6.1464 | -57.778 | 2026-08-28 01:13:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d82d8db2-636b-32d1-8f8c-dbc8f68d9903 | -9.535 | -66.766296 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac72eca1-8697-39bd-97f8-d019286b9917 | -8.6406 | -66.532799 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dff50ee7-74fc-365b-9fbe-198a8eccb60f | -6.7331 | -55.666901 | 2026-08-28 01:13:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0c4cf6f-684f-3eff-9193-c03d4ad919de | -10.5027 | -64.500198 | 2026-08-28 01:13:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a040ce25-2bc8-3a04-bba9-eb084b7f7265 | -11.506 | -58.503601 | 2026-08-28 01:13:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dafb844d-92c6-3177-b662-b1aad229a6ec | -11.701 | -54.5313 | 2026-08-28 01:13:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9a6d2e6-38d4-3d62-b0e2-d2dd0ac80110 | -14.1467 | -52.812401 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d98ccd32-23a7-3745-8a43-73e944ab9a17 | -8.6053 | -70.201202 | 2026-08-28 01:13:00 | METOP-B | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 32e369a4-131f-3111-9df0-39b100acec5d | -14.1299 | -52.788502 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f1ac220a-2c1a-35f5-8d45-eb31367d0953 | -9.2094 | -67.767502 | 2026-08-28 01:13:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06c81cc6-d628-3054-aa20-bb35d34b2b24 | -14.1372 | -52.815201 | 2026-08-28 01:13:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8f921881-e309-376b-b949-471d5d71e5ca | -9.5448 | -66.764099 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 90cf3823-7dd6-3164-ab65-7f5de9e10dd9 | -9.2803 | -68.761002 | 2026-08-28 01:13:00 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b0a6297e-bd93-3775-af06-718f9b999eb6 | -11.1955 | -53.981899 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 567144b6-a647-36a8-9932-71dea9a2ea43 | -11.2147 | -53.976601 | 2026-08-28 01:13:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ddae63da-cbf1-3462-8fc2-53d4e49eb3c0 | -9.5432 | -66.756798 | 2026-08-28 01:13:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63b17fec-de12-35ff-a350-242531c8491f | -12.905 | -59.876598 | 2026-08-28 01:13:00 | METOP-B | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4a20f3c-f703-3fee-82e5-c1eac13f2982 | -7.25 | -45.83 | 2026-08-28 01:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24301fa6-c4f0-3e0c-992d-e8e1c209a1c4 | -7.28 | -45.88 | 2026-08-28 01:15:00 | MSG-03 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f2bf707-498e-3c5f-8a2c-ec19c7d018cb | -7.28 | -45.84 | 2026-08-28 01:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a5fd887-9672-351e-b6fc-cc33cbc44aab | -12.45 | -43.42 | 2026-08-28 01:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 560474fa-1f10-3d77-ab06-40772d7f68dc | -7.25 | -45.88 | 2026-08-28 01:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26871b3a-ede9-32e9-84c4-fd845ccb58a5 | -12.42 | -43.41 | 2026-08-28 01:15:00 | MSG-03 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8e9dd00-9e25-3f03-8ac9-e35c25b4b3dc | -11.7165 | -54.5449 | 2026-08-28 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| afd0fab0-8e38-3d84-8a5f-93bcad4a7591 | -7.2471 | -45.8685 | 2026-08-28 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 473.7 |
| 93e4b9d9-19a6-3476-88f8-71395b327e7f | -14.1645 | -52.8269 | 2026-08-28 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 394.7 |
| 79d2c436-970e-3e64-b97c-9d16058fc7b6 | -7.2659 | -45.8668 | 2026-08-28 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 623.6 |
| b5d44f9e-f36f-3c77-b92a-57f067221e42 | -14.1841 | -52.8034 | 2026-08-28 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 97d738a1-9e47-360a-b9dd-3de688384444 | -10.4081 | -61.2492 | 2026-08-28 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0946fa84-7c39-3b88-92b2-0ad6064bfb9f | -11.2317 | -53.9958 | 2026-08-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 29bfc0d6-b003-30a1-859f-4e6bcb1f644a | -10.7596 | -54.0384 | 2026-08-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c6a1219a-2b0a-3965-ac95-ad556578ffff | -8.5783 | -54.7768 | 2026-08-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 01578e38-d79b-3424-8faf-cdb4c4393bef | -11.2693 | -54.0129 | 2026-08-28 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 58715ebe-4843-34a8-ace5-aacf7faa2394 | -6.1472 | -57.7995 | 2026-08-28 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 8a59247b-77fe-36e3-b4cf-23e48c9d6c7b | -10.4981 | -64.5005 | 2026-08-28 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 80e8a16d-2691-324c-9c0f-f67f1aa38ca4 | -20.3458 | -47.5939 | 2026-08-28 01:20:00 | GOES-19 | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 181f3afa-1aec-3757-8664-197e3cf063d6 | -6.1657 | -57.7793 | 2026-08-28 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 4c422ec8-4a3f-3932-bd90-4a52319f0210 | -4.8583 | -45.3915 | 2026-08-28 01:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2fb413f5-9753-33a2-bc73-1cadd80d9dec | -12.4107 | -43.4214 | 2026-08-28 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 17c5aadb-dbda-3312-9d10-21bd5d1651e8 | -10.3895 | -61.231 | 2026-08-28 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 1808a61e-12ec-3e7c-9ba5-5b4f3817779a | -11.8239 | -47.2178 | 2026-08-28 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a5c90ddc-ca1b-3105-a353-37acb8793f3e | -16.1638 | -58.6053 | 2026-08-28 01:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 3cf916c2-2513-34dd-9cff-f134385708f0 | -15.5403 | -41.9175 | 2026-08-28 01:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| 22f853ff-d3ae-3571-8062-d369e9eaa269 | -7.2661 | -45.8443 | 2026-08-28 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 348.9 |
| b3f1be8d-a96e-3038-bf24-3ec98ecec729 | -14.1649 | -52.8058 | 2026-08-28 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 50875c21-903c-3d42-a56d-dcfa4fd73c2d | -11.2879 | -54.0317 | 2026-08-28 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| d260ccba-e81c-39d7-a309-0a62935a3cf4 | -11.7167 | -54.5244 | 2026-08-28 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 175ea93c-869a-3ac0-9d20-adec8b4780aa | -12.4498 | -43.3911 | 2026-08-28 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 92b95bd8-4736-3fc0-8229-aaacf067b6b6 | -11.269 | -54.0334 | 2026-08-28 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| f8b94674-0cd9-315c-aaa0-061d4a3964a7 | -11.2314 | -54.0164 | 2026-08-28 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6b055b4a-9499-34a2-955a-61cdea0e1f34 | -8.6156 | -54.7743 | 2026-08-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3c8b673f-d769-35bf-9d91-ca7cb815e416 | -12.4494 | -43.415 | 2026-08-28 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 52bfc7ad-dd0c-3772-a37f-dfb02bac2986 | -8.5781 | -54.797 | 2026-08-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| efb3d0b0-0c61-3fc6-b39e-ccc405c7d799 | -11.5659 | -45.5338 | 2026-08-28 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 740dfe76-445d-38a9-9c1c-9b66b1594355 | -7.2469 | -45.891 | 2026-08-28 01:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1a279ae5-0379-3402-aa4f-f650fcdae535 | -12.7603 | -44.2608 | 2026-08-28 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 75ad0a08-3820-3605-8a9b-a781185ac03f | -12.4305 | -43.3944 | 2026-08-28 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 4b1472bb-d28f-36bb-ac5d-6e5ba045aef0 | -12.4112 | -43.3976 | 2026-08-28 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7e117b30-1cfb-3242-9fe3-cbc4c8fc730d | -8.5968 | -54.7957 | 2026-08-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 204.1 |
| ba26ed7e-ecfc-3de5-b38c-31af3c0dd402 | -10.3894 | -61.2502 | 2026-08-28 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 758f463d-fda7-3a12-a272-1f214f725b48 | -6.1656 | -57.7988 | 2026-08-28 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| d1314dd5-b5e8-3192-b45a-8adf45dcaccc | -8.6154 | -54.7945 | 2026-08-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 5a2ab839-87ae-3794-b443-eca5275e5b69 | -14.1838 | -52.8245 | 2026-08-28 01:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 159.4 |
| fb8e14e6-e07c-396b-b013-5baa325ed322 | -11.8243 | -47.1954 | 2026-08-28 01:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8d74184d-7ae0-3fbd-a985-7ad2bce6beb5 | -7.2474 | -45.846 | 2026-08-28 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 266.1 |
| 4b184913-1541-37c7-8dce-6fb65321a6eb | -11.2882 | -54.0111 | 2026-08-28 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 51e04dd0-738b-3958-926a-04721b1b1a4b | -4.8397 | -45.3926 | 2026-08-28 01:20:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| d80a5748-8c4b-30fb-abe5-aa4cdfb41eeb | -12.43 | -43.4182 | 2026-08-28 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 301.5 |
| 0625ce07-ccdb-3dda-84d1-4409bb114dfd | -7.2657 | -45.8893 | 2026-08-28 01:20:00 | GOES-19 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0e30ff2d-307b-3e84-b77e-843c09f30224 | -8.5969 | -54.7755 | 2026-08-28 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 204.6 |
| a3394452-c243-32a6-b4b8-6f6313d2d7b8 | -10.4082 | -61.23 | 2026-08-28 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |


[Clique aqui para ver as próximas entradas](README7.md)
