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
| b0b2d2a4-544c-33d2-bd45-498cfe2fbb4b | -9.73873 | -48.28726 | 2024-10-13 00:37:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9f26834f-c0f3-32a2-9513-fabd9565c8c7 | -9.73281 | -46.95752 | 2024-10-13 00:37:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 21167bc7-fc89-37a2-9913-29ada080ef61 | -9.73123 | -46.94505 | 2024-10-13 00:37:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e59d3d4d-cf67-30be-b366-7c225ca721e3 | -9.70813 | -47.77489 | 2024-10-13 00:37:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 87823467-77d8-39c1-b3df-0dcacc263228 | -10.1662 | -48.04472 | 2024-10-13 00:37:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e01d9e77-0b8d-3816-9fe7-951318e77b40 | -10.32129 | -48.80447 | 2024-10-13 00:37:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0ae397e4-6fab-3428-bdc5-867e974f8492 | -10.32601 | -48.798 | 2024-10-13 00:37:00 | TERRA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 659d5740-c25d-386a-885f-a4dba7d7843b | -10.5314 | -49.96484 | 2024-10-13 00:37:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 22a054b6-e5c0-366e-b5a3-c4ef8274ad69 | -10.53407 | -49.98675 | 2024-10-13 00:37:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e711e39c-e94b-3e58-bc70-7ddfa56e27f7 | -10.53674 | -50.00874 | 2024-10-13 00:37:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 30.6 |
| acabcb9b-66a2-3377-8505-c1e4ea1059a8 | -10.63776 | -49.89579 | 2024-10-13 00:37:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e32f4a5b-8514-3c21-a28d-8cc6c8acc859 | -4.40782 | -50.57375 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 2eac8767-2519-332f-b57b-66efa0736622 | -4.40183 | -49.76902 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bf4bf275-cc5c-35c7-ab16-f8591309906a | -4.39678 | -44.48233 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d1534ad0-051e-3b58-94a0-551bf14f0fea | -4.39612 | -49.76337 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 1cff39ad-2215-3e1a-b24d-0f66b8462305 | -4.39555 | -44.47352 | 2024-10-13 00:39:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 86bc2749-b188-3ffc-9a30-ce4f339919b7 | -4.36229 | -50.82036 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 31e5e6ab-3a8d-3f30-8daf-4f0ef651f074 | -4.36094 | -50.80665 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 79e507e4-7b47-3d5d-b23c-7d21a60b3e15 | -4.35968 | -50.80015 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 16a55b51-71cc-3324-a41e-11413977ee9c | -4.34749 | -45.58648 | 2024-10-13 00:39:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 76338e25-71f3-3d27-85d3-d74560b4a8cb | -4.81445 | -42.72329 | 2024-10-13 00:39:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 1ca4348f-d909-36d6-ab11-301bcefa689e | -4.3306 | -46.73271 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 53893f9b-cbf2-3c16-a593-fa5de5da618e | -4.30832 | -45.36899 | 2024-10-13 00:39:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ccbdabc1-55cd-3feb-a1f5-0773ad54d7ae | -4.29937 | -45.37025 | 2024-10-13 00:39:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8a5bc60-a5ce-3679-9bbc-a617254de3f3 | -4.28759 | -47.30745 | 2024-10-13 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a1f9cef2-1a7c-3261-9258-e6954894c7c7 | -4.28612 | -47.29655 | 2024-10-13 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| aaa576f4-908f-341d-b09d-104d78a4d072 | -4.28224 | -48.63487 | 2024-10-13 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4ff45dbe-6d94-3ada-be1a-ccb7cfc8ed22 | -4.27586 | -50.96299 | 2024-10-13 00:39:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 25bcb0be-6abe-3d97-8149-1afa50ae5bdc | -4.1642 | -45.79427 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c9f40e44-f4c6-31d2-a59e-0cc35ba82778 | -4.16293 | -45.78495 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 1e6843cf-f2bf-3958-aea9-15bfca06a1a7 | -4.16165 | -45.77565 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 621f496e-2cde-37e0-ba55-2c2ab1270926 | -4.15387 | -45.78624 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 41466741-22b1-3418-b0c1-894a0c7402dd | -4.1526 | -45.77696 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d244d6e3-7cfa-3f9e-a0e9-206829f85487 | -4.12679 | -51.12122 | 2024-10-13 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d4e49c92-cea0-38d0-b63e-1be52beb7b1e | -4.12081 | -48.27547 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 1148f9ae-3a96-337c-b3d7-af7cb0b08d22 | -4.11741 | -48.24978 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 361d9627-01f0-3221-a746-2b70e7d3b219 | -4.11575 | -48.23732 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 230.6 |
| b5e90aa0-40d8-3d52-8024-5aa0440c0abb | -4.11536 | -48.28199 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 08147a21-8ede-31e9-9263-0038d5aba790 | -4.11178 | -48.25634 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| caefa38a-7693-3a1c-83cc-b555522f075f | -4.11034 | -48.27702 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 3bec58c9-4899-3c33-a5f5-c3b6231c6651 | -4.11002 | -48.24368 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 69695cb8-bb3f-3ccb-8fb6-5b08258e6ffe | -4.07716 | -47.25923 | 2024-10-13 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 60f3122f-8247-3795-96c6-e6dc1e4aa4e7 | -4.07571 | -47.24846 | 2024-10-13 00:39:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 87d582e6-6483-37f6-a95c-1521f36e3b5d | -4.06951 | -44.05328 | 2024-10-13 00:39:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8be8fc6-b128-322e-997e-b91459507551 | -4.0553 | -47.92588 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 393a049c-10d3-3424-8e27-7b17347075d9 | -4.05363 | -47.91383 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c092f6ca-bd49-339b-99ab-025ffed0e368 | -3.9589 | -47.97007 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 8325db60-d4d2-38ab-b805-b89e73831794 | -3.95725 | -47.95806 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4d428fef-8c9a-3d15-b3a4-ddd3ed59b367 | -3.94126 | -46.44268 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 70a1ca2b-692d-3f10-80ad-6b5732ac12f5 | -3.93989 | -46.43285 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 351cf79b-4c49-334a-91e7-9854bb223b54 | -3.9306 | -46.43418 | 2024-10-13 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 3af0b1c3-5856-35e6-b4f1-2e22737753a6 | -3.92081 | -48.36 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3ba83297-3e92-34b9-a7a6-cb020a9c49d7 | -3.91903 | -48.34716 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| aa048e0c-84fc-3620-b2bc-5ea685cdff45 | -3.9173 | -52.21435 | 2024-10-13 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| f511d876-1062-3750-abc7-e1ebbeb8d5cb | -3.91028 | -48.36145 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| fb276088-d6c1-3b46-9886-52470d6dab3b | -3.90851 | -48.34851 | 2024-10-13 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| b029adc1-8e05-3bbb-a42a-57213b19ac67 | -3.89526 | -45.98333 | 2024-10-13 00:39:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 52148ca5-8603-3bf9-bde0-c0c9581698d6 | -3.77591 | -50.15487 | 2024-10-13 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 339db25c-cdb4-379b-8d84-b018ed49a8d3 | -3.73189 | -44.66382 | 2024-10-13 00:39:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3a95af9-f0d0-3ffb-b032-025fdb57c2f6 | -3.70376 | -50.11806 | 2024-10-13 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d5ec8852-8204-37f2-bac5-61563900ef5c | -3.69168 | -50.11964 | 2024-10-13 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 654fff41-945f-3892-8788-344529c906d5 | -3.61021 | -47.51712 | 2024-10-13 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| c295bd55-b382-30aa-973e-0066e64fd55f | -3.58076 | -51.5237 | 2024-10-13 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 75b0c2ea-1d9f-3829-a8bb-945ed44d7868 | -3.51393 | -45.48897 | 2024-10-13 00:39:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4947958c-8ed1-31df-b050-4a6fb5351a82 | -3.46471 | -51.54596 | 2024-10-13 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1343d7bf-0c9c-3d36-b86c-5d83e765cc5a | -3.367 | -45.1602 | 2024-10-13 00:39:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e118a67-f078-393f-ba2d-612ed769d514 | -3.34955 | -47.32036 | 2024-10-13 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 4428d3ed-191d-33ca-b18c-69cefb5e3457 | -3.34809 | -47.30958 | 2024-10-13 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 8fa5c13b-d9d6-31d7-b0bc-7d39d35dce94 | -3.33117 | -49.15842 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f17ffa4f-9bd6-3b0c-aeda-0f27e9ae0925 | -3.22074 | -48.93647 | 2024-10-13 00:39:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9fc19f19-e584-30e2-a7e1-46a5ae1e21a9 | -3.21888 | -48.92272 | 2024-10-13 00:39:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| ba53a97c-b787-313f-b5d4-eb50ea9044a6 | -3.20112 | -45.03326 | 2024-10-13 00:39:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c615434b-9b89-3a4a-8e3d-1aac61a49783 | -3.13506 | -48.9826 | 2024-10-13 00:39:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 35ae8782-2582-3bab-8a91-18922c3966c6 | -3.09983 | -44.50037 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 6a0657bf-afb1-3e77-8080-1f9850934c0b | -3.0986 | -44.49158 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c7fa823e-c54f-35b3-8fdb-78ce9e1d5593 | -3.08517 | -47.78697 | 2024-10-13 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a85dab20-10e9-3609-bd3c-54eaf84e1d84 | -3.0836 | -47.77558 | 2024-10-13 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6b915de8-12fb-39ff-96c9-dacfc0867841 | -3.07029 | -45.9446 | 2024-10-13 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da1d7adf-f69d-39b2-b3d3-4b25bfdebfc9 | -3.04835 | -44.4539 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ed007355-9753-3e78-be51-c5fa914bc4d6 | -2.96543 | -47.37124 | 2024-10-13 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d4daebb3-40a8-3159-bfed-0a79dccfd8d1 | -2.96394 | -47.36055 | 2024-10-13 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9c05e7d0-91da-367c-89cb-b82168d7df22 | -2.79364 | -45.61123 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7b26e825-ebbb-36ef-8f10-0b9ff7773b3b | -2.79239 | -45.60224 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 13.8 |
| fcfd2005-6ce1-38c5-944e-aed4f24adb7e | -2.60218 | -45.49471 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7ff479ec-8fa1-3053-9cb6-562d2a954aa8 | -2.60094 | -45.48578 | 2024-10-13 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2495417d-b97d-36af-ae70-d93a431605d2 | -4.08865 | -43.91838 | 2024-10-13 00:39:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 36.2 |
| acfa975e-0c3c-302f-992e-b602df9b45d9 | -3.87343 | -40.64025 | 2024-10-13 00:39:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 025a579b-5ead-34ed-ab59-b80e4adbc622 | -7.7112 | -43.20022 | 2024-10-13 00:39:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 35278278-1436-324d-88c5-962c8c1fe745 | -8.07368 | -44.8181 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 834d5d1a-e8f2-3cdd-b83f-634fd0c46a3b | -8.72547 | -44.12836 | 2024-10-13 00:39:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 34.5 |
| b4dcdbd5-76b2-3e83-8771-91146e40aa0d | -8.69528 | -45.26513 | 2024-10-13 00:39:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| bd4a50d5-86d6-35ed-8953-7e8f0decd634 | -8.13732 | -43.01667 | 2024-10-13 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| e919199b-f191-31d2-b2c4-d7617b9e23e5 | -8.13606 | -43.00774 | 2024-10-13 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| fc5ecda7-085b-3db1-8a2b-6ad5eeccdc4e | -8.12846 | -43.01796 | 2024-10-13 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7ac972f1-1d27-34af-936c-0716ec2c281a | -8.12721 | -43.00905 | 2024-10-13 00:39:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 02acd7d6-9742-3b6d-a9ad-3eba3e5433bf | -8.07491 | -44.82719 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 3fa73a14-6929-3b03-b774-8c63d4b6126c | -8.06588 | -44.8284 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 76ed3e2b-6d65-3114-a9ed-a7fab25aa110 | -8.06465 | -44.81931 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| b1558b28-affb-3326-97a8-be8a19e4ebb0 | -8.06342 | -44.81017 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a72c798-1a39-33d5-806a-6b13a6257470 | -8.05628 | -44.82611 | 2024-10-13 00:39:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README8.md)
