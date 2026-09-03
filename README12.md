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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0a06888-bbf6-3110-8c4f-daa202ccb45b | -12.4033 | -44.8089 | 2026-09-03 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 3ca14e3d-c062-39dc-ad31-8b4faf09f14a | -6.6357 | -59.4459 | 2026-09-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| a0f25347-fefc-3e97-b073-e1ae5b79a389 | -9.0987 | -65.3783 | 2026-09-03 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| aff10e3e-e05f-374d-b4e5-22f53c8f7c89 | -6.7648 | -59.4408 | 2026-09-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 7a47598e-96a2-376c-875c-c76e858dadbc | -6.6698 | -59.9443 | 2026-09-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 60b2f247-339c-36ae-a814-27e15d17ac1c | -11.001 | -45.0617 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 71334c11-ab37-3edc-8460-eedbc7b65478 | -8.0737 | -50.9656 | 2026-09-03 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a1000d4e-7649-3912-8809-ef58e116dcc4 | -18.1699 | -51.8122 | 2026-09-03 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9d56c37f-e979-31f0-a5b2-10f588eb0138 | -9.0802 | -65.3789 | 2026-09-03 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 255f3f65-f7d1-3c55-9118-2949adbed6c9 | -9.0803 | -65.3602 | 2026-09-03 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 47d82929-9b55-330e-9a29-b4b05aea8ea1 | -8.4488 | -54.6644 | 2026-09-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ee7f20f3-6090-36cc-8237-9981de6f6ab0 | -8.449 | -54.6442 | 2026-09-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 16a2ad80-9f75-3b3d-9047-aa86434d6d29 | -6.6697 | -59.9635 | 2026-09-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 356c893f-2bc2-3440-afdf-af23a55642f1 | -12.4037 | -44.7856 | 2026-09-03 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7f0df9ff-4012-32a6-afdf-0db5eefe318f | -10.8826 | -45.3075 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 1b15b758-5d26-3e14-9a27-2a6561ea3ffd | -11.0006 | -45.0847 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 578c0c0a-4556-30d4-a0cc-fe82cc1c62bc | -6.3051 | -56.064 | 2026-09-03 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 33be1f94-0463-36e2-a394-a291424ccc6b | -6.6882 | -59.9628 | 2026-09-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2b33e789-799b-3725-b305-07f18be2df25 | -6.3052 | -56.0442 | 2026-09-03 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 1bb53656-ddda-38dd-b7c6-4036234e005e | -6.6542 | -59.426 | 2026-09-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 19630831-afc1-370f-9765-e48d8fba990c | -8.4863 | -54.6417 | 2026-09-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5b68bbca-6c3b-39ff-b665-dc44539190ba | -6.3236 | -56.0632 | 2026-09-03 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 3891da6b-6d3c-3aac-9592-221ca81ed752 | -6.6883 | -59.9436 | 2026-09-03 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 1dca36f9-a526-36e9-a62e-3109a643501e | -3.2486 | -47.2438 | 2026-09-03 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c269ad36-6142-3ff4-b95d-d14bc3248500 | -11.0003 | -45.1078 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ea69e81a-f3a5-3fc5-a6ad-43fd5a29c39e | -6.3237 | -56.0434 | 2026-09-03 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 932c331a-cc47-366f-8e71-cfd8d29ce9ac | -18.1704 | -51.7904 | 2026-09-03 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 562c6df5-2b45-3218-9970-cec3704ef9fe | -8.4677 | -54.6429 | 2026-09-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 205.2 |
| fb5ac92e-fa9e-3038-b408-64518d613e4f | -8.4675 | -54.6631 | 2026-09-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.9 |
| 2722a016-784f-38a9-8966-da7fcf3d0b35 | -6.4208 | -58.3137 | 2026-09-03 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| e91c49ae-c523-3b41-a34d-7a0fe38d0f49 | -9.0988 | -65.3596 | 2026-09-03 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| abb87741-edb3-3706-9529-e7aec4b24c41 | -10.9017 | -45.3049 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 90a07ad9-a5d7-34f5-b813-a02f34917c6c | -9.0415 | -65.7349 | 2026-09-03 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 7f190465-c7de-3139-8d9d-7e7bb08e7e89 | -6.7463 | -59.4416 | 2026-09-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6aadd3fb-9c14-30ac-be47-c578ed57b116 | -8.0924 | -50.9642 | 2026-09-03 01:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 78bc534f-4fab-3ade-9536-57f0a6241535 | -6.4209 | -58.2943 | 2026-09-03 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 6ee1f16b-c0d9-3fbd-bbd0-6a5d8ce37e6b | -6.3841 | -58.2764 | 2026-09-03 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 930d5715-1168-3cf0-b8fb-fe7ec770e4df | -6.4208 | -58.3137 | 2026-09-03 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 4719d1bb-a9a2-3577-b216-df2025257074 | -11.0006 | -45.0847 | 2026-09-03 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.0 |
| 07fbb080-352a-3dc7-b5a3-fc378312dcc3 | -8.4487 | -54.6846 | 2026-09-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 87348b7e-c809-3c60-b980-3309dab55a2e | -8.4677 | -54.6429 | 2026-09-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| b9a52428-ab6e-3677-8e9d-5dd48cdebac4 | -6.3052 | -56.0442 | 2026-09-03 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| e57f0141-8766-3bca-a4b5-11c5b0bc1534 | -9.0987 | -65.3783 | 2026-09-03 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 410965b8-574c-3282-8bd6-78a25df68213 | -9.0802 | -65.3789 | 2026-09-03 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| fb21bbf8-43df-3e9a-9d16-d564a756574a | -6.6541 | -59.4452 | 2026-09-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 83122914-ab1c-378a-85f2-391d6d6bbadc | -6.6697 | -59.9635 | 2026-09-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 4d6e2165-36d1-3b12-89e6-22ade07f5d72 | -6.3051 | -56.064 | 2026-09-03 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 91ba1685-3d0d-35b2-ae7c-452ad837f635 | -9.0415 | -65.7349 | 2026-09-03 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 8b423d2f-3d03-3f47-a1c5-37c67f806785 | -10.9815 | -45.0874 | 2026-09-03 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 59bc7e33-bb35-38af-b13a-12595e38b232 | -6.6883 | -59.9436 | 2026-09-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 154.5 |
| 050c9e05-431e-360f-aec2-5d892d7e61fc | -8.0737 | -50.9656 | 2026-09-03 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 423eac56-c46b-3788-9a94-d253112d5b2a | -6.384 | -58.2958 | 2026-09-03 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| bf591307-5d49-358a-a9c2-8d1229d8c6ce | -12.4225 | -44.8059 | 2026-09-03 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 860e7b4e-7569-317f-912a-75a70252c1b1 | -9.7131 | -65.0013 | 2026-09-03 01:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 0893c898-3654-38ed-90a8-37dfde9ac5b6 | -6.6698 | -59.9443 | 2026-09-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 3f047ce3-a25e-3c1b-bd4a-0843491ba156 | -6.3236 | -56.0632 | 2026-09-03 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| beb6dcb6-f18c-3918-8246-075cdbeb2ce6 | -6.7648 | -59.4408 | 2026-09-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a1488a57-1861-380b-97aa-7901362ec5e5 | -6.6882 | -59.9628 | 2026-09-03 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 0c8599f8-cfcb-3413-9226-4cb670e4f034 | -18.1704 | -51.7904 | 2026-09-03 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 5ca8fc9a-42cb-36c5-a531-7fd56120e319 | -8.0924 | -50.9642 | 2026-09-03 01:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 2d9f94fe-2336-39cb-9afb-6e2bc95c8460 | -6.1689 | -47.0877 | 2026-09-03 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 611add19-d2d9-3e37-b6d7-f7c590f53eb0 | -8.4488 | -54.6644 | 2026-09-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 5b45a32b-6267-3a8f-808a-0209729eccee | -3.2486 | -47.2438 | 2026-09-03 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| d3cc1fd3-6c08-3632-86f7-cbf769005e68 | -6.3841 | -58.2764 | 2026-09-03 01:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| bb7bafbe-3459-324f-a51b-0b0c449ebba6 | -18.1699 | -51.8122 | 2026-09-03 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 460ccc18-9e10-3bbc-86b3-71a44957d966 | -12.4033 | -44.8089 | 2026-09-03 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 339c5c1a-251f-38d7-9412-f8edaa335de8 | -6.6542 | -59.426 | 2026-09-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| c7409094-5942-3138-b687-dfcca53dacf6 | -8.449 | -54.6442 | 2026-09-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| d0224671-bc04-3983-9cd9-a95ba585e800 | -10.9017 | -45.3049 | 2026-09-03 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0c578b3c-8c26-3293-a166-e3c8e87f4937 | -8.4675 | -54.6631 | 2026-09-03 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| d56a7bb4-5061-3cac-aff1-b47b5dc5ffaa | -6.7463 | -59.4416 | 2026-09-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 13f91b00-694f-3c30-b479-ffbaf9ebda7b | -6.3237 | -56.0434 | 2026-09-03 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 414b797b-b85e-385f-9249-3281a4294e79 | -6.6357 | -59.4459 | 2026-09-03 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 22818046-722b-3ad3-97f6-cca52a503c75 | -12.4037 | -44.7856 | 2026-09-03 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0212a66d-9a9d-3e23-aeb2-5c6fca6f05a6 | -10.8826 | -45.3075 | 2026-09-03 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 62041b5c-997a-33d1-8b0e-1733be6821e1 | -10.2028 | -50.2895 | 2026-09-03 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 638b3ccb-caf4-31c1-b250-ac3306bbb362 | -10.2031 | -50.2681 | 2026-09-03 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 9cc46786-7a69-3004-9622-72aa153e42a4 | -9.04003 | -65.7439 | 2026-09-03 01:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 473c5f5d-8eb8-388d-b707-29241eb37114 | -9.09083 | -65.37515 | 2026-09-03 01:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b310cf72-69ab-3512-bb3e-1157cf58c2cf | -8.58929 | -67.1823 | 2026-09-03 01:43:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 99a053ea-8700-3e56-b057-5ba9710be82c | -9.02389 | -65.72044 | 2026-09-03 01:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| f92e0dcd-4376-35ef-a4e1-22587daf7a55 | -9.04435 | -65.74855 | 2026-09-03 01:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| ceec47e9-d87e-3b31-ad40-6b4118f0151c | -9.08409 | -65.36942 | 2026-09-03 01:43:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e7d35e6c-ce75-3631-9a44-3be1fcaad69d | -10.28613 | -68.85626 | 2026-09-03 01:43:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8665bce5-4a31-37cc-9de1-7b425cd0dd9d | -9.7138 | -65.00979 | 2026-09-03 01:43:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ab283b37-3cb4-3fb4-bf93-6da016a11b74 | -8.4487 | -54.6846 | 2026-09-03 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 695c4b15-e802-35b5-90ec-c92be1f93c45 | -10.8826 | -45.3075 | 2026-09-03 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| dca28686-6f9d-36f3-98b4-29856c8b07d5 | -6.7648 | -59.4408 | 2026-09-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| be3aa01e-1376-3399-871e-eadfd99139bc | -8.0924 | -50.9642 | 2026-09-03 01:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 5eb43d36-76ae-30ae-9c56-9baa7df93f92 | -3.2485 | -47.2657 | 2026-09-03 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 98350cdc-3dbd-3b3e-84a7-1eeec831ba98 | -12.4033 | -44.8089 | 2026-09-03 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 4a5c2115-7476-3e4c-86c4-d422cb821429 | -8.4675 | -54.6631 | 2026-09-03 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 65c65f25-6e35-3c7d-b840-6d8520858d35 | -9.0987 | -65.3783 | 2026-09-03 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7a362e90-2233-3a01-a3dd-5fb76c7ccfdd | -6.4208 | -58.3137 | 2026-09-03 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 92c773a9-6876-3cf0-aa20-7417c9035adb | -6.3052 | -56.0442 | 2026-09-03 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 06a18f01-6a04-3087-a47b-4334a24cd776 | -18.1704 | -51.7904 | 2026-09-03 01:50:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 992da0a7-b04f-3e17-91c1-988751f36b3b | -6.7463 | -59.4416 | 2026-09-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c0e86820-0766-3d74-9dcc-cb5af86ba2eb | -6.3236 | -56.0632 | 2026-09-03 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 78f1d286-bdbf-3d7e-8136-e425d8d13efb | -6.6357 | -59.4459 | 2026-09-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| eeafa82d-eea6-3bcb-a2b6-235498d8bb7a | -6.654 | -59.4645 | 2026-09-03 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |


[Clique aqui para ver as próximas entradas](README13.md)
