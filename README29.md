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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b857141-79e9-3c05-ae80-89476e442b89 | -12.74213 | -48.64814 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60bb95de-8064-30ee-bb9e-9052dab076d3 | -12.23886 | -51.13908 | 2025-10-11 04:34:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8004de70-1bf5-31a9-beed-389e80433416 | -10.5238 | -47.35107 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2795b62-34c7-3b67-a0b0-a5841453e4bc | -15.608 | -42.67041 | 2025-10-11 04:34:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 138a8852-75be-3971-b55f-6fc7680b367b | -12.04667 | -55.35461 | 2025-10-11 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 241ef0dc-92fc-3379-a8dc-68867acfb069 | -13.26095 | -48.01231 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4e573f7-84ce-33c2-ae46-ca5c22d06d62 | -9.44236 | -45.45655 | 2025-10-11 04:34:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e82836a-e80e-3ec5-9894-988d8b3892b7 | -13.45892 | -48.09531 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72295cb4-3dbf-3f6a-a813-113f23ab521e | -16.30015 | -47.16381 | 2025-10-11 04:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a765943-4806-3f88-a546-55258a0967c9 | -14.28142 | -45.90451 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e574da02-c2a8-3da0-abf2-6443c15ee73c | -12.75897 | -48.65057 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b46bd4ba-0969-3e8c-b5ce-7b37a9633b7c | -16.32505 | -45.05545 | 2025-10-11 04:34:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b08aa22-02a3-3096-84a8-0fd9ee83946e | -11.76242 | -46.36279 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b60facf1-f7b9-3903-8627-9f6faf050da3 | -15.55655 | -44.32569 | 2025-10-11 04:34:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf290e5e-fd00-3753-90e1-2a51ec78759b | -14.26847 | -45.88875 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8cda9652-7100-3634-8723-10909f5b20b4 | -9.10907 | -45.04573 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e25c84f-755d-3cfb-bd56-42a007b7e9b5 | -11.7643 | -43.31688 | 2025-10-11 04:34:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 197c1c81-7480-3561-b032-89b164cffdc1 | -13.68935 | -48.07791 | 2025-10-11 04:34:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 99293ffa-e2a3-31a8-ab04-f2d9b3917fab | -10.16779 | -44.55375 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e074b7b8-499b-381d-a234-4773ca9bff50 | -13.26432 | -48.01279 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fc35e92b-839b-34ba-a076-cf48d7996074 | -13.66858 | -48.74895 | 2025-10-11 04:34:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 027d88cf-72f3-316c-85c8-321ed7319315 | -14.95031 | -45.59233 | 2025-10-11 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d0a0df8-06a0-328c-9922-6c83247fcf96 | -12.74659 | -48.66324 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0a83124f-8c9a-3a2f-92f8-3883f241b609 | -11.19423 | -50.51726 | 2025-10-11 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e8869e3-795d-36cc-956b-5aa3aedeaf96 | -13.85657 | -45.84554 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db5b4da9-adf9-3cc0-9935-44219fef70a8 | -12.64051 | -48.31424 | 2025-10-11 04:34:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a6dc501-efef-3fbb-a8d5-f75e09961706 | -12.74713 | -48.65971 | 2025-10-11 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3715daa6-2b25-314d-9727-dc27ff2c411e | -11.02903 | -44.64471 | 2025-10-11 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 402c8529-b9d2-3724-9593-6a5de078197d | -9.08974 | -45.02472 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3d21fa15-f68c-3010-83bd-a296c517970c | -9.11189 | -45.07721 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 707f869a-89c4-3c2b-8cc1-83f50e7748d0 | -12.67949 | -51.1776 | 2025-10-11 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b819a1-8df0-336c-8e32-b0ff021b01f5 | -13.21752 | -42.33107 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e4caa36a-1771-3834-8ace-018c90457d24 | -10.52997 | -47.35572 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a84c6cb-5b04-335a-8563-20c091056cef | -10.52044 | -47.35055 | 2025-10-11 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f8d1708c-d5fe-31da-b53e-146a7c830fdc | -12.14542 | -48.01658 | 2025-10-11 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 55a5798f-c5d2-32f5-a3de-6f6dcc3ed428 | -15.69085 | -46.64095 | 2025-10-11 04:34:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f86fb9cd-86d5-340e-a900-1ef03a9fa6c5 | -10.11157 | -47.26939 | 2025-10-11 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49137be3-de5e-3247-8801-20f7cdf11419 | -12.90224 | -47.03476 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e148810-11d2-3898-836a-96dae3051330 | -10.42476 | -44.99866 | 2025-10-11 04:34:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6bb2605a-917f-318b-a711-72b3dab948f5 | -15.67989 | -48.13282 | 2025-10-11 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6cfa584f-f89c-3729-bd96-68f926da3c36 | -12.91936 | -45.05587 | 2025-10-11 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2a2f17b-e8c0-393a-8140-5aecc77cac4a | -11.77831 | -46.37696 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ba82231-c87e-3ce4-8cd7-26adea833af4 | -15.6833 | -48.13332 | 2025-10-11 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 323377bf-eb7f-31bc-8a9e-3b6131ac4e3d | -10.19853 | -44.60751 | 2025-10-11 04:34:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c0466e6-c53f-35cf-bdc9-26e0afe5f33b | -13.78087 | -45.41638 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0217d8f0-1d63-3a8d-9a2c-bead70346ac7 | -14.27897 | -45.89491 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5cd2345-eb80-3c64-8e91-9780ecc9a99e | -13.34172 | -48.48457 | 2025-10-11 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a07bd8a6-60df-3250-84cf-ec53974ca8b1 | -13.45556 | -48.09477 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e1a499f7-6248-3277-a9b1-36f92b938026 | -11.76182 | -46.36686 | 2025-10-11 04:34:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cea91134-0cb8-3c06-87ef-c2ad649c6c5c | -13.76702 | -45.40458 | 2025-10-11 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d02edd4-9bf0-39e8-80c2-477a718508b7 | -9.10435 | -45.02698 | 2025-10-11 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3faefd56-624b-36f3-9e70-08bece49b098 | -13.30782 | -47.98927 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08795641-ad16-3d99-819b-17d79d26e51c | -12.90001 | -47.04996 | 2025-10-11 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00865af0-5cd5-3a97-9d45-eec078722044 | -13.20706 | -42.33944 | 2025-10-11 04:34:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9c4a2c5c-a979-3502-9554-8ab1bd0ffbbd | -14.89602 | -47.22215 | 2025-10-11 04:34:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99a0f3c3-dbf2-301d-85bf-36c7668e5880 | -13.58034 | -47.42703 | 2025-10-11 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0381b809-1acc-3337-bab0-caea79e3010b | -17.27016 | -46.80024 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0462aa45-ace7-3ee4-80ad-ba346dc24347 | -17.51609 | -44.2882 | 2025-10-11 04:36:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3edec202-18d3-3e99-963c-1c04fc1992a6 | -15.01943 | -56.01933 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a52365a2-a8ab-3d61-9ce3-f6290c92e745 | -14.95404 | -59.43003 | 2025-10-11 04:36:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fddf40f-9ebc-32aa-88fb-7ba3094a6a65 | -17.89111 | -57.50933 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cc4aee9c-3c71-327b-9027-a713120ad574 | -17.81772 | -57.6613 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| c9ea6781-2943-3f5c-9976-de88e9bb967e | -16.30966 | -47.14817 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2f50192-3b03-3411-a22c-a5e7b353f806 | -18.0553 | -57.56071 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5dee68c2-5621-3fec-abfd-1e6eb1fa5d35 | -15.18962 | -56.78955 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45d36440-a462-3c14-b1e3-4bc6dc7b8f9a | -17.81327 | -57.66006 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4ed7b7b7-a21b-3556-a7f1-bd2a54299725 | -17.24431 | -52.26647 | 2025-10-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b1f6901-a349-37ff-852f-be41f79a649e | -16.0186 | -59.54499 | 2025-10-11 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f522f48-a514-3335-869f-9b03dbf7b9b2 | -16.79906 | -47.68869 | 2025-10-11 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e15db88e-3672-37d6-a630-301e53dbe50c | -19.72866 | -43.897 | 2025-10-11 04:36:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d941fefa-3f09-3b7a-be16-69cd356b6fd4 | -17.83633 | -57.66201 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e183f15c-20d9-35d2-88b0-56e4814b179f | -18.07487 | -57.53109 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 03dc5fbe-bbcb-3170-bb0f-2180e2f5b029 | -17.26348 | -46.90383 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7df8e90e-b9d8-3924-8ab8-5b55f97e25f5 | -15.15667 | -56.81727 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c338e4fe-7994-33c8-b317-ddcb74f1caed | -18.24426 | -55.37811 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e2b5863f-7c34-3baa-9d81-2020f6e59817 | -15.19235 | -56.86046 | 2025-10-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d089f13c-cde2-3a09-b148-ffc2fea50db7 | -17.82103 | -57.66843 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 644cff8a-329b-335a-a825-ff02d36532aa | -16.83734 | -43.18453 | 2025-10-11 04:36:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20ca5893-4c2e-3e56-8387-8597d7e592f6 | -15.01738 | -56.07779 | 2025-10-11 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0206e763-0af2-359d-91b7-65f0b67e5445 | -17.38882 | -46.86095 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e3f6e31-7e5f-39ba-8dd1-b38a7d2ffe01 | -18.07308 | -57.54049 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d22cc0b8-8813-3695-8523-6eb79ca8641a | -17.20692 | -45.88966 | 2025-10-11 04:36:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2abf0c2-5580-3909-b913-ccd4c935c5a9 | -17.84786 | -57.65744 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3e717d74-e85c-3ffd-b262-d8ed36d955ff | -17.84621 | -57.65933 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f31758fb-3a76-348a-9bcf-524ba5403199 | -17.3961 | -46.8623 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55c572aa-e197-3e17-8ab9-b698a2721953 | -17.20786 | -47.33275 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c56243b5-11a3-312c-97f4-308de46160f8 | -16.30312 | -47.16848 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4bd4a39b-b27c-384a-a9f5-c53c3895a049 | -15.19505 | -56.79761 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d998133c-98b4-3a77-842d-6529216b07ff | -15.1603 | -56.82273 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11f13097-7dbe-35e5-a24c-7cae76de5c9e | -18.81271 | -54.97089 | 2025-10-11 04:36:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8332de6-2cb7-3700-b34e-3486d770b6e1 | -15.19228 | -56.77508 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b98d296a-dc50-35a4-b867-e2fa2c03233d | -19.33089 | -45.79185 | 2025-10-11 04:36:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dcdf8173-9c4e-30f7-9eaf-82ee5ac74d38 | -17.26774 | -46.89995 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4183eb84-c752-3a62-b7db-772d3b1138b9 | -16.0135 | -59.54308 | 2025-10-11 04:36:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d35b84a6-d12d-37be-835e-7e0cce7a36f4 | -18.63305 | -43.93647 | 2025-10-11 04:36:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d19903-f82a-37a8-a9fa-51b9bd3c78cb | -18.589 | -46.55049 | 2025-10-11 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 133aba3f-6de1-3d3b-b4b1-dd1199545631 | -15.01036 | -56.06791 | 2025-10-11 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 130e6dc2-7438-391f-ac0a-a2c8251f3a94 | -16.3037 | -47.1644 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 87cc3fa2-01fb-382a-9fb7-6a284bd519e9 | -14.94804 | -59.43228 | 2025-10-11 04:36:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ffb3355-c11f-3ed0-9204-fff051f2c728 | -15.18962 | -56.77751 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README30.md)
