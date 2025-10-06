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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb73b798-49c6-3464-996f-dda250f9ea49 | -4.6505 | -43.1805 | 2025-10-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a9cfbb64-527c-3008-a88b-acf0be6ca9e6 | -14.5442 | -46.9405 | 2025-10-06 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cabea1b0-506b-38c6-891d-d22d4475ceb4 | -12.3793 | -63.7294 | 2025-10-06 00:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| b6e6ce18-9c13-3f2b-b2b1-564c8f475fd9 | -17.9605 | -57.5904 | 2025-10-06 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.1 |
| 0acd83be-08d1-3403-b7ff-40764790e514 | -5.1882 | -46.1557 | 2025-10-06 00:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 5e068d05-c431-39ec-9979-50cdd63a4fee | -14.5438 | -46.9633 | 2025-10-06 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 95547ac7-50ee-34fb-b574-1ac9c2299e96 | -2.5967 | -48.134 | 2025-10-06 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d15608ba-fd26-3eb1-b6a0-70d86c244086 | -17.9803 | -57.588 | 2025-10-06 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 8db85e22-9897-3d45-8efa-80eba794dee5 | -18.1167 | -53.3977 | 2025-10-06 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 8ef76bce-f294-389a-a1b8-33ea90574851 | -9.3159 | -46.0231 | 2025-10-06 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 56ea2a38-da98-30dc-830e-6234ac5c925f | -14.6703 | -48.3828 | 2025-10-06 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4322c173-fab8-3989-a558-6f47cc85d0db | -9.3162 | -46.0005 | 2025-10-06 00:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a41b8268-c201-3527-b6f7-3c2c023bcf8b | -18.1366 | -53.3946 | 2025-10-06 00:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8731b780-5f37-38cb-8501-1372faa272ad | -11.0151 | -46.5393 | 2025-10-06 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 2162a538-e37a-3a79-aa2e-0d053214b87f | -14.6897 | -48.3797 | 2025-10-06 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 10b445f5-3743-3e20-a5df-05936394e7f0 | -10.9848 | -51.1655 | 2025-10-06 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| e4df4bf6-bbc2-3b8b-9df8-8a9ed1e5f401 | -5.3285 | -47.2963 | 2025-10-06 00:40:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| c16f2e64-eff6-3945-a588-683c24aa98d4 | -4.6504 | -43.2038 | 2025-10-06 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.3 |
| e81a1fd1-2a81-3d73-953e-e5ad0bf2858d | -14.55 | -46.6662 | 2025-10-06 00:40:00 | GOES-19 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 530a0df6-2c3e-35bd-a909-ea3b6d21b26e | -2.5783 | -48.1129 | 2025-10-06 00:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 6863e035-bb0a-38e6-9b7e-8b8a4e66ecfa | -17.9803 | -57.588 | 2025-10-06 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.4 |
| ebc3d8c5-bd3c-33ca-b4cb-3392f525a90c | -18.1968 | -53.3638 | 2025-10-06 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| d62fd6cb-c79c-3b1c-87fa-cc6d60289cc6 | -14.6703 | -48.3828 | 2025-10-06 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 914deaed-f60d-3969-9f31-e185498f0ced | -21.7083 | -50.0972 | 2025-10-06 00:50:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.3 |
| 4cbda8a7-b535-37ae-b8c3-9e5b09d17124 | -13.2699 | -47.8398 | 2025-10-06 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 44e5c6a5-2b89-3298-af9b-1e77afb7f4b6 | -14.6897 | -48.3797 | 2025-10-06 00:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| de2969cf-1add-3da4-ac53-7b632053e880 | -12.5791 | -46.7294 | 2025-10-06 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 20b0debb-b749-3f4b-b3c1-c6fb6043e2f4 | -6.5735 | -49.8695 | 2025-10-06 00:50:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 66a4d961-5fbe-3ba3-aa04-e987118f1f4c | -13.2892 | -47.837 | 2025-10-06 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 6cdae282-d9c3-3947-b00a-3b1efa252989 | -14.6135 | -52.495 | 2025-10-06 00:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| be1ac8ae-3c42-3559-8eaf-5d7d3dde4c64 | -18.1963 | -53.3853 | 2025-10-06 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8995fffb-cf9f-3200-9be0-5998695a13b0 | -12.3793 | -63.7294 | 2025-10-06 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 802de5ea-9483-3f75-8b68-a1f6865311cc | -5.7217 | -44.8366 | 2025-10-06 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 2e1f7f2e-7e5c-39dc-aac6-00d9437cb06a | -11.0151 | -46.5393 | 2025-10-06 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9151882b-7442-31e0-806b-657b7766837a | -7.0181 | -42.7818 | 2025-10-06 00:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 6899af42-947f-34a6-b699-482042cec02d | -5.6373 | -45.9705 | 2025-10-06 00:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 88b0c482-36a2-3eb8-ba7a-9bb4e32c2c47 | -17.981 | -57.5468 | 2025-10-06 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 404ab06a-77f6-3b53-8778-16576e8267ef | -14.6131 | -52.5163 | 2025-10-06 00:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f920dae1-3213-3a80-9e2d-e355353b20e1 | -5.3285 | -47.2963 | 2025-10-06 00:50:00 | GOES-19 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| beebf53a-8d60-3e48-8aec-e093bd174df4 | -12.4468 | -45.5646 | 2025-10-06 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 6d5edf45-ba53-3eeb-a517-3776da0d53c8 | -18.1366 | -53.3946 | 2025-10-06 00:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 5bcb136a-093b-30fa-9ec7-cd862b26dbb6 | -13.2703 | -47.8175 | 2025-10-06 00:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| ca5cd8aa-17e7-3928-865b-dee35afcfd4c | -4.6505 | -43.1805 | 2025-10-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 950436d7-815d-36d8-91fa-9765276ec6be | -18.0008 | -57.5444 | 2025-10-06 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 85ce656a-10f4-3a84-a646-ad57791dea1d | -5.703 | -44.838 | 2025-10-06 00:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 60346b29-07b4-3d01-8476-95efa24adaba | -4.6504 | -43.2038 | 2025-10-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 21fb632d-c2b8-3ac0-aaa7-2a20a22d1748 | -14.5438 | -46.9633 | 2025-10-06 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 55.4 |
| f6afcd58-b020-3182-b2bd-69c3d6709a59 | -2.5968 | -48.1124 | 2025-10-06 00:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 8d276456-3664-3a23-bbea-fe2b7a9ed067 | -4.6318 | -43.1816 | 2025-10-06 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d1ec6e51-5858-3f94-afcf-61105599c9dd | -18.1968 | -53.3638 | 2025-10-06 01:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ca78a78b-7e13-3fc9-abc0-3c64443ca370 | -17.9998 | -57.6062 | 2025-10-06 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 54a0bcb0-d11a-3ced-85b4-466e1d2535d7 | -21.7083 | -50.0972 | 2025-10-06 01:00:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| 3375d56f-1fe7-3421-b710-435cd4a30860 | -17.9803 | -57.588 | 2025-10-06 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| f151a907-8460-373a-932d-2e0432ad1740 | -18.1963 | -53.3853 | 2025-10-06 01:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.2 |
| bad9e8a2-051c-3a80-ad4c-7080f899810b | -9.3351 | -45.9984 | 2025-10-06 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| ccfd4604-8706-3c54-8d3d-5f5757a5b9a4 | -13.2703 | -47.8175 | 2025-10-06 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 0c34faa3-a0bd-3965-963d-316993a0cc4f | -14.5442 | -46.9405 | 2025-10-06 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ee678f0f-ab01-3d8c-878d-48801d7308c8 | -12.3793 | -63.7294 | 2025-10-06 01:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e28c91eb-ecea-3bab-9397-e478a5a0f382 | -9.3162 | -46.0005 | 2025-10-06 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 329.5 |
| 67badc96-1629-3521-b99e-3eedd2b80e2a | -9.3348 | -46.021 | 2025-10-06 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4f4ebd52-7c8b-33a0-8c8e-c30867481d71 | -9.3159 | -46.0231 | 2025-10-06 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 545fef2d-435b-3ed5-b2cd-0f44b1d1f03c | -18.1366 | -53.3946 | 2025-10-06 01:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 3686986c-9999-300c-a7d7-06cd3782de36 | -2.5967 | -48.134 | 2025-10-06 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 1e40acd4-4c2e-3aab-828b-e0756cbc39c7 | -14.5438 | -46.9633 | 2025-10-06 01:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 85615fed-a746-3f41-894d-a68735c90aef | -11.0151 | -46.5393 | 2025-10-06 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 81c31e92-7d02-3644-9b45-13fe27467f42 | -2.5968 | -48.1124 | 2025-10-06 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c9078f8c-b933-3dbb-aaec-529c6a44c324 | -10.9848 | -51.1655 | 2025-10-06 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| b0aeb61e-0a75-32d3-9746-8f42c965edd3 | -13.2892 | -47.837 | 2025-10-06 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2ba0e82b-c5fd-3a16-bb29-8ee9e24e601f | -17.981 | -57.5468 | 2025-10-06 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| 45c19f4f-7360-33bc-98e5-79bca48e4625 | -9.3165 | -45.9779 | 2025-10-06 01:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4a150dec-3592-3e72-9a86-6a84e8437d42 | -14.6897 | -48.3797 | 2025-10-06 01:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 19215611-6cc5-33a1-87f5-ac003fc28ccf | -5.6373 | -45.9705 | 2025-10-06 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 293ecde7-164d-338a-aeb9-8975ccd8e88f | -13.2699 | -47.8398 | 2025-10-06 01:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4d119a83-ab99-3ddb-b9a6-8959c7f5f13c | -10.9851 | -51.1443 | 2025-10-06 01:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 25537c85-9bab-3418-afd7-de5a6ad1511d | -8.6144 | -46.2778 | 2025-10-06 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b420a95b-2686-3712-998b-4dbf03dbebeb | -6.5735 | -49.8695 | 2025-10-06 01:00:00 | GOES-19 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| bdd466aa-1fc1-3310-aab9-97ff04ade2b5 | -14.75388 | -54.67733 | 2025-10-06 01:09:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5a02fa46-b05a-37eb-b7a8-aa98dc51d24a | -17.96386 | -57.59106 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 4789036b-3b8a-3dfd-bd44-444d4b656dae | -17.68363 | -52.23808 | 2025-10-06 01:09:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d776ef05-b595-3e0a-b57b-6c03d5218ef1 | -21.73152 | -50.08562 | 2025-10-06 01:09:00 | TERRA_M-M | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 30909452-cb4b-32f2-9775-8aa2b8e615ec | -18.12774 | -53.40147 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 750bdde4-ab00-39c5-a0dc-fbe5dcc0fbe9 | -18.01124 | -57.5968 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 91ce9223-370e-3bb6-8295-295922d12686 | -16.05335 | -50.93235 | 2025-10-06 01:09:00 | TERRA_M-M | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 2550db61-b973-3665-9aa9-caff2041bb0b | -18.10818 | -53.41013 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 692bd377-8307-3189-9185-1730a4d5b5d4 | -17.86296 | -57.59246 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 976ec7ea-16ff-389b-b348-555022e854bb | -14.86254 | -51.48665 | 2025-10-06 01:09:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 4ed4bc52-5309-3b71-b66f-36c92c5d6bc0 | -18.13937 | -53.41074 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 6411d0b6-f3c3-372f-b26c-2601fb1ef13c | -17.95621 | -57.60182 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 26b5bbf5-7d53-3c39-9931-f2c0c4dac577 | -17.8502 | -57.63277 | 2025-10-06 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 9faed770-effc-3862-8876-4c50d0dd2f49 | -16.95913 | -52.69314 | 2025-10-06 01:09:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 57f0b6d4-ca39-3ae1-8c62-ce141770c423 | -14.56439 | -46.66505 | 2025-10-06 01:09:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 40c0b468-750f-3e90-a631-3425c8a45ba8 | -13.61268 | -48.69886 | 2025-10-06 01:09:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 41a50793-8028-3ae5-b34a-c48b9643c702 | -15.57161 | -52.46302 | 2025-10-06 01:09:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 38e55b7a-3fbe-3cf0-95fa-bbe7ea4b1618 | -18.13586 | -53.38853 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 25.1 |
| f7deed3a-0748-3c01-93d1-6e99334a2258 | -18.11628 | -53.39675 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 40e39b48-74cd-3f14-9368-012385c07f9b | -18.10092 | -51.82906 | 2025-10-06 01:09:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e4cf5762-cd3f-3c63-9c9a-55c37abd30df | -16.00702 | -50.82881 | 2025-10-06 01:09:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| d04a247f-9d39-353f-a3f5-92844fae5e51 | -14.83938 | -54.22604 | 2025-10-06 01:09:00 | TERRA_M-M | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 48248b65-8f31-33e0-b218-bf5521dc5eb4 | -14.53997 | -46.93261 | 2025-10-06 01:09:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d175dde1-6acf-3020-8622-afc8b86563f0 | -18.19497 | -53.37626 | 2025-10-06 01:09:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 63.1 |


[Clique aqui para ver as próximas entradas](README4.md)
