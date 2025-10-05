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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccd275a0-5df0-3618-ac88-7fb4318faf10 | -10.6572 | -46.3146 | 2025-10-05 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 821bf0a5-0be7-3320-a3dc-dcb653b51512 | -11.8418 | -45.0799 | 2025-10-05 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 856e6591-de7d-3882-bc3d-1521a9cfa618 | -6.4131 | -43.0724 | 2025-10-05 02:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 09c50016-90f7-326c-82d9-b2e37da378b8 | -4.6318 | -43.1816 | 2025-10-05 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 05fb85f5-c132-3d82-b348-f0922e6c883a | -15.928 | -48.822 | 2025-10-05 02:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 229b1bbf-30b7-3c86-850e-d180c9cc200f | -4.6505 | -43.1805 | 2025-10-05 02:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 2c4d734c-3b1c-3695-a103-64a78435729e | -11.8225 | -45.0827 | 2025-10-05 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 4250bf5f-12bb-3f05-8754-8ab9107259db | -15.9084 | -48.8254 | 2025-10-05 02:00:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ace74e0a-115b-375f-9d09-51e23706ece9 | -11.9167 | -46.259 | 2025-10-05 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 1fac7d2b-ad08-3727-ab64-1b19f98a04a3 | -6.1536 | -44.6675 | 2025-10-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 521.4 |
| 76314271-50b7-3b67-981d-4c1036f7ce74 | -4.6505 | -43.1805 | 2025-10-05 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 1da9cfd6-891d-3733-89da-360021064625 | -8.5576 | -46.306 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 29ddee57-bef5-3f28-bdc9-edcc70d0434f | -11.8422 | -45.0567 | 2025-10-05 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| eb6ca3bb-94ed-36d9-a540-82229d0b3524 | -4.6504 | -43.2038 | 2025-10-05 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| fd2f72a5-8e63-347d-8205-ed88ba5de59d | -4.6318 | -43.1816 | 2025-10-05 02:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 80c87266-f142-38fc-abd5-3597cb6b9ac4 | -5.6361 | -43.9258 | 2025-10-05 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 75dc7fcc-5c4c-3af7-8b84-5d58415872d1 | -10.6382 | -46.317 | 2025-10-05 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| d84e4218-bdea-3469-881e-8413c03d01fb | -13.0955 | -47.9099 | 2025-10-05 02:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f83867f8-88c5-36a5-8526-39526eedfe42 | -13.1161 | -43.847 | 2025-10-05 02:10:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ef719fcf-d577-31ca-8c8d-818ee89b73ea | -4.4445 | -43.2397 | 2025-10-05 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 0e7f86a8-1a6a-3ef7-b357-5152ac45615d | -11.8777 | -56.8769 | 2025-10-05 02:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 33c0264e-cb6d-3085-8b0f-d73103198ce2 | -3.6196 | -51.0461 | 2025-10-05 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 28987e7a-43a2-3886-9375-b0a9b01fcc99 | -11.8225 | -45.0827 | 2025-10-05 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| f0dbc85c-c091-3681-93a1-49a03cb4049c | -12.2876 | -49.2101 | 2025-10-05 02:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 4a4715ff-6093-33d5-bc93-8cc7aae9aba9 | -8.5956 | -46.2798 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f07e433a-31ec-385b-9340-8815a6b7a541 | -5.6363 | -43.9027 | 2025-10-05 02:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b1c7e96b-eda7-3d71-a9f7-78743ad641d3 | -13.2745 | -47.5933 | 2025-10-05 02:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 36f35108-9b31-308a-99b3-afe6872719b3 | -3.6197 | -51.0253 | 2025-10-05 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 1f643aa9-0272-31c3-98dd-0fbdef2db24e | -10.6568 | -46.3372 | 2025-10-05 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d30de059-6893-3c85-b0c6-9274c15e8e52 | -6.4134 | -43.0489 | 2025-10-05 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ca410296-a9c1-3b91-a441-3baf508589e2 | -8.5578 | -46.2836 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 3af3dcf8-a1df-3fdd-894e-b78083e3ab44 | -11.8418 | -45.0799 | 2025-10-05 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 206b687b-1828-37d3-a996-348fb1331f0e | -17.9006 | -57.6388 | 2025-10-05 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.3 |
| d7a460b0-aa27-3460-ad49-2be356cb9d07 | -8.5764 | -46.3041 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| d7fcb433-572d-3518-a183-3fc0a586ca4a | -8.5573 | -46.3285 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ea76a1d0-dec8-313a-bb8d-0f10ed139e16 | -8.5761 | -46.3266 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 179.0 |
| e6f1f647-d186-3b56-97e8-c31046996aa0 | -6.4131 | -43.0724 | 2025-10-05 02:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d9e1bff8-9081-3380-9861-f6e50137a93c | -3.6013 | -51.0259 | 2025-10-05 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| c6151755-0a8c-31b0-991d-9b4e7de6be1e | -10.6572 | -46.3146 | 2025-10-05 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 8bd930be-9284-3f66-b51c-f2c373f2b8b6 | -18.3345 | -45.8734 | 2025-10-05 02:10:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f20b2959-8198-3703-b006-474b68762c76 | -11.823 | -45.0596 | 2025-10-05 02:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 55d10fa6-7e14-345d-91c2-eebbc2a1e190 | -18.2565 | -53.3544 | 2025-10-05 02:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3bfedd75-1f68-3f5f-87dd-17a655198102 | -18.237 | -53.336 | 2025-10-05 02:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 6023c1b4-a901-3a7d-b862-d8d2c2bb41a3 | -17.8808 | -57.6412 | 2025-10-05 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.7 |
| c19117b7-1a62-329d-b16f-1690ba1d080b | -15.928 | -48.822 | 2025-10-05 02:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0afb2b63-ade7-39c3-9969-d812563f468f | -3.6012 | -51.0467 | 2025-10-05 02:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 843e89ca-a001-3d2f-a065-a9e162444361 | -14.3353 | -47.6755 | 2025-10-05 02:10:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 28adcf04-379d-327a-b3ae-641693dbe4e0 | -18.2569 | -53.3329 | 2025-10-05 02:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d7f8cae1-b776-3861-a85c-26a844f365e5 | -15.9084 | -48.8254 | 2025-10-05 02:10:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4dbc042c-78b8-3fbb-ae09-930792044daa | -8.5581 | -46.2611 | 2025-10-05 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| e3d9eae3-e3c1-3384-b414-800bf9293e79 | -7.76091 | -73.07088 | 2025-10-05 02:11:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9a47203-50ca-30ab-bc3d-492b6f8eea7c | -8.43658 | -70.11502 | 2025-10-05 02:11:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e684ee94-35c3-393f-8d1d-f42522c8925b | -8.42648 | -70.11656 | 2025-10-05 02:11:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4f392f24-5cbe-3326-a88d-86ceb6206884 | -9.71484 | -67.46965 | 2025-10-05 02:11:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 12691ae0-e80a-34c4-b312-20ae653d9498 | -8.42822 | -70.12839 | 2025-10-05 02:11:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 14f67b41-b2b6-3106-abc6-fc214cb86086 | -10.80452 | -69.04057 | 2025-10-05 02:11:00 | TERRA_M-M | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 27d5aa39-be91-33b0-a0de-5d82a1f52d9c | -8.4383 | -70.12684 | 2025-10-05 02:11:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 739dfa1e-c2ae-3e05-81da-424fbf4fb702 | -8.32578 | -70.19868 | 2025-10-05 02:11:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a7a616e3-79a4-3db6-8cad-19ab4e7027ec | -5.8891 | -42.9048 | 2025-10-05 02:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 59.3 |
| 01cb9b38-ab7b-3b34-9b51-b93d12b1bc7a | -14.3353 | -47.6755 | 2025-10-05 02:20:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 862904f7-c9f0-34c8-b865-c6c1ed75a73f | -3.6196 | -51.0461 | 2025-10-05 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 860e9d4c-970a-3615-a696-6e1b8cd1e98c | -6.4134 | -43.0489 | 2025-10-05 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 77d4fc00-3dd3-384c-9f5b-6ef214307cd8 | -11.8225 | -45.0827 | 2025-10-05 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| bb5e63b7-523b-37e8-ae43-f7dc3fe0b62e | -8.5953 | -46.3022 | 2025-10-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 89cd5e46-480b-3026-a392-6037b0d5a4d2 | -13.1161 | -43.847 | 2025-10-05 02:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4ec4c9c6-ada8-3f8a-97fc-dd20f646cbc7 | -18.237 | -53.336 | 2025-10-05 02:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 102.5 |
| bfb4eb48-478d-3ed6-b774-155c5f4a3a34 | -3.6012 | -51.0467 | 2025-10-05 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d0ed4348-75e0-3ff3-ac3c-d128206f7921 | -4.6504 | -43.2038 | 2025-10-05 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 1d5c0422-d2ea-3f61-9d63-1d6784b489be | -8.5576 | -46.306 | 2025-10-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a1ea0ed5-9ae1-3d69-868b-02820dabc5ac | -8.5581 | -46.2611 | 2025-10-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ed17f79a-e48b-339c-a9be-5799da1e03cb | -13.0955 | -47.9099 | 2025-10-05 02:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 0bb2e6db-282e-34fa-b87d-1814da233b4f | -3.6013 | -51.0259 | 2025-10-05 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 28925c57-55a8-317d-b0ad-511909380c2f | -8.5764 | -46.3041 | 2025-10-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 20975e29-be84-3d52-9e72-4f61c639edc3 | -12.4669 | -45.5155 | 2025-10-05 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| 080de5f7-1e38-38ce-9550-9dd6a6041265 | -4.6505 | -43.1805 | 2025-10-05 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 9e5fe516-692e-329b-9620-081f7ccf7be9 | -11.8422 | -45.0567 | 2025-10-05 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.7 |
| ad28eb7a-d33e-3ee6-8eb1-db4c7d8a0b9a | -17.8808 | -57.6412 | 2025-10-05 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 7bc5c930-a2b1-3275-8de0-ebeb1d58367c | -18.2569 | -53.3329 | 2025-10-05 02:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 20015aa5-e1ea-3324-8632-0049276903fc | -11.823 | -45.0596 | 2025-10-05 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| b631427e-e360-37a8-ad90-83febc9a139c | -8.5761 | -46.3266 | 2025-10-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 265.2 |
| 7ece70f0-c616-38eb-9fc4-d820f0ffab2a | -11.8777 | -56.8769 | 2025-10-05 02:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 6551bc16-8508-322f-9fc2-f380a13d0310 | -5.6361 | -43.9258 | 2025-10-05 02:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 7cda552c-674e-3c84-a320-4748b492908d | -12.4665 | -45.5386 | 2025-10-05 02:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| e33b01da-20a5-3435-89bf-764f5d6db909 | -8.5573 | -46.3285 | 2025-10-05 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 4b9b0354-9fc5-3b47-8362-39a17f305537 | -18.2565 | -53.3544 | 2025-10-05 02:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e15ea454-4194-3526-bbe0-3938b82fb439 | -11.8418 | -45.0799 | 2025-10-05 02:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 245.6 |
| b444662f-279f-3ca4-ba94-ae954c9cdb50 | -3.6197 | -51.0253 | 2025-10-05 02:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| afdc8ac9-f8a6-3903-9d89-3a9c8ab4ead5 | -4.6318 | -43.1816 | 2025-10-05 02:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3800188b-2d54-32b8-a6ce-cc3b22857bb8 | -6.4131 | -43.0724 | 2025-10-05 02:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 25f35e68-0aad-3f5c-b9b7-ad5fa6dd7c14 | -4.4445 | -43.2397 | 2025-10-05 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3d4c7b67-0492-3060-951d-bcb11434887f | -10.345 | -48.176 | 2025-10-05 02:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 2526c660-1166-35a4-814f-7cb3f43f3c6b | -4.6505 | -43.1805 | 2025-10-05 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| d7fb0bbd-1e0d-35a6-9916-5ffac0cb7804 | -14.3353 | -47.6755 | 2025-10-05 02:30:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| ad6ccc6f-2cff-3305-a8c2-c0976a7fdc73 | -4.4445 | -43.2397 | 2025-10-05 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f286f317-2507-3ade-b205-103c14f80294 | -4.6317 | -43.205 | 2025-10-05 02:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 54f7359a-e095-3092-b95d-37fcf638ae95 | -10.6568 | -46.3372 | 2025-10-05 02:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| e1a4f85d-5ce3-3129-8009-45701d069a0c | -11.823 | -45.0596 | 2025-10-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e8983c6c-18ae-3ed0-9252-6cd742a24936 | -3.6012 | -51.0467 | 2025-10-05 02:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| a7c4070b-4bc7-3de6-b7ec-f5c10abfeee1 | -17.8808 | -57.6412 | 2025-10-05 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 7e79fcd1-7298-328f-956a-680450810c00 | -11.8418 | -45.0799 | 2025-10-05 02:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |


[Clique aqui para ver as próximas entradas](README18.md)
