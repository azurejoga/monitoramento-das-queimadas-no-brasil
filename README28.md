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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 445f368e-c181-35f6-bbb4-cb08607338e9 | -15.3764 | -58.160099 | 2024-10-01 01:45:12 | METOP-C | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 75ce2f6e-4980-3d99-ab39-f73a8b472d93 | -15.3784 | -58.168499 | 2024-10-01 01:45:12 | METOP-C | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e356aa-91a1-3f02-8aac-9c1c8eeb6e19 | -13.5619 | -51.136101 | 2024-10-01 01:45:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ba8805ec-8c2d-32bc-b822-30d0f028057d | -13.5685 | -51.160301 | 2024-10-01 01:45:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7b5d631e-6272-30d3-a0e4-fb75164ad60a | -13.5751 | -51.184299 | 2024-10-01 01:45:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3ac9b7af-b0b4-3fe4-9f78-a5b2b93dfdb9 | -13.5816 | -51.208302 | 2024-10-01 01:45:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eea58b62-9c27-3594-bc71-ff8d3b898136 | -13.5456 | -51.1147 | 2024-10-01 01:45:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d106542c-488d-31ff-bb55-131c60f07aeb | -13.5523 | -51.138901 | 2024-10-01 01:45:13 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 09f6358c-470e-380c-a00a-d13e7f8549ff | -15.2769 | -58.1763 | 2024-10-01 01:45:14 | METOP-C | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b16e545-79b2-3dcc-af8b-8e05f0004349 | -13.2361 | -51.229198 | 2024-10-01 01:45:18 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dfd5a8b3-a8af-3997-b73f-a664f60bd1e0 | -2.4048 | -50.3085 | 2024-10-01 01:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 009959af-de28-30e5-b845-c2d7653f1983 | -2.4047 | -50.3295 | 2024-10-01 01:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 489.2 |
| 7bb81ff9-6793-3d51-b42d-328a1f1f74fd | -2.4046 | -50.3505 | 2024-10-01 01:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 704795ad-aae2-3bce-8609-96eb844e1056 | -2.3863 | -50.309 | 2024-10-01 01:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b72187fe-6b8c-348f-9589-7c070553123f | -2.3863 | -50.3299 | 2024-10-01 01:45:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 183.6 |
| 949e8106-292b-35c0-acb9-3f3a4199df37 | -2.3862 | -50.3509 | 2024-10-01 01:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 6ee473c0-3f24-3d2d-8746-02c4dddfc7b3 | -14.8818 | -57.9958 | 2024-10-01 01:45:20 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8568eaf4-7806-35c4-8368-e2388d7cdb3f | -14.8839 | -58.004398 | 2024-10-01 01:45:20 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61331d40-f5bc-36be-9aef-1b1df74cdbaa | -14.886 | -58.013 | 2024-10-01 01:45:20 | METOP-C | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f32ae069-0fb3-31c1-897b-510e8c4fbd00 | -12.9603 | -51.202702 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10e1c01b-5ca2-3803-b7ea-62a571bda611 | -12.967 | -51.2272 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 92fe49c3-0b5d-3329-b08c-31239f907d69 | -12.9736 | -51.251598 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0d90fc47-4ddd-348b-9f6a-29f522180966 | -12.9803 | -51.275902 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9233cde1-038a-3321-9f0a-97f812f3d83a | -12.9934 | -51.3242 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d48345a3-aa34-3d6f-aeda-a895d9fbe393 | -13.0 | -51.348202 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5dee98a5-1203-3700-bcd8-87552fd8e934 | -12.9507 | -51.205399 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b1b8d3a2-b217-3aed-80c9-9b0ee7313ae2 | -12.9574 | -51.2299 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df858115-1281-39d0-afe3-6549785c0aa6 | -12.9641 | -51.254299 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 514fc278-b362-3c2c-a715-c07b32bcf934 | -12.9838 | -51.3269 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6bc8ea0b-7d36-3528-b85a-cf30f1cf6172 | -12.9904 | -51.350899 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c5df8a8-ff1d-363a-a5cb-ccd3fb558102 | -12.9969 | -51.374802 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 028df425-6afb-3b03-9bf0-d3846f9bd290 | -12.9411 | -51.208099 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa00785-0ec0-341b-a2e4-f53f7e84d9e0 | -12.9478 | -51.232601 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d87aae6d-12d3-3c71-a2b1-9245fe500208 | -12.9545 | -51.257 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51dad7cc-e377-3384-a279-b0f32f6a5d75 | -12.9677 | -51.3055 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66ae4d91-a47e-3472-a31e-3f2d5e5adef7 | -12.9742 | -51.329601 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 114e8a3c-00ba-3fa5-bd73-26108e76d808 | -12.9808 | -51.3536 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e21b2d4d-2aed-3edd-9fdb-71895c7c8dc0 | -12.9581 | -51.308201 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d11a199-6d6f-3541-901f-d65b708f1665 | -12.9646 | -51.332298 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46ff9f75-4c60-32db-918c-a57a355e0aab | -12.9712 | -51.3563 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 41013829-9260-3072-971d-cc15b6a833b1 | -12.9485 | -51.311001 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 869ee117-dbcb-3df9-83f8-cbdfe7a9c9a8 | -12.955 | -51.335098 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c365dce-838a-3aeb-86ea-0dd3251a6dad | -12.9616 | -51.3591 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5bdbf3cd-2a74-31cb-911a-1a20bd0f16da | -12.9454 | -51.337799 | 2024-10-01 01:45:23 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cb29d72f-a4e5-3b96-96ea-1b2ea288ae57 | -3.0282 | -51.3345 | 2024-10-01 01:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ef4ebfcc-51f2-342a-b868-3704ee00fc6e | -12.9131 | -51.294899 | 2024-10-01 01:45:24 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5080532e-c3cc-3688-89fa-a8b29875def4 | -12.9197 | -51.319099 | 2024-10-01 01:45:24 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d4e62a93-2cf6-3d10-afd1-c6df6890c77c | -12.9035 | -51.2976 | 2024-10-01 01:45:24 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05053806-4f5b-3690-b28b-aee0be315d95 | -12.9101 | -51.3218 | 2024-10-01 01:45:24 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9fdb8b4-d947-3dd4-9a05-f7a1f66bb860 | -12.8748 | -51.305698 | 2024-10-01 01:45:24 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5469c3a8-11e9-30b7-9c58-623e2fa6a2a3 | -12.1407 | -50.059399 | 2024-10-01 01:45:31 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f79132c2-34b7-3ce9-b558-71be13262f14 | -12.1312 | -50.062099 | 2024-10-01 01:45:31 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f02a315b-6039-3077-8153-b9e9960b6a9e | -12.5966 | -53.4772 | 2024-10-01 01:45:38 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fbf5768e-21b2-3056-a152-0571f611c79d | -12.6012 | -53.494801 | 2024-10-01 01:45:38 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2c88833-981b-3092-8f39-491b6b33afed | -12.4971 | -53.1371 | 2024-10-01 01:45:38 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39653708-21b9-391f-b1c9-0ceb46d95f01 | -12.5019 | -53.155602 | 2024-10-01 01:45:38 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2286d8-bb0a-3e0f-ab5c-66fe190f3945 | -12.587 | -53.479801 | 2024-10-01 01:45:38 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1dba714-a008-3563-8087-5bd446163a7a | -12.5915 | -53.497398 | 2024-10-01 01:45:38 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| af8c40e2-b97a-3a3a-b307-29c412070192 | -12.4922 | -53.158199 | 2024-10-01 01:45:39 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9509ab66-e133-3e4a-8e23-acd9b8d1ac7a | -12.4971 | -53.176701 | 2024-10-01 01:45:39 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6410750-65ad-3ac8-9d92-8f65ef36db32 | -5.9788 | -45.3621 | 2024-10-01 01:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b38588c5-e498-399c-bbef-9ecf1380b3f8 | -5.9786 | -45.3847 | 2024-10-01 01:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 938301db-69b4-3829-8af6-18c5c83ea5e3 | -10.9301 | -50.070702 | 2024-10-01 01:45:50 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f39639e-dc9f-35e6-b86b-ef8278411364 | -10.9206 | -50.073399 | 2024-10-01 01:45:51 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c6c3e0e-5445-3975-a3fb-43f2098f9db6 | -10.9111 | -50.076099 | 2024-10-01 01:45:51 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0eafcc27-917a-354d-aa64-26d50e4405ee | -12.9843 | -62.688999 | 2024-10-01 01:46:08 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aff92eb0-c046-3883-b702-eb1d85b7242d | -12.9859 | -62.696098 | 2024-10-01 01:46:08 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86c13cf9-6ee2-3793-84c2-15ab0f25616e | -12.9778 | -62.705399 | 2024-10-01 01:46:08 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3998eeb-dc0d-3e95-a7f2-e403cc162bef | -10.924 | -50.0854 | 2024-10-01 01:46:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 44e87edd-8d0a-3f02-b5ac-fd759d57b0c2 | -12.9095 | -62.6763 | 2024-10-01 01:46:09 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9bf1a1-bd50-3ebd-9195-0e9ff563140d | -12.9111 | -62.6833 | 2024-10-01 01:46:09 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e45cbfce-b2ae-3267-8bf3-a5077bdcd216 | -12.7728 | -62.894199 | 2024-10-01 01:46:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b189463-2aef-3102-88d6-ae999d35ac8d | -12.763 | -62.8965 | 2024-10-01 01:46:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3edd0033-7d65-32f7-a30c-22f9c4299877 | -12.7646 | -62.903599 | 2024-10-01 01:46:12 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa651598-1a97-3989-aeaf-0dac1169b3b1 | -11.6744 | -64.9793 | 2024-10-01 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6717f8f7-e354-3ee0-aee3-967a58b1377d | -11.6743 | -64.9983 | 2024-10-01 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 18da2344-ef08-358c-a289-b7832a7300ad | -11.6556 | -64.9802 | 2024-10-01 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3988058f-d78d-38b5-bcbe-f69837583577 | -11.6555 | -64.9991 | 2024-10-01 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 8f353f54-e355-3750-884c-58f5f69f6854 | -12.6039 | -53.4879 | 2024-10-01 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 994cd0ea-bf05-394a-8003-821ab809856d | -12.9228 | -51.307 | 2024-10-01 01:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6b67d15c-b594-3b93-8057-8e1611687a8d | -12.9037 | -51.3094 | 2024-10-01 01:46:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ea36d2a3-a5d7-3f33-9bc7-7f46ce29533a | -13.5957 | -51.1796 | 2024-10-01 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| c6e51dc7-5a6c-32ab-a64d-d030df2007ea | -13.5954 | -51.2011 | 2024-10-01 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 532bc38b-dca7-3875-a1ef-85eaab2ad75a | -13.5765 | -51.1821 | 2024-10-01 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 7040b2b3-a054-3d95-acbf-3cf60a60596b | -13.5761 | -51.2036 | 2024-10-01 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 7b54f2dd-078c-3903-9bd3-2a6305636ec8 | -13.5583 | -51.1203 | 2024-10-01 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b6ede8cb-a0a4-3e84-82d0-0f2491ea2b7a | -14.7406 | -48.7498 | 2024-10-01 01:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| bd2d8f1c-8a8f-3bbf-8460-95d7019aac69 | -14.7402 | -48.7721 | 2024-10-01 01:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 65a4b5b7-4b29-3322-9e80-ab35013a0a3a | -14.7211 | -48.7529 | 2024-10-01 01:46:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e1896e0a-cad4-36e7-bd89-faa8cf27a6b8 | -14.7596 | -48.769 | 2024-10-01 01:46:29 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c2f708f7-7d1d-3ecc-bd02-544b2ccc1874 | -11.6687 | -64.980103 | 2024-10-01 01:46:37 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 93ffa684-4294-362e-838b-a9b51dc11bfe | -11.6704 | -64.988197 | 2024-10-01 01:46:37 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 74fcad73-21ad-3bde-a4a7-3bb2e505cba1 | -11.6571 | -64.974197 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 09ac1cd2-212d-370a-a048-08b4fbad96c0 | -11.6589 | -64.9823 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6514cf15-b2e8-3454-9f3b-5ae5d0f1947c | -11.6606 | -64.990402 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 182c9916-d5fd-3d1c-98a3-18aaf0295501 | -11.6624 | -64.998497 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 99b0ec57-b06f-3d01-92cf-d6789446dc6b | -11.6491 | -64.984398 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 272f34a6-baa6-3f29-9859-5d02fb3fcfdd | -11.6508 | -64.9925 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd407055-61cf-3ca7-bb2a-f0114c8a1d79 | -11.6526 | -65.000603 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cf32a5f2-2954-38b9-b71b-543fdaeb84a4 | -11.6623 | -65.187302 | 2024-10-01 01:46:38 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README29.md)
