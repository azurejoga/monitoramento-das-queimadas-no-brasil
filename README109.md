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

## Dados Diários - Página 109

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9bef858-1440-384d-ad7b-3f226c70001c | -12.24282 | -47.8241 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 35141268-389f-3971-a76f-21827e2add01 | -9.35568 | -46.3295 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| dea7ab5d-5801-3ce0-8b89-ddd9545866e9 | -14.43685 | -46.35382 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61da0474-bd44-3759-946e-9791543d984c | -13.36687 | -48.09555 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d61e1de-6b5b-3f71-97bf-f6b21dfbd510 | -14.89601 | -48.37552 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce80ece0-7a07-35b0-8ffb-4791e85d104d | -11.7577 | -46.86762 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e41db59b-442a-36a4-8d04-eb41fc1eb8aa | -11.85479 | -45.00328 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76eea3a1-bf6e-383b-9ec4-c50e2180db82 | -10.02075 | -50.24943 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac90065a-b5ec-3a84-bdef-221dab8b51c5 | -12.69247 | -48.56326 | 2025-10-01 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cda9e57f-d643-301b-bd96-9e80e34b869e | -14.92188 | -47.81712 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 003e119f-51c1-3496-9b82-1423f1324d91 | -15.43926 | -51.5603 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c222afa8-2dbd-3824-aa22-65ce816efcc2 | -14.04662 | -47.99103 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 57ee5702-aa7e-3d36-b806-a17c1a73d8c2 | -16.49442 | -43.73032 | 2025-10-01 04:51:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80bc6275-9bd1-3cd3-8810-c6c4253c9456 | -8.97598 | -50.26665 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 439f912e-4015-3e12-9f28-85d7ee2a39f5 | -12.95121 | -48.41941 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1aa3533-f5d1-35d1-b170-c18f891c1695 | -8.74731 | -50.81441 | 2025-10-01 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a7484bd-a66c-3558-bd6a-9439b20af0f1 | -14.8932 | -48.11382 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0ed163c-0630-3594-9f74-36f9aaf9cd87 | -10.76898 | -45.36869 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acaa3071-f6a3-31e2-beb4-f99802bdcd58 | -14.18087 | -46.11395 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80d3abe5-c904-3eba-8004-e06fcada1a02 | -14.05978 | -44.3712 | 2025-10-01 04:51:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19254343-6008-38ef-90bd-12eac5eef549 | -11.75824 | -46.86366 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46d251b4-5095-38cc-aa23-92442366e768 | -14.70294 | -48.12693 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5784d6c9-a1e0-3da9-a741-1cf49bb66638 | -11.83334 | -44.98439 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffa0e697-7695-31c6-9aae-94a0e44cf0a7 | -11.43636 | -43.50331 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d9bd232e-3b23-3546-9e87-2baf70bc0352 | -12.92825 | -54.72409 | 2025-10-01 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 957493b4-7d7e-327e-a853-f27dea879f30 | -11.16632 | -54.12408 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7469f531-e5ce-34eb-8931-f935fb6f56bf | -15.33514 | -46.27955 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fb291c6f-f3a4-3c08-98db-79257eb27747 | -13.91775 | -48.10439 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6603d73-7477-3083-9e7f-978aaec7023c | -8.91124 | -54.92869 | 2025-10-01 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9e77934-fe8d-3e23-9941-59de52d57cca | -15.33855 | -47.94145 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 892c4a86-35e2-3cb7-886b-254ed1144b6d | -10.44217 | -50.86603 | 2025-10-01 04:51:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9914cb66-fcce-32dd-8a1b-0919a356712d | -13.34846 | -48.16907 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f24f151-29ca-33ac-9eb8-be36098c3897 | -9.93877 | -43.64038 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1d3d8e7-a7fa-301f-8fce-1768a3b17794 | -10.90238 | -46.53474 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 3ec831b3-ebc4-345a-b2eb-872c27653ae8 | -12.96134 | -48.43062 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e424d0d9-5666-3ccb-84a7-efc596b9c0ac | -13.45705 | -47.2417 | 2025-10-01 04:51:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 243907d2-9e4d-3df6-89d8-f9a5f06fb01c | -11.56923 | -50.18911 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b10cfa06-43e3-3985-be18-1e2b5cfe1c11 | -15.34396 | -47.8416 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60d1f596-c473-3799-a1e6-e1e60aa67b5c | -13.8209 | -47.50496 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6edda579-5928-3642-a5ea-6f10f723457b | -14.89248 | -48.119 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d3443de2-949c-3838-bc99-e90282b88dcd | -14.89105 | -48.12917 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e2e4f8e-c4bd-3e52-99c1-f7d61e7b977b | -13.76353 | -47.95714 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 34f9950f-d51a-3eb3-9bcd-0aa537e07369 | -11.62628 | -52.24268 | 2025-10-01 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3be75165-8559-3bcc-8232-97004ede0e8f | -13.20606 | -47.32406 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1366411b-5b60-30ae-8adb-01b9aebca1ec | -14.6594 | -48.13288 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7ae9aa32-9661-3339-9c2b-f2d7c01f1a5d | -15.76743 | -43.70414 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32d50edb-e243-3645-937c-d8e1bea7fa87 | -14.68734 | -46.95898 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3a5075d-8fdd-3864-8311-80b54a46857e | -16.05634 | -51.02022 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd48c46f-b74c-383c-9c41-38669c59c47e | -13.3701 | -48.15703 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5da622f-4a44-3679-a4d1-8b270955b7da | -11.26884 | -47.2091 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2977d69-30e8-378b-8504-3401cde9e4f2 | -11.1521 | -54.30925 | 2025-10-01 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 17544ca8-aa73-372b-b267-e134ad80dcd3 | -13.1753 | -47.78649 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 891ef15f-a114-3016-bca4-770ebe2fbb99 | -12.81898 | -47.01466 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0a5f7aa-6a8a-3f86-a07d-998e8183a4d2 | -12.85334 | -46.95 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2d8f1b14-61b4-3801-9ffd-ee5b8772d49e | -9.92954 | -43.67397 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac2de05f-f38c-3049-bb63-0754b06af942 | -13.65064 | -48.02882 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2c4031e-5552-345d-b1fb-945636cf1145 | -11.27968 | -47.81131 | 2025-10-01 04:51:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82280b4b-f20f-3ea3-85e7-16daf1258576 | -16.40529 | -47.05389 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 284b1435-6146-3d25-8e70-98fe0e6777b6 | -11.42639 | -43.49867 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62a7a8dc-0ac7-3b56-ab8f-83bfe70ce35b | -14.18933 | -46.11967 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f813535b-eca5-305b-a90b-621d3402176e | -13.78464 | -51.2327 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 037f7b81-2212-3763-bf47-ad7db5d2858c | -15.26264 | -49.27532 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cdd13ee8-4dbf-3cee-bf4d-6fe8fe1403ff | -12.86644 | -46.94783 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ebf4ca1-0af1-3dc4-bbdc-11d68cf907cc | -11.64366 | -45.32689 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4fa112ec-6f10-36b5-bfe5-0e7f2eeaece0 | -9.55567 | -54.59554 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 856d6225-ced2-3016-8e0f-b62e7b5b1887 | -14.73046 | -46.8338 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3c3fbff5-7276-3902-8e68-31e5134256b4 | -11.6713 | -46.96197 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24e85fb5-1320-38dd-9d70-42c89b948483 | -11.63747 | -47.49037 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e43101de-1f26-37f1-82fe-81d1bb37c9ec | -15.29416 | -46.19479 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e8060e2-fe55-3cb3-ada1-23b42e13e2fe | -14.68679 | -46.96311 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 782d5edb-1270-3da3-99c6-9500aa37229a | -15.17465 | -49.07812 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 091afbad-b23e-392b-8f66-6a4862c7a7ab | -13.6738 | -46.78938 | 2025-10-01 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b56b2482-f5e5-3391-b03a-4b484d2ec7bd | -10.90549 | -46.5429 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2559d03c-0dbb-39b1-b0bf-2e2a400c4074 | -16.02671 | -50.90589 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d6ceac64-f23f-37a9-bba7-e7a22039dd7a | -14.04916 | -47.98751 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96c56326-d979-386c-b436-3db0286adb12 | -13.6761 | -46.78791 | 2025-10-01 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72f3f1e6-df94-3e3f-8750-0e698a62b4a3 | -13.77299 | -48.00597 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26942e89-7ac0-3357-9972-0ace92a80f65 | -10.97458 | -46.53984 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a30bd79-ffdb-3cd6-8ac8-fb3eff16b3c3 | -10.17519 | -44.90282 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 989e8969-9598-398f-ba19-331b052d8c3c | -10.47929 | -55.62407 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a398843-4285-3daf-8e21-1520ed92c09b | -10.63357 | -48.60323 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e135db8b-075c-3df0-a64f-52d7c1b1bf64 | -10.01961 | -50.25682 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2f93c86-3849-3df2-9249-c09d010ba929 | -11.18696 | -47.20528 | 2025-10-01 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b35b1fa-23b9-3277-b5e7-2ebd5d9b812e | -13.37284 | -48.10837 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e745fa-d560-3953-aeb9-c9899f9439b5 | -14.9856 | -46.96557 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9c8d835b-90df-3359-b440-f80875216ec6 | -15.12813 | -46.4485 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc7058cc-eb2b-3f53-a0ca-2619df3b62c0 | -13.29941 | -48.70041 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1bb2d36-430b-31a4-b630-6112edc696d0 | -13.6726 | -48.07365 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 40434cf6-206e-3075-bf03-9da1e7292145 | -9.33292 | -45.68875 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e49a12fd-dc2f-3000-a99d-764cda40c6aa | -12.43012 | -50.17404 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75cdea94-2d59-3ded-ad82-d041048ac5a2 | -10.77409 | -45.3649 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73406b1d-1131-3915-80bc-416886240e29 | -12.88874 | -45.26377 | 2025-10-01 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a312cc26-35d8-3adb-bee0-84d1d651d23c | -11.84477 | -45.00655 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9c01906-bb5a-3307-b1dc-51821ff93f91 | -14.51834 | -48.36942 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aea2d4ac-e78e-3bf2-8e14-71ed7c82d2a9 | -12.03905 | -47.90907 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 677a2cc3-ba6e-34c7-a737-34430838e783 | -14.92548 | -47.8213 | 2025-10-01 04:51:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45278b64-c59f-397c-8e59-27ad234b4c40 | -9.41209 | -47.33627 | 2025-10-01 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd992d39-f07a-31b2-a1f7-ca00646ad711 | -15.26482 | -47.84144 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4234342a-4824-3d87-9951-d1fa3b10c4bd | -16.01681 | -50.90017 | 2025-10-01 04:51:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ea2199e-5763-356f-a697-07528921ebf5 | -14.36792 | -47.13375 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README110.md)
