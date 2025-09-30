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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d6330ae-4bad-3d35-b09f-1bd3fcfaedb3 | -14.51026 | -48.41449 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ce4819a6-d795-3417-a153-905e7ef0a143 | -10.6059 | -49.64383 | 2025-09-30 00:33:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e7a372eb-22e9-3f53-b639-6bf61ae44360 | -12.84951 | -46.99728 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 99655c19-ba30-34ed-bb4c-f5e011c7b861 | -15.37628 | -47.0725 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 80dd7b6b-c9a9-3413-b9ef-fc41a7d7972e | -14.52165 | -48.43166 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| ce507782-85b9-3c1d-81c1-96c9af225a65 | -15.28244 | -47.86068 | 2025-09-30 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 08699e9b-70ee-3d44-bffe-b0a962b60d3c | -14.40004 | -47.14837 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 15527f13-4eec-3e6b-acd8-dda90fbc1ff1 | -8.71005 | -47.98863 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 27f1d8bb-9a10-31bd-80ac-103ef1f07382 | -12.8508 | -47.00637 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cf25d466-a173-3125-bfcd-f8ad46f37344 | -14.72217 | -45.22361 | 2025-09-30 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| d0272723-60a2-39a0-a4ad-828259429490 | -15.27441 | -49.26304 | 2025-09-30 00:33:00 | TERRA_M-M | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b6b4661c-af54-3bc0-8790-163b4b17a08e | -15.5321 | -47.87725 | 2025-09-30 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8b33e83f-19fe-3b1a-97a9-2df43eab0de6 | -11.43395 | -43.50612 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 764e0b35-5b02-3521-959d-5d31c660e2a7 | -12.2341 | -47.80153 | 2025-09-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 59bb26f7-e7f8-39a5-8a3a-119435a272c2 | -11.16208 | -54.10874 | 2025-09-30 00:33:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 77e97a2b-2a1a-3d16-98e1-3ef66eac2049 | -13.15665 | -47.42021 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 227b59c2-8f2e-3c13-be77-32c5783ad843 | -13.37352 | -43.72421 | 2025-09-30 00:33:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 827bd3df-5ec6-3c36-bd6c-eba7f30f179c | -13.24411 | -48.44839 | 2025-09-30 00:33:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0807b9b1-5429-3d77-af61-a2aa0b2d8a3a | -13.72113 | -48.63963 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c73976a-368d-3176-bdf6-af54facb4e93 | -11.45865 | -45.00468 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 189df9e0-2e50-35c6-a9cd-ed3e68a8997f | -8.96719 | -47.45409 | 2025-09-30 00:33:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f4865c8c-eae8-3732-9aa7-2fc4f93f8550 | -15.59877 | -47.82383 | 2025-09-30 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.1 |
| afeb4917-aa05-3eb7-a8c3-8b577513aa5b | -10.64825 | -48.54021 | 2025-09-30 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6f9534af-6399-38e6-b6d7-5a59f6d6b133 | -14.25482 | -52.95864 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 3ff78567-1c7b-3122-9f2d-ebb903ae8e94 | -11.05716 | -47.82526 | 2025-09-30 00:33:00 | TERRA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 45a5a08f-6e4e-36db-8bf1-2c912a4801b6 | -15.49632 | -48.56595 | 2025-09-30 00:33:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 63cc457d-d9fc-3548-803b-f3fb45a8e796 | -14.5254 | -48.45974 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bb910698-dc6b-3b71-95f0-9af0c303b66c | -10.25905 | -48.05172 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4e8fecfb-d9b4-3010-8e3c-ddde999defac | -12.06619 | -47.98462 | 2025-09-30 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| af5a7487-8eed-328c-a18a-cd1058ad5fd2 | -7.85186 | -46.75199 | 2025-09-30 00:33:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d0fdacea-28fc-3aee-85f6-9f9770154846 | -13.38627 | -48.07304 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 81c11084-5844-3c13-bf18-c1879d578ee6 | -11.21247 | -47.22216 | 2025-09-30 00:33:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 42a3e416-fd62-333b-935a-891dc0d319cb | -14.55266 | -48.25729 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4cc822b8-64da-3a51-a6e5-d73c104d4d9d | -9.69661 | -48.24271 | 2025-09-30 00:33:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bcb897c2-cc04-3af0-b29e-9d49b9764be5 | -12.8393 | -46.98935 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b8c580f6-c52d-3e39-9be2-0a8184ddbd3e | -11.37639 | -45.06998 | 2025-09-30 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 6d749473-a977-346d-bdff-d30ab86e64c1 | -10.39038 | -47.80133 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca954e1f-8199-3c4f-bf5d-bcd0bb4164ec | -14.56797 | -48.23642 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7fe50c67-11e1-3ab4-801c-dd54c1e86ca6 | -11.65583 | -47.49273 | 2025-09-30 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 99347b0c-7e56-3d82-b8bf-5f49bd53d0de | -10.10171 | -47.77932 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4cf79605-9089-3cb1-880a-48e12acc68c6 | -13.66166 | -44.31972 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09ce0e1e-e9e3-322d-8ef1-1cc74526ae6a | -13.40611 | -47.54865 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| f94e7c2d-204a-37bf-af12-abb05cd134d1 | -15.2812 | -47.85151 | 2025-09-30 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 64a909e6-8b06-3bd7-af4c-16d61f817664 | -13.3056 | -48.70218 | 2025-09-30 00:33:00 | TERRA_M-M | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e56ea3f7-9f32-3f30-a304-ba7c1a02271f | -12.8482 | -46.9881 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8e0c943c-dd88-31ab-a99b-0b311c6dd993 | -8.38253 | -49.40779 | 2025-09-30 00:33:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0c1dfe4a-14b6-320a-b37d-76b28f5962bc | -13.85137 | -47.9741 | 2025-09-30 00:33:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f5196e7e-349d-327b-9755-c9f9b1eedec8 | -8.88804 | -51.69108 | 2025-09-30 00:33:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1799a09d-3bd2-3164-835f-b8c3b77ae042 | -13.36039 | -46.38099 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a0e105eb-0263-3bb9-b9f8-6776d28b4d54 | -15.20588 | -49.56648 | 2025-09-30 00:33:00 | TERRA_M-M | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee071fdb-721f-3fc1-8478-ffd6589b7fa3 | -16.16042 | -51.94226 | 2025-09-30 00:33:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c0746b46-cadc-3923-aca6-efce14064dcc | -14.71755 | -48.24902 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4d837991-57c2-397e-bd41-3011fa3503bc | -10.54162 | -47.90091 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c37caf6-741e-3950-b289-5042bece285f | -14.56112 | -48.45449 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6cc195a6-d897-3e86-8c85-8c8b0abd7723 | -12.86448 | -46.91114 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 2c0edcba-7628-307b-99b5-861018ef3cb5 | -14.64436 | -42.37159 | 2025-09-30 00:33:00 | TERRA_M-M | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 75.6 |
| f1496ac5-3a0c-338a-9e42-2bc8bde388a1 | -8.50589 | -50.95003 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d3cd3ed-f9e4-319b-a189-f4d1d99ac73a | -13.5739 | -48.09797 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f47a6cc6-c561-336d-8eb4-88b98b3e2b56 | -14.61286 | -48.28947 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 49a08611-79b9-3af2-8d94-860d0e425254 | -9.55696 | -54.64246 | 2025-09-30 00:33:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9d07ff8b-dce5-35f3-8fd8-deff519d7b58 | -8.77097 | -50.58216 | 2025-09-30 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| aa83f4be-cb4f-34b2-a7f3-7ec030c8ddc1 | -9.44737 | -50.89592 | 2025-09-30 00:33:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 4ea4d203-d1c5-3671-ab78-fd5bacc1e966 | -14.38996 | -47.14069 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 925462f0-6903-3dcb-b019-5685b65985ce | -14.38869 | -47.13157 | 2025-09-30 00:33:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dbcfc907-53a6-3821-8b07-634e4408f957 | -14.69979 | -48.25183 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4ba3bd62-fd18-3344-88d4-044c19fd116d | -14.51646 | -48.46098 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 15f97f86-f0e7-337e-9ff0-025c9461d435 | -8.09567 | -48.00435 | 2025-09-30 00:33:00 | TERRA_M-M | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c8739ac5-3057-3805-8124-efb788c2b639 | -13.73256 | -48.65699 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 089d9167-258c-3c94-bea9-4510ec55eb7d | -15.46618 | -47.92459 | 2025-09-30 00:33:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1bc6e0ea-1b30-31ff-9b98-95cd7be6963c | -7.82265 | -46.99308 | 2025-09-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 73ee9321-dbac-321f-bfcd-3966f1b83303 | -14.70261 | -48.13857 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 993d910b-22ad-30fa-b65f-1bb5cb0951e9 | -13.65981 | -44.30776 | 2025-09-30 00:33:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9bac7de3-9afa-32b3-be08-5a41f728dc8b | -10.33942 | -48.22462 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d2060cf9-276d-3266-a721-590db0a3b03f | -12.66626 | -46.87806 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ba1c15a4-8a76-3d55-9b11-f716eacb12b7 | -11.49082 | -43.51109 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3b173bc0-2427-36b1-afeb-009be940572a | -7.81345 | -46.99442 | 2025-09-30 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| de8ee80a-0f1b-3506-b206-c94cd74b6d95 | -11.8909 | -48.04982 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 98ed8059-d088-31be-aa58-5588489183b9 | -10.40369 | -48.16985 | 2025-09-30 00:33:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 7c2a1422-9ee5-3993-bc35-792918943263 | -11.72392 | -44.44993 | 2025-09-30 00:33:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 3b04e620-a180-3d7e-b8eb-74973cc96f25 | -14.6141 | -48.29869 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f93c53d9-4bb6-3e67-b348-2a1f16c96802 | -13.57266 | -48.0889 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d2e72022-8785-3ac1-b865-38e699fa9b39 | -15.53085 | -47.86811 | 2025-09-30 00:33:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a2171bf2-7f6a-3356-947b-fd56b091d57b | -13.21841 | -47.33109 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 70427bdc-7885-31dd-846d-79632644758a | -10.83759 | -47.97635 | 2025-09-30 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2a370b2b-3dbb-3a19-89b0-d5a35d3ccd5f | -11.44711 | -43.51861 | 2025-09-30 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4728860c-6808-3950-ad93-8973437a28de | -13.78581 | -47.97126 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0a4f3689-b41c-36eb-8c48-c2bc3409a6b0 | -14.57625 | -48.21952 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 29.5 |
| cd41fb78-9eb4-3510-9105-8f8a272da910 | -13.64424 | -47.3385 | 2025-09-30 00:33:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bb779fe5-59e3-331e-b5ff-c5bfbe4427e8 | -10.11181 | -47.78697 | 2025-09-30 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5dc3f7f4-a730-34dd-a312-78c8a6479e65 | -8.25566 | -45.52158 | 2025-09-30 00:33:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 08d0b550-94a9-3415-af9b-74bd488f42ad | -12.96915 | -46.41765 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e5f8ffdd-9974-3876-a951-7ac55660289a | -11.91981 | -48.06385 | 2025-09-30 00:33:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e3b8ae53-bae3-3579-9d93-7b090e09a18e | -14.25754 | -52.94772 | 2025-09-30 00:33:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 96286526-beec-39aa-a092-132f749cc7d4 | -13.07305 | -47.08158 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3aa90f5-d4df-391e-b5c5-196bad68e08a | -14.70386 | -48.14779 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e8245724-7529-3cce-b26f-00c420f5bbcd | -14.52041 | -48.4224 | 2025-09-30 00:33:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 951f8501-48f0-3d63-b5c0-f6d034418110 | -10.03561 | -50.19334 | 2025-09-30 00:33:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0fac9328-dde8-3a24-87b8-525ae35f7e30 | -7.84262 | -47.26413 | 2025-09-30 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9aff03ea-a100-3884-ac21-05c5361674ea | -15.39829 | -44.97657 | 2025-09-30 00:33:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bb921114-512d-3213-ba40-cd5be5a8f080 | -12.86318 | -46.90203 | 2025-09-30 00:33:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |


[Clique aqui para ver as próximas entradas](README7.md)
