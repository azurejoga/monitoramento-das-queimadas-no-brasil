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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50a1470b-4146-3db9-9af7-e75934ab74de | -9.38839 | -35.67273 | 2024-12-30 00:07:00 | TERRA_M-M | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 2060fada-7525-36bb-8583-0198ea94a083 | -10.50218 | -36.97841 | 2024-12-30 00:07:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| a93ef802-615b-3b9d-b4d5-3c5b9e7f647b | -12.32554 | -43.43362 | 2024-12-30 00:07:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 59f87c4d-27b6-33d7-a148-205e772796a0 | -9.50081 | -35.94484 | 2024-12-30 00:07:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| d4512c13-b7a3-3728-9400-94460dcc4040 | -9.84192 | -37.12572 | 2024-12-30 00:07:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 625fb720-4d94-3245-b266-d466dc42f8b5 | -10.11841 | -36.1382 | 2024-12-30 00:07:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3a39016e-ee9a-393f-8072-d4b6ccdcf5d3 | -10.12733 | -36.13687 | 2024-12-30 00:07:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.9 |
| 0b5a703c-51b3-34e7-acf7-897b60a957f6 | -9.42548 | -35.93414 | 2024-12-30 00:07:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 3a74b82f-bf72-33cc-a9b8-40754e38c3dc | -9.84068 | -37.11678 | 2024-12-30 00:07:00 | TERRA_M-M | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8a33367c-75ed-3177-b45d-7f19c1d1f1b0 | -10.12603 | -36.12777 | 2024-12-30 00:07:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 7180c7b9-e95f-352d-bcb0-aaf39cf9b6be | -10.49331 | -36.97969 | 2024-12-30 00:07:00 | TERRA_M-M | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 76360db1-c6ff-394e-aed4-299a29481a09 | -11.05941 | -37.67949 | 2024-12-30 00:07:00 | TERRA_M-M | RIACHÃO DO DANTAS | SERGIPE | Brasil | 2805802 | 28 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 597136f6-4c8a-3e1a-9e0d-45939efece6c | -9.49951 | -35.93565 | 2024-12-30 00:07:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| 1812b9c7-018a-3a7c-97d5-44c395d7a53d | -10.82234 | -37.21918 | 2024-12-30 00:07:00 | TERRA_M-M | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| a9deef42-7800-3432-89dd-59b814091375 | -10.15946 | -36.3633 | 2024-12-30 00:07:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 06ea3c30-da77-3470-a990-a710e966ee06 | -9.42679 | -35.94339 | 2024-12-30 00:07:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 4ba5205d-2d97-375e-a1cf-ff4b4dca796d | -2.88011 | -40.05907 | 2024-12-30 00:09:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 537d6763-2ed5-31f8-95db-3acd5688a0ca | -7.36152 | -35.02505 | 2024-12-30 00:09:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| d09a9d73-87eb-3a58-9b95-d6b165ea28da | -6.94193 | -35.14406 | 2024-12-30 00:09:00 | TERRA_M-M | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| cfff25ab-c491-32fd-a201-613b406fa89d | -6.55548 | -35.25397 | 2024-12-30 00:09:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 17.0 |
| cf07b7c1-e51b-3c7c-83aa-f3d8e6f75215 | -6.30904 | -35.22797 | 2024-12-30 00:09:00 | TERRA_M-M | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| d53eb30a-f128-3304-818b-8c292eb2e2be | -8.00569 | -37.16766 | 2024-12-30 00:09:00 | TERRA_M-M | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ce3ed339-80dd-30b7-b117-4406ebea6c57 | -7.7979 | -34.99289 | 2024-12-30 00:09:00 | TERRA_M-M | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 5d0fa458-a1e6-3928-b87e-46f1fec1c643 | -4.90396 | -41.10221 | 2024-12-30 00:09:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b997004e-ce98-34d1-9830-972c6aeca9b0 | -7.75268 | -35.18405 | 2024-12-30 00:09:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8c2beb0f-c02b-3baf-9145-3889cb822aa9 | -6.95148 | -35.1427 | 2024-12-30 00:09:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 47fc121f-ad39-3f28-aa86-0dd316860143 | -5.25027 | -39.42047 | 2024-12-30 00:09:00 | TERRA_M-M | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7fe8b96b-a761-3f2c-bdf2-dea7e4f85b6b | -3.50442 | -39.31171 | 2024-12-30 00:09:00 | TERRA_M-M | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 18e6ae3c-ede9-3752-9646-7a9930c31e48 | -6.94041 | -35.13366 | 2024-12-30 00:09:00 | TERRA_M-M | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| 2e90e79c-9734-32e5-9969-da239f262581 | -8.8594 | -35.71458 | 2024-12-30 00:09:00 | TERRA_M-M | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 590d5221-61db-3072-bba8-92a27d0649cc | -2.80138 | -41.78811 | 2024-12-30 00:09:00 | TERRA_M-M | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a41f6a36-ea0b-3087-939f-fb5025727884 | -6.77808 | -38.60844 | 2024-12-30 00:09:00 | TERRA_M-M | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d1a72070-18dd-357d-a9f8-2ca2b6c244d4 | -7.80743 | -34.99156 | 2024-12-30 00:09:00 | TERRA_M-M | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 6b144447-6a56-3793-816f-cb2131fe6d1c | -6.78579 | -38.59808 | 2024-12-30 00:09:00 | TERRA_M-M | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e5cd5861-c549-38f5-ac60-dd35cec78e64 | -6.31055 | -35.23833 | 2024-12-30 00:09:00 | TERRA_M-M | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 7748df0d-059a-3568-92f7-abf5aed5cbf3 | -8.58354 | -41.12608 | 2024-12-30 00:09:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 561675d0-6a46-34cb-a37c-1ee051f589f4 | -4.90574 | -41.1077 | 2024-12-30 00:09:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 9b5ee1b0-d9bf-3a28-8af6-ae13019d8e45 | -6.94995 | -35.13228 | 2024-12-30 00:09:00 | TERRA_M-M | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a9396c73-2e6f-3ed3-ad80-d19c7f60525b | -8.70299 | -35.77911 | 2024-12-30 00:09:00 | TERRA_M-M | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ba173c95-3594-3af6-8d33-90dba5c7b214 | -5.9404 | -39.68961 | 2024-12-30 00:09:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 3e2f5e00-fffa-3391-aad5-10515a3a8b5f | -7.75413 | -35.19423 | 2024-12-30 00:09:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| dc5957cf-9714-3460-bc0a-851a8791f3d4 | -6.46226 | -35.17729 | 2024-12-30 00:09:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 84282487-610c-3566-b4dc-efc8dd8af177 | -8.57867 | -41.12068 | 2024-12-30 00:09:00 | TERRA_M-M | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a31f1f9b-6638-3f11-83b9-e0efbee5d096 | -7.36003 | -35.01465 | 2024-12-30 00:09:00 | TERRA_M-M | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1291b371-35b3-3a62-b191-02c366b4ada8 | -6.55099 | -35.22256 | 2024-12-30 00:09:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 502b2eda-e713-3aba-918f-c8c56656f091 | -3.92866 | -40.70608 | 2024-12-30 00:09:00 | TERRA_M-M | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| c72a0f3f-c58b-3266-af86-9abb8caa8301 | -6.55399 | -35.24356 | 2024-12-30 00:09:00 | TERRA_M-M | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| af494422-20a4-363b-9349-65b3602a3c7b | -4.90555 | -41.11364 | 2024-12-30 00:09:00 | TERRA_M-M | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 9f59d330-cd8f-30c2-a6fb-c3004daba3f0 | -19.334 | -54.16409 | 2024-12-30 01:43:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 53943add-b125-36ce-a161-e1e843c0ba14 | -9.13509 | -61.51326 | 2024-12-30 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74d245e7-b089-3d96-ba9b-96ba90928d98 | -9.13634 | -61.5222 | 2024-12-30 01:47:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5f0c3ad8-251c-39c4-b026-fce247965cc6 | -4.90767 | -41.09795 | 2024-12-30 03:36:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 47254847-3249-3285-b0d3-e5d9c80595dd | -5.25547 | -44.98572 | 2024-12-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a22037c8-d91c-3b5d-b0a4-a42059ab4d71 | -5.2539 | -44.98806 | 2024-12-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a65a62e4-9956-3760-8a92-b3a2ffb330e0 | -6.55143 | -38.6134 | 2024-12-30 03:36:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4735ec42-b810-3c03-a40e-a942bff8f7f9 | -5.24928 | -44.98467 | 2024-12-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f70fc13b-7a03-354b-a25c-37f57677d38e | -7.14885 | -35.05235 | 2024-12-30 03:36:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5b5b9502-8ba3-334a-b799-fdd13a03cc56 | -4.90284 | -41.0972 | 2024-12-30 03:36:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 7e7a9630-7470-36e2-8bca-c6695f71b3b5 | -4.90195 | -41.10253 | 2024-12-30 03:36:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 49005353-b7c4-3dfb-aed5-6d6438933aaa | -5.25629 | -44.981 | 2024-12-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fa990bd-71f6-3dfe-b60a-324b9fcd0a17 | -2.88151 | -40.05767 | 2024-12-30 03:36:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a930ebc-7c66-3560-83cc-82f8846273a5 | -7.14607 | -35.04829 | 2024-12-30 03:36:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37acbb7b-7587-3cba-be89-ad1b1da366b7 | -6.54963 | -38.61589 | 2024-12-30 03:36:00 | NOAA-21 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 38add500-bcc1-3d4a-b39b-97b467dc1671 | -5.63272 | -35.30245 | 2024-12-30 03:36:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| e160e9cc-e5ad-3909-acd1-120501768c8f | -4.90677 | -41.10327 | 2024-12-30 03:36:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c7d6ad66-843d-32d5-a354-215926d66c2d | -7.14942 | -35.04879 | 2024-12-30 03:36:00 | NOAA-21 | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11879915-0917-38e2-8a4b-bab720b7beb0 | -5.84732 | -35.3663 | 2024-12-30 03:36:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d06c02be-46c7-3187-a21c-938d8af3aea7 | -5.34019 | -40.56849 | 2024-12-30 03:36:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5662e160-4650-38cf-9609-8a3112389af6 | -4.90584 | -41.10884 | 2024-12-30 03:36:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 6a54152b-4bcc-3fde-b1bc-10de41ca678b | -2.90879 | -40.49003 | 2024-12-30 03:36:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1599cde0-2a6a-3db9-884c-06d1bba7b85b | -5.25476 | -44.98333 | 2024-12-30 03:36:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95f4fff6-d6fa-37ec-b889-d02c42a14cbc | -5.25164 | -39.41859 | 2024-12-30 03:36:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e8a779f-b410-309b-9953-2c4fc86b7c26 | -5.62932 | -35.30191 | 2024-12-30 03:36:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5fc8148e-8c7b-318a-be49-3f8a1ab5699d | -5.94389 | -39.68946 | 2024-12-30 03:36:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 30485837-9a04-3e1e-b2f7-3849ddf00a35 | -9.49316 | -35.95854 | 2024-12-30 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9c407fd-e18f-344e-8a64-c55336182da6 | -7.82618 | -35.18225 | 2024-12-30 03:38:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ce46f99a-aeb5-3a04-b30d-e1d2e564bbaf | -6.95887 | -43.00724 | 2024-12-30 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ab9674b6-0648-3820-a1a1-635509cf4196 | -6.9872 | -43.02612 | 2024-12-30 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c539d327-4c94-36fb-9823-ed2c8551e038 | -8.96919 | -36.07644 | 2024-12-30 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71b54b11-d72f-394b-af90-0a839c6e0caa | -7.85125 | -35.17532 | 2024-12-30 03:38:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7ade8229-678c-3ccd-ac1f-9b5b442f71cf | -7.82674 | -35.1787 | 2024-12-30 03:38:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4bedf658-3191-3971-92a4-50949992ebb3 | -7.24744 | -39.16088 | 2024-12-30 03:38:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b17f439f-21f6-35d0-a776-9ef19e9ee153 | -10.80928 | -41.67616 | 2024-12-30 03:38:00 | NOAA-21 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| cbeb2147-fcd6-361a-bc8a-f36e19a3b2f6 | -9.67245 | -36.22796 | 2024-12-30 03:38:00 | NOAA-21 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8052069b-9469-3e3f-a65b-1ac923f2f29c | -10.06818 | -36.14534 | 2024-12-30 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 53bff729-0cca-3c85-945e-c2c28e3acaea | -7.82284 | -35.18172 | 2024-12-30 03:38:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 79d577f7-8a83-331b-aeab-c192226eb0f1 | -13.05904 | -42.02945 | 2024-12-30 03:38:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f7dfd367-8028-354f-a889-86e8f0cbf60c | -9.48556 | -40.96032 | 2024-12-30 03:38:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 36bdf63c-2530-34d4-a90d-834c5d27b7a5 | -12.86235 | -38.36838 | 2024-12-30 03:38:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a8a37cc3-5f65-3d75-b5d8-b1f0baff474a | -7.85068 | -35.17889 | 2024-12-30 03:38:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a86ea24c-d61a-329b-9379-b03985b99788 | -6.96695 | -38.65592 | 2024-12-30 03:38:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 92cb65bf-c1ab-359d-b08f-530b87badc48 | -9.84415 | -37.12033 | 2024-12-30 03:38:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b8ac740a-13a3-343a-89a2-ca2d215f720b | -9.49711 | -35.95546 | 2024-12-30 03:38:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f75ec588-50ce-33b8-8036-a343bb49bcaf | -6.95945 | -43.00394 | 2024-12-30 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88944f88-f4bd-3a45-b428-9099e3515328 | -6.90633 | -39.55092 | 2024-12-30 03:38:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bff9cc5-0b95-3053-bb2a-53c664177db1 | -7.8234 | -35.17817 | 2024-12-30 03:38:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ca009512-6b72-3159-a485-0442182c0eb9 | -6.96418 | -43.00808 | 2024-12-30 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 874d3d8f-5317-3997-bd9d-9ae2832b7245 | -6.96476 | -43.00478 | 2024-12-30 03:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1f48e43-0171-37c1-8692-c08e22d739ef | -15.37878 | -39.22058 | 2024-12-30 03:40:00 | NOAA-21 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5889eaaa-f80e-36e2-a2e4-44897c3a5ae4 | -29.60348 | -51.98909 | 2024-12-30 03:44:00 | NOAA-21 | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |


[Clique aqui para ver as próximas entradas](README2.md)
