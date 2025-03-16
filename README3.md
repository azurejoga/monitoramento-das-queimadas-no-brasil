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
| d338e636-df45-3a09-8775-f7facda47b27 | -15.6389 | -57.312 | 2025-03-16 04:53:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a7aabea-763a-3806-996b-a282cab39a9b | -20.09292 | -51.11085 | 2025-03-16 04:55:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b573bc8f-071d-3c82-be9a-8390f975da0c | -20.72894 | -56.04548 | 2025-03-16 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4c30541-0331-390b-8553-adcb45920ac0 | -17.78131 | -54.28732 | 2025-03-16 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ec351d1-5998-3409-b5d4-0aa8414e32ed | -19.48611 | -54.8497 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52fd195a-bc86-3085-86c9-8c97a69e16c0 | -22.13253 | -51.45649 | 2025-03-16 04:55:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6042c339-eba3-3106-9dc9-30fd41bd7546 | -19.34855 | -50.47978 | 2025-03-16 04:55:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14fe2288-de64-3215-8e41-1fe25654dc6e | -21.89579 | -55.37357 | 2025-03-16 04:55:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6404961-bc2b-3cf3-8109-a18124278336 | -22.54174 | -48.81207 | 2025-03-16 04:55:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90a4464a-04c4-3d72-a031-e5638e307222 | -19.49334 | -54.84711 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ee7a7d6-f1be-38b3-b949-8a133959755b | -20.73287 | -56.04192 | 2025-03-16 04:55:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1d529ac-ecd2-3ae5-b95d-36d98cd7b83e | -19.49 | -54.84658 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17325fff-e7d7-3d26-a420-ce82d2faa782 | -19.02418 | -57.6203 | 2025-03-16 04:55:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 63146794-51f7-30e4-ae73-17e106d266f5 | -19.48278 | -54.84913 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7439880e-e434-378c-b5d0-32507ae52691 | -20.41222 | -51.35653 | 2025-03-16 04:55:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 28826bc7-7ce3-3821-baef-d99409d10fd6 | -19.48555 | -54.85337 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3fb0489-c5aa-3020-8305-4cd370c62be4 | -22.13231 | -51.46063 | 2025-03-16 04:55:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a8ef339c-18c2-3ed6-ba35-351f435920b4 | -19.48888 | -54.85391 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bd21ee2-978e-342a-82a7-7975bc7d5a9a | -21.38517 | -56.19757 | 2025-03-16 04:55:00 | NOAA-21 | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 644c6515-fc74-3890-a646-e16e355a94c2 | -18.53801 | -56.17558 | 2025-03-16 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9c81154b-fbb3-3c4c-8703-dea13fd6c0a5 | -18.37126 | -55.70565 | 2025-03-16 04:55:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 34e3b18b-66fc-3c18-8872-de86fb664942 | -19.48944 | -54.85024 | 2025-03-16 04:55:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fc64445-01f0-363f-b104-e406cf4df504 | -30.45763 | -54.63597 | 2025-03-16 04:57:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 368a480f-e265-32d8-bba1-86650c1e636e | -29.77929 | -51.17847 | 2025-03-16 04:57:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.4 |
| 7eddf30f-55b6-362e-afe5-eea295101421 | -30.45826 | -54.63103 | 2025-03-16 04:57:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 830e4dda-9999-3de4-b900-f526533c596c | -29.86547 | -51.16286 | 2025-03-16 04:57:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 7383c950-824a-3ffe-929b-0c039c286cd4 | -29.77979 | -51.17368 | 2025-03-16 04:57:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| f5347017-a10e-31ae-84eb-24f248e038ae | -27.33829 | -50.57716 | 2025-03-16 04:57:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 94c4ca2e-14e2-3610-9a52-8f450dc32788 | -30.70731 | -54.33617 | 2025-03-16 04:57:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 38c4f9de-d7a3-3928-9896-24e9fadfa28b | -29.77921 | -51.17567 | 2025-03-16 04:57:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| 6cb1792c-eb0b-363e-a3cc-97f673450440 | -7.30829 | -55.30738 | 2025-03-16 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e6384d-c58c-327b-8d07-bbdb80f7fd5b | -9.82526 | -63.56318 | 2025-03-16 05:18:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8dc9201b-793d-3575-9016-7165e61dff4d | -10.68593 | -62.9846 | 2025-03-16 05:18:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ce658f72-5285-3e86-b5fb-b4ff69b1fbf7 | -10.1982 | -48.48972 | 2025-03-16 05:18:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c285cee5-b520-3729-b0c1-8ab85a72b5f6 | -12.08436 | -54.5804 | 2025-03-16 05:18:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0069382-65f4-3655-96f9-de0a6b77245a | -12.30264 | -47.26589 | 2025-03-16 05:18:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44f9b47a-fa4e-30e1-bc91-4465d6329f1b | -10.19878 | -48.48492 | 2025-03-16 05:18:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d12dadd5-3be4-3156-b409-5ac1998f2dce | -9.93022 | -59.90327 | 2025-03-16 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77e14eb5-ccb9-3e6f-85c1-55b8860d180f | -7.3086 | -55.30986 | 2025-03-16 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b42df719-1eed-3254-96a3-5924994fece4 | -19.49173 | -54.84877 | 2025-03-16 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3dec6dae-4b9e-386c-94b8-6f35ab869309 | -19.49152 | -54.8458 | 2025-03-16 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a2997b9-f535-3230-813f-31d524776ba8 | -15.63484 | -57.31083 | 2025-03-16 05:21:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3eabfb0c-cd6d-3385-8c6a-63a3f1565452 | -15.63961 | -57.31398 | 2025-03-16 05:21:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 180c0571-637a-32bf-8682-9645dd142e2f | -18.53759 | -56.17454 | 2025-03-16 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7f9497e2-f56c-3972-8587-3fd6e1d1d9d7 | -19.48658 | -54.853 | 2025-03-16 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a63ae49-c25b-3e34-abee-4119ba96b78e | -15.63854 | -57.31145 | 2025-03-16 05:21:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 845a33e8-c767-3f9d-ae09-0084407e4a0a | -18.36988 | -55.70609 | 2025-03-16 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7cd116dc-a598-36a5-9fc9-03f1921dab79 | -17.7091 | -54.07952 | 2025-03-16 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de5f04d3-7545-3dd8-9016-d0bef298f066 | -15.6342 | -57.31527 | 2025-03-16 05:21:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7e63a61-1f6c-3d2e-bb4b-5f83cf8de3d0 | -17.71379 | -54.08011 | 2025-03-16 05:21:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c192560-608a-3e96-b941-88e655df2cd6 | -19.491 | -54.85034 | 2025-03-16 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12772141-3cce-3a72-a6da-df8a71e9175f | -19.48713 | -54.84847 | 2025-03-16 05:21:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f60b7faa-8a3d-377e-9a36-895484427243 | -15.63112 | -57.31022 | 2025-03-16 05:21:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0c85c95-5493-38c0-9401-877f10793948 | -15.63791 | -57.31587 | 2025-03-16 05:21:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9f9d4d1-7437-320d-9120-1cc1332316ce | -21.89518 | -55.37175 | 2025-03-16 05:23:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ff946f8-6248-3911-93b4-e3f56611cdf0 | -21.89421 | -55.37447 | 2025-03-16 05:23:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9e3c7cb-4b96-35b0-bcc9-376bb233ef09 | -27.33183 | -50.57483 | 2025-03-16 05:23:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4b69eab0-5484-3393-9a58-44d75ce5a906 | -21.38429 | -56.19525 | 2025-03-16 05:23:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c62e8eee-102b-3850-a8bc-936ed797daf9 | -25.30243 | -54.29243 | 2025-03-16 05:23:00 | NPP-375D | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 772a46e3-8900-3db7-a72f-4ba550d3be7a | -25.30214 | -54.29563 | 2025-03-16 05:23:00 | NPP-375D | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 32dac1a9-9a49-3996-b0a9-83fe1b12dd7f | -27.33833 | -50.57536 | 2025-03-16 05:23:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6b9827da-a9c2-33d9-b696-1b496cce76e1 | -9.93084 | -59.90331 | 2025-03-16 05:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00a2d341-081d-3a30-ba18-55fd149ebb89 | -9.82336 | -63.56426 | 2025-03-16 05:40:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b5f3dfd-de08-3fc0-b38f-25f87f2be2d4 | -12.47194 | -44.32298 | 2025-03-16 05:42:00 | AQUA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 418bf216-1a89-34ba-ad2b-c6b67104543c | -15.62975 | -57.3103 | 2025-03-16 05:42:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df450239-0110-39d0-af2e-9fb3e3b10d97 | -12.16111 | -63.66014 | 2025-03-16 05:42:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 730206f2-36d2-35a7-818d-ce3d6bfdc369 | -15.63602 | -57.31503 | 2025-03-16 05:42:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cc52dc1-f48c-3336-a3b5-be0b9a942dd4 | -15.63531 | -57.31121 | 2025-03-16 05:42:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3911da89-9f51-36af-906b-1b18a126afc1 | -15.63087 | -57.31055 | 2025-03-16 05:42:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5c31292-f0ed-377f-9d45-7afc8c107c7e | -15.63492 | -57.3148 | 2025-03-16 05:42:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acd09c5e-fff6-31df-a979-10b5e3f477b8 | -15.63046 | -57.31414 | 2025-03-16 05:42:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3a24391-c0ca-39cc-88fb-3a2703d29f47 | -19.48045 | -54.84637 | 2025-03-16 05:44:00 | AQUA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3384a4c-bbf5-339b-b067-9f7faaef2073 | -19.48622 | -54.85377 | 2025-03-16 05:44:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bcb3d45-130a-3303-ba5f-1bf68f2955c9 | -19.48896 | -54.84985 | 2025-03-16 05:44:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0b5a8ae-f40f-3a84-9b0c-29e3472f0cb5 | -19.48852 | -54.85524 | 2025-03-16 05:44:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dd58af7b-7876-3abe-927d-e62a8727ad50 | -6.95709 | -38.57756 | 2025-03-16 12:04:00 | TERRA_M-T | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b3f4ad66-6a5f-3eb4-a929-5bc1d54f4e37 | -4.11567 | -41.50576 | 2025-03-16 12:04:00 | TERRA_M-T | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9fbca749-2cae-345a-8a2a-543ace885eb9 | -9.90687 | -38.11184 | 2025-03-16 12:04:00 | TERRA_M-T | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 32792d98-d63c-33e1-8db3-650dda47a9c2 | -9.56344 | -38.03611 | 2025-03-16 12:04:00 | TERRA_M-T | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 84cf2883-6033-31f4-b2b9-a3a43a029f1e | -10.57186 | -38.42096 | 2025-03-16 12:04:00 | TERRA_M-T | CÍCERO DANTAS | BAHIA | Brasil | 2907806 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 01b41e80-cc74-3515-be51-8200e660726f | -9.90832 | -38.10141 | 2025-03-16 12:04:00 | TERRA_M-T | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 8094ad7a-e155-3935-a507-a43459da3bfe | -7.73496 | -37.6274 | 2025-03-16 12:04:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 62ed195d-bc09-3842-b656-1b27626f06f9 | -17.67058 | -45.57442 | 2025-03-16 12:06:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 149a520a-4d73-3a92-8c1c-cc50e54e6f4a | -11.75286 | -38.14558 | 2025-03-16 12:06:00 | TERRA_M-T | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 0cd8d1c6-166e-36af-887b-144fc6d65612 | -14.03657 | -41.38299 | 2025-03-16 12:06:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3e70f59e-2de1-39f8-931a-718dc62fcde6 | -17.66068 | -45.57274 | 2025-03-16 12:06:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 33fff91e-03cb-3572-a414-44c7c0606c3d | -15.70385 | -39.24739 | 2025-03-16 12:06:00 | TERRA_M-T | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 466cfc65-4f14-3bf7-aee4-13a2d4266c28 | -18.60796 | -39.82263 | 2025-03-16 12:06:00 | TERRA_M-T | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 43e8db75-38cd-3436-bc5e-899ad5a6961b | -16.79947 | -39.70744 | 2025-03-16 12:06:00 | TERRA_M-T | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 578fd281-f895-3dda-ba55-2177faf3f780 | -17.61266 | -40.58227 | 2025-03-16 12:06:00 | TERRA_M-T | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 216de03e-5efd-38fa-bb55-a4ff89853578 | -12.55127 | -40.22117 | 2025-03-16 12:06:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 33c89a9c-d07f-34c8-812e-1258b315ac2a | -14.03527 | -41.39203 | 2025-03-16 12:06:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 81169237-226e-3976-b5b5-19e06255d407 | -14.80977 | -39.6729 | 2025-03-16 12:06:00 | TERRA_M-T | FLORESTA AZUL | BAHIA | Brasil | 2911006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b55120da-df96-3ed4-9977-a552c8b135d0 | -17.6634 | -45.574 | 2025-03-16 14:00:00 | GOES-16 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 866b7d0f-a49f-32b0-9ed0-ab36c9ba222d | -21.731 | -54.0174 | 2025-03-16 14:30:00 | GOES-16 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| ca2fa9fc-6d5e-3577-9d22-c08321b813c8 | -17.6634 | -45.574 | 2025-03-16 14:30:00 | GOES-16 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 87.8 |


