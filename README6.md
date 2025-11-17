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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d641683-dcb4-3e2c-aea7-412834478d0c | -11.89608 | -46.19693 | 2025-11-17 00:52:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 14ab815c-4329-379a-a980-64fd30b1f624 | -11.82777 | -47.60014 | 2025-11-17 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 589fa45f-441c-34d9-a970-c791549770dd | -11.20121 | -49.42032 | 2025-11-17 00:52:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a36e8c70-0e57-3397-bb54-1725e0ae09e9 | -12.70745 | -46.78352 | 2025-11-17 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 9fdfe4d3-29c5-3240-9821-a1abd8eb354d | -8.57642 | -46.48132 | 2025-11-17 00:52:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 8f699a4b-39c7-35af-8acb-8be3decb47e9 | -8.52713 | -46.07927 | 2025-11-17 00:52:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 6edc530b-8a4f-3a64-a8a1-326257b92e7d | -11.83888 | -49.22675 | 2025-11-17 00:52:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| a89610fd-e011-3ad5-88e3-02afa2c139dd | -10.95105 | -48.70248 | 2025-11-17 00:52:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 942b32dc-cbf4-3af6-a802-496c53838cb9 | -11.82503 | -47.58589 | 2025-11-17 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 59993972-bb8a-322d-902f-6529600de38b | -10.85814 | -46.7545 | 2025-11-17 00:52:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 692d0ec7-6f99-34cd-89ae-59bb89012a4b | -12.70385 | -46.76136 | 2025-11-17 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 12380fef-ab48-3afb-906d-637ebd97539d | -12.22013 | -49.61421 | 2025-11-17 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| dffc4be0-1857-3ba3-b796-0facd84178aa | -9.57551 | -49.12026 | 2025-11-17 00:52:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 4494ff35-0cbc-399a-992d-95a5ab5f0fe7 | -11.85006 | -49.22501 | 2025-11-17 00:52:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| ebecadd8-e2e1-3730-9bcb-8f181ebffacf | -11.81189 | -47.58331 | 2025-11-17 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 1a220f5f-be9a-342d-8a46-806907049b95 | -12.20306 | -54.26764 | 2025-11-17 00:52:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 534d43e7-ba00-3da9-a32b-298660631359 | -10.96551 | -44.52686 | 2025-11-17 00:52:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e5b57335-d6fa-3093-8c31-2107b73ad03e | -12.00489 | -52.46511 | 2025-11-17 00:52:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 454bc725-5755-359d-83f9-fd876e02a583 | -11.34967 | -48.89644 | 2025-11-17 00:52:00 | TERRA_M-M | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| afa7ecb0-971b-3de0-ba19-08f188caa58d | -12.22517 | -49.62103 | 2025-11-17 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8d7cb6a0-a98b-3aed-9869-48642252ce50 | -7.2586 | -48.0118 | 2025-11-17 00:52:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| c18ffe61-72bf-38c7-9ee6-40d31c56f6f6 | -12.70255 | -46.77779 | 2025-11-17 00:52:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bfe8870a-6034-3159-8b8e-cd02b1b01ad8 | -11.82452 | -47.5806 | 2025-11-17 00:52:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| eb401a7c-b9a7-3602-9094-2b8c3178e5ff | -11.70093 | -48.86248 | 2025-11-17 00:52:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 50e45445-c606-38a5-a88e-34f30cc590ca | -12.89176 | -54.72942 | 2025-11-17 00:52:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c20da200-42a5-30b8-91b4-94352510311a | -11.89173 | -46.17134 | 2025-11-17 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 69275922-0176-3e86-aecd-84a285f67d2e | -11.81754 | -45.29562 | 2025-11-17 00:52:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| bc0ac2eb-23ae-3aef-992a-991ce58a9aae | -3.7507 | -50.4269 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 1f965b73-adfa-36bb-a548-51804a6d0848 | -3.57496 | -52.10505 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d3a0f18-4468-326d-9c42-83c8746dd7ab | -3.77811 | -49.26958 | 2025-11-17 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ac3159dc-9072-3d99-b7de-781e1a5e9b1d | -2.67396 | -51.88858 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e3557958-8ea8-3a83-9232-e2e3320b23e7 | -4.71911 | -46.3834 | 2025-11-17 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 2ef3c63e-ff46-31c2-a613-99912a2100a2 | -3.47321 | -49.69605 | 2025-11-17 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 77481740-3436-316f-9ffd-08e6f6627fe2 | -4.64402 | -50.41245 | 2025-11-17 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2440d763-5a84-37ab-9f51-486a0c95ca85 | -3.83292 | -55.81003 | 2025-11-17 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 354f9d04-c996-36f5-beec-765f20390104 | -3.49407 | -54.04824 | 2025-11-17 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5b074f7c-1764-32d1-a561-20563a885ec3 | -1.47006 | -53.42178 | 2025-11-17 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b97ae6ed-37c3-3c7b-bd43-7b98be8dffae | -3.83125 | -49.80666 | 2025-11-17 00:54:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8adeb483-325e-39ca-9f26-76529b5414de | -3.39894 | -50.19606 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 31e8c099-6392-326a-b704-84b1227f2f69 | -3.3007 | -53.85099 | 2025-11-17 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a77de263-429b-3e40-be2a-caeffa3eed3b | -3.76404 | -51.07411 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3800a08f-a28e-32d4-9a3b-a61afcbd7325 | -3.01161 | -51.34978 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c6973c23-3010-373a-80a6-3215b1ce2d6a | -3.74632 | -51.81824 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0464c732-bb38-36bc-9f97-8903a1b94ed4 | -1.77246 | -56.16747 | 2025-11-17 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cfbd140e-5053-3f6c-a68f-8ce6f9e9c02a | -3.78344 | -47.74686 | 2025-11-17 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 9221f290-ad14-3be2-939a-9ae0a1024609 | -3.24418 | -50.51598 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| a07f35e4-47f3-3f43-977a-6a81d16da7ff | -3.31 | -53.84966 | 2025-11-17 00:54:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ef9f9413-d89e-37d2-8db1-7adde2db4b19 | -3.23272 | -50.48982 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 5a708021-172c-3f93-8f60-6490274b655f | -3.18362 | -50.64594 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b0da69ec-c792-33c2-93f2-e9280b9cfb6c | -3.4194 | -50.37712 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 72bcfa3b-c41d-3de4-a8c5-976613013b63 | -5.83686 | -48.83486 | 2025-11-17 00:54:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 76a027d8-3b52-39c1-b6af-2f20832b4539 | -2.94299 | -51.76425 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 70227d81-0201-3bc4-8dd8-cfb07e3ed2a8 | 1.62924 | -55.95958 | 2025-11-17 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1947d67c-1420-33f9-b5ac-8408653bc776 | -1.38441 | -53.84309 | 2025-11-17 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 849adfa7-ca6c-3741-9bde-ce3f4fd6e257 | 1.64932 | -55.87978 | 2025-11-17 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b91cad2-5290-34fb-9341-63e5f9ffdd36 | -3.34855 | -51.38276 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 91c0af7e-041c-3207-9ac9-df64dbb8703b | -2.51563 | -47.83511 | 2025-11-17 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 3b2562e3-2d96-3304-8fe8-af8dcc7d3081 | -2.24607 | -53.62802 | 2025-11-17 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| df53763e-0dc6-30d1-9867-8be3392171aa | -4.69291 | -46.31944 | 2025-11-17 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 00c64f5f-2a81-340b-a010-5caff134e959 | -4.09668 | -48.02847 | 2025-11-17 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 5d471c85-72e2-3309-8399-7fc0c56a9d7d | -5.12596 | -56.04458 | 2025-11-17 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ce756543-c307-3689-a873-5d10790ca010 | -4.57271 | -50.94359 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b995d428-3216-3ef6-a949-6704794ede23 | -3.76884 | -47.74897 | 2025-11-17 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| d0cd30e8-1d3f-3cae-954d-4dba5695a6cb | -3.65428 | -50.22771 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 74d73096-0966-3bc7-9d46-ea1b496a5c56 | -2.47442 | -50.23291 | 2025-11-17 00:54:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 28785b3f-ca32-3f34-91c6-efed0ada82cb | -3.90702 | -54.69169 | 2025-11-17 00:54:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d4bb5ee4-6cb2-368c-9d98-ebe01225779a | 1.63047 | -55.9506 | 2025-11-17 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f2a7429e-c740-3604-a2c1-3619c4684611 | -4.1648 | -50.20053 | 2025-11-17 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 7e252f30-9f8e-31a7-a56b-9db18a463486 | -2.51516 | -47.82988 | 2025-11-17 00:54:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| bf8189ea-6c1f-3c49-aa46-12f343ac3a74 | -2.91226 | -54.1643 | 2025-11-17 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5ab3552c-5db9-3eca-8565-4fd7d4434b6c | -3.57127 | -52.09921 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 52d38dbb-8922-3dd4-a1bd-ab16d364fdcb | -2.44214 | -56.28199 | 2025-11-17 00:54:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb98f673-7652-3455-9db8-ee3a0ca4d20a | -3.30614 | -50.06758 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f19c6327-ae8f-3382-9334-808c2b8c0c82 | -2.2446 | -53.61769 | 2025-11-17 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| ad4ec55d-0fce-325c-ba72-7b29aa070f96 | -2.89213 | -53.29083 | 2025-11-17 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6106d9a0-8b22-37b4-be87-b5ed1030e215 | -6.22569 | -47.24611 | 2025-11-17 00:54:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| bb3a5e1a-ff22-376e-9eff-63cbe49d95f6 | -3.77691 | -50.14494 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c13227e1-a797-3281-a13c-59650b64ffb3 | -3.186 | -50.66198 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c187f625-cfad-3beb-bb9b-5e48aee5f984 | -3.24685 | -50.50457 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 5da5e878-12ab-389e-b57e-20e16dca2c17 | -4.73274 | -46.40733 | 2025-11-17 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c9448828-e2e5-3089-8028-bbbf83b50d35 | -3.2417 | -50.49945 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 8c2af16e-da18-3b99-a93b-a9e586ed84ed | -3.23509 | -50.50641 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 176147b7-b9bf-30b3-9a5d-3e4b5c81d441 | -2.67209 | -51.87543 | 2025-11-17 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7ace8f90-5767-3056-85d7-32882b82bc00 | -3.85697 | -51.31409 | 2025-11-17 00:54:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a2c43012-d034-31a2-89f0-8c7b2deabe97 | -3.73478 | -52.66348 | 2025-11-17 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 50041541-55f6-30db-85cf-5659daa8306b | -3.46076 | -50.12189 | 2025-11-17 00:54:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ed9ea4c8-9f78-348b-8e7e-4fcf09e683ab | -3.14353 | -50.21078 | 2025-11-17 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 888d0499-2867-35c1-8e2d-175f1c595b6c | -4.94654 | -48.25394 | 2025-11-17 00:54:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| eb22af36-aba9-3340-bc01-9528b5aa900e | -2.68918 | -52.07098 | 2025-11-17 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 4315e08c-c082-3d19-b974-4bc729f14dcb | -4.40215 | -45.83966 | 2025-11-17 00:54:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 5a5c3da3-852e-31c7-b91c-946ad3312201 | -3.60234 | -55.54067 | 2025-11-17 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 83fbc0f8-53e2-3e07-8ae0-3e502fc71e41 | -4.16726 | -50.2172 | 2025-11-17 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| a6d5f744-609c-3727-998d-a4c182b8490f | -2.4318 | -52.1267 | 2025-11-17 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0c46fad6-56ab-3d82-8275-18bd1d1653c4 | -3.78252 | -47.75248 | 2025-11-17 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| a55f8e64-2245-3672-b08e-0bd086abd99f | -2.57359 | -55.30125 | 2025-11-17 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 57980fc6-be48-33e5-961c-c6df64bcb521 | -4.1554 | -50.21894 | 2025-11-17 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 75cb064d-cecb-3029-b5f3-567045ded4b2 | -4.72757 | -46.37499 | 2025-11-17 00:54:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 9f1dcd89-d530-3dbd-8e98-6335c8f67fc9 | -3.77516 | -49.24946 | 2025-11-17 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 58daad4a-d190-3106-b06e-77cb4616dedf | -2.88526 | -53.97088 | 2025-11-17 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 95b22235-21c0-390d-8728-472b8f08751e | -4.06424 | -47.48624 | 2025-11-17 00:54:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |


[Clique aqui para ver as próximas entradas](README7.md)
