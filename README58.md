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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| faa427bd-cd3c-3800-95da-d9448eaecaa2 | -15.92019 | -59.26968 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d85df4ee-4450-3aa4-8257-77fe43b60969 | -16.9378 | -57.62693 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| fe86ef07-a891-3b89-9cd4-b64185fa97f5 | -17.23331 | -57.45517 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| b6ee9ebf-1e6c-359b-8326-15d7b7c433db | -16.01553 | -59.36942 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 61d306e3-621d-3c91-8c47-dd7ffc83cdcf | -11.88414 | -62.97999 | 2024-11-16 05:46:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dffaa88-24e8-3659-a2b5-986c7f3da309 | -17.56513 | -57.42946 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e21e48b6-9c71-38eb-8679-f498de921e30 | -17.55563 | -57.52512 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3a7eb297-2a8c-31cd-913e-ae81bded905f | -17.57929 | -57.57793 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| eb220268-723f-3b8b-84e4-59b976d8b62f | -17.26075 | -57.47106 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| a4338fa7-03fc-37d3-ad9f-e401078cf8d1 | -17.23845 | -57.44651 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| e79d6edc-6c60-314d-9066-0caeb7b6bcc3 | -17.58485 | -57.4657 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2320546c-14c8-3458-b34e-09c26d3e9727 | -16.04287 | -60.1208 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 60c5aef1-383c-3416-b3fc-2988e0bdaa05 | -16.95874 | -57.6456 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 48c4bde0-1f80-3561-80dc-ba1a9f7c2540 | -17.68739 | -57.5585 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.3 |
| a143cbee-c59a-3a53-85d9-85e31efbc2f8 | -16.94387 | -57.62365 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a53979bb-20c0-36ec-945d-c71579fba454 | -16.10036 | -60.09283 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 09fd02ce-afac-33ad-bb68-bbc1a2d1151a | -17.59679 | -57.4629 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b642b477-1ffb-3bb0-95c3-25e08dd0d972 | -17.6448 | -57.56083 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 83efd133-be6d-3d13-ad67-ad8e5a21146f | -16.08074 | -60.09551 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22457b05-6ae4-3f78-886f-c16268eec558 | -17.64037 | -57.54781 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| b7802721-0084-39ff-839b-9549738208a9 | -16.09974 | -60.0981 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fdeb7f35-ad32-36e3-a298-6cd7264cfbc8 | -16.94345 | -57.62762 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| d74f4fd8-b090-330e-a182-83d23eb97071 | -17.64153 | -57.55294 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 1fab5bc6-8361-301d-a421-6cc8d62bf22c | -17.59645 | -57.57996 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 9195b890-4416-3ba2-9449-4e0875e181fb | -15.91012 | -59.26878 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d7637ca-7d22-36ef-b181-cebb0fa74c47 | -17.62313 | -57.56319 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 274aff21-412f-36bf-8d6d-ba3657c86837 | -17.63206 | -57.57176 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| dce19d04-bb6f-3147-a99d-d3409b7ec85a | -16.84365 | -57.00443 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0748f8d8-85e6-33b7-90eb-43d7ac558062 | -15.91983 | -59.27281 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec97b43a-6881-3039-8a78-5130a9691d18 | -17.64234 | -57.54469 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 08498674-b28e-377e-a884-cccef885df92 | -17.57409 | -57.5148 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 30610840-cf2c-3c49-b8a5-00fe4311c093 | -17.23139 | -57.45819 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ec0c1399-d534-391e-a98d-679204293154 | -15.90544 | -59.26529 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5f99ba9c-9dde-3e73-ba9a-4df2bec513f0 | -17.23166 | -57.47166 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 264cc2bd-dc45-3d8d-8f53-4839f8150712 | -17.57742 | -57.48164 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c672a405-4aea-3fcc-809d-1b24c7c47c5d | -17.23455 | -57.44279 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 19f4c55a-6934-3dcf-904d-5e45b558f828 | -15.91553 | -59.266 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bdb1554-df7a-3b4a-9468-090834cd5cff | -17.66446 | -57.55574 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| c89aea80-df98-383e-9aec-fc0c9fc75266 | -17.68697 | -57.56263 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b6ad6335-487a-3735-8ee0-62897b295978 | -16.04824 | -60.1162 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9159bb5e-ad9e-34da-b742-a8ed06d107e2 | -17.23372 | -57.45104 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 255fd38c-9c3e-30cc-9fe5-4951eaa1ba64 | -17.8285 | -54.54253 | 2024-11-16 05:46:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b1a3481d-12f5-35a5-a776-8a0799d8c529 | -17.64112 | -57.55707 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 10896809-2466-3ccf-b90c-8e3a9c480d1b | -17.62719 | -57.56289 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.6 |
| c5dac0c1-c74b-39fe-bca4-571a11dcb791 | -16.93655 | -57.63886 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| df70485c-8918-3e8b-b47b-7c74e016ba26 | -17.6358 | -57.55224 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| a4cfea1c-88c8-3516-840a-e89141667864 | -17.82843 | -54.54728 | 2024-11-16 05:46:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d9699be2-1413-3c02-9711-a07423070932 | -17.31507 | -57.50676 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 312aa281-bcb7-37b6-93f8-3fd65561ce81 | -17.62676 | -57.56699 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 2971c529-d4e0-38a7-9665-5232e26faf58 | -17.23864 | -57.46001 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 202dc3d5-46d0-311d-9aa1-b85ac268521e | -17.63378 | -57.55536 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1e1197c2-0afd-34e8-8d99-7bc0ae0378e0 | -15.91086 | -59.26246 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8aefad3-5b0e-33b8-ae4c-f6c9303e6258 | -17.63994 | -57.55193 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| d2abbe80-6f7c-39ca-96dd-94c732532d2b | -17.57542 | -57.44344 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e3f46ef6-69c0-3a2e-8720-f93ce2260e4e | -17.5973 | -57.57175 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| c35e638b-55e3-33d1-b17d-760562818057 | -16.93173 | -57.63021 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 843087e3-fd83-3f19-b843-7aef94cf854a | -17.58977 | -57.4747 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 003408c7-2963-3f76-af3c-1d6bc5792dbe | -17.55439 | -57.53749 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3c628ace-78ab-368b-ab99-1738dc1fdaa7 | -17.63335 | -57.55948 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3aa08e89-694f-326b-9c8c-b78a489a70d6 | -16.94953 | -57.62434 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d8864408-04fc-36ff-8ae3-a9d45b7e5b98 | -16.96439 | -57.64629 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 87a31466-3ea1-3e3f-8f9c-88d64854b008 | -16.02047 | -59.37051 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c51636df-ff9c-38b6-b692-41ac9133c862 | -17.66528 | -57.54747 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 88b9edf8-0ac9-37ea-bfbd-2744d373917c | -17.63419 | -57.56869 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 13ff8a7a-68fa-3beb-92a6-3e04d0a37ba1 | -17.57846 | -57.58611 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 59d1bb8f-6771-3d55-8750-af9d025acf60 | -17.23757 | -57.45477 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 536f7a1c-b107-33bc-933a-7a5185d24c6a | -17.63951 | -57.55603 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| fae42e08-9593-38b0-95b7-bed80a6ae471 | -17.59115 | -57.57518 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 76215aa9-ccb3-3383-ab71-19f9890b5140 | -17.66487 | -57.5516 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 3e9ed6f4-f664-3ea5-8b61-b4795cffb784 | -17.26117 | -57.46695 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| fbed8b25-4dce-3f9b-879a-8de2fa5cb900 | -17.59061 | -57.46638 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b075f518-2160-394a-bdcc-e37cf194c846 | -15.89021 | -59.26497 | 2024-11-16 05:46:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ed0e17e-a125-3f47-80cb-893390e601e5 | -17.57867 | -57.46916 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 70cd8eb8-e4d2-3c62-bbe0-891c682d7de7 | -15.47735 | -60.04938 | 2024-11-16 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bece9d2d-604d-3a2e-bdcd-b2cb4dd9119d | -12.17627 | -64.0847 | 2024-11-16 05:46:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2e9faf4-c5e1-3c3c-a589-a97400631f7e | -17.54866 | -57.53679 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 45da6e07-b51f-3cc4-a961-92829ed5339a | -17.63864 | -57.56427 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 9c8ad0ce-836a-30d0-b1c7-6f39296c1aa9 | -17.24562 | -57.44833 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 778af487-7e2b-3543-be2b-7e3b69fbb45f | -17.62886 | -57.56389 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 269ecec1-16f5-3324-b831-8cc3cc8d12ef | -17.31067 | -57.50767 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a4814a65-0959-33e7-a255-1dad15b32f63 | -17.62926 | -57.5598 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 407d9ccf-c376-39e4-9a98-ce55c4806a99 | -17.31679 | -57.50428 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 821d68cb-156b-350d-897c-2320da73d4d6 | -17.59494 | -57.53821 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 22f360c4-fc39-37ea-bd87-4485afaac55c | -17.62433 | -57.55085 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 6f17b998-5ecb-3b13-a053-ce4de21f898f | -17.5643 | -57.43783 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 34b90a6e-163d-371b-a794-dd4c426db808 | -17.25543 | -57.46624 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 288b0f9c-50c6-31f4-b7d7-0d9819dca285 | -17.58669 | -57.56218 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 0b5161d3-3f9a-3c87-a004-a5033d3dafb5 | -17.65227 | -57.54506 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5b1ef530-ff11-3447-91ec-54ca576e6397 | -16.96481 | -57.64231 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| d88023c1-e78a-382c-a5bb-be769bbcc1dd | -17.64031 | -57.56529 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 0d005f90-7b95-3bdc-a954-3f29f7875af8 | -17.62234 | -57.5714 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 7f654efc-367d-39b2-a77a-0c2f759d1a56 | -16.84229 | -57.00702 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ee432e51-dc5a-33f5-91ae-7b6e7ae34946 | -16.93821 | -57.62297 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| bf193346-c14b-3bdb-b86d-238d522365d7 | -17.54907 | -57.53267 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 9a8a9422-5748-37e6-a3a7-24c323692539 | -16.93131 | -57.63419 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dee51c29-9a07-396e-99de-b2eef01fdf20 | -17.59073 | -57.57927 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| e0e8a383-f584-3f9b-a23f-2a5e3aa27639 | -17.63539 | -57.55637 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| a1250a22-80ea-3a79-b46e-23f56980e51f | -17.2303 | -57.19009 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1a7f433f-3c7c-35de-bfaa-96490e553733 | -17.30891 | -57.51014 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 766121b2-6517-325c-b825-6e209733d06f | -17.58527 | -57.46156 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |


[Clique aqui para ver as próximas entradas](README59.md)
