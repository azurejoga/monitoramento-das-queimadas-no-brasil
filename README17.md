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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75bcaabe-e8e6-339f-8eac-64c329212c55 | -14.10738 | -46.26925 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6d37ea8-d5aa-3889-bcaa-cdaa82ea79cb | -12.77636 | -54.01591 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d67a83d3-7b02-324d-b4c3-244551a1bcb2 | -15.09103 | -48.32678 | 2026-09-30 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 62ea5add-cecc-305b-9c90-b0b1f6553983 | -13.30215 | -43.46806 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fce88e76-c2d7-3d76-8d5b-cb5d75233e9b | -18.11228 | -44.40851 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 590a8d9c-0435-3a0c-bbbc-dd1a27cf61d8 | -18.28435 | -43.69803 | 2026-09-30 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e973dedf-d85f-3d28-b812-3a4e5489b59b | -17.52294 | -43.70507 | 2026-09-30 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2da756f6-7925-3096-b809-5b9f4123f6b1 | -17.91916 | -44.40422 | 2026-09-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e907d033-af1f-3fb4-bf21-094cbd060ddb | -13.07031 | -43.2774 | 2026-09-30 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 284e1b0d-fb01-362c-b243-0a5179f591a6 | -19.34201 | -43.72833 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68d46192-15c3-3044-a602-8cdd427f61eb | -13.36512 | -46.822 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16914313-8d40-313b-81a1-70994e47c63d | -12.06543 | -46.46438 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34cdd433-65d2-3434-ad6e-f3bd5009f9a3 | -16.35229 | -42.58269 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcee8205-4a9b-3de3-b54f-fc3c2197213c | -18.13558 | -44.35201 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 899a550a-695c-35f4-8091-f0a65618344c | -12.2729 | -50.28807 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd98c893-529e-339b-8941-8e8d1ac32a6c | -16.91501 | -42.11127 | 2026-09-30 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1386a13-8cfa-31db-9e1e-7c0ad1ea9581 | -17.57304 | -43.70602 | 2026-09-30 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a7809a1-5eb0-3f9d-a634-e22377aee39a | -15.66684 | -39.92376 | 2026-09-30 03:57:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dc0a7b12-1fc1-3111-a21e-0f29aafd6b60 | -15.76047 | -46.04003 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0122d347-c82d-340f-8c7a-d2cb3384759c | -13.37239 | -46.83231 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eaa4d31e-71b6-3f07-9033-d95f1250f9ac | -12.07665 | -46.45272 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0976f7b8-0e1f-3cac-80a6-b962157a3e13 | -13.371 | -46.81494 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 395bb638-c455-3c69-ae2e-1e489af2e55e | -12.14571 | -47.20112 | 2026-09-30 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01ad968a-8c89-3ee8-a5c9-fa6a12e27264 | -14.37901 | -43.4834 | 2026-09-30 03:57:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c7637b2-883d-37cf-b619-88a77eee7b4a | -13.38277 | -46.82566 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| adb4db69-3508-329b-8d9b-59577f6b3913 | -19.35819 | -41.49308 | 2026-09-30 03:57:00 | NOAA-21 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b66c8c2e-3b85-36e6-92a0-c6e0eb1e14e6 | -18.04209 | -44.32512 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 694b9c92-303a-349f-b83f-e89a2422efb5 | -16.03392 | -41.32323 | 2026-09-30 03:57:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 99dcd7ba-c403-34bf-80e2-caea5975a671 | -15.46746 | -46.12811 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e37d8a5-d7c7-3074-aa26-fac31fbf7d6a | -12.26802 | -50.28297 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 339475ef-f7c7-3171-8742-8789afaedaca | -19.93732 | -41.83591 | 2026-09-30 03:57:00 | NOAA-21 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a6cbee04-99d8-3364-8d04-3073afeb67e0 | -17.52227 | -43.70906 | 2026-09-30 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36ea92d5-bda4-3fec-82b6-987938239f0f | -19.26361 | -43.75553 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac7628b0-fcb8-3761-812b-7e4adcb3a7f9 | -12.51675 | -43.08645 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f45b9ed4-4c73-3c1b-9575-852635398876 | -14.20008 | -42.07373 | 2026-09-30 03:57:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| ce360a5f-99d6-33fd-9ffe-44fac2bcd4f0 | -12.34594 | -48.19886 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e8a30445-8690-381e-a5df-9dca13a3728d | -15.20371 | -46.14577 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0036504b-c6c2-38b7-8374-415dcfbe5bcb | -12.24694 | -50.27054 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a59b13f-c0cd-35a7-b82a-b977b588e2b0 | -14.01046 | -42.90791 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 6d884b29-7b5e-34b4-b597-cbe7da84cc78 | -13.36655 | -46.8142 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d97f2145-bf16-34f9-a2bc-5818ed38127f | -13.37399 | -46.82361 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4c97fd1-fc0c-304d-8337-107339007192 | -12.25242 | -50.25983 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 272b5723-5da5-3225-a7c3-e9657b035f38 | -14.91068 | -43.41412 | 2026-09-30 03:57:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 8d461ffd-2c3f-306b-9b3e-b5bfefa38129 | -12.69601 | -43.22894 | 2026-09-30 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2277a486-5e10-3797-b8bc-04d631015c98 | -12.08027 | -46.45806 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2faf1a94-17b2-34a8-a6cb-3f76939def7a | -12.24829 | -50.25076 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4d16364-cc00-3505-8925-73c37ec51bdc | -18.50103 | -45.14257 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| af6b980e-22ff-3fff-8af7-c8a5b70079f9 | -13.07101 | -43.27317 | 2026-09-30 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dd159d69-7a04-323a-a4e9-234e1fc382b5 | -12.77784 | -54.00912 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9a23396-5be3-3521-88bd-ce781ba54cdd | -19.27326 | -43.76133 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1aa2f6b-dcf2-3d1d-ac85-f8d46b7dca64 | -12.78334 | -54.01743 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 460d3341-cbdd-3171-ac5c-f776db019200 | -14.9075 | -43.41399 | 2026-09-30 03:57:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 87ec9087-8ae8-34d2-9559-8593e4b23b35 | -16.35568 | -42.58324 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f79362ee-f798-33df-b9ae-5e5dd47a55b8 | -14.12149 | -46.2636 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5bb806b3-b536-3057-a0f6-309843d4d739 | -12.1946 | -47.11079 | 2026-09-30 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc8f66e4-ebe8-36ad-b4ec-5106776f098f | -12.25748 | -50.27674 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c338eb2b-38d3-3765-8d11-d8dc496c03dc | -15.91347 | -40.98677 | 2026-09-30 03:57:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9ba08ad7-a7f1-3a52-a4e1-a39a9709cf83 | -15.75073 | -42.28279 | 2026-09-30 03:57:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b23cbc6-3827-3999-ae87-99209d297d83 | -12.78094 | -54.00373 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc108067-d66e-3be8-809f-eb90f9da8bce | -12.04619 | -50.21977 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd762ba9-4342-304e-ab1a-3e10630f0170 | -16.35506 | -42.58706 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e62b5330-ff7b-3079-b650-6ad31248cb73 | -16.42029 | -43.29932 | 2026-09-30 03:57:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee782ff-3162-327e-b63d-062bbd2dbaa9 | -13.42798 | -43.81242 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a9be2a1e-9124-3ae9-aaab-0c6f5a7dcc8a | -14.74544 | -47.13911 | 2026-09-30 03:57:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f4ba2ec-ee24-3bbb-946c-97779dee0ecc | -12.04412 | -50.21788 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4bf6a44f-5aca-3dfd-aaa2-4378e597fcd5 | -18.50022 | -45.14718 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 98a43370-db12-32a5-a41d-e9144df82355 | -12.30762 | -47.96034 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 56616586-8de2-392a-a204-f9e55b48ce75 | -16.67783 | -41.85265 | 2026-09-30 03:57:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 08c55710-2fea-3298-b17f-24266e5f5458 | -17.91558 | -44.40356 | 2026-09-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5b3bede-a493-35cb-9ac8-0d67b312ff84 | -15.94403 | -40.53081 | 2026-09-30 03:57:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a37a7b2-5122-3a55-8f54-530323070884 | -19.2506 | -46.68152 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bafae27-72c1-3dfe-a05c-54646680ebcf | -13.75641 | -42.09935 | 2026-09-30 03:57:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3048924a-f29f-3ea1-94f7-462e50f57777 | -14.53823 | -48.29388 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe26ad4f-2e12-32eb-919e-be5c253a08bf | -13.37676 | -46.83345 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc5ecbf2-1873-395d-ad8a-68e1c30fc2a6 | -14.94164 | -49.75088 | 2026-09-30 03:57:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6fd3e1a-62ec-3917-8bb9-39983784721f | -15.6361 | -43.23134 | 2026-09-30 03:57:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 20.5 |
| 06447727-d5ab-3298-bd00-3637b3084563 | -17.4092 | -42.38137 | 2026-09-30 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a27fbd2-fbc8-3d64-9dd2-e78e1977ee90 | -16.35606 | -42.58683 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c14bdb54-66e3-3a45-9d91-9eb26c832651 | -13.32649 | -43.96162 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c9f59e6-bd29-32df-b063-7cd83ebd51e3 | -15.97463 | -48.1349 | 2026-09-30 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c263cb6a-f1e7-37e3-bea0-1aa0b60957bb | -14.13411 | -46.26611 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14bbf539-e645-389e-8796-ae9cfc868690 | -15.96276 | -40.51926 | 2026-09-30 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5819db3a-0596-3561-8625-0e98de522e8f | -12.24524 | -50.24961 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a009b76-985a-3ede-91cf-ceb7ff8451b0 | -12.83845 | -50.6226 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3a7a354-9c25-320d-99bf-55934c3ae863 | -15.91122 | -41.32406 | 2026-09-30 03:57:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27cc7ebc-1b31-3eae-90b5-896962c63b4a | -18.49655 | -45.14641 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0ee1e86-2705-35e0-9771-38aa225c450e | -19.26704 | -43.75616 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4314c29-5ce4-3ff9-ae8e-a9d7bc3ed3d7 | -13.52425 | -46.89124 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fbc0fbd-caaf-3447-8e8f-db668e830484 | -12.07947 | -46.46254 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4488e6a-1a64-3444-98ef-75eaab18e433 | -12.56749 | -43.06945 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbfa8297-aa48-384f-8187-517d5de793be | -13.70115 | -44.22775 | 2026-09-30 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24b8e444-93b4-3dd8-ad2a-238031061ca1 | -12.78625 | -54.00401 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 81f02c9d-430e-3ea8-8258-2533c12db9ae | -15.7521 | -46.03845 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7efed301-18c9-3ae2-91d0-9dc68f30a61a | -14.01092 | -42.91182 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| cd247b97-3447-3ea4-941c-9d490e99d62f | -14.0151 | -42.90841 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 2ef80987-2c6f-3753-b633-ce1b1cc4db70 | -18.49369 | -45.14103 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fa39300-cf53-30c6-a65d-53cd834c62f6 | -18.88814 | -43.80959 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a711592d-2e15-3190-8097-4eef1ef54884 | -13.37764 | -46.82867 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 669787e9-38dc-38d5-af18-9b604b4c8a1f | -12.78481 | -54.01065 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f2e016d7-74fd-3e3a-a825-9ce6e50c28d1 | -13.35626 | -46.82031 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README18.md)
