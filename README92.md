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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c41c05cb-cfaf-320c-bdda-d4777e3d0aff | -21.10162 | -48.825 | 2025-10-04 04:17:00 | NOAA-20 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15c4d197-a38d-3ca3-ae02-f13d522cd5b6 | -19.59538 | -44.62466 | 2025-10-04 04:17:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6fb02fe-ee22-35a6-a021-4415624d184b | -16.03099 | -50.94097 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9032f77d-cca8-33d3-bada-b64f7ad2075d | -19.76752 | -46.58352 | 2025-10-04 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 14349175-a772-35bf-933d-3b2ba1bb1383 | -15.60657 | -52.46905 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ce0ef19-8f6b-3581-a69d-b8dbf447b25d | -15.59818 | -52.49639 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9b2e0385-0f75-300e-b76a-e0ca28b0ca0e | -15.59462 | -52.46445 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb91c0f5-39cb-3ce1-b97d-f24b670b08ae | -16.01287 | -50.93789 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d08fa587-3433-3049-a68b-c81e07c30dc7 | -21.10868 | -49.18037 | 2025-10-04 04:17:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2669a60-efb1-3e0d-82c9-b5aeaeee85af | -19.88997 | -44.78486 | 2025-10-04 04:17:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5b6f056e-566c-364a-8253-023442711acb | -17.9883 | -45.00932 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ce5c13f-8992-358c-a3e2-5d9323fc35a9 | -17.15494 | -47.02827 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d479fcb6-1f9d-3785-a57c-f72ae524f8f8 | -15.37239 | -47.952 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10bfbd25-40fb-3e2c-866b-41fce5658c0f | -17.15578 | -47.04407 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5d54273-851f-35b1-8de4-ed12033ebccb | -15.58061 | -52.46257 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82bf4b3c-ec4b-3952-87e0-12c663bed23a | -16.34379 | -47.09033 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92da7558-f9c0-37f8-ba52-a5528d6a475f | -15.65019 | -46.25424 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e00b9a2-cd85-3ae5-8a4b-9fc6743ee98f | -19.13133 | -43.14358 | 2025-10-04 04:17:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 972708a5-1813-3295-97af-a0b4ed20b605 | -21.66373 | -45.31902 | 2025-10-04 04:17:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 26a4e735-a462-3154-a6d4-835d286eecd0 | -19.88691 | -42.62809 | 2025-10-04 04:17:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e47a1b7a-4930-35e2-a82c-02f80bdf93be | -21.09122 | -47.76515 | 2025-10-04 04:17:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 447a4a7d-4da7-3f79-91f2-1738c5281ba9 | -15.72596 | -46.27485 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87caf841-fc81-3a88-a7bb-6a778a7bb071 | -19.70714 | -44.127 | 2025-10-04 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd386bda-6427-3841-9cf8-51458a326174 | -19.59818 | -44.62906 | 2025-10-04 04:17:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5d7d0e6-4ac6-3525-85eb-24b1a592d154 | -17.63957 | -44.45319 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 674a7545-25a2-37bb-9a07-b3c7b1286059 | -17.07586 | -43.36283 | 2025-10-04 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32e11021-2082-31b2-80fd-960719704349 | -19.461 | -43.66013 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1a1438e7-b4dc-339c-877c-a825aba60c94 | -22.30548 | -46.51487 | 2025-10-04 04:17:00 | NOAA-20 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a43465e-2d59-3b75-8599-0dcb96037175 | -16.35798 | -51.472 | 2025-10-04 04:17:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4d7eed4d-d313-3727-87ca-4c0c20f26032 | -19.58414 | -45.89887 | 2025-10-04 04:17:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a24cece-64cd-3d5f-8e48-088687089f08 | -19.00035 | -48.49654 | 2025-10-04 04:17:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ddb95a85-92dd-3385-9e6d-dccf5c21e9c2 | -22.30606 | -46.51114 | 2025-10-04 04:17:00 | NOAA-20 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3755449f-4941-38f9-9233-0a42cb73aaf3 | -15.79251 | -46.25999 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cf0be6b-18d7-3d78-b697-758634310c3d | -15.37877 | -47.95739 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb48920c-8be3-3dbf-9653-0261a38fdecd | -20.41546 | -44.13185 | 2025-10-04 04:17:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d21b9734-14b9-370d-95ea-f37c3cd07252 | -14.98572 | -49.95395 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 98c70cb0-75b7-3638-bfd0-685e33eec5f2 | -21.93188 | -46.60101 | 2025-10-04 04:17:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| feb5f16c-7a7e-3d01-9927-3c1ff4a38eed | -15.76224 | -47.77361 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fb8b5c9-e791-300d-86b9-48326240657f | -15.79706 | -46.25312 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8386d571-b0ce-3fb3-92ce-64cc235e142a | -16.35121 | -43.41748 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e03d5400-301d-3cb6-a97d-ef88b813abdc | -16.03586 | -50.93793 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf049155-80b9-3a06-8a35-05c7c3c939bc | -16.34532 | -47.1023 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac907be9-9f82-3db2-9ae2-25107006f124 | -17.08476 | -46.23418 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 74560d0c-7948-33ce-b6f8-148411ee1475 | -22.28485 | -46.73295 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bca09bf-3d09-31b3-a70a-1e2d84be1ea4 | -19.48452 | -45.31361 | 2025-10-04 04:17:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1a64ddb-2bfe-3492-bd86-1664c84d7236 | -17.29905 | -50.59147 | 2025-10-04 04:17:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0b15c6d-fc87-329c-abf2-3096f8b2c35d | -14.94311 | -49.97416 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e3e64f0-adcf-3f09-8dc7-df5a95f5f24d | -15.72081 | -46.28548 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b42ae040-20a9-30d4-8e40-3a81152eb371 | -21.62425 | -47.39942 | 2025-10-04 04:17:00 | NOAA-20 | SANTA RITA DO PASSA QUATRO | SÃO PAULO | Brasil | 3547502 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85c1f8bd-049a-3961-b79d-52c49676bd42 | -16.04079 | -51.05059 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbc596a7-4864-324a-bd6b-fcceaefb5b7b | -19.59792 | -44.86058 | 2025-10-04 04:17:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a8d1ed1-b3a2-3214-9510-57b16431aae6 | -21.68426 | -50.06128 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b9a71572-b958-32f2-9c1d-34a4bf616d1d | -17.29583 | -49.27044 | 2025-10-04 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e1a15a4-e66d-38fc-a1d5-80abc750af20 | -19.74018 | -47.19074 | 2025-10-04 04:17:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27231eeb-3145-3ba4-ab31-519b0ec29b4b | -16.06851 | -50.90076 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 648615d2-896c-3ec2-a1f7-d0ae1aeb5a27 | -17.0793 | -43.36334 | 2025-10-04 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b337e50c-0e41-309c-bc99-98a5b063f531 | -15.35392 | -47.95309 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01aa9807-cf74-3bcb-8248-ebd66ef85962 | -22.07477 | -43.10153 | 2025-10-04 04:17:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6fb77de0-ed7b-3f54-a85a-1d024bd6a0fa | -17.47828 | -44.04134 | 2025-10-04 04:17:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b720bb37-b71d-38c8-be8c-a14082bfe084 | -17.08044 | -43.35559 | 2025-10-04 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ee4bfc4-cbad-3409-a2aa-a921262e40ef | -20.92306 | -42.92067 | 2025-10-04 04:17:00 | NOAA-20 | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 20df0426-0230-3c3d-9324-1244c1032311 | -17.0034 | -49.15285 | 2025-10-04 04:17:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32925364-afdf-3f5b-997d-b94a8bd4a02d | -15.52669 | -46.8093 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56c2f07a-593a-3689-bdd8-28fd11347312 | -16.00871 | -50.93715 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fae5200-4864-384e-97a1-f00814942228 | -21.03899 | -55.74778 | 2025-10-04 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a338090-c825-3feb-9b11-d2c5774f5f59 | -17.98108 | -45.0119 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e16b1c16-4759-3f7f-a018-d3f1de552dac | -17.62377 | -46.70025 | 2025-10-04 04:17:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4c8a3c8-fa7f-33e0-a68e-55122a703c98 | -17.08299 | -46.24509 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d10b259-3630-389e-afcd-2bdc773e3077 | -19.10617 | -44.70808 | 2025-10-04 04:17:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2f836a3b-3b60-378b-882d-9e1c1f44b91d | -19.24583 | -45.99812 | 2025-10-04 04:17:00 | NOAA-20 | MATUTINA | MINAS GERAIS | Brasil | 3141207 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec32abc-133c-36a0-a492-d093216a8f33 | -15.62059 | -46.94203 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0568d662-1f89-37df-8e9f-82aa7ec19808 | -15.72415 | -46.28606 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae23c803-7a8c-338c-9e26-0584668f917b | -15.71593 | -46.27307 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d12e823a-faf6-3e03-a14a-599ac05b3137 | -16.08031 | -51.07117 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8715b0d7-8909-3552-b6de-e578b80bc3b0 | -20.38587 | -44.45651 | 2025-10-04 04:17:00 | NOAA-20 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 96a87559-917f-35da-a48b-e2d7e798aa26 | -15.03259 | -49.44916 | 2025-10-04 04:17:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cbc842d5-e50b-3300-a004-81d9abccd6da | -15.49554 | -52.85596 | 2025-10-04 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b0532d4-b1ac-3357-a92c-6bf65f006d61 | -15.35675 | -47.9579 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bd96c3c-8f50-3424-a712-17def5b5d9ed | -19.81463 | -46.07285 | 2025-10-04 04:17:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3e3902b6-6a30-30a4-a8b2-9e5f4e25ff98 | -16.02348 | -50.84382 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3a5c851d-b04b-38a2-b6d1-d33918be4b81 | -20.13704 | -46.41911 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9db27156-2da4-3b7d-b5f9-3cff15fd0800 | -15.53371 | -46.83292 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dee12501-b44c-3a50-a9dd-3391c0913ead | -17.15642 | -47.04028 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4fe7040e-0d33-3585-91a3-5a2eed4b87c5 | -22.30275 | -46.51054 | 2025-10-04 04:17:00 | NOAA-20 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e25110a0-5798-3eef-8f6c-62e9259e07fa | -17.50054 | -43.46967 | 2025-10-04 04:17:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09f8479a-9cc9-3dd3-a0c0-c4fe20471311 | -20.11802 | -44.39851 | 2025-10-04 04:17:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4802fe5-9cbc-3df6-b00b-6161f9f5020a | -17.92073 | -51.74073 | 2025-10-04 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 006219b1-17cb-3c6c-82ca-ca322bb363d1 | -19.96693 | -43.70706 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5c70c737-fbeb-36ac-b73b-9f008c597351 | -16.36221 | -51.47306 | 2025-10-04 04:17:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 534a57ae-f716-34f8-b3bd-64fd5eeffa14 | -17.29373 | -49.27248 | 2025-10-04 04:17:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44cd13ed-8ad4-302e-b7e0-a2bde7abe728 | -16.35061 | -47.09141 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0c1f6ba-5232-37fd-b73b-a656f28b9b37 | -16.92009 | -43.59001 | 2025-10-04 04:17:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5829a0d6-d1f0-3ce8-b6cf-52f392434dc5 | -15.80041 | -46.25368 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f4eeabf-43eb-3912-bf08-001b8435dc0a | -16.0457 | -50.93124 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a28d1f44-9d0d-3e64-a039-3f5320ca3359 | -22.07843 | -43.10205 | 2025-10-04 04:17:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eb8c633b-7c3d-3d04-ab11-606ea29a6880 | -17.95986 | -44.26014 | 2025-10-04 04:17:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e49b05a5-38e5-38bb-aab9-5016a32ca8d7 | -15.24432 | -49.30534 | 2025-10-04 04:17:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7439bd04-bc4a-32b0-8566-7abb3beb2da6 | -16.75589 | -43.96651 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 866cbbe7-73b6-39f9-9b88-cb3ff37e3be4 | -21.69431 | -50.06801 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6a631df-51f4-3291-9bef-785c1db601d5 | -20.35636 | -48.78549 | 2025-10-04 04:17:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README93.md)
