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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43d58e01-8fa0-3427-83f6-9c872b3db57c | -14.72168 | -45.56788 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6625f973-3941-37ed-bfe1-9c9a834b1365 | -13.69187 | -48.82062 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a2165059-00fa-31b6-9d12-e32d26dfdf5a | -15.18197 | -46.16774 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 057a94d2-750e-3e65-b74b-5ef5fad90dd3 | -12.8513 | -51.00367 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f20417aa-6b54-3c54-8346-ce572e4fda9d | -11.28389 | -43.55371 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 5db5df4e-7574-33c4-a883-4d06fd1c2af5 | -13.16735 | -48.55626 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0421ca22-a8c2-3364-9d5b-37a74e93fc1e | -14.32943 | -40.09209 | 2026-09-28 16:24:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 55542003-e2de-3d2b-a0ef-688713adcb27 | -11.85801 | -47.11016 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1f28b366-ce8a-38a4-baf4-1a6b8e379d2d | -15.09865 | -54.71991 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| f9f84cd6-eb07-3a2e-afb8-cea93a856ffa | -13.05098 | -46.90889 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79aee5a2-860d-3746-a6e7-33260f07cafe | -12.67285 | -46.9836 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c3de9532-5ee8-3a58-bcdb-2063e12a7167 | -11.50604 | -47.37068 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc61e3cb-4583-313f-b5e0-5cec18ca47df | -13.58963 | -51.44719 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 6af893d1-1c14-317f-a219-78f478009dd8 | -15.33209 | -39.76982 | 2026-09-28 16:24:00 | NOAA-20 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 74ad6c07-6d15-33ec-a5b0-263ded629126 | -11.5493 | -47.37301 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d3b66377-c382-306f-a56f-d8c2ef2bae0b | -12.30753 | -50.25493 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f82d4a47-7a7d-3b76-9f7f-ea0bf158a9b0 | -12.29946 | -50.27531 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b227e78c-065f-3f84-991b-69d8bb919382 | -12.6687 | -46.98433 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c0a422e4-9aa4-3821-8955-342e738c243b | -16.3555 | -42.57301 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a483ed51-c99f-37d3-856f-6e1122dfa8db | -12.69567 | -47.35087 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| db13058f-665b-3943-9d4d-a04de164d136 | -13.48489 | -48.6011 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 591e491e-ddc2-3eb2-8b43-255139d10e92 | -12.38045 | -50.23578 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9700f5da-92c6-35e0-a5a2-43cd5e5d9c31 | -11.71604 | -44.52306 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| b4266d64-9143-39a4-8294-ec3b07020ad4 | -15.15254 | -43.60638 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.4 |
| d1903119-69ab-3f12-9e73-26eb46fc1c3a | -13.36312 | -40.9736 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0aeca65f-9e8d-329a-ab61-ccab60b4b727 | -13.5236 | -46.9051 | 2026-09-28 16:24:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7947cbca-c73d-3460-9bfc-f28162ab7d64 | -12.28753 | -50.2639 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e6f5d67b-f44d-397e-9738-0643544141a8 | -17.41139 | -52.02673 | 2026-09-28 16:24:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 61f66c39-2aa4-3b7c-a869-6550dde5062f | -12.06444 | -45.74497 | 2026-09-28 16:24:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5d4d9505-4fa3-311f-a2a8-ffecbc743810 | -12.16001 | -50.40324 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 1f7723fe-2703-3f8c-a4d8-0e6f4153c482 | -16.35151 | -42.56972 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 61.2 |
| cdf1db64-019b-36e6-a03b-df0bc22bcf4c | -15.26963 | -47.62967 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7adc681a-b39e-3c03-83fc-c0fd72b83c06 | -15.09559 | -54.71957 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 1fc7bb58-c5d5-3cfa-bf98-b24fe7945b60 | -12.14273 | -50.34991 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 26069592-c776-3a78-a3a0-5803036c9148 | -12.16402 | -50.39289 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c0306858-b89b-39f5-8a3d-43827d0182db | -15.44914 | -41.44386 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| b7eb47a8-df0c-373e-afb3-753cd7a2999e | -14.50404 | -40.53635 | 2026-09-28 16:24:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 34e2a3a3-0270-348d-82e6-c1898327a02d | -12.82987 | -38.24606 | 2026-09-28 16:24:00 | NOAA-20 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 404b772b-3fd2-3962-8285-d82aa4fc3dfd | -12.14553 | -50.37235 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9cd2913e-4469-3ff3-be4d-24b74f01f39b | -12.64022 | -47.29199 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 467654c3-aeb6-3200-86ad-478d764ee515 | -12.62903 | -47.26766 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| baa6fedc-c34f-3568-a396-f52878f9ed6e | -12.16362 | -50.38967 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5b355433-a4cc-31b2-a333-55a1041ac8df | -15.56629 | -47.91298 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8cf0ce8e-f524-3d73-a248-89ba92e9b5c0 | -12.9853 | -44.7342 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| c6679097-80ea-302b-b9e4-7996d4043421 | -13.17597 | -48.5491 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d723ad6c-9cc5-3269-8e0c-bc83cfe51bd3 | -11.89815 | -47.01813 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| a7e8e94f-3132-3f5c-a616-20609a7ef532 | -15.68192 | -47.59621 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 43e7aa4c-bb74-34e5-9c49-72c9b6998387 | -12.42946 | -44.1671 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6d1f2b94-1d26-309a-a5e8-da109ed4f03e | -11.71048 | -43.45867 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b1dc53f9-d73b-3adc-896e-a398bded3f31 | -11.37339 | -43.42483 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4a6c9dc7-36c7-3259-b584-db29254a4507 | -15.45687 | -41.45004 | 2026-09-28 16:24:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 5f7b455b-0638-3bb5-b621-64e9e02cb4a6 | -11.52187 | -47.39276 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| fdc3d846-c8c5-363b-879f-d44e178cf245 | -11.3263 | -42.21404 | 2026-09-28 16:24:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 36.3 |
| 1fe20061-f45b-32d3-a28e-b0160180e383 | -15.19401 | -46.13919 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 651ea1f5-d3ac-3bfe-b688-988826f2588a | -11.4515 | -44.91398 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| f2692c48-f1d8-3f08-b984-7938e44f1abe | -11.70405 | -43.48655 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| dda9f3cb-baa5-33b1-a236-3c8930d5b8e1 | -12.17856 | -50.42388 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7817dd6b-dbf7-362c-891f-4fb08b74ce00 | -11.90024 | -47.0023 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 645b0427-139f-3f25-bf69-819e9680e7c7 | -11.38184 | -43.43497 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| a54ab003-f10f-3412-91b7-d883aabd3c68 | -12.64426 | -47.34832 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a4952bcb-426f-3320-832f-b79390b5f576 | -11.43881 | -44.92873 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7b5fbb85-87f0-3c04-99a9-309007903d29 | -14.13873 | -41.45593 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 1e0bd0c2-6743-3cc2-9cb6-9f92a5f48c4d | -11.2221 | -44.78699 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5fb69770-6dc0-3093-8694-f475739c8433 | -12.75798 | -47.30534 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ee0ffca2-33aa-3110-8239-ff88e4827e90 | -15.06334 | -54.60231 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b685946c-2061-3bee-a21f-63ca83958889 | -13.81962 | -44.25188 | 2026-09-28 16:24:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| a678b229-d9b6-37c0-b267-114045e58b86 | -13.46876 | -48.58663 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3e17f00f-743c-3f28-9b69-b0042c3a1359 | -13.37374 | -51.31239 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 58b58ea8-4897-3436-a729-59f26cfe783d | -12.63698 | -47.26242 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 39889411-ab6b-3e34-aa1f-f38b30b1ad8a | -12.05445 | -46.48733 | 2026-09-28 16:24:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 031c588e-2db5-31c4-9267-db9ae0ce741e | -11.56629 | -47.40296 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 59c70c19-c3b5-37ba-a966-5b9c3e43780b | -12.75673 | -47.35091 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c126683b-bd7f-3a75-9b66-14e0209c2cca | -11.53296 | -47.37927 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0503c705-f492-3754-b5a9-a084abd48186 | -14.90623 | -41.1034 | 2026-09-28 16:24:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 94e0ac65-44c2-3e75-8357-ec7eb20c286e | -13.47183 | -40.46829 | 2026-09-28 16:24:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7eeba85f-79a3-39f1-a494-d8fbd3d2a06d | -13.70729 | -48.82807 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3ea50325-9e78-3276-81ab-b39e3e3e080a | -11.89866 | -47.02195 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 305f198a-23a9-3007-b681-1f7e20a18d7b | -13.47954 | -48.59647 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 94f093a8-b62f-33f6-a3c3-1a61b7b92423 | -16.42386 | -43.29026 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 035b28b5-ca47-3dc0-818b-100c07525b8a | -15.46833 | -46.1444 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 41b6ff51-7df6-33a8-b6b6-7e0fbca2e584 | -12.74723 | -50.68214 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 2a776ad9-48c7-3b44-a9b7-9f083abb76fa | -13.0412 | -46.99805 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| b2d3fdb7-e687-3abf-9668-d9798b0694ef | -14.32134 | -44.82838 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 3755772a-038c-39e7-a230-3ac497d1d3e2 | -15.20438 | -46.1879 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e5f2880b-def6-3938-9806-6a8be84e68aa | -12.97359 | -51.08836 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eac7b317-1b44-3d76-bdb1-aaeb6a7f1257 | -13.15125 | -48.54146 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fb10ee1f-3348-3374-b2ff-1891b2ce5deb | -12.79218 | -54.0281 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| d1b93d3f-cab9-3158-b3a4-840eab26551d | -12.06558 | -48.54411 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 79ce72c5-e029-311f-8f19-0ba34c87ae9b | -13.82022 | -44.25613 | 2026-09-28 16:24:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 64b7f2e5-85fe-3ce3-b6af-9bddc95092dd | -16.63463 | -48.47039 | 2026-09-28 16:24:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4cc26af6-fd27-3fe4-80eb-3ba3e3b3b591 | -15.1697 | -46.16967 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27b4f50f-0a1b-32d8-a9f7-5e936461c0c2 | -14.09967 | -46.31549 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 7ce32a07-af64-3f35-a981-2587a5439c1d | -11.85748 | -47.10633 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6ab6de36-9298-390e-9902-4f73d90ef720 | -11.39243 | -45.41218 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2971d46-5fd8-374c-8bd6-b679b8421b24 | -13.14942 | -40.12408 | 2026-09-28 16:24:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cf34b90a-2553-3c6c-888a-ffa74258308f | -13.95153 | -49.08245 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 06c8ce13-5794-3e96-a376-9ff03d016923 | -12.86428 | -44.80331 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fab089f9-142e-306c-9518-85b72c06ba1f | -11.68631 | -44.519 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| fc129e5a-8656-32c1-8b7b-046620b4029f | -14.08539 | -46.33303 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 461e2232-3439-3dd0-892a-0cd0f890f735 | -11.36279 | -43.39983 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README102.md)
