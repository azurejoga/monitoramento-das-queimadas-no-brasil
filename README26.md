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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4845a0bb-ea7f-3b8e-9ead-2636228f17d0 | -18.6681 | -57.261101 | 2024-10-06 01:40:29 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 141a7d1f-c159-315a-86cc-d1eb475398af | -17.8165 | -53.754902 | 2024-10-06 01:40:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e5eed2d-d446-3fcb-9784-67c465804b0e | -17.819599 | -53.766998 | 2024-10-06 01:40:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 42952522-c09a-3e7a-89bf-0c03e15b6537 | -17.806801 | -53.7575 | 2024-10-06 01:40:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59d7be9c-b660-31ef-b4b5-82f2ba2d4381 | -17.8099 | -53.769699 | 2024-10-06 01:40:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48e96e31-4496-3782-97ee-3c3b1f4051d4 | -17.813 | -53.781898 | 2024-10-06 01:40:29 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6407aa72-a254-3088-ba70-b1962919a6fa | -18.654699 | -57.2477 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fded63e9-0c75-3774-8fa0-99de1e3aabe3 | -18.656601 | -57.2556 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 92837800-4798-36fe-9e5c-9dcb53db9266 | -18.6584 | -57.263599 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 09ed74ba-1800-3d54-8f52-7163e25fa047 | -18.646799 | -57.258099 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b81bf33c-3754-3a40-9964-a6af5d55afba | -18.6486 | -57.266102 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fc0495d0-ea3f-3229-98e4-01c76fd11e14 | -18.650499 | -57.273998 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1f5f7ae4-5bca-3f2c-9c52-da174314cb30 | -18.6371 | -57.260601 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7703c393-2065-3129-85d6-039b38560613 | -18.638901 | -57.268501 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 99878c04-f95f-32a9-99d8-381ebd903b10 | -18.6408 | -57.276402 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f65a7691-f7c1-3eff-92c1-fac6e6e3542f | -18.6427 | -57.284401 | 2024-10-06 01:40:30 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 849a2b21-bf81-318b-987e-686bc96bcb78 | -17.7971 | -53.760201 | 2024-10-06 01:40:30 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 43e922da-cb5b-3a6b-a70f-21830e33aad0 | -17.8002 | -53.7724 | 2024-10-06 01:40:30 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e2b21078-b44b-3f50-b06f-f490d1fd2bb9 | -17.803301 | -53.784599 | 2024-10-06 01:40:30 | METOP-C | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d98d4859-0cb7-3234-b1ad-77779ae07219 | -16.3134 | -51.243198 | 2024-10-06 01:40:43 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 590b0e23-9d2b-3287-8470-cc43f9127eaa | -16.318501 | -51.261902 | 2024-10-06 01:40:43 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1dd4ff6d-5f58-326d-9a62-e3bb9cd77abe | -17.844 | -57.670601 | 2024-10-06 01:40:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 512c333f-20ac-3631-9576-e31f0c622379 | -17.8459 | -57.678398 | 2024-10-06 01:40:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4729caac-c6a1-3b25-b476-622f9c246610 | -17.8477 | -57.6861 | 2024-10-06 01:40:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 31f10e9b-10ca-337c-8e2b-00be9cb0cf8b | -17.834299 | -57.6731 | 2024-10-06 01:40:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bbd3dafd-9dd7-3a7c-b687-1bd5cc2af5fa | -17.836201 | -57.680901 | 2024-10-06 01:40:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 05cfbbcb-21b7-3ae4-86b1-f7ad07ea6e4c | -17.837999 | -57.688599 | 2024-10-06 01:40:44 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7df7a670-4aa4-3b55-aa9a-a531d049b3fc | -17.007601 | -55.027302 | 2024-10-06 01:40:47 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9a83a020-4101-3f99-a525-1873f5f402e2 | -17.010201 | -55.0378 | 2024-10-06 01:40:47 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b4c8d6cc-637a-37d5-99b0-04be365a00c5 | -17.0128 | -55.048302 | 2024-10-06 01:40:47 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a52958de-6220-385f-90b0-76c805837bbf | -16.997801 | -55.0299 | 2024-10-06 01:40:48 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6e944ac5-43d1-3aa5-b792-9ffb723dcbd9 | -17.000401 | -55.040401 | 2024-10-06 01:40:48 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c6336a6b-f728-3ba0-a68e-7b810eebf1c7 | -17.003 | -55.0509 | 2024-10-06 01:40:48 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 47a0cd76-20a3-3a8a-be6a-1ae519a0d77e | -17.005699 | -55.061401 | 2024-10-06 01:40:48 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59a4a47a-98eb-3c05-84e3-ffb39a3a6c7b | -16.863899 | -54.8265 | 2024-10-06 01:40:49 | METOP-C | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5052e61e-7b55-3ca6-8101-b216780a9b7e | -17.1387 | -56.147701 | 2024-10-06 01:40:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44e7ef09-9105-3c95-b78f-1c48687385d7 | -17.1409 | -56.156799 | 2024-10-06 01:40:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1a57510a-e8c2-36c7-980d-9991114e37f5 | -17.063101 | -56.050201 | 2024-10-06 01:40:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8eba140f-1ef1-3de5-81fc-2aa633e4b71e | -17.065399 | -56.059502 | 2024-10-06 01:40:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 728ca2a4-c786-379e-8dfd-f149d3e0be2d | -17.051201 | -56.043598 | 2024-10-06 01:40:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d5711a6-eec8-3c55-954e-b556c89c1c47 | -17.0534 | -56.052799 | 2024-10-06 01:40:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f7ee07a3-ed42-3c0c-b799-01bd71bf670a | -17.0557 | -56.062 | 2024-10-06 01:40:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3045360f-d559-347f-b409-231fef634669 | -17.1444 | -56.469898 | 2024-10-06 01:40:51 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bd5e02a5-f076-35b5-b41c-eeecddee81f3 | -16.9354 | -55.824299 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0ae58a6-fbee-3b62-990e-62b468963e1f | -16.9377 | -55.833801 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5693e955-a28a-3aab-a20d-ba1b0b12cf67 | -16.9209 | -55.807701 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e64d01bd-4b2d-3c71-a046-76cef38d9cf6 | -16.9233 | -55.817299 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 12d7a006-d040-369e-99ae-f6073214cb4d | -16.9256 | -55.826801 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66bddb2e-be2c-3dd4-a715-3a69168dbfcc | -16.9279 | -55.8363 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 36886728-9901-3cce-9866-92f53be5fb04 | -17.1486 | -56.7449 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1266bfef-a937-30d9-a3fd-d49498c4e70f | -16.9135 | -55.819801 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e4f72c53-b983-305f-876a-d21665753333 | -16.915899 | -55.8293 | 2024-10-06 01:40:52 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e2352ac-a1e1-336d-bfc2-921518d52cac | -17.1367 | -56.738899 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a7171cf-40a6-3ba4-a34b-c4364e6769e8 | -17.1388 | -56.747398 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07262c7b-31fd-3d36-a86a-d7624be85932 | -17.1409 | -56.756001 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c3e34f4-e52c-35b5-8efe-4c18dc532c8b | -17.131201 | -56.758499 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dbf0ac60-3164-33af-a73a-b8bbe12e4f83 | -17.1152 | -56.735401 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 430482e4-6c7a-3fab-aa5a-ab52892aa380 | -17.117201 | -56.743999 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6fbd0f9c-8b4a-3b07-9f15-688a09a986c5 | -17.119301 | -56.752499 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b784d18e-6497-32e6-b3c9-c2c4cc3dd796 | -17.121401 | -56.761101 | 2024-10-06 01:40:52 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a6abf28-e0df-3f5e-a506-37f117c42306 | -16.959801 | -56.136002 | 2024-10-06 01:40:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f1b80f76-e87a-3fbb-9978-446babc82e50 | -17.089001 | -56.669201 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6d81e21f-01ed-38e5-8a71-2354d17903c5 | -17.091 | -56.677799 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 407953f6-2730-324f-b0e0-0a0bf2bbc6c6 | -17.105499 | -56.7379 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc0ac5de-887b-3135-8991-eb1667afdcbc | -17.1075 | -56.746498 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4f6f8c0-766b-34a0-8d0d-308dac90dd93 | -17.1096 | -56.755001 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 703a7117-431e-33c7-87e3-b5f55d6629ef | -17.1117 | -56.763599 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 568a166a-0e95-3935-85a9-9bf8ba369541 | -17.113701 | -56.772099 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 793f9ec0-3e93-3b24-9043-ba9f240625af | -17.1157 | -56.780602 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 996f28ed-3107-313a-a480-1c1352bdd8aa | -17.158199 | -56.957802 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ccfa47bc-b286-3216-9edb-bd508a27b653 | -16.879299 | -55.849098 | 2024-10-06 01:40:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 85059970-c129-328b-8873-a4fdb64b3ab9 | -16.881599 | -55.858601 | 2024-10-06 01:40:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4550691-8ac7-3feb-b71a-b57eb45e63a9 | -17.079201 | -56.6717 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f3d68c9f-d0b0-3a89-9ec5-7045421160fb | -17.0812 | -56.680302 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 466f331b-67ca-37b0-b624-79a476481ac9 | -17.1059 | -56.7831 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 487bbdc1-da59-3291-9df0-55eb6a8f0227 | -17.108 | -56.791599 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f59b52c1-fe0b-3116-b3b8-df2371a0ba8b | -17.110001 | -56.800098 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88b9fccd-ded8-3c87-b8d3-a642d1c32423 | -17.112101 | -56.808601 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 401d7be7-e404-3ad4-937e-67b37bf25ed3 | -16.867201 | -55.842098 | 2024-10-06 01:40:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 404464b4-cc49-3c31-84f9-38e8f0155294 | -16.8696 | -55.8517 | 2024-10-06 01:40:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1f9a05c9-530a-3944-8b9d-6932e1611dfd | -16.871901 | -55.861198 | 2024-10-06 01:40:53 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3c3d01f-4808-3b4a-a044-e443d9f7aebc | -17.096201 | -56.785599 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6cd3a712-496e-35a5-a2ac-b3df9972b521 | -17.098301 | -56.794102 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 106017df-2ae9-3323-86b6-1e017f2601e1 | -17.1003 | -56.802601 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 79e571fb-9cd2-3039-835e-93b7950d41ed | -17.1024 | -56.8111 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c212f52-6079-31c4-96f2-10a570afc2d0 | -17.0576 | -56.668098 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2132045a-866b-3272-b55a-41ebd18646ec | -17.0597 | -56.676701 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15ddff1e-1a32-32d8-8928-4df023383ca5 | -17.0844 | -56.779598 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 62cf37a2-28fc-3a83-a991-a6d1cba2326a | -17.086399 | -56.788101 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 730275c1-5bf6-302e-98e0-54abb6ce597f | -17.088499 | -56.7966 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7a5bae90-607a-316a-bfb0-7d4e074e5af5 | -17.0905 | -56.805099 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0aca4fdf-5b01-3107-b967-ea9456fed179 | -17.0926 | -56.813599 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 06ee5ad6-6c8d-3749-a771-e9beff3df97f | -17.074699 | -56.782101 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b4444a6-4f52-3e28-b76c-4c4f22962b63 | -17.0767 | -56.7906 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc39433d-10dc-33b5-b064-72085d8f6c38 | -17.0788 | -56.799099 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bb49dfc1-7a85-3340-9221-0f6973ce9ead | -17.080799 | -56.807598 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ce6cf7fd-2125-30ab-b0c7-73096bff01f4 | -17.038099 | -56.6731 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b9520200-89d5-3aac-a5cb-c4eca0f65512 | -17.040199 | -56.681702 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 783d5334-1825-375c-a905-a65e8e2ad9ba | -17.0669 | -56.793098 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 557004ca-60f3-3017-a97d-2c62a21c551f | -17.069 | -56.801601 | 2024-10-06 01:40:53 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README27.md)
