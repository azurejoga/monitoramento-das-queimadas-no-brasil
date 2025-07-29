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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29016460-3332-3f2a-997b-24ee546343e1 | -6.9456 | -44.2342 | 2025-07-29 13:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 270f7df1-05d3-3fa4-94ba-cb530d4e1c56 | -6.9456 | -44.2342 | 2025-07-29 13:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 81a27b4b-37dd-3d6b-8f03-f45cc0f85f15 | -12.0001 | -46.9696 | 2025-07-29 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d5eb0133-707f-35bd-a554-5b406cb42078 | -6.9456 | -44.2342 | 2025-07-29 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 2e8f3217-7bfd-3fc0-b2eb-c0e13f069213 | -12.0005 | -46.9471 | 2025-07-29 13:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 787f492b-f7a1-328c-969e-e244ec56c5c9 | -6.7992 | -43.8776 | 2025-07-29 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| f133400c-370d-3e71-970b-74ed0b35f256 | -7.6128 | -45.066 | 2025-07-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 79b040c9-2176-31d6-a41a-29e98f1d07ff | -12.0005 | -46.9471 | 2025-07-29 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 5bb0701d-2db5-39bd-8272-794e11e98724 | -12.0196 | -46.9444 | 2025-07-29 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 19c851a0-c9d1-31f9-b706-a0db0704a959 | -11.3708 | -50.6565 | 2025-07-29 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 3eddb954-9c93-3537-84fa-d4c4c9d364e7 | -6.9456 | -44.2342 | 2025-07-29 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 70e5ee02-c112-36b9-aa78-0b6f56b0908f | -7.7834 | -44.9584 | 2025-07-29 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 127.6 |
| f34adcd5-3d82-324c-bf8c-a2d9d3231e8c | -2.9373 | -42.2354 | 2025-07-29 14:00:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 786304d4-ccb7-360c-ace1-4a3b3f0565a2 | -6.0343 | -47.5579 | 2025-07-29 14:00:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 3dccefd5-5c6a-3c30-b32e-7ebfb5f7fca9 | -11.3708 | -50.6565 | 2025-07-29 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 509bd95f-7fc5-3199-aa9e-2dd83f0a58d2 | -7.6128 | -45.066 | 2025-07-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| d7e267b3-2680-3f0b-9b12-f81d27bb7559 | -6.9456 | -44.2342 | 2025-07-29 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 1b1b0401-aa83-37d8-8e59-04db226767a2 | -7.6317 | -45.0642 | 2025-07-29 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 23f9caed-a799-3fde-a5ad-d89d2f053031 | -12.0001 | -46.9696 | 2025-07-29 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 62172ce7-3fc3-3efc-b379-9e1105d33019 | -12.0196 | -46.9444 | 2025-07-29 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 828baecd-b457-377d-9212-23f9b7822948 | -6.7992 | -43.8776 | 2025-07-29 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 997f37a1-5dfe-30b8-a5ab-c9cb45acec9f | -6.7992 | -43.8776 | 2025-07-29 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 13f24ef4-7cdc-32f1-9e9c-d42ee7c3fae4 | -11.3708 | -50.6565 | 2025-07-29 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 176.6 |
| a65c8251-f924-3f54-979e-685bdb67969a | -13.5247 | -45.6231 | 2025-07-29 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 70b1670b-2198-3db3-aaba-b4639b2f4875 | -12.0196 | -46.9444 | 2025-07-29 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| bfe17a78-ca2a-3c70-b0cc-d91ccf3fb586 | -13.5053 | -45.6263 | 2025-07-29 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| febaefe7-8ba4-3a8d-9cf9-df1366f37ab2 | -12.0005 | -46.9471 | 2025-07-29 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| bf1b2768-36a3-3f5b-8842-93eb102cdf21 | -6.9456 | -44.2342 | 2025-07-29 14:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 70ae067a-e52a-349b-8fbc-17b33be65401 | -12.0001 | -46.9696 | 2025-07-29 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| bda744be-99f9-36fe-bd98-95e77ed4b81b | -6.5033 | -45.2992 | 2025-07-29 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 734fa9b4-4671-364d-adde-4728bda139c6 | -11.3708 | -50.6565 | 2025-07-29 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 7b3e38d3-8a6d-384f-af2c-4390956b6b12 | -6.3975 | -53.3495 | 2025-07-29 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 8bfae323-c874-32e9-8e96-9b7571b4a356 | -6.7992 | -43.8776 | 2025-07-29 14:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 98894323-f2b6-3514-90a7-2905c02ba1ea | -6.9644 | -44.2325 | 2025-07-29 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d748cb3a-d4d7-3193-9aea-6e0033a48445 | -6.2458 | -44.82 | 2025-07-29 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b96b73eb-c542-3138-b5f2-f4d73c22d6ac | -5.0577 | -43.7352 | 2025-07-29 14:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 07461135-d63e-38fc-8345-a7f57c536ba3 | -13.5053 | -45.6263 | 2025-07-29 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| e931a33c-2b76-34f3-ac2f-7db7529bedb8 | -13.5053 | -45.6263 | 2025-07-29 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 401.5 |
| 49f55ea6-1952-3124-9778-e6774623de72 | -6.3791 | -53.3301 | 2025-07-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| d84f841f-b4d6-3873-9b03-dd3685a099f8 | -6.3975 | -53.3495 | 2025-07-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 67accb0e-e306-3277-86e5-f2fba32ed389 | -11.3708 | -50.6565 | 2025-07-29 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| eb8a9a37-7228-3a75-9e1b-5159fdf8e3b3 | -12.0001 | -46.9696 | 2025-07-29 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| 00077908-1775-357c-ae8f-f7946c116575 | -6.3789 | -53.3505 | 2025-07-29 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 529e0675-147f-387d-add8-ce1709ee929b | -12.4431 | -44.7328 | 2025-07-29 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 0fd1cbb9-8c55-3aa9-8ffd-8cea9758d478 | -7.545 | -44.4316 | 2025-07-29 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f4558d53-2ef2-3496-a9f4-f24d5c459902 | -13.5252 | -45.5999 | 2025-07-29 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 80b015b7-d80e-3f65-b2ec-f4be5105a2b2 | -13.5247 | -45.6231 | 2025-07-29 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 379.9 |
| 449fcaca-5ef3-3cf1-8bcc-aed93d919e94 | -6.7992 | -43.8776 | 2025-07-29 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 287.9 |
| 56d5b154-beef-3fb2-b1e4-e3d601d3a399 | -6.526 | -56.1923 | 2025-07-29 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8e734786-b54d-332c-9f86-f45b0bca1cbe | -6.3789 | -53.3505 | 2025-07-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| ce6a7f94-ce38-30dd-97f4-e91ce0b51428 | -6.3976 | -53.3291 | 2025-07-29 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 1b87b1e1-9193-38a2-aa89-fbc6a9c7229b | -7.3121 | -43.411 | 2025-07-29 14:40:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 804f9dbe-e63e-3980-aaeb-576e3f8841dc | -13.5053 | -45.6263 | 2025-07-29 14:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 160.9 |


