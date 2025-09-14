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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0e15dd6-8094-3984-b302-799d8e12767e | -14.20072 | -46.18114 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 573702a1-c124-35bd-ab46-dacc54cc746d | -15.64046 | -44.37818 | 2025-09-14 03:28:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 33eafc1a-3d7d-3289-a41d-8fd0037d078b | -17.69493 | -42.56237 | 2025-09-14 03:28:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 38d5caf0-f67d-3a2c-b580-fbfdca87531c | -14.19376 | -46.17948 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c7294ba3-c7be-3639-9905-b0e28a53078c | -10.60339 | -44.33865 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 09adc254-b9ff-3063-9f90-2445bc2fcdba | -14.20013 | -46.3353 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0500ae13-423c-36d4-8029-e9220c77e0ac | -15.4413 | -47.35754 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c35a1f54-54c1-3f40-880e-46091be9855c | -12.10007 | -44.86413 | 2025-09-14 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bdc6809-1e9d-38a0-804c-4c5458d28e92 | -13.93397 | -44.8612 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a4c24103-dc84-343a-883e-27dbb7bf8f7a | -14.4352 | -43.20012 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8edcb739-8d18-3d67-ac6a-64c5d74bb25d | -13.28874 | -43.78365 | 2025-09-14 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ed15182-be88-3eb8-83a6-c853a1feeb08 | -11.49195 | -43.64006 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1e56a1d-3e97-32b5-9eb1-58c3020cdd35 | -14.16936 | -46.15765 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04c8d068-a6f0-3d10-ab85-157f1ede1aed | -14.31404 | -46.08956 | 2025-09-14 03:28:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2d409b8-0f15-3577-8a42-b22787b5cf53 | -11.39868 | -43.52866 | 2025-09-14 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af3cf1fa-8cb6-38e4-9332-fb8e4ac2a703 | -11.09461 | -38.52552 | 2025-09-14 03:28:00 | NPP-375D | CIPÓ | BAHIA | Brasil | 2907905 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d4b485dd-5a93-3dff-b6cc-9808a00398c9 | -13.28284 | -43.79111 | 2025-09-14 03:28:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f5e843f-c6bb-3350-b3cc-e7ff31ae654f | -14.6291 | -46.36866 | 2025-09-14 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7740546a-6fda-3e76-9f48-b30d1869110f | -13.93609 | -44.84491 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3044b881-da67-321a-8916-dc20810f2bed | -12.0842 | -44.7374 | 2025-09-14 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75883c19-2b2d-367b-9117-b50721729a52 | -10.59793 | -44.3311 | 2025-09-14 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| eb6f552b-aeb2-328a-ba72-74cf09e235a4 | -12.08554 | -44.73091 | 2025-09-14 03:28:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7cd4cfe0-f33c-30e5-acd1-583d564f9be7 | -12.1028 | -44.85777 | 2025-09-14 03:28:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d6b07407-453a-3702-aec2-00fc20694fcd | -14.75976 | -45.28072 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3da883bc-0108-3be5-96f8-e9f86a00de67 | -13.92712 | -44.85488 | 2025-09-14 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0da17672-b94d-3d28-b36a-ae26f00073dd | -14.43341 | -43.20881 | 2025-09-14 03:28:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18a9e687-6b6f-3aa8-8114-6a7778af3769 | -16.52505 | -43.75566 | 2025-09-14 03:28:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52869ad1-1172-3dfd-b5a2-9056fbde9881 | -14.19684 | -46.16563 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9699f3e-2835-3e12-97dd-02c7d7383a9a | -15.47247 | -47.32179 | 2025-09-14 03:28:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05bad5c4-0e80-374d-a673-0bbe96beb4d7 | -14.17182 | -46.16004 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a8c8d5b2-2670-3615-ba65-d8f7574e40a1 | -14.19525 | -46.1728 | 2025-09-14 03:28:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 81e6f2c5-dadd-3ced-9615-eee5e7553150 | -12.7675 | -48.0013 | 2025-09-14 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7254d582-6987-309a-b73d-573bc1d08d24 | -12.7671 | -48.0236 | 2025-09-14 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| b2455700-c0ad-3b76-bf68-15671a14a337 | -22.2133 | -48.338 | 2025-09-14 03:30:00 | GOES-19 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3b0f175d-625a-3125-8431-603809df784e | -12.7867 | -47.9986 | 2025-09-14 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 261.5 |
| c3e6c0ac-28d0-3d19-b022-f429710d10f6 | -12.8019 | -47.1474 | 2025-09-14 03:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| cd539d4e-fe24-334f-a9f5-07ed5e483dab | -12.8055 | -48.0182 | 2025-09-14 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7763d146-a8f3-342d-8d0c-5a3a79f9ec05 | -12.8059 | -47.9959 | 2025-09-14 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 78581133-64b4-34dd-b1da-7dfd154c8939 | -11.2888 | -51.0909 | 2025-09-14 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5a2347ec-8812-32a9-a269-0ca724386a56 | -12.7863 | -48.0209 | 2025-09-14 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| bd649979-1968-38eb-ba9c-737f1f189ca0 | -11.2885 | -51.1122 | 2025-09-14 03:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| b8a704ef-fdcf-3164-ae57-c06d0f9af66c | -17.93946 | -45.25813 | 2025-09-14 03:30:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 251cb13d-2980-3259-835c-5ea58659cd02 | -18.29663 | -45.11126 | 2025-09-14 03:30:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d987217-52d0-3ab5-8171-35bb6cc6d3a2 | -19.99637 | -46.90787 | 2025-09-14 03:30:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0df351c3-7c20-3bdc-9ecd-046c973d74c1 | -18.01793 | -46.96888 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1586ae54-2bf5-3d46-8b77-2c12957dcd69 | -17.94465 | -45.26402 | 2025-09-14 03:30:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cec7065-973a-3565-8582-6f94b3f6be26 | -19.14721 | -44.84057 | 2025-09-14 03:30:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f87785af-d545-3954-846c-0b07856b35f2 | -17.06775 | -47.16203 | 2025-09-14 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c76fc6d-934b-3d11-b797-8f87e08c27ba | -20.09002 | -43.21077 | 2025-09-14 03:30:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5dfb5bc4-bceb-3d84-87eb-1ed75390679a | -20.09413 | -43.21 | 2025-09-14 03:30:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a93173d-b5b6-3313-8e7a-b439d4e4f191 | -18.38141 | -48.34496 | 2025-09-14 03:30:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 70b01052-7fcb-3d84-bfa3-aed60b7e2c54 | -18.26117 | -46.94378 | 2025-09-14 03:30:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b817058-695b-39fb-957c-d7cbfdfdd4bc | -18.01293 | -46.95958 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef3992ae-5312-3db1-88cf-13a0d086d76a | -19.17418 | -42.66536 | 2025-09-14 03:30:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c1c881a1-ed15-39a1-9a3f-cf4a46e66b3a | -21.62809 | -46.81931 | 2025-09-14 03:30:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 71591f52-52e1-39ef-a315-38a0d9d8fc95 | -22.49568 | -47.41219 | 2025-09-14 03:30:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0c097c57-882e-3a7a-85c3-4490910a8b7a | -17.06937 | -47.15518 | 2025-09-14 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6008d22e-c1f7-34a1-a010-7a243d29dde3 | -21.92019 | -46.55955 | 2025-09-14 03:30:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6e7a17ca-aa43-399e-9e8f-62d7df68d7fb | -20.13081 | -46.87534 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47a7db5d-65ae-3962-a7bb-e382a264c425 | -22.28924 | -45.96659 | 2025-09-14 03:30:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 81aa5208-2ccb-390f-8a9d-21521d627ac5 | -22.17671 | -49.61586 | 2025-09-14 03:30:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2b16a040-5f14-392d-81d0-82dc7842754b | -18.29062 | -45.10944 | 2025-09-14 03:30:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5b8fa15-1f7b-36c7-b66f-10a929b1350a | -20.09076 | -43.2073 | 2025-09-14 03:30:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cea67f0e-25b2-3044-83c3-efd8089df58b | -17.32287 | -46.09766 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a758cc1-6a74-33fe-9093-d0575a14fd3b | -21.91529 | -46.55262 | 2025-09-14 03:30:00 | NPP-375D | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ed9cadb8-a029-3454-8092-8700cc157d37 | -20.12264 | -46.8806 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8e12122-9ada-3c8f-bc1b-e7d6cd680337 | -22.19879 | -48.35716 | 2025-09-14 03:30:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d96b44ab-6883-34a5-bb3d-09a03afdccda | -17.27834 | -46.12331 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 022f78e8-7068-3f7a-a8f9-6c49a74ea956 | -17.27975 | -46.10445 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab44c8e2-df35-3f6d-a306-8cb884f8f6fe | -19.69996 | -45.43911 | 2025-09-14 03:30:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a951d227-30e6-326b-886c-3dd26bf2597f | -17.99734 | -46.96482 | 2025-09-14 03:30:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c70d9b40-08a9-3c9d-a7a7-5fc6547e004d | -17.2701 | -46.11613 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1cc65c7e-8010-34e1-abb3-5761a5a1c1bc | -19.43685 | -42.22346 | 2025-09-14 03:30:00 | NPP-375D | IAPU | MINAS GERAIS | Brasil | 3129301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 24691ebf-f07c-35cf-88d2-5d2286648b23 | -22.17482 | -49.6232 | 2025-09-14 03:30:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e899854b-9505-3818-bfe5-04a188f4c88c | -19.17489 | -42.66199 | 2025-09-14 03:30:00 | NPP-375D | JOANÉSIA | MINAS GERAIS | Brasil | 3136108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e0a8e2aa-d162-3e82-b371-5aa90ee059e9 | -19.43036 | -47.41008 | 2025-09-14 03:30:00 | NPP-375D | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 748189c2-9ac4-3d30-96e0-db34816b3946 | -20.25029 | -47.80013 | 2025-09-14 03:30:00 | NPP-375D | BURITIZAL | SÃO PAULO | Brasil | 3508207 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1ceebec8-824d-3881-a65a-9e1a80b2d8a2 | -18.5952 | -47.20378 | 2025-09-14 03:30:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5bfa183-b81c-3ec4-bd66-115414691295 | -21.07783 | -47.11267 | 2025-09-14 03:30:00 | NPP-375D | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 305ed9cf-384e-38d2-bdbb-946a1850c7c0 | -22.22218 | -48.61047 | 2025-09-14 03:30:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 349f3219-6293-399d-a8f8-ceac2582c693 | -20.08612 | -46.89667 | 2025-09-14 03:30:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a8d8243f-335a-3634-9b91-a1f2b5c85754 | -19.09059 | -44.49689 | 2025-09-14 03:30:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c58a85df-57c2-34d2-8e70-512fe02f4e79 | -17.07219 | -47.15542 | 2025-09-14 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdde113c-0c65-3a66-abfc-30a616f72bf8 | -19.70531 | -45.44118 | 2025-09-14 03:30:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a5641a4-c4de-3525-8cf9-d8512c05b89a | -22.49475 | -47.41464 | 2025-09-14 03:30:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 90a8c0da-44b4-3671-91bd-b81ca7f92032 | -18.20018 | -47.91968 | 2025-09-14 03:30:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24ce42ff-f60f-37fb-81ae-0fa42c704d32 | -17.31666 | -46.09456 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 57e12894-876f-3610-a037-517fa2671bfa | -17.28293 | -46.10294 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a725437c-7f24-303f-9515-c371ff6ffa47 | -22.29204 | -45.96486 | 2025-09-14 03:30:00 | NPP-375D | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0eb981be-812a-3dad-9878-13a0913b9314 | -17.27467 | -46.10888 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77ff81a6-351c-3b50-8350-e8dfa4d477fb | -19.67404 | -43.11825 | 2025-09-14 03:30:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8997e3b4-5dfd-3bc3-905f-9944aa93084c | -17.31793 | -46.10113 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 984e31c8-863a-3cfe-878a-ae5ae9e46205 | -22.05335 | -45.65934 | 2025-09-14 03:30:00 | NPP-375D | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 424ee883-58e5-3ec6-89e5-a7913058495e | -18.37245 | -48.34832 | 2025-09-14 03:30:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d20237db-373a-311b-9b9c-462334cea6a4 | -19.09641 | -44.49812 | 2025-09-14 03:30:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e6477d3-8111-3788-a6df-cf1a2a08f748 | -21.62958 | -46.81307 | 2025-09-14 03:30:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d632ace8-567b-3fad-95ea-eea5d10fced5 | -18.26727 | -46.94625 | 2025-09-14 03:30:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ced56360-7d11-3e69-8e34-c0451aaff85f | -22.05072 | -45.65773 | 2025-09-14 03:30:00 | NPP-375D | CAREAÇU | MINAS GERAIS | Brasil | 3113602 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 899ca0ed-af75-39ea-9433-7f4716c3f60a | -17.07061 | -47.16228 | 2025-09-14 03:30:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b359b0e4-b1e1-3b5b-9565-4a3b62e32690 | -17.31945 | -46.09431 | 2025-09-14 03:30:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README10.md)
