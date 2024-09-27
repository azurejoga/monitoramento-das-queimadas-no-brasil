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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 477ec446-9d89-3a70-8dbd-2f6d329b8aeb | -9.1032 | -61.3343 | 2024-09-27 04:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 3f940118-1bc9-3955-8397-0f7c57d31083 | -9.1215 | -61.3717 | 2024-09-27 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| d01e5905-beb5-3664-b3b6-d166eaf4e0fb | -9.1217 | -61.3334 | 2024-09-27 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 939def8c-222a-31bb-a592-ba5f8dcfc7d3 | -9.1216 | -61.3526 | 2024-09-27 04:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 77d761ce-d517-3c83-bb46-5736ffb61b53 | -9.5829 | -50.137 | 2024-09-27 04:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| a34f5716-c441-3605-af30-aa91af70b32e | -9.6018 | -50.1352 | 2024-09-27 04:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| bee27f73-45ca-3b03-83f8-52508a9d74b5 | -9.602 | -50.1139 | 2024-09-27 04:16:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f2c0aab3-7275-33f9-8535-57004761f712 | -9.949 | -60.2334 | 2024-09-27 04:16:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 59e607c8-4e8f-31de-9d84-3d2b97a8bfcf | -10.0322 | -53.4859 | 2024-09-27 04:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 1b391f25-c014-306f-a146-b96df0831920 | -10.0324 | -53.4654 | 2024-09-27 04:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2c040fa6-cd33-3ee3-a66b-ed4e43a599c4 | -10.0327 | -53.4448 | 2024-09-27 04:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| c3f01b32-f0e7-3199-abc4-07d7498e4ad4 | -10.0329 | -53.4242 | 2024-09-27 04:16:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 8131de35-1b5a-3496-b0af-9c26a51698d8 | -10.1501 | -49.9956 | 2024-09-27 04:16:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 07d569cc-3e5f-35c8-8fea-f03fa1d62ddc | -10.3672 | -53.7858 | 2024-09-27 04:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 05d45622-ac44-35e2-82e0-e71f43df79ed | -10.7214 | -51.0657 | 2024-09-27 04:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 01cf6231-5d6e-3456-8666-fff27f58c33b | -10.7403 | -51.0637 | 2024-09-27 04:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ce1820d1-7d6f-3b7b-bf3b-e46f00700c2f | -10.9264 | -54.2692 | 2024-09-27 04:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| ed5f05be-53d5-31bc-9733-5d60ba990254 | -10.9267 | -54.2488 | 2024-09-27 04:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 71442cf9-dbfa-3f98-a276-f8f8f84e583c | -11.2034 | -54.7752 | 2024-09-27 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b3e40544-3499-380a-9363-de893f466c33 | -11.2223 | -54.7735 | 2024-09-27 04:16:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 653f96cf-730a-3386-8577-e7ff7c85f6fc | -12.6636 | -54.6782 | 2024-09-27 04:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 7ec44ac8-f421-3762-b7f1-3da628b7e237 | -12.6639 | -54.6577 | 2024-09-27 04:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 6fde0967-556f-3829-be90-cfef809c845f | -12.6824 | -54.6968 | 2024-09-27 04:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| fceadf9b-30c9-353a-8fdb-cc05e7e12a62 | -12.6826 | -54.6763 | 2024-09-27 04:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| fa516c75-6df1-3e76-a3cc-5ff768dca5ac | -12.6829 | -54.6558 | 2024-09-27 04:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 931ed906-b443-346d-ae27-2f74c242e942 | -14.8443 | -51.4616 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 49998efb-2f30-3db0-982f-527eeae7a9db | -14.8634 | -51.4804 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| a4bb3c96-aa1c-3737-b9b0-c31edcee7ea4 | -14.8637 | -51.4589 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| e13f7ee1-7f1e-39dc-b6ed-7f8b7c162792 | -14.9216 | -51.4722 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 43c29d11-fce0-3a15-a79f-672c082db274 | -14.922 | -51.4507 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 214.3 |
| 2728ef1c-0796-3bf0-bfe5-9a7189540e3f | -14.941 | -51.4695 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 251.9 |
| dcf1299b-7f74-3d9f-968a-b4de530f9729 | -14.9414 | -51.448 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 050a5c06-2a8e-387f-8816-de662c4cceea | -14.9605 | -51.4668 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 9d3f5581-1597-3c9f-9d39-c207438338ea | -14.9609 | -51.4452 | 2024-09-27 04:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 15976628-64d2-3890-a169-786fa02a47a0 | -16.0793 | -51.9709 | 2024-09-27 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ac2ccdf7-cb29-3002-87da-53af1f258ae6 | -16.0989 | -51.968 | 2024-09-27 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 9a9af19a-7dd8-3733-8a77-15fa1e391ca9 | -16.0993 | -51.9465 | 2024-09-27 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 142.5 |
| be3a09d1-2ef0-323e-aba9-8e88ba857556 | -16.1185 | -51.9651 | 2024-09-27 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0dede813-c2d9-3883-9b3b-60416ea5f051 | -16.1189 | -51.9436 | 2024-09-27 04:16:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 496f19f4-4cbf-3cb8-bad2-773563e28885 | -19.6136 | -42.8159 | 2024-09-27 04:16:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 124.1 |
| 97dca5a5-1578-307d-8f6b-c2cd86c03f0d | -20.1828 | -43.5049 | 2024-09-27 04:16:57 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| fc823038-c36e-3a52-bfef-f4fc874f9668 | -20.5199 | -41.952 | 2024-09-27 04:16:59 | GOES-16 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| 446adc98-c8ad-335f-bafa-840d39ef7bbf | -21.9409 | -48.4514 | 2024-09-27 04:17:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 7e787010-1776-3f27-a37d-6576fdd7d150 | -22.2891 | -48.5766 | 2024-09-27 04:17:09 | GOES-16 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| cfcaf31c-9c69-3016-ac1e-7096b493671a | -22.7433 | -44.8035 | 2024-09-27 04:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| a7badafd-1b80-3aaa-a3b0-7544f8b77880 | -22.7442 | -44.7785 | 2024-09-27 04:17:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.9 |
| 3eb95dc4-38f2-3f35-ac99-36badd5e96ff | -7.5703 | -60.5984 | 2024-09-27 04:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6abf2abe-8046-304a-bdb5-22108bd2fdf1 | -7.5887 | -60.5976 | 2024-09-27 04:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1e31a738-9809-3b8b-a9d0-9e9b2229238a | -7.5888 | -60.5785 | 2024-09-27 04:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 49a174d4-d27b-3b28-8551-8b29c55146c5 | -7.7701 | -61.1825 | 2024-09-27 04:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 164afd7c-16a2-32ec-a417-533207336283 | -7.8156 | -54.7252 | 2024-09-27 04:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 06c12d8b-b219-3246-8a98-e081ab3367bd | -7.7886 | -61.1817 | 2024-09-27 04:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 43c27124-9fa3-3484-af77-557d360c3e31 | -7.77 | -61.2015 | 2024-09-27 04:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 757026d4-0f9b-36f9-ad12-a033ede61c92 | -7.9175 | -61.2718 | 2024-09-27 04:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4f9d2271-70e4-3ac7-8e69-7bdfa1aa653a | -8.1394 | -61.2817 | 2024-09-27 04:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8bc7f530-bce6-3399-adfd-27fd4beb0a93 | -8.1395 | -61.2626 | 2024-09-27 04:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5f19082d-fb28-3a51-8059-11709a461242 | -8.6101 | -63.1226 | 2024-09-27 04:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 0db02cbf-ed6e-3f0f-a582-6dd360f15b9e | -8.8117 | -67.6732 | 2024-09-27 04:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 103a6faa-c18e-31c9-991d-d833d8338f3e | -8.9978 | -67.3724 | 2024-09-27 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| c1e02ca0-7576-368f-bce1-2bc3d6f4db66 | -8.9978 | -67.3538 | 2024-09-27 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 65a21d55-0d80-3417-9060-eada0f1eb5ad | -9.0163 | -67.3719 | 2024-09-27 04:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 931a1341-d53e-3f61-9b5c-2a7ebbb75832 | -9.0657 | -61.3743 | 2024-09-27 04:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c66408c2-1baf-318f-96c3-7385a0776128 | -9.949 | -60.2334 | 2024-09-27 04:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b7e3e43d-6cee-3550-8429-ae4bbbdbeebb | -10.3672 | -53.7858 | 2024-09-27 04:26:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 9be9ecbb-0699-373f-9eef-97648d4d3c09 | -10.7214 | -51.0657 | 2024-09-27 04:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| a77967d6-cdc8-3fa9-a1f6-e81709d65851 | -10.7403 | -51.0637 | 2024-09-27 04:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 58b780a4-c6e3-33dc-bcf6-1108bb6685ab | -10.6871 | -64.1335 | 2024-09-27 04:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| fd79dbe6-785b-345b-ba59-a9196d0a3190 | -10.7057 | -64.1327 | 2024-09-27 04:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 88.6 |
| ca3933e2-9586-33cf-88b0-788822b015f4 | -10.9264 | -54.2692 | 2024-09-27 04:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| a5180247-d3cd-3ced-98fe-5a9ba40f7446 | -10.9267 | -54.2488 | 2024-09-27 04:26:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 68ed2b1a-3476-3f82-b9d7-2abf9a44e50b | -10.9168 | -60.8351 | 2024-09-27 04:26:09 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 3bc762dd-6d49-3e65-8705-82e8cb824e65 | -11.2223 | -54.7735 | 2024-09-27 04:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 65b6f7d6-b161-32ab-8b3e-f3b63ed3f42c | -12.6636 | -54.6782 | 2024-09-27 04:26:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 840171e7-a822-32b5-a3a6-0b868a56aff8 | -14.8443 | -51.4616 | 2024-09-27 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| d8c07ebf-7319-3f59-adf5-32763967fd5d | -14.8637 | -51.4589 | 2024-09-27 04:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 4e51903a-5a17-3688-988d-525c64d8774c | -16.0989 | -51.968 | 2024-09-27 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 138.7 |
| cb40948a-6c74-3982-8d6c-12105b38f652 | -16.0993 | -51.9465 | 2024-09-27 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 144.8 |
| abc96bf5-5a49-37a0-8afd-6cc5943b77c9 | -16.1189 | -51.9436 | 2024-09-27 04:26:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d0127989-44f7-37d3-93da-afa386b71da9 | -16.8933 | -58.0213 | 2024-09-27 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| cdef1ba6-f466-3aaa-a09b-6e4125830d92 | -7.4605 | -60.4114 | 2024-09-27 04:35:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 28a059b6-ea61-3462-b9ae-57c3754992bf | -7.4606 | -60.3923 | 2024-09-27 04:35:49 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 93f4a8e2-2f16-3f6f-a037-68cd8c2ca252 | -7.5703 | -60.5984 | 2024-09-27 04:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 8f08588c-2b16-3d3a-96f4-5e7dc7996f8e | -7.5887 | -60.5976 | 2024-09-27 04:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| ee55028e-d022-30d8-9dcf-797eea987239 | -7.5888 | -60.5785 | 2024-09-27 04:35:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 89706950-eabc-3f27-be84-843356b096b9 | -7.77 | -61.2015 | 2024-09-27 04:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 510d92c2-0ed8-3e10-838e-b6fee56dd788 | -7.7886 | -61.1817 | 2024-09-27 04:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| f7dd36f9-6d04-3192-b133-09b4493cba0b | -7.7701 | -61.1825 | 2024-09-27 04:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 1049d680-4151-3c3a-81a7-aaffd54b64f9 | -7.9175 | -61.2718 | 2024-09-27 04:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ffdc1226-d238-3355-b1fa-8ab634fea523 | -8.1394 | -61.2817 | 2024-09-27 04:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ce1c6371-6a53-3507-8772-88655eb1564b | -8.9978 | -67.3724 | 2024-09-27 04:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6ca85ace-b4a8-3981-873e-be09dc166861 | -9.3672 | -63.6972 | 2024-09-27 04:36:00 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| eac69fb7-6b56-3522-be16-94f99d97b94b | -16.893 | -58.0417 | 2024-09-27 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| b4e4023c-be13-3007-b975-2edcfff25e19 | -16.8933 | -58.0213 | 2024-09-27 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.4 |
| 2d1d72ea-a460-347c-971f-e8abb16af3e4 | -17.0209 | -56.1603 | 2024-09-27 04:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 129.2 |
| 06674e06-3616-3cd2-965d-954fce086343 | -1.0466 | -53.35172 | 2024-09-27 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46ff7d4b-958e-3ce9-ac47-eab4117832c1 | 1.30515 | -52.99447 | 2024-09-27 04:38:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c9f478-0782-3511-9b14-33f2a735a6cf | -1.62268 | -54.77626 | 2024-09-27 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e058c2d-d60b-36ed-8a0c-8bc33b4109bb | -1.57115 | -54.33288 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76cd70ca-9d62-313a-8a0e-40f93e4a6ea0 | -1.5705 | -54.33697 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 692e8d70-0303-3c72-b674-a1d4ed76b504 | -1.19267 | -54.20779 | 2024-09-27 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README69.md)
