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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d28587c-81b9-302e-a1d0-400ea31f61dd | -17.35152 | -48.17132 | 2025-08-22 04:00:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| baf224e6-3906-359d-a049-2a14d699d0eb | -15.00106 | -54.86847 | 2025-08-22 04:00:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8064287e-fae5-343a-bbcb-c83e14c7f468 | -19.93162 | -43.91428 | 2025-08-22 04:00:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2bb84fbf-f0bf-3011-9612-2457cda21665 | -14.9943 | -54.86202 | 2025-08-22 04:00:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15444e0e-21f6-337a-bf0a-a436bd09d64d | -17.39955 | -44.24981 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a639da8-f215-343e-8643-9d7ab85f967e | -18.88408 | -45.019 | 2025-08-22 04:00:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 140cd87c-d76b-3250-99d0-6f2675c88ec7 | -20.25127 | -46.65461 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 818c22c5-1a04-35a3-9617-aa992994512c | -18.74899 | -43.84862 | 2025-08-22 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cb6a238-c2a2-3cd5-8233-17e21ce39a79 | -15.00148 | -54.86382 | 2025-08-22 04:00:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02f8b878-8444-3acf-b499-0ddc9b5a8f38 | -19.88963 | -44.81521 | 2025-08-22 04:00:00 | NPP-375D | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3c74b4d-a2e2-3e29-8309-3f2fe85ae05f | -20.08286 | -46.1254 | 2025-08-22 04:00:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc919bc4-c40c-3ef3-8d1a-db9a3fdfb5b2 | -21.41295 | -47.97299 | 2025-08-22 04:00:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d6d13ff-9617-3b02-81ef-f32362672c68 | -17.50604 | -48.00133 | 2025-08-22 04:00:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 667205d9-1f48-395f-a66f-c86e61d1e759 | -16.74581 | -49.31464 | 2025-08-22 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a1f54e4-6857-3d21-95bb-9b25b9be5b79 | -14.63127 | -54.84814 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 602c17c5-d38a-322e-bd19-8fc79d01e4a2 | -20.45448 | -41.68198 | 2025-08-22 04:00:00 | NPP-375D | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 37d9a233-cade-399c-834f-552e0a71d60c | -20.24843 | -46.69247 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fcf0e154-9f44-3648-9755-c1397ae5ea77 | -20.67198 | -41.41621 | 2025-08-22 04:00:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b3f8bc29-6879-3843-998f-d66cd531ca7f | -20.23466 | -46.61005 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 58328e75-8085-322c-a70a-1108c4b676a6 | -16.29485 | -43.8054 | 2025-08-22 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a62d133d-a3f4-39d6-993f-61296c30d662 | -19.58717 | -46.36488 | 2025-08-22 04:00:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b625c59-e1de-319f-be7e-3a6f540edec0 | -18.75252 | -43.84926 | 2025-08-22 04:00:00 | NPP-375D | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2aef9ff2-93a8-3f65-87cb-7819bb4188d7 | -20.26675 | -46.68745 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0a3f72f-b810-32a3-813c-3d32a4be95e3 | -21.18399 | -47.13889 | 2025-08-22 04:00:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a474ef7c-433e-37a2-99de-58aab1e17dac | -14.66844 | -54.85231 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8800d286-4f90-3c84-ae55-87e22f0d8157 | -21.24007 | -44.58808 | 2025-08-22 04:00:00 | NPP-375D | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5f2d8617-0562-3075-89fb-06a0ada43d46 | -19.96731 | -47.2028 | 2025-08-22 04:00:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0659d2c-acf4-3e11-9cd6-580db70d3a14 | -20.26946 | -46.69507 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43e993d-a68a-304a-a14c-8306d7d4b32b | -16.61342 | -43.36094 | 2025-08-22 04:00:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cda64f92-f646-3c89-a66c-e6b0c092f312 | -20.8736 | -48.53295 | 2025-08-22 04:00:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a943578-3d30-34d9-91c5-fe3a231bcd86 | -15.5646 | -51.69684 | 2025-08-22 04:00:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a4499be-53a1-3125-a8b3-9bb232210868 | -16.18552 | -47.98753 | 2025-08-22 04:00:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8891cb59-2e3e-30fa-bfe5-f8bcd141351b | -20.30431 | -46.62072 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4cc5eff-184a-3de1-b3b6-5c4660ef64cf | -22.55816 | -42.13351 | 2025-08-22 04:00:00 | NPP-375D | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1058a209-b82c-39b9-9b36-50f0832a29b6 | -16.55472 | -49.26601 | 2025-08-22 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 511064e2-dee9-3338-b181-88ef637f71e7 | -16.52103 | -43.45159 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dffca6cb-0297-3e1c-a949-85a5955e7009 | -18.88118 | -45.01365 | 2025-08-22 04:00:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24f3536e-cf97-3da9-8d93-91b72afae63a | -16.48288 | -45.09509 | 2025-08-22 04:00:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46eedcfc-0533-329d-a67b-764ecb93b94f | -18.79464 | -41.45731 | 2025-08-22 04:00:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3096876d-7217-31dc-bdc7-8f752119dc76 | -19.65116 | -45.97857 | 2025-08-22 04:00:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8d506ec-5bec-39ab-9816-77e164af2a16 | -17.61222 | -46.70006 | 2025-08-22 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7a0b12b-7c21-3d6b-8f6e-4cd89993ed83 | -15.56178 | -50.31369 | 2025-08-22 04:00:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 200b9cfc-b27a-381c-b5bc-dc3f1445c6ea | -19.67098 | -48.99261 | 2025-08-22 04:00:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 53eeec1a-b514-34a5-b348-8979553f036f | -16.61226 | -43.35992 | 2025-08-22 04:00:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 370573c4-4bc5-3ce4-b2cc-e9bb861acbd0 | -20.07898 | -46.1246 | 2025-08-22 04:00:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32104751-51bb-3fa3-9e00-0191916fdee2 | -15.00828 | -54.87005 | 2025-08-22 04:00:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bebd8ce8-7f61-3c75-a8a6-ea85de2d189f | -17.88361 | -45.93089 | 2025-08-22 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b36d89c-867e-3925-9b29-89fc9c48ece4 | -20.2436 | -46.60646 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5df62330-9bb4-3f4a-97f6-04658d529662 | -20.67806 | -41.42109 | 2025-08-22 04:00:00 | NPP-375D | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| eb4e29a5-77e8-383f-be1d-076bb188447c | -16.52366 | -42.51686 | 2025-08-22 04:00:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0953dd62-e958-33b0-9dfe-bbc6b26265d4 | -18.28282 | -45.5201 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 554ee00a-0997-360b-9e66-1a29ed0824b1 | -20.74587 | -47.90014 | 2025-08-22 04:00:00 | NPP-375D | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17af6b87-9d5c-31db-91df-d54069580810 | -20.33019 | -46.57104 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c5165fd-aae4-36e9-b20b-cfd3115bfbd6 | -15.82953 | -48.2784 | 2025-08-22 04:00:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab7a70a0-6938-3fd4-94d4-15263588f315 | -19.93624 | -44.57243 | 2025-08-22 04:00:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd0f80bd-3bc2-3190-b537-794a0dc11ac3 | -18.88035 | -45.01825 | 2025-08-22 04:00:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 57b70641-d01d-3606-8461-4f1819a78cab | -20.43847 | -46.50637 | 2025-08-22 04:00:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b540f128-659a-3a3b-80c8-94b9424f9e6f | -20.30609 | -46.63325 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90f38f1a-e552-375a-914c-078a74974fea | -16.78397 | -47.66533 | 2025-08-22 04:00:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 66c99d9f-052a-3317-ba91-ba00fd6340de | -17.35009 | -48.16782 | 2025-08-22 04:00:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aeac1ab3-fabf-3228-994f-370c774b47e1 | -17.88429 | -45.93251 | 2025-08-22 04:00:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5965ab2b-9f8c-3473-acc6-d66e855aeeef | -16.56035 | -49.26417 | 2025-08-22 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 5a29aa4c-e409-333e-b85d-70ec212a0f8b | -16.60401 | -43.91996 | 2025-08-22 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ec1b60f8-85e1-3705-9246-d81a8539e139 | -21.41455 | -47.97523 | 2025-08-22 04:00:00 | NPP-375D | GUATAPARÁ | SÃO PAULO | Brasil | 3518859 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2b3eba9-5846-363e-90d6-23f679647dbd | -20.75392 | -41.88598 | 2025-08-22 04:00:00 | NPP-375D | CAIANA | MINAS GERAIS | Brasil | 3110103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 37260c67-57b4-300a-b44c-71c694a1e197 | -18.66566 | -46.98561 | 2025-08-22 04:00:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aa5d25ba-19d7-3fc0-884c-38b67e2363f0 | -18.87953 | -45.02288 | 2025-08-22 04:00:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 45.4 |
| e41ef831-aa0f-35de-a853-c5863ec60976 | -19.71435 | -48.97697 | 2025-08-22 04:00:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cfcb91e-40f6-35e8-bd61-ca998c73da98 | -18.30807 | -45.51749 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72bbd7e7-ea32-38e6-910a-53c3b16123a8 | -17.57743 | -42.2983 | 2025-08-22 04:00:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 96f0a219-ec40-34e9-b63d-c6dba87b1aab | -19.2833 | -46.00867 | 2025-08-22 04:00:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97eed7a4-0286-3268-97ec-fab42faaeaf5 | -22.1919 | -42.87125 | 2025-08-22 04:00:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ec4939fb-6f17-3764-b846-015729f9fa36 | -18.28423 | -45.53812 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be7fbbdf-1c3a-3667-8ac8-bb2a2d4014bf | -18.94184 | -41.49092 | 2025-08-22 04:00:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8fd806f2-1873-34a9-9e38-903f04d009fe | -17.80632 | -44.31952 | 2025-08-22 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64135f31-1ee5-3a86-8db0-e9cd76432687 | -18.28808 | -45.53897 | 2025-08-22 04:00:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09b9f55c-a4a5-3500-8d4f-e50335fc7b35 | -20.27434 | -46.57444 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0291df6e-dca5-3f6d-bfa5-e1e09bde3608 | -21.42696 | -45.97157 | 2025-08-22 04:00:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| eebb0f52-5911-3b3a-88ac-dfd63828f0d0 | -14.62896 | -54.8555 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dc04ebf-4b8f-3111-9ee7-2b40533660cb | -14.62966 | -54.85513 | 2025-08-22 04:00:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2a66a86-250d-3827-96bb-78acd9d51ea0 | -20.87205 | -48.53066 | 2025-08-22 04:00:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68ef78ac-d00f-3450-a002-161f93c5ed6c | -18.8886 | -47.25156 | 2025-08-22 04:00:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d0c370d5-4bba-3756-98c0-fa6e40ee6d8c | -21.55042 | -43.4938 | 2025-08-22 04:00:00 | NPP-375D | EWBANK DA CÂMARA | MINAS GERAIS | Brasil | 3125002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9205aa6b-5610-3842-b28b-692d963ffa9d | -20.36629 | -46.50985 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4ce1f62-bba6-3e36-9dbc-43e4cd3ffa21 | -22.19252 | -42.86745 | 2025-08-22 04:00:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 13005a54-e386-3f3e-b7c9-12426b0294cb | -20.18591 | -45.23969 | 2025-08-22 04:00:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 67ed519a-a480-39d2-a279-6e22bae7d377 | -20.13463 | -47.46205 | 2025-08-22 04:00:00 | NPP-375D | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53775cf2-a900-3485-99d0-7b623de966bb | -17.39111 | -44.27651 | 2025-08-22 04:00:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55aa6a63-2d01-3241-83ec-8912080e4ef9 | -16.75085 | -49.31569 | 2025-08-22 04:00:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 774fa04f-b0e6-3a7b-9aa7-48787b879ed8 | -15.56112 | -50.31692 | 2025-08-22 04:00:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85b04a05-c40a-3cc5-a2b5-eb3facf9128f | -18.89285 | -47.25242 | 2025-08-22 04:00:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f627e57-a4cf-31c4-9675-28c0b170b9f2 | -20.24916 | -46.69233 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de8224b7-2abb-3096-8a33-a3ca33470827 | -18.66146 | -46.98479 | 2025-08-22 04:00:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec42d135-75ca-3c23-8cf7-197328ae3234 | -20.23068 | -46.60913 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 714a075e-09bd-300f-802f-ea2b4f4ba0b9 | -16.50248 | -46.7388 | 2025-08-22 04:00:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e29d36a-892e-38cd-ab3c-0670d34b3dd5 | -20.27013 | -46.69152 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6328a95f-009d-39d5-b47c-7871d73ccfeb | -20.33727 | -46.55521 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 83f7e77e-ac12-37ac-b56c-de6628923256 | -21.42786 | -45.96663 | 2025-08-22 04:00:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 34e1950b-be2b-3fbb-8aa7-886be3d5cb86 | -20.26609 | -46.69089 | 2025-08-22 04:00:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d76e5b5-3543-3546-8695-e04a7fa9c74c | -17.92014 | -44.48466 | 2025-08-22 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README22.md)
