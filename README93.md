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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33b9bba8-9121-3bf2-ae36-84aeced2f49c | -3.6216 | -60.547 | 2026-08-31 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 057ce27f-e627-3e17-91ab-b4ae7a5e0dbd | -9.6676 | -47.9429 | 2026-08-31 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 43351270-0e0a-302e-a47b-a07a6788be99 | -7.5659 | -61.362 | 2026-08-31 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6da4e0a2-4a47-3271-a63b-b7907be83ff6 | -11.2482 | -45.1194 | 2026-08-31 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.2 |
| 176a3b9c-3ae1-3b10-ae06-e02e3747c048 | -7.2934 | -60.5713 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 386af969-02d2-3549-a156-137bacabdb86 | -7.9236 | -44.2558 | 2026-08-31 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| cda1ae79-e483-3313-84fa-1a7cebddcb96 | -7.566 | -61.343 | 2026-08-31 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 06ec8088-ef1e-303f-9f15-9998a3bfbc5d | -11.3611 | -45.2185 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f470871a-3953-3946-b71b-01f3b1a7be4f | -8.7989 | -62.5095 | 2026-08-31 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.8 |
| fe66b704-0835-3e4c-9ace-cd04219ed4ee | -9.4721 | -57.0156 | 2026-08-31 14:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| c2de9d26-e08d-3a8b-adbe-d6e295f5ed0a | -14.4201 | -52.5201 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 8ed63ce4-8e23-3d57-90ce-970e03ba5fb4 | -14.2599 | -52.8782 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 2723a0c6-8c24-3b58-9511-627fda811df4 | -18.2695 | -52.7284 | 2026-08-31 14:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 15fd134d-57cd-3ea9-95a8-f2051e23db3b | -12.9056 | -59.8661 | 2026-08-31 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| b6e2cc71-aeb7-3cf7-abfb-aa3e7bd66bfe | -5.8967 | -59.9719 | 2026-08-31 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 2574cc9d-f9f4-3482-9277-cc2ac7889701 | -7.3119 | -60.5706 | 2026-08-31 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 188.3 |
| c7388290-a2fc-3868-a7a9-35415de4084f | -5.9451 | -57.6906 | 2026-08-31 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 33426280-b4d9-3960-b459-8068b4ccd7f0 | -14.439 | -52.5388 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 631599a1-e5b9-3bf8-8c97-0891fd43a6d3 | -8.9481 | -62.3704 | 2026-08-31 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8320a084-faa7-33e4-9919-de8cbcf4693f | -10.3394 | -49.9547 | 2026-08-31 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 6087ceab-9421-33e9-a356-c56636498d43 | -14.6535 | -53.5642 | 2026-08-31 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| d383c2c0-1e92-3c21-adee-6115d9a12ccd | -10.7596 | -54.0384 | 2026-08-31 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 99233d08-40f5-3998-a33a-6bea638b142a | -18.27 | -52.7068 | 2026-08-31 14:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 10070be3-9e49-3cfe-88a9-02217062ef97 | -7.9239 | -44.2327 | 2026-08-31 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 9b5e53a7-429e-30ce-93a0-10123666030a | -18.2704 | -52.6851 | 2026-08-31 14:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 170a53d3-ac80-3505-8dfe-4a45ead63971 | -11.2103 | -45.1017 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.1 |
| f4919496-3da1-30be-8967-7722482a9b64 | -11.3806 | -45.1928 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ac409d8b-6e7a-30d4-a62e-b59585a9e3a0 | -3.6215 | -60.566 | 2026-08-31 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 132.3 |
| 45ce3ea7-212b-3a0b-8102-3fa58a798166 | -11.2485 | -45.0963 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 272.1 |
| 7184e918-8ac9-34e8-8d51-1036aa6d0a96 | -5.5647 | -60.2312 | 2026-08-31 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 2d329dea-10e4-3e49-8171-68f19b5da828 | -18.2899 | -52.7035 | 2026-08-31 14:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 5a69e0cf-4677-3fad-8de1-c45393cc3443 | -11.0434 | -49.6851 | 2026-08-31 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 56a0795c-c164-31b6-9bb3-c295956c4a7a | -6.1109 | -57.684 | 2026-08-31 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 234.9 |
| ac57e1e1-87f4-3ae1-9916-298017756f17 | -7.9605 | -44.3212 | 2026-08-31 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| e511581e-6acd-3005-96b4-f4bcaaca9ab3 | -11.9378 | -45.0656 | 2026-08-31 14:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 2701e83c-a8f3-3650-a8d5-e64e3cdc1114 | -7.9236 | -44.2558 | 2026-08-31 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| d026c6d0-7039-33f2-bdd6-316321d574cd | -18.2904 | -52.6818 | 2026-08-31 14:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 139.7 |
| e136b83e-5075-3342-8efe-84e1e849a1b9 | -7.9425 | -44.2538 | 2026-08-31 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| fbea68d5-ce58-35f2-9d98-03807d834df0 | -7.6253 | -55.2787 | 2026-08-31 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3d67e542-5f9d-3162-85b5-98db740dd336 | -9.6676 | -47.9429 | 2026-08-31 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| a9911b78-2c1c-3453-9bb7-8af5710eacee | -14.4004 | -52.5438 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| f92244dd-c607-3c07-9f1c-35047849d4be | -8.8175 | -62.4898 | 2026-08-31 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| ac72fb86-1b12-35b8-a6a3-1499f3a5f920 | -11.2482 | -45.1194 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 248.5 |
| f0ee1840-53bc-3638-a7cb-7a234354d50f | -7.5843 | -61.3803 | 2026-08-31 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1c0ca620-2bb0-3a0f-98a6-b811b9b6bb48 | -10.7409 | -54.0196 | 2026-08-31 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3c09e6c9-cd46-36fa-90b6-a064973247f7 | -10.8541 | -48.3587 | 2026-08-31 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 82a3aa52-7880-337d-b478-c6ec211ca839 | -14.5868 | -54.1153 | 2026-08-31 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 293566d5-3636-3363-8cea-8649c107e663 | -11.8506 | -46.7654 | 2026-08-31 14:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c410f689-86e1-3d8c-a39d-fe42f3b07198 | -10.5598 | -50.4236 | 2026-08-31 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| f843fda5-0ad8-34eb-8097-07d356afdcf5 | -6.1295 | -57.6637 | 2026-08-31 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6d843db9-111c-352a-82bd-977c2bab3bfd | -7.5658 | -61.3811 | 2026-08-31 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| af4c64a6-0fb4-33b5-b143-fa147530179c | -15.4594 | -53.9653 | 2026-08-31 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 70e29d41-717d-392c-9ca1-0cc497a5109c | -7.2933 | -60.5905 | 2026-08-31 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 42cad643-afea-3bf7-8375-5879e1320a91 | -5.8783 | -59.9726 | 2026-08-31 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7e709b8a-e288-3523-b3b2-259f3de74ed2 | -3.1997 | -61.1799 | 2026-08-31 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 49479d31-d99d-38a7-ba5f-01e0c81799c1 | -8.9665 | -62.3886 | 2026-08-31 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 433efdf9-3cfd-3c9f-a4d8-194d828e5e44 | -10.7598 | -54.0179 | 2026-08-31 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2e57dbe5-f402-33f1-a6c6-1e53dcb564be | -3.6076 | -59.0769 | 2026-08-31 14:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 529760c6-1d79-3173-93f2-41479333e9ec | -11.0747 | -51.5153 | 2026-08-31 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| f2d414dc-9c69-3f40-9605-4c1aa03ca51c | -5.8537 | -57.5576 | 2026-08-31 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 317ac6e4-80ec-3389-8c3f-3a6d837df825 | -9.4156 | -45.6499 | 2026-08-31 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 893f928a-f36a-3a4a-97eb-29b75ad17fc0 | -4.9604 | -55.8424 | 2026-08-31 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6cee9c5c-4580-3c97-a99f-d3c021e47e84 | -14.4 | -52.565 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 10a15453-a336-30c3-9641-d47606809b9a | -8.5969 | -54.7755 | 2026-08-31 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 1bd4f9bd-09b9-354f-b746-31c37b35b7a1 | -14.4007 | -52.5226 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 180ac53e-cdc1-3e2b-b027-056afe53be1f | -11.3236 | -45.1778 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.3 |
| acfac6b6-fcc5-312d-b2ed-6a8fa978f3df | -12.9054 | -59.8857 | 2026-08-31 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f87e82b1-0308-3fcf-94f3-198c4682469b | -10.8046 | -50.5046 | 2026-08-31 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 05ea03e7-bad3-3d38-8533-90680591883f | -8.7442 | -46.4437 | 2026-08-31 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 3bcc2344-4529-396e-8657-865f55193083 | -14.1459 | -52.7871 | 2026-08-31 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6821b6af-b5dc-3b94-ae89-327f5f8d68ed | -11.0744 | -51.5365 | 2026-08-31 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 8e59f9b2-5b54-397e-9251-c92649556065 | -14.2792 | -52.8758 | 2026-08-31 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 8d9be6bc-69f3-3d4c-9ebb-e0cc13ca5cf7 | -9.0615 | -65.4169 | 2026-08-31 14:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 12453ea9-5bcf-3e03-9394-c4724ee41ad2 | -6.7832 | -59.4401 | 2026-08-31 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| bf90b13b-4ad2-32f2-95c0-9bcfdbf27efb | -10.1087 | -50.2776 | 2026-08-31 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 9d60ce26-3352-31e3-a907-29668694ec5c | -7.9794 | -44.3193 | 2026-08-31 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 6ed7063a-24f2-3014-820a-e7429363e613 | -9.5964 | -47.6204 | 2026-08-31 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 229.4 |
| 3598a973-f447-3cde-aa59-698c6118fb31 | -15.2669 | -53.8851 | 2026-08-31 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 9fbc829e-c644-304c-bdba-7c3345d9f03f | -7.917 | -61.3481 | 2026-08-31 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| e05526e5-3b2c-3edd-8cb0-ede5223d022e | -7.3117 | -60.6089 | 2026-08-31 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 532c06f8-7e48-3cd4-bbd3-945ae16b3cb5 | -11.3615 | -45.1955 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 44e5a236-3bf8-3b16-a419-45b5762a7949 | -14.1456 | -52.8082 | 2026-08-31 14:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| c20a52e2-631e-3341-9c0e-8a671169a445 | -11.8859 | -45.831 | 2026-08-31 14:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 767707c1-e15d-32c5-8648-833595050b71 | -14.5028 | -52.1913 | 2026-08-31 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c141fe7b-9043-3c90-8e9b-09f95a7d2d51 | -5.8782 | -59.9917 | 2026-08-31 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed3a662c-3abf-3353-a3bc-821d088b3ef0 | -7.1123 | -42.7727 | 2026-08-31 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| dd7360c6-e8fa-31b9-80ce-72db39f65538 | -11.2298 | -45.0759 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| 9fccab16-4762-3413-b085-12e92f0dc3a8 | -8.7628 | -46.4642 | 2026-08-31 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 246.1 |
| 036738eb-eaf2-3cf5-b908-635ca2628528 | -11.0569 | -51.4328 | 2026-08-31 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4713ee8f-c49e-35a7-b3bf-3d7d3cc4a596 | -14.8319 | -55.7194 | 2026-08-31 14:30:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| a11b7a3c-faac-3b44-a985-f48e44957ea6 | -6.9176 | -55.7166 | 2026-08-31 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| a87bd2a9-69b1-3dc9-b473-2c46ef78cdb3 | -8.7631 | -46.4418 | 2026-08-31 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 251.1 |
| c11f0cb8-0a51-3ea2-a131-5e346c2db5cc | -11.2294 | -45.099 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 299.1 |
| 44a008f3-c251-3a90-a963-060ae16e7301 | -5.5941 | -42.338 | 2026-08-31 14:30:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| c8f9e643-2000-36b9-b8f8-0d5c71620900 | -11.229 | -45.1221 | 2026-08-31 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 532d8360-1ce6-325a-81a1-02a9b6d98b74 | -7.9797 | -44.2962 | 2026-08-31 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 263d9052-c9b3-3c44-b456-47f959710cb4 | -9.1904 | -51.567 | 2026-08-31 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 47dd6f15-544a-3cff-bedc-4e4067db4793 | -7.9907 | -46.5177 | 2026-08-31 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 138.3 |
| 90e2df04-070c-3367-9ef1-6a6dcbf2914f | -7.2934 | -60.5713 | 2026-08-31 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 92c23364-cf04-3098-b55b-d50deed4f7f0 | -11.0566 | -51.4539 | 2026-08-31 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |


[Clique aqui para ver as próximas entradas](README94.md)
