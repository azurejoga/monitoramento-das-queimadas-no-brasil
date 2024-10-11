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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbccb982-e280-393e-96d5-fd61012c1983 | -6.75119 | -59.33438 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c8422b8a-11b1-388a-b3ff-31a82d1f98cf | -6.74447 | -59.33298 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ede49339-c295-3080-859a-323a0f08082f | -6.74331 | -59.33915 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cb9f630a-09e0-320e-a5fc-597bb5a86bb6 | -6.73001 | -59.2984 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a150ff8-c2d0-3e2f-97cc-056f4c67630d | -6.55394 | -60.03658 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83e910f5-ccfe-3a37-98de-38ca76b61a71 | -6.54833 | -60.02779 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8ac7ab0-4380-3380-92b2-3c5530ad648c | -6.54422 | -60.02523 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bbfce2e0-3318-3c7e-ba52-b02ec1019ef0 | -6.54245 | -59.7712 | 2024-10-11 04:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bcf3eec-c4b4-3dd8-bcd1-560937be275b | -6.54167 | -60.03893 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9d4b64dd-5eb7-3e45-9525-880b8bda86f0 | -6.54061 | -59.77382 | 2024-10-11 04:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5871d76d-6acb-3c39-93ce-d9fc6f2d3c32 | -6.53998 | -60.03322 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bbe16ee0-2f49-395d-8045-a6f0e473d81b | -6.5355 | -59.76991 | 2024-10-11 04:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73e88895-c052-356c-846e-6e6d1a560931 | -6.52231 | -60.06441 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a86eb7d3-445d-3873-9a0d-906b45293ea2 | -6.51524 | -60.06314 | 2024-10-11 04:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dbba9256-3469-3dbe-881b-b795a37099de | -7.10583 | -59.3003 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 819df8d5-c76a-3fdb-8cec-7c1ba9f68a47 | -7.09914 | -59.29895 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bbb8119-a480-3666-b115-b68a6ad4136c | -7.09804 | -59.30489 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3977f258-2586-3c20-8222-6f7382cbd38f | -7.0912 | -59.41646 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a954a92e-79fd-32a8-9cb4-2c2819501999 | -7.08446 | -59.41513 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0ae3b26-aa04-3dc8-9c57-4c33c593fe60 | -7.07772 | -59.41377 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 111bba6c-4510-3128-8e2f-6ccd5c712cfa | -7.07097 | -59.41254 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73acd533-7962-342d-b59b-fa5c47be92b6 | -7.06981 | -59.41871 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e58b5cda-e2c9-3cd3-a547-eddd058617f6 | -7.04216 | -59.36877 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb30e1d7-20bc-35af-9605-5a2033f55b73 | -6.9667 | -59.47464 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19dd1afd-7906-3c85-bc82-bf7f5112956a | -6.77372 | -59.32592 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6ccb904-d0b0-30bd-8616-a4faab44f5ba | -6.76698 | -59.32464 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 939275e8-f028-3bd8-a99d-72dc5b18985b | -6.76581 | -59.33092 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d414c47e-b5de-31e9-b4d2-2db076e716f4 | -6.75905 | -59.3297 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62ffa2ba-3da6-3a1c-b3d3-d2f515cac9dc | -6.75006 | -59.34047 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 179a1744-20d4-3307-9c3c-309a70b835b1 | -6.73671 | -59.29985 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f11b1775-76bd-30db-85f4-81f64bc74f57 | -6.73487 | -59.29732 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d4614d3-9e2c-30d0-a8db-b222d44cfd93 | -6.73375 | -59.30351 | 2024-10-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39100416-5d32-3e17-a1f3-e24eaf90982e | -2.6533 | -53.3506 | 2024-10-11 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 48e5f317-195c-39da-aaaf-a4f89c8588d3 | -2.6716 | -53.3502 | 2024-10-11 04:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 41b4bf62-5b77-383a-ae74-882e00fa2a73 | -2.9673 | -52.9169 | 2024-10-11 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5b5d3ef3-d84c-3f05-96e4-d344c41334aa | -2.9673 | -52.8966 | 2024-10-11 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| c842db83-ff72-35bc-91bc-991bdd7417e4 | -2.9857 | -52.9164 | 2024-10-11 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 50657fb9-4757-3010-9042-f9c05308765c | -2.9857 | -52.8961 | 2024-10-11 04:25:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| e91d98a5-6ca0-386e-957a-629fbe14f344 | -3.1423 | -50.4352 | 2024-10-11 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 7b6d2cac-e577-33fa-888f-a4ea142fd975 | -3.1607 | -50.4556 | 2024-10-11 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 99cd269f-3e06-3397-bf2d-274ec9cff5b6 | -3.1608 | -50.4347 | 2024-10-11 04:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7a4484ba-204f-30ce-9b8c-af1476fad85d | -4.0962 | -48.2523 | 2024-10-11 04:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 178.0 |
| 93a5e2e2-2456-3fed-8fff-bb164c19e2eb | -4.0963 | -48.2307 | 2024-10-11 04:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 6485eb4e-a6ed-3d30-8060-b52130b67ca0 | -4.1146 | -48.2731 | 2024-10-11 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 0cbdcc90-e4d9-37bc-b99e-e2c758cf2a34 | -4.1333 | -48.2507 | 2024-10-11 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e2743c06-4e3e-36f8-9200-cb9b7d73af3f | -4.1149 | -48.2299 | 2024-10-11 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 233.8 |
| 8eddc752-50d6-3fe6-8c0c-941d05211ead | -4.1148 | -48.2515 | 2024-10-11 04:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 358.2 |
| aa3525e0-d84a-3f52-8fb4-8a2b801a820f | -8.4417 | -55.4692 | 2024-10-11 04:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9ad76c83-21be-30b9-82f0-8525a09d2223 | -8.4419 | -55.4491 | 2024-10-11 04:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 8e5a4210-2a07-3124-b8b0-2ba77408893c | -9.6389 | -64.9664 | 2024-10-11 04:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 652e502a-06a2-376e-af18-8fb259ca2c59 | -9.6575 | -64.9658 | 2024-10-11 04:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 55c95549-9d7d-3027-98d4-1f981f7e6212 | -9.6576 | -64.947 | 2024-10-11 04:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 6b10c646-41c5-3609-b951-282dbd3cdf0a | -10.6962 | -53.0354 | 2024-10-11 04:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 6c4d770d-60c9-30f2-8ee3-d9803080ae04 | -10.7059 | -64.1138 | 2024-10-11 04:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 746b2333-91d0-3588-b95e-04a9abbfb899 | -11.2763 | -60.4844 | 2024-10-11 04:26:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 85abc961-ce0f-3ad7-801f-d2a016d48d7b | -12.4182 | -53.1544 | 2024-10-11 04:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 6509e8d7-8ee3-3407-805d-527740f541b5 | -12.7678 | -44.8671 | 2024-10-11 04:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 1f9a8d91-58a1-3404-b220-cc8c5eac109a | -12.9658 | -53.511 | 2024-10-11 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9ca8a0f1-935a-35e5-8942-0e8056e03cc2 | -12.9661 | -53.4902 | 2024-10-11 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3c9b043d-6d40-3ddc-853b-6f18f82fed2c | -12.9852 | -53.4881 | 2024-10-11 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a3c7c0a6-d561-3bd7-a0ac-e762bdca5d9b | -12.9855 | -53.4673 | 2024-10-11 04:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 9868b852-dcb6-3f69-bf87-55913dd4b57f | -13.7346 | -60.6079 | 2024-10-11 04:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 0204eb91-dc9e-31e8-9600-611d64e65e2e | -17.65272 | -56.32917 | 2024-10-11 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 991ba0e1-6e37-3664-8173-2c0a973af541 | -17.64811 | -56.32816 | 2024-10-11 04:27:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 977ee807-3e74-38b9-a2c7-7ba846c4dba7 | -15.73589 | -46.88223 | 2024-10-11 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1f1dc08-6b4f-3199-af91-099fb691779c | -16.60875 | -47.29686 | 2024-10-11 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54ebc6db-2843-3851-bd3c-382f0d78a643 | -16.6082 | -47.30056 | 2024-10-11 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 69a25247-8f8c-3e6a-a958-4eb35b1a4f62 | -16.60539 | -47.29633 | 2024-10-11 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5d16e95f-eb7e-3c2a-8ee9-d2ddae8b313b | -16.60484 | -47.30003 | 2024-10-11 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6a3966b3-cc0e-3aba-b770-9ac7a675808b | -16.60341 | -47.29615 | 2024-10-11 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e73a13f0-dfb8-31c4-bcf8-dc2848cdee31 | -16.60284 | -47.29985 | 2024-10-11 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5a06255d-e3bd-37eb-8312-74379f40e059 | -15.30477 | -48.77039 | 2024-10-11 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 315848f8-1f98-37e6-9cc6-606bbc0357b1 | -15.30306 | -48.78112 | 2024-10-11 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 258ce466-0634-3748-98a5-165af79ed240 | -16.0441 | -49.11933 | 2024-10-11 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4afee87e-efce-3ce4-9084-80d050b58051 | -16.04353 | -49.12292 | 2024-10-11 04:27:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80eedd42-12e0-3b9b-b23c-b655ca782e71 | -15.31243 | -48.78637 | 2024-10-11 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd624181-624e-31cc-a7d5-1bb795ffc997 | -15.30854 | -48.78941 | 2024-10-11 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdedecc1-7e59-3024-8071-405be2fd7d6a | -15.30523 | -48.78885 | 2024-10-11 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d173ade7-348f-3bf5-b5b5-069b36213a51 | -17.16385 | -57.47814 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2b98deed-b838-31c2-ad71-50162582cdff | -17.15883 | -57.47701 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 334ede05-191c-39d7-bf39-6c058802b794 | -16.99668 | -57.46248 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 91661e94-6e42-370f-8fcf-30189a229662 | -16.99607 | -57.46555 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ef35aaa9-10e3-351d-8725-6fa161aae9b7 | -16.99547 | -57.46861 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b87c5aa9-fbd7-374a-a449-9d9ba460b7b8 | -16.99539 | -57.4622 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b336c800-a344-3d8f-898e-5452c8acd665 | -16.99477 | -57.46525 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f0640c68-2b7e-340c-9eaa-80157ca756bd | -16.99414 | -57.4683 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c8e7a7ee-7f70-328c-af0d-9e7a365efa9c | -16.99165 | -57.46136 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 3184e237-9eb4-3950-9dd7-91bbd874d0d1 | -16.99105 | -57.46442 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 56cd752a-e766-35ad-9170-9632bee4c378 | -16.99044 | -57.46748 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| b534090e-67a6-30b0-9dcc-30ef5cef180b | -16.98983 | -57.47055 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 488c5fb8-c97c-314e-ae11-bbddf95ffd27 | -16.98923 | -57.47362 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5f5d6c00-f5f3-3290-88b4-801aba633e31 | -16.98785 | -57.47332 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 410861e0-d655-3d2f-9d58-a363513257f2 | -16.9746 | -57.44159 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7779d432-12aa-3762-8748-a3cd620a77cc | -16.97399 | -57.44464 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 5636d97b-b4f7-33b6-ade1-3e329964b0df | -16.97338 | -57.4477 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0edb1911-1233-3f68-bd73-3da09ed6e078 | -16.96897 | -57.44353 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a4378547-956a-3f61-aa03-7b75774f8bb5 | -16.96836 | -57.44659 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6d84ccc3-5eef-3447-9882-d55c71b555d2 | -16.96579 | -57.43324 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a8f4e9b2-a8a5-3ffe-8821-7d4c44cb38f6 | -16.96517 | -57.43629 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 682ce584-cdc6-3820-8f6e-d0cd12c7e600 | -16.96395 | -57.4424 | 2024-10-11 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
