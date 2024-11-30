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
| 12880a18-85b9-3a31-9b5d-baf768cc8882 | -1.6938 | -46.7833 | 2024-11-30 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 156.1 |
| e81b614e-6572-34a2-a374-884b4d600352 | -2.5963 | -53.9771 | 2024-11-30 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 90c792ee-9f73-33df-8fe5-d18cdf65de9c | -17.6654 | -57.5645 | 2024-11-30 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.8 |
| dd368a8a-8f33-3e77-8f57-f5b1e5bc7bea | -3.9886 | -41.5165 | 2024-11-30 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 287.7 |
| 72d30cf3-78cc-37d3-ae9e-e269b82327a6 | -4.8713 | -41.2915 | 2024-11-30 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 304.1 |
| 3525ec5c-7951-3f88-b5f5-db68185a9e56 | -3.2406 | -53.6393 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 50392a73-11b0-310a-a012-9507531ec416 | -4.8523 | -41.317 | 2024-11-30 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| e8020f76-0264-37cb-b44b-c552cf2bb446 | -3.9884 | -41.5405 | 2024-11-30 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 383a8e70-62e6-3da8-a5e9-e476a1300d69 | -3.3668 | -49.7545 | 2024-11-30 00:00:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| fcdff1fc-5f8b-3be5-a060-797a1fac7951 | -6.086 | -48.0557 | 2024-11-30 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 98f02716-9814-33fd-9b15-437160ed1f58 | -3.2591 | -53.6186 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| f5d6920b-5e08-3d7a-aa1d-896637fb806b | -11.4205 | -45.095 | 2024-11-30 00:00:00 | GOES-16 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3294ac02-05ba-313f-b488-c2a13178cfd6 | -6.0862 | -48.0339 | 2024-11-30 00:00:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 1c1b70e9-cdbc-34a4-ba3f-1b5c7ae200e4 | -4.8711 | -41.3157 | 2024-11-30 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 91.6 |
| d38bd17e-4309-3689-bbed-3663839e0989 | -17.6651 | -57.585 | 2024-11-30 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 20a61ecd-8d34-343a-8565-2fe977f6abe0 | -1.6777 | -45.7868 | 2024-11-30 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2222a277-d1b2-376a-8f5e-10c231d7d4d8 | -3.9699 | -41.5176 | 2024-11-30 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 325.2 |
| c386cd4d-5e94-30f1-92df-744337074292 | -1.4379 | -55.2533 | 2024-11-30 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 142.1 |
| 70d01331-3dee-3995-9ee4-de5253f9cbf9 | -1.2739 | -54.5587 | 2024-11-30 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 94c5097f-b87d-3df3-8f28-41c5f9c3a82f | -1.2556 | -54.5589 | 2024-11-30 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 3842c98a-79bf-3194-8346-0de5c2538adc | -3.1481 | -53.8233 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 3e13afb2-96c7-3410-b282-f438e9365c8a | -1.438 | -55.1343 | 2024-11-30 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2d97d8f4-eab0-3cd6-9803-8e0f33dc61be | -1.2556 | -54.5389 | 2024-11-30 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 625b2ca3-dbde-3b38-8886-2c789154a7ed | -1.6419 | -53.8731 | 2024-11-30 00:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 21819343-0f6e-3edd-811d-d4cc935b0f4c | -2.614 | -54.2177 | 2024-11-30 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| cb10701e-df8c-3091-8552-2760900ed92a | -3.9888 | -41.4925 | 2024-11-30 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| af9cc1c5-9322-38b7-b066-cf16b23cca16 | -4.8525 | -41.2928 | 2024-11-30 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 113.7 |
| e9856800-ea54-3c22-87de-67798d56f463 | -4.6652 | -46.364 | 2024-11-30 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 899b362c-d817-3b49-8930-b620999d0e8a | -3.9697 | -41.5416 | 2024-11-30 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 47d37a66-6479-3793-8292-e3a0531d27fe | -3.4976 | -53.7935 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1ebb46a8-7e6b-363b-91da-d95a7d2d7510 | -3.7021 | -45.6764 | 2024-11-30 00:00:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 81049e89-4495-3306-b189-23b480b506d0 | -3.2407 | -53.6191 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 961f0bf9-6032-31b6-9893-199bfd5c1c20 | -4.665 | -46.3862 | 2024-11-30 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2229234c-5ad6-3887-97f4-a23237da6bf0 | -1.2739 | -54.5387 | 2024-11-30 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7cbcd121-3d7a-32fd-a42a-847b8d2d4237 | -1.6595 | -54.2341 | 2024-11-30 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 591f249e-57c7-341d-a8f3-d419b35abe60 | -4.6838 | -46.363 | 2024-11-30 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 158.0 |
| dd80da1d-7c68-3560-addc-11df53f4efb6 | -2.9965 | -45.5258 | 2024-11-30 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 194.2 |
| 2b0f7b1b-7466-3682-95a2-f8fa80ac7d79 | -4.6237 | -47.0069 | 2024-11-30 00:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 48.4 |
| b8c3a096-00a9-327e-b79f-b8cc33ead3c0 | -2.9966 | -45.5033 | 2024-11-30 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 0ba8e084-9d4d-3ab6-b650-1e61b4a8ae65 | -3.4792 | -53.7941 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 6fdc066f-e7b0-31fe-bff7-8ed18273d0fa | -4.8715 | -41.2674 | 2024-11-30 00:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 0075d8bd-36b8-31f5-953e-11a59d21ed9d | -3.148 | -53.8434 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d2f83e94-c5a8-3bd1-8a08-a924d139f905 | -3.3306 | -54.1805 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fa2ace36-a5d9-38dd-a078-6aa21bcf9323 | -3.0151 | -45.5251 | 2024-11-30 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 90d0e5bd-0bec-3cca-bef7-1b4f2c02924b | -1.4379 | -55.2335 | 2024-11-30 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 1fd0200c-eb2c-3e45-b256-af0d5b7f61f9 | -1.0022 | -51.7235 | 2024-11-30 00:00:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 7b2a0b5d-625b-38b4-84cf-c49c6d44e9f5 | -3.259 | -53.6388 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 91026295-c90a-30b0-83f1-8838ab0b946f | -3.1292 | -44.9801 | 2024-11-30 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 478aa3f7-3d6f-3268-9ab4-8feb9d0fad4c | -2.1928 | -47.1451 | 2024-11-30 00:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d7adba77-0a66-385c-b6bf-9300d022362d | -3.97 | -41.4935 | 2024-11-30 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 7747df3f-46be-3900-a484-338a316b7858 | -1.5668 | -45.6549 | 2024-11-30 00:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 50b3ddb6-02f4-3801-a1cc-74dde2c0c93d | -4.6837 | -46.3852 | 2024-11-30 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4a62993c-71eb-3005-9cc0-f6075aa944c4 | -1.6753 | -46.7836 | 2024-11-30 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| dc41806f-92a0-32e5-80ee-cbd467420f96 | -4.6051 | -47.0079 | 2024-11-30 00:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 32108dc2-2992-376c-8656-a8845dd770bb | -3.4975 | -53.8137 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| eefc3a56-3679-3b68-aed5-2fcaeac5858c | -17.6457 | -57.5668 | 2024-11-30 00:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 523e580b-2079-3f13-83fe-f88fdd1c5e05 | -3.3998 | -50.6573 | 2024-11-30 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 57d21025-4138-39a5-9db1-87a1a1cb6412 | -2.8304 | -45.2845 | 2024-11-30 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b11d7c18-68d2-32dc-a140-51a57ff3d185 | -1.6939 | -46.7613 | 2024-11-30 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| cd72d7d0-0865-399a-ae9c-30fbb670897e | -3.1291 | -45.0028 | 2024-11-30 00:00:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fb99f7e5-1a72-30ef-b56d-fe1454a9cbf2 | -3.4791 | -53.8142 | 2024-11-30 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 1191f241-1d4b-3000-bd43-2d2a452b6337 | -3.99 | -41.54 | 2024-11-30 00:00:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 176d1ddf-b0d5-382d-a8d3-5c524266270e | -4.85 | -41.32 | 2024-11-30 00:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c43caf5e-dd95-3b1b-a631-b97379d93ab4 | -3.97 | -41.54 | 2024-11-30 00:00:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0c3c0ab4-4f9d-3596-97a5-b49c772aae47 | -3.97 | -41.5 | 2024-11-30 00:00:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8415dadb-2508-3b39-9f38-b2286f27c457 | -4.85 | -41.27 | 2024-11-30 00:00:00 | MSG-03 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d864476b-af30-3f2b-ba80-4f087a2a4e32 | -3.99 | -41.5 | 2024-11-30 00:00:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bc7d9499-d4cc-35ae-a647-e9f504f37561 | -17.6654 | -57.5645 | 2024-11-30 00:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.3 |
| a1e8c2b6-869a-3ab5-acac-606a9fdef7ed | -2.9614 | -45.0769 | 2024-11-30 00:10:00 | GOES-16 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 1331494b-36d4-33b1-be75-8d4ff2834e4f | -3.9886 | -41.5165 | 2024-11-30 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 259.9 |
| 09d79c32-acc1-3ab5-8b22-2f2c8ed691bb | -4.8525 | -41.2928 | 2024-11-30 00:10:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 8f1c7235-d9a9-3b3f-a33b-0e55969b02cf | -3.97 | -41.4935 | 2024-11-30 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 7258a4e8-d8bc-3a3c-b534-4d943d995c2a | -2.614 | -54.2177 | 2024-11-30 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ebf8217b-e628-3956-aafa-8f999a9951a3 | -1.6753 | -46.7836 | 2024-11-30 00:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| bb6ddb59-0481-3193-b585-914fc4346179 | -1.2739 | -54.5387 | 2024-11-30 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 4d962f92-f063-3425-80d9-886559352f99 | -3.702 | -45.6988 | 2024-11-30 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e2d28df8-0964-310b-86a6-2dac69ea98a7 | -3.3998 | -50.6573 | 2024-11-30 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 481122a1-8794-35dc-b3e0-21726ff274a6 | -3.9699 | -41.5176 | 2024-11-30 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 286.7 |
| 2edf6209-c295-3cf9-ad88-9747460ab218 | -3.4791 | -53.8142 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 198.9 |
| 2d5de849-347d-3455-b38b-8385c1a9a688 | -1.2739 | -54.5587 | 2024-11-30 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 146.0 |
| 8570ab5f-59d4-3f48-953d-d77cd4b23ed6 | -1.6938 | -46.7833 | 2024-11-30 00:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 9fbdf454-29ec-362f-87a1-2edca0f70d10 | -1.4379 | -55.2533 | 2024-11-30 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| b60e6986-cfb2-3e83-a32a-7599cb1f3a3d | -2.5963 | -53.9771 | 2024-11-30 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e90a5038-dd11-3273-8816-91b6165fd167 | -4.6051 | -47.0079 | 2024-11-30 00:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 140.0 |
| 0d808549-729f-37cd-a59f-680c940f7b12 | -1.2556 | -54.5389 | 2024-11-30 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 01f37ae8-5374-3951-8eac-6c6ac5c41516 | -3.4976 | -53.7935 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e0162d18-d72a-3609-8b77-7587f7603360 | -4.6237 | -47.0069 | 2024-11-30 00:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 137.9 |
| f250d8d6-cb91-35c6-9b19-d8ccd8991cd4 | -2.9966 | -45.5033 | 2024-11-30 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0bd70c85-1c4f-341d-8a8f-e25033a61215 | -1.4562 | -55.2134 | 2024-11-30 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ce140444-eaab-336c-b17e-fdfdd30250b7 | -3.2591 | -53.6186 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fc678e1a-558d-3807-b954-55a239b35c1a | -3.148 | -53.8434 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7f2a93f6-4b59-3397-b487-bb7045ba4020 | -3.2406 | -53.6393 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 9a357241-73f2-3793-9673-c8869e1fba41 | -3.259 | -53.6388 | 2024-11-30 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 87234d6a-4b21-3434-93c2-00250036d41e | -3.9888 | -41.4925 | 2024-11-30 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 121.1 |
| ef1ac0c0-ad9c-331a-bc2d-d53f1d6b41f4 | -4.6652 | -46.364 | 2024-11-30 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 127.2 |
| b2343ed4-4f7c-33d7-9c92-66e7b428ccd8 | -3.6758 | -47.1176 | 2024-11-30 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| febeef81-c711-3018-97a2-b339143167cf | -2.9965 | -45.5258 | 2024-11-30 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 56f035af-ef1a-3f0a-9050-600369f996e2 | -1.6777 | -45.7868 | 2024-11-30 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 08c61582-6375-32dd-9a5e-859189306be3 | -1.4933 | -54.9548 | 2024-11-30 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 2df4f988-49b4-3fbb-a131-5a7eb2940789 | -4.6838 | -46.363 | 2024-11-30 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 117.3 |


[Clique aqui para ver as próximas entradas](README2.md)
