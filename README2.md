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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3cbaf2e-e74d-3048-b1cf-54df61216987 | -11.4205 | -45.095 | 2025-07-08 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 3c8a991c-ae4a-3be2-b0da-b12edda36382 | -7.2405 | -43.0899 | 2025-07-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| c23f1006-162e-3441-93f8-a29fb19ab59b | -7.2025 | -43.1171 | 2025-07-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| b219acea-c38f-344a-b88e-89ab3ad669a4 | -10.6489 | -49.4483 | 2025-07-08 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b9a38716-d1fb-3f44-8a44-a5827f0fa97d | -10.6486 | -49.47 | 2025-07-08 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 365d9776-59c0-38c4-b29b-704544ea0442 | -10.6299 | -49.4504 | 2025-07-08 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 87bdb893-4e73-3f62-9e30-72817850f0ff | -11.4201 | -45.1181 | 2025-07-08 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| ef462103-7e4a-3046-a8b0-07c50d65dc0c | -7.2594 | -43.0881 | 2025-07-08 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 173.3 |
| a39c82fe-6c6d-345d-8538-1d16b753ed85 | -10.6296 | -49.472 | 2025-07-08 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4b2c08b5-2ff7-3bf3-b8d6-89f8781cee44 | -21.79689 | -52.77058 | 2025-07-08 01:00:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aeaec7a6-35dc-3b93-9ad5-0784268ed1d4 | -20.78194 | -49.8611 | 2025-07-08 01:00:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3c032530-3d44-31b7-92df-74427ee71fd7 | -21.04619 | -56.0008 | 2025-07-08 01:00:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 15cff16c-c4f4-3dc8-aeab-af91f290e44a | -21.03885 | -55.99409 | 2025-07-08 01:00:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4eb2626f-23e4-329b-83b6-3f6a36bb2e9c | -22.23979 | -49.61221 | 2025-07-08 01:00:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e2e2aecf-369c-360c-a5de-667e7f18c7f6 | -21.30585 | -48.56911 | 2025-07-08 01:00:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 2477bd49-622a-3217-9b64-23a03c76d2b4 | -19.75302 | -54.00037 | 2025-07-08 01:00:00 | TERRA_M-M | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8c0f6286-4fa4-33d4-ad9c-ec9e83a9cb67 | -20.77526 | -49.85727 | 2025-07-08 01:00:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 1119f432-a224-3f1f-8465-ac913f32dd0f | -20.62324 | -54.8418 | 2025-07-08 01:00:00 | TERRA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 542b8732-3c1d-345e-b97c-7c18fe45530e | -20.77683 | -49.86771 | 2025-07-08 01:00:00 | TERRA_M-M | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 9ba17e30-041c-35e5-964c-a289b5c4a31c | -21.18968 | -48.94308 | 2025-07-08 01:00:00 | TERRA_M-M | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b81b5335-64b5-38d4-a121-03aee8af8913 | -21.30397 | -48.55711 | 2025-07-08 01:00:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 220746de-cc13-34ab-9f4a-36954e9f4219 | -18.22629 | -44.19329 | 2025-07-08 01:00:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 20b3aa14-218d-3a33-b6a2-bd45d64b5d1d | -21.79559 | -52.76084 | 2025-07-08 01:00:00 | TERRA_M-M | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 15.0 |
| afee5566-c239-38f1-8fa3-e4b905502778 | -18.22537 | -44.20015 | 2025-07-08 01:00:00 | TERRA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 95c3ac46-87ef-3c06-883c-903bfb0ca196 | -11.42739 | -45.11872 | 2025-07-08 01:02:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 1255e18f-d57f-36b3-bef2-b2dff94f83ef | -15.8125 | -49.96524 | 2025-07-08 01:02:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 0bc980cf-f593-3aa1-87be-cccc80d3047d | -18.64637 | -55.73077 | 2025-07-08 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 75efd999-3fbc-3aef-b49b-80cc7eea7476 | -12.57771 | -56.98695 | 2025-07-08 01:02:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| fd09c044-540f-34de-8c76-42b68d379459 | -11.44287 | -45.11594 | 2025-07-08 01:02:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 630ed3e7-c996-333f-8f38-9c6d9c4f5f7f | -15.69033 | -53.3283 | 2025-07-08 01:02:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f296b3e9-40e3-3a42-a46b-3a0e743ac103 | -11.42695 | -45.09341 | 2025-07-08 01:02:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 52e2ae7f-153f-3bbb-8212-06e793b0834c | -10.63445 | -49.47 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 905678ac-b6e0-3602-8a44-926321f1e26c | -12.28936 | -50.11634 | 2025-07-08 01:02:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0e4106c6-6357-368d-94c1-2a6da18d2b75 | -10.36542 | -48.72261 | 2025-07-08 01:02:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 785cb1f3-ffb1-3734-a1f4-7ee3a2d3a5b1 | -14.31816 | -58.7006 | 2025-07-08 01:02:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 97696f22-caa1-39b0-af1d-8d86f18e7233 | -10.94665 | -49.25626 | 2025-07-08 01:02:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 18d66952-61ad-3411-b6b1-e9f6f68c2928 | -11.43219 | -45.12451 | 2025-07-08 01:02:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 12cb7fd3-e18f-34cb-a52f-d63038aaa92c | -11.35156 | -55.39906 | 2025-07-08 01:02:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7313c3ff-b916-3cd1-af62-3efe438dbea4 | -10.35993 | -48.73025 | 2025-07-08 01:02:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9cbf8d5e-0c5f-3a46-8cf0-dc59eaa9ae37 | -11.42192 | -45.08764 | 2025-07-08 01:02:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 1bf63fd2-65dd-3f99-90ef-25137188f2ab | -10.64563 | -49.4682 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 158.7 |
| be87fa91-83d2-3104-b0b7-8fe574b40126 | -12.32697 | -49.31378 | 2025-07-08 01:02:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 00d28726-e2ac-3160-b606-fe56c5658e41 | -10.97095 | -45.10498 | 2025-07-08 01:02:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| da5bb286-6cc9-392b-9a64-96304293e46b | -10.63216 | -49.45517 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| dc0f8a10-d660-38d2-a9a8-bffd4e183caf | -15.25947 | -51.53474 | 2025-07-08 01:02:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9246097f-2af8-3e64-bafd-d3b9e617492c | -19.09247 | -56.05409 | 2025-07-08 01:02:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| f8bf0efa-2d12-391d-b66d-41bb442903ed | -15.8107 | -49.95378 | 2025-07-08 01:02:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1cc64cb3-88b5-3c32-a118-39121e081a14 | -15.81074 | -49.95958 | 2025-07-08 01:02:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 125d1b5b-380d-34ca-bb94-446a9015743f | -11.35281 | -55.40843 | 2025-07-08 01:02:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 23b36bb1-0c72-3461-8f1d-7a324948a400 | -11.87453 | -58.7103 | 2025-07-08 01:02:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 03eff4d6-5c58-3c40-8970-c9966af9c0b7 | -10.6568 | -49.46637 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| dff3ae9e-dc80-3a26-916a-4c0fec3bf49a | -12.32923 | -49.32808 | 2025-07-08 01:02:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| b98f2c95-4571-3e66-9f38-a2d9e3392ad5 | -10.58022 | -49.11922 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9f050045-0381-368d-9fbb-25ee59a75de2 | -10.58265 | -49.13491 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| c010def2-c7a7-3110-99cf-9f74ec0e2410 | -18.41977 | -54.7123 | 2025-07-08 01:02:00 | TERRA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 865558ce-72e6-38b0-96a4-5d629bc51da9 | -17.77649 | -52.4392 | 2025-07-08 01:02:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f1baac3b-3774-30ab-9b2a-f3dcdfdd5340 | -10.64336 | -49.45342 | 2025-07-08 01:02:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 7e0ac459-522e-3808-b258-321157a19b29 | -9.37659 | -48.95291 | 2025-07-08 01:05:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 3923540c-a710-3d62-a865-a2ba3d961157 | -10.41639 | -49.77599 | 2025-07-08 01:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 98d3dc29-162d-39d0-81a0-cfce7503e6db | -5.7348 | -49.13752 | 2025-07-08 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 9a27d559-4eef-3523-9d10-8fd4e571a46e | -11.02351 | -56.25296 | 2025-07-08 01:05:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cdfd8cc9-41b5-3550-84b2-5a4d074c5d6f | -4.29311 | -48.0642 | 2025-07-08 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 1f56e84d-b5e9-3792-97ff-e1a4a89e7ccf | -10.83092 | -54.01876 | 2025-07-08 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 48ef9947-a751-3114-b857-1fc1270101dc | -5.7356 | -49.13179 | 2025-07-08 01:05:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 214dd7c1-b68d-3917-95e5-760585ee670a | -8.70366 | -50.01921 | 2025-07-08 01:05:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4f586fe1-e299-3c83-8ed3-3af810179357 | -9.22542 | -48.58659 | 2025-07-08 01:05:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| f2529f41-65e9-3d6f-a9f1-e1ab103ce192 | -10.47511 | -51.86884 | 2025-07-08 01:05:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4207c5f3-81f9-3781-b570-28636fc85df7 | -10.41423 | -49.7618 | 2025-07-08 01:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4a70e4e1-c6d3-38eb-995d-edfd0a285954 | -9.22834 | -48.60463 | 2025-07-08 01:05:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 5f380764-cb93-3b85-b113-6c92be1d1a51 | -10.82207 | -54.02005 | 2025-07-08 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| af7c4fe7-9c21-3ed1-bdaa-41ea079c889c | -10.82082 | -54.0111 | 2025-07-08 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8b3d50f8-7aed-3e91-8b88-5aa356ce0336 | -4.29746 | -48.0579 | 2025-07-08 01:05:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 8784204e-92dd-3e37-912a-c691d2235e55 | -10.2298 | -56.76582 | 2025-07-08 01:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f6d08e4e-243a-37b0-8e0a-96dbc53b903c | -10.83216 | -54.02771 | 2025-07-08 01:05:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 663c02c5-2d69-3288-9248-f5e34acfa3d8 | -9.23495 | -48.59133 | 2025-07-08 01:05:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bf0a7486-86ff-34c2-99ab-fef4a1c88ada | -9.22266 | -48.59344 | 2025-07-08 01:05:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 43d4b723-b9f5-3a05-8825-c2b51ec06018 | -9.37116 | -48.95934 | 2025-07-08 01:05:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1ce307e7-5c8d-3157-ac08-b5875be37393 | -10.39376 | -52.17631 | 2025-07-08 01:05:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2a868ac5-9907-38d9-8ab1-87536b3538ab | -9.70804 | -56.18063 | 2025-07-08 01:05:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9c4e3a1-ba17-3573-a014-634fda56b90f | -11.4397 | -45.0923 | 2025-07-08 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 1230226c-47ea-3b1c-962c-61f19d138d77 | -7.2405 | -43.0899 | 2025-07-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 1ec9636c-bc86-379e-9485-2b18cccf07a5 | -10.6489 | -49.4483 | 2025-07-08 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| fb770edb-6727-38dd-80df-7ec4987acf55 | -7.2025 | -43.1171 | 2025-07-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| c7801c5c-d9e4-34c3-ac84-ea404508b838 | -7.2408 | -43.0664 | 2025-07-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 5830c526-7bfa-3ed4-92f9-d94edf9ef2cd | -7.2597 | -43.0645 | 2025-07-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| 831cebab-9f1c-3609-8dd9-8deffb90963f | -10.6299 | -49.4504 | 2025-07-08 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ce246574-9bd1-3000-b01a-fc0870efda7b | -7.2023 | -43.1406 | 2025-07-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 66068f82-9864-3725-8bc7-7fa120ca98cd | -7.2594 | -43.0881 | 2025-07-08 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 851deb1d-d031-39c2-979e-e216114940dc | -10.6486 | -49.47 | 2025-07-08 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| f83951f0-3193-3b90-9c23-d51a2c3a27c3 | -10.6296 | -49.472 | 2025-07-08 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 68dbfdeb-d8ae-399b-a9fc-b2c8e94927dd | -10.9811 | -45.1104 | 2025-07-08 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.7 |
| e63e7664-0ad1-351e-bf1b-6744ea4c281c | -10.6489 | -49.4483 | 2025-07-08 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 0be8b0fa-9c29-32e8-83f6-b6fbde81f27d | -7.2405 | -43.0899 | 2025-07-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 863982e8-9a04-34d7-af38-750fc73bb24d | -7.2408 | -43.0664 | 2025-07-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 600a6dd7-33ab-3569-81c4-e0a6859d489a | -7.2594 | -43.0881 | 2025-07-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 82aacf20-9eff-39d7-9ff3-dd5e63336a5d | -10.6296 | -49.472 | 2025-07-08 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d5969ea6-3a56-31c7-8cf5-f86adc298abe | -7.2025 | -43.1171 | 2025-07-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.1 |
| adedabe3-78dc-3d6a-afd6-c4e2eb368c88 | -10.6486 | -49.47 | 2025-07-08 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 405aeef0-44bf-39cc-ae20-b147d3219f66 | -7.2597 | -43.0645 | 2025-07-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| aca75430-4fbf-3beb-8b4c-c3103d3c621b | -7.2023 | -43.1406 | 2025-07-08 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |


[Clique aqui para ver as próximas entradas](README3.md)
