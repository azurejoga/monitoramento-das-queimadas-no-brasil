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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e3a1a41-cb72-3bfc-afa0-b25181ce1028 | -6.24993 | -43.56212 | 2024-12-04 03:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf9caef0-a13b-33d2-a39b-f4e2417e5c95 | -6.01999 | -42.36417 | 2024-12-04 03:46:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52731941-e42d-3f82-a293-d979de9eefa0 | -10.04492 | -36.5591 | 2024-12-04 03:46:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6233ed50-39db-32b4-bcb3-404a0e9f4cc9 | -6.39886 | -44.05598 | 2024-12-04 03:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 249ef2b7-5371-35bc-a2de-38a6f19bfc69 | -9.27749 | -35.94668 | 2024-12-04 03:46:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 53631153-701d-36f4-9a9b-be322c86a3dd | -2.09938 | -46.14035 | 2024-12-04 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8850dfa1-3500-311a-9b0f-29fad1a249d1 | -2.31388 | -45.41862 | 2024-12-04 03:46:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1b2c793a-dd0a-333d-8381-f08aa1a08d42 | -3.12398 | -40.06031 | 2024-12-04 03:46:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b696ab96-7857-3be4-b27c-0b5583ff7e3e | -6.08274 | -48.06853 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6030f587-db46-35d5-9fd9-1248bd986518 | -2.32375 | -45.42769 | 2024-12-04 03:46:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b8058a0-a04e-3130-b58d-19f532774af5 | -2.10006 | -46.13625 | 2024-12-04 03:46:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28649f6b-146c-3dee-850f-3c253f63a036 | -5.26972 | -46.17211 | 2024-12-04 03:46:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be4f0753-4947-3e0a-adb2-4f56adecef96 | -2.31268 | -45.42588 | 2024-12-04 03:46:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e2156a69-a1fe-35b4-8d0e-b7d1e715a1c7 | -8.56283 | -39.59091 | 2024-12-04 03:46:00 | NPP-375D | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| dd50b530-6e8c-3fb8-8a8f-e84dfd75cb23 | -5.62281 | -43.95526 | 2024-12-04 03:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f02f5ff-786a-339c-9c4b-7ada83e37a5d | -6.25152 | -43.5556 | 2024-12-04 03:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7f7826b-ad26-3163-988a-b62f3f2f4e59 | -6.01642 | -42.36497 | 2024-12-04 03:46:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6c0fc7c4-2bd0-3de7-a63e-5df9f2546bc2 | -6.25702 | -43.16374 | 2024-12-04 03:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c43cd3d1-b8b4-39f8-b9ab-d0d4bea962e3 | -1.05238 | -46.59505 | 2024-12-04 03:46:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bb970fd-eb47-30b1-aa1b-75bea8f7cdab | -3.13308 | -39.90593 | 2024-12-04 03:46:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b3e17e80-7bb9-3367-ac20-2956a6715e10 | -8.15693 | -42.94215 | 2024-12-04 03:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 86c1b7ca-686d-3b28-9c7c-c97f6d0f5b4c | -3.13685 | -39.90654 | 2024-12-04 03:46:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60901a89-dbaf-3958-85c4-2b399b11ba9d | -6.01933 | -42.36802 | 2024-12-04 03:46:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 35a6639c-fb64-3f93-a264-72218aa88100 | -7.44528 | -39.75476 | 2024-12-04 03:46:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ac228a49-4aed-3ed9-aa0b-7d5bd8a9652b | -6.25073 | -43.56033 | 2024-12-04 03:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 644900d2-1367-3e2d-a00f-b834f2ee0512 | -6.08355 | -48.06394 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad80aa8f-a121-35d8-acc0-fc6c9f1c03bf | -2.0956 | -46.58301 | 2024-12-04 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2022b8fa-c471-3bc3-b9ab-948c4a7b3db1 | -2.07209 | -45.48294 | 2024-12-04 03:46:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88d22d26-c224-3b3d-94f5-c291a86660b4 | -2.0938 | -46.58339 | 2024-12-04 03:46:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89e340fc-be06-3e9b-9258-b2893e92bbb0 | -2.19773 | -47.24049 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f34c6bdd-1779-3775-bfd3-547dcd11db32 | -7.12745 | -45.39724 | 2024-12-04 03:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3bd0267b-777e-3e08-ac0c-0a5ff7572fc6 | -2.19986 | -47.24473 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1c6a2b87-eecf-34c2-8d22-a731478bcaf2 | -8.11515 | -38.97293 | 2024-12-04 03:46:00 | NPP-375D | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| db978dad-65e9-3cbe-beaf-38a20d21407b | -2.31328 | -45.42223 | 2024-12-04 03:46:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8066fed8-28cc-3a87-9911-0ce4bc0315dd | -10.04772 | -36.56319 | 2024-12-04 03:46:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de787a38-258a-3e67-94fe-c6af32512d58 | -5.62619 | -44.84135 | 2024-12-04 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea322506-9410-3af5-97f2-cd06d924031e | -2.19907 | -47.2496 | 2024-12-04 03:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 34ea4502-b64a-3fc7-b3ed-6f17dfaba250 | -9.35208 | -40.52864 | 2024-12-04 03:46:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f2b941ed-4eb1-3ee1-91fc-87ddbf31bf74 | -6.08139 | -48.06677 | 2024-12-04 03:46:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ba068fa-6fb4-3c1c-9a81-ffe60ccb8068 | -11.24544 | -40.98026 | 2024-12-04 03:49:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78b18dcd-5852-3909-881e-18f30b0dd52a | -12.93117 | -41.11687 | 2024-12-04 03:49:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 90ae7cb4-5839-37d4-ad3e-586b09f31d93 | -3.85272 | -40.9846 | 2024-12-04 03:49:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 099cd9d6-6dbd-38f1-a5cc-77e39bb76c6f | -3.81698 | -46.9539 | 2024-12-04 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 34668747-7df2-3edb-8727-649cb2f6bcee | -3.68936 | -42.04211 | 2024-12-04 03:49:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2a37faf3-7e45-35ee-87ae-f401edd7000f | -5.61783 | -43.9525 | 2024-12-04 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66cb3c14-9ab8-381c-9246-b5c2189a0ab9 | -3.85153 | -46.52133 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fac70cb0-e2f7-33c7-813d-18d806fc7fe8 | -4.05625 | -46.60958 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3753f675-df7f-3310-af49-d8be24095107 | -5.61867 | -43.94749 | 2024-12-04 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26577f56-9542-3aa1-8d74-0469f20da7d9 | -3.85667 | -46.52623 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c2020ea-1db3-3734-b85d-734dd426cdc3 | -11.18611 | -40.3238 | 2024-12-04 03:49:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a6f34d0-1c23-37a7-8ddd-bfd5cd67f014 | -11.18676 | -40.31987 | 2024-12-04 03:49:00 | NPP-375D | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6c7b5e0b-1dda-3143-8ff8-39808e4dac93 | -3.84871 | -40.98403 | 2024-12-04 03:49:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7095a22a-64c3-3424-81c8-bba1cab280c9 | -3.81482 | -46.95111 | 2024-12-04 03:49:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6914d2c6-1fff-3e83-8b06-ef30728d5f51 | -3.27019 | -46.27259 | 2024-12-04 03:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b38701b-78eb-3023-ba1f-87ed8fe47161 | -4.53735 | -45.90923 | 2024-12-04 03:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b55df81-e980-35c6-9f77-eee06930956a | -4.68751 | -40.69529 | 2024-12-04 03:49:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa38e45f-aaa2-3498-9079-ed788eb9d998 | -17.85067 | -40.13049 | 2024-12-04 03:49:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b3fc96e-8504-3418-b368-141cfd256722 | -4.53175 | -45.90877 | 2024-12-04 03:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0edb1ea8-f76e-3674-92f8-1c83456b8a6c | -10.21946 | -42.18832 | 2024-12-04 03:49:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 381c03cf-d978-3a83-8fc5-5c5fac09be60 | -10.68383 | -40.54202 | 2024-12-04 03:49:00 | NPP-375D | ANTÔNIO GONÇALVES | BAHIA | Brasil | 2901809 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4dac7b07-963c-3917-b929-563d89ddb22f | -3.68127 | -50.256 | 2024-12-04 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e528856-2c4c-3344-9c1b-6f4209349648 | -3.80811 | -46.95448 | 2024-12-04 03:49:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a17a1575-ea39-3b36-9cd5-2443654f8d76 | -5.33843 | -40.35757 | 2024-12-04 03:49:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 33c6ffc9-ca92-3bc1-b7f2-f066272480b2 | -3.17336 | -44.43657 | 2024-12-04 03:49:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fad0df10-775e-30d3-9f24-39a35558d57b | -3.80963 | -46.94553 | 2024-12-04 03:49:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3523feec-08d9-33f5-9674-bfa6ea4d1b5b | -3.81408 | -46.95548 | 2024-12-04 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ee6bcb6-5fe1-348a-9202-7c91250fa1d5 | -3.84648 | -46.51595 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e360108c-430f-38c9-8b6a-c345552e0c94 | -4.02218 | -48.81433 | 2024-12-04 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 212a08f2-2544-36e6-993d-567b08bcbd7c | -3.85219 | -46.51749 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81bf4f62-b2be-3c1b-b267-428c70ed039a | -3.87419 | -48.36292 | 2024-12-04 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a81be7b-dba0-35d7-b274-0f0a0d5600fd | -5.37546 | -36.78913 | 2024-12-04 03:49:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2f476864-c898-3457-8247-a9ec37488190 | -11.5291 | -38.01043 | 2024-12-04 03:49:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6f2c89a-c135-37fd-80ce-435f4a6b43c3 | -5.1116 | -35.69199 | 2024-12-04 03:49:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 125bb173-c472-3260-ad38-c6b12a45462c | -13.80852 | -41.57936 | 2024-12-04 03:49:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfe9d54d-2f76-39c1-b631-5288d70a0a41 | -13.41688 | -41.11281 | 2024-12-04 03:49:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5ff9d0ac-b18c-3c29-aeaf-16d6ae7e1e1c | -4.05689 | -46.60583 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d258b2d1-1cef-3e82-a12e-f6e930ffa0ad | -4.01452 | -48.81882 | 2024-12-04 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4b6aa5c8-fdc0-368f-8f54-03c902ada2f5 | -3.66585 | -47.12933 | 2024-12-04 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a63c392-5353-3d7a-be54-0e5a13432f55 | -4.71391 | -44.45845 | 2024-12-04 03:49:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94b1d7e9-99bc-32ec-bcda-1b2cf6d86aef | -12.93188 | -41.11278 | 2024-12-04 03:49:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1da48130-74cb-347d-bf02-fb493d86b140 | -3.87322 | -48.36854 | 2024-12-04 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 862c60e7-2984-3759-9c26-0fe6e4b6bbf4 | -3.26444 | -46.27154 | 2024-12-04 03:49:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83897df7-87d7-3ad0-afa1-8dc8b8435814 | -3.68021 | -50.25668 | 2024-12-04 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79342bc0-a0cb-3d99-a1eb-fb7c8654d889 | -4.53635 | -45.90988 | 2024-12-04 03:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0cc2309-9bd0-3e2d-a5e4-661e8bf4788e | -5.62258 | -43.95327 | 2024-12-04 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1406855e-d741-312b-bbee-920ebd9627bd | -2.83296 | -46.75315 | 2024-12-04 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6bd6912b-9aaa-3960-a9bf-06cc75d70b68 | -5.22802 | -35.63813 | 2024-12-04 03:49:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6301a0dd-f2c3-355d-be91-eb53fc04399b | -3.17385 | -44.43356 | 2024-12-04 03:49:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25996209-73b3-36da-a364-031cd14068c0 | -3.6789 | -50.26425 | 2024-12-04 03:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f5ab7b10-7aa4-3c3f-9689-dcf7e099c2ba | -4.27022 | -46.57423 | 2024-12-04 03:49:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6fdfd44-83f3-38f1-91e8-3112e1116966 | -11.53242 | -38.01097 | 2024-12-04 03:49:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bfcd2937-e042-33b8-b2d0-a775803f8513 | -11.24183 | -40.97965 | 2024-12-04 03:49:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bd3afd3-8460-34f2-974e-5e9cfb3441c8 | -5.11105 | -35.69549 | 2024-12-04 03:49:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0af1ec91-c7c0-37ad-82a2-31d48c16752f | -3.57686 | -43.30854 | 2024-12-04 03:49:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1aa6e3c6-b3f6-3164-a6ab-b643dad2e329 | -4.01554 | -48.813 | 2024-12-04 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b25646c-cc5d-3f12-a38a-eef64d2bbe48 | -6.78796 | -35.19219 | 2024-12-04 03:49:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c1e0f4eb-d247-36c2-8eb3-ea213415c584 | -4.01787 | -48.81619 | 2024-12-04 03:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 69020180-fd1a-3cb1-b11c-1e035c29f4b3 | -4.98887 | -40.90597 | 2024-12-04 03:49:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec2b6ad3-e272-31c5-8a36-2c627c9515eb | -4.90365 | -40.55429 | 2024-12-04 03:49:00 | NPP-375D | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b5e57e60-205b-38fb-97ad-653e90d437cb | -17.85126 | -40.12681 | 2024-12-04 03:49:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |


[Clique aqui para ver as próximas entradas](README21.md)
