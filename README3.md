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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99547b04-55f9-38ce-91bc-039f657ecb19 | -9.4071 | -60.417 | 2026-08-20 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 4008052f-19e1-3d63-a418-0a8ce6b7faac | -17.3172 | -43.6186 | 2026-08-20 00:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 7ac045aa-9f67-33b3-8645-f711eb4bc0fa | -23.0838 | -49.1511 | 2026-08-20 00:30:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 9b998253-b58b-3b7a-840c-43c9da42192a | -6.6014 | -58.9844 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.2 |
| a39316fb-a56a-3448-b45e-39b21841a004 | -8.6725 | -54.6695 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 8ca064dd-1341-30d4-970e-d6690180c958 | -11.2189 | -55.0585 | 2026-08-20 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| fc391709-2539-31c5-ba51-f0426016703c | -6.7114 | -59.0958 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| b675392e-23df-31b8-a105-cbb9928c060f | -5.8088 | -55.7095 | 2026-08-20 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 20549a05-0def-358f-9abe-598bc182d8e4 | -9.2071 | -59.771 | 2026-08-20 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| de4b88fb-4b1c-3d86-a966-446beaba5d3a | -17.3372 | -43.6139 | 2026-08-20 00:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 253.2 |
| 762b01ac-70e5-3e8a-b732-56fa3ca7993a | -6.8593 | -59.0318 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 8ad9dfd5-681d-3606-985d-c331a00d5c15 | -6.5829 | -58.9851 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| eac69462-e5bb-3bdf-ad28-ae5eb21ed996 | -14.4559 | -45.6019 | 2026-08-20 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 85ccc6a3-e380-37b3-bb70-378258962e98 | -9.207 | -59.7903 | 2026-08-20 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| aec0d606-d337-331b-820c-389cd9d95b0d | -5.8087 | -55.7293 | 2026-08-20 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 3027a535-9258-3dce-94aa-45e37a7e5542 | -17.3365 | -43.6383 | 2026-08-20 00:30:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 117.0 |
| e26b2029-c507-3bb2-a5ce-ddec1f1baba5 | -10.4513 | -54.6565 | 2026-08-20 00:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 547490d7-d49b-389c-bda9-19d655af5a53 | -6.4391 | -52.7343 | 2026-08-20 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e37b8608-df8b-3b7d-9759-58314e1b55e1 | -8.6727 | -54.6492 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 189.0 |
| d39dff70-bebb-3658-b6da-9baf42bdb427 | -18.0487 | -44.6066 | 2026-08-20 00:30:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a4f6cdd0-d876-34a0-bc74-5f3c9f6c5210 | -9.4256 | -60.4353 | 2026-08-20 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 188.8 |
| 21fa2fb1-fe23-3ae5-8643-c4551f37610e | -9.2256 | -59.7894 | 2026-08-20 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 6cd971e3-eed7-3d62-83ff-09c410d4424f | -8.5214 | -54.8814 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| da04feb1-4628-30a7-ac8b-cfa3602f784b | -9.12 | -61.6011 | 2026-08-20 00:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.2 |
| ce6acdcd-fbc3-333c-913d-27dfb631c0cc | -9.4069 | -60.4362 | 2026-08-20 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 178.6 |
| a24e6b75-6987-339d-9579-b9254b0b0eb8 | -5.7904 | -55.7103 | 2026-08-20 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| eae39d84-e1a3-3d98-895a-941f9c644f70 | -6.9128 | -59.3578 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.2 |
| c64059a3-3a3a-3b2e-9029-6d30eb6d03bd | -9.4257 | -60.416 | 2026-08-20 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 161.6 |
| 83ae4223-d105-3132-86c0-bd07f1dbcf2b | -6.7123 | -58.9412 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b86f027e-4418-37f9-90a2-6125b4e16588 | -8.6913 | -54.648 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 83eb5eeb-4872-34b1-aeea-eae3b6e95d25 | -9.12 | -51.1534 | 2026-08-20 00:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 091ed227-17e5-39c0-9348-74d19ab639ef | -8.6729 | -54.629 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 7bf14ac4-6a3f-31a6-8d29-2a76cea82bad | -7.9563 | -44.6667 | 2026-08-20 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 627cbd15-dc38-3df1-a3c1-12125402cd93 | -11.8377 | -58.8445 | 2026-08-20 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 372f48b6-8a02-38b0-94ff-8a626d5d1cf5 | -7.3413 | -45.8377 | 2026-08-20 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 284.1 |
| 4c9d424b-9a0f-344a-aa55-223bb5757a8c | -11.1939 | -53.9993 | 2026-08-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 80ebc405-2639-3281-82c4-7c674fe7e9b2 | -6.6015 | -58.9651 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 8c1847f4-3fbe-36f1-b17e-d3b72c88f6a8 | -6.4389 | -52.7548 | 2026-08-20 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| be4390f1-a4c4-3de0-927a-911f8b46e939 | -7.3603 | -45.8136 | 2026-08-20 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 323.7 |
| 682aa3eb-b958-3e78-95ed-375300d1926e | -2.5629 | -47.2445 | 2026-08-20 00:30:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 8c920162-3fb3-3265-a837-59da899c011f | -6.583 | -58.9658 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 985ffd78-4783-3170-a4a6-b708e5f7efb3 | -12.4916 | -54.7364 | 2026-08-20 00:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 260f9ee9-2e36-3e0d-b496-abbace1ffe41 | -6.3863 | -54.9451 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 07fd8097-0fdc-3544-b828-d9e8c418de5d | -11.2191 | -55.0382 | 2026-08-20 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 97c703c4-ba59-3674-bc85-ef621a492e14 | -6.6929 | -59.0966 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 4bbb5e3a-21e4-3437-b855-34ad73c4bc24 | -1.8425 | -54.4917 | 2026-08-20 00:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 127.4 |
| e8bc0801-0081-3026-b5e4-8bc9b719868b | -8.654 | -54.6505 | 2026-08-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 40afa6d9-119b-3458-9c3e-48b3feb33ef6 | -7.36 | -45.8361 | 2026-08-20 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 55a24fd3-3aa8-3433-9bd1-26bd67bff392 | -11.8083 | -44.8072 | 2026-08-20 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f3a1ed18-bc5b-3cad-8b0e-764c10f3fe17 | -7.9751 | -44.6648 | 2026-08-20 00:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| b25a280a-2127-3840-be1b-0f339754babb | -6.9313 | -59.357 | 2026-08-20 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 45257bb8-ec63-3a76-ae4a-3d97b955a775 | -8.5275 | -54.8666 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c46d1c1-319d-3280-8e49-3c72d7d79c38 | -10.5192 | -50.7878 | 2026-08-20 00:38:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| da6dff17-1773-3833-8802-223103fd0f00 | -3.0959 | -61.198601 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1088bf7f-dcc3-309b-bfc1-2171b59725b7 | -7.3321 | -45.839199 | 2026-08-20 00:38:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| beda25eb-40af-331c-94e8-5a5fc32cc7d4 | -17.7736 | -49.1203 | 2026-08-20 00:38:00 | METOP-B | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c74c457c-4d8d-34e7-b6b6-2313925809d9 | -13.4027 | -54.3675 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78230083-4d13-339e-b886-c379fbb0d698 | -9.2236 | -59.761299 | 2026-08-20 00:38:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c002b94a-e516-3e7f-a957-874e2adad2e4 | -11.1801 | -54.025501 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c5fee3f5-5df8-35f4-a0a9-7438550cb7aa | -13.5902 | -51.662498 | 2026-08-20 00:38:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed7304f-f2db-381a-90c0-4440ee1e0059 | -16.0798 | -54.965599 | 2026-08-20 00:38:00 | METOP-B | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 06a7ea4a-0e5b-3df3-a34d-e070f758825a | -8.5308 | -54.8811 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 858ba3eb-9048-35cd-930b-cd51fe405f29 | -6.3883 | -54.932899 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35419b17-124c-3280-bb32-b17f38e49db5 | -8.5483 | -54.7775 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43cf5a1d-3b56-3bd3-ad23-2cfd9206bb91 | -3.0998 | -61.2159 | 2026-08-20 00:38:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e9b5c67-5311-3e9c-8773-21dda7eb9d38 | -8.5889 | -54.729801 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b18c443-5925-3286-9e79-ffe00265d58d | -6.8081 | -58.990398 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65c415c3-126b-3612-9889-2c0e513bb78b | -8.5639 | -54.666199 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad9b6a5-6501-3c2d-ba61-1826ad7daedd | -7.3817 | -55.535599 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b40ec8b-259c-3d30-91dc-5d3fcde7239e | -7.4507 | -60.001099 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8c7641-89de-3cee-b776-25eecb6d7bda | -8.55 | -54.784801 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1206852c-da5d-39a3-828b-18c2ccdc17a2 | -8.5629 | -54.751202 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8a7664d-1cc0-3f1a-8d7b-915c74ad1449 | -11.8096 | -56.592499 | 2026-08-20 00:38:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae278a0a-71ef-3f0f-929e-aa02dc8f747e | -16.0814 | -54.972801 | 2026-08-20 00:38:00 | METOP-B | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0caef5b-d1c1-3c28-959a-ef0ff4330b81 | -23.312201 | -46.7938 | 2026-08-20 00:38:00 | METOP-B | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b68d6f16-67da-3bb3-b018-3fb7ad1bb079 | -12.4713 | -54.169701 | 2026-08-20 00:38:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd3f3566-7091-3a05-9333-9dfb482ffe5b | -8.5874 | -54.768501 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da869ba5-7dee-3982-a3d5-080c9d7c0574 | -7.6019 | -60.9352 | 2026-08-20 00:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b72204e-25d3-3a55-a366-f12ff31f9517 | -8.4964 | -54.866001 | 2026-08-20 00:38:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be697947-bebe-3cba-bf9a-065238ce9a56 | -4.505 | -55.4389 | 2026-08-20 00:38:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6020e279-f68f-3f24-927c-ab07844eaf2f | -6.2422 | -55.4198 | 2026-08-20 00:38:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 511346d3-18f6-39cd-bedc-ccee6010030d | -8.7054 | -49.607498 | 2026-08-20 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f370d974-360a-3625-8cb1-a0468f9d1450 | -10.8016 | -50.292801 | 2026-08-20 00:38:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6171e539-c053-3d43-90db-fdffb2e72bba | -6.7935 | -59.577301 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 943bf4e0-25f9-37cd-b154-3f36b186554e | -6.4413 | -52.762699 | 2026-08-20 00:38:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 322ceea5-4901-3765-8259-8676d961ddf2 | -15.1857 | -48.219398 | 2026-08-20 00:38:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ca967349-1850-39f6-83d6-8f49eeb500dd | -8.7151 | -49.605099 | 2026-08-20 00:38:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5869771d-6336-3e73-b823-241ca5801f7b | -7.7975 | -61.178299 | 2026-08-20 00:38:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d661904f-202a-38e0-8d6e-a516ebbc2f6d | -12.4841 | -54.725101 | 2026-08-20 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe08b9ea-4444-3fdf-9b05-731320e31c61 | -6.5792 | -58.9776 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6caae696-6641-3599-97a8-7e4d77856aee | -6.6935 | -58.936798 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a16ade7a-d376-36e2-8631-2f96acbf7ce0 | -17.995199 | -49.388302 | 2026-08-20 00:38:00 | METOP-B | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 370174af-9e12-3db4-82bc-c421a05c27fe | -17.992599 | -49.377899 | 2026-08-20 00:38:00 | METOP-B | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c79d8600-9f9f-3836-a18f-3700d5db837c | -13.5686 | -51.6586 | 2026-08-20 00:38:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3bcd200-417e-3c38-b983-1409551fa503 | -12.0028 | -53.433498 | 2026-08-20 00:38:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 64e40671-41c1-35c9-9558-54f9d2405306 | -6.7953 | -59.585201 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b920f219-8a20-3dd5-9029-8ee28c779165 | -11.1979 | -54.0135 | 2026-08-20 00:38:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8bfd41-5691-3b65-9945-6dd66b1977bc | -6.8556 | -59.0196 | 2026-08-20 00:38:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34ce7e39-2f87-380c-83dc-0a0982748b21 | -11.4205 | -54.309399 | 2026-08-20 00:38:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df176b21-abcb-3759-b17f-ff5b514738a5 | -7.5479 | -55.5868 | 2026-08-20 00:38:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
