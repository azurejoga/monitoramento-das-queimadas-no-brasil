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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 809f6992-de9c-3be6-9110-6fa433fe049b | -14.91121 | -44.673 | 2026-09-04 11:32:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 99913e12-2cad-3e18-976d-2ee2c657b9b3 | -14.24107 | -41.4257 | 2026-09-04 11:32:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 806e685f-b2ab-35a5-9bd8-2bc925557606 | -16.81559 | -44.0185 | 2026-09-04 11:32:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8183e540-fb8f-39f6-b683-3b517e4dff3c | -12.59829 | -42.74969 | 2026-09-04 11:32:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c95a06ba-8355-3018-aa3f-1b877752ea14 | -14.24255 | -41.4139 | 2026-09-04 11:32:00 | TERRA_M-M | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 52c90bb2-7617-3ff1-bd87-878d550d99f5 | -16.81426 | -44.02822 | 2026-09-04 11:32:00 | TERRA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 721855e5-c234-38aa-b8f3-6686ee864e0b | -12.00884 | -43.28971 | 2026-09-04 11:32:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| caba6a56-8346-3407-b4b8-d64ba14ff524 | -12.01014 | -43.28043 | 2026-09-04 11:32:00 | TERRA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 64e910fe-f577-333f-8b7d-a06d607a171b | -16.51391 | -46.59151 | 2026-09-04 11:32:00 | TERRA_M-M | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5e864e16-8c25-3807-9859-098ee8c535b2 | -14.90993 | -44.68211 | 2026-09-04 11:32:00 | TERRA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 59b06a91-ec23-36b6-8233-b49c879d4354 | -12.59961 | -42.73985 | 2026-09-04 11:32:00 | TERRA_M-M | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 2ef7ea9d-dcdf-3080-ab40-3c3e80f437a5 | -13.40421 | -41.89544 | 2026-09-04 11:32:00 | TERRA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| eed12c5d-891b-3dd5-a510-ec094540dc76 | -17.07345 | -45.40396 | 2026-09-04 11:34:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6f510709-c5f5-39c4-bee8-9cbfe7a3361d | -19.01903 | -47.05705 | 2026-09-04 11:34:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e983a3f1-9c47-311a-975e-076467b2f7f4 | -19.59224 | -46.54157 | 2026-09-04 11:34:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d5e5097f-69ac-3d60-b3ab-cbd920f43038 | -20.0842 | -45.81797 | 2026-09-04 11:34:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ceb9b01-aaab-37b1-b1b2-3a4cdcc5aaac | -19.85579 | -46.3817 | 2026-09-04 11:34:00 | TERRA_M-M | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 244e2587-5160-3f9d-ad35-c7b1a32de5cc | -23.28034 | -46.60384 | 2026-09-04 11:34:00 | TERRA_M-M | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 86c7af16-c8cf-3834-a11c-765510d82c2d | -16.85217 | -46.29755 | 2026-09-04 11:34:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 280a41f3-4762-3681-a91e-be7ccdf741d4 | -19.2854 | -47.18801 | 2026-09-04 11:34:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 76749f26-c743-31ef-af97-92a1eb04f703 | -19.28683 | -47.17839 | 2026-09-04 11:34:00 | TERRA_M-M | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b1a9fbe-c540-3910-b34b-146abd6f08b6 | -19.69356 | -40.24497 | 2026-09-04 11:34:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| dcc573d7-ec00-3204-a254-059e0f4ade97 | -18.57496 | -48.28199 | 2026-09-04 11:34:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 02b4a52a-b3cc-3d4b-9484-da4998cbe51a | -22.84273 | -49.34349 | 2026-09-04 11:34:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 37.3 |
| b0753b29-a5f4-30e1-b801-a2287d0e21cf | -18.23437 | -40.45952 | 2026-09-04 11:34:00 | TERRA_M-M | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 3d54867f-c32e-31fd-8fb1-bd0ce1c6d9da | -19.69551 | -40.22694 | 2026-09-04 11:34:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 20.1 |
| 77e6d736-2d17-356a-aaf5-a0bc1a74ffce | -21.9333 | -49.00549 | 2026-09-04 11:34:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 5fcb0100-d27b-3026-a102-d2032e943771 | -21.06588 | -48.46354 | 2026-09-04 11:34:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b8a099c7-2e31-35e1-9637-010246371f94 | -20.66191 | -44.96022 | 2026-09-04 11:34:00 | TERRA_M-M | SÃO FRANCISCO DE PAULA | MINAS GERAIS | Brasil | 3161205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 5f1e85f4-a15a-37fa-8e07-2eaaf7de8e21 | -19.5936 | -46.5322 | 2026-09-04 11:34:00 | TERRA_M-M | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e3d7c87e-7562-3ba9-97fe-e876baec4297 | -20.07534 | -45.8166 | 2026-09-04 11:34:00 | TERRA_M-M | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cf631741-fb48-3676-aa3a-c72ca71797ec | -18.52231 | -48.18602 | 2026-09-04 11:34:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f9b6c99-e14c-3048-ba63-e22145d47729 | -17.30429 | -48.79811 | 2026-09-04 11:34:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| da8e5a8e-59c9-376b-b630-e35d1dc289be | -22.85217 | -49.34525 | 2026-09-04 11:34:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b99bd2b6-09e3-3a3d-866c-ae20801fd590 | -19.01761 | -47.06662 | 2026-09-04 11:34:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| c66ec33e-baa4-39e6-8cd4-8537f34b7593 | -8.6101 | -67.1783 | 2026-09-04 11:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3a3f66ff-d000-347f-ad08-9d07e6c0f5e7 | -5.598 | -43.9978 | 2026-09-04 11:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 313a0546-1558-3781-a73d-7883d4aa13c3 | -5.598 | -43.9978 | 2026-09-04 11:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 7611b387-14c4-31e3-ba89-1d03d6a80e45 | -5.598 | -43.9978 | 2026-09-04 12:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 11584e38-6124-316a-9fb5-503f2d5c255f | -5.5978 | -44.0209 | 2026-09-04 12:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 252a9ebc-0d96-3ff1-88ed-e09684c584b1 | -5.5793 | -43.9992 | 2026-09-04 12:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| df050e06-f69e-3ba1-b314-eb73d4445d16 | -5.5982 | -43.9748 | 2026-09-04 12:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e94f4807-e83a-37dd-bb25-215eca3dddf3 | -5.5793 | -43.9992 | 2026-09-04 12:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| fc1a75ef-b822-3503-be8e-87b5e95274fb | -5.598 | -43.9978 | 2026-09-04 12:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 2476cd4f-94f8-3509-978e-ed2db311923d | -5.598 | -43.9978 | 2026-09-04 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 21cf94a2-b24c-314c-909e-30dba6a385f8 | -5.5793 | -43.9992 | 2026-09-04 12:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 048d4e59-04a3-37d1-9e5d-4dee1a6da20a | -5.5793 | -43.9992 | 2026-09-04 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 36ed52ad-5125-3a74-892d-07ee5e671d21 | -5.598 | -43.9978 | 2026-09-04 12:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 285.0 |
| 64a72864-ed5b-3c33-8454-eb716a5cb58f | -5.598 | -43.9978 | 2026-09-04 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| fef32773-0bbe-35b8-933e-c090b3fa8b9b | -5.5793 | -43.9992 | 2026-09-04 12:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c62b1c26-9158-3238-b4f6-6e8042c7c782 | -5.565 | -60.1739 | 2026-09-04 12:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9e021c56-bc8c-3409-afaa-95d6cfb9b553 | -5.598 | -43.9978 | 2026-09-04 12:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 32f88734-87d8-378f-ac19-6baa076efd8c | -19.0948 | -57.3641 | 2026-09-04 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.5 |
| 9d03cf59-2a18-3ac0-8731-e97069acdd6f | -19.0748 | -57.3668 | 2026-09-04 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.2 |
| 3e6ece60-55c0-3370-a294-96ebd19bba46 | -5.5793 | -43.9992 | 2026-09-04 12:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 7d423c8f-cdcf-3f4c-af81-9c6a578dbf58 | -5.5978 | -44.0209 | 2026-09-04 12:50:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d0882835-bab1-3629-82b4-72d2217557e1 | -5.565 | -60.1739 | 2026-09-04 12:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3e02526a-82f4-35f3-beec-fb3e3c06b330 | -3.234 | -50.5789 | 2026-09-04 13:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 6cd112a9-c101-32b4-bcb4-54f6d6d6dce7 | -19.0748 | -57.3668 | 2026-09-04 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.4 |
| c8ac67ff-ccc1-3461-ac78-78cc94de7032 | -5.598 | -43.9978 | 2026-09-04 13:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 167.4 |
| bf0db655-c6f4-3ae1-a69e-8b77b33b79da | -19.0948 | -57.3641 | 2026-09-04 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.3 |
| de1be9ae-900f-3de9-b42d-929dcf3c4a7d | -5.5793 | -43.9992 | 2026-09-04 13:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 8a805fcc-b7cd-3725-9167-ca4a67ed2bb7 | 3.59513 | -61.17299 | 2026-09-04 13:04:00 | TERRA_M-T | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 9bb77899-0224-307f-a0b1-0c218a82a6f8 | 4.93887 | -60.16424 | 2026-09-04 13:04:00 | TERRA_M-T | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 86492379-3577-3b4a-8965-4b30ba16a548 | -3.76458 | -61.74864 | 2026-09-04 13:06:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d3aecb8f-acb4-3835-9cc2-b4bc140b932d | -3.77659 | -61.75024 | 2026-09-04 13:06:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| ae5248ef-cf78-3b80-ae99-fb562d0b9d30 | -3.02637 | -61.47221 | 2026-09-04 13:06:00 | TERRA_M-T | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 19.0 |
| c2a91348-fa04-35ca-a26e-8f86f8053be0 | -3.77428 | -61.76728 | 2026-09-04 13:06:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 88db0c6b-f2e5-3209-854a-208c2f085b42 | -3.02394 | -61.48963 | 2026-09-04 13:06:00 | TERRA_M-T | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 3b54521f-3a6b-3d90-a8cf-1c75b02d2b93 | -4.13422 | -63.17118 | 2026-09-04 13:06:00 | TERRA_M-T | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3d488fdf-6a7e-30e7-a2f3-de9862829db2 | -9.11057 | -65.49959 | 2026-09-04 13:08:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bf23c99e-f7bf-37fa-a5cb-59c978ff7c09 | -8.6771 | -66.94594 | 2026-09-04 13:08:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| d96d2f21-fd9f-38ee-b22a-aace9d722a3c | -6.68844 | -59.99578 | 2026-09-04 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3efc2f21-dff2-31d3-afcc-55b5d916eea8 | -6.69161 | -59.96955 | 2026-09-04 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 0a626e70-6278-32aa-baa5-22de9f92a821 | -7.55754 | -61.34181 | 2026-09-04 13:08:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 71131c4f-683e-3b0a-8f30-661080b7b8f0 | -5.57008 | -60.16342 | 2026-09-04 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 1341d413-de99-3061-82d2-c4bfa01dd021 | -7.55676 | -61.32576 | 2026-09-04 13:08:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6379f5d0-9ead-3d0c-ac39-5f464d34481c | -9.10949 | -65.49299 | 2026-09-04 13:08:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cb6dcdfe-20c0-3ca7-9f1f-22ff719049a2 | -6.68712 | -59.98904 | 2026-09-04 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| f106a4d3-7ca3-3fd3-af50-01e3f713f98c | -8.59751 | -67.18435 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a652aa6c-4714-3370-b846-80b75ba6c549 | -8.60752 | -67.18241 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| b17548fb-2221-31bf-9a19-37efb9626d21 | -7.55412 | -61.34711 | 2026-09-04 13:08:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 795c35b3-17f3-3be5-8396-a6a18b0b68bb | -7.02851 | -62.97902 | 2026-09-04 13:08:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b45f7cb3-1c09-3c26-bb1e-5c7f6ca4a925 | -8.60625 | -67.19161 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 73282dce-9ef5-376f-a2fe-ea75f8ee6571 | -7.01705 | -62.97754 | 2026-09-04 13:08:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e8b7d7f4-9ee5-3fc8-8ced-dad2544ad1b9 | -6.67587 | -59.96117 | 2026-09-04 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ce5fe26d-3292-3288-8df5-2e9455247897 | -8.59881 | -67.17515 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 58bb5ee5-723e-368f-bfcf-56352626ff65 | -8.6088 | -67.17319 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 605617d3-13dd-3f1a-82fc-f79904914d5f | -9.04599 | -65.73996 | 2026-09-04 13:08:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 28562c24-6491-30f5-af66-e64ff94a4ebd | -9.20923 | -64.44407 | 2026-09-04 13:08:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 46c661eb-c8f0-312b-9e6d-53297355eee9 | -8.52689 | -67.16528 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3a88cee-abb8-304a-b3e5-20292f288784 | -9.57508 | -64.28613 | 2026-09-04 13:08:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fca49498-375a-3d39-bfc5-287228e22424 | -6.69049 | -59.96275 | 2026-09-04 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a98a8035-42a1-3583-9c0a-f8b66b6bf16c | -4.8697 | -66.89214 | 2026-09-04 13:08:00 | TERRA_M-T | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff7a04f4-0777-350c-adb6-2923fa0ee7ba | -8.87547 | -68.61305 | 2026-09-04 13:08:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c8d5915a-2a5b-3b2a-a2a5-e6ba8a3d1ba9 | -7.79172 | -66.95174 | 2026-09-04 13:08:00 | TERRA_M-T | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c982b0ee-f995-32de-8430-500e16a8a769 | -7.58011 | -60.47338 | 2026-09-04 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 0c147f58-4233-33e1-8925-fab5ca212f47 | -6.67922 | -59.93475 | 2026-09-04 13:08:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| e70fc885-4690-3a4c-82f9-5cbd9af9d0ea | -5.5793 | -43.9992 | 2026-09-04 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c9a89f77-0f16-3eac-8591-3a59dc2a2ad8 | -5.598 | -43.9978 | 2026-09-04 13:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 241.0 |


[Clique aqui para ver as próximas entradas](README42.md)
