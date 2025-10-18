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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b06979a-8c7d-36a7-bafb-83b0b6eed5c5 | -13.92491 | -45.60054 | 2025-10-18 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4ee9c948-9bf2-37e0-8872-cd43704ddd1e | -10.46478 | -44.06781 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81787a55-7b5f-3271-b76d-4af1c3ea8f95 | -13.40901 | -47.97678 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4593109d-0a38-3bf1-b6e4-49e9e7287d4c | -10.49572 | -43.43902 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0151c692-c725-3529-bb99-6171b23e722d | -13.70652 | -47.71816 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c8e5a39-c816-3c78-a544-674cdf761e04 | -10.49196 | -43.42372 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aa181e6-a730-3aaa-be7f-cbaa292d1f4c | -12.90279 | -47.01401 | 2025-10-18 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84076d96-6096-3ad9-9153-d8c0a0a1dd5f | -11.43294 | -54.09476 | 2025-10-18 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4f21aeda-94e6-3d74-b76e-7935c1e8775d | -9.21961 | -61.8316 | 2025-10-18 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db3a6e67-4c2e-3a91-b390-7e2695393d03 | -14.91619 | -46.72757 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef17fa33-cfde-35f6-8145-64fbf31b82d5 | -11.75729 | -61.07302 | 2025-10-18 04:51:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5d6779d-9d5b-3d76-9146-fd4fd51ecdbe | -12.24273 | -49.37514 | 2025-10-18 04:51:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42647e4c-76af-33f5-83f8-e66b9a6e8785 | -7.49589 | -63.5211 | 2025-10-18 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 800b6e7b-b4b8-3175-95fc-913666ce18f0 | -14.91638 | -52.42688 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7331eb5d-9987-3fe9-8574-3db2a44876ca | -10.96844 | -45.46433 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 633db4e3-1a69-35f5-9631-c07e30c52132 | -10.24607 | -44.06507 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee79ec3b-03d9-3a96-9dd1-183c2ce4f2dc | -10.49711 | -43.42804 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f63811a4-c676-3769-a964-2935a198725f | -17.50121 | -43.46516 | 2025-10-18 04:51:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6228eab2-b31d-36fd-bca4-07462154cf35 | -8.63409 | -54.62776 | 2025-10-18 04:51:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9a7bf28-e3e2-341e-81b8-3d77c78ce876 | -11.61344 | -44.09429 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a3d771b5-266f-3879-aa71-e4e79196ff39 | -9.77372 | -57.41039 | 2025-10-18 04:51:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| affdec33-ff4a-3cce-9610-5f6ec3ffcfba | -9.2227 | -61.83392 | 2025-10-18 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2ac7a95-57f6-3d59-8227-053749a6f12e | -12.1534 | -45.09101 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 428f2b07-337b-3775-bacf-583d85a6316b | -17.49516 | -43.46406 | 2025-10-18 04:51:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4f2476a-0125-3ad8-9a05-c9538e235aa8 | -10.47939 | -43.43312 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 574ec9b4-804b-3cc7-b5c8-30dac5f7d401 | -14.90724 | -52.41772 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5bf969c-7a72-3931-9ac5-926c9ad17b2d | -10.68885 | -44.5597 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| faa49c5f-a45e-3398-b12f-41b15118340a | -13.76754 | -48.22942 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acf45b8f-84cf-3cd1-8ccb-729e702ea5b0 | -14.09734 | -43.63686 | 2025-10-18 04:51:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36ce176b-8e53-35b5-9478-e473ea2545ce | -14.90156 | -52.3854 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3520e17-24f6-37dd-9b09-3fb70d724c76 | -15.07958 | -48.45918 | 2025-10-18 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3ffa4e7-57eb-365e-8864-7d321f951a5a | -10.55401 | -43.82132 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13d0276d-9a04-34d6-a9cb-86859a26336c | -12.04097 | -54.24496 | 2025-10-18 04:51:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4dc65457-8174-3dd2-aae5-3209dfbc4d18 | -14.90326 | -52.3975 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ae380e0-8360-3bce-bc30-de8a06dbc80e | -12.4608 | -45.46934 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| eee7ce26-b9bb-39aa-9581-b5ec4d36bc1a | -10.02919 | -62.16196 | 2025-10-18 04:51:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1186ce58-3057-3b66-a3ef-81978afdf62e | -14.90268 | -52.40134 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 043b8316-b552-3d6a-9932-0c4222458ea6 | -10.94949 | -45.45616 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bf52f44-2283-3cc0-8e82-0fad11af9b1b | -10.68967 | -44.55339 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9792dffe-9359-37da-96cb-d21e2fd1c2c0 | -10.48545 | -43.43018 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e72afca-4cd8-3f5d-b968-f41349ff0545 | -11.37065 | -44.28307 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b25fcaf-6148-3984-b62e-8890c4a1c50f | -10.23809 | -44.04293 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec51cb1b-6af7-36cd-827e-f2f8ac991ac4 | -10.92372 | -47.98449 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9ba432c-f37f-34cf-81d4-b2350a2fa7c2 | -10.49105 | -43.43092 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a71df252-ce8c-3df1-91e1-e0eacf6ad15f | -9.61284 | -49.67867 | 2025-10-18 04:51:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0466bd93-2a7d-3536-a59c-6816d2f8fbee | -10.7162 | -44.55319 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 656f4c42-91f9-3975-9e64-2321e9cafde4 | -12.44776 | -54.52655 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f66a8e5-84ee-3169-8779-ee179d652101 | -10.48872 | -43.44942 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 43b211a6-95bd-301c-a183-5e3abfbefe67 | -10.71097 | -44.55266 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ce716dc-6f60-3a36-97cf-9701a90820d1 | -13.41328 | -47.97745 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5279c947-9286-3fe5-8958-a0b0913fff0d | -9.53048 | -62.96236 | 2025-10-18 04:51:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70c002a4-4874-36c2-996d-a1309b6a4bd3 | -11.49596 | -44.17854 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82a49c49-2e9e-30bb-992b-e57f4a142610 | -12.75079 | -48.63204 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44a2faa0-ab3f-30ba-9654-2fa682fcf00f | -11.19816 | -47.83321 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a914217-45dc-3fc9-9224-ac893c27f5fd | -10.46523 | -44.06443 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cb50142-2c56-316c-99ef-1327ea384381 | -14.90726 | -52.39419 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6bb2fec-0c9e-3452-a602-1e2984bfc763 | -9.80246 | -51.07255 | 2025-10-18 04:51:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0421d488-c8bb-3c8a-ac85-c8a973d4b83a | -10.14095 | -44.5796 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40e05f89-ef67-3316-9eaa-b57cc1687106 | -10.16342 | -44.52881 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8c57d4bd-ef1d-3793-bbb7-9f904c8249dc | -10.42632 | -47.74458 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3d1c56e-6bc5-38a9-9341-002ae9fe2d61 | -10.18519 | -49.51526 | 2025-10-18 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0efc90c9-d28c-3f67-9af5-e88dc132e89c | -13.08793 | -61.05735 | 2025-10-18 04:51:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7346dc41-bc1f-399e-a656-dbd57e29a16e | -11.37458 | -45.27806 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f63995f6-6b78-3115-9298-d10dae7a3dca | -12.39032 | -47.20866 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84ec2ebb-6b2d-3731-a353-357da41e47cf | -10.07324 | -47.64252 | 2025-10-18 04:51:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8146fe54-68c9-356c-a58c-db353e9844fe | -11.36979 | -44.28988 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d25cf441-c4dc-335d-b3ee-4213d7dc525a | -12.91486 | -48.58345 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dece4ff4-6a84-3ebb-a92e-e2a7560ef5e0 | -10.80241 | -44.02094 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d41fa9c0-12a3-3595-9205-6d8d2e1e1f7a | -10.41794 | -44.91587 | 2025-10-18 04:51:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1290d2d4-f325-32fb-92f7-809a03d3c804 | -12.64808 | -54.76058 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fdd0579-3195-3b2c-9dd8-d1196a8fc358 | -17.48855 | -43.46855 | 2025-10-18 04:51:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ece7bd4-58b5-36d2-bde7-9dc3d15fe263 | -9.90968 | -48.14584 | 2025-10-18 04:51:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4265513-62fb-3e67-80e9-e0b0c664c591 | -11.45383 | -44.20827 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 313b4cda-f0c4-39ed-845a-bd51fb2fea27 | -11.48742 | -44.02705 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdd1eb03-8f38-3126-a558-afbb8613f106 | -14.71113 | -48.31923 | 2025-10-18 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34b678c5-3550-3550-81a7-14b0617c4a7b | -10.16739 | -44.53863 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29e99a52-d241-3feb-bd87-80334288c3b5 | -13.53115 | -47.99768 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be445bf7-5ddf-3fe9-aa27-42f6d8d0964a | -11.4964 | -44.17505 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e79c44df-3c04-3db3-8b8d-9d375fa2256c | -10.24484 | -44.03309 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3aa1135b-7a7c-31a4-83ec-039fae5e0211 | -14.91681 | -46.72264 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9148efcd-4369-3e1b-8615-82b8ed44d29d | -12.29671 | -47.10642 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff27ba31-1119-33f3-be6d-1e2b1f94bbe6 | -13.76956 | -48.24635 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07a5ff16-f13e-3184-8e70-f6d8d9304828 | -7.81018 | -61.34472 | 2025-10-18 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecc0f9dd-ee40-3693-8586-1009dd1d314c | -10.62529 | -48.01782 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a3a8462-7864-3060-a673-e4fbcc3694de | -10.24168 | -44.05711 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a86f2850-1f2b-3cd2-b73e-3225308b9cac | -11.37514 | -44.29056 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41ba09ef-a4d3-3275-84c5-78c0cb47907f | -10.41851 | -47.73944 | 2025-10-18 04:51:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a071aeca-0055-3055-8b98-b76bfc932088 | -15.61115 | -51.93607 | 2025-10-18 04:51:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26bfbb72-732f-3273-8e67-c7c667dacb51 | -10.70407 | -44.56479 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff9b8adc-0792-3857-a9d0-86e7d2acdd76 | -10.25498 | -44.03885 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0afa6129-9e44-34ca-ab51-4b8891628232 | -10.11904 | -44.54608 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4fc9883a-448c-384b-a59f-b9d79ae76053 | -10.62121 | -48.01697 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab0326ec-7ba1-3092-87d0-141d1c4bc555 | -13.04494 | -48.19283 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7250e41-5fc9-39f2-b1b2-f35a7dfb7e99 | -10.12501 | -44.54053 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c2430b0-eac3-37ca-ad89-36f369581062 | -12.60005 | -52.82084 | 2025-10-18 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41845be6-7f31-35f3-adf1-57e80721452d | -13.46248 | -43.76862 | 2025-10-18 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42ff5a68-e405-3a91-be12-801b0b835334 | -11.19869 | -47.82937 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e75ecebf-0c44-33ca-872c-882798000218 | -13.48536 | -47.96145 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 564f7d41-397f-358f-a150-a933dee940f5 | -13.40356 | -48.59041 | 2025-10-18 04:51:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af0bcbee-e2f5-3904-b0e0-0d8fd21fd61f | -10.47892 | -43.43684 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README83.md)
