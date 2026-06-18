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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6740ac96-7712-3574-b97e-4b1a3a7ad575 | -15.76603 | -39.17999 | 2026-06-18 04:00:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cefc9ae8-4d1d-3ae0-8121-4e763af1e56e | -10.5577 | -46.23342 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 943661e5-85b0-3bb2-b3bc-b7ecb3e50233 | -11.24663 | -46.62012 | 2026-06-18 04:00:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a497d6a6-e547-38a3-82a1-2667137da9b5 | -11.80394 | -52.52454 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c49af07b-7308-3f0e-9509-71f01e698db0 | -8.8373 | -44.78999 | 2026-06-18 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25815a35-003d-3711-bd29-71be2ac21d99 | -12.20912 | -52.77859 | 2026-06-18 04:00:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f4f96f2-0d53-3b44-87c7-ef5a14d9c877 | -12.73971 | -46.31618 | 2026-06-18 04:00:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c52e04db-6959-3dde-b83e-d851d04e0c62 | -10.90967 | -46.34663 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d08cd01-83b1-3fa0-8926-313792738280 | -12.83347 | -44.37258 | 2026-06-18 04:00:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 14d5a4e1-5d1c-3b04-ac22-8e141d5305ea | -10.22996 | -44.77512 | 2026-06-18 04:00:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 268c5301-8940-32f3-bd96-a68582def7e4 | -10.90785 | -46.4342 | 2026-06-18 04:00:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d725866-fe44-3d57-8d53-0cb9ae2248a8 | -10.58216 | -53.48553 | 2026-06-18 04:00:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ecd74f4-ad82-3c7d-afdc-777825915410 | -15.76546 | -39.18367 | 2026-06-18 04:00:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 52191f47-a40d-3b10-805d-2ce4123eafc2 | -11.47982 | -52.9182 | 2026-06-18 04:00:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9fc3b17-c5c7-30f3-b117-2bc38b3aca48 | -22.67353 | -43.47612 | 2026-06-18 04:02:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d0047be2-73e0-3194-978a-4ec8c0bbb47d | -18.98542 | -52.45613 | 2026-06-18 04:02:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93fd8bb3-df36-366c-af64-8704081a59fb | -16.8936 | -46.79174 | 2026-06-18 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09e817d8-de58-3ea5-b9a6-43ca81fa03b1 | -22.85327 | -42.04213 | 2026-06-18 04:02:00 | NOAA-20 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1441d387-ad3f-3d47-86e5-d6ddc29d4911 | -18.83054 | -51.47387 | 2026-06-18 04:02:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d657d016-273a-359a-95ca-077fe69b9d7c | -18.98447 | -52.46033 | 2026-06-18 04:02:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab4dc867-80d4-3aba-a995-be74fa718b38 | -16.14127 | -43.59735 | 2026-06-18 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5a0d711-2bc6-3899-9ed4-92619acf502a | -16.02555 | -43.42367 | 2026-06-18 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7897e31e-da1f-3de4-81f5-9bd6eacb5cad | -19.89444 | -40.28011 | 2026-06-18 04:02:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3f25867f-7cfd-3bf5-9a92-ce762b285496 | -16.23283 | -40.13285 | 2026-06-18 04:02:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2c329d15-6dff-321d-a967-3a565ed45fc4 | -18.86136 | -41.97881 | 2026-06-18 04:02:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b7d6a080-aff1-3ce0-8dbe-c89091298ba6 | -16.50167 | -43.5048 | 2026-06-18 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8b238fb-fbf9-3c35-9f40-169a20ada339 | -20.06589 | -40.18379 | 2026-06-18 04:02:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36fc5dd3-e883-3e12-a4be-13deb7f7cbe8 | -18.9902 | -52.46252 | 2026-06-18 04:02:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d74e78f4-0693-360a-8beb-440d3eab76e8 | -17.32028 | -43.6436 | 2026-06-18 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| cc003094-a8ae-38ae-be9a-60dfd3faa955 | -16.02625 | -43.41955 | 2026-06-18 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 732965fd-d981-3323-b4df-4a105cbf17c0 | -18.98537 | -52.45688 | 2026-06-18 04:02:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21151e73-e310-3502-8ea2-0da643b91b5d | -18.97626 | -39.87246 | 2026-06-18 04:02:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00e6a965-916a-3b26-9160-64329ce5004d | -17.31676 | -43.64297 | 2026-06-18 04:02:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d6cb5794-06f6-3fa8-8b92-a9c3cc374c01 | -21.65805 | -41.32352 | 2026-06-18 04:02:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 20b26d11-8c00-3189-87a0-416b9c0e8975 | -17.60125 | -42.59549 | 2026-06-18 04:02:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3dda72a0-9a0c-30d7-bcc3-4578c1f9da7a | -18.82594 | -51.46867 | 2026-06-18 04:02:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b1c72a5-9ace-3cd2-b5cd-9077c76f1857 | -18.98445 | -52.46111 | 2026-06-18 04:02:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c05816-e678-344c-85c1-ea5ccd748676 | -17.79391 | -44.57957 | 2026-06-18 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d2eda3c-0f7b-3f53-9b58-15dc392e154f | -18.97288 | -39.87191 | 2026-06-18 04:02:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8fd28f41-e126-32e6-950d-2ff616d37b61 | -18.82053 | -51.46727 | 2026-06-18 04:02:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f8fcd67c-ff2a-30eb-a37e-e04464d166ad | -17.7947 | -44.5751 | 2026-06-18 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75a80ef9-1124-3873-8073-4a5c7f5db552 | -16.89437 | -46.7877 | 2026-06-18 04:02:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 409b89ff-127c-31fa-b99c-a172e61afaa5 | -16.14008 | -43.59965 | 2026-06-18 04:02:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 888bea8e-b334-3358-83b6-9112dc03c3c9 | -17.94663 | -44.41355 | 2026-06-18 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d44cd26-2f8d-32a6-8430-82978f05aaa9 | -20.82006 | -45.17491 | 2026-06-18 04:02:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71d5f139-2c86-3a4d-abcc-c8ba0ac6281a | -17.9474 | -44.40914 | 2026-06-18 04:02:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea5c1b4-2f70-3363-ba7f-7108186bca3e | -18.99022 | -52.46172 | 2026-06-18 04:02:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 902af32e-9d62-3e5f-830d-0fc4cd5beed8 | -19.89108 | -40.27953 | 2026-06-18 04:02:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 13608b7b-47a2-3417-86a7-9a62d6df31df | -27.4474 | -48.44405 | 2026-06-18 04:04:00 | NOAA-20 | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 928ec1a3-05e5-303b-a323-277f397b041e | -27.33263 | -50.11609 | 2026-06-18 04:04:00 | NOAA-20 | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df0f2c34-61c2-35bf-9801-c0ab1da4345d | -23.40506 | -46.42126 | 2026-06-18 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 53022196-9956-3be7-80c2-93ffa59abcd1 | -10.9164 | -56.8536 | 2026-06-18 04:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c71795a8-b135-3d75-a430-5320c07863bc | -10.9164 | -56.8536 | 2026-06-18 04:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2dd2d32e-b651-34df-ab73-1537d54bded9 | -12.8354 | -44.3657 | 2026-06-18 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f1f3eb68-4c8c-3743-a478-8cce9f945c94 | -3.3579 | -43.16769 | 2026-06-18 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8707b89b-4880-36e7-ad87-c06570183daa | -1.2971 | -48.43734 | 2026-06-18 04:44:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c540dbfb-8efa-3420-84e8-894cba7ec388 | -3.85326 | -54.22289 | 2026-06-18 04:44:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e3dcab3f-f124-3d1a-a33f-5eb65c147bea | -3.5088 | -48.03584 | 2026-06-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21e7ab19-09ae-3933-ad38-d627d3fe30c2 | -3.51225 | -48.03638 | 2026-06-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 347c5bc0-b19a-3a42-8b27-96aed2dffa1e | -3.55084 | -49.1054 | 2026-06-18 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd637a95-2fb0-3ce7-af1d-9a7f5d6e37bf | -3.4193 | -43.16354 | 2026-06-18 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5156d1f-9b77-3c46-918d-caf4192aab61 | -5.29322 | -43.95822 | 2026-06-18 04:44:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c2e943b3-b5e5-3904-8fad-8e3598e99dc6 | -5.29455 | -43.94905 | 2026-06-18 04:44:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 814a9512-b3e7-357a-8555-34a36d147c7e | -3.72893 | -49.27332 | 2026-06-18 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83c7999d-826b-3ebf-b0ec-2bf2016d3e70 | -3.51283 | -48.0326 | 2026-06-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 381c04d3-36b3-3091-852e-275689659413 | -4.35625 | -47.76153 | 2026-06-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f003255d-7126-3251-9284-a772faecf446 | -4.35274 | -47.76097 | 2026-06-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85fa4209-d703-37f2-a2fe-1d071672fc00 | -3.5503 | -49.10892 | 2026-06-18 04:44:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270a46bd-74f8-39d0-8f29-85881e47c592 | -4.35566 | -47.76548 | 2026-06-18 04:44:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 29511d82-653e-3ed5-82ea-bfa7f76786e6 | -3.35719 | -43.17247 | 2026-06-18 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 92bb08bc-739c-30f8-8632-ea7b22a4a443 | -3.4201 | -43.16248 | 2026-06-18 04:44:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98e9b973-cd46-34f7-bb17-b6c4c0a83b4e | -3.50478 | -48.03905 | 2026-06-18 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cbe43fc-082d-3ebf-ba9a-13def0572e24 | -3.42392 | -43.16425 | 2026-06-18 04:44:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab3bfc31-4d92-37a8-9daa-6bbcfcf6ac3b | -2.73934 | -58.18969 | 2026-06-18 04:44:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28f55bf5-c17e-3ae2-85be-4c6783d63dca | -5.29388 | -43.95364 | 2026-06-18 04:44:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f7cd15f1-3b8d-34f8-8c85-f52aec4dc6ce | -8.91232 | -46.9692 | 2026-06-18 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6941e30-cb46-3d1a-8e2d-6605f744e966 | -10.65465 | -49.20398 | 2026-06-18 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ffbdd0-e489-3fae-8c4e-ba9c307c2fc2 | -10.05086 | -48.09453 | 2026-06-18 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 005f9c8f-026b-3db5-b3cb-f7c45a3d721a | -7.36258 | -49.86122 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da18a1af-835f-350b-91de-34238f4422b0 | -8.25772 | -43.92599 | 2026-06-18 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0650489-be17-3cd5-9812-a3e15c553107 | -7.36647 | -49.85816 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 685238d5-0f89-3c74-a805-312c3680ba6f | -8.8589 | -50.19283 | 2026-06-18 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 073beb26-b88c-3ebb-b046-6c1d6030d1b4 | -11.66576 | -43.76239 | 2026-06-18 04:46:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f72784c-1aec-385a-9a58-3b4184f3140e | -7.60487 | -46.47228 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 012781be-6fba-33c3-9fc3-92dee0d6510b | -7.36538 | -49.8653 | 2026-06-18 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38ae3f74-14ce-39d5-88fd-c7b074808275 | -7.7254 | -44.1641 | 2026-06-18 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf74be9e-8e73-364a-a897-1d2086676581 | -12.76235 | -44.53611 | 2026-06-18 04:46:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f2675f0-b8a5-3a10-aaba-4b0aa21237ac | -10.12281 | -52.17809 | 2026-06-18 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fce1f38b-92ae-3d06-8a18-876040624cf4 | -7.50132 | -45.76653 | 2026-06-18 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c28bbc0c-d736-3f36-a976-9d50af6ad2e3 | -8.45635 | -51.54358 | 2026-06-18 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1c98699-8167-329c-baa8-efb328c65e34 | -5.13294 | -47.98928 | 2026-06-18 04:46:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 32c07140-258e-3932-9162-8d0b8d5dbccc | -9.0005 | -49.68305 | 2026-06-18 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36f87f41-c341-39c3-b1f7-dd34bec62cec | -7.80301 | -46.45944 | 2026-06-18 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbf99c8f-0156-3575-abb7-82808fefcd75 | -10.76075 | -48.54199 | 2026-06-18 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f15231d-1c24-3810-9cea-6267e6a63c1d | -10.91501 | -56.854 | 2026-06-18 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| e8c4cf3c-af0b-3aea-9ded-60a7c8377d7e | -5.81033 | -45.06972 | 2026-06-18 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52430f95-bd37-3701-aa0c-59121929a1b8 | -11.25088 | -46.62422 | 2026-06-18 04:46:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d61ed2-71a0-3e82-b25e-9c57350e5bf5 | -6.31639 | -48.43455 | 2026-06-18 04:46:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1891480-0ef2-3c9d-85a1-ab386a975041 | -6.87618 | -52.41221 | 2026-06-18 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07a11c4e-f347-345a-8850-9b0e1a915a4e | -7.92213 | -48.24922 | 2026-06-18 04:46:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README8.md)
