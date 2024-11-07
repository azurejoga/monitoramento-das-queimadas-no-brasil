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
| 7012dc1a-63da-3324-892b-46d4232e2d28 | -3.7033 | -48.9986 | 2024-11-07 00:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 53fcc377-7fac-3cc9-ab1c-c614168cab25 | -1.1831 | -53.8985 | 2024-11-07 00:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| abc95a05-700c-3242-9ebe-15740e02643c | -5.1395 | -47.7008 | 2024-11-07 00:30:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 59f0c354-0752-31ff-8264-ea43490fd468 | -2.8016 | -52.9414 | 2024-11-07 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 17f65575-89c7-3c5c-8032-d782e86aecfb | -5.3738 | -46.2555 | 2024-11-07 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 7aad8769-46e4-32c7-8cc6-66669412f628 | -5.0155 | -46.8311 | 2024-11-07 00:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| fcca1ffe-c726-3097-9789-ae9d58c7d5ca | -5.0526 | -46.851 | 2024-11-07 00:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 71.8 |
| c70d647a-e499-3ef9-a651-87b720cda048 | -1.1466 | -53.7177 | 2024-11-07 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 63506373-193c-33b9-8a5b-1a58117964f7 | -1.1283 | -53.7179 | 2024-11-07 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 07f0c302-96a2-3005-b8c2-5f8c71f604e3 | -3.1617 | -50.2038 | 2024-11-07 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 967ea505-a7c8-3bcf-9790-255c59104321 | -5.0528 | -46.8289 | 2024-11-07 00:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4478c7c3-d45e-3fc9-925b-6e7e6c81870f | -8.0313 | -49.6341 | 2024-11-07 00:30:00 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 3d8c1221-49b1-3e7c-84bb-896a6a1fe332 | -4.5218 | -42.8843 | 2024-11-07 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| d97d9631-b0c5-3f35-a17c-f0b3b9a2ada5 | -5.0342 | -46.83 | 2024-11-07 00:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 33339759-e45a-3b1d-ad90-0e704356d60a | -4.6655 | -46.3196 | 2024-11-07 00:30:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 909fd419-fb04-38a8-95c9-0d4e41932c8b | -3.7218 | -48.9979 | 2024-11-07 00:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b0b638ab-d384-364c-9092-d41ffa443267 | -3.4564 | -50.3832 | 2024-11-07 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 5159fa07-56dd-3228-abcd-758c117b6269 | -17.293 | -57.5062 | 2024-11-07 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| a86c17e1-4838-3517-bc9f-736aa51a4704 | -2.8536 | -48.6856 | 2024-11-07 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 2627a08d-0edd-3501-b371-e17b9746db21 | -2.8537 | -48.6642 | 2024-11-07 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 35e3ab51-f07b-3b87-acad-2893aaad67b2 | -6.0782 | -44.719 | 2024-11-07 00:30:00 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 28ad353e-7b16-3203-a6b8-fa60a27af998 | -3.967 | -48.15 | 2024-11-07 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 36efefe6-f217-395b-8930-4273aa3263a8 | -4.5031 | -42.8854 | 2024-11-07 00:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 244d7e53-98ec-3549-832f-0140cda73146 | -3.9485 | -48.1508 | 2024-11-07 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| ec963dcb-9a80-358a-a80a-4f0527ea5d7f | -2.7639 | -53.2265 | 2024-11-07 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 2a191fd4-360e-3b22-8c4c-a77429320015 | -5.9975 | -45.3607 | 2024-11-07 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| ff9aa870-63c6-3a50-b866-8c300b0fd7e2 | -5.9788 | -45.3621 | 2024-11-07 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| 5c99768d-2817-3a35-87ac-6a9b2b344b4c | -5.0154 | -46.8531 | 2024-11-07 00:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 24d5ee74-7c55-393c-8869-0d8bcc9c9b86 | -2.6017 | -51.7491 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04590b3a-3dc6-3f9a-84f7-825c2fc6be05 | -4.2397 | -48.528301 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 454ad826-80dc-38f7-bf2c-e8dd8a795869 | -3.003 | -53.437698 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236cb33e-bf39-3ca0-a8e1-56eb7d63e575 | -2.2373 | -48.023102 | 2024-11-07 00:31:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69f29682-77a0-3728-b8c5-6fa19d4564d7 | -2.8423 | -52.905102 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d260b64-e96d-3fe5-a729-9df5501fb6d0 | -4.9363 | -43.634701 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 517b2772-2403-3f30-8e02-c43e66beb9e1 | -8.1121 | -44.4119 | 2024-11-07 00:31:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4f6a5945-25a2-3f02-9510-4880e8584ff8 | -4.2315 | -48.537399 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c418271-f610-39eb-96a2-ee6f9ff26f97 | -1.0146 | -47.055801 | 2024-11-07 00:31:00 | METOP-C | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 195d307f-81f2-3b58-865f-fd0e8f49333b | -4.1081 | -48.856098 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 699e154a-b290-37d9-9eb9-8414b0cd86c3 | -3.2134 | -53.095798 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdeed562-5700-3ce3-85ce-b8e2f6dbf05d | -2.2324 | -53.656799 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65d503df-6aca-3d67-9e6c-077f1de956f0 | -2.8729 | -49.541801 | 2024-11-07 00:31:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cc46fc5-a33b-3d8d-b582-4465040ca00c | -12.2735 | -51.2118 | 2024-11-07 00:31:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4ed604-6d08-3c26-ae46-6b2b2b3c78f4 | -5.1045 | -43.956299 | 2024-11-07 00:31:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e9a196c-706a-3ce6-89a9-e78e4d027208 | -2.7248 | -51.702599 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5095499-2e3e-376d-bbdc-9498936c7299 | -3.958 | -48.151199 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7476ecd6-f20b-3835-90c1-2b30d0eef2ee | -3.027 | -53.2705 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0371d1d0-a06c-3e62-9537-8198148c6fc5 | -6.6851 | -46.185699 | 2024-11-07 00:31:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3850fc7c-2700-34c2-b296-c4c4919fe612 | -2.7793 | -45.1353 | 2024-11-07 00:31:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9288b8-0e7e-3f04-a1b3-d7341faa3289 | -5.9807 | -45.3685 | 2024-11-07 00:31:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 967fc6ea-a0be-3882-85d3-6ef01380a8cb | -4.7384 | -44.4202 | 2024-11-07 00:31:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ecb88e4-f1f1-3423-8472-61fcd02a82c9 | -5.5612 | -43.703098 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52a2968c-11a5-3669-a527-c0ba16f6642d | -3.5164 | -50.471699 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c92141cf-d1fb-3c5a-a5b2-f9460fbdb91e | -1.9786 | -47.165199 | 2024-11-07 00:31:00 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 938f62e6-043d-38d1-8dea-9ca130cef235 | -3.4839 | -48.242199 | 2024-11-07 00:31:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daedc169-c4c7-367f-b733-850375a1dd92 | -11.6098 | -44.1334 | 2024-11-07 00:31:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4875572c-272f-340a-b387-582eaaceb1a1 | -4.4221 | -47.248699 | 2024-11-07 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 41988992-0d68-3439-a1fa-7823b96ab978 | -6.291 | -43.383202 | 2024-11-07 00:31:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2867bac0-e2fb-3195-9514-241180a3c150 | -5.0397 | -46.8377 | 2024-11-07 00:31:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8286d07-13e3-30cb-a4dd-5fd9b33c45ed | -1.1685 | -47.725899 | 2024-11-07 00:31:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45234f67-60ff-304c-9d02-d9e8ca26fcf7 | -4.1108 | -48.5051 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| affea708-1d5f-3f11-806a-d12c9f2d4b7a | -5.7714 | -46.160702 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c0f2563-81f4-3b2a-b0f1-837406ea0de8 | -6.1721 | -44.859299 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4b62a2de-ae9b-3535-8c47-ca58f8ea3322 | -12.1828 | -43.533401 | 2024-11-07 00:31:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adf0747a-239f-3477-bf7d-af825247c992 | -2.5366 | -45.646999 | 2024-11-07 00:31:00 | METOP-C | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9443e242-9047-337f-8746-af73082a8fcc | -5.4514 | -45.534 | 2024-11-07 00:31:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59b75cf9-b883-3220-8ace-df4cbb2565fb | -4.2768 | -48.646301 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdfee53c-ccc3-3cc0-94c0-9042011d15fe | -4.4866 | -48.4809 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16d18ab8-5bc0-3ab0-a093-688d9a7143ab | -1.7109 | -45.778702 | 2024-11-07 00:31:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1381e674-2a12-3348-8086-b1a00e89543e | -2.8106 | -52.946701 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26ea1cf4-2093-332c-bea2-1bfc5dc74024 | -4.5169 | -42.861 | 2024-11-07 00:31:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 30119326-81d4-3c74-a2d8-4d3371960add | -4.3514 | -48.158199 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 297afd87-2d83-31dc-8f92-f696c8d25222 | -5.4416 | -43.589401 | 2024-11-07 00:31:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8639178-1054-3260-b4f9-b0384c30731e | -15.6114 | -43.576099 | 2024-11-07 00:31:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c9c21f69-5786-3b5e-933f-7b1eea5f094c | -2.6094 | -51.737598 | 2024-11-07 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485870b9-8e45-3d41-8180-bd640ac9bbe9 | -4.2115 | -48.6758 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74f9c4ab-ca55-3ebb-83a7-47367539835e | -3.3048 | -50.082802 | 2024-11-07 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a3504ee-5c9d-3d32-8bfa-f526bfe69665 | -2.8056 | -52.924599 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 201ef3c6-5339-36c9-9418-a21f611fa734 | -4.3455 | -48.6311 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bedaeae-aa2b-3b91-942b-9b99223865ef | -4.3385 | -46.794201 | 2024-11-07 00:31:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e9f665ec-0b01-3fd4-be68-ad5acff660d4 | -6.9494 | -39.812 | 2024-11-07 00:31:00 | METOP-C | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f5368d96-2f96-376c-8f73-14cbac52fcd0 | -3.9729 | -48.125999 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b609c6a-6043-37e2-a464-fe6318ec1e35 | -4.6684 | -46.344501 | 2024-11-07 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d5414f1b-01bc-331a-9f8b-63e8b032da64 | -5.6991 | -45.936401 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97d235d3-74ad-3c43-b477-e1411d5ffc13 | -2.2448 | -53.666801 | 2024-11-07 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c18da7a-1bb6-3f83-ba1e-d706487dcfe6 | -5.841 | -46.239201 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 560718b2-b3ff-30d7-8fd6-0aa237642d0d | -2.0819 | -52.041302 | 2024-11-07 00:31:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66343db8-a2ae-331a-a66c-864ea942f261 | -2.7663 | -53.205399 | 2024-11-07 00:31:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdd490c2-e774-350c-bd57-99b27b21d9ca | -3.7091 | -49.004902 | 2024-11-07 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70580ebe-0450-3846-8ba9-f6e9375242f2 | -6.2483 | -43.552502 | 2024-11-07 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 239eb548-f05a-3782-90cb-4893356492a0 | -6.2502 | -43.560799 | 2024-11-07 00:31:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac0bac4f-ec46-3884-a84a-2e86a54c0837 | -3.0435 | -48.0298 | 2024-11-07 00:31:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64834c1e-07dc-361c-afb0-d505d641b4f5 | -3.9631 | -48.128201 | 2024-11-07 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dafa2d5c-0834-349f-8ecc-f43c8504ade5 | -4.2851 | -48.6371 | 2024-11-07 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41096d39-3774-368a-8c84-8a041615caa2 | -5.7105 | -45.9412 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23ad0d9d-4296-343d-ada1-4c85f4ea01ef | -5.4812 | -43.188099 | 2024-11-07 00:31:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4347c6fe-cdbc-3104-9bf2-42860e88fd07 | -5.3724 | -46.2654 | 2024-11-07 00:31:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8be2e946-03cd-3c14-971b-2777f0614283 | -5.2362 | -44.917702 | 2024-11-07 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 503f59fb-97f4-336e-8db9-7277a6d8edf9 | -5.9456 | -39.666901 | 2024-11-07 00:31:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9c2fd117-cbd3-3405-ac94-e6c8fe0eb34f | -6.4812 | -44.679199 | 2024-11-07 00:31:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 542a0cbb-5e57-3da7-88bb-f1556f0f154f | -2.8821 | -48.903801 | 2024-11-07 00:31:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
