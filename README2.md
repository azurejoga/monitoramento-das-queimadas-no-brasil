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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7aa46a58-0104-3584-9388-4ea1cd7a1482 | -11.5499 | -52.7867 | 2026-06-16 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 82a05410-4197-33ae-94c0-b57204c0c46e | -8.9449 | -46.9582 | 2026-06-16 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.8 |
| 6105e4c5-14f3-326d-84f6-1f0ae2ce3cc1 | -8.9452 | -46.936 | 2026-06-16 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| ee973660-1f7f-3cdf-a592-a1dca4e759e8 | -9.3423 | -45.4765 | 2026-06-16 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 91e82770-a3c5-3ba5-aedb-2de6d3e83013 | -8.9449 | -46.9582 | 2026-06-16 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 0dfdcfca-8867-3c2e-913a-4e471e1695b2 | -11.5502 | -52.7659 | 2026-06-16 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d66a177a-7620-38ce-8f6a-ce92b1892d42 | -8.9638 | -46.9563 | 2026-06-16 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| a45c0de6-28c5-3148-84ff-4c3ddbe27c9d | -9.3423 | -45.4765 | 2026-06-16 01:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7875ab36-d3f2-39f0-bbd8-82a923babd5a | -11.5499 | -52.7867 | 2026-06-16 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 590bc3f9-a557-3d31-b631-4daaf33acc1d | -6.1379 | -48.5285 | 2026-06-16 01:00:00 | GOES-19 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9824396d-ec65-33c4-b6b3-8e16122b2c1c | -10.71448 | -56.25555 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| d9d234e3-09ce-3291-9942-baf825929d34 | -10.71282 | -56.26139 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f89c56fb-fbc5-3b12-8595-4e8f19864f7f | -10.15073 | -56.6001 | 2026-06-16 01:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 6cd98245-60e0-3b44-8b97-92d356ad97d3 | -11.79043 | -56.98808 | 2026-06-16 01:05:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| e57be2be-183e-3ef1-b1e1-334fab645ff2 | -12.80332 | -54.8665 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 699b9202-8583-3878-9d9e-4147cd6a9b5c | -11.48564 | -57.10539 | 2026-06-16 01:05:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e5f91dc7-3878-3ec4-a9f1-d0947075d443 | -15.06828 | -55.81662 | 2026-06-16 01:05:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e1dbfc96-14bb-31a8-a483-fa29b47d04bb | -11.58955 | -55.339 | 2026-06-16 01:05:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| f3736a5d-1a8f-3031-aacb-72584e8beb3b | -11.59296 | -55.34479 | 2026-06-16 01:05:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| e795e3d9-7e80-3b3e-96a1-44350567e28f | -11.53766 | -52.76146 | 2026-06-16 01:05:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 85502d30-93dc-3fb7-8913-47cd07596ea2 | -11.79293 | -57.00391 | 2026-06-16 01:05:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.5 |
| adb2ad38-1764-3625-b92b-db764da1c071 | -11.90449 | -57.78743 | 2026-06-16 01:05:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3e90a397-73d6-31ea-86d1-3bfb2865cdf4 | -11.53502 | -52.79012 | 2026-06-16 01:05:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 135c9cc9-3abe-30cc-9430-1e398f5bea53 | -11.47927 | -57.12895 | 2026-06-16 01:05:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8b0b1250-4d65-32a3-9faa-a6c0830439be | -10.70994 | -56.24294 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| ce8c2d9b-199b-33a3-bf18-b6a165922aba | -11.55106 | -52.78744 | 2026-06-16 01:05:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 139.0 |
| df80e190-ffd9-3a2a-8cd4-67d2b90757bc | -11.48815 | -57.12096 | 2026-06-16 01:05:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 6741e756-dae0-32fa-a517-ec310913a5fa | -10.15357 | -56.61796 | 2026-06-16 01:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 32b02811-9cc1-30d0-b054-d1ff57b1563b | -11.47686 | -57.11337 | 2026-06-16 01:05:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6fef5989-ceb6-3d73-b581-8b29dbd0a122 | -12.7984 | -54.86097 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d588900e-4c94-3881-a7f3-bb98bd6496f3 | -11.54339 | -52.7955 | 2026-06-16 01:05:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 956b5143-37f2-3550-8111-b7e3b73e4d85 | -15.07447 | -55.82172 | 2026-06-16 01:05:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 549cb47a-d7c0-3d5c-aad1-4c7327553619 | -14.10546 | -59.45776 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c513509d-f402-3faf-8822-86b855a3d2d9 | -14.0961 | -59.45926 | 2026-06-16 01:05:00 | TERRA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cec3f8a2-21b7-3cee-93a2-eba67c87bce7 | -11.90787 | -55.91545 | 2026-06-16 01:05:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9553d73a-ac41-32bd-bafb-261350bf26fd | -11.5499 | -52.7867 | 2026-06-16 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c22daf98-6d45-3acf-862c-e5e3307756ea | -11.5502 | -52.7659 | 2026-06-16 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 2fde93d7-4eab-3cde-b72e-5ec1fb8cd14f | -8.9449 | -46.9582 | 2026-06-16 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 138.3 |
| d9179f5f-cb87-343a-8eb2-d4647d095911 | -9.3423 | -45.4765 | 2026-06-16 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| eb2858b3-0b45-359f-b947-394d86948a02 | -8.9446 | -46.9805 | 2026-06-16 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| acc1f719-cbc2-382b-8d75-753d2cabe169 | -12.8548 | -44.3625 | 2026-06-16 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| bd32e627-29ab-35e4-a719-4ccd329a73c8 | -11.5499 | -52.7867 | 2026-06-16 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 76922368-3c50-30cc-8969-a716bf67c38d | -9.3423 | -45.4765 | 2026-06-16 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 59b0b5a7-2188-304e-af36-b8d78ef48f19 | -11.5502 | -52.7659 | 2026-06-16 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 28b3bb36-73a9-33ef-8d78-45a44ff1fcfd | -8.9449 | -46.9582 | 2026-06-16 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 1a71a395-039d-323e-a497-25dda4b64468 | -11.784 | -56.9781 | 2026-06-16 01:20:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 16529580-0af5-3919-a604-50b56315110f | -11.4751 | -57.1012 | 2026-06-16 01:20:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b49ad2e2-7b1b-30f8-b144-ee5a1865ced4 | -14.0976 | -59.449799 | 2026-06-16 01:20:00 | METOP-B | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1db6c8de-00f2-39ff-b1a6-1aaff608ed67 | -10.139 | -56.597599 | 2026-06-16 01:20:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 099ccddb-7e77-3d4b-982c-e4add770f7ad | -11.7889 | -56.997002 | 2026-06-16 01:20:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ecbdba9-cf9b-367d-ad02-1b2163674bc7 | -10.1487 | -56.5951 | 2026-06-16 01:20:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fdb8d26-aea8-3f0e-b463-e587691c3e8c | -11.4703 | -57.082298 | 2026-06-16 01:20:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa7a517b-1eac-352a-a84a-d537f129970c | -10.1431 | -56.573601 | 2026-06-16 01:20:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca1716ad-7615-339c-8ab0-31ca0c954f6e | -9.3423 | -45.4765 | 2026-06-16 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 93837143-a308-346d-af4d-da50613b69a9 | -8.9449 | -46.9582 | 2026-06-16 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c27b8a83-5a40-3eee-825d-f0c3b0868d9d | -11.5499 | -52.7867 | 2026-06-16 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 757c6d3f-dd07-3cac-9af2-193fb2a5b9b0 | -11.5502 | -52.7659 | 2026-06-16 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 6b1bc439-9be5-3f8e-8893-2035abdf3bb7 | -8.9446 | -46.9805 | 2026-06-16 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 12c5351b-62b8-3654-a312-fde4890bd825 | -9.3423 | -45.4765 | 2026-06-16 01:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 5361a277-4c42-3f62-a913-c99d1f78bb00 | -11.5499 | -52.7867 | 2026-06-16 01:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 74f3bf14-6618-3ac2-87b4-459faf2d3225 | -8.9449 | -46.9582 | 2026-06-16 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 198.1 |
| ce32d9df-b471-39ac-8653-86afce7ef1de | -14.1034 | -59.453999 | 2026-06-16 01:46:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce252772-273b-3a7a-ab1f-cae732bf2e92 | -11.4839 | -57.093498 | 2026-06-16 01:46:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45828b7c-6747-314e-818d-58f5b49a39a1 | -14.1132 | -59.4515 | 2026-06-16 01:46:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ab0ff669-eb2f-390b-a8ae-5da230dfac74 | -10.7181 | -56.242298 | 2026-06-16 01:46:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae474792-e787-31ab-9cdc-d42a5ed53fa0 | -14.1009 | -59.443802 | 2026-06-16 01:46:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3faf8520-c30e-39dc-903d-a651124a2edd | -11.4782 | -57.111698 | 2026-06-16 01:46:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdba4e1-ac51-3917-b2d5-324c7077bb18 | -10.1561 | -56.583099 | 2026-06-16 01:46:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93f2e758-54a3-3122-b747-8c3c6542c166 | -11.5437 | -52.764 | 2026-06-16 01:46:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd720f1-8b9e-3dce-bae5-d12212d4cbdb | -10.151 | -56.6035 | 2026-06-16 01:46:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4e7ef7-815b-3eb4-8e56-6d2c36f8ec5d | -11.7993 | -56.9939 | 2026-06-16 01:46:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06b07562-94c6-3309-a660-3da05a193c1d | -11.4879 | -57.1092 | 2026-06-16 01:46:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 798b554c-822b-37dd-974c-a1417bb95ebb | -11.7897 | -56.996498 | 2026-06-16 01:46:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27ddce36-5ece-3ce9-b1df-63a540da5ea7 | -10.1464 | -56.585602 | 2026-06-16 01:46:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9f1325-ab0d-3fc0-bbe7-709a16059853 | -11.7953 | -56.978199 | 2026-06-16 01:46:00 | METOP-C | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c370c70a-634d-3f9e-ae3a-f50c6db339e7 | -11.5532 | -52.761299 | 2026-06-16 01:46:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a391cb13-8720-340e-8d18-298460931a16 | -10.1607 | -56.601002 | 2026-06-16 01:46:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38fdacb0-cde3-3337-832f-f10cc5a931a1 | -9.3423 | -45.4765 | 2026-06-16 01:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 5c9e68f9-0ea0-3dc8-bb07-eeac29b215dd | -12.8548 | -44.3625 | 2026-06-16 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 7990951a-95a7-3719-b703-fda32763d0ee | -8.9449 | -46.9582 | 2026-06-16 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 56ee7a88-4b7e-3f4b-b983-168e4b56b91e | -8.9261 | -46.9602 | 2026-06-16 01:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 91397525-161c-3580-9075-fd03e07dc907 | -11.5499 | -52.7867 | 2026-06-16 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 44b70c12-cc9b-3dbb-9afd-4c6d7f832589 | -8.9261 | -46.9602 | 2026-06-16 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 7079284d-244d-31b4-9f1b-f8077593ef74 | -12.8548 | -44.3625 | 2026-06-16 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9669d49e-cff3-3682-bf80-4af08695ca23 | -9.3423 | -45.4765 | 2026-06-16 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e4048075-e7c7-3243-89ae-b0d10b3db195 | -8.9446 | -46.9805 | 2026-06-16 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d4f0ac62-cd39-31b9-95a7-26e3ac391e2d | -8.9449 | -46.9582 | 2026-06-16 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 181.4 |
| 5bd36385-8ca4-3a20-a1cf-87a5198015c8 | -8.9258 | -46.9824 | 2026-06-16 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 510359a8-37a3-3041-b851-b2d96512d5d7 | -8.9449 | -46.9582 | 2026-06-16 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8889f0d8-e3b0-33d2-a6f3-291acf1a736d | -9.3423 | -45.4765 | 2026-06-16 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 52ed574d-7463-3b4b-8c97-7deab482faaa | -8.9261 | -46.9602 | 2026-06-16 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 7212de49-2ed2-370a-a98e-4e6454a4abf8 | -12.8548 | -44.3625 | 2026-06-16 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| fa19dd19-c2b8-3154-82ca-8c9514b76984 | -9.3423 | -45.4765 | 2026-06-16 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 148c1c17-49d6-37fc-a509-a1611b1be55b | -8.9449 | -46.9582 | 2026-06-16 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 743330a1-59be-3e0c-8ef0-d228633ca92c | -9.3234 | -45.4787 | 2026-06-16 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b61950ff-a3ba-3687-a8cf-1bfb106f78b8 | -11.5499 | -52.7867 | 2026-06-16 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b374c3f0-3502-384b-88c2-113a77a47457 | -9.3234 | -45.4787 | 2026-06-16 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 6f1aba96-33fc-3e72-b720-ae0163d88eeb | -8.9449 | -46.9582 | 2026-06-16 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 00dabbfe-0e71-3bd4-96ce-bc2b778f3b4d | -9.3423 | -45.4765 | 2026-06-16 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| fb7563c9-9f6c-30ce-b2a7-c7c83e2ad0a4 | -9.3234 | -45.4787 | 2026-06-16 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |


[Clique aqui para ver as próximas entradas](README3.md)
