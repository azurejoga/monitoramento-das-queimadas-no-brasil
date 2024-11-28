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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38a59b7-83ce-34ed-8f00-f449d1e4fb29 | -3.3837 | -50.1125 | 2024-11-28 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 7dee69ea-bcd8-31ab-8c0c-418dca273989 | -3.1114 | -53.8041 | 2024-11-28 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 0b562b3c-6277-3e96-b33d-b44bbb2fe607 | -3.6643 | -45.7899 | 2024-11-28 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 12362c27-9d5e-3759-8b95-3cd1dcbc3532 | -6.1737 | -42.5985 | 2024-11-28 00:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 38.0 |
| 8c8150f9-5603-3f9a-9605-2db74fd0bce7 | -6.1048 | -48.0327 | 2024-11-28 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| a949f142-094a-390c-b309-b8f8c88f3f45 | -6.1735 | -42.6221 | 2024-11-28 00:30:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| d20105df-ae57-3003-9dcd-87c04fc1a2a1 | -18.764 | -55.8444 | 2024-11-28 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 9eb7cec5-b5df-34e3-99ce-92df01e2a830 | -3.9674 | -48.0851 | 2024-11-28 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| b910485b-aa73-3aed-a658-a266dc5410b6 | -3.0929 | -53.8247 | 2024-11-28 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9cd737bb-8a04-36a1-9386-963040f0bf4f | -5.979 | -45.3395 | 2024-11-28 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| c2026f14-6300-3032-b9f0-3f6cf7fe6a2d | -3.1113 | -53.8242 | 2024-11-28 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 9aefc3f8-294c-3821-a04d-758431a00c6b | -1.5897 | -52.271 | 2024-11-28 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 94374df9-d229-3fcd-925d-ca4991e3d74e | -6.1041 | -43.9593 | 2024-11-28 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 01d623a5-944c-3fdb-9b0b-df6b6fcb0261 | -3.6829 | -45.7891 | 2024-11-28 00:30:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7ca4a325-0d84-376e-91f9-a2c15325a9ec | -2.5963 | -53.9771 | 2024-11-28 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3d7b58c8-653a-3941-9874-119fe25aea28 | -3.0661 | -53.215302 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 351b647e-ca35-388f-8cea-8c6c3a28a89a | -2.6379 | -54.289101 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31ed698b-38bd-3831-8c19-b990a789de44 | -3.1152 | -53.799599 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bfbec54-6e8e-3e28-8ee4-0229ef54381e | -3.1054 | -53.801701 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66bb8836-8e78-3052-9be2-0c107e8e61af | -3.6885 | -49.562599 | 2024-11-28 00:38:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9076c02c-1b13-3d40-834f-1f183e32571b | -2.8589 | -54.080299 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 342fa569-b0dd-3287-8f3d-eb790f55633a | -3.1078 | -53.263302 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd230da3-533f-3cd9-a7bb-f899ddb3db9f | -2.9063 | -51.371101 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4839874f-3ad8-3d1e-a5ff-bd6f90ee2315 | -20.6838 | -49.111099 | 2024-11-28 00:38:00 | METOP-B | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f6391321-e593-399b-a04a-e11f38da32ac | -2.8661 | -54.020699 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d956727b-c9c0-3488-a40a-1e85df8438aa | -21.179001 | -48.6894 | 2024-11-28 00:38:00 | METOP-B | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9de52d82-a206-3aa6-b8ef-e30d8e84dea7 | -3.2981 | -51.1446 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aaedd927-aaab-3f37-88be-0830252b72cf | -3.0407 | -54.018398 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 682d2852-4f16-3266-a950-657d3b11e4fb | -2.5469 | -53.975601 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e977e4-1e2c-35ad-9b52-ac3b81537dc8 | -2.5087 | -45.191898 | 2024-11-28 00:38:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3011cd49-98ac-3f6e-883d-f50239517a4b | -2.8108 | -53.043201 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc8ae9b2-f18a-3492-b17a-ec88a62ef257 | -2.9965 | -51.450199 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f343468-9089-39be-b403-829632611fc5 | -3.2285 | -53.616199 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da9b6be4-58cd-3d31-8f6a-d065e6b6ab7c | -2.8451 | -46.8517 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e70f0bb-4d87-356b-8f58-04a87fd2c94c | -2.9556 | -51.5881 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84e0b35c-9040-3370-83cc-b801774987fc | -2.6026 | -54.086102 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bb66e49-bbad-3d75-8360-824402dd0d09 | -2.2598 | -53.615601 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fee4e6f2-c955-3fdd-af98-28d492e3b117 | -2.6171 | -53.9674 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44fb3d3f-878c-394a-a2e8-9776f6b27edc | -3.2542 | -53.639301 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e550b76-fe66-305f-923f-a5170d842101 | -2.8384 | -46.866699 | 2024-11-28 00:38:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31dfeb5b-c5ac-3d30-bc85-2b5ffb0e6aed | -21.138399 | -48.645199 | 2024-11-28 00:38:00 | METOP-B | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c5a480b-d2ca-3b06-b04a-e8b7f79ef80e | -3.5374 | -52.153801 | 2024-11-28 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cca6c451-254d-3cfe-a2df-65ab46f68860 | -2.7411 | -54.1063 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4feefb65-c672-3e9b-ae57-1e322e8ffe80 | -2.802 | -54.056599 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5531eb1c-5981-3b12-9f9b-06ce106d2bb4 | -3.0698 | -51.047798 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84eac3a7-e9d8-311f-bdbd-d36fd88ad747 | -3.2527 | -53.632401 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dde0da2-994f-374c-910e-69444a5aeba9 | -3.2083 | -46.602798 | 2024-11-28 00:38:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6dc5400e-70be-31ca-98d6-90199774b87b | -3.5066 | -53.799599 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cd4c201-15db-3d02-ab2a-addda06c71bf | -2.6047 | -54.049599 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbcd16b-6277-3348-b27f-f59e340004ab | -2.6141 | -53.953602 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79d91b75-0002-3b56-ae5a-c758887cfbbd | -3.1047 | -53.249699 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4d1374a-b964-31c6-b4e1-c14963f94e76 | -5.9743 | -45.351002 | 2024-11-28 00:38:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fab2157-8137-31ac-af7d-2ca3dae8459b | -3.5754 | -52.276199 | 2024-11-28 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12b8e0cd-ca3c-347c-931f-27b8f53ac62b | -2.8393 | -54.084702 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ab1de1-86cc-3163-8e0a-f3da3d4d8100 | -2.1815 | -53.268501 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 230df493-1e6b-3b03-b294-82897ce3b42e | -2.8455 | -54.112301 | 2024-11-28 00:38:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7276dacb-d86f-3dc7-ad39-216035501d0f | -2.3174 | -51.955299 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750db2fb-42c1-36b5-9c7f-c1506c4b2357 | -3.2398 | -53.620899 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b187cd4-6cde-33c3-82c6-c0b8b346285f | -3.1402 | -51.039799 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4cfbcd5-b448-357e-8dc9-f91e498bb0aa | -2.8465 | -54.025002 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d816f74-04c4-3d3b-b601-ffaff48aa59d | -3.9766 | -50.189499 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 673cdd7e-4ae9-31fd-9993-07696fb37ed2 | -3.3154 | -50.271999 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c26628d-4392-3f87-8a59-f5aa17f0c0cb | -21.1474 | -49.981201 | 2024-11-28 00:38:00 | METOP-B | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92c10819-b19e-3472-b15c-8989f3f24bc7 | -21.136801 | -48.637901 | 2024-11-28 00:38:00 | METOP-B | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 93efcd79-d50a-3105-a7a9-e6cd82e3da0d | -2.63 | -53.978901 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c9a5dcf-00de-30c0-bafd-46c91df5a274 | -3.6741 | -45.787601 | 2024-11-28 00:38:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4d3495-09b2-3a9a-b8fe-88b12e68979e | -2.6156 | -53.960499 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b310ea0-ff60-3370-963e-8a4b4ede3949 | -3.161 | -50.137699 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adc2d6e8-581a-37d0-bc46-1dbdef861f5a | -1.5492 | -46.0411 | 2024-11-28 00:38:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6516e4a-10f4-3f65-bd26-94af49d1590d | -2.7625 | -52.099899 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95ff18de-01e2-3e4d-8ddc-25d38bc10dad | -3.4244 | -50.163101 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ffa24af-1dd1-36c4-9891-6f27439d106e | -3.634 | -51.488998 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6651d5c3-6412-3dc2-98c6-d150f3eac92d | -3.7008 | -43.444199 | 2024-11-28 00:38:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d01fbb1a-4a84-320d-a8a2-6559276c1133 | -3.261 | -53.623402 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0423312-6b82-3aa5-8d6e-f548eac37461 | -3.8564 | -51.378799 | 2024-11-28 00:38:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0342d2-0bad-3c16-8eb4-69c6fd53ae6a | -2.1826 | -52.133499 | 2024-11-28 00:38:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a012c58-a936-36cb-8267-b82cea18d915 | -3.1043 | -54.026199 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19ffb64a-207b-35fa-990f-57da7df11f3a | -2.598 | -54.065399 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30090ae7-7aef-32a5-b5be-014cad148688 | -3.5432 | -50.187 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fdff323-fd75-3811-b548-b3d9eaf7b838 | -17.2806 | -46.280201 | 2024-11-28 00:38:00 | METOP-B | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| af98ad14-181c-3620-bf30-4653bf20997e | -3.191 | -54.3209 | 2024-11-28 00:38:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41ca7ac4-573f-32b1-81c6-c87dc8a21c23 | -2.6094 | -54.070202 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 091f57cd-876c-3d52-9383-589cb87efdd3 | -3.058 | -48.5242 | 2024-11-28 00:38:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39a976d4-faed-3dc2-b443-c4a56ac51800 | -3.2784 | -50.561401 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3ba0d3d-d0ac-3f25-941f-07e6acf4ecbb | -3.2818 | -53.303398 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79a538ca-8750-32ce-9469-52caa69a95b4 | -3.1628 | -50.145802 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 062624e6-4026-374e-8ed0-a7b69450d5ab | -3.7537 | -51.834499 | 2024-11-28 00:38:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0b49fd-baf4-3e5d-bf86-22b8cdf07c67 | -6.0928 | -48.0214 | 2024-11-28 00:38:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9a29276-41f2-3dfe-92a4-508fa3cb2596 | -3.6706 | -45.7728 | 2024-11-28 00:38:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c90615e2-9c96-3ba6-9d77-37f0c0f20837 | -3.1259 | -53.252201 | 2024-11-28 00:38:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f849012-13cc-3c01-a049-e61f2495d46e | -2.599 | -53.9785 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a8ff21-964d-39c2-8b0a-d6c050a0a102 | -3.6004 | -49.9869 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e105ec24-5f01-3825-a2bc-9b24b62402a2 | -3.6187 | -51.149899 | 2024-11-28 00:38:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4187ad6c-a736-32eb-97e3-177df6b2538b | -6.0876 | -48.043098 | 2024-11-28 00:38:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e620a8f-4266-3165-94d2-5ec5a3528013 | -4.0176 | -46.330502 | 2024-11-28 00:38:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1811737c-1827-38ed-bd8a-c71f95dd5ec9 | -2.0198 | -51.188599 | 2024-11-28 00:38:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5156823-3143-3f37-a00e-168c29bf8be6 | -5.429 | -47.914902 | 2024-11-28 00:38:00 | METOP-B | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bdcdeb3-dde1-3aa7-a1bd-5e26919c866d | -2.6593 | -49.5215 | 2024-11-28 00:38:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9f310f5-f654-3d28-9c4b-2b1743669696 | -2.2441 | -53.683498 | 2024-11-28 00:38:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73333bc6-b71b-3a1f-9349-bc11572bea89 | -3.1096 | -53.728802 | 2024-11-28 00:38:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
