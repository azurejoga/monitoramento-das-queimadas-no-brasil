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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cddf3af-cd93-34f7-b68e-81a8aeaff712 | -11.71655 | -43.4431 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 48518c40-93f9-38cb-9b69-fa01cf4376d0 | -10.72698 | -45.32911 | 2026-10-01 00:18:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 044ed64f-6f5b-3696-b1c9-6ebd5ca3d662 | -11.352 | -54.11619 | 2026-10-01 00:18:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5d14921f-c931-30b8-a9d6-552e53e23821 | -8.22401 | -54.74995 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bc1743ee-e766-37d3-9953-92abfebaef53 | -12.17911 | -47.39679 | 2026-10-01 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| efd53a95-c964-3975-bd5c-0b0be6afdd61 | -11.4342 | -43.40576 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1584.0 |
| d68c4dae-b45b-3030-bf2e-bfe5a69f920a | -11.73667 | -50.41892 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 212f7c41-332c-3b9a-bf76-6e3b345d5f92 | -10.56381 | -50.86271 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0fbf7ab3-2ff7-3b43-a569-bb3a37cbe9c3 | -12.18829 | -47.37796 | 2026-10-01 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 36d00f1a-e291-3d2b-8596-892f98310ab1 | -11.42433 | -43.4444 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fc1eeecb-baff-3b67-a978-70d239240f11 | -8.38989 | -46.29655 | 2026-10-01 00:18:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 947db5b6-082a-30af-b3f6-3ef67289efb8 | -11.3062 | -54.88184 | 2026-10-01 00:18:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f6d00d4a-0ee0-3150-8978-1de5ff7f6f35 | -6.85969 | -44.92329 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0ddd1d6e-03ad-3793-878f-bbb32a3dd881 | -11.3282 | -50.98005 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8473b6f4-005c-384e-8ad1-a3abf3f45f40 | -10.75912 | -50.51052 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3165fc7d-93b9-3c8d-ada2-06fad425c623 | -6.74144 | -44.1361 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1d4d42e9-789b-38a0-93c3-244856941c5e | -12.78876 | -53.99149 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f8033679-f264-34ce-9d85-46eda1c01a0a | -10.8493 | -48.70402 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| de147697-0a7c-330d-80ff-fd013c20d61a | -9.54223 | -56.15647 | 2026-10-01 00:18:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 469f1417-8b8a-3c11-8b52-bc9ca7e8327d | -10.2819 | -53.9706 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c5467e24-cc63-3cde-a60d-92f1993df2a6 | -8.15843 | -54.81122 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 28276d87-b289-3bf9-8a94-3bb6ad37e566 | -14.89447 | -51.87948 | 2026-10-01 00:18:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a7bc893f-9ae5-3363-945d-dad95d5c41d5 | -9.0666 | -49.87488 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| b543513d-1206-3a93-b6b2-04b6e3d51d69 | -12.7733 | -54.01261 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 39880052-d4c9-3c79-a2d0-8fe2a76a60dc | -9.31437 | -57.70221 | 2026-10-01 00:18:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ca1e18d5-b650-3407-802d-7ea9b8ba99b5 | -10.75024 | -50.53981 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 07b19c32-8421-3058-8357-2896ee9877cd | -11.19925 | -45.20813 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| da8312af-acfb-3e8a-b13c-a00d44965913 | -12.85319 | -44.31654 | 2026-10-01 00:18:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 9e28178c-57d1-39e4-99db-61f860ce22a7 | -8.00492 | -49.22564 | 2026-10-01 00:18:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e57f295a-3dc7-340b-a2f4-364c5a409dba | -14.41904 | -51.3153 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 938b8290-b838-3595-9516-7ba94102f7fd | -10.8385 | -48.70676 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 5fe7f4c2-5e99-3865-9f73-ac687deb0957 | -10.7544 | -51.672 | 2026-10-01 00:18:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c5dc93ae-2035-3cbd-b90b-a8d8869192fd | -9.58833 | -54.62566 | 2026-10-01 00:18:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3a81ac12-f622-3ab2-b95e-530a484257bf | -10.73903 | -50.53049 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 264ed7f0-6943-3f9e-86eb-922174cd829d | -11.95283 | -55.92127 | 2026-10-01 00:18:00 | TERRA_M-M | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1abd99a1-d49e-308c-b886-f604829988b1 | -12.39077 | -54.11012 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0ae10868-f32a-3380-8194-ace0f33df84e | -13.38012 | -46.83916 | 2026-10-01 00:18:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 744d1a93-7b5b-3bd9-8643-edb1fa3baaeb | -10.85138 | -48.71791 | 2026-10-01 00:18:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fbd15a08-d72b-3e77-81e6-e78b15801426 | -10.77198 | -50.53067 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 3754aaf0-3d57-3316-a860-43fd30cdd9fa | -13.37725 | -46.82141 | 2026-10-01 00:18:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0011ffc0-d8a7-3ca4-b360-1bb4f6485e02 | -8.31727 | -54.75832 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 177af578-d895-3d35-bb0d-3e3781e249be | -11.25511 | -54.08023 | 2026-10-01 00:18:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a9b9e038-26f9-3bcd-a5be-10c0a28db1ee | -12.19095 | -47.39485 | 2026-10-01 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| d65f224c-10fa-3f3d-9a04-95e37bc23104 | -12.84758 | -51.02504 | 2026-10-01 00:18:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 893ec8d8-5b8b-3d6a-8898-335624792c58 | -8.32256 | -46.76928 | 2026-10-01 00:18:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3432b39c-f665-36ee-b8a6-be16a7d0a0b6 | -8.26859 | -54.74371 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a104df92-ffef-3203-aea2-d0d8035162df | -10.76073 | -50.52135 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 03ff245a-9c3e-3d4a-94e1-192d25c36a68 | -12.70674 | -54.06586 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c46792de-1716-3e2f-b878-0ecce7095c32 | -12.19243 | -48.43031 | 2026-10-01 00:18:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| b70f775d-0f0b-3763-a0a6-c7a29e2a7593 | -9.65027 | -51.75376 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 66cf91ca-ac42-35a2-b070-a2f23f2e511f | -14.44195 | -51.28294 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7f99fcc1-e3c7-396f-b4d2-75ee8252c84f | -9.21679 | -50.68318 | 2026-10-01 00:18:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 517d0bb0-7393-37c8-8ccf-1ded9046f137 | -14.88562 | -51.88083 | 2026-10-01 00:18:00 | TERRA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| af7ec2a4-2904-3d23-9950-29ad93af0485 | -10.76351 | -51.67064 | 2026-10-01 00:18:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b89ef31b-f3ed-3765-8644-12b680223fcc | -11.41111 | -50.98217 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d49bdd45-5a07-3c3f-b009-d8739fcd8a04 | -14.41098 | -51.25884 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 63580bc2-0da8-3019-9036-42ada608e22a | -8.26982 | -54.75278 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29807307-243b-3bbc-8162-d45543e0a248 | -10.32628 | -47.79302 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| bc09d5a7-8d8e-30c8-8cfb-a0286399b523 | -13.55887 | -53.21164 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 48c362be-6070-33e1-8863-dfe4ace884e9 | -9.12385 | -49.92311 | 2026-10-01 00:18:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b0535d9a-ee66-3e16-813a-02fe79b7048e | -10.77476 | -54.75792 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 73826c75-6584-3796-ba21-fb347e237700 | -10.50941 | -50.85624 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 5b263966-9e5b-34ae-a64e-cb7c800c8ff0 | -13.34098 | -46.82775 | 2026-10-01 00:18:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| b631f87d-4669-32d7-abe1-eb4ec71c3d8c | -9.34658 | -57.16414 | 2026-10-01 00:18:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bb869824-20d8-321f-ad37-7f62656d41c7 | -11.37674 | -55.1314 | 2026-10-01 00:18:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b3dcc4d4-a264-301c-bc12-70b42fe51af8 | -11.40791 | -43.48937 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 735f36b2-97b5-38e6-9e0b-df96ddd95656 | -10.32355 | -47.77612 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 810a1c44-c5fd-33b6-803e-d61a7eab8430 | -10.77038 | -50.51986 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 38a344c9-2be7-31de-ae39-0362f4a7c218 | -12.17645 | -47.37996 | 2026-10-01 00:18:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 99704934-9d5c-398b-86a3-4107808f17a2 | -10.60554 | -53.97389 | 2026-10-01 00:18:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d3ab1d1-2898-320e-9d70-88132d1af09b | -14.4177 | -51.3059 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bb87a9b4-f8c5-3faa-9fa7-376fdc6766a6 | -9.74063 | -53.85596 | 2026-10-01 00:18:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d97d9e94-7afa-3c33-8d14-e328befb9c9d | -14.43164 | -51.27491 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| abdabc21-35f0-3db3-8317-a694e40733fb | -8.26213 | -54.7631 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 600165ec-13ab-331e-af49-1d30f0d65f69 | -8.84278 | -50.51262 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b2d89333-3c8d-3f9e-bb13-ccaae7b48eae | -10.77518 | -50.55223 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 03a8551b-233e-3821-b819-0dd56ce4f118 | -11.61782 | -43.54564 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 2780540f-d501-300e-8933-25638438c5b7 | -11.45683 | -43.43824 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 339.3 |
| 7bc9582e-9c49-3487-bad6-1b99fec2cfa9 | -11.41174 | -43.41512 | 2026-10-01 00:18:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 3b62d9ef-3964-3bec-83d9-0b0ed22e08a8 | -11.40964 | -50.97206 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 89be5142-8c66-3363-b8c3-77f9a324de49 | -11.87012 | -50.60202 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7c2d9039-9486-327d-aee4-14cd167c4c3c | -8.27105 | -54.76186 | 2026-10-01 00:18:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3c217db3-2d05-31c2-a402-ddbc99256ffe | -10.76214 | -51.66107 | 2026-10-01 00:18:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 92d245cc-8e49-3383-81f2-1f6325341c1b | -13.65642 | -53.94118 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a6a5d184-486c-3514-a43c-cccf9302dea4 | -10.77349 | -54.74847 | 2026-10-01 00:18:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7cc3c1b3-c4b9-3f15-a18c-d66542672222 | -8.84604 | -49.70059 | 2026-10-01 00:18:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 20a765bc-693e-3f87-99ab-d2a50562a116 | -12.2559 | -53.99327 | 2026-10-01 00:18:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cc9f94d0-9975-3861-ade8-9aee7365cfc6 | -13.65517 | -53.93176 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 08c7d831-8f26-3fb2-8112-fe671cd6741c | -10.82792 | -57.20975 | 2026-10-01 00:18:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5328fc39-3365-3a71-8f99-6b5f4980fbd8 | -14.76335 | -51.40039 | 2026-10-01 00:18:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21035d09-f6a2-3e0c-950d-a758c5b42b8e | -13.66418 | -53.9305 | 2026-10-01 00:18:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 99bed061-dfb4-333f-9ee9-bc54c7e23fce | -9.90851 | -50.16936 | 2026-10-01 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6505e2f8-d46a-3f32-b509-d9c159a1c5c8 | -10.55481 | -50.03834 | 2026-10-01 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 0af1a9b8-7e2e-3eb6-a10e-49d992c71e80 | -9.08426 | -45.00735 | 2026-10-01 00:18:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 21aade8e-8584-3ed2-9077-bde556692855 | -10.75432 | -50.54443 | 2026-10-01 00:18:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| f691b40e-239d-353b-a235-ac2d9dc88b27 | -8.21273 | -45.48199 | 2026-10-01 00:18:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 01cdde83-cec6-322d-854e-304055431b43 | -9.34819 | -57.17641 | 2026-10-01 00:18:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| a08ada30-b9ff-3bae-b36c-fadd424cad88 | -11.83868 | -50.94757 | 2026-10-01 00:18:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e82da5d6-dbc8-3d4c-89b8-afac25da8431 | -13.73623 | -48.97853 | 2026-10-01 00:18:00 | TERRA_M-M | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 80dc3e7c-7fe4-3b2a-bf93-ed8764e8b26d | -9.90679 | -50.15773 | 2026-10-01 00:18:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README4.md)
