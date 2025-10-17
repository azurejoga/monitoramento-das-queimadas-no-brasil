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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da7ed61b-94a4-3654-947f-e9ac4b298a68 | -11.47525 | -44.28133 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d58d9f81-46b6-315c-aa96-4e61bfc1da83 | -11.45207 | -44.23378 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eeaf3283-c432-37a0-aaa5-6b0498a65115 | -11.40304 | -44.10547 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b377e75-57ae-3be6-a966-5f453e8c5d20 | -13.12582 | -43.68603 | 2025-10-17 03:30:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 005c44f2-2ad7-3145-aa12-68a767ec242a | -9.13808 | -46.65204 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 3c6fdfa0-c353-31bf-873a-996c29863d1c | -11.485 | -44.1932 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f1e40fdc-cc73-30a3-a6c6-747a1da246e1 | -10.11959 | -44.55457 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd8af482-9309-3793-bcb5-adc5e5771370 | -11.41377 | -44.20664 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ca9e57f-4320-3689-ab34-616e6b4277dd | -10.25767 | -44.05444 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3f9ed9f-8d33-3df9-8e67-3589cdb5cb20 | -11.40213 | -44.10996 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2a68620-ed59-3d9d-ab44-868a117e9532 | -10.11299 | -44.61981 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac93c4b4-0f1f-301e-bb20-77a66ce07f19 | -10.28924 | -44.05405 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 12233c1c-14f4-3c51-94bc-7cdeb1e81dd1 | -11.96901 | -46.56231 | 2025-10-17 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a8623aaf-5380-3b3e-ad49-9ca5efcf43ce | -10.27942 | -44.07204 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 03ab510d-1188-3d47-be8d-3a1c2fe79937 | -10.28208 | -44.02628 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d71a2189-9c08-3926-a8ee-b40786e02c91 | -10.27843 | -44.04491 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2df6fcfc-a529-330e-8aff-f74d46060d38 | -10.10406 | -44.58382 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98e9afcb-b0ed-3576-9cc0-36f869df4122 | -11.47905 | -44.28733 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76d104b4-064a-3531-890d-33e4c51a6f9b | -10.42798 | -45.0222 | 2025-10-17 03:30:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c49901ea-2efc-361e-8a46-06a65062389c | -10.26649 | -44.04165 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9775d33b-4e9c-3949-bb14-13e30ca60009 | -11.40364 | -44.19498 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2a24dac7-80be-3d64-b40c-04f7016443e8 | -11.40321 | -44.22816 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3b4c34cb-9b33-3759-b7c3-a6c548ec9508 | -9.14355 | -46.66198 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| c605cd99-a6dc-30ca-abce-d74d19ccaca1 | -13.38447 | -47.21008 | 2025-10-17 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0671fc85-dc7d-38e7-ad88-f81ed8373a0e | -10.81052 | -43.94114 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27667893-42fb-3902-999f-941d03145009 | -11.96758 | -46.56898 | 2025-10-17 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 740e3f4e-5fb3-3b5e-b6ed-4a7b3262ea57 | -11.39398 | -44.21194 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38be691d-94b6-3ed0-9047-aa03530d89bf | -10.26456 | -44.05146 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25bb7ca4-ef73-314e-ad28-6547fe028958 | -12.62541 | -43.43778 | 2025-10-17 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19e7d134-c457-30bf-8a65-215194ac7dbc | -11.39618 | -44.22324 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1691cd4f-470f-3372-8be5-85e370c0b213 | -10.28229 | -44.05741 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03eb319a-fcec-39a9-ac2b-753a1a4ff5ad | -10.09782 | -44.58236 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48ebfc4-3f22-337d-b1c7-24e33ec33536 | -10.27946 | -44.03967 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5716202-35f3-31d3-ba9f-e870616a3021 | -10.29422 | -44.02849 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 55f23e96-bf0f-3d74-a616-ee98ed446ca9 | -10.17039 | -44.79386 | 2025-10-17 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 90ccf286-d211-3786-8e6e-f2d41de182c7 | -11.39577 | -44.14141 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60e1d41d-737f-3b54-a45c-e03b39d54c00 | -10.15882 | -44.53611 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d54ca881-166c-3461-898e-35d52b8f2535 | -11.45174 | -44.26709 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38ad6b5f-5b69-331f-91c4-3395c92f2f26 | -11.59113 | -44.07532 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ba088fc0-46b5-352a-a7e7-f7414728c489 | -11.45569 | -44.21549 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 303362b4-79e5-30d3-a4d1-7ada375b4e20 | -11.40687 | -44.20992 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0905673e-db7f-33bb-a481-a8cffb810edb | -14.16727 | -47.94492 | 2025-10-17 03:30:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5aa3b390-9f61-3542-95d8-c6c739d3c4b2 | -10.6618 | -44.86159 | 2025-10-17 03:30:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee728d5c-4c37-3d89-a799-9372023aa467 | -10.27246 | -44.04328 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3749ef87-538e-379d-adb9-576986e127e2 | -10.13291 | -44.58562 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 008d95f2-d533-358c-bc11-be9c5a43dcfb | -10.11468 | -44.5627 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48e03c3b-da0c-385f-b6fb-3cb49467fa8d | -11.40272 | -44.19953 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 80efaf49-4836-38c5-8ee1-672872ac99ea | -10.29743 | -44.04426 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b2ee275-cc2a-3396-b708-74e788c57c22 | -11.38014 | -44.21855 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f78be4e1-533b-3215-a606-3a7be44030ce | -10.1342 | -44.54664 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ee4b46f3-92b2-3418-ab78-4c6f393140c3 | -10.14865 | -44.53946 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e52f667d-3d75-3f99-8bca-0b9c2bb9fedd | -10.53032 | -44.50496 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ca44cb0-d411-3216-95cc-0a1e6ea0e10d | -13.70831 | -40.98952 | 2025-10-17 03:30:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 67b93752-1e60-3dc1-b120-c72ec946a856 | -10.2804 | -44.03487 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37c4b667-ae4d-31a6-97d2-afc4c61d1f4b | -10.26554 | -44.04647 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66032087-b832-3cf2-87a5-a33307474da3 | -11.58105 | -44.06392 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7a5175b3-eea6-3073-afc9-be68822275a4 | -13.26469 | -42.54591 | 2025-10-17 03:30:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bbfe6bb-80b7-363f-b917-0a8420f181dd | -10.81142 | -43.93644 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a7ad8ae-023d-3a13-b11e-0ee8bd0ea65b | -12.62209 | -43.43692 | 2025-10-17 03:30:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d78a5453-a299-34b3-b48c-3ed82708bc15 | -10.28289 | -44.02219 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be8c1532-6862-3e72-ab88-3566f726b99c | -11.41012 | -44.22487 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd890085-31eb-3619-ab32-924be545cd70 | -9.1325 | -46.64266 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9815d5c5-5d2b-35cb-8dfb-516f5090c417 | -11.48322 | -44.20229 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5d8330cf-49ff-3065-9c1b-9194d0ef0cb9 | -10.64381 | -45.25212 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a461732f-bb08-3116-a277-8001cd898563 | -10.1074 | -44.56663 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b98d267-f9e9-3d40-879f-0c240427e421 | -9.13648 | -46.66 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 23b0e569-213b-3400-9b75-8f4af00b11f5 | -10.71277 | -44.54078 | 2025-10-17 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72905ed0-f3c4-3f47-a452-a6be474e0980 | -10.28543 | -44.07357 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1819f454-bc18-351b-86de-7519b0a95fcc | -9.70939 | -44.55079 | 2025-10-17 03:30:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5934c394-c49d-37e9-839e-59d2d1a19cda | -10.17144 | -44.7885 | 2025-10-17 03:30:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 49b29c90-868b-30cf-910d-939a2cd52dde | -11.39974 | -44.2049 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87a713cf-0571-344a-a959-b5ddd0532a04 | -10.27632 | -44.05569 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bdcebc18-5080-3205-a5d8-3cf14ea13bb4 | -10.13411 | -44.57965 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7153f568-b142-3200-9500-315b055c1c56 | -11.44845 | -44.25205 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4dd0d6b-aca0-311b-89ce-d7e9600c2e4e | -12.32314 | -41.40195 | 2025-10-17 03:30:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d82f8c62-036f-31e6-99d6-11eb89de64bc | -11.48347 | -44.16928 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ec1d0eb-b0b0-3606-aec6-485e8acbc19a | -10.26102 | -44.03397 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 072976af-d9c9-3f3f-9279-c4ca5d0e31cd | -9.71244 | -44.55551 | 2025-10-17 03:30:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d917e10-d026-3d83-b0ac-cfce99751648 | -17.96752 | -39.88415 | 2025-10-17 03:32:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 09eae476-f776-33cf-bf28-29785b1ab605 | -18.20561 | -42.20429 | 2025-10-17 03:32:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 8a099765-1fac-3142-8663-fb924df60f3f | -19.06979 | -46.82456 | 2025-10-17 03:32:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cea79362-bf98-3805-b083-40bd5c89e500 | -19.21249 | -44.11638 | 2025-10-17 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ce86d7d-1424-37ba-a423-cea1616ceaf4 | -18.20719 | -42.20612 | 2025-10-17 03:32:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9445287-f8f2-35df-a700-e8af16fef7c8 | -17.35602 | -39.42688 | 2025-10-17 03:32:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70be42e5-b9c4-3f49-bac5-563cccc0f339 | -18.09349 | -42.45002 | 2025-10-17 03:32:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d1be21fa-063d-3e9d-b8ca-d3a9c67dc285 | -16.02203 | -43.49458 | 2025-10-17 03:32:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 549b1e21-af8f-3ebe-bdc6-4b2c556f8c2e | -17.38932 | -46.65617 | 2025-10-17 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbff3921-2d60-3c99-89dc-29bdd7365e8b | -16.61366 | -43.36502 | 2025-10-17 03:32:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a93ec0b-45ef-3e6f-a77c-f24726b4c4bc | -18.20243 | -42.20559 | 2025-10-17 03:32:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9ace0f75-a4b6-3b51-a570-b6ec84c0a30b | -19.07588 | -46.82597 | 2025-10-17 03:32:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad53a9b3-5afd-3581-b502-1457b3ee57ac | -19.91077 | -45.89514 | 2025-10-17 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b78a4465-ee66-3d3c-bada-63a18ed95f1d | -20.03288 | -44.0764 | 2025-10-17 03:32:00 | NOAA-20 | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 652adfd1-6f17-36e8-89f9-fd5bf19e514c | -15.78291 | -43.65639 | 2025-10-17 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0222d65-fdeb-3654-bdad-4a8c0b231a7e | -16.19617 | -43.67837 | 2025-10-17 03:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c1bb41-49f0-3091-bfae-bee9fecae7d1 | -17.39048 | -46.65103 | 2025-10-17 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14b91cb0-71b1-37c0-a8e8-9c8869c31b5a | -19.21762 | -44.11771 | 2025-10-17 03:32:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 915e7e85-00a1-31ef-b579-e9a9cc013ac6 | -15.78502 | -43.64605 | 2025-10-17 03:32:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8819b3ca-dc8b-3b41-89e6-9a71421a90a3 | -19.83636 | -46.03441 | 2025-10-17 03:32:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92b922de-bdf7-3bb0-b7c6-8bf838d4a66d | -19.83724 | -46.03046 | 2025-10-17 03:32:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a89747cc-67f1-3bb7-ad30-2911cd74c201 | -17.9682 | -39.88041 | 2025-10-17 03:32:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |


[Clique aqui para ver as próximas entradas](README33.md)
