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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd59e5c4-51ff-33ae-976f-f3fb8430640e | -8.55533 | -63.01351 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b5f9595-e257-3c10-8e62-7aeae82cb68c | -9.07178 | -65.43087 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 570bd7e1-71e3-3a42-a62d-e3af11d20435 | -9.07333 | -65.43107 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68f04e00-5e43-3c3f-8664-39fbb279c9dd | -7.58336 | -61.62977 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c2af90a-7a32-3da7-a4d9-47eb6f32ff75 | -8.22573 | -62.9393 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0793ddef-eee2-36be-925c-858c12899a4c | -8.06046 | -72.35297 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aff544c3-a028-3620-bc34-d3609e21c8ed | -10.09122 | -68.46973 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2db67bb0-6b87-302d-8d8c-8e8e0d53573f | -8.84814 | -70.84414 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1a4ac3f-c0b1-3068-8569-4c9808a0fe4f | -8.66173 | -62.92455 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f60f8c9c-35c5-328a-b3d2-4880e646a557 | -9.86656 | -65.03142 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 948d6122-2a85-3e5f-9771-33c0f918d9c3 | -9.11474 | -61.21651 | 2025-09-01 06:14:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37147e66-95c6-36da-a5fd-6c8770ad8193 | -7.68015 | -61.08858 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 01ff4676-014c-3ef7-b1f5-df3b231db726 | -9.48376 | -65.60005 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 061e6bcf-1740-3e44-98a6-a4e3b5f8adb8 | -8.73008 | -62.41121 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 21934067-b1f5-3533-be93-160862ae20eb | -9.21903 | -71.835 | 2025-09-01 06:14:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 713dbfc8-6e98-3d63-856d-500929e6979a | -8.06378 | -72.28727 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 44f4b4bd-385b-3d2c-b9a0-85037cf36df9 | -8.83812 | -64.15173 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1544a394-3f67-394b-b21a-3163d83960ea | -9.07687 | -65.43159 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2d086395-89df-371f-b899-7e8468e039c8 | -9.06908 | -65.42435 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acad4c1a-7c20-3d4d-ae00-97d2e4bcd08f | -6.97485 | -71.74653 | 2025-09-01 06:14:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74105eb3-6a57-30ac-8a8b-a91b20661d69 | -7.69615 | -61.47583 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c293553-397a-3c4f-8010-28d085a768b4 | -8.35124 | -70.26214 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d739ca61-88ea-3c49-b075-61877afa6382 | -8.50685 | -67.12933 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f6033fc-95a8-3a09-9f9e-3f3844aef8a8 | -7.69546 | -61.4812 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3d9895a3-2f73-3d76-a52e-8e08451432df | -10.36346 | -68.59283 | 2025-09-01 06:14:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 357c77d6-82e7-30a9-8e6c-c8d305c77449 | -8.72896 | -62.41309 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 485a5bbf-e46d-30d4-b809-cc05ad30e374 | -7.93342 | -63.01371 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bf51b66-b706-331e-8e09-c10dd63404eb | -9.86609 | -65.02809 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf583061-5676-34ae-ac3a-65ac27bef276 | -8.65765 | -62.93089 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea4ed89c-1283-3b6e-9701-7a46cbd514b4 | -9.07648 | -65.43458 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dae8aec0-6b2e-3a05-b0d4-f347b5375629 | -8.75814 | -61.44072 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d72b87b7-0b2c-305e-acd2-356129c2b66d | -8.54882 | -63.01707 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 862871e3-4e01-32e5-a7c6-b3e6a2dfeb9f | -9.13912 | -65.84801 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7848c0d-5635-3677-a33b-6dc9c4cf8236 | -9.07411 | -65.45261 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4cf0f92b-372e-3b2d-b0fc-621fb9cb0091 | -7.67675 | -72.5052 | 2025-09-01 06:14:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22f966a8-835b-370a-97fe-abf7a0baec95 | -9.01117 | -65.69577 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c1df94a-4651-3478-81e0-5db25682aedf | -9.87801 | -65.02632 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b51ad03c-609b-3132-8459-f2dbf35fc21f | -9.12929 | -65.54169 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 515f3877-61d8-3613-8195-81bbee45f6f6 | -8.73019 | -62.40329 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 135f76e3-cfbc-3002-806b-6eb16669a554 | -8.24234 | -72.81769 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57e4631e-9836-3fad-8d46-b4f922b6b07e | -9.17906 | -67.73027 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb233fd4-713b-3295-bcb1-a57cf05a7b25 | -9.06701 | -65.43936 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e376f42-c15b-384c-b267-afcc363a29a5 | -8.73572 | -62.40923 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ec52d500-8bb2-377b-bca2-c1789b1b9e44 | -9.95353 | -66.87509 | 2025-09-01 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78309c2-c2ed-36aa-847f-b69b6dc1e7d2 | -8.73201 | -62.38876 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b3deb8c-782e-36f0-81b0-3a81357bb1c2 | -8.24179 | -72.82121 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22f8c651-baa5-3bba-a5e6-d12867108e0d | -9.12998 | -65.84091 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 583d0738-1efd-30dc-9d16-a71c4f3a108e | -8.72717 | -62.42738 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a452e59c-f08a-3bf5-a52c-e5292d2024f0 | -10.08284 | -68.4685 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ddcc5b7-e344-382a-a65e-4bbb5d83f61f | -9.86651 | -65.02478 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74d2ebb7-a8bf-3d00-bcc1-2d9fef17009c | -8.35426 | -70.26698 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be262386-64ff-3d63-9c28-5dfb12f7a373 | -8.74804 | -62.41113 | 2025-09-01 06:14:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a3b67e6-7550-3fc6-ad85-6831ec570af0 | -8.65167 | -62.93015 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a71dff7-547e-349d-82b6-a80df1b985f1 | -9.69205 | -65.0134 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc33b8f8-7072-3496-b978-0dbc68b32c7b | -7.34316 | -72.59824 | 2025-09-01 06:14:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4660376b-86fa-3dff-aa55-87c79be82855 | -8.76615 | -61.43052 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c2b78f7-24b1-3e1c-a536-6a98a2f18ec2 | -9.07126 | -65.44607 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e747b833-2222-3ccc-8f63-90995d8c917b | -9.06904 | -65.45191 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea5ebc43-69ce-32d9-b28e-bd0f226e902c | -7.28052 | -60.65121 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a7f01c4-daca-31e1-8104-9a8b73722aea | -6.5494 | -68.33718 | 2025-09-01 06:14:00 | NOAA-20 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fef4260-5a7f-3883-8555-e98ff23fbd70 | -9.95565 | -66.87274 | 2025-09-01 06:14:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af006cf5-c933-3d55-b3a2-e5b183ca11ef | -9.87229 | -65.02886 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 956e2573-cb50-3fb0-9bbe-6d066837b621 | -8.86997 | -71.27932 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1bed152-874c-3d85-b873-7890aebd2a91 | -8.86646 | -71.27879 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ac158bf-bb3a-3073-8cdb-557751213511 | -8.65223 | -62.92575 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5d83440-3fff-3704-bcb5-e156247f61d4 | -9.05767 | -65.43199 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6e3d136-053c-3ed7-83fd-fe68379adab6 | -9.1389 | -65.84092 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88189589-3f82-3d36-b617-29fdf4bf54a6 | -9.12423 | -65.54102 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 898e3e77-ee27-394b-a2fe-f40a5c869f14 | -9.87185 | -65.03214 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2cdb13ce-11d1-36bf-877a-98937a059048 | -8.73754 | -62.40232 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ebf5d2a-c4ed-3345-ae9e-89f4b075dd18 | -9.17471 | -67.72968 | 2025-09-01 06:14:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6828bd11-533f-38e8-809c-a13cc415b045 | -10.11746 | -68.28069 | 2025-09-01 06:14:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9a7a8a3-12ef-3df6-bb4a-e400b68d9c0f | -8.72204 | -62.42456 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 016043be-111d-311c-8439-4f6f5aacaf61 | -8.73202 | -62.39655 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 225e6c4b-6733-3e32-b15b-ca5ef588140f | -9.07375 | -65.42808 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ca823df-05e2-3017-b696-ef94b9a4bdc6 | -8.70928 | -62.41991 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50f9a2e5-268b-3560-8a8b-236eb0acec4c | -9.07032 | -65.41537 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f80e46e-ffd0-3dd4-a20c-27b57ac5b216 | -10.08409 | -68.99695 | 2025-09-01 06:14:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 630d56f0-e688-33a3-8498-bd855682a73e | -9.02762 | -70.66169 | 2025-09-01 06:14:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9386bdca-87fc-3413-b2e2-a5c279e5856a | -9.83054 | -65.05986 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23826474-9c00-3723-b4c7-6d4565b2401e | -9.13859 | -65.54897 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17c5cfb8-edc3-3241-9af3-2eb012c8b277 | -8.88212 | -69.4677 | 2025-09-01 06:14:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c4785fa-f8ab-3b86-9bbd-3a0db0361c35 | -9.87707 | -65.02631 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f2d901c-b93b-3fbf-a168-09a80e2c77cb | -7.28335 | -60.66347 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2195aa27-26bd-3e63-8121-4b4ab3680350 | -7.27894 | -60.66349 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66fed001-7761-3a38-b4ed-fdf1a2cbdc9a | -7.10841 | -63.03799 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11571170-d903-3a76-a85f-450ddd15e66d | -7.69415 | -61.48378 | 2025-09-01 06:14:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6b86aed-179c-3c44-8fcc-03d814ebffe7 | -12.42381 | -63.9136 | 2025-09-01 06:14:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 087f01db-6a2c-3545-8c5c-8a893ee258b6 | -8.72776 | -62.42264 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbc375f1-3bc0-3ffc-ab5a-7a1554de34c3 | -8.23676 | -72.80959 | 2025-09-01 06:14:00 | NOAA-20 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7065786-cfd7-3b2e-be1e-5c31639c4ce9 | -7.67431 | -61.08174 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a20b37b-60e6-3b9d-b0e4-caff6415fb48 | -8.72266 | -62.41983 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f855947-76dd-395b-ba02-0afbfc06fc4e | -8.64413 | -62.82751 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc2fab4a-c838-3564-bf10-9ba4ae957c01 | -8.7097 | -62.42291 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 974a7ffb-caf4-3523-ae19-404753ced2a5 | -8.73266 | -62.39174 | 2025-09-01 06:14:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b6ebb54-52cd-3d1d-a6fa-38e99c4194e1 | -8.65278 | -62.92132 | 2025-09-01 06:14:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 35403adb-2572-3245-8f5b-1997c86f31a0 | -9.12889 | -65.54463 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8db70464-b69d-3830-a9b7-c08a85c4fcd3 | -8.9685 | -65.96923 | 2025-09-01 06:14:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7249386-50a6-39ed-9af6-1757d12b7b5d | -7.06865 | -63.07 | 2025-09-01 06:14:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592362d7-0dcd-36da-8a4a-86abe2191b9b | -7.6794 | -61.09429 | 2025-09-01 06:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README96.md)
