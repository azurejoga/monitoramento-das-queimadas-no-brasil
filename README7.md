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
| f9b4044a-b382-37d1-852a-255552dfe733 | -5.7978 | -57.723499 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ebe732a-b067-3fac-8a7f-9099d3a80c8c | -8.0753 | -54.852001 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c890d2b-31d0-3087-8904-84716afef3bd | -8.6354 | -66.486397 | 2026-09-12 01:26:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d48ca0c3-aeac-36d5-ae55-3395d7a00c8c | -13.2646 | -61.604801 | 2026-09-12 01:26:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7b09495-1411-3dde-ad52-8ad09363f024 | -6.2794 | -59.9296 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd8ebe62-252d-3e73-bcab-1cdf1581799f | -6.1222 | -55.652302 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2beaba77-719f-3826-a23b-25e9d05b45c2 | -7.0292 | -55.3918 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9dd22bc7-71f3-3e2f-a2b2-ada41d71da97 | -3.3588 | -59.434101 | 2026-09-12 01:26:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7bc85c2-5fcb-3e5d-82e1-9cc7225b67fd | -3.3473 | -59.428902 | 2026-09-12 01:26:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99b2fe37-cda3-3983-b8e1-29f2def94de5 | -2.9429 | -50.372002 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 334e9958-556f-3f20-a7a7-6d06bcf754a2 | -6.0767 | -53.5042 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9535d397-8924-36be-af84-c52d5e050372 | -8.5853 | -54.572701 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 045483b0-f0ad-3271-ad87-2af54235b4a0 | -4.8657 | -56.003399 | 2026-09-12 01:26:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 962c50c2-464c-3e7e-9442-369c27493669 | -10.6851 | -54.162399 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 118eef1c-d5cf-36d5-b737-a67577285775 | -5.796 | -53.8307 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6a379b2-dc19-38b4-96d0-135c278a27a1 | -9.6354 | -49.669601 | 2026-09-12 01:26:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45fa61bd-44e8-3af6-93ec-e6da2993ec9a | -9.4665 | -67.097298 | 2026-09-12 01:26:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f33b9e89-fc04-349d-9182-f95761c65a81 | -5.8184 | -53.795502 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfad7c9-9480-376e-8b29-3d199e038783 | -5.8281 | -53.793098 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8ddbee6e-56db-3f5d-962f-e23866e25a2b | -14.5928 | -52.6544 | 2026-09-12 01:26:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0757b39f-bc9c-3a39-a95c-9479d2ab9f6c | -9.7104 | -64.960098 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 81f6bde4-8f7e-3ab0-951c-842bb599c421 | -2.9525 | -50.369598 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51ef70a7-f0d9-30be-b80f-ed119dd4a3b0 | -9.6511 | -49.690498 | 2026-09-12 01:26:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4710f4a3-ca8d-3e7a-8ddd-935a81bff4ab | -3.8924 | -55.809101 | 2026-09-12 01:26:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2ff2c2-e7a6-31b5-9b4a-96324a0df0cd | -6.1829 | -57.737301 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76684bf7-71f0-3a1a-b3d9-d659c648c342 | -6.1772 | -57.713001 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abccacca-02e3-3c80-9070-73497952ace5 | -6.0983 | -59.904999 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eafbf264-d1f0-36b8-8556-ee164ec10c2f | -13.2436 | -49.582802 | 2026-09-12 01:26:00 | METOP-C | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec1f7090-f899-38a7-8772-d8c5aef216d2 | -6.3352 | -55.293301 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6184d0c6-368c-3b74-9124-45e1eb14309d | -8.5825 | -54.561298 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4577e2ad-a5a2-3a68-8c23-e927cc047c56 | -6.6057 | -58.841499 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6ef9a6b-a609-3dce-a5c7-661d3ca6bac2 | -5.8121 | -53.811901 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee5d0ef0-37af-3a02-b642-51ddfe830471 | -8.5032 | -50.1404 | 2026-09-12 01:26:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e305a05a-bdcd-39e1-8418-e2bb5185adf3 | -14.58 | -52.6446 | 2026-09-12 01:26:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 937f15cb-c8df-34c4-b568-0ea8be8a5860 | -10.6976 | -54.1712 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32ae17c8-73a1-38fd-b986-05a5af64ce51 | -2.7346 | -57.634399 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db5bb1b8-9eda-3070-a1ac-41527b087677 | -6.1163 | -59.8937 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4081ec5-a20b-391e-ba2d-db1d49ddaccc | -8.1131 | -54.795399 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2cf4b221-a36d-31f1-8713-fa4fc464db45 | -2.9464 | -50.428398 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7fc1cd-39ce-35e4-bff1-776afcb66101 | -2.9753 | -50.421398 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f638e35-ff17-324a-8d0a-5976553c3ec3 | -6.2838 | -56.026402 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f48ce865-107e-3440-9024-8d4884b9a3a6 | -4.3006 | -49.109501 | 2026-09-12 01:26:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8ef431b-7050-3aaa-8b6c-85d2b44d901e | -14.5831 | -52.657001 | 2026-09-12 01:26:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8f610b4-acdd-3e02-8b71-8a6106404fbf | -6.4269 | -56.1077 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 800bb123-0e43-3311-a90c-b4eda6f11e58 | -5.8023 | -53.814301 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2437a25-2eee-33aa-8fd4-10fba37305e5 | -12.1278 | -48.966499 | 2026-09-12 01:26:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a875094-258b-3d3f-b7db-23556befb74d | -9.1817 | -59.451199 | 2026-09-12 01:26:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57ee3d9e-218e-3162-a99b-0d88f433c63f | -5.9735 | -57.7686 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60047fc-f842-30b3-bb76-4c2a2c712fdb | -6.2876 | -59.920502 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1dbbcf4b-4185-3227-b072-511b8512988b | -13.3491 | -51.638401 | 2026-09-12 01:26:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 024523e7-8758-344c-a392-50ed4db3716f | -3.3693 | -57.703602 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cb92bdf-1338-37d6-976d-55b851b410e6 | -4.8294 | -55.764301 | 2026-09-12 01:26:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fedbbb68-8f7b-3ece-8847-da816cf6646a | -6.202 | -55.254398 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb784ea-9f05-324f-b683-fcf6eda6993d | -5.1002 | -56.1231 | 2026-09-12 01:26:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 400c61d9-e8d7-3c6a-896d-d8376bcd61d1 | -6.1576 | -57.717499 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1459df8e-4d2b-3684-b773-fd2061d90f52 | -6.3475 | -55.301998 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1318d928-aeaa-3848-b133-1fea3e43c943 | -6.2234 | -51.682098 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a53a431e-eb0b-3659-910f-d22714c03039 | -2.7186 | -57.609798 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ba851fb0-6b06-35ee-b04a-7b5b8d554acf | -6.771 | -59.421501 | 2026-09-12 01:26:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb5e9917-1564-36de-ace7-09c680701d70 | -11.2358 | -54.131599 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb918f84-7085-3eed-a211-3b91c4573167 | -8.5756 | -54.5751 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 234e42d4-a0e4-32dc-8a91-0efbfca87416 | -6.1196 | -55.641701 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5dff1b-1152-33a6-88bf-fe08b8f49fc3 | -2.7248 | -57.6367 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66898640-0b61-322e-aa6f-e2e5ca811a67 | -3.7371 | -61.7528 | 2026-09-12 01:26:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e017a8c4-8aa3-3ca3-95e2-091b10df4680 | -13.3452 | -51.623402 | 2026-09-12 01:26:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb1969cb-18ca-3a6e-acd8-994421a7fb5b | -6.887 | -55.658501 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 964fb215-f777-3a07-ab22-27afafa49eb3 | -5.9716 | -57.760502 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58ea6e51-76e5-36ab-a41a-07e2840d9730 | -2.9398 | -50.401402 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5fd6a9e-7463-3451-ad9f-f60d9c02a14c | -14.5936 | -48.8339 | 2026-09-12 01:26:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 16dd2657-63cf-30ca-9f46-6a2b25e53894 | -6.0676 | -57.729801 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f86429fe-5366-3e5e-bca3-bb1f738cc858 | -5.7958 | -57.715302 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8435db-4e8f-3b1b-8797-3428f15eaffb | -9.7081 | -64.949501 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 260189c0-5764-3f77-8828-aa059466bc7e | -2.7269 | -57.645599 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 760fb563-4084-3c85-99d9-6ad3373e707c | -9.6415 | -49.693001 | 2026-09-12 01:26:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0135213d-d0a9-335a-9fe1-348dc207f5b8 | -9.7375 | -64.943298 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1ae4def8-c968-3c06-a7c3-15b35e8c3d52 | -2.9657 | -50.423698 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 324050a6-d09e-3744-ba1c-823284c14909 | -15.2333 | -55.464699 | 2026-09-12 01:26:00 | METOP-C | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 83468110-0ea7-34c7-871a-0fe62fa3534a | -6.2892 | -59.927399 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c809496-9386-3d2e-b225-a54ba78c5016 | -13.2663 | -61.612598 | 2026-09-12 01:26:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3fa0de5-5b89-35f0-8258-e16585badbc4 | -6.2282 | -51.7015 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d9c1cc-8367-3376-9fb8-3957094373b7 | -6.1753 | -57.7048 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8765e83b-04a1-3f56-9439-d47f65da9d61 | -2.9687 | -50.394402 | 2026-09-12 01:26:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0e5372-c2ee-37c7-97d8-2581bda4385e | -6.6041 | -58.834301 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 47c316bc-1255-34d2-b387-e9402472b740 | -9.7029 | -64.972801 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e3a97ee8-55c7-3e67-b439-a1ddb068cf65 | -15.9844 | -52.705299 | 2026-09-12 01:26:00 | METOP-C | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7929f3f5-1fd5-35e2-a73d-57bf844514a0 | -6.0634 | -53.491901 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c426bb69-1fed-34d3-a538-1b9d8d949e65 | -12.1513 | -64.128601 | 2026-09-12 01:26:00 | METOP-C | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 63f01e77-8266-3da3-a947-6353ed3e45e4 | -11.2482 | -54.140301 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8d269f-ad74-3066-a400-b416fee0828a | -2.7228 | -57.627701 | 2026-09-12 01:26:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5577ae5-2385-3b37-a7d2-796a18d9712b | -8.6382 | -66.499199 | 2026-09-12 01:26:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce5839b6-f8b2-3ff5-80c1-d83974716bd3 | -6.1125 | -55.654701 | 2026-09-12 01:26:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2d3059-cb8c-3a74-986e-108893ee1a19 | -6.1065 | -59.895901 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b2587a0-01f5-378e-bc88-12186d82398b | -6.1081 | -59.902802 | 2026-09-12 01:26:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2fbd28b2-a011-3eab-9cae-87f806737042 | -4.3103 | -49.107201 | 2026-09-12 01:26:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5650ce45-1576-3d12-8db0-a9e0f33f1be3 | -2.7148 | -57.6469 | 2026-09-12 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f38b7356-c23c-38df-90ae-f9008a329f8e | -9.1613 | -68.2383 | 2026-09-12 01:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 395e19e2-4ffc-30a4-b52e-5b8c702df945 | -14.5912 | -52.6673 | 2026-09-12 01:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 85c3b87c-802b-39bf-8ade-2d600911e4d5 | -6.6021 | -58.849 | 2026-09-12 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f49fbdaf-00d6-32da-92e7-30f9730bb797 | -9.7319 | -64.9631 | 2026-09-12 01:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 97bafa50-fd5a-3ba7-8668-a7eea99b0efa | -6.2429 | -51.6939 | 2026-09-12 01:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |


[Clique aqui para ver as próximas entradas](README8.md)
