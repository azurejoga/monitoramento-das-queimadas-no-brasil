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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91d809b0-47ea-359b-b5fb-9d49132296b4 | -9.02311 | -59.75594 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d3e4960-9914-394b-8fdd-543853cb0b80 | -8.51366 | -63.86437 | 2025-07-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0453473a-7185-3df6-82ea-52c9bbde2e48 | -9.03201 | -59.77003 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99d5476a-2fa5-36d9-8b1f-56c50ed16d65 | -9.02182 | -59.76445 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc00b8eb-bf1c-3d4b-8dd5-93c3b4685954 | -8.50994 | -64.05064 | 2025-07-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d920c3a2-1a64-38ad-b0ee-323ccd9da669 | -10.55178 | -59.70277 | 2025-07-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82db586c-220d-3fad-9952-b33b63e7c404 | -11.52029 | -54.68579 | 2025-07-28 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2a5b272-90b4-3ca4-91e7-cfd5f799075d | -10.41876 | -60.27675 | 2025-07-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30fc18ce-193e-3307-ace3-a164500c8e05 | -10.31143 | -54.15603 | 2025-07-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80f523a5-9bf5-3587-99ea-3b3c7b9de3ff | -10.42231 | -60.27736 | 2025-07-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f74d9e7-74b9-3961-ad46-c981a1de3d2f | -10.61997 | -65.03767 | 2025-07-28 05:29:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5014148-f44f-30eb-ae52-8aeb15606a31 | -9.72528 | -63.38138 | 2025-07-28 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72e88e8f-395c-321d-b445-dae134e13006 | -10.5448 | -49.49696 | 2025-07-28 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f1d1511-fe81-32df-ad18-8e0ab075da4e | -9.98481 | -67.56945 | 2025-07-28 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e46cb0a2-786c-3a50-b947-6d8f9306ebfc | -10.31101 | -54.15925 | 2025-07-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 38b7da1d-8da6-3505-ba03-4af53f50aacd | -9.98809 | -67.90211 | 2025-07-28 05:29:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54b100b7-8589-3154-824b-5bb9e063824e | -10.31668 | -54.15679 | 2025-07-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a913af6-07b7-3c5b-928f-35e7fabc570b | -9.02246 | -59.76024 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e694db84-ab11-3e57-93f5-9b6b148bc98d | -9.02962 | -59.76151 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a6752cc-0488-3cc9-bae1-b002f56a47dd | -10.41936 | -60.27268 | 2025-07-28 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f9b2c1a-9669-3e36-b08c-e9e1df0772ff | -8.50658 | -64.05009 | 2025-07-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d71a01d5-ecc4-3ffe-9472-45747c7cb4c9 | -8.50936 | -64.05423 | 2025-07-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df6e1a6d-146b-36ea-a563-7ecf65c09852 | -11.52068 | -54.68272 | 2025-07-28 05:29:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d640a73-00b3-3a99-9893-827315b02685 | -9.45988 | -57.85018 | 2025-07-28 05:29:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fcd38b0-7559-3ed4-a56d-f880a5d54d06 | -8.66174 | -63.84825 | 2025-07-28 05:29:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47d9c9d3-7511-39b1-821d-9f2a8d8cd275 | -10.54559 | -49.49007 | 2025-07-28 05:29:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 173d9a31-9d1f-34cf-bfdc-342d64ae41d8 | -9.029 | -59.76562 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7cd7fbcd-7202-3806-a0ed-dd48c48d92e7 | -9.02603 | -59.76091 | 2025-07-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bb66062-48c6-36e4-bd96-63ccf53d8ca0 | -8.506 | -64.05369 | 2025-07-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5813a5-4871-3a9c-8baf-d79900654e6e | -8.07045 | -63.85171 | 2025-07-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 941dcf61-6297-315c-b750-e45d24073987 | -6.5074 | -56.213 | 2025-07-28 05:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7f711256-7df3-3f03-9cfe-2d0dd532dce7 | -14.31736 | -54.15225 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 70fbeeaa-c4dc-3ad7-9dc9-992c394725c8 | -14.31778 | -54.1487 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 425c4a79-f862-3cb7-b7c5-b54fbb83f5b8 | -14.31265 | -54.14452 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f87dd83f-a3c7-3e8f-9256-a59e705318f7 | -14.31673 | -54.15224 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3f2eb46b-797f-3f77-a6f8-beb7f14f3a8a | -14.31176 | -54.15188 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96905a2a-6d30-3cf8-9387-fd52bcf6c5a8 | -18.40357 | -54.89088 | 2025-07-28 05:31:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7d33713-79e5-375b-ad2b-cf490df61f11 | -14.31198 | -54.14442 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc72ec5c-279b-3a3b-ad9a-b2dffc378252 | -14.31714 | -54.14866 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 62da7090-d2dd-35f9-b621-a8da48d29ebc | -14.31822 | -54.14508 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ba06b21f-9414-3834-94f7-a39f24b32fcc | -14.3122 | -54.14824 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 698ee5b6-bac0-3f21-8e7f-e9ad5f8083bc | -14.30618 | -54.15139 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c7c129c-e3e9-309f-805c-5ceea689091b | -18.39796 | -54.89062 | 2025-07-28 05:31:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be837008-09e3-3f66-b045-fa4348a41b9d | -14.31133 | -54.15553 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20ccd655-2675-3f8e-910e-daa59d1a0772 | -14.31156 | -54.14817 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1805c5d-7565-3f8e-bb67-bd418a1b01e6 | -14.31755 | -54.14502 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e6abf796-f834-3a1a-aa7c-45429d58b45b | -14.31114 | -54.15183 | 2025-07-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d3528c53-fba2-325a-8d2b-c29a6acc4bec | -6.5074 | -56.213 | 2025-07-28 05:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0af0ac70-45bb-3970-8285-3ea7f275c326 | -6.4889 | -56.2139 | 2025-07-28 05:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 92571ca4-436e-3cfe-8417-20065a4b63e1 | -6.5074 | -56.213 | 2025-07-28 05:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| fb63ae57-0abd-33c1-9f61-5f54ee227489 | -7.65064 | -44.79619 | 2025-07-28 05:53:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a4231bf1-5bde-35e6-a096-972fa7b5b8b6 | -7.09803 | -44.92661 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 90425c62-a591-3f7c-baf1-bec5a11bda7e | -7.10898 | -44.91784 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f0381fa3-e1b1-3036-a945-35d8dd0d2006 | -4.30619 | -48.10283 | 2025-07-28 05:53:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| ef3525de-e127-3342-927a-29b352bf1772 | -4.16774 | -46.81112 | 2025-07-28 05:53:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1be8297b-21ea-3427-867f-3aaaf072647c | -7.24318 | -45.39065 | 2025-07-28 05:53:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9fb9a118-b4dc-3bb0-bbd4-2bffe997b774 | -4.15895 | -46.80982 | 2025-07-28 05:53:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0040e8e7-31e8-3a6a-a5aa-0b296cc5bb63 | -7.33271 | -44.37077 | 2025-07-28 05:53:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 93f2c15c-6c8c-39f1-a4d0-4084c845eefa | -4.15764 | -46.81856 | 2025-07-28 05:53:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 73dc41bc-d460-3895-b38a-c8606053f231 | -6.88347 | -44.7995 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6256c298-49ef-351a-bd40-9def3dffbaeb | -7.66022 | -44.79779 | 2025-07-28 05:53:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 83632171-6040-3108-83e7-432764326baf | -3.21904 | -48.81395 | 2025-07-28 05:53:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 36b5fd37-f483-35ab-a1f9-dddf29a4c21b | -7.33111 | -44.38206 | 2025-07-28 05:53:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 97702467-a691-3d89-9106-f900a8dc1122 | -7.11047 | -44.90765 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| dfd9aecb-bf34-3396-a550-d1e75c54ea71 | -7.09654 | -44.93685 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 42c7ab9a-edc9-3b58-bf20-4aa0f8777793 | -3.39941 | -47.493 | 2025-07-28 05:53:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 454d6749-0077-3e86-b85d-a56cf82c2352 | -4.16642 | -46.81985 | 2025-07-28 05:53:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 38753491-f1a8-3eb3-b690-d42e80061bb1 | -4.11089 | -47.9305 | 2025-07-28 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bb99a6d3-cf8f-333b-8aec-5f5bef0ab97c | -4.2986 | -48.09229 | 2025-07-28 05:53:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3ce3361f-a943-3f63-8e6a-68d7956d8ed3 | -4.11227 | -47.92148 | 2025-07-28 05:53:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5c9fc8c5-1ff4-3acf-8f63-f22067a1be4f | -7.09351 | -44.95767 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 23d96ecc-fb2a-3482-8670-db215f498d32 | -7.09502 | -44.9473 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| f5794f6f-8a43-38bd-ae02-63ce5772ad5d | -4.30759 | -48.09364 | 2025-07-28 05:53:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 572d289f-9144-32ad-bc43-ec96bc3b731a | -7.08052 | -44.91392 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fc1cdce4-a1ec-388e-a9b9-a4f26f052c9b | -7.07903 | -44.92425 | 2025-07-28 05:53:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 0e2167db-3e69-335a-8519-7828b3bb0c98 | -17.36008 | -42.65536 | 2025-07-28 05:55:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 988701a8-f837-39a4-b338-722811bed76f | -16.60315 | -47.82154 | 2025-07-28 05:55:00 | AQUA_M-M | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 551d0e81-c6d2-35ff-8984-cac7a056459d | -9.6404 | -48.27965 | 2025-07-28 05:55:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b55f5d58-4954-3f83-9b97-35ad7acee0e5 | -14.49922 | -48.64639 | 2025-07-28 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f0d3cc9c-25ff-3a06-a80b-1ad09c2bd2f1 | -14.49041 | -48.645 | 2025-07-28 05:55:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 036dda6b-5b6b-327e-93b3-805b9b68b1de | -6.4889 | -56.20509 | 2025-07-28 05:55:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 4cd15307-8fe9-34e0-b954-1474dc8ccf14 | -10.54532 | -49.49567 | 2025-07-28 05:55:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 57c04ba7-f40e-3a84-942f-5e69ba41087e | -14.31674 | -54.1398 | 2025-07-28 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 46d5135c-6cd0-3ea0-8084-b6587fbc1dcf | -17.36255 | -42.63345 | 2025-07-28 05:55:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ab1669c5-f86d-3d93-9c96-aea1107ee50e | -6.40239 | -53.3475 | 2025-07-28 05:55:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4a97b5ce-b6e7-3fda-b691-054b8f57e95b | -7.80567 | -50.77505 | 2025-07-28 05:55:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| be3f6216-9a38-37f2-936d-dae5cde700f7 | -13.12822 | -47.3659 | 2025-07-28 05:55:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7b816de4-e68f-303e-914b-7ea3a2e76ea5 | -14.98153 | -46.97445 | 2025-07-28 05:55:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7ebfaafb-e07b-3493-8c09-bfa1029b27a1 | -13.11705 | -47.31627 | 2025-07-28 05:55:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4dea2562-93fc-3ad6-8666-614765f5a7d6 | -14.31398 | -54.15567 | 2025-07-28 05:55:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| adb92b15-663b-321a-a4b9-6ace866d347c | -6.49283 | -56.20053 | 2025-07-28 05:55:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 27162ff3-1479-36b9-90f0-51d94caad89d | -10.84784 | -46.67355 | 2025-07-28 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7b2df2f7-8521-3333-a0c2-cc9637fb404f | -12.71785 | -47.01248 | 2025-07-28 05:55:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7f14b9bd-51b3-336f-9c06-341ec5723b09 | -12.66061 | -47.02344 | 2025-07-28 05:55:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 59fab2fd-df0c-33be-98a1-2a51e8d56327 | -14.98286 | -46.96492 | 2025-07-28 05:55:00 | AQUA_M-M | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 59be1984-8c79-3067-9db5-87bcbcaefb41 | -10.54677 | -49.48634 | 2025-07-28 05:55:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| cd0a1e2d-043f-3b68-ad86-8ea9982ffea1 | -8.51362 | -63.86549 | 2025-07-28 06:20:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d233628-5d19-31c8-8982-5529e0a7b3d5 | -9.98477 | -67.57179 | 2025-07-28 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f2b8c56-9efd-3ba8-863c-876f0ef7c0fa | -7.0881 | -44.9547 | 2025-07-28 11:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6bd3c964-9e2e-3a34-8fe0-fda963eec811 | -3.43747 | -39.26949 | 2025-07-28 11:49:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 10.2 |


[Clique aqui para ver as próximas entradas](README20.md)
