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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39069fea-d7c1-377c-a7a6-a52a79dbcf3a | -8.8925 | -62.3538 | 2026-09-03 16:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 251d8899-7cba-3b8a-ba63-941040a8c1a2 | -19.0944 | -57.3849 | 2026-09-03 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 9e5bcfad-c4bf-3404-a24e-8c5224040453 | -15.287 | -53.8407 | 2026-09-03 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b8b69048-130f-317a-9673-f859170a7e94 | -3.0721 | -61.0685 | 2026-09-03 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 07fb2287-b4bc-38c4-90ff-eb484f1131c8 | -13.4519 | -57.039 | 2026-09-03 16:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 4caa4bfd-7c2a-38d6-a724-ff36075245a0 | -17.0878 | -56.8534 | 2026-09-03 16:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 182.4 |
| 289df191-3923-365f-943d-1b418235b104 | -10.6472 | -61.7741 | 2026-09-03 16:30:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 194.3 |
| 86c316da-b453-3ade-8f6a-b6b10aa1bd63 | -20.8174 | -57.6709 | 2026-09-03 16:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 119.2 |
| 6325cd82-69e6-31ad-9a06-c14ed842bedb | -14.2989 | -51.7072 | 2026-09-03 16:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 1541afba-2bad-3a11-8c42-b1150ab4e068 | -3.4003 | -61.3087 | 2026-09-03 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| d145de16-97da-3bf5-ac09-480ce6634eb1 | -20.8377 | -57.6681 | 2026-09-03 16:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| cdb7e1d5-cf6b-30c4-9807-d3ea7fc772c3 | -3.4002 | -61.3276 | 2026-09-03 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 6a507456-3ebc-35a3-8668-886797002d99 | -15.2866 | -53.8617 | 2026-09-03 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 7c843d67-c2d4-39ed-8a31-9cff898d66b1 | -19.1147 | -57.3615 | 2026-09-03 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.3 |
| 5a14b434-e3f0-3046-a760-b3518a36735a | -6.6938 | -58.942 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9eef90bf-0274-3af8-8707-bcea96bedcf0 | -11.2295 | -51.2667 | 2026-09-03 16:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d9c449ea-efe4-3bed-ae6d-3fa412d71745 | -3.7645 | -61.7548 | 2026-09-03 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| f2caf554-97ec-3053-98e9-de5d6b8c818a | -9.4812 | -60.4709 | 2026-09-03 16:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 08db446a-2ab5-31eb-8375-782bc375b2e8 | -6.5486 | -58.5413 | 2026-09-03 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 38ef4153-d34e-3388-b707-c021f2002c17 | -15.3852 | -53.7652 | 2026-09-03 16:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 4673b0f1-68d9-3652-ac84-0a97335599ca | -19.0948 | -57.3641 | 2026-09-03 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 43b2d2ac-0567-3cab-95ff-2916702087a9 | -3.0347 | -61.4846 | 2026-09-03 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| dad4b3d5-a8a8-3113-a5be-549f80716e16 | -6.7453 | -59.6341 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 72e30af5-b82f-3370-835b-5b50a4347b8d | -6.7094 | -59.443 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 0fb78639-7ef8-3e39-91a0-b9aa3fbbe339 | -7.3118 | -60.5897 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 6ffeddfe-6348-3bf2-b15a-d9b46cc9887a | -3.7828 | -61.7545 | 2026-09-03 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| df8c7c0c-84ef-3817-accc-a93c987f25ea | -19.1144 | -57.3823 | 2026-09-03 16:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.8 |
| b0264574-24f1-3bbd-a223-2303bc6b74d1 | -6.6013 | -59.0037 | 2026-09-03 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 698b25ac-fa94-3d72-9a20-c326da1e60f9 | -4.2383 | -62.2349 | 2026-09-03 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| de771832-7c64-37e4-842d-fc86f19e028d | -6.6925 | -62.8493 | 2026-09-03 16:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 9366dca7-2151-3dd5-8ef0-45d7df86bdf8 | -14.2369 | -51.9498 | 2026-09-03 16:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0b41029a-763b-348e-96ab-866351103c44 | -19.1147 | -57.3615 | 2026-09-03 16:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.4 |
| 8cb698b0-cb16-31b7-9365-512378ef3937 | -3.4003 | -61.3087 | 2026-09-03 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 487f4f35-5cff-3167-bbf9-e1f2bff0501f | -3.1449 | -61.1808 | 2026-09-03 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cf59515d-4222-316d-a49f-2f4c34cc37aa | -8.9428 | -63.2797 | 2026-09-03 16:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7e7765b8-5bce-317d-ab92-6c0cb09ab8aa | -20.8174 | -57.6709 | 2026-09-03 16:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 191.7 |
| 462a0c02-8b44-397d-8d25-b6439f53eb42 | -8.6853 | -62.9307 | 2026-09-03 16:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1caeb860-e8ec-3591-ba1e-1374618e4f5e | -3.1083 | -61.2191 | 2026-09-03 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a4c6e399-3ea0-3102-aaf9-5fe785519b20 | -13.3998 | -51.4183 | 2026-09-03 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2b108e40-25b7-3127-b9e9-b4511a0ea65e | -3.0904 | -61.0871 | 2026-09-03 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 8d99b4df-8693-33bd-aadd-3ec6505c77d9 | -9.12 | -61.6011 | 2026-09-03 16:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 7faa18bb-0a31-30be-a354-f34e814045f3 | -8.9685 | -71.2595 | 2026-09-03 16:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c9592971-9493-3f68-8afb-c02f14f0b9bb | -3.4002 | -61.3276 | 2026-09-03 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 106.5 |
| e0766cad-e637-3101-a757-3e857237b25b | -11.7722 | -50.4829 | 2026-09-03 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 910b5a63-4dd5-32ea-90f9-d37e14f98c6a | -3.7645 | -61.7548 | 2026-09-03 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5bb1ac6c-6c59-3584-aa88-f40143b52d98 | -6.693 | -59.0773 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| cfa480c9-a193-33e3-b290-1222125df17d | -7.2933 | -60.5905 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2cc96571-5629-3665-8c61-4ff4baa71fa7 | -3.0164 | -61.4848 | 2026-09-03 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 132.5 |
| e31f92ef-9368-3e23-95c5-06fb43873cd5 | -19.1547 | -57.3562 | 2026-09-03 16:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 60eebc21-c92b-3d05-af35-e882aa316e5f | -19.1144 | -57.3823 | 2026-09-03 16:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.8 |
| 1ac5559a-6d28-3217-8117-8a31a4b28665 | -20.8377 | -57.6681 | 2026-09-03 16:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 193.4 |
| e0e8db40-9c9e-34dc-a32f-aeb2b4ee53c9 | -6.5486 | -58.5413 | 2026-09-03 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 8925ed84-52f0-3b94-aa2e-b1127645cb78 | -6.6013 | -59.0037 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 40dae947-f807-37c7-8a52-e35f38d21388 | -6.6938 | -58.942 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 934533f5-d36b-36ea-8a79-5316aa4283f2 | -8.6852 | -62.9496 | 2026-09-03 16:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 210b0b5c-dedc-33ff-958c-2ae7d8ae6ac4 | -6.6226 | -58.4995 | 2026-09-03 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 167d374a-2cde-3c48-a42c-2d802c56aa8e | -3.7828 | -61.7545 | 2026-09-03 16:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 771754af-2f5a-3f8a-bab8-6915835f1e99 | -3.0721 | -61.0685 | 2026-09-03 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| da9d58f3-d800-334f-8c7c-3e3112499325 | -6.7453 | -59.6341 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 10daf261-0c9c-347d-961b-03e51b7bc1a0 | -3.0347 | -61.4657 | 2026-09-03 16:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 519bb7b8-98c2-3b23-8dfd-43121b33e15c | -3.2181 | -61.1418 | 2026-09-03 16:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 128.5 |
| cbd8aa1a-0755-3793-8bb2-38d095efe4e6 | -7.3118 | -60.5897 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 48868d56-62c1-3ff3-a18c-70b08ab8abe9 | -7.3116 | -60.628 | 2026-09-03 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 666a876c-65d1-3b2d-85a1-4ba8c8bcc61b | -3.3872 | -59.3692 | 2026-09-03 16:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 32286dcd-fc4f-377b-87b8-c4c8531b4bc8 | -11.2295 | -51.2667 | 2026-09-03 16:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2cc5e508-cda5-3c45-a37f-a595b00d0787 | -13.3597 | -51.5299 | 2026-09-03 16:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 070d990a-5827-3f5b-9b31-d6a1836a8d02 | -6.7507 | -58.6687 | 2026-09-03 16:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 6a007d5a-8781-36b9-b6fb-10a1433b6878 | -3.1815 | -61.1613 | 2026-09-03 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 198.2 |
| 8d51dceb-f05a-35ff-8c9e-1ce3f8ce5619 | -3.7828 | -61.7545 | 2026-09-03 16:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 079f15b5-08d0-3ca1-bb40-97626107df4d | -6.6226 | -58.4995 | 2026-09-03 16:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| b9347565-eca5-3b81-9cb6-419782da8492 | -3.1449 | -61.1808 | 2026-09-03 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 77e23a79-e765-3108-a1a2-7abdcce14eba | -8.3717 | -62.716 | 2026-09-03 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 58b50ad5-c849-3d32-b278-3b12dd7d7e26 | -19.1144 | -57.3823 | 2026-09-03 16:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.6 |
| 788f0da4-a93e-3407-bcba-e09e0dccaeff | -3.0164 | -61.4848 | 2026-09-03 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 167.8 |
| dde3a60c-7118-3130-8195-7f6fad2a2bf2 | -3.4003 | -61.3087 | 2026-09-03 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 20847c56-6bbd-3b3d-8fbc-a84e9d27a913 | -15.287 | -53.8407 | 2026-09-03 16:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 595f2fa7-0e0e-3ee5-8a7a-04093019e169 | -7.2933 | -60.5905 | 2026-09-03 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 3166ad2f-8330-39a5-9051-581c0021ad6b | -3.1998 | -61.161 | 2026-09-03 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 5f8a9b3e-927f-3231-8b0e-6a992aaf145d | -3.1633 | -61.1238 | 2026-09-03 16:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 2cd1311a-7b3f-3f7a-aae3-50d8d4597776 | -8.6852 | -62.9496 | 2026-09-03 16:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 7d9ce969-e12e-3c5c-a71a-c754df09a9c2 | -8.6853 | -62.9307 | 2026-09-03 16:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 57884692-811c-3ead-a651-f034ae464436 | -3.4002 | -61.3276 | 2026-09-03 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 19edae3c-fe12-30c8-be5d-90284ae63610 | -3.7645 | -61.7548 | 2026-09-03 16:50:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c1a337ff-87f3-35e1-8623-455e808d2353 | -3.3871 | -59.3883 | 2026-09-03 17:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 24d63512-0680-3387-9e43-650d4acc9977 | -3.0347 | -61.4846 | 2026-09-03 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 146.7 |
| b807c954-8110-3f49-adb6-ee0fed18b318 | -3.4003 | -61.3087 | 2026-09-03 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 106bee91-2c0f-34c2-8cd1-85291bb87399 | -6.6766 | -58.7299 | 2026-09-03 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9ab38188-4a4e-3427-91ab-23eb3097a6ea | -3.1266 | -61.2188 | 2026-09-03 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 8fbbe8ed-a726-38cc-b7b1-e9ec6880e0ec | -8.6852 | -62.9496 | 2026-09-03 17:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 4092f6da-c144-36b3-b007-abb44d941338 | -3.1449 | -61.1997 | 2026-09-03 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 76a5689e-b500-39c3-8b66-71922a391ece | -3.7828 | -61.7545 | 2026-09-03 17:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 85f2542d-bef4-313e-ab0f-5fd4fd836913 | -3.1449 | -61.1808 | 2026-09-03 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 3ff60c1f-52a2-3424-b7b7-6a0eed6f0b04 | -3.7645 | -61.7548 | 2026-09-03 17:00:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| aef55f09-891a-3e98-944b-134fcbc5405b | -5.5098 | -60.1947 | 2026-09-03 17:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 428.4 |
| 67f60821-5167-32dd-8e52-725110893033 | -6.6226 | -58.4995 | 2026-09-03 17:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 0a9f8819-c8e3-3d06-a2ff-6e2abf7384cb | -10.1653 | -50.2719 | 2026-09-03 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| bda1ab37-dafa-328a-8a59-3164f012a975 | -19.1144 | -57.3823 | 2026-09-03 17:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 146.7 |
| 26221b49-dd9f-3de8-a39d-a153fb3a1851 | -3.0347 | -61.4657 | 2026-09-03 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 6fe6ba83-84c5-3698-9267-1d3fac5379eb | -3.4002 | -61.3276 | 2026-09-03 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| bc61b670-9d13-32e6-a5df-038cc882c44c | -3.1267 | -61.1811 | 2026-09-03 17:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |


[Clique aqui para ver as próximas entradas](README72.md)
