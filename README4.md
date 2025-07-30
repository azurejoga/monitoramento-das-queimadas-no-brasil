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
| eb4ce046-b523-3a51-ba6b-29c8f61c6b1b | -11.5503 | -44.2407 | 2025-07-30 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 7441ddd7-9f59-382c-bdde-b646903ce225 | -18.4 | -49.5826 | 2025-07-30 00:20:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 53.1 |
| f682d6f8-976d-3030-a810-6c0330cdf064 | -4.6696 | -43.1326 | 2025-07-30 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| cc81e57a-acab-36d2-a866-4e6e8ab61f6c | -10.6172 | -45.2282 | 2025-07-30 00:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 5f39d18d-45ee-3d89-924d-9e9ec34bb7b5 | -2.9108 | -48.254 | 2025-07-30 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 84db0c9a-af8d-3c04-8be1-52f3cafaecfc | -11.4584 | -45.1126 | 2025-07-30 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 29892b44-ca97-3de7-a231-b98180d5e58d | -15.7372 | -41.9227 | 2025-07-30 00:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| eacee284-559e-35f5-88b2-69d16f9b6ae2 | -9.1538 | -49.857 | 2025-07-30 00:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4255a46c-5a40-31de-80eb-63fae5d2d5bf | -11.5499 | -44.2641 | 2025-07-30 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| f6ac57f5-ec15-3d3c-9d3c-56d7864fa614 | -8.5211 | -43.3063 | 2025-07-30 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 210d3cf7-45de-349f-961b-436706d3b410 | -11.5307 | -44.267 | 2025-07-30 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 06d5d8ab-c4f6-3134-a0b4-5ee6f6c9915e | -6.6328 | -59.9841 | 2025-07-30 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 67801e86-a42c-3b43-aeaa-09691bd2cc2b | -7.8568 | -46.7304 | 2025-07-30 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 098cf830-f9bc-3ca0-8e53-bb6dc2eca27c | -15.718 | -41.9023 | 2025-07-30 00:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.4 |
| ff97deca-f242-30cb-85eb-7002e4215539 | -18.38 | -49.5864 | 2025-07-30 00:20:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| da935ad7-c065-3c1f-aecd-cab58570a69c | -15.6969 | -41.9566 | 2025-07-30 00:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.9 |
| 95c06b7d-3220-38c6-a836-258d4b7e39cf | -2.9109 | -48.2325 | 2025-07-30 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9eebddec-e301-3105-b242-967b295c55f5 | -15.7167 | -41.9521 | 2025-07-30 00:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.0 |
| 9a409334-5288-38be-b90f-e553eb897b2b | -11.4776 | -45.1099 | 2025-07-30 00:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 33fb8149-d665-351d-b4b7-5bb7e236c81a | -4.6511 | -43.1104 | 2025-07-30 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 6c7a1db3-13e5-3f99-8c98-d28aa5cdffed | -11.5311 | -44.2436 | 2025-07-30 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 841acd15-776f-3483-8a82-edcf87a8e540 | -9.154 | -49.8356 | 2025-07-30 00:20:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 138ba69c-3727-3728-a642-26522aed9331 | -4.6509 | -43.1337 | 2025-07-30 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d36fc451-929f-363e-8c13-39d301f24ac3 | -15.7174 | -41.9272 | 2025-07-30 00:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 429.6 |
| b8533db9-3b9e-3035-9191-46f37110fec8 | -15.6975 | -41.9317 | 2025-07-30 00:20:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.3 |
| 08fda6a7-32e0-370b-8eef-ecaf5e8e532c | -2.9109 | -48.2325 | 2025-07-30 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9fbb63d9-cd22-326c-ba3f-3cd3805563bf | -15.718 | -41.9023 | 2025-07-30 00:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 52.2 |
| bea75b7d-e212-30ac-92b1-1b82bb55c2bd | -15.7174 | -41.9272 | 2025-07-30 00:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 444.5 |
| b25c60ba-905c-3b56-a07c-f6a589b33c9c | -15.7372 | -41.9227 | 2025-07-30 00:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| d4ddc849-269a-3beb-9a90-21e8619ec563 | -11.5503 | -44.2407 | 2025-07-30 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 036cbad0-89a5-324a-84a4-307e2439ba13 | -10.6169 | -45.2512 | 2025-07-30 00:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 31526151-240e-37c4-b362-e2d652e247c1 | -2.9108 | -48.254 | 2025-07-30 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b06726c5-8031-3687-9911-e78d365e872c | -4.6509 | -43.1337 | 2025-07-30 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| db9986b0-a524-34ba-8f44-f300aa9cf843 | -8.5211 | -43.3063 | 2025-07-30 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4af4902a-9649-3d2c-98b1-724c55046011 | -9.1538 | -49.857 | 2025-07-30 00:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| c00917e9-6899-3d32-8728-02212d1b43da | -10.6172 | -45.2282 | 2025-07-30 00:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| c8bd2ea7-ac54-38ab-957a-377e2a0cca00 | -15.7167 | -41.9521 | 2025-07-30 00:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 163.5 |
| 38555ccc-2487-3fb4-a246-3c6d6889bdb1 | -9.4387 | -40.3419 | 2025-07-30 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.9 |
| e4dae175-6f15-3c81-bf57-ae97effae2b7 | -15.6975 | -41.9317 | 2025-07-30 00:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.0 |
| 1999ef95-5e1d-33c7-98f0-f4565c50253b | -9.154 | -49.8356 | 2025-07-30 00:30:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1d5798d6-2c91-3db1-9309-bb961668d66b | -4.6511 | -43.1104 | 2025-07-30 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 8a7e3843-4c63-3b6f-a610-82b98659c117 | -9.4383 | -40.3668 | 2025-07-30 00:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 1a92430f-3b10-36b2-9c95-59d601789282 | -15.6969 | -41.9566 | 2025-07-30 00:30:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.3 |
| 026d3fe4-5d5f-3edb-a8a1-436d9781e9ee | -11.4776 | -45.1099 | 2025-07-30 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 314489c1-23a1-39d8-997d-1a834267f931 | -11.4584 | -45.1126 | 2025-07-30 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| ca3feb5e-f5f8-3fb9-85a1-9874a8eb9ad5 | -7.8568 | -46.7304 | 2025-07-30 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 8a020dbf-c47c-3e10-9ff1-53fd18d31db8 | -7.8568 | -46.7304 | 2025-07-30 00:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 4d984500-b6d0-3018-9135-33924ae0d109 | -11.4584 | -45.1126 | 2025-07-30 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| fac778f7-bdcf-3af8-925c-343a0551c4db | -10.6172 | -45.2282 | 2025-07-30 00:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 12957629-6185-3add-afae-a498d766f575 | -15.7372 | -41.9227 | 2025-07-30 00:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| 69d2ba8d-f83d-3116-8dab-0e64f216ebfc | -15.7174 | -41.9272 | 2025-07-30 00:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 328.9 |
| 4db6c57e-eb1c-3c65-b594-485c80b9c5e5 | -4.6509 | -43.1337 | 2025-07-30 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| bb3704f7-f3d5-3f53-9fca-3a3aa4e782f0 | -4.6511 | -43.1104 | 2025-07-30 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d76a19f1-ce87-3db4-8897-1cdb41aa67d9 | -9.1538 | -49.857 | 2025-07-30 00:40:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| fc71a42b-7681-3cc4-8da3-2a9b5434ff4b | -2.9108 | -48.254 | 2025-07-30 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| da5e25ac-d4be-33e1-a5ed-7739cbb715eb | -10.6169 | -45.2512 | 2025-07-30 00:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4c3e9490-51d2-3b7f-bebf-91cbf8b38b8e | -11.4776 | -45.1099 | 2025-07-30 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 62b95aac-2330-36ca-af30-4594133adda6 | -15.7167 | -41.9521 | 2025-07-30 00:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.5 |
| b12ef5bd-02ea-3f75-8e2e-131acbf1013e | -15.71196 | -41.94001 | 2025-07-30 00:43:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 199.8 |
| d7636f85-aa6d-3b07-924a-ee6b51a363b8 | -17.48425 | -46.73193 | 2025-07-30 00:43:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 7ed97964-3e32-3a40-af0a-27afd15008c1 | -18.56494 | -44.42271 | 2025-07-30 00:43:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b59ed401-038c-34d0-a6fa-7ede2cdcaafa | -21.32162 | -48.69128 | 2025-07-30 00:43:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 2f28b452-68c0-3a3e-8372-2a9a6cc18fbf | -17.48584 | -46.74245 | 2025-07-30 00:43:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3de074a8-0298-37e0-a1ec-4a836ac0f4a6 | -17.95415 | -50.38865 | 2025-07-30 00:43:00 | TERRA_M-M | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 94ccb8fe-19da-3d6b-92ba-c9374db841f9 | -15.71818 | -41.93217 | 2025-07-30 00:43:00 | TERRA_M-M | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 168.1 |
| 0c192f60-b76e-3df6-9357-b14f1d2db505 | -18.37967 | -49.58505 | 2025-07-30 00:43:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| c224c796-3aa6-3aa7-aa1c-57d97ff6f680 | -20.29495 | -50.96134 | 2025-07-30 00:43:00 | TERRA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 3ceed9b4-e29c-3f93-a254-96fe1d40817a | -17.08062 | -49.83667 | 2025-07-30 00:43:00 | TERRA_M-M | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cd3a4910-3bd3-3930-b115-0bde69dba7aa | -17.05058 | -43.78237 | 2025-07-30 00:43:00 | TERRA_M-M | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 532f5dd6-b10b-3f73-8343-d6ba3be0a710 | -21.32291 | -48.70082 | 2025-07-30 00:43:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 07cc9401-b833-3430-8930-d1a1afb4c5f0 | -18.77805 | -47.62519 | 2025-07-30 00:43:00 | TERRA_M-M | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d6a55b00-d77d-3dc0-99ef-13456278cac4 | -18.56156 | -44.42974 | 2025-07-30 00:43:00 | TERRA_M-M | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dfcdc8c9-edf2-32d7-ab9a-ca62a5ed2d88 | -18.38095 | -49.5945 | 2025-07-30 00:43:00 | TERRA_M-M | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| e79a2aa3-df4b-313d-8969-0fa521c4d885 | -12.48531 | -47.28072 | 2025-07-30 00:45:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4185879b-d874-3d8b-846e-5aa99850ecf4 | -11.81475 | -44.26696 | 2025-07-30 00:45:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 28731ef8-6036-3409-8bd7-dd02677f030a | -12.81156 | -45.43573 | 2025-07-30 00:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c5fa2e69-d1e2-32db-824c-3dfaf669260a | -12.81055 | -45.44232 | 2025-07-30 00:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| add289ca-fd6b-3279-8d66-4986b054bc66 | -12.4756 | -47.28227 | 2025-07-30 00:45:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| d9822310-91e7-3514-a283-bd8c14580f98 | -11.80906 | -44.25479 | 2025-07-30 00:45:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 22d498ac-7a4e-3575-983e-4ef5605a7ba8 | -14.74367 | -46.3006 | 2025-07-30 00:45:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 931d625b-dfc5-3f61-b04c-3df1b5cad282 | -12.48364 | -47.26964 | 2025-07-30 00:45:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b1256775-a588-3bd0-8a3b-051eeb1c80f9 | -11.92389 | -44.55818 | 2025-07-30 00:45:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 5519b201-6beb-39fe-bbde-afc1ed4a1ae1 | -12.46658 | -44.07767 | 2025-07-30 00:45:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| af68144c-8c93-342f-ba02-0c41b88a60a9 | -15.59053 | -47.88947 | 2025-07-30 00:45:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2ad30212-3b22-393d-ac90-3707438c5b0c | -12.57473 | -49.79924 | 2025-07-30 00:45:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3771c348-544f-3543-a489-ceef9164629f | -12.81387 | -45.45005 | 2025-07-30 00:45:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 404f8c1e-86bc-36ad-8061-7e95d714450a | -13.54612 | -44.14593 | 2025-07-30 00:45:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 29fe8087-d719-3ab8-b180-70f0b62a3a61 | -12.47392 | -47.27119 | 2025-07-30 00:45:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| febfc250-e764-395d-8f9c-9afb9059e690 | -12.46956 | -44.09601 | 2025-07-30 00:45:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 7316e359-92e1-3f94-aeb7-21288704c748 | -13.08354 | -47.31728 | 2025-07-30 00:45:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5c06ed8e-90e6-31e6-8c36-64692a482d44 | -11.81193 | -44.27309 | 2025-07-30 00:45:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 631b915c-9168-3438-9886-c6509bba5e6e | -12.58359 | -49.79792 | 2025-07-30 00:45:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 78a65f15-22c2-384f-83ef-93f574e62524 | -11.92116 | -44.5409 | 2025-07-30 00:45:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 60131c5b-080f-38d6-a1c0-788e042a4f59 | -11.81174 | -44.24869 | 2025-07-30 00:45:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bbfe5d80-e2d8-3ba1-b1d2-5fa0f0de4653 | -13.06432 | -47.38625 | 2025-07-30 00:45:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1fbe77a3-821a-3731-82b4-0c7e20ed1e59 | -11.926 | -44.53343 | 2025-07-30 00:45:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fcf1c3ef-ab15-3d14-914d-84e06b5511f2 | -11.92886 | -44.55072 | 2025-07-30 00:45:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 12bae214-0ec3-3267-8f54-b8e5ed7ba1fe | -11.98728 | -46.6944 | 2025-07-30 00:45:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 24747ae2-00f9-3bc2-a6c0-3d4591a960a2 | -12.73069 | -47.00661 | 2025-07-30 00:45:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3e0cb067-c5bf-3761-8bf0-aba3f32f4908 | -13.09163 | -47.30545 | 2025-07-30 00:45:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README5.md)
