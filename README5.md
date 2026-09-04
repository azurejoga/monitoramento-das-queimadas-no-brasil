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
| ebd4116f-5283-3dfa-a319-1798c4957ffe | -8.48467 | -54.65163 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 2cc18141-258b-372d-8796-827d7374568b | -9.02955 | -65.72828 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 676cf52c-125d-3c17-9da2-ec0f3383b979 | -7.01888 | -62.98075 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 17.0 |
| fda78873-774e-3da6-9471-0e9822e2d4c6 | -9.28575 | -60.18796 | 2026-09-04 00:45:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 02ee3494-d63f-3e97-8de4-d6e9254bf9f6 | -7.58913 | -61.19898 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 88a83816-7ff1-332d-9a43-a4ca9d1a8298 | -8.51023 | -54.66407 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 186.4 |
| ed4e4d91-f2e3-39d9-a80e-304f361974ef | -8.49624 | -54.64985 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 295.1 |
| 2a2367a8-c714-33a9-bb41-0e863da596ed | -6.99128 | -62.99546 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 46e8d08c-1178-355b-9e20-25a64c020175 | -7.26378 | -61.105 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| fb264624-c9d7-3697-82e6-198e8fdb9710 | -7.27512 | -61.12185 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4fe970e8-5c8a-32a4-86b6-edb93814fa53 | -7.97941 | -61.15765 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 30ba9adc-004c-3d57-9b3d-f66dc3bc0bd6 | -7.02033 | -62.99154 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 543d3997-4f07-3460-92fa-6cf30cb238fc | -9.04418 | -65.74493 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 9095cd3d-1054-3fce-ac7d-ea38822b963d | -8.20047 | -62.79799 | 2026-09-04 00:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| dbac4bd6-3480-3031-8b96-4d9b0088de23 | -8.29476 | -54.91889 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 10cac265-1942-3962-8959-836441e024db | -8.71275 | -62.95276 | 2026-09-04 00:45:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 07ef5ef8-7e9c-3f1c-ab2a-f9916d4243d5 | -8.56006 | -63.19572 | 2026-09-04 00:45:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 919ab27f-0777-3ea5-abb9-128c40b91855 | -8.46236 | -54.73643 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 0c822dc0-909e-36e7-b593-c6f4490e438a | -6.70814 | -62.86787 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| fb62f74c-2071-3d1a-aa25-2100ed76f282 | -7.57125 | -61.20145 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d1a1166-67c5-3f23-87f9-8ecb116456c8 | -8.4938 | -54.63377 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 0f0bc4f2-c122-3cb9-a522-f012822b69a7 | -7.55282 | -61.34068 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 81215df8-c937-31a7-a62e-38ce1639bf64 | -8.79645 | -62.8892 | 2026-09-04 00:45:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b85a2ec8-5aeb-3aba-a948-cd4507aa1be5 | -8.10123 | -54.78537 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 063e4c2e-c1fe-36a1-a96c-7f027acc4f67 | -8.7113 | -62.94145 | 2026-09-04 00:45:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8d5737f4-66ef-33fa-bb63-1f9cd98d70ea | -7.73359 | -61.65548 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cbf1e4be-4b8f-3f42-9522-ff3ea4d39fbb | -8.10202 | -54.77476 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bec66231-2f44-35e8-9bc9-6ad70c692ae8 | -6.13019 | -57.69238 | 2026-09-04 00:45:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0d7c7b7a-bd5a-388a-a560-0d1dce4c3216 | -8.11276 | -54.78361 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| a5989a7c-8616-3e45-89fe-1ee8c709d43c | -6.13978 | -57.69089 | 2026-09-04 00:45:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cd1affc3-5ef9-3245-af82-830f49558750 | -7.4219 | -61.73249 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8dddff07-a5ee-3fae-8c81-d5271108f57a | -7.56407 | -61.35207 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5b0fc789-219d-39b7-86b8-d7c93b752182 | -7.25488 | -61.10625 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| af0e19d9-d0a2-3c71-880d-335314c29995 | -9.17549 | -68.27938 | 2026-09-04 00:45:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 587c4b1e-0a4a-3dfb-b7e8-4964e3f4b8c3 | -8.1922 | -62.8102 | 2026-09-04 00:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| fc1b9b45-769c-3929-b6c1-e6b73f73fa77 | -8.49868 | -54.66589 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 192.8 |
| eed88bb0-9ec6-31ba-92e2-21c736e4dd92 | -8.57009 | -63.19438 | 2026-09-04 00:45:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e5fd8a02-a72b-3b6a-b408-d867f0fbd2b9 | -7.56284 | -61.34285 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 8a4657b0-8c76-3a45-9059-63d02a75fcbf | -7.98066 | -61.1668 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0311f1d-4b99-3849-a139-5cbb9f9523a1 | -9.53561 | -63.56424 | 2026-09-04 00:45:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 42e9f41a-5587-322d-a2ac-63769451c2b1 | -7.00921 | -62.98206 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 77ae5a5c-fd97-30a8-8e8f-32333b692770 | -8.48714 | -54.66771 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9d3a2714-63b0-30f7-8b00-70d2707d9e36 | -7.51508 | -60.78629 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5fffbc98-fcd2-30d9-bfcc-c7cf7d6be1cd | -8.10436 | -54.79063 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| a0c24a18-9292-3485-8b86-c76d04d27b2d | -7.28402 | -61.12061 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 608c33d4-df81-3d2e-8ca0-16e6dbdac464 | -8.46483 | -54.75225 | 2026-09-04 00:45:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| d7774b06-2f18-3018-bbd6-3c8e3833b096 | -8.78567 | -62.57714 | 2026-09-04 00:45:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d2884e14-30c8-39f7-8d25-64399269ab43 | -6.99953 | -62.98336 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| dc5062c4-8abc-380c-b7d7-482009178aef | -8.88688 | -62.35209 | 2026-09-04 00:45:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c64504c3-7c9b-31fb-8f2c-ab1c2d3e1fb5 | -8.59302 | -67.1815 | 2026-09-04 00:45:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 38762ab6-01e9-3abf-9c32-286e3ea1049b | -7.55157 | -61.33147 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f0eb6cb3-3358-3b79-8d1a-950e70695c16 | -8.83235 | -62.30628 | 2026-09-04 00:45:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54b9038d-35e3-3115-a9bf-dc58b10d454c | -7.00097 | -62.99416 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| dfdbfb1d-32fb-375b-96f5-8a531816a63d | -7.46801 | -63.74744 | 2026-09-04 00:45:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 9acdccf6-d433-3358-859d-f88c9766bd15 | -9.1161 | -65.49352 | 2026-09-04 00:45:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9f3124fe-edd7-3b09-95cf-6b6950061265 | -10.28602 | -68.85197 | 2026-09-04 00:45:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 36.1 |
| da83d8c4-2e0b-33ad-886d-738e91304e12 | -7.79673 | -62.34566 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4524f615-c985-30f7-8fbe-c510e762d054 | -7.02856 | -62.97945 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d05512e0-9378-33c5-8eb6-1cf63f7bb5ab | -6.70674 | -62.85735 | 2026-09-04 00:45:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 734e4096-46fb-3c10-94c7-a890c2a5a12b | -7.57248 | -61.2106 | 2026-09-04 00:45:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 49040a87-d997-3d0d-8bcc-3741b35072e9 | -7.54906 | -61.31309 | 2026-09-04 00:45:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a95eca93-fe7a-3477-bcb8-dafee0344267 | -3.14374 | -61.17688 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c7f7bb6-a984-34dd-939e-e50400d9b133 | -5.16791 | -60.27954 | 2026-09-04 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c04e449a-6b6c-3340-8977-1774d545a361 | -3.3935 | -61.32635 | 2026-09-04 00:48:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1e8be79f-ced9-3d04-8f55-049eb1dbd966 | -3.37245 | -59.49886 | 2026-09-04 00:48:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 28d19b0b-d636-399f-9bca-156a0ce2f897 | -3.97333 | -60.03449 | 2026-09-04 00:48:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 487d6088-7fad-323b-9d2e-be83f866db50 | -3.12459 | -61.23307 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9af5db6d-b63e-3799-b704-db0b38a9a8a1 | -4.47977 | -55.41095 | 2026-09-04 00:48:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| b23e0571-6cb3-3066-80bf-4b8302717d0f | 0.88681 | -59.6916 | 2026-09-04 00:48:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c823159c-ef98-3341-b3af-d41abfbddd22 | -3.75933 | -61.76527 | 2026-09-04 00:48:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4d0e5c0f-3723-3e86-b47d-4d629edb64f6 | -3.19248 | -61.20576 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bde9b230-fa62-37b9-8d8b-91be96756648 | -5.85243 | -61.17033 | 2026-09-04 00:48:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c541b5b1-4e4b-30f1-b9ca-c3ed8aef9572 | -3.21465 | -61.15179 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f4e2d89a-c95e-3a61-98d7-86cc6f6f8818 | -3.14474 | -60.6443 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 95f746ba-bdfb-361c-bb6e-ef8e692d94f7 | -5.33257 | -60.13641 | 2026-09-04 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8bfc1db6-bc1d-3f48-a102-a2149635bbd8 | -4.23829 | -62.24086 | 2026-09-04 00:48:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0782286a-cbd8-32e4-aa3b-536446dcd551 | -1.2463 | -54.53378 | 2026-09-04 00:48:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f4c1c561-caf8-3c59-b5ab-6d74caf07c6e | -5.17792 | -60.28709 | 2026-09-04 00:48:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 99ee6356-fab5-3814-8698-df4c0248609c | -3.01934 | -61.4834 | 2026-09-04 00:48:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| abc0cccc-1b4c-3b0e-a937-2eb504f38a2b | -3.13976 | -61.21311 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8d909530-60a5-3c73-bca1-c6f5858d577a | -4.10532 | -60.66312 | 2026-09-04 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2ea9047f-3838-3ac7-a5eb-638351301b1e | -3.17648 | -61.15448 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 96d18eab-58fd-3174-81e3-edeadf292a8b | -1.80837 | -53.97066 | 2026-09-04 00:48:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f1330d55-51d3-3b77-b0f2-0a12b21cc64e | -3.07482 | -61.08541 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 6faefb24-58af-32d7-a91b-4217b7185d80 | -2.58545 | -59.40698 | 2026-09-04 00:48:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8fd758fc-5aec-3a61-9565-015f34bd8325 | -4.12163 | -56.35127 | 2026-09-04 00:48:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 18a5d168-d6c8-3922-b577-35939012f65e | -1.74294 | -54.9935 | 2026-09-04 00:48:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4e1022ae-9285-3c6e-b0aa-d55e7db28269 | -3.16529 | -61.13822 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a0dabe9-920d-36e8-96c1-bf040e10cee8 | -3.61292 | -60.56626 | 2026-09-04 00:48:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6075f0b8-24d4-3f86-96f3-c44274a9fb22 | -3.39229 | -61.31757 | 2026-09-04 00:48:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c9a1950a-1056-3ed8-afc5-f21a7b4bd960 | -4.29283 | -59.95306 | 2026-09-04 00:48:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 56c86b81-bc01-399a-80ab-837e69b20a02 | -4.14529 | -60.69323 | 2026-09-04 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 2531e101-e81f-318a-9e99-4d5f8fc1a7be | -3.17768 | -61.16323 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ef12bbc5-1827-324a-bf2e-dc978e8b191b | -3.37375 | -59.50813 | 2026-09-04 00:48:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 29dee1fa-8fd9-39a4-9f66-cd7ba2903e5a | -3.07362 | -61.07667 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 7594eb51-8918-3a3a-90c9-9cdaa5c70107 | -3.16408 | -61.12947 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 83a22725-9c46-36f8-aea1-0d4822060b85 | -3.14494 | -61.18563 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7f22949c-09fe-396f-a8d7-e66aae6d32c5 | -3.77587 | -61.75386 | 2026-09-04 00:48:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 544756be-39c1-3be9-bc44-fc8ec2c3d8ad | -3.16288 | -61.12073 | 2026-09-04 00:48:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c9123ec7-8dc4-394a-a913-2a86ed70e072 | -4.09654 | -60.66435 | 2026-09-04 00:48:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README6.md)
