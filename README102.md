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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6ce5bd7-d259-374b-bbde-9db9ef0c6e1a | -22.87786 | -48.13411 | 2025-09-10 05:08:00 | NOAA-20 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95a8f3d2-a1f2-3dc3-8cdb-6f3c931a268b | -20.37566 | -46.64367 | 2025-09-10 05:08:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7bed0bd-0471-3fd0-8ac7-73b5cb50679c | -20.05928 | -47.53683 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d3d2b00-5698-36c0-b02f-a67438424da6 | -20.89461 | -55.18199 | 2025-09-10 05:08:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d869c96-e7e2-3e31-a055-72bdab9a080a | -23.0282 | -50.10622 | 2025-09-10 05:08:00 | NOAA-20 | CAMBARÁ | PARANÁ | Brasil | 4103602 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b43265cb-16e3-3c5b-9a1c-d6106f3faa8d | -21.92112 | -45.63758 | 2025-09-10 05:08:00 | NOAA-20 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 19d4e989-7798-3914-8e6e-85995138eac6 | -20.06878 | -47.53987 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3737b4bc-e9c1-3ecb-be5e-47c3898b4fbb | -20.00187 | -47.60685 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25c75def-fdfa-32fc-8361-7784d70e2ce5 | -20.01203 | -47.62738 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44e3b584-c191-3b8b-908d-cc7c7098a5e2 | -20.00136 | -47.61235 | 2025-09-10 05:08:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 457b8046-ed97-3f00-8ae1-4017c1a71321 | -20.07087 | -47.54298 | 2025-09-10 05:08:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f145f438-f09a-3deb-a8ef-3ad6d9659a94 | -21.12306 | -47.73356 | 2025-09-10 05:08:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f67eeb24-2524-3374-98dd-286600a03aad | -12.0314 | -50.9656 | 2025-09-10 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| b30d6c33-5701-38f0-aa3d-50ec09ad825a | -12.0498 | -51.0061 | 2025-09-10 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| f4d821a6-5798-37d7-a395-22ca1e93d25c | -12.0307 | -51.0083 | 2025-09-10 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 41e48cfb-01d9-3c68-a541-e761d4f09ffe | -12.0311 | -50.9869 | 2025-09-10 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 460.0 |
| d3f7bdf2-ff00-3a6c-985f-87bc7c8fbf39 | -12.0501 | -50.9847 | 2025-09-10 05:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 9ba68568-3541-3f86-9055-862100123a98 | -15.1374 | -52.4039 | 2025-09-10 05:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5ab297ad-235d-32ae-8920-983dd04abec9 | -20.4756 | -43.9435 | 2025-09-10 05:50:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| 176e7328-e0ff-3540-91af-29c320149a15 | -9.5322 | -54.648 | 2025-09-10 05:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8fd84e0a-339f-3c9f-abd7-ddd53794921a | -20.4549 | -43.9491 | 2025-09-10 05:50:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| be95ecbe-95e5-3c26-a27a-0569e6e7ab78 | -11.77851 | -64.93496 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d51e8a85-6f10-3d8d-b8e7-e17cd930c8e5 | -12.87288 | -62.11406 | 2025-09-10 05:55:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| faccd0cb-8823-3cb6-8772-78d0ecd9a740 | -11.77781 | -64.94016 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 53adc5a8-74f6-3ec8-893e-b6c9d045bcdb | -9.80499 | -61.52538 | 2025-09-10 05:55:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfd45cbf-ef1a-31fd-9f74-fe01dbcd406d | -12.41982 | -63.89233 | 2025-09-10 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b4bc043-34e1-3b7c-83ee-4a25017c55b6 | -10.1527 | -64.24859 | 2025-09-10 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1552ac9-b239-3c49-8e30-4081c63ddbd4 | -11.77454 | -64.93438 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc215087-0850-3dc9-bff7-4c95d2d9495f | -10.05268 | -66.9921 | 2025-09-10 05:55:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e95ab344-c9de-3e30-b3b3-7a8e453f9bb8 | -10.15676 | -64.24918 | 2025-09-10 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf283468-71b2-345e-ac7f-b82d44c65f47 | -8.44705 | -72.79671 | 2025-09-10 05:55:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d1be4fe2-abdf-3597-a465-59cc149397ae | -11.78179 | -64.94071 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d2c1c86-b221-3f6a-acde-6ce5de28f757 | -12.35559 | -63.63626 | 2025-09-10 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eede5932-a5f1-373e-92f7-9736325f0cd2 | -8.7403 | -71.03693 | 2025-09-10 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cfa6dc4-72ce-3cfa-a508-b5a78da52b87 | -12.41552 | -63.89172 | 2025-09-10 05:55:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f702203b-afec-3d9d-8b10-f2809cd0af06 | -12.35501 | -63.64056 | 2025-09-10 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da75812c-65e3-3e34-999b-4cee0468682e | -8.89703 | -69.31902 | 2025-09-10 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 953bc9b1-fd2c-37a1-94bf-cb4722a8b4a5 | -9.80086 | -61.51921 | 2025-09-10 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d25e0203-4bd7-3170-b829-f25c26fa28f2 | -12.35064 | -63.63994 | 2025-09-10 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4526cbd-be1c-3ac6-a280-ddbc6eabd28b | -9.79599 | -61.51851 | 2025-09-10 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25450159-2e89-3ad7-b32a-d702cbe66ba0 | -11.07575 | -65.18464 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 891370a8-b6ed-38c5-a3de-2c570dac973a | -9.80012 | -61.5247 | 2025-09-10 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46656356-6cea-3af4-9974-1fed82fff93e | -12.87518 | -62.11395 | 2025-09-10 05:55:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fa2a8d3-ad30-3967-ad1a-e3b0e4f2e5fe | -8.77803 | -69.53497 | 2025-09-10 05:55:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a32c4058-41be-3d92-a0f7-ae4f2d89890d | -12.35571 | -63.64238 | 2025-09-10 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dfe3aba9-408d-3d1c-a7b0-943c5863a360 | -10.61051 | -68.71113 | 2025-09-10 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c36c42d0-e1c8-3327-8b09-c1e9aeabbfab | -11.07007 | -65.18737 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e43a34e5-00ea-37b4-b705-9c4c966d3be2 | -11.07395 | -65.18795 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4a26e3ec-45e0-3625-9dab-9e02e6088f56 | -8.53578 | -67.56945 | 2025-09-10 05:55:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08ef6039-8103-3dc1-a65d-5fd6f82218ab | -9.79526 | -61.52401 | 2025-09-10 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7b90edf-1575-3146-acd7-8fb35b51d305 | -11.7825 | -64.9355 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa7f26c9-ef6d-384f-8fb4-8a1ad361c7ed | -12.35189 | -63.63745 | 2025-09-10 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39e9b9d2-8a97-3f81-8e8a-bebb80994b26 | -11.07187 | -65.18407 | 2025-09-10 05:55:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4bf3267-144b-3da8-9f8a-3ff36212a1d1 | -11.79283 | -62.74208 | 2025-09-10 05:55:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb74df8f-e966-304a-b076-a17bd89c9ec7 | -7.35005 | -70.04355 | 2025-09-10 05:55:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dacd812d-17ae-32a6-9fd3-6af459169dc6 | -12.35626 | -63.63808 | 2025-09-10 05:55:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57f40c95-5787-3493-af4e-d52d34129e61 | -10.57794 | -68.74583 | 2025-09-10 05:55:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84e4525d-1825-36dd-9c89-1237c540b6a2 | -9.5135 | -54.6494 | 2025-09-10 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c72b3304-75fa-33ac-a674-297f9526c515 | -9.5322 | -54.648 | 2025-09-10 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5941c168-4216-3f76-a21a-000d2002209d | -15.1569 | -52.4013 | 2025-09-10 06:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c1bfdf81-6d41-3f5c-b103-9e0d9a9d0bb1 | -20.4756 | -43.9435 | 2025-09-10 06:00:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 141.9 |
| 4c5aad90-88e0-3908-84a5-56ed42f4bbb9 | -20.4549 | -43.9491 | 2025-09-10 06:00:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.4 |
| de5a4364-6fb8-3bd2-8d78-333bd9c5c7e0 | -15.1374 | -52.4039 | 2025-09-10 06:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| beabdaed-45e6-3d67-a56c-785abd28f7b5 | -9.5137 | -54.6292 | 2025-09-10 06:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bd58d350-3f2d-3545-9da2-1fcc7bbc9226 | -9.5322 | -54.648 | 2025-09-10 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 843bb7f1-e663-32d4-a0f1-0f3872c4019c | -9.5324 | -54.6277 | 2025-09-10 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 57e1cdfe-7baf-3feb-8a85-a36d8b3ec3ff | -9.5135 | -54.6494 | 2025-09-10 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e62fd099-0cc6-39f2-af5d-5deaaff32fb9 | -20.4549 | -43.9491 | 2025-09-10 06:10:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.7 |
| a267fb46-0a79-3e27-90a7-f886d069fb29 | -9.5137 | -54.6292 | 2025-09-10 06:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d1e06263-7d4d-3edb-9de3-3c1875cb2019 | -20.4756 | -43.9435 | 2025-09-10 06:10:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 101.9 |
| 8883dcfc-5ce8-38c4-ad5e-5551471a8cc1 | -20.4549 | -43.9491 | 2025-09-10 06:20:00 | GOES-19 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.4 |
| 84625e62-48cf-389a-a667-719ec8f98b76 | -9.5324 | -54.6277 | 2025-09-10 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 002bb73d-42b5-38cc-afed-98548dd4b2c8 | -12.0504 | -50.9634 | 2025-09-10 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| c01812c3-78cb-3261-8e8c-8f3cac4059c5 | -12.0311 | -50.9869 | 2025-09-10 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 48960db6-2260-3c23-a8ba-e45af2c2c1ba | -9.5322 | -54.648 | 2025-09-10 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 6004b17f-59d8-3a70-b9b2-33452ac82f50 | -12.0501 | -50.9847 | 2025-09-10 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 275.7 |
| 01ec87fc-fe7a-3d4c-ad9c-c93f9ac4c1e1 | -9.5135 | -54.6494 | 2025-09-10 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| b6ea9038-31f5-32a6-86b5-b1217f61d837 | -20.4756 | -43.9435 | 2025-09-10 06:20:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| 5cd681fa-d7db-38ab-bf80-c9e02b164102 | -9.5137 | -54.6292 | 2025-09-10 06:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6969104a-b318-31c9-a9f2-f5fa40b5617f | -12.0314 | -50.9656 | 2025-09-10 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 204.0 |
| 4beb4168-0b1a-34c8-8006-0a78a8fd01e1 | -12.0123 | -50.9678 | 2025-09-10 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 6b226db2-960f-3cf6-b8e0-87b45339d033 | -12.0692 | -50.9825 | 2025-09-10 06:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 29adb980-6659-3c42-bb53-921b2604f213 | -9.11773 | -68.34608 | 2025-09-10 06:25:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 438517cd-9f43-3d40-8672-a8e8af68c290 | -10.58585 | -68.40584 | 2025-09-10 06:25:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73e6516f-807e-3cdf-953f-f331d5b2100d | -8.86185 | -71.03494 | 2025-09-10 06:25:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24cb6518-d4a8-3139-977a-23d379c7a849 | -10.58653 | -68.40081 | 2025-09-10 06:25:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a96d3f1-458d-334c-a1a8-4a26e4542535 | -8.44589 | -72.79546 | 2025-09-10 06:25:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 000cb220-746e-30a0-8b98-f01da1ed0dd7 | -12.41995 | -63.89462 | 2025-09-10 06:25:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c7bcd53-d3a5-326d-bb11-73345686dfa5 | -11.77604 | -64.93914 | 2025-09-10 06:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad521735-2ce9-39dd-bd5d-e99d4738f57e | -11.7821 | -64.9398 | 2025-09-10 06:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b01fd35-1c00-3292-a299-2916ec42b16a | -8.4453 | -72.79936 | 2025-09-10 06:25:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c357fdd1-0486-3c4a-a6b4-1acc78279f46 | -8.30679 | -72.66656 | 2025-09-10 06:25:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d4464184-57a7-308c-93f1-e7dfb609a09a | -11.77659 | -64.93465 | 2025-09-10 06:25:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66ec212c-db69-3378-ad7c-3b91dd1ab612 | -6.88675 | -47.87732 | 2025-09-10 06:27:00 | AQUA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| c22f8920-02a0-3006-a814-18cd5e0d96c8 | -5.58502 | -45.0215 | 2025-09-10 06:27:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 0e655016-1a7a-306c-b72c-314aee3e8c48 | -5.5753 | -45.02473 | 2025-09-10 06:27:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b5e3dc35-a35b-3875-affa-4cdfaa770d2a | -15.13581 | -52.40986 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fba05244-4c85-3e95-8889-9560125e169e | -12.17959 | -50.61139 | 2025-09-10 06:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| bab0b674-5d20-38db-b43a-f71ba65840c4 | -15.13296 | -52.40221 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| f8e389d0-8227-364f-b7a0-558c49cec9f0 | -15.80442 | -52.26305 | 2025-09-10 06:29:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |


[Clique aqui para ver as próximas entradas](README103.md)
