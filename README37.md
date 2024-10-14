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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee9538b-05ad-33ec-a83d-f7eb2f27926f | -7.02253 | -43.74191 | 2024-10-14 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2fa05a8-bbc8-3910-8b0d-bc329bc55e5d | -6.23114 | -43.5147 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e207acd-7b8d-3363-81eb-500329479e69 | -6.22726 | -43.5177 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f3e3ffd-30ad-3dc5-b5f3-14a35b3a358b | -6.21485 | -43.5124 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15fdab8c-a4ba-392d-858a-dfa82753d68d | -6.2126 | -43.50487 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74b69286-9f70-3e79-a9d1-a94f5403c259 | -6.21539 | -43.50891 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8fbc2810-71cc-3681-824a-276da1275d4f | -6.21652 | -43.52358 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84b6a875-f641-322a-afcb-94a70b9c69ae | -6.56277 | -43.78968 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b9f8434c-d640-3bcb-913d-87de0a6de7bc | -6.2633 | -43.90014 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50fdea5e-0142-3084-8aff-f1aa45667174 | -6.26275 | -43.90361 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9db5a26-74f4-31af-bab9-dd9a9d70b3fb | -6.21707 | -43.52006 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16dcc5a5-e1b8-30c4-9f41-b2baeffdfb5d | -6.21597 | -43.52708 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d9e021f-ec34-3b76-a40a-f1ae97bf5c83 | -6.65468 | -43.96482 | 2024-10-14 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d12ff80-90dc-35f0-afc5-2736066f2840 | -5.30007 | -42.78549 | 2024-10-14 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b91658a-8c94-3cbb-861e-f1358608e85e | -5.29951 | -42.7891 | 2024-10-14 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 319ecf7a-7810-3a51-bf17-699a61f91c30 | -5.29613 | -42.78858 | 2024-10-14 04:19:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ebeaf40-eb81-3424-b441-cc577902b666 | -5.29305 | -43.07555 | 2024-10-14 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5d986be-80c2-3499-877c-428cedddbcea | -5.2925 | -43.07912 | 2024-10-14 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63e3ab11-53b8-3f86-ad7c-26ffe260420a | -5.28915 | -43.07859 | 2024-10-14 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2ae9d7d-a478-3c91-a375-7bd78b4b6d3b | -5.33207 | -43.93857 | 2024-10-14 04:19:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 120732c3-2ad1-3fe0-ae1d-cbdada8e72c3 | -5.29142 | -43.41211 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bddf205e-13d6-3c94-8bb6-b77e58361f31 | -5.07778 | -43.14779 | 2024-10-14 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2085437-2796-3a3e-9050-5e7854875265 | -4.42808 | -42.90573 | 2024-10-14 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 297c83f3-6d7f-3aed-b14b-037c250f3ce3 | -4.42528 | -42.90165 | 2024-10-14 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5adafc99-9a9f-397a-a9dc-2b801d7c201b | -4.04539 | -43.0461 | 2024-10-14 04:19:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37f4c79c-14d3-3333-815b-bb25f0b6b4f9 | -4.0426 | -43.04206 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2a57a2ea-e55f-3759-9774-892cbf1585a1 | -4.04205 | -43.04558 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0649d6d9-8f94-37ae-b0ba-73775e2ce272 | -4.03926 | -43.04154 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abb57263-f104-3325-9343-bdbe249d199c | -4.03817 | -43.04858 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 62294991-a98a-338f-b851-f680c6375f95 | -4.03483 | -43.04807 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b9b9c71-d8cf-3717-a50d-944a3c3422aa | -4.03368 | -43.03348 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b308906-8e02-3990-aee9-cc3c1db3c67b | -4.03313 | -43.03699 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fed9cdd7-3c12-3828-939d-606893a327ba | -5.00302 | -43.82321 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9f7f48c-4bd5-3258-b88c-b92bb9258ca8 | -6.03276 | -43.38954 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1dbce3c6-b92d-3731-b61a-bfbdbb420b9a | -6.02736 | -43.99473 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c3d3ab-4a0f-3673-94a1-cd8a2839cb51 | -5.98988 | -43.99602 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e6b375c-525b-36d6-b60e-0576d17f86c6 | -6.03066 | -43.99527 | 2024-10-14 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81687b7b-b162-3e9d-9d43-c85b0bbfa3e0 | -5.97083 | -43.90058 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a94ec83-e7b7-3557-8ce5-7f64618db23c | -5.69234 | -43.37322 | 2024-10-14 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 065b99f0-7211-3d87-b3cf-27e0261ef36b | -5.57185 | -43.27161 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09f00fe6-c39f-345a-bfe4-b93b8bbfd67f | -5.5713 | -43.27516 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa45eb6e-e763-38b2-ace9-9ea83b2c0589 | -5.56965 | -43.28578 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a66a9782-3333-3112-bc29-86f9503ba061 | -7.4356 | -42.99863 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4cf65a91-a768-3458-b80f-dba28291497d | -7.43503 | -43.00232 | 2024-10-14 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2c9248f-bbaa-346f-b8a8-d2cf7ada6e45 | -7.4629 | -35.07885 | 2024-10-14 04:19:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e0a55d95-42ba-353f-adfc-e074989b8789 | -8.12672 | -37.57886 | 2024-10-14 04:19:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3e81eee7-adf3-31e3-b9d8-021a25974493 | -8.15194 | -44.11324 | 2024-10-14 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36207a81-80e2-3bed-acbe-7de0c8e7cc66 | -8.13431 | -43.96189 | 2024-10-14 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| daffb5df-b1f0-389c-b69e-d805cb778bd9 | -8.13377 | -43.96543 | 2024-10-14 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4576630a-cfbc-33ad-948b-cef8b521bd33 | -3.91956 | -43.156 | 2024-10-14 04:19:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ab59565-9cdf-3422-962e-cab5df034403 | -3.86028 | -43.29676 | 2024-10-14 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40ed3d81-13e1-3a88-9914-8fef7ba98139 | -3.8592 | -43.3037 | 2024-10-14 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 381ec080-1789-377e-9601-a2d8a5349bfd | -6.93208 | -43.8217 | 2024-10-14 04:19:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| efdb859c-6e2a-31cd-8d2d-382d4841c81e | -6.68651 | -43.64982 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4a495c0-5984-3034-b4be-2670a565f4db | -6.68372 | -43.64577 | 2024-10-14 04:19:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9262477a-66dd-3f4f-96b6-0157050cf992 | -6.15305 | -43.88672 | 2024-10-14 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4216724d-2b7c-3fa5-883f-19f7f441da15 | -5.95812 | -43.89503 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d80f787a-ec06-3cc2-b69e-41ebcde14fba | -5.95427 | -43.89799 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac335250-11cf-3988-a4c7-9d19098fbd28 | -5.5663 | -43.28528 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02fb2d64-d774-3664-a599-7f62d8e30727 | -5.48783 | -43.11234 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47f81b04-4c13-3854-afbb-cebe72a6ed33 | -5.48728 | -43.11592 | 2024-10-14 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9fb53cd8-fae1-33e4-a188-fd4a018389e7 | -5.84537 | -43.94164 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7557878-0a37-3c02-85cd-196d204d19f0 | -5.84483 | -43.9451 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 862f834a-f5df-3e49-ba79-94281dd8ed22 | -5.72477 | -43.84052 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9d00bd3-3d5a-398c-b490-98eaeab43994 | -5.68753 | -43.75284 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 578785ee-28ea-30cf-b88d-758f36c3f9df | -5.68421 | -43.75232 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1239ab19-c8cc-30a0-8e9d-206510252623 | -5.68367 | -43.7558 | 2024-10-14 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24e2146d-aaf8-3215-a651-6b5556b29f70 | -4.14935 | -38.48346 | 2024-10-14 04:19:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aca84970-46db-3c5f-87e4-7c9ef23a1fe8 | -5.95373 | -39.67788 | 2024-10-14 04:19:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4651119e-e2a2-3225-9838-c73655df4e94 | -7.15634 | -39.30917 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 37381d72-adcb-381d-9ee9-d6f78475c4b3 | -7.81816 | -39.46709 | 2024-10-14 04:19:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 296c3a40-4211-3383-b52e-8bd58baeaf8e | -7.81763 | -39.47086 | 2024-10-14 04:19:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 99955fb5-4721-360c-843e-6fb3565d7188 | -7.71211 | -39.35201 | 2024-10-14 04:19:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 77676ced-f2c9-33a9-989a-c3314aed63cb | -7.5195 | -40.51621 | 2024-10-14 04:19:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fcaed28d-de28-3a56-9ba4-c345af3b2a8d | -7.51563 | -40.51562 | 2024-10-14 04:19:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f79d5b99-368c-378e-8f75-a3947f01442f | -7.51488 | -40.52069 | 2024-10-14 04:19:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a2b951ec-a632-394a-8722-f3c17ec638a4 | -8.51471 | -40.24084 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26d69db9-063b-3c1f-8d60-3e67cf060c5c | -8.51421 | -40.24432 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 47fd7c89-b434-31b1-a607-7350e36686b4 | -8.37768 | -40.27088 | 2024-10-14 04:19:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0ee4f03a-d9fb-39ff-8d92-b13ecc7aa1d7 | -3.01184 | -41.16535 | 2024-10-14 04:19:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| db7f1922-7323-3ccf-9759-9213d169042a | -3.01123 | -41.16931 | 2024-10-14 04:19:00 | NOAA-21 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dda429e9-7852-3de8-b972-48aef6e36d3d | -2.8243 | -40.35371 | 2024-10-14 04:19:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c77e826b-26c1-396c-b39e-6fca6b284009 | -4.74278 | -41.54998 | 2024-10-14 04:19:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c52a6869-a7b8-371a-95c2-2db9478cd623 | -4.3138 | -40.35254 | 2024-10-14 04:19:00 | NOAA-21 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8287fdc6-d9f4-3457-9673-cd368a555d27 | -4.0357 | -40.41659 | 2024-10-14 04:19:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 77eaf152-70ea-3ac6-b830-cdedd4d5e45a | -4.0161 | -40.39542 | 2024-10-14 04:19:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 808a4a4f-2cda-3891-9c43-9d7149fb18ab | -4.01238 | -40.39485 | 2024-10-14 04:19:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ce28ea6e-58dd-3dfb-b38f-b0a7902cec7f | -6.39794 | -41.71513 | 2024-10-14 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9e04004c-8ffe-3738-8d51-a0bc801d3d70 | -6.37742 | -41.59194 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a76df0ce-73f4-3c9c-89e3-f4795a761693 | -6.3768 | -41.59606 | 2024-10-14 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 016e063d-ee4c-3656-8e04-3572e0ba7a04 | -6.37492 | -41.60839 | 2024-10-14 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c97b66c3-bf82-39b1-9b07-fabc0e2818ea | -6.15429 | -41.18797 | 2024-10-14 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99842013-33dc-3043-bf86-3df0a9ec625e | -5.31236 | -41.64 | 2024-10-14 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 470a05f3-4222-39bc-ae0d-2162adff7c30 | -5.31195 | -41.6428 | 2024-10-14 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55e9cb90-6c25-387a-a7d6-c06cb792cad8 | -5.31174 | -41.64399 | 2024-10-14 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54ed6566-11b9-3d9c-ae59-683dcffed22f | -5.30841 | -41.64224 | 2024-10-14 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c3f484c9-9627-34ea-b85b-e77082516896 | -5.30821 | -41.64344 | 2024-10-14 04:19:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43482476-a822-30fc-81af-dc1dbc1be158 | -5.1884 | -41.28648 | 2024-10-14 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d97ecc6-c549-3c43-a454-b81d2dea5a4c | -5.12841 | -41.70646 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 41c250b4-2c35-390a-adb6-9575a415225d | -5.12781 | -41.71041 | 2024-10-14 04:19:00 | NOAA-21 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README38.md)
