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
| 0ab10b60-190b-3161-b304-df1b4089a51c | -6.7951 | -47.073399 | 2025-09-07 00:45:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 507fb571-f674-3bb8-82bd-f0637de985ee | -5.9474 | -46.186699 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7ec979d9-7d3c-336d-8a97-9bc4d20afa02 | -14.4351 | -48.4645 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f4b2446d-c5e2-3d71-a5b9-d251cfca3906 | -13.0104 | -48.078499 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3d92df4-326b-3095-be1f-de7867988dea | -7.7522 | -50.759102 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f049835-b7fe-3b9c-bd6f-fd0e4a8294e2 | -11.7646 | -50.632 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2af8bb-2828-3c62-a10b-b93dbc0a342e | -6.8226 | -46.397099 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb738c27-8ce4-3009-88d5-4a6316a33761 | -7.4308 | -44.9552 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd9e7d87-fb21-3768-bb8c-017a917aab17 | -8.6818 | -54.680801 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 402537f6-27d3-30e3-8af5-8e2d812dfdb4 | -8.4976 | -51.334099 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e668e7f6-1ab4-3d3d-8b09-25f904c47e9a | -13.3258 | -43.259499 | 2025-09-07 00:45:00 | METOP-C | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| dc4e3fc7-8746-3d88-908a-fe9eef431a9e | -14.578 | -52.168701 | 2025-09-07 00:45:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d3388e65-db44-32c3-a99d-9b63b88e7e5a | -7.7506 | -50.751801 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf8a20d-38bf-3e82-b70f-8e1bb1f9b993 | -1.9244 | -56.606701 | 2025-09-07 00:45:00 | METOP-C | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0d49f5-2560-35ce-bfb7-e9d660fc35ac | -11.5947 | -47.1604 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d45f31e0-6959-3edb-8b33-711466d4a1b3 | -13.7639 | -52.776699 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d9aa649-79b3-353b-bd1e-a54ace24b281 | -11.4032 | -43.647301 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc797d7-6956-3340-9212-92b42e02ec4d | -9.4075 | -46.765701 | 2025-09-07 00:45:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 124be063-90cf-3553-be9d-40dec414b43e | -8.3344 | -46.9454 | 2025-09-07 00:45:00 | METOP-C | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 572945bf-e920-30a5-8943-a5369b18a355 | -7.7051 | -44.720402 | 2025-09-07 00:45:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 63e66e71-07bb-3c55-b59a-05cf9917a87e | -2.809 | -49.197102 | 2025-09-07 00:45:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb38fe5a-5cb7-3827-b9ac-dfc0cda2052b | -6.2304 | -43.309399 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 688f38d5-4309-38ca-b982-b902fd79610f | -13.7563 | -52.7896 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03fdcfae-97c3-38b6-848b-7b52e33b191e | -6.7582 | -44.215199 | 2025-09-07 00:45:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f89b186f-35c8-398b-ba73-79b9f95fe991 | -9.7216 | -51.1059 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3db49096-e685-3b9e-aa83-7a931fd47767 | -6.1205 | -44.2658 | 2025-09-07 00:45:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7d3068a-772f-3e90-8cd3-741e1b75abbb | -3.5753 | -47.5145 | 2025-09-07 00:45:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62bc0701-dedb-3571-91a8-4f23769abfb2 | -17.211201 | -46.729401 | 2025-09-07 00:45:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ad57c5e2-e210-3383-88a8-7c8fb9a2792b | -6.8294 | -52.802502 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e3ecfe5-8d23-3d46-b17e-9a625e9795b1 | -6.2083 | -42.455898 | 2025-09-07 00:45:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0d159a15-e519-386c-bc50-23ae582ef76d | -12.7619 | -52.9646 | 2025-09-07 00:45:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24635f47-bd10-3590-92ad-59769f562af4 | -6.6013 | -43.9916 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfb0e16a-4df0-3eb7-b68a-d950792f79f6 | -10.7773 | -48.276699 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cc1760e3-0760-3ea3-84da-eb54c607e0e6 | -10.0499 | -48.071602 | 2025-09-07 00:45:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c7a0296-c67e-30c8-a1b6-547fde9dad72 | -1.9314 | -56.5919 | 2025-09-07 00:45:00 | METOP-C | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27874b8-70d9-3a40-801b-648177225701 | -14.8396 | -48.198898 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bb089739-7b59-379d-a315-ee8c62b7dcce | -8.3424 | -48.2728 | 2025-09-07 00:45:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a30efbf3-8885-318e-abaf-bd8012312557 | -9.0448 | -50.464901 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20dfd6f6-8888-3974-b2a1-ea4774172d26 | -8.1083 | -45.328499 | 2025-09-07 00:45:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd5a7db-11db-3cd8-a592-7ce6a817d178 | -6.1848 | -53.276001 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9cecca-7b84-3043-abfe-a3c3993158a9 | -8.9055 | -45.815399 | 2025-09-07 00:45:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e891e472-e50e-3ff9-bdd5-f5f4c0b5362d | -3.2286 | -50.8009 | 2025-09-07 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a702bd8-ba19-3e14-8b0e-05b742c22336 | -8.9396 | -44.271 | 2025-09-07 00:45:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 51d828f9-d8a2-31eb-93e2-f7c8fc1e717f | -5.8537 | -42.437099 | 2025-09-07 00:45:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e6ef1e57-481e-3d8e-86b7-96b8607284ca | -17.3507 | -42.6502 | 2025-09-07 00:45:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8f01ca64-3d11-342e-a928-1cf429708193 | -17.674299 | -43.556702 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 583cc6e6-c31f-3ba6-af43-559dc397be49 | -21.695101 | -47.193001 | 2025-09-07 00:45:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 432d2d12-1f47-3a81-8760-a04089fb4e46 | -10.1741 | -46.687401 | 2025-09-07 00:45:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 289882a4-4512-381e-a082-f06997e25323 | -19.4074 | -44.320499 | 2025-09-07 00:45:00 | METOP-C | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bf200503-d596-3176-a395-5af09d709bc8 | -11.7583 | -50.649899 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cde225f9-7750-3cc5-b484-8cb205dc9b9c | -2.8106 | -49.203999 | 2025-09-07 00:45:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4460d51-08e7-3e9d-946d-1c74a5ffd7a4 | -7.7171 | -44.7276 | 2025-09-07 00:45:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4707e513-f182-3be5-a1e5-84f660a66f9f | -14.8086 | -48.198502 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 13b4f566-c3ac-3c46-aa40-5776eb88c571 | -10.0742 | -48.087898 | 2025-09-07 00:45:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ed48f8a-470c-3102-9eee-a16cca2e9b63 | -10.7175 | -48.603901 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b062283-f53b-3e92-850c-daf1d4300cee | -8.5287 | -51.3353 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 873d93a7-5692-32b5-8459-833880a247b4 | -6.2244 | -43.284901 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 04ec8211-b443-36b2-95ce-36c777dcb77b | -11.245 | -46.497501 | 2025-09-07 00:45:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90c9d414-3fb0-3c89-bce8-6256318670d9 | -6.6235 | -53.171299 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eefa56e-1d2b-3591-824b-ad26bbf90c4a | -10.7808 | -47.749401 | 2025-09-07 00:45:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4971c3f2-ff85-33a2-831e-74e971e86b45 | -22.406601 | -47.454899 | 2025-09-07 00:45:00 | METOP-C | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8718cc4d-a6ab-3eb2-99e5-2326abfa4689 | -9.0432 | -50.4576 | 2025-09-07 00:45:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b09e74-4578-3c7e-93a4-cf4f574ab623 | -12.5361 | -48.077499 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b11821b-4a44-32fe-bfac-837b1160baea | -9.5168 | -40.310299 | 2025-09-07 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| da75c93f-de24-38ca-94b7-250a0258a4de | -10.3684 | -44.971699 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c66d6b09-9f07-30db-a98c-7f941fb4eb30 | -7.6622 | -50.267101 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7bcd3d-3380-3baa-98ee-addb10897aed | -11.7683 | -47.5574 | 2025-09-07 00:45:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2916ba3-2cb7-3689-873f-367390df9687 | -19.466499 | -47.772701 | 2025-09-07 00:45:00 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 490af0dc-ef16-3d46-890c-63ca616f9085 | -6.2051 | -46.757099 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f0dbc4ef-5fa4-3089-a138-9b15562af1c9 | -7.7408 | -50.754002 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f6ce18e-ec18-3052-9c36-93ee8ec40105 | -13.035 | -48.050701 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c8716e54-fb95-3bc7-bba7-876c81f7e0cd | -11.5963 | -47.1675 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cde9bb29-b27e-35c2-9e69-486363cea8df | -13.7518 | -52.768002 | 2025-09-07 00:45:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71f8d807-9bea-3014-adbf-b10a2bfbfca2 | -11.0368 | -54.187801 | 2025-09-07 00:45:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 237fa08e-031f-322b-b993-44f9ee97be1a | -4.25 | -48.556499 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a65b78b0-76ee-3fc9-8428-b840d9daaa12 | -7.7267 | -48.8265 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 69677294-41c3-387d-91b2-7f517be1389c | -5.8228 | -44.141899 | 2025-09-07 00:45:00 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 25492247-f29b-3c5e-bfca-0b9647ab9bf9 | -15.6905 | -53.5555 | 2025-09-07 00:45:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 30254a97-6e94-3ecb-acab-65eddfc9f731 | -6.7969 | -47.080898 | 2025-09-07 00:45:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7224091f-6c2d-337b-8c64-1635fc9dd8eb | -12.5376 | -48.084499 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7caca3cc-2e23-3068-9e1d-3653b51f3ac6 | -9.4092 | -46.773102 | 2025-09-07 00:45:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2281bf6d-e9f7-3957-b77c-fda95dad4422 | -5.8299 | -44.128601 | 2025-09-07 00:45:00 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf4cea66-0bb2-309b-a7f1-d1f13d7af79b | -13.0268 | -48.059898 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 126e8bfd-8a90-3938-88bf-b645245db95d | -11.5667 | -47.758598 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3aa6ab9f-8af4-30bf-9acf-bc6be26bebea | -5.0332 | -45.329399 | 2025-09-07 00:45:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d99bd5cb-d7ab-31b6-b109-a905f9c50177 | -17.673901 | -44.514099 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed231e98-f1b5-3084-bc70-172575ad4592 | -18.0158 | -44.9161 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0fb0463c-5473-3f8e-96a5-4b918382920a | -13.8255 | -46.269901 | 2025-09-07 00:45:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80c147e8-3c5e-3ef7-8c6a-fe04411611e3 | -7.056 | -50.867599 | 2025-09-07 00:45:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e42e05-37a5-333e-bbb6-43ab597af7ca | -6.1704 | -45.427299 | 2025-09-07 00:45:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07b5f5ba-bddb-30a4-a609-3273b8792873 | -16.7705 | -51.3592 | 2025-09-07 00:45:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b84ef75f-187c-3552-ad15-8beba701385d | -10.7257 | -48.594601 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6ed4166-def3-3239-b07b-074573b1c48e | -7.0079 | -44.9561 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c74da41-a334-3982-8608-d5c989ce13fe | -11.0035 | -52.0466 | 2025-09-07 00:45:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 42aeb772-9212-35f9-9965-f9ef5634f1f0 | -14.6539 | -46.821201 | 2025-09-07 00:45:00 | METOP-C | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| beea6073-7a38-398b-8252-e52dc0c72e04 | -6.8 | -52.808899 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2da95010-10f0-3fca-a374-07cefc8d2c08 | -11.5765 | -47.756302 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82b4ad73-c530-3fd2-ad07-a49d4d297738 | -7.669 | -47.324001 | 2025-09-07 00:45:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07dc871e-1f50-340c-8b52-cb5271a15686 | -9.5212 | -40.327599 | 2025-09-07 00:45:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 64db8f76-a87b-3840-97f2-b606e05b51da | -5.9751 | -44.175098 | 2025-09-07 00:45:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
