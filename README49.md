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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ccbebbb-df5a-392c-a372-00280d519b55 | -11.8027 | -44.91578 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e96cd8fa-19e9-3800-8b9a-1f4fbf785676 | -13.97086 | -44.42314 | 2025-09-29 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89064f92-4694-3ef6-8656-77db8ae0a848 | -15.58547 | -41.81179 | 2025-09-29 04:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e0731ff3-cdc2-3b21-83e8-5efde1f6c4ee | -15.61287 | -46.25047 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e036688-c74b-33ea-a6f9-14f22bb4f41c | -8.66343 | -49.43411 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a519acc5-40d9-33ca-830c-70f81f7931fe | -10.53854 | -43.63876 | 2025-09-29 04:08:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f829321-0ba1-32c0-8ce3-291d63a0cc7d | -11.69226 | -44.43451 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c2536bc9-1301-3571-ad2f-663e3ce92072 | -15.25487 | -48.75855 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75cb08d0-270d-323d-b38f-4809979ec772 | -11.66078 | -45.33377 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb5105d9-60bb-3fa9-808d-51aedaca4736 | -10.80297 | -45.36576 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ecc66a70-f8b0-3135-821e-8e656bc6ad8e | -13.78846 | -47.8763 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd4a9d71-c4a9-34b5-8529-c70cb97fa822 | -9.99429 | -45.41623 | 2025-09-29 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b5bd00c9-88bf-3c19-8014-7600928194d8 | -13.71974 | -48.65646 | 2025-09-29 04:08:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4fcba51-993f-3657-8c6f-ffb21709ac70 | -13.79311 | -47.87292 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b77970c-f4c2-37b5-b0c7-caf72f064dc3 | -9.05157 | -46.72045 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb024d7-3344-3fd2-92ea-022841d952ed | -9.31172 | -45.7137 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4fd49bcd-f23c-3060-b4db-497a46bb9c93 | -13.16395 | -47.41316 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a528a9c5-7a72-364a-9f99-30d9a12c3713 | -11.81837 | -51.793 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c5411606-ab0f-3b2b-9b87-f74a4fcd4ceb | -12.01743 | -47.7912 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 77466d74-cba5-3cae-995c-f993b14781e0 | -15.28144 | -49.25492 | 2025-09-29 04:08:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92e4d580-1198-304d-9524-4ddc0dac0467 | -13.38046 | -48.14977 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 36d6d4fd-f8e4-3045-a8a1-d3de30e737a8 | -15.90502 | -46.24102 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 791b26e1-393b-3189-925b-b53421f57032 | -13.35349 | -47.30043 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1b85e1-2908-3e79-84ad-0ef76781ce8a | -10.83087 | -45.39594 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f6ddb54-2b37-31cf-bbde-d8fd519c2c97 | -15.0408 | -46.96283 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2714f570-de86-3cf4-9058-7346eb9b95ff | -12.57819 | -41.29224 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e52c4403-0f44-3b32-a812-2639d112754b | -12.17505 | -43.56604 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2b4275b2-567d-39d7-b300-51bfb78b1fcb | -8.88587 | -45.03247 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4c5d4e1-476b-318e-9954-fb137c27a46a | -11.4447 | -44.97726 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5ed1128-89d9-3f76-8104-1495a3541cd1 | -15.41441 | -48.23211 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33573c5c-394e-3a4d-a1c1-6c8adb5d470b | -9.7735 | -46.18153 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57712d05-030c-35d5-ac17-ef83d65b8c02 | -10.39063 | -48.15487 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee93cd58-66df-3260-a3ce-50a0cbd15628 | -8.71698 | -50.04341 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2448803c-074a-36d0-b001-de6bbf80168d | -13.6367 | -47.3229 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b4683556-4e4c-3405-9ec5-4f87a3048c68 | -13.49109 | -47.40688 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d5d7a2d-006e-3b6a-a3e1-8a6ce7b00075 | -15.4186 | -44.99042 | 2025-09-29 04:08:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d38075e-a5ed-37b5-9865-6c2abb9bd279 | -15.5339 | -47.87792 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 248a36ff-5fd0-3143-a5f6-db2828ee400a | -15.50496 | -45.88495 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| baeb3c2a-9e44-3387-80a5-56b54572fac2 | -15.28584 | -49.51283 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0fe22aa9-0bfc-3a1f-bf73-308f1e06d321 | -12.03261 | -47.91619 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5106798-db89-35ad-95f0-8023786004ab | -12.89571 | -47.09624 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2244858-d91d-3088-af5a-33992f97445d | -9.34883 | -47.62963 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa9f97a2-4e24-36a4-bc67-59d675cc02e1 | -14.78902 | -45.73831 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8537afc0-a0f7-36af-b018-d33f46c799ca | -10.79393 | -46.68595 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88b0d871-0d7b-3246-9b4e-1b1aeccc90ad | -11.66933 | -44.2969 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5dd7042-2ca8-349a-ace6-7acd51091c40 | -10.26613 | -48.07162 | 2025-09-29 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 582e59a1-af5e-334a-ad30-960539005337 | -13.77133 | -47.85886 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5734824-ee01-3857-860d-32b0373896c5 | -11.86109 | -48.24661 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 094ded31-7f87-3ee2-b904-51f4529c58a2 | -11.79988 | -48.24353 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d1e8ae5-2840-3b54-ba9f-9ded22b76705 | -13.39783 | -47.92422 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5d28835-5f16-306a-bf14-d3dac1ff1df7 | -10.28695 | -45.19893 | 2025-09-29 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c36312b7-a784-3f6b-93e2-6c8edf7db184 | -15.87409 | -46.83773 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f86e6b3c-309e-3d16-95af-26b7932c6635 | -10.19331 | -46.91751 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb57cb04-ce50-340f-8885-0c6d3bf88d4f | -9.4664 | -45.5033 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3415ff34-fbdd-3671-b538-d714c6a8d73a | -15.32526 | -47.9159 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ab81f63-e67e-3eba-a54a-85a683f5a28e | -11.71299 | -44.43742 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d98396f-0867-38cf-8a33-fb2bd275fe5c | -10.08147 | -45.63576 | 2025-09-29 04:08:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5324165-7f9e-3209-8f0b-d859a0d8751e | -13.83722 | -47.48733 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00017e56-7d0a-3593-b103-fe8b7f999a4c | -14.57731 | -48.26733 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5be3dc81-ad39-3dc9-a1d6-b6c61db5a712 | -11.94241 | -46.53904 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a638a1a-e93c-3872-bf94-8b81c7475fc5 | -8.71226 | -47.98688 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5682001a-929e-3cb3-a75c-44cf8b2c07ea | -13.38722 | -48.15828 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| e72aeef6-f450-31c9-b022-744237628161 | -14.47596 | -48.57444 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7ad7e7a-3bff-3957-8bf7-583939d1baf4 | -11.80469 | -48.24042 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add62738-e96e-3131-a4bb-1d403b444dd5 | -9.77406 | -46.20269 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09965ef4-0637-37fe-844f-1695b82209e2 | -12.76341 | -46.84855 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2dc56553-9902-3840-a6d0-bb14c411928e | -13.33249 | -47.28547 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 234a35c9-e065-3ebf-91b2-b55471d93c9c | -13.38786 | -48.15473 | 2025-09-29 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0ee2022e-bbc2-34cc-a780-30a0540023f7 | -9.31369 | -45.7159 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29bc0243-ba3e-3363-9e0f-ed3aec212bee | -12.92407 | -47.15404 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7e7a23aa-77f5-3681-94cb-b28c17304646 | -10.76127 | -45.38039 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65b8af95-6c29-324b-adbb-4a524f8fa924 | -9.05246 | -46.71533 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a41414f2-bc54-3e1b-9ff8-6915ca043c2e | -10.94671 | -44.31592 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbb6b636-baf8-3865-b759-e7e1ab8708f7 | -13.01535 | -49.45422 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 022e5064-6054-3b49-bf06-38dd421e3574 | -11.82528 | -51.78659 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 093fe072-39c9-36c6-8e4c-a43c0f0abc68 | -14.54683 | -48.41368 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c412699-7a88-32dd-b4be-faf0137c41a9 | -13.57584 | -47.29581 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5dda264f-aa23-3649-985d-8f2f7c34220a | -10.05165 | -50.19739 | 2025-09-29 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e93bf049-7404-33ef-b5cb-6698ded26d76 | -13.8105 | -47.93546 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6885e6fa-7615-37d1-8798-38eaa2789f85 | -11.65636 | -47.48915 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22d98a5a-6882-3fac-ab56-c02ebce82178 | -15.32614 | -47.91093 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3419ae1b-3130-39d9-8ec2-dabe3c3b78c4 | -15.70604 | -47.80398 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 859778a3-45be-322c-827d-f87d7bdf76b4 | -10.48258 | -49.37366 | 2025-09-29 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfa92b16-83f3-3366-887e-7a9720814f62 | -10.82886 | -45.4079 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 822c27ad-ea18-3e92-b72d-9b7c8f90d2bf | -14.53353 | -48.44142 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 801de09a-3e1b-34b6-b0f7-6097f921a27f | -15.90153 | -46.24033 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b67979db-9099-3e08-bd8f-63a7f363b3ef | -13.75141 | -47.90231 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45c23f7b-9d25-36d4-88e3-1adf276ceecc | -11.5058 | -43.54705 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2112e80-61c5-34a7-a250-c0d1ed6368ec | -9.75332 | -47.80122 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05856848-34b2-36c4-bb9f-c8c7d2e148b6 | -12.86394 | -45.16279 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac935748-dfdc-3d09-bae1-37bcfb2faf11 | -14.54488 | -48.42448 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5507623-2f92-303b-8f0c-d357ea43ce75 | -13.58511 | -47.28756 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ab14156-98b0-37b1-a473-a22bb2df3bd0 | -13.79937 | -47.95247 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18da1d9a-215c-37ae-a02d-4388f76220f1 | -13.83772 | -47.93806 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f814a041-812a-3a3a-a9b3-7688aa28cda7 | -8.43361 | -46.87995 | 2025-09-29 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc1d2c34-4bcf-3944-a2df-01571cb8740b | -14.56655 | -48.28158 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6a0768a-986e-3eba-a318-1e0a4547f58f | -11.45607 | -44.99494 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2340a39-ad44-335c-bc85-d5f11e1d4d3e | -13.75039 | -47.90799 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b80de4a-e9e2-365f-8040-db020b6d3e1b | -11.36031 | -45.06852 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9d91eeb4-f55e-3d59-833c-990c717d10e0 | -13.01192 | -49.44801 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README50.md)
