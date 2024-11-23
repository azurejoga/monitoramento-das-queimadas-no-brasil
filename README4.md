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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7a98dd4-2f31-389c-9809-7afc2619fd00 | -2.6466 | -46.243198 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 68400df9-bac1-3f4f-a332-c5a29345432a | -6.3462 | -39.795601 | 2024-11-23 00:00:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| cede3a61-e61b-3bf4-b76d-0088550b7c42 | -7.6839 | -42.987 | 2024-11-23 00:00:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 94a9470a-1ab8-3439-8613-52b8d171bcfa | -2.9348 | -45.611401 | 2024-11-23 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f86d4918-4f98-31ae-be7b-b83e038ece43 | -4.5597 | -48.0098 | 2024-11-23 00:00:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d56188e4-a1ac-383b-9b9e-0b8c3c59967d | -5.7543 | -46.2467 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3da0018c-b8c9-3c73-823a-1c3f34f037b8 | -10.0413 | -36.118198 | 2024-11-23 00:00:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af69972a-e208-316d-9c92-300b1efd9b93 | -5.7445 | -46.248699 | 2024-11-23 00:00:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8583f992-737a-3bdd-9838-e689af86ab40 | -6.8621 | -39.570999 | 2024-11-23 00:00:00 | METOP-C | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2f250a17-5d35-3842-85db-97e197699f5a | -9.632 | -40.540501 | 2024-11-23 00:00:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4bb88c09-243f-3c72-a35f-5d6953d56dfc | -4.6774 | -45.666698 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ddefd83c-bc37-3217-835c-07bd7537ba8b | -6.1496 | -46.661098 | 2024-11-23 00:00:00 | METOP-C | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9fb9b3ea-f28b-3c32-b645-b5cc73ee975e | -9.7361 | -37.027401 | 2024-11-23 00:00:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 331b2cbc-7f46-373e-991a-f682cf16893e | -3.9331 | -47.198898 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a90ba859-36c4-3eb4-9a71-7a11d91ea49d | -10.0431 | -36.125599 | 2024-11-23 00:00:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dacd6741-822a-3d33-af5f-fd75398a30e8 | -3.6584 | -43.213799 | 2024-11-23 00:00:00 | METOP-C | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be55d162-0114-3cbd-9998-4a032bf8f608 | -8.6628 | -36.983601 | 2024-11-23 00:00:00 | METOP-C | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| db057ace-fe26-3288-aee8-a7a078a5c190 | -3.1423 | -44.4813 | 2024-11-23 00:00:00 | METOP-C | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a2aaffa2-3a18-34f4-b289-a4b58d50046d | -9.9276 | -36.339298 | 2024-11-23 00:00:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 62e7c47c-7a91-3914-b1da-6f32eae340dd | -3.1337 | -44.397499 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d2a1799c-3b13-3e65-b194-cd262915926f | -4.5067 | -44.711399 | 2024-11-23 00:00:00 | METOP-C | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6febc3c5-a3fa-3ac4-a268-2a543f88b5ee | -3.9496 | -47.965698 | 2024-11-23 00:00:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3515b39b-98a2-358f-ad0d-671e33bd2ffc | -4.3543 | -44.993801 | 2024-11-23 00:00:00 | METOP-C | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d6d5b8a2-7e53-3276-85c1-d9e992a630e5 | -4.0347 | -46.181999 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef0bb544-8919-31a5-a45b-8bd661a03e2a | -10.5051 | -36.691799 | 2024-11-23 00:00:00 | METOP-C | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1faa45a-4c9d-3223-a8ff-99276a869a55 | -3.1336 | -44.260399 | 2024-11-23 00:00:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ead6a26a-daf2-3eed-a640-f435ffc19a46 | -10.076 | -36.4888 | 2024-11-23 00:00:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c81634fa-c4ff-37f6-b7f0-8e3ded062473 | -6.4917 | -47.022099 | 2024-11-23 00:00:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 618e27e0-8504-3e92-87c5-db400be834d6 | -4.3667 | -45.0033 | 2024-11-23 00:00:00 | METOP-C | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 23f0b2ac-f2de-376c-abbc-485d95c19416 | -4.6676 | -45.6688 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b79cfd9a-b8cd-3303-a6ed-6a66f81ccad3 | -7.6154 | -43.001801 | 2024-11-23 00:00:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f78c668a-fcf8-387c-ad91-035149bb7ed7 | -7.0521 | -40.412701 | 2024-11-23 00:00:00 | METOP-C | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6ecb2722-c7c2-3444-a0b3-cb35f7b7d98e | -4.5364 | -45.8619 | 2024-11-23 00:00:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f3f0db2e-992d-3812-9b08-c4909b6f3946 | -2.7304 | -47.526299 | 2024-11-23 00:00:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfd2e335-80cf-3f41-975c-a61c4bbdbe8b | -6.0338 | -39.690601 | 2024-11-23 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| e33aa352-e277-3466-8af9-a9272800b6d5 | -3.742 | -50.019199 | 2024-11-23 00:00:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa280ec6-51f9-39e1-b0b7-282174b3e6d2 | -3.7462 | -49.991901 | 2024-11-23 00:00:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7d457f6-efb6-35c4-b8c8-74e0a7d9b229 | -6.219 | -39.4175 | 2024-11-23 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7e96b80c-33ee-3309-a5ae-bee4ff6f5a0a | -4.6069 | -46.506199 | 2024-11-23 00:00:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fd8f2568-1a4b-39b9-9aae-e39f5dcaea9e | -3.7262 | -46.036499 | 2024-11-23 00:00:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b17e30f5-1cce-3f00-a080-37e5c74aef60 | -4.8971 | -47.411499 | 2024-11-23 00:00:00 | METOP-C | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99aaab1c-4ba3-3408-a836-a00f9ea78ee8 | -4.5265 | -42.913502 | 2024-11-23 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1da4b2ce-cc83-3787-a698-606ce8aa78a1 | -3.889 | -47.9217 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a7ff3f-a383-3b5e-b205-46e86315a538 | -4.1252 | -43.2327 | 2024-11-23 00:00:00 | METOP-C | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a5b9874-3fe3-3763-81b7-e1c042ddf23c | -3.5314 | -43.334499 | 2024-11-23 00:00:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee66477d-ae0e-3c7f-9235-a1ea9970411c | -3.6746 | -47.1376 | 2024-11-23 00:00:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc411104-0a3c-37a2-90d6-a53de623a50f | -6.3576 | -39.8004 | 2024-11-23 00:00:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 91d2e061-7599-3abb-9622-b4994ce88a1b | -6.1468 | -46.695202 | 2024-11-23 00:00:00 | METOP-C | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8f3a2d-1030-32f8-9e39-728fb1a79d93 | -8.1585 | -38.2449 | 2024-11-23 00:00:00 | METOP-C | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| dd0748a6-951c-3336-a2c9-fb19186dcaab | -4.6858 | -44.409599 | 2024-11-23 00:00:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed611efc-8b93-344c-8072-e6444c14729c | -2.8301 | -45.146198 | 2024-11-23 00:00:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f13f9e2-cb4f-327d-8a03-172286d79932 | -4.7216 | -45.496498 | 2024-11-23 00:00:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11b8a03f-0898-3d75-b82d-21b0a8d9a6ce | -4.4158 | -44.118099 | 2024-11-23 00:00:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29440dc0-ab3e-34ec-a3ab-b158b6ec3dc7 | -2.714 | -46.2701 | 2024-11-23 00:00:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5413bb55-e2d7-3224-8139-932c2b0a29b4 | -6.356 | -39.7934 | 2024-11-23 00:00:00 | METOP-C | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 97052a8a-2df7-3165-98de-dba7839fd859 | -2.6879 | -45.652599 | 2024-11-23 00:05:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb9609cd-3f2e-3ff9-9759-8fadca8fc4ca | -2.1285 | -46.398102 | 2024-11-23 00:05:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494139cd-7514-378c-8d3b-c0d47e3f544c | -6.4857 | -47.041302 | 2024-11-23 00:05:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e12c9385-b4f1-39e1-8020-a6b7cf2981db | -2.7149 | -46.0914 | 2024-11-23 00:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff996c0-8758-31e4-af3c-23db2e06ab6b | -2.6953 | -46.095699 | 2024-11-23 00:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e83cdc5c-ff97-3958-8c65-cd6d7782a8ac | -2.1804 | -45.6758 | 2024-11-23 00:05:00 | METOP-C | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c07a40fd-78c6-3984-b445-9d8a5165fe4e | -2.3114 | -45.4384 | 2024-11-23 00:05:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f6393df3-50ec-3681-a189-cab66420659c | -4.3714 | -40.4035 | 2024-11-23 00:05:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 78ad2ca8-dd60-39ad-9f23-81f0bc4e3d6e | -2.1097 | -47.627602 | 2024-11-23 00:05:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08309712-5494-374b-8b09-330c9bf7b5b4 | -2.3211 | -45.436298 | 2024-11-23 00:05:00 | METOP-C | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba4f3cd3-2f6f-3a98-a0b3-d65baeb83857 | -2.3229 | -47.0774 | 2024-11-23 00:05:00 | METOP-C | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51dbf756-9887-3286-b702-4f43c1a3d268 | -5.542 | -45.787701 | 2024-11-23 00:05:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 459f05c1-3e6f-3d86-b7b3-6ba35527855b | -4.5717 | -38.484402 | 2024-11-23 00:05:00 | METOP-C | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a14cb520-6b22-3367-b010-2a3623e2e98b | -2.708 | -46.1064 | 2024-11-23 00:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 09ce3d22-106a-3022-bfb5-c0223685ca9e | -3.4684 | -50.429901 | 2024-11-23 00:05:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f8519d3-0aa9-3b53-af2d-827f53d915c0 | -2.7022 | -46.080601 | 2024-11-23 00:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1131a0b2-26f7-3760-8b77-f916cdca9ee2 | -1.8883 | -46.423 | 2024-11-23 00:05:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 509e0120-a896-3700-b7c6-e1b872932f8d | -2.6906 | -45.6647 | 2024-11-23 00:05:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d3468f6f-5a2d-3db3-b11d-e41ba6dad65d | -1.2448 | -46.747398 | 2024-11-23 00:05:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96728c0e-c1bb-3d21-9b32-558d20f0322c | -6.0511 | -44.048199 | 2024-11-23 00:05:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 515e5473-1bbc-300c-81ee-32d86c50ae55 | -6.3302 | -46.033001 | 2024-11-23 00:05:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2d4b97b-754d-3004-8447-79d6a6f2d939 | -1.5242 | -47.2995 | 2024-11-23 00:05:00 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de9ab1e8-f088-3d63-98d8-713689f95168 | -1.5208 | -47.284599 | 2024-11-23 00:05:00 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5eed813-f135-33c8-a53e-8211ea6e4093 | -4.5329 | -42.7584 | 2024-11-23 00:05:00 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e63a234-1e6c-33fd-98e5-f27567265e2b | -5.5391 | -45.774101 | 2024-11-23 00:05:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4d43fa3-e1da-3510-b7a3-16219661d982 | -2.5805 | -46.540501 | 2024-11-23 00:05:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f998118-cbe7-3c13-8490-699d604c4302 | -6.0609 | -44.046101 | 2024-11-23 00:05:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cce7cbbb-0ed6-345c-b2aa-b3d65e8228a6 | -2.7051 | -46.093498 | 2024-11-23 00:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59ecede5-5e8d-3a1b-8a83-508d4090eaeb | -2.6781 | -45.6548 | 2024-11-23 00:05:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4584415-bfc5-3b0f-b34e-41c44619d395 | -4.8699 | -42.702702 | 2024-11-23 00:05:00 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3c3bca9-07b3-34fc-994e-9d8e6917b2f9 | -2.5347 | -45.246101 | 2024-11-23 00:05:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 403fdc69-077a-3ebe-882a-fe666ddc6969 | -5.683 | -46.481602 | 2024-11-23 00:05:00 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 284f7e77-5f0a-34d3-9364-4de64d7bb6a8 | -2.2885 | -46.3353 | 2024-11-23 00:05:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d230416-b4ad-3297-a2a5-5981fddfd46d | -4.373 | -40.4105 | 2024-11-23 00:05:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 22aefacf-d939-39ef-9d1b-5f285536cd26 | -2.6808 | -45.666801 | 2024-11-23 00:05:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e6555b1a-8b28-3873-9ede-b3c89173cb53 | -5.0114 | -44.305698 | 2024-11-23 00:05:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 188f5a8b-adb8-39a2-804f-4b1fa4f43db6 | -5.5611 | -43.315102 | 2024-11-23 00:05:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3ae78089-fed0-3cb5-9d3e-a8964ba0ae17 | -9.93687 | -36.34707 | 2024-11-23 00:07:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 143.6 |
| d417075a-f294-3958-bb8a-ddfdfc2d2133 | -7.01974 | -39.22615 | 2024-11-23 00:07:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b89d6a16-d45f-353d-9860-1d3d1e1c777a | -10.47878 | -37.13847 | 2024-11-23 00:07:00 | TERRA_M-M | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 20edf518-1d95-3297-a8d5-b3c8a7278696 | -7.33001 | -34.83568 | 2024-11-23 00:07:00 | TERRA_M-M | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 7c6e5e70-1d3a-3011-9dad-62238d4c2211 | -9.93811 | -36.35603 | 2024-11-23 00:07:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7b193598-6965-325d-b0da-9a9776b68ae4 | -5.59603 | -37.97741 | 2024-11-23 00:07:00 | TERRA_M-M | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 4f126b0c-6cec-3b7a-a07d-813891da40f1 | -6.49311 | -47.04252 | 2024-11-23 00:07:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| db61964b-49ae-325f-a035-e42705fa7a44 | -9.92676 | -36.33941 | 2024-11-23 00:07:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |


[Clique aqui para ver as próximas entradas](README5.md)
