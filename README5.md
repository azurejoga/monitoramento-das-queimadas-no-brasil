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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ccb0a6a-3b97-3a8a-99d9-d1a531b50647 | -8.7341 | -62.40623 | 2026-09-09 00:43:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5898e784-e3aa-354b-8077-6eea012ec8ea | -6.76424 | -58.96469 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 6cd811f5-c7f1-3d5a-990d-b2f569086369 | -9.09493 | -65.71142 | 2026-09-09 00:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7eed22db-c40e-342c-ab48-2f0c8de6cf1c | -6.7872 | -58.93351 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 710ec677-07ad-37d4-bfdd-84aed8902e0b | -9.00825 | -65.42257 | 2026-09-09 00:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 94e9b8cb-edb5-34e2-9108-4b3cf52751c3 | -5.2917 | -60.1191 | 2026-09-09 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2883f827-24a2-3a13-a10b-d3c80c08252f | -10.75346 | -60.70748 | 2026-09-09 00:43:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6e0b0d3-1cd6-343d-9d15-75f1a829d575 | -5.44878 | -60.24591 | 2026-09-09 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8dd02ac3-d4ff-3481-9ad5-6f6e82e77f75 | -4.57651 | -56.24974 | 2026-09-09 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 71a84dd5-921e-39e8-aee9-0449ecd94208 | -2.80457 | -54.76644 | 2026-09-09 00:45:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 95eefe1f-a7da-3bce-be36-a5e4b68928d3 | -4.29394 | -59.96154 | 2026-09-09 00:45:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| be8a5685-8436-378e-a6fb-e64f89c35784 | -3.4399 | -59.26177 | 2026-09-09 00:45:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 40587475-a566-3e91-b6c6-15e990f87ed2 | -3.19686 | -61.23785 | 2026-09-09 00:45:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a27f204c-37ac-315f-a665-835c4da42142 | -3.15379 | -60.66369 | 2026-09-09 00:45:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f28bb4af-6b17-33aa-837b-32b726561362 | -2.94438 | -50.50263 | 2026-09-09 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0599ed61-e5a3-3c8f-90b4-53d52150a409 | -3.81316 | -55.88927 | 2026-09-09 00:45:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 830280d5-4b00-3694-8ee0-1f64e240e5b5 | -3.74577 | -55.98008 | 2026-09-09 00:45:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9c70f021-0d05-32ca-8c3a-2666b5a529b1 | -3.82751 | -59.39872 | 2026-09-09 00:45:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d408afb1-5a81-3747-b241-db43f1b559a3 | -3.82877 | -59.40787 | 2026-09-09 00:45:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| cbc9ab3a-38d3-372a-aa5b-7194431ff60c | -1.31042 | -54.66967 | 2026-09-09 00:45:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 2c05cd61-f14a-3dd2-8680-29bb54e6f0c1 | -3.76891 | -58.84809 | 2026-09-09 00:45:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4ed7b641-b902-33bb-adc5-c8ef0ad62524 | -2.93723 | -50.467 | 2026-09-09 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| fe6c1f35-234e-3a2f-a7c9-a86919a51260 | -1.32199 | -54.66265 | 2026-09-09 00:45:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 28f0220e-d967-3a8a-a304-9fae150c3dd1 | -3.14019 | -60.62992 | 2026-09-09 00:45:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 4c84af6d-ffa9-3161-a360-57598f1449df | -1.30764 | -54.64977 | 2026-09-09 00:45:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 77032fb0-534f-3828-a1b5-f7c88ac88af3 | -3.85314 | -54.30356 | 2026-09-09 00:45:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| fe07d6d9-e04d-33ce-853d-b71dc8e0016a | -3.39063 | -61.30652 | 2026-09-09 00:45:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6041f6d-b585-36ff-935e-c70290dbfab0 | -3.37805 | -59.41192 | 2026-09-09 00:45:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 40611101-e930-313c-bf06-1b16ddcee5b2 | -2.74396 | -60.23515 | 2026-09-09 00:45:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7cc03127-39ee-3623-b50f-9aabee58ccd2 | -3.67906 | -58.52871 | 2026-09-09 00:45:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d9546e27-5b1c-3d1e-bbe7-7493d9222a5e | -2.93821 | -50.46197 | 2026-09-09 00:45:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 50076adf-1f86-3b93-b6f0-12d05d7da913 | -3.36055 | -61.28373 | 2026-09-09 00:45:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3a8126dd-6f09-30ff-b39b-23870358ee82 | -3.96183 | -59.36755 | 2026-09-09 00:45:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 778ca24b-9752-3653-a03d-b2f525e62bbb | -3.36291 | -59.43909 | 2026-09-09 00:45:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 71074412-7845-37f8-9519-4114e188324c | -3.36164 | -59.42991 | 2026-09-09 00:45:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 716dd4e5-5368-3d22-9681-3927e094f161 | -3.14139 | -60.63867 | 2026-09-09 00:45:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4d785e4b-5fe3-3916-a1ea-c39f1c81a6ac | -3.38422 | -61.32541 | 2026-09-09 00:45:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fab336c9-d1ab-365d-8ba7-6f60ebe9234f | -3.77808 | -58.84679 | 2026-09-09 00:45:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cca642ed-98ba-3b2f-8163-98ea7cb0c534 | -3.89363 | -59.60573 | 2026-09-09 00:45:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1f8d4055-6388-35df-8da4-fddaf8539833 | -3.38302 | -61.31658 | 2026-09-09 00:45:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 17929235-e3c8-36b1-9335-b4c53d36bc5d | -3.96055 | -59.35839 | 2026-09-09 00:45:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 245dc8ea-4efc-3dc2-9848-9a1a4b0e051c | -3.15259 | -60.65494 | 2026-09-09 00:45:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| c6f1ec61-e54f-397b-b915-dd3180830f13 | -1.30903 | -54.6642 | 2026-09-09 00:45:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| fa027b47-cd2b-3890-a0e0-ba4398d04222 | -4.19184 | -59.95477 | 2026-09-09 00:45:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b4d43e77-30dc-3363-910f-655ee4df46a0 | -3.81532 | -55.90396 | 2026-09-09 00:45:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 0e7f917e-28cf-3211-981d-52604dd88a12 | -5.7823 | -45.0849 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96247804-529b-3d12-9dc7-e31c041002a6 | -2.9432 | -50.465599 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5527d38d-7aa4-33e2-b3f5-e510cf8e8108 | -5.7598 | -45.077202 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8fd2cb3-9aff-3481-9dc3-13cc9030d11e | -14.2878 | -44.5881 | 2026-09-09 00:48:00 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d844e54b-6350-36d1-add9-5c717a9ba5a3 | -6.413 | -47.5112 | 2026-09-09 00:48:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d7acc41e-0634-38f5-9340-a7b09e247b9e | -10.7658 | -45.9715 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96a801fe-f565-3f92-93f3-eb116d28d0ef | -1.3172 | -54.6661 | 2026-09-09 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da1744a5-b984-3419-9f22-ac8a66feb309 | -6.1505 | -44.6479 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c5f40ab-18b5-3eb7-b55e-98c58756c063 | -9.7015 | -43.446899 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5c481356-3616-30f9-9984-a4f1a657b86a | -9.7735 | -43.487099 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 27be1fac-bd57-39cb-8af1-30d254fe794f | -12.2765 | -45.804798 | 2026-09-09 00:48:00 | METOP-C | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8062beea-27f0-32d7-99d2-dd4dcd538336 | -9.7769 | -43.500801 | 2026-09-09 00:48:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fab3c374-c82c-3745-b335-eb498c4e9cf3 | -6.411 | -47.502499 | 2026-09-09 00:48:00 | METOP-C | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c13eeeb8-8d1b-318e-9243-f7ff25b53529 | -10.7493 | -45.945999 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4c5869-487e-3327-a3f6-9838049e377f | -4.0004 | -51.025002 | 2026-09-09 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba6f7b4-07ae-3dad-953b-9d5591005efb | -2.1183 | -54.384399 | 2026-09-09 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 245f7bcf-0b8b-3b4b-aeb3-0b0beb68a587 | -2.9367 | -50.481998 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b699f741-9d2a-32cc-a5f8-881ac3e33602 | -5.7763 | -45.0602 | 2026-09-09 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8cec1b8-4542-3255-9c64-df324ef2ce3e | -3.3584 | -59.432098 | 2026-09-09 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ef09bba-9f01-3e4a-8720-3871c273a3d3 | -3.8128 | -53.772999 | 2026-09-09 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de4346f-7a48-39b0-abb1-caa94238b508 | -1.3137 | -54.650799 | 2026-09-09 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c57a620-26f0-3ca9-977f-73e8640a9d7b | -5.7986 | -53.816002 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33df1fb4-d258-34f4-99a2-40916622907e | -5.6754 | -50.100498 | 2026-09-09 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b807f001-0089-35a2-91c6-825995ce9aab | -2.5603 | -54.743099 | 2026-09-09 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| defb738f-0931-3152-9756-4bb71ab6bb05 | -10.7538 | -45.9646 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a2d53706-1e89-3bb5-8615-6956b054d61c | -3.1396 | -60.6465 | 2026-09-09 00:48:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d10a4ca-9ac0-3b4e-97fd-23a8e62aae6d | -1.197 | -55.718399 | 2026-09-09 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64ca5274-c2a9-3255-9d9f-1835f74a7ef3 | -3.548 | -48.181801 | 2026-09-09 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58afbfcc-4a24-3239-9745-b6bbf3d8814a | -3.7623 | -49.101601 | 2026-09-09 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed56959c-6bfa-39a4-bc66-6a908bd65245 | -5.3743 | -56.0168 | 2026-09-09 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5f6b554-8094-32f5-acba-eb04aa397542 | -10.3011 | -46.879601 | 2026-09-09 00:48:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 883879a9-d657-3dd7-9d26-a30d542c8aaf | -2.7999 | -49.577202 | 2026-09-09 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33107a43-4ef0-3639-9430-39ca6c0d8efe | -3.8111 | -53.765499 | 2026-09-09 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd80c76a-435f-3435-9764-94a100ad59ab | -3.3549 | -59.416302 | 2026-09-09 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d7e0bb50-5500-3840-9548-ca897e31fd78 | -3.2696 | -50.091702 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f0f635d-402a-32a4-b4f0-58cb48fbc8a0 | -5.8182 | -53.811699 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467c039c-b56c-376c-9f6a-4b2cb7039cfb | -5.3667 | -56.028999 | 2026-09-09 00:48:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f68236d-34d4-3462-888e-250dec1edbac | 0.6192 | -50.803799 | 2026-09-09 00:48:00 | METOP-C | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff2b478-e96e-3aa1-9d4b-3b809bb0fdef | -3.145 | -60.625301 | 2026-09-09 00:48:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec83571-1149-3d08-a98c-e852d4579085 | -6.1633 | -44.6586 | 2026-09-09 00:48:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 977b51af-7552-31e1-bfe7-0f828b987fcc | -2.7981 | -49.569698 | 2026-09-09 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc42050f-68d0-39b8-9ec3-f0c7b7e9a587 | -2.9465 | -50.479698 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0950c857-a019-359d-b3cf-c1ed73024b96 | -3.55 | -48.190399 | 2026-09-09 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2e5590-86ac-3821-a302-1ec43a0c622e | -3.4465 | -47.264 | 2026-09-09 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523c6951-f540-378f-9550-294c3c30dd1a | -5.8262 | -53.8018 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84b919d-7755-3a81-b74c-569652a647a2 | -6.3675 | -43.596699 | 2026-09-09 00:48:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1edc7714-b970-367c-b531-1910d18f8fd5 | -5.6112 | -44.8456 | 2026-09-09 00:48:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06539ebc-d2cd-361f-9237-455b7769f3ce | -4.2951 | -49.0858 | 2026-09-09 00:48:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aff2c7ab-fbc4-3997-b96c-04a3f02adfc3 | -2.9449 | -50.472698 | 2026-09-09 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04e7c20f-b7b0-3071-abf0-0eaf7d9306c6 | -3.7993 | -52.398899 | 2026-09-09 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11d7f928-9ca7-3a00-8d7b-a3287da015df | -11.6386 | -52.858002 | 2026-09-09 00:48:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b235bc79-346b-326a-aaec-378fc6ece138 | -12.4311 | -43.408901 | 2026-09-09 00:48:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dbad8dc4-42d2-3888-9617-33c06a8100b0 | -6.8391 | -51.488998 | 2026-09-09 00:48:00 | METOP-C | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0910225-2a36-3fea-8e64-c571671a41a1 | -4.3775 | -55.0457 | 2026-09-09 00:48:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c48e3a-2e42-3586-a88a-89b5d2e04704 | -10.7635 | -45.9622 | 2026-09-09 00:48:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
