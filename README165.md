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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a78ea5d5-b472-3f17-bbd4-d3e114372fb9 | -6.7168 | -44.5758 | 2025-10-01 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 120.1 |
| b6a96fbb-4cfc-3530-841d-7f01bca382a7 | -8.5079 | -47.2897 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 186fb0eb-f0be-3695-8b0f-c97ba98ec5e9 | -8.3867 | -48.0042 | 2025-10-01 14:40:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3fd84364-8242-3043-a084-00e95417c809 | -14.8021 | -45.7946 | 2025-10-01 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 15239e7c-ae9d-3054-ac25-008e7d0301ad | -9.4455 | -47.6144 | 2025-10-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| d61287e9-ed40-394f-9b85-d2ce98f50650 | -6.0625 | -42.4422 | 2025-10-01 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 309.9 |
| 3c05e0db-f574-3dac-8d22-b56fbf547362 | -6.2813 | -45.022 | 2025-10-01 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| dd9fab1e-1ee2-3554-8af9-b505d441c426 | -5.2903 | -42.7624 | 2025-10-01 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| c041c262-1840-3a94-bbd0-3cc91bda7320 | -12.877 | -45.1974 | 2025-10-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 3dbf60a7-8872-3b14-a262-928085701b98 | -11.9431 | -50.5058 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 7baaea26-8c42-3411-bbbc-ab302369ffbd | -9.4005 | -54.7186 | 2025-10-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fae0326d-e91c-3550-a3a5-f41f2c84eaae | -14.1727 | -46.1354 | 2025-10-01 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| e7c59a90-53e1-3eb9-94f1-451e450b5a96 | -5.6412 | -45.4989 | 2025-10-01 14:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 834a3bc7-acfe-3404-b95f-493cb0263b7b | -6.7165 | -44.5987 | 2025-10-01 14:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 1b49c45b-2040-363b-b731-ed5ccf9482f5 | -5.325 | -43.0884 | 2025-10-01 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 0d12de41-5314-354f-a5fe-cc3e0b3aefef | -12.788 | -46.8566 | 2025-10-01 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 76cd8e22-d670-316b-b5d6-a133ca806510 | -10.9182 | -44.3092 | 2025-10-01 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| dfe85af3-6a52-3e27-9071-5c856ec587f4 | -8.5587 | -44.7414 | 2025-10-01 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 0277ff7e-2847-3b91-a2d3-56a94fb33dbe | -9.1434 | -47.6457 | 2025-10-01 14:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 55e579c7-e635-32e1-856b-13715b25e2cb | -12.7819 | -50.5543 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 248.3 |
| 59cfdece-fd82-3097-b757-0f1d77948abe | -9.9581 | -43.5987 | 2025-10-01 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 9bd9df00-b79b-3818-8e06-d6c6918d6ffa | -8.6908 | -47.7126 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| dc5ccfe3-370f-304d-b3cb-578b5c987847 | -8.5016 | -47.8184 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 379e8aa4-da04-313d-8638-5292d46da254 | -9.4115 | -47.3308 | 2025-10-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 02de0b6d-d6a4-3cf2-b371-c9c857417024 | -7.4659 | -46.4537 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 96529e60-e8d1-3362-92b3-64eedec45c59 | -9.8842 | -45.9802 | 2025-10-01 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| b23def7a-ecf7-35d5-b02b-d3a26d0db83c | -7.4761 | -47.2508 | 2025-10-01 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 44434fc2-7a6c-31a1-b2a9-bf59819191c4 | -5.338 | -43.7623 | 2025-10-01 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 2cf6878c-d416-3617-b033-ace95b8815b9 | -6.3 | -45.0205 | 2025-10-01 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| ecf8b8d4-2eff-3a17-8417-95533c25e6a9 | -6.544 | -44.9783 | 2025-10-01 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 634834d1-dbd5-3440-837f-b9af9ef3456f | -5.3276 | -42.7832 | 2025-10-01 14:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 164.5 |
| 0e030ec5-94b9-35f3-84d1-b70a690ee5c3 | -4.1386 | -44.2965 | 2025-10-01 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| e2d95401-4437-395c-bf1a-10f210e68976 | -8.4833 | -47.7763 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 92ea0599-64dd-3c30-a26e-8933d8e89334 | -6.7624 | -45.617 | 2025-10-01 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| c583d23c-cca6-3c71-ab82-52a6d02119cb | -6.0999 | -42.4628 | 2025-10-01 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| fec04d17-cfa8-3d58-a10a-911210149492 | -6.6978 | -42.8118 | 2025-10-01 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 900b2655-b789-30a3-bc7f-40f72e8a748d | -10.8433 | -45.3815 | 2025-10-01 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 99b38567-519a-39d7-9995-84921d8e9fb1 | -13.3274 | -47.8536 | 2025-10-01 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.6 |
| e3610339-2854-3180-95db-c6f9c9bff9cc | -14.3519 | -45.9206 | 2025-10-01 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 8e763aed-cebf-33b4-b297-a462b32dc9ca | -4.1379 | -44.4109 | 2025-10-01 14:40:00 | GOES-19 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 08c59c0c-2fc0-3cfe-9c5d-0b5256b677b4 | -11.7729 | -46.8435 | 2025-10-01 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| c656c8f6-9bd2-3942-a40b-33b2a24cddc8 | -8.8609 | -47.6521 | 2025-10-01 14:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ce2b6b0e-8448-31fe-966c-faae10bb96ad | -12.7822 | -50.5328 | 2025-10-01 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| aeb95a6c-3080-3bdc-b321-966ea731cc00 | -12.8963 | -45.1943 | 2025-10-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 865ebbc1-e48a-3182-9ebf-cdbec723b099 | -4.098 | -44.823 | 2025-10-01 14:40:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 4b42cff7-d2e4-35b1-9167-d64c349d07b6 | -5.3248 | -43.1118 | 2025-10-01 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 3b35a0d9-b530-3c69-b300-95473cbab3c7 | -11.6126 | -45.0443 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 0321e5ef-9e11-3927-a73b-6ba7f9550d74 | -8.9115 | -46.6276 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| f4d31c2a-53dc-3418-a99b-151e0e7eecb4 | -5.4967 | -42.7471 | 2025-10-01 14:40:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 6cdc9f95-d1d7-3ce3-b3f7-3c64bf685b7b | -9.9585 | -43.5752 | 2025-10-01 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b08a5062-f20f-36e9-a299-857787e89bc1 | -8.4827 | -47.8202 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5c9f6e46-ce12-38b2-b2e6-622360eeb61c | -8.2105 | -47.0084 | 2025-10-01 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 8bebee09-d089-324c-9378-20f7dcb5f5b1 | -8.2102 | -47.0305 | 2025-10-01 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| eeb8a4ba-863e-3f49-8cf7-bdb3ed48e217 | -13.6703 | -48.07 | 2025-10-01 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 90.5 |
| f7b6db10-fe0f-3bc9-a9e3-05e28b9e369e | -6.214 | -44.2272 | 2025-10-01 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 8285b000-8334-3ecb-9c6b-ccdd7e9ccc2f | -9.4458 | -47.5923 | 2025-10-01 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| e1e9dceb-575e-3d6d-ae8b-d71f1e6e0553 | -7.4226 | -46.9904 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| a3214df7-9290-32c8-99c8-b7161a525038 | -9.1889 | -48.5166 | 2025-10-01 14:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| f3f2b7df-3d0f-3789-a187-96a48015e11a | -12.8967 | -45.1711 | 2025-10-01 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.2 |
| 1b66458f-8071-3be0-a853-14c25787c51f | -9.4194 | -54.697 | 2025-10-01 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 4fb11c82-ad20-395d-a67c-17792328ea50 | -8.5267 | -47.2879 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1aa90863-0e64-3e0c-bc7c-3d7ff41c9b0a | -8.8923 | -46.6519 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 71903b8b-80e2-3a8f-bf68-d9dff265874e | -3.8885 | -42.5211 | 2025-10-01 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 99.9 |
| 88dbec20-0efd-36a8-8789-8f891efe04d6 | -5.4156 | -41.3233 | 2025-10-01 14:40:00 | GOES-19 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 2a1fa490-3ed0-33cc-971b-a7496c2a0f5c | -8.874 | -46.6092 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8d991794-f85f-3cda-a5af-b316da4fde65 | -11.8246 | -44.9669 | 2025-10-01 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.0 |
| fc34df71-0077-3b8b-9cb7-92bd32407671 | -5.6461 | -44.933 | 2025-10-01 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 26102acb-fe32-359a-988f-a857fd366006 | -9.0405 | -49.9101 | 2025-10-01 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 15f9c1ef-c62f-3970-869e-009aeec81191 | -5.17 | -43.7276 | 2025-10-01 14:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 5f7b3000-d225-3b76-8750-0efbaf47a503 | -7.8165 | -46.9781 | 2025-10-01 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| dc91a3ed-bfd6-31f7-8aa7-428ae9cc8411 | -8.5773 | -44.7623 | 2025-10-01 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 837ebae5-3dab-3a7b-bb86-fa07f158b2a8 | -11.1178 | -49.7845 | 2025-10-01 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 7da784ce-1031-316a-8fb5-8c2d109c5772 | -10.5094 | -47.2956 | 2025-10-01 14:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 6c3df653-3a1c-3d44-8b44-5f03a3eaf9b8 | -11.9272 | -47.8941 | 2025-10-01 14:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 289f498f-c67c-39b9-815f-5c33774c2b3d | -8.672 | -47.7144 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f9b72857-ce46-387b-a5c5-ec41e1c81ead | -4.1388 | -44.2736 | 2025-10-01 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 8609de08-9584-3eac-bd86-7cef27478691 | -7.8735 | -45.2911 | 2025-10-01 14:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| f16dcd67-0603-3f95-844b-a46a43426044 | -6.079 | -42.6773 | 2025-10-01 14:40:00 | GOES-19 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 73d28b61-9413-3a9c-aebf-36f7f73b7252 | -14.1732 | -46.1124 | 2025-10-01 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 541ac76b-789c-3e79-99a9-1ba7c8761f93 | -10.2707 | -48.0746 | 2025-10-01 14:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 79667fb9-7cde-37bb-8786-c63aac8e6580 | -8.483 | -47.7983 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| a0479a08-827b-3dac-9b08-43b738689324 | -8.8743 | -46.5868 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| bca2682c-d1d7-3399-8c16-ffbd22d14680 | -12.282 | -44.1039 | 2025-10-01 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 83704ced-c9d9-3fff-b39b-914b3a684b15 | -13.5506 | -47.2595 | 2025-10-01 14:40:00 | GOES-19 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e473badf-3732-3ddf-80b6-47cafe5b0568 | -9.0219 | -49.8904 | 2025-10-01 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 6f6e5dfd-9255-39f5-a485-e1dc5fdb3c47 | -11.1181 | -49.7629 | 2025-10-01 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 7dce48c6-7980-3bf8-b67f-fb65f9e1e271 | -8.8926 | -46.6296 | 2025-10-01 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2d85d7cd-bc53-3343-9933-6e612bc2133f | -9.0407 | -49.8887 | 2025-10-01 14:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 219b8275-b088-3784-b698-984c3e7640e6 | -8.6911 | -47.6906 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| b9f74c26-82e4-37ac-b965-8087c00b94f1 | -15.5379 | -45.2375 | 2025-10-01 14:40:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 390b85d5-e5e0-39c1-93d7-9961bab36a92 | -6.1166 | -42.6742 | 2025-10-01 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 79ca80e6-c251-3827-82e5-d59aaefc34a9 | -9.8049 | -48.9756 | 2025-10-01 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 5606daa8-22ea-33ac-9007-c7d5832115b0 | -5.3195 | -43.7405 | 2025-10-01 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| e5da9528-1327-3367-af7c-d1d58e85eb9f | -14.3714 | -45.9172 | 2025-10-01 14:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| a419d20b-c64f-3be7-b2da-bc069121b6b3 | -7.8353 | -46.9764 | 2025-10-01 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 230bc76a-8075-3798-932c-a71b25ebdd51 | -9.4196 | -54.6767 | 2025-10-01 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 0cbf7237-6d5b-354f-be17-aae3370306ba | -8.5081 | -47.2676 | 2025-10-01 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d0850c0c-62b1-3967-9f6e-4bce3cf6da95 | -5.0449 | -42.991 | 2025-10-01 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cf1e6d94-9e2e-367c-82d0-8546c50f65ec | -10.8995 | -44.2886 | 2025-10-01 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| dc8280ff-b4c8-3694-9af1-09fd4e56d700 | -12.2816 | -44.1275 | 2025-10-01 14:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |


