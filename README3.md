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
| 7bf9e98f-8247-3a15-8d0a-c5f2ec673f7a | -21.9166 | -48.5738 | 2024-09-26 00:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 45.8 |
| b240947b-ffe7-3576-8c20-0cf234aca2cc | -21.9173 | -48.5504 | 2024-09-26 00:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 57.1 |
| ed2c7478-7e8f-371f-b683-d77035041d78 | -21.9374 | -48.5688 | 2024-09-26 00:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 57363fcc-e7c3-3741-9ac9-6fe2d3274d7b | -21.9381 | -48.5453 | 2024-09-26 00:07:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 4909e41d-ecbd-3172-9df1-4581946cc309 | -17.978001 | -42.2934 | 2024-09-26 00:07:07 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4dd11911-1548-39f9-8e84-291d38f46983 | -17.9804 | -42.305901 | 2024-09-26 00:07:07 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0f8f97b-16e1-38d0-97f9-0b793423da6e | -17.908199 | -42.141102 | 2024-09-26 00:07:07 | METOP-C | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f4f8fa00-5867-3fe6-88c3-3c1ed89c3f9d | -18.035999 | -44.394299 | 2024-09-26 00:07:12 | METOP-C | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1ff9309-aad2-387a-aa48-f50c1f58bb92 | -18.0231 | -44.378899 | 2024-09-26 00:07:12 | METOP-C | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5274b35-8947-3659-92f6-c43e11eb0f7a | -18.013399 | -44.380798 | 2024-09-26 00:07:12 | METOP-C | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4c654c-4aa1-3f0f-a754-99c2340d6a8e | -17.783899 | -43.245602 | 2024-09-26 00:07:13 | METOP-C | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c9a4a7e0-4617-3da0-b0d1-6cf47dc385cc | -17.9772 | -44.4589 | 2024-09-26 00:07:13 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3c8c674-a615-3ae6-bcdc-53f9b2cb4a69 | -17.0518 | -41.145901 | 2024-09-26 00:07:18 | METOP-C | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d48915e-9430-3a4d-9cfd-d12c263a4590 | -17.053801 | -41.156101 | 2024-09-26 00:07:18 | METOP-C | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f75b0bf-7815-370b-9f77-2bb50e053de4 | -17.042 | -41.147999 | 2024-09-26 00:07:18 | METOP-C | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b23e805-ddaf-3b99-99fa-767be687f1d1 | -17.044001 | -41.158199 | 2024-09-26 00:07:18 | METOP-C | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f870bb41-5896-3840-8b10-8b720263d0c3 | -16.6404 | -41.891998 | 2024-09-26 00:07:27 | METOP-C | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7b406043-83b9-3b24-92d1-4555c325f347 | -16.263399 | -40.978298 | 2024-09-26 00:07:30 | METOP-C | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 15cf8962-2ede-3d04-b7c4-aca2f61eba5e | -16.2654 | -40.988098 | 2024-09-26 00:07:30 | METOP-C | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a85a8b4d-73d0-39db-8d40-1918c0dac58f | -16.267401 | -40.997898 | 2024-09-26 00:07:30 | METOP-C | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 55fb999c-2e4c-3464-b2e4-b830b043ee31 | -15.7021 | -41.077599 | 2024-09-26 00:07:40 | METOP-C | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a238eec-cbf9-3c39-b299-ce5d98f02033 | -16.0315 | -43.609299 | 2024-09-26 00:07:43 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 66af69ec-23af-38d3-96b0-a8eef00b0e18 | -16.316601 | -45.670601 | 2024-09-26 00:07:44 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6e3753-029d-3b3f-8bf0-407614a281c5 | -15.3172 | -47.462101 | 2024-09-26 00:08:06 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e01a1b49-3e2d-3aed-bdb2-d6561ef2f1ea | -15.3075 | -47.463799 | 2024-09-26 00:08:07 | METOP-C | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 12ed9d34-1e13-3954-a98a-bdfe2b7d5d9e | -14.6575 | -45.4627 | 2024-09-26 00:08:11 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0fa1ac9-b69f-3960-ae39-ed919ee15cfd | -14.5558 | -45.6712 | 2024-09-26 00:08:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2eafd361-c967-3178-8781-f1c3a8fc493a | -14.5593 | -45.689701 | 2024-09-26 00:08:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c3ff8b35-f86c-3630-9b9f-51ad100ee649 | -14.5496 | -45.691601 | 2024-09-26 00:08:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48de6e6a-3595-3e74-8477-c4d942ce9d58 | -14.5531 | -45.710201 | 2024-09-26 00:08:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b56b7719-3ccf-3401-b03c-2171d98e93cb | -14.5399 | -45.693501 | 2024-09-26 00:08:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52e15127-9e99-35ce-bc54-ea9f103df001 | -14.5434 | -45.712101 | 2024-09-26 00:08:14 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f98a93e-32ea-3b8e-ac5f-f1737e377879 | -14.4354 | -45.2505 | 2024-09-26 00:08:14 | METOP-C | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6a434d49-1aa3-3630-859a-fd734de0de22 | -13.5277 | -42.5634 | 2024-09-26 00:08:20 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6ffb5a50-2f7f-3a36-bd08-d4347942ae57 | -13.266 | -41.496799 | 2024-09-26 00:08:21 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c72b5a98-83db-327d-9d2f-7cdfb1b7d435 | -13.2562 | -41.498901 | 2024-09-26 00:08:21 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e45ecba9-d06b-3ee0-aa04-f6844e4ae7f9 | -13.2582 | -41.508499 | 2024-09-26 00:08:21 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6c24c426-a81a-38d2-bd1e-583c26fa52fd | -13.3083 | -42.438202 | 2024-09-26 00:08:24 | METOP-C | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f8eec229-e52e-3042-b89b-334a5b941360 | -13.3106 | -42.449001 | 2024-09-26 00:08:24 | METOP-C | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 24965baa-bd9a-3bfe-94d8-5c111931b869 | -13.4353 | -43.764099 | 2024-09-26 00:08:26 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c01432c2-851f-3e5b-877e-20e3d329fef6 | -13.4379 | -43.777302 | 2024-09-26 00:08:26 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9e85a94-fd52-364e-9398-647cf258e291 | -13.1843 | -45.621899 | 2024-09-26 00:08:36 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7c055be9-b883-35bd-9a4d-11bb7984500c | -13.1877 | -45.6394 | 2024-09-26 00:08:36 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e66e299-aa98-3d0f-bd56-60ca14aae4dd | -13.1911 | -45.656898 | 2024-09-26 00:08:36 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1c3bc512-fe7c-3a3c-964d-18e7c31164df | -13.3104 | -46.3265 | 2024-09-26 00:08:36 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 73b76240-920d-3df8-98e5-9d4419be34f0 | -13.2969 | -46.308899 | 2024-09-26 00:08:36 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1320249-1704-3b0c-8d05-20fd5fa447de | -13.3007 | -46.3284 | 2024-09-26 00:08:36 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5382079-57e3-32ee-becd-9b46281e6d39 | -12.1494 | -40.864399 | 2024-09-26 00:08:37 | METOP-C | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 78334973-0f14-3991-b7fc-4df5a06f1507 | -12.2158 | -45.478901 | 2024-09-26 00:08:52 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a76732e0-8ea4-345a-8acf-375c34958e41 | -12.2191 | -45.495499 | 2024-09-26 00:08:52 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ca48a40-b8e9-3d9b-9cae-8ea086bac3ab | -10.1854 | -36.191502 | 2024-09-26 00:08:52 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 24c52a38-a1e9-3d99-bfec-106cf70718c8 | -10.1871 | -36.198898 | 2024-09-26 00:08:52 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7070603f-77e1-3145-b19c-d818f7f6f6fb | -11.8381 | -43.810501 | 2024-09-26 00:08:52 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b5e0821f-c7ad-32e0-8ce4-50729ff6d13b | -11.8407 | -43.823002 | 2024-09-26 00:08:52 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88d7bc8b-c496-3178-bd0e-3ced7d178314 | -11.831 | -43.825001 | 2024-09-26 00:08:52 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00d60e80-ecfa-3f5c-92fd-2d62b136970d | -12.1658 | -46.713402 | 2024-09-26 00:08:56 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e1dc33f-e85a-30f4-a3f0-e1b497fbe1f9 | -12.1698 | -46.733501 | 2024-09-26 00:08:56 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc372be9-ae02-318c-85ea-a02d6334875f | -12.1737 | -46.753601 | 2024-09-26 00:08:56 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45751b13-835d-3519-a41a-708eddfa9025 | -12.1601 | -46.735401 | 2024-09-26 00:08:57 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ebfc915-c6a9-3e1d-b273-937ad3c1474e | -11.8523 | -45.5345 | 2024-09-26 00:08:58 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87b234c7-4591-3415-92f6-eb6f6eeee976 | -9.6145 | -35.825699 | 2024-09-26 00:09:00 | METOP-C | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dc52da85-7a09-3457-b3f8-ac01bf33b171 | -9.6163 | -35.833401 | 2024-09-26 00:09:00 | METOP-C | SANTA LUZIA DO NORTE | ALAGOAS | Brasil | 2707909 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d01b50cb-3230-371c-9a11-d59d318d2b04 | -11.9277 | -47.301498 | 2024-09-26 00:09:02 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e62a6c54-3240-3508-ade0-445de3d484c6 | -11.4439 | -45.719501 | 2024-09-26 00:09:05 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2832f1b7-6a93-3e5e-92cc-bcf8ee4437a1 | -10.9864 | -44.4179 | 2024-09-26 00:09:08 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d9d3950a-5046-39ec-8fad-13322fd15340 | -10.9766 | -44.419899 | 2024-09-26 00:09:08 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad363e0-e887-3d30-b2e5-587428cf02b2 | -10.9793 | -44.4333 | 2024-09-26 00:09:08 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 13f475ad-44fa-3f7d-84a2-af27810d81f3 | -11.4605 | -47.280399 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e0f972ad-b014-3158-9484-a55c2fb806ca | -11.4647 | -47.3018 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 475a81c5-e807-3ba0-8a57-0f73e0806d06 | -11.4508 | -47.282299 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2812466c-a12d-30db-a226-c3bf57adcf8c | -11.455 | -47.303699 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 778390cc-cb61-3b8f-988e-a86990ad21fd | -11.4592 | -47.325199 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d047b94-78db-39e7-9529-ac0405d3f673 | -11.4453 | -47.305599 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba18b5ba-74ca-38d8-8fba-c948a360afeb | -11.4495 | -47.327099 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4413d4aa-1bb9-3a4b-86aa-e0a770a55e3f | -11.4314 | -47.285999 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 74db5157-0b3f-3602-8270-f9644711f4a6 | -11.4356 | -47.3074 | 2024-09-26 00:09:10 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca954dbc-73c9-39ae-b213-1f8a1804e871 | -11.8363 | -49.607399 | 2024-09-26 00:09:11 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9761e7eb-2445-33e9-b4c8-549eb317bc91 | -11.8422 | -49.638802 | 2024-09-26 00:09:11 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df25f1ba-0573-3eda-8659-0873331701ac | -11.8267 | -49.6092 | 2024-09-26 00:09:11 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78b037b6-5454-362f-8a86-4d4528421723 | -11.8326 | -49.640598 | 2024-09-26 00:09:11 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 795bc3dd-38a7-34a4-829c-5f138becdc24 | -10.8277 | -45.878101 | 2024-09-26 00:09:16 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f4dc5f89-7755-38f9-9941-66a5a1477bf1 | -10.8311 | -45.894901 | 2024-09-26 00:09:16 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b077e72-1be5-3a4d-8ab4-1704b70b5685 | -10.818 | -45.8801 | 2024-09-26 00:09:16 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5716312c-85ce-34da-ac4e-c6ec541a4150 | -10.8214 | -45.896801 | 2024-09-26 00:09:16 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e5dcec6-8079-3667-be18-84eb7224568a | -10.6259 | -45.8325 | 2024-09-26 00:09:19 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 162014e0-5cef-382b-b04e-210401efc8cd | -10.6293 | -45.848999 | 2024-09-26 00:09:19 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 24f8e663-e6e2-3687-9f8b-ba58e1fd396e | -10.6162 | -45.834499 | 2024-09-26 00:09:19 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a882b07b-5806-3a94-974e-9af9a22a4ea9 | -10.6195 | -45.851002 | 2024-09-26 00:09:19 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9bfae15-d388-3b2d-af55-b151ba4e3ab1 | -10.6229 | -45.8675 | 2024-09-26 00:09:19 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 28f1825b-447d-3490-9153-6561365d3f6b | -10.6098 | -45.852901 | 2024-09-26 00:09:19 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb192658-eea6-3f17-a268-bb9d9d0d0c26 | -7.993 | -35.2537 | 2024-09-26 00:09:24 | METOP-C | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6d7bae9-746e-3dcb-9d73-1fee7256f401 | -7.995 | -35.2621 | 2024-09-26 00:09:24 | METOP-C | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8ea4ea2-e95e-336f-8a9f-3e4aba0ce6e9 | -6.992 | -35.210602 | 2024-09-26 00:09:40 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dd2c998a-02d8-3a87-b74c-ffcfb7a2034d | -6.994 | -35.2192 | 2024-09-26 00:09:40 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 327c352c-3718-3cee-86e2-c0b6ff567a10 | -7.2423 | -39.859699 | 2024-09-26 00:09:53 | METOP-C | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 9f11add2-c973-332c-8c2a-fe08b3df9153 | -8.2332 | -44.839199 | 2024-09-26 00:09:55 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4f2ef2b-0b19-3dce-90a7-9f8ed7cbd5c4 | -8.2234 | -44.841301 | 2024-09-26 00:09:55 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 21ffb468-d3b6-390c-808d-be183e654db0 | -8.2262 | -44.854198 | 2024-09-26 00:09:55 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4f5e9a2-9916-3a8b-9331-b03f50179c1a | -6.9469 | -39.419102 | 2024-09-26 00:09:56 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4c189bb4-285b-3035-91cf-fc2a64ad23e6 | -6.9484 | -39.425999 | 2024-09-26 00:09:56 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README4.md)
