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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 080b37b3-cbcc-3b4b-b53a-d6baf6d0b003 | -10.77732 | -68.72881 | 2026-09-28 05:31:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d275049c-582f-31d2-961f-0fe303129fa4 | -10.55796 | -68.56166 | 2026-09-28 05:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85ec4733-9c0c-3005-b869-fd072822ad89 | -9.93121 | -60.71996 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e7622df-426b-3312-afae-115127032aaa | -13.69092 | -48.82025 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b1851d16-0b3a-32bd-b1b5-b9489c7a6704 | -9.22136 | -67.59731 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc3f1af7-22d7-3a1c-944f-ea65d6162da1 | -10.82644 | -60.74787 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 765e41d7-24f8-3155-92bc-c4ea2bf9f623 | -12.29313 | -50.26575 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aae7ad06-d693-34d3-8adf-5e476a764071 | -10.17077 | -63.05962 | 2026-09-28 05:31:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7080246-4479-399c-b753-c5474421c2f9 | -13.97495 | -54.00743 | 2026-09-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6107d0c1-e77b-3758-ad98-4ad76b21ea09 | -11.33765 | -54.11381 | 2026-09-28 05:31:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d02b280-b2a9-3244-b482-68e5ddb4eec6 | -13.97027 | -54.00385 | 2026-09-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 471f5d29-fa37-35f7-936a-b7bf7820bad2 | -11.90945 | -50.61357 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 47ba43c4-e473-37f0-9717-6a118630f29f | -12.29063 | -50.26298 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac5f4519-fe4e-346b-9565-bcf329f86f2b | -11.54851 | -50.50826 | 2026-09-28 05:31:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9051ae31-3f34-364f-aef8-d3033b23b78a | -13.46466 | -48.59644 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f341c622-cb37-3ac9-8116-f15721f692d9 | -10.17474 | -63.05653 | 2026-09-28 05:31:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 587e4d27-5018-3f8c-9d39-c8835d989874 | -9.92733 | -60.72297 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 321fb98e-5f6b-371c-b2f0-b5ed323afa59 | -15.10179 | -53.88555 | 2026-09-28 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86a629be-b140-32a2-9842-f4262df09513 | -12.28565 | -50.36484 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91c31898-9da4-319b-9b14-56dc6a9631b5 | -12.76373 | -54.04349 | 2026-09-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6373a955-db4e-3704-9c06-6f1fd08e5a69 | -11.78702 | -51.05093 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10cef575-23e7-3c75-be28-7b23ed881168 | -10.88626 | -61.40953 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d989904a-00b0-3fc5-aff0-8c289fb3b670 | -14.90107 | -49.50001 | 2026-09-28 05:31:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1361214-9b53-3bca-9178-30226acba742 | -11.54792 | -50.51302 | 2026-09-28 05:31:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 54d5d80a-a073-3d2a-baf4-17d014f6a2ea | -13.1531 | -48.55085 | 2026-09-28 05:31:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 795cf849-16b7-34a5-b8ee-65bf9ab3e603 | -10.82386 | -61.41747 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 922ccb02-a860-37e8-a092-1b9436a17bbc | -15.10216 | -53.88235 | 2026-09-28 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed54b609-d9ec-3265-b68b-bce4f75dc8ed | -12.21458 | -50.35929 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aba1ddf0-c0c0-38f7-bcc5-3c14f3e99559 | -13.4626 | -48.59287 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5a8a4cd8-d363-3333-8436-9d0485497851 | -9.22569 | -67.59808 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aef779bf-b7a2-3701-92a7-66431be2561d | -12.59057 | -51.96027 | 2026-09-28 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78e9c8da-7567-3d97-89e5-1fe75a5de62e | -9.19561 | -67.7412 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 594e969e-aa9c-3893-9a91-c648e389f998 | -13.15363 | -48.5458 | 2026-09-28 05:31:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2946f483-fc21-3bb1-892c-cb06cbba1ec7 | -12.27938 | -50.36407 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04b79ee4-c410-3ff7-9402-b89f663cd2d0 | -10.65149 | -58.77496 | 2026-09-28 05:31:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5bd3644-0103-366f-9c3a-6e96bd64f7a0 | -11.77699 | -51.06185 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6f707081-852c-31fb-97d4-8a5f08dd2c41 | -10.82497 | -61.41046 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3be47948-a94c-3b09-b683-2a64e896b844 | -13.47113 | -48.60247 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3e62602-a1e6-3af1-8bb3-80815434fe43 | -10.82163 | -57.22097 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8c532ce-3688-3c9c-aed8-97c50d3a0e86 | -11.54787 | -50.51013 | 2026-09-28 05:31:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 23137b39-1e6e-3180-9261-a36294a32df6 | -12.21916 | -50.35402 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 88ee1cee-8f71-3508-9c3a-e1c6073d0261 | -13.45698 | -48.60143 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d8fcee45-5149-31ea-9ce8-f77a45445868 | -12.13912 | -60.7733 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c6af2e2-bd66-363d-b83f-6a2a51df0dcf | -10.81976 | -60.74681 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3144d723-a1c6-3196-909b-a19720170043 | -12.59009 | -51.96428 | 2026-09-28 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97ebb8cd-96cf-389f-b11c-d99e89e2d8e9 | -10.64661 | -61.74387 | 2026-09-28 05:31:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 209ef614-2593-3d29-83ea-4c53e3bd92bb | -9.53807 | -63.56263 | 2026-09-28 05:31:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8705495-94bc-39e0-bbdd-3a257f444fc7 | -13.71945 | -48.81743 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71ccafd8-e483-3026-b097-4c4bf35a9e36 | -9.13477 | -67.93578 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9ae3999-3376-355c-af50-216b22454b55 | -10.82092 | -57.22589 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2e999fea-bdf2-3dd1-92b3-e08d5510e610 | -15.11251 | -53.88364 | 2026-09-28 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a6041ca-9479-3670-8b95-988533b3059f | -10.82022 | -57.23081 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc6034d5-fe30-320a-916f-b6371d95704d | -10.54717 | -69.23231 | 2026-09-28 05:31:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e87d3ef7-dd4b-3a90-a912-a33dcf0055c1 | -11.78346 | -51.05819 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca11e217-7388-3dc9-a29a-70793ccb99d4 | -12.28683 | -50.26499 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c85c61e6-9908-35cc-9bd3-e8af56cf5e75 | -18.74792 | -53.28598 | 2026-09-28 05:33:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1713446-31bc-3212-8176-5a1acdcd7593 | -20.83596 | -57.69951 | 2026-09-28 05:33:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3b53b086-a4ad-3185-8ab8-2c1faf35da76 | -20.8403 | -57.70011 | 2026-09-28 05:33:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 05591d13-0e2b-3838-9c2b-c2135a6e6629 | -28.75714 | -55.605 | 2026-09-28 05:36:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 16b22f08-f3e5-3504-81ab-dd470699b800 | -28.75745 | -55.60113 | 2026-09-28 05:36:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 2412263d-41bd-36a9-98e0-d7da0e4a4933 | -28.752 | -55.60049 | 2026-09-28 05:36:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 420e68df-7428-3d81-aae7-34deaf8dafe7 | -28.75683 | -55.60883 | 2026-09-28 05:36:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a37a9c1d-9758-3ecb-849a-b6d831dbf6a5 | -7.87542 | -61.18334 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0842d4f2-7424-3ed7-819b-ca23dc39976b | -7.87761 | -61.18389 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f213c9c4-760c-3e84-9d0f-2178fd58781f | -7.86285 | -61.1936 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 057d2bff-c853-3281-9b3e-ea6658c4c381 | -7.87024 | -61.18866 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f91b47c2-92ba-3e93-a1b1-d5f2cb3036b4 | -7.86947 | -61.19454 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3add9bdd-10e7-3daa-b4cc-be8d314fa16a | -8.66407 | -64.02995 | 2026-09-28 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d3e9eb1-6a71-3d5c-b87c-0f8f02e9b6ae | -7.86881 | -61.18231 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ca2a4616-a404-3a50-be0d-9ac5a45e569b | -7.86808 | -61.18821 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6c1ef9d9-8476-37f5-be38-5f7f018ea7bf | -8.60829 | -64.06438 | 2026-09-28 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49a20ac1-04d9-3e02-9029-ec14487a23a9 | -7.86144 | -61.18739 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb33fb12-3650-3cde-9afa-c012f70f97bd | -6.98162 | -71.68527 | 2026-09-28 06:14:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eb2f2ba-f53e-3e50-961d-f3e525d92940 | -7.86735 | -61.19406 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 84f0dc34-a8d2-3308-87ed-84aacab1335c | -6.97821 | -71.68476 | 2026-09-28 06:14:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b3002b8-fdf8-35dd-aa95-85bf320992bc | -8.60878 | -64.0606 | 2026-09-28 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8943e014-2a10-310a-b5dc-d3d7a494fbe1 | -7.87101 | -61.1828 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ab9fd75a-a763-3d39-94d2-bbbdc494b984 | -7.86359 | -61.1879 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0933724d-da77-3eea-8425-97c58e712bfe | -7.87469 | -61.18923 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2866c96d-0719-3aea-b094-090416c41b9d | -7.87683 | -61.18979 | 2026-09-28 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 86808d7f-8834-3ab4-8cfe-bd78a1d1366e | -11.19 | -44.8 | 2026-09-28 06:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 576a0b4e-1a63-3923-bc55-7d5840a768fe | -10.81566 | -60.73865 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 24a1040e-cc83-31b5-a235-6bbbc44b10b3 | -10.82675 | -69.50873 | 2026-09-28 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73bfe5fb-a948-3c01-958c-220010fff3c3 | -9.19689 | -67.74086 | 2026-09-28 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d55e2f35-b1a9-3379-a68e-419081b23c55 | -9.92859 | -60.7155 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25d582b2-e30b-30d2-9ab2-850c46f844ab | -10.82493 | -69.50888 | 2026-09-28 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfc7a797-c7ca-33d7-ae36-8c981e6ede00 | -9.17007 | -67.67548 | 2026-09-28 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ceadfeab-a8ad-3699-bab2-7045156e8bb3 | -10.82358 | -61.41199 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 809e5496-d10c-3719-acc9-2c922f242c75 | -10.80334 | -69.50174 | 2026-09-28 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ea802f1-a3b7-320b-bdca-8f2f39f405b6 | -10.5471 | -69.22995 | 2026-09-28 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45945609-67d6-342c-9649-0dada2e069e0 | -10.55898 | -68.15868 | 2026-09-28 06:16:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fdb1c22-1484-3112-a6af-b0e38b1ecda9 | -10.25325 | -68.62112 | 2026-09-28 06:16:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db633413-1105-3972-904c-5f769bed4e67 | -10.55923 | -68.56173 | 2026-09-28 06:16:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30b21aec-5a15-3d51-983e-4382ec664a10 | -10.16972 | -63.05759 | 2026-09-28 06:16:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 734ea254-c626-3f56-9abf-251339fd8b57 | -10.12231 | -69.14698 | 2026-09-28 06:16:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 224d0ab6-1101-359a-9c0a-f1fbb2c95546 | -10.5037 | -69.35484 | 2026-09-28 06:16:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f79704f-4793-339b-885c-7ed9a202249c | -9.20127 | -67.74152 | 2026-09-28 06:16:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7395f6b5-4474-32ee-9586-524be0c6924e | -10.82191 | -60.74656 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5067908d-30b5-3c14-9267-98dbf1c58d79 | -9.9268 | -60.72297 | 2026-09-28 06:16:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c10d54eb-e84a-348e-8d23-d073a0b50468 | -9.16329 | -61.40724 | 2026-09-28 06:16:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |


[Clique aqui para ver as próximas entradas](README67.md)
