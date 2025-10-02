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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 668b21a3-be86-3eed-9229-685213bea6f7 | -18.65662 | -43.69323 | 2025-10-02 04:53:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00bdb007-5ac3-3ed7-9bd9-fc59c185935b | -19.59657 | -45.89497 | 2025-10-02 04:53:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f35c38f2-b2fe-314a-b13a-c27f2f3f76c0 | -18.84523 | -43.14537 | 2025-10-02 04:53:00 | NOAA-20 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e9172626-0420-3ef9-a4db-cb1c837c297f | -21.79378 | -47.20512 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09bc38f1-a071-371a-93f7-83b562751dbc | -15.96832 | -57.23835 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1bbdfc7-7bd0-3306-a6af-bf4c386be29d | -19.71752 | -45.90839 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a77a9f52-58cd-36fa-9a68-73c706da8cc9 | -21.78868 | -47.20459 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4d1106e5-fef0-3103-b774-2c0529687245 | -20.4924 | -43.93382 | 2025-10-02 04:53:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 780ab4fb-1178-3fb0-8cdc-0ed9fdfa81f1 | -19.71902 | -45.89394 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72ce1a0d-5bc3-3361-830b-42104a2f4125 | -19.71939 | -45.89035 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58350f9e-4148-301b-9355-6b9b2aa03001 | -19.00786 | -45.00556 | 2025-10-02 04:53:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b147148e-6c4c-37c6-9d68-0fe11108db6e | -22.28347 | -46.71443 | 2025-10-02 04:53:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 53947f29-52ae-3b49-8830-5bbd7b46d19b | -17.1639 | -47.02767 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cb6232ec-8974-3293-b5ee-e61973ffa08f | -16.41909 | -52.16119 | 2025-10-02 04:53:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f86c0d7-bae2-3b8c-b3c2-3b0c8a0fd7a7 | -19.41908 | -46.811 | 2025-10-02 04:53:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a8d5542-ab29-31e6-bd96-508acefeabe0 | -19.63004 | -44.90625 | 2025-10-02 04:53:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 767d00dd-7c09-38c8-9b73-845761138d32 | -20.4931 | -43.93195 | 2025-10-02 04:53:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b7cb3229-2263-3d05-a309-2fbc4231d089 | -18.42627 | -46.53115 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f06ab1cd-53b8-376f-b56c-48a2de8ad035 | -20.87562 | -46.46194 | 2025-10-02 04:53:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15c1571b-57b3-39eb-ace6-7b2c96230d51 | -19.58403 | -49.45611 | 2025-10-02 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2706370-e3bc-33a4-b82d-3be4a926f2de | -17.09065 | -47.10858 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63451f83-331c-3a2f-9b13-16f991874d80 | -17.17781 | -47.03476 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 4bc47726-11b3-3694-a4bc-d28c178bf31d | -21.79409 | -47.2021 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e276ece6-a040-3432-8e12-613cd66b6fb4 | -22.68083 | -47.64269 | 2025-10-02 04:53:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 12afb231-18a5-31d9-8b2e-a1566afbb487 | -22.56243 | -46.78743 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 19f499cb-a3be-30b4-a9ad-0ab0222a6306 | -17.3948 | -47.17048 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e30b3ea-c4ba-3e8e-80b0-343fb0b79e3c | -19.7248 | -45.89085 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da3ae710-f641-39bf-8b64-660f781e76c5 | -19.5133 | -43.60677 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db5a78d5-4c4c-3ea9-97f4-8d374c7c9b7e | -16.18698 | -57.59478 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 381e23a9-b6bf-3469-a619-8ca965b4e283 | -18.52358 | -45.03868 | 2025-10-02 04:53:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fa3e039-b6f1-307e-a52a-e40d3b3527c2 | -21.57311 | -44.96132 | 2025-10-02 04:53:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 924c67db-eaaa-366c-9b7f-5ab899479f6f | -20.23714 | -43.88539 | 2025-10-02 04:53:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5ec167e-1505-342e-85d4-992a4b681dc5 | -18.6049 | -50.6985 | 2025-10-02 04:53:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 281ac40c-efa3-3a9e-9c67-4b61246a6dd4 | -18.61267 | -50.6997 | 2025-10-02 04:53:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63da9869-3a63-3a12-b51f-342c4d0d4aa7 | -22.5631 | -46.78043 | 2025-10-02 04:53:00 | NOAA-20 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c9f2b49e-a028-30d0-a5ff-e76eb3a88492 | -18.19691 | -43.57431 | 2025-10-02 04:53:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cd42a31d-e519-34f9-9408-14e95f318d7f | -17.1736 | -47.02882 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fb028af0-4236-314c-bf75-5d8eff6ede76 | -21.78899 | -47.20157 | 2025-10-02 04:53:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c936ed9b-f6a8-33c0-8ea4-7838f63f60be | -17.08599 | -48.56466 | 2025-10-02 04:53:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb1c1b05-0d24-3437-8f72-593f2f2994e4 | -18.52321 | -45.04225 | 2025-10-02 04:53:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01e17907-f86c-31ee-a6cc-e257aa56e604 | -17.17426 | -47.02334 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 44e1e505-18a3-38fa-add8-9801ac9653f0 | -17.18056 | -47.04038 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b3059d39-0f40-3b9b-9170-37d13ac1d53b | -19.02446 | -49.74877 | 2025-10-02 04:53:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 178eb7fd-29be-3874-b658-cd6208bb9775 | -17.17009 | -47.01708 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 308495f2-244a-327f-ac84-1b007e5ef4d0 | -20.48678 | -43.93303 | 2025-10-02 04:53:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 89f629c3-a346-3f97-b922-f8692b50ec89 | -19.88765 | -42.63129 | 2025-10-02 04:53:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8165c1a5-d449-373f-a259-ef38fb1fd39f | -20.13696 | -42.86481 | 2025-10-02 04:53:00 | NOAA-20 | SEM-PEIXE | MINAS GERAIS | Brasil | 3165560 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 30f8bf09-86a1-3081-a432-cb0c01061e46 | -18.42917 | -46.53573 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 078082d9-a887-343e-83b8-ae5bffaf42da | -20.13345 | -46.35176 | 2025-10-02 04:53:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb5dc17b-514c-3716-a186-2f94dd02743b | -19.7121 | -45.90804 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbaa3885-06a0-3f56-b9d8-1a8715564b41 | -20.1188 | -44.38441 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f08199c4-eab5-357e-ae31-21b4825539c4 | -17.97916 | -45.0169 | 2025-10-02 04:53:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d17925e-e4da-34cb-9920-70fa224bf635 | -22.57395 | -46.77863 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| aafec035-0be9-36f0-ad32-68697b5917b4 | -20.8405 | -49.43352 | 2025-10-02 04:53:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 221a4d36-2307-3f95-a429-5ed019831b38 | -20.70402 | -43.28419 | 2025-10-02 04:53:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 73c8e305-7dd5-3906-8dd7-43737c749151 | -18.17886 | -53.2785 | 2025-10-02 04:53:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56afea0d-e349-33b6-b768-44be21f95b6c | -22.57362 | -46.78207 | 2025-10-02 04:53:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| ebb455e8-37c8-3708-9e49-7e28dd5ece73 | -18.12925 | -44.00536 | 2025-10-02 04:53:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67adbdf2-2530-3f2a-98e3-e5c8d7e2fc91 | -18.505 | -44.04855 | 2025-10-02 04:53:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 359d6e22-fa95-3e33-8afd-73cc78f8f430 | -17.32369 | -49.38636 | 2025-10-02 04:53:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21eb716c-fa92-3f88-a20c-2cfec3d5effa | -20.71036 | -43.28568 | 2025-10-02 04:53:00 | NOAA-20 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d136b862-3cf9-396c-9c76-162525e9d74c | -19.71977 | -45.88668 | 2025-10-02 04:53:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| efbb047b-cd54-39d4-98dc-048f7f392ab9 | -17.03135 | -52.2415 | 2025-10-02 04:53:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ae3e44a-a8c2-3b08-a6ce-912bf86adeb1 | -18.50576 | -44.04074 | 2025-10-02 04:53:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9af27c05-19b3-3c77-916c-19b718cbff0d | -16.17283 | -57.59235 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a7e2838-5a79-3493-be8b-c6972d1e7840 | -19.70446 | -49.29192 | 2025-10-02 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6fb970b-62e9-3750-b234-b3a8a111169b | -19.70596 | -49.29465 | 2025-10-02 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fbdb2ae-4b16-3702-8e6b-d8b7304233fc | -18.17487 | -53.28183 | 2025-10-02 04:53:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 529b1dbc-3b5f-3b89-8a12-67bd7c636b47 | -17.17716 | -47.04016 | 2025-10-02 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| b912d374-a2c2-301d-a4a9-45cc97cd5e3e | -16.19117 | -57.59159 | 2025-10-02 04:53:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1eec31ef-34d1-3bab-b117-fa31b3100757 | -16.42497 | -52.17031 | 2025-10-02 04:53:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5900ee7e-e8b6-3a28-8fe4-2f10f976c7f7 | -19.85749 | -42.59259 | 2025-10-02 04:53:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 19759d23-ec8f-383d-b794-de169001b61a | -18.43102 | -46.53473 | 2025-10-02 04:53:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0259ccc7-a6c1-3c7f-9967-47741733f261 | -23.06922 | -46.70979 | 2025-10-02 04:53:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8b674ef4-e729-3ab8-b205-220a0d89c62b | -20.18819 | -46.015 | 2025-10-02 04:53:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8809e8e2-cc35-3225-8e07-203399a88fbd | -19.5191 | -43.61182 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 959a5fea-4442-3c92-a821-a32a3eb3db7e | -19.89801 | -44.93612 | 2025-10-02 04:53:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28107ec3-5d46-39c4-8d1a-50740311235f | -19.80465 | -46.50166 | 2025-10-02 04:53:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75f810c9-60b1-33e0-95a5-ea15b90cfeea | -18.60879 | -50.69911 | 2025-10-02 04:53:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c030b3bc-72bf-372c-afb6-224df4830a6e | -20.4211 | -48.86369 | 2025-10-02 04:53:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ef37c46b-bfb1-37ba-befb-d741c81c552d | -19.88948 | -42.62931 | 2025-10-02 04:53:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 60418bca-2ca9-398d-b957-e81730522144 | -19.45897 | -43.65374 | 2025-10-02 04:53:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 58c71b2b-65a1-3559-80f4-249fcf2ac3b6 | -20.10847 | -44.39566 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 131a329a-dc78-34c9-9a37-6c7e38e07f1e | -20.11223 | -44.39049 | 2025-10-02 04:53:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e7e28181-0cb9-356a-8edc-39fd6ab01165 | -19.58483 | -49.45729 | 2025-10-02 04:53:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dbab1c5d-ffb1-3599-aded-81bda77c669b | -18.17544 | -53.27797 | 2025-10-02 04:53:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fe5d5ee0-57bb-3744-b3be-6d3f384626e9 | 4.25554 | -60.02623 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38e86d9d-4a33-32a5-aa8d-bf74f02e46c5 | -0.39442 | -51.80375 | 2025-10-02 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7a43e5b-cc0d-3563-af42-e03bf88e3ac3 | 4.25103 | -60.04328 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2400fe6e-ea99-33c9-8cd7-a4c7e8add103 | 4.25489 | -60.02222 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fe6f1530-9239-3512-97a8-e864b5fba2ca | 4.25619 | -60.03024 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea5184de-7ef0-3ef3-80dd-af1a14189c4d | 4.25327 | -60.03467 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ca6a273-415b-3f94-92a7-fcf94df4c25c | 4.25113 | -60.04257 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 209f4167-afed-3058-84fe-1b75cf1d24e9 | 4.25342 | -60.03395 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9994f15e-7743-31f3-9b85-5dd2c544cd84 | -1.24804 | -54.22111 | 2025-10-02 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a347fef-8cea-38f6-ab21-358d9a2cf7df | 4.26338 | -60.02963 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7abdd049-2891-37ad-bc85-1ee480f4ca2a | 2.45937 | -60.91557 | 2025-10-02 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf9f3e4d-26bf-3d62-b373-1ae1d5fcf670 | -3.80388 | -51.31767 | 2025-10-02 05:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42094f9b-dde1-3ac9-b378-e7ae959ac556 | 4.25215 | -60.02588 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0b1eb9b-5440-3d0e-bd15-06fd1b3c6c12 | -0.39529 | -51.79826 | 2025-10-02 05:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README137.md)
