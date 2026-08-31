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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 45606431-dea5-38f6-9d38-de7c06032e71 | -10.83937 | -45.31799 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19c74720-42f9-332a-a5e7-8505193f0a5f | -14.44068 | -52.52741 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4429a279-dd39-3397-ba53-ce733b90da0f | -14.57833 | -54.11879 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f8119cc2-a1f7-3edd-815a-c40a309cf92e | -10.81906 | -50.68415 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e834659-39ba-3efb-9dc0-f5bc5bcefa70 | -7.58211 | -61.35093 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a881fef-a47e-334e-a1bc-f7cbb4abaf06 | -11.32813 | -45.17699 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4af1dd4f-c778-3cfc-bcc1-fd613e205bdb | -10.4917 | -59.61257 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 995071b9-ab0d-3275-a297-1c686e53a7a4 | -9.30615 | -56.80487 | 2026-08-31 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2584a0e-34cc-33fc-b48c-0b56c15a9d40 | -9.79856 | -60.1756 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d64b194d-6893-30a1-b39a-b3127b04e04f | -14.44251 | -52.54138 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21d78b0d-b1dd-39d4-a0d2-adbdd0858b34 | -9.24781 | -60.43183 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7d76f38c-68c4-3fba-82d1-5a65c0c47540 | -10.76427 | -53.99847 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92cee35a-be27-3286-98a2-6b74f7d4a7ac | -14.44621 | -52.54187 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 395c297b-31ca-3753-bfe7-6ff9958e885b | -9.05368 | -65.41499 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc7f0fd8-840e-3bf9-a66b-c29e9d011b33 | -11.69319 | -47.60991 | 2026-08-31 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| da9bb0d6-7098-35f9-9056-f73695a6ba2b | -14.19797 | -52.87474 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d6271be-12f4-305a-ab9b-9dea1ccc9538 | -14.60639 | -54.09563 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 78222eb8-5677-343c-b686-0a71db08eb6f | -8.49792 | -55.29219 | 2026-08-31 04:59:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0d6c311-c93e-325b-bb96-023b9d2de1a7 | -14.17266 | -52.87092 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e24b6943-a3a8-3e7d-b0d3-af1bbfa94ef8 | -11.95669 | -63.28844 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c20bbf83-d9c8-3f31-85fa-abc80d1f86d7 | -9.30955 | -56.80541 | 2026-08-31 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57b70041-ef70-3a74-8741-64a593f92e54 | -9.47602 | -57.01612 | 2026-08-31 04:59:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ceca3d68-6051-3c9d-8b5a-70097394483f | -9.70813 | -60.75436 | 2026-08-31 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f2183c8-213b-34b0-a453-ad8019fffbee | -8.56126 | -54.71471 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bad6880b-b9a6-393b-b0d8-6cd48f9bf37e | -11.36919 | -45.221 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f15092b-8b59-380a-9c7f-263491dffb21 | -14.58348 | -54.10772 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1f62f76-deef-347c-960d-d955ae335666 | -10.14595 | -45.76304 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 44887cdc-ae35-3179-858e-8e0403955242 | -14.39897 | -52.53705 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcfecbc0-96d8-3114-90d6-a27a4c37ff7d | -12.08316 | -44.9856 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62402d07-3413-3a5d-8583-ddf8ec165d2c | -13.46763 | -51.41381 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 531c9a9d-3f4a-3cbd-aab6-50778907dfa4 | -10.75554 | -44.87588 | 2026-08-31 04:59:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ae61c19d-d6bc-3446-82a0-8171c365ab3e | -9.36976 | -60.3117 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07cc407c-89bb-37b4-8f81-b63b06560fa1 | -11.18741 | -55.09713 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3478467a-920c-3197-9580-5190d05a5aca | -9.72343 | -64.99864 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3538d5c-c7e5-38a9-9e21-3a79842ffcc7 | -14.2009 | -46.5675 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7bbd727f-6874-33ab-b558-d4de6eee56c2 | -9.2298 | -59.58471 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 09b491a9-7858-3d87-bd98-3e0ec55fec91 | -9.40147 | -60.59097 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b3aa859-2784-3010-9851-1a2e5f344d62 | -12.39957 | -46.45026 | 2026-08-31 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7617cac1-9e95-3fef-ab09-aaab8eab9850 | -7.92451 | -61.33519 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43124c45-4438-3032-8539-95e138f754be | -11.1841 | -55.09661 | 2026-08-31 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90fa2128-ae46-3369-b3ba-6efa26f13e8c | -11.15963 | -50.56647 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| f623b56d-0ce4-3ccd-907b-e720f0235d33 | -11.33756 | -45.1951 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2f58ebb-b1b7-3453-be28-63cd0772a4c3 | -14.20282 | -44.59031 | 2026-08-31 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a62963a-683a-35ce-b581-1c1bfd72fe91 | -9.15365 | -59.55836 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 141253f9-0c6c-3bd3-8861-9a64d66ccbaf | -11.33182 | -45.19453 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c44a30af-e245-3edd-b748-c478736eec29 | -14.145 | -52.79846 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e964c396-d545-3333-8ac8-872cfd32423b | -14.51874 | -52.18326 | 2026-08-31 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62fe81da-c204-3af9-90d2-582dfb106c75 | -11.34637 | -45.21803 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34d245e2-8c40-3e82-9d10-30e614665fe8 | -14.58804 | -54.10066 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 412fd1e4-1bff-380c-8789-8281a7fc5972 | -9.47121 | -51.58056 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e914917-7dc2-3553-85e9-7b31676b0a42 | -10.78287 | -50.71327 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d1aa67e-08d7-3bef-9321-94e2227ff119 | -11.33284 | -45.18607 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1380f47c-c1b9-33c7-843e-40341660dff7 | -12.94464 | -45.90599 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7491ade5-8d5d-3951-a12b-ec9494a4c8a6 | -9.94859 | -46.31292 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4c34fc0-3592-3f99-ade7-97de2106a91a | -10.14864 | -45.69642 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 720c0648-aaaa-3166-aae4-4b54c9fdb045 | -14.40392 | -52.52874 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b907b6a2-6158-365a-9a9e-fa1029c38b63 | -9.9387 | -60.50524 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be5f274f-0d5a-3e84-8c87-780c7c439704 | -9.15532 | -59.54841 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ee938d7-4570-3af2-ac0f-5c49d28d0fc8 | -10.48077 | -59.61823 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b4b6a10-9f2e-315b-acff-44474ad6a757 | -9.20838 | -60.87881 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c42c5a3-8e75-3c24-a01b-25e61ef85abc | -6.1295 | -57.6637 | 2026-08-31 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 05cb1372-7499-3e57-863d-d9662f091631 | -7.3119 | -60.5706 | 2026-08-31 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 51ae4f94-c5e7-3067-b45b-ab864ef51402 | -5.2547 | -55.9105 | 2026-08-31 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 204.4 |
| 25840c25-ab2d-3a7b-817b-aec33887014d | -6.1294 | -57.6833 | 2026-08-31 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| cc987d3a-4101-30b0-858a-b3f3c01d16f2 | -11.1634 | -50.5727 | 2026-08-31 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 9d8077c7-ff7c-3624-9c3b-1986171836c0 | -5.2362 | -55.9112 | 2026-08-31 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1c533f68-6b63-36fc-9f1d-3232da43d6b0 | -6.6036 | -58.5972 | 2026-08-31 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 0a6b435a-16aa-358e-8c78-ea3fc0634f2e | -6.1111 | -57.6645 | 2026-08-31 05:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 59d108a3-05b4-30c0-b7f6-36bb7bdd8fbb | -6.622 | -58.5965 | 2026-08-31 05:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| cb1a2973-0f8e-3f9b-94a0-ce85ae5fe75b | -5.2548 | -55.8907 | 2026-08-31 05:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3d0791dd-1818-3896-9649-f78ddcd5e7e2 | -7.9236 | -44.2558 | 2026-08-31 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 272c5e2e-08e8-31a5-82c0-97fcb027e46d | -11.1637 | -50.5513 | 2026-08-31 05:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ee63e445-00d5-3bb3-9cc6-ab522b861558 | -7.3118 | -60.5897 | 2026-08-31 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7b78e810-1193-3b7c-af82-e93a249f75f5 | -15.36565 | -53.80328 | 2026-08-31 05:01:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2554aee-231d-39e0-9f55-df7cfabfa038 | -18.28257 | -52.69036 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d7e74ef1-3b4d-3bcf-8a1b-76863cbaf062 | -15.23972 | -56.38545 | 2026-08-31 05:01:00 | NOAA-21 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f94d43e-fb57-356d-967e-ab6cc43d3afa | -15.87655 | -56.48737 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec2a3821-4d79-37ee-88d7-633654618b41 | -15.58575 | -56.01774 | 2026-08-31 05:01:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7287c3b3-c394-3eb0-b732-4c07aff582ee | -20.25596 | -58.15499 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 15451693-8e1c-3797-b0d4-e846cf4383f9 | -18.27494 | -52.70681 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85bb22b6-bb7e-3ad4-8837-a8e8d9202e79 | -15.41495 | -52.71384 | 2026-08-31 05:01:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d3caadb3-1c87-3809-9bfe-1d72adfab37c | -19.07874 | -57.40448 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 24ef2cfa-b365-38a2-85b3-9a575a0dc6ce | -15.24385 | -53.87191 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58c27014-0df4-3e63-a962-ad92f55b3812 | -15.12268 | -53.58291 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60e8548a-cccb-31c4-b681-67751e9428bd | -18.27624 | -52.67928 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e39601a-dc28-308a-a41a-f3c53f69ec94 | -15.63967 | -50.09893 | 2026-08-31 05:01:00 | NOAA-21 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38427c11-255a-3aa3-a255-39866aaae3db | -15.92097 | -56.2233 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f7f1fba3-0b52-3bc5-a5e0-80289f43ff8e | -15.92152 | -56.21972 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5b86c37d-4b8f-3e77-92f7-d161f89acba9 | -15.78548 | -56.43938 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08952327-8e75-368f-b5af-6d1fb2f3884d | -15.61213 | -56.39567 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a74393c7-9e11-3778-9a5c-79565010509e | -15.24327 | -53.87592 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a71b0790-884d-3429-88a5-270755ba04fe | -15.61488 | -56.39979 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3c25192-0aad-3293-8cb4-34635c01a862 | -18.28452 | -52.69307 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 94ff962f-733e-344f-b649-97c9c2edc868 | -18.28775 | -52.68099 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5779ff20-7ea0-3321-b2c7-2572d0067dca | -18.28261 | -52.67755 | 2026-08-31 05:01:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99c070d4-cef0-3935-bc3d-0854907ca645 | -15.61872 | -56.41874 | 2026-08-31 05:01:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d697f0e5-3a11-3b15-9e93-a9ba8b9cc6a7 | -20.24932 | -58.15381 | 2026-08-31 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2a516794-bc3b-3325-9895-0eea1166dec6 | -15.23686 | -53.87088 | 2026-08-31 05:01:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ac5b366-7c5c-3cb2-9565-d42e0c459cbe | -15.67847 | -56.27476 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8ac2d164-7340-36d7-9304-0dc949079001 | -15.55091 | -56.28686 | 2026-08-31 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README55.md)
