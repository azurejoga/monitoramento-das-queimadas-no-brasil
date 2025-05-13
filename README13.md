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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0f2c683-4f15-3493-80fb-fd64254c3c7d | -9.97298 | -48.50418 | 2025-05-13 12:38:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 2a553fca-ba61-39ab-adcd-1d395fdc7f7c | -8.07207 | -47.13985 | 2025-05-13 12:38:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 83f98dc1-0db6-3b89-ae6a-c0edbe6eb166 | -6.97393 | -42.78204 | 2025-05-13 12:38:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 98.9 |
| 442ef4c6-197f-3457-8a22-20e5a361e763 | -8.93973 | -44.22973 | 2025-05-13 12:38:00 | TERRA_M-T | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 94b52b3a-045d-31e6-adcc-1b7ed53b4f98 | -10.48522 | -46.18018 | 2025-05-13 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d4d2bead-37ff-3d70-b7b8-08b1990f9613 | -10.49593 | -46.18161 | 2025-05-13 12:38:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 2c538bf9-6ad6-371e-9f1c-eda5c373a2b8 | -7.5902 | -45.86817 | 2025-05-13 12:38:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 70ab8a7c-ee9c-3aa2-a959-94b04aea1419 | -10.04984 | -49.66473 | 2025-05-13 12:38:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2513dd12-5e8d-34d4-ac2d-2ceb161d5c69 | -9.67397 | -49.71514 | 2025-05-13 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 496ae880-3bc0-380d-9b6c-17e86f372a64 | -9.67526 | -49.70616 | 2025-05-13 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c61e9ffe-5231-38cf-81a9-e716df853ffb | -9.6651 | -49.71388 | 2025-05-13 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 47d6e0e9-ede6-376a-bc46-b104bad3e6d3 | -6.95022 | -41.11848 | 2025-05-13 12:38:00 | TERRA_M-T | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 52e2f1cd-b909-3976-9699-1eab7ec83f4f | -13.9902 | -56.8058 | 2025-05-13 12:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 4edc36bd-f499-3a71-8c9d-4128f093cab2 | -10.63047 | -46.27233 | 2025-05-13 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 1e580d79-c442-3973-95c6-5df96b79e732 | -11.55351 | -47.61253 | 2025-05-13 12:40:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 349ae64c-2d7a-3c19-a87e-4aa326012077 | -10.45468 | -49.08328 | 2025-05-13 12:40:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 86f4e31e-6126-3f5e-afe1-1b7eeaafad32 | -11.33478 | -48.09967 | 2025-05-13 12:40:00 | TERRA_M-T | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 301ce37a-f8c4-3e3c-9f64-a4b65c462f04 | -12.10821 | -49.31042 | 2025-05-13 12:40:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d5a1d8f2-d4c6-3e08-b583-4eca138bfdda | -11.50874 | -48.59364 | 2025-05-13 12:40:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 809bf80c-a58b-3599-9cf8-a7960b41f77e | -11.61334 | -48.00547 | 2025-05-13 12:40:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 65b6b7c8-06be-3bd0-8d6d-a0a16182bddf | -12.49613 | -44.49585 | 2025-05-13 12:40:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| ee407a15-e8c9-3177-9382-1577b6043988 | -12.76416 | -48.95105 | 2025-05-13 12:40:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 7d24ce97-380e-3be2-99a4-aa87d71a478e | -11.46853 | -49.34093 | 2025-05-13 12:40:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 002830cc-7a19-3009-8106-1fd51dcf4145 | -11.96926 | -44.00432 | 2025-05-13 12:40:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 7ac4f13d-8c60-3bc8-9fd6-f0bfc2006216 | -13.2395 | -49.84798 | 2025-05-13 12:40:00 | TERRA_M-T | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 782c988f-2ea6-3aa1-96d9-d3cad39034f7 | -13.56603 | -52.8717 | 2025-05-13 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 71805447-7663-30d8-8bd3-dad93516877c | -13.56457 | -52.88152 | 2025-05-13 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a8d17c0b-79d5-36b6-a55b-281db0ae657c | -11.98436 | -49.66859 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 90b73eff-526d-3596-b3ae-b67abea64533 | -11.98175 | -49.68708 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| ed534c46-e4c8-34f7-b130-24e466136e4a | -12.21188 | -49.62456 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a28904d8-7125-3d15-877d-45e629beb1dd | -10.45598 | -49.07394 | 2025-05-13 12:40:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b72fb934-21e2-3b4e-a629-f7bd6456fb5e | -10.62556 | -46.26403 | 2025-05-13 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 6180342d-6afc-3e14-9a52-7d81c2b29c76 | -12.49373 | -44.51526 | 2025-05-13 12:40:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.6 |
| d2aed606-96cd-307c-9897-4fe7440789ef | -11.46984 | -49.33156 | 2025-05-13 12:40:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1ac64293-eac9-362f-b362-43073c979c14 | -10.62158 | -46.25761 | 2025-05-13 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ba1b41a9-8df2-3745-adde-ddbaa3c15926 | -11.07551 | -46.12708 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 78ec9455-0204-3a78-ba50-92e23de18083 | -10.74524 | -49.89585 | 2025-05-13 12:40:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1d93f458-f627-38c4-97ca-5ebb935e1390 | -12.7655 | -48.94115 | 2025-05-13 12:40:00 | TERRA_M-T | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| b7c8aaf7-80bb-3c21-a7da-2dc8521ec5ac | -12.15474 | -48.00617 | 2025-05-13 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| f9f78650-e6d2-3df9-a5de-3792a511025d | -11.97148 | -49.69505 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 385.7 |
| 13fb9be4-b975-3b60-9b03-7f9a3a1535f5 | -11.97278 | -49.68581 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 25f37289-1a45-3690-90cf-d56adf0d0bb6 | -13.04954 | -53.71898 | 2025-05-13 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| c173476f-11dd-399f-adb6-a2dcb5a83ce0 | -12.52327 | -54.73443 | 2025-05-13 12:40:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 5fefda5f-ba1d-3058-ad11-49d8f319a22c | -12.63902 | -54.05476 | 2025-05-13 12:40:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| dfd10dfe-7c21-37b0-8509-43c01591ee1c | -11.97018 | -49.70428 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c644a62c-ea12-35b1-af2d-1dd0cb6bbd22 | -12.49674 | -44.50152 | 2025-05-13 12:40:00 | TERRA_M-T | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 5736c7ea-5c10-324e-ad10-ba11cd6c2343 | -13.57244 | -52.87866 | 2025-05-13 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 5fe3cc17-88dd-339d-9d54-ee711f9d2317 | -12.63725 | -54.06634 | 2025-05-13 12:40:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 13f53ca6-db37-350c-940e-1a6aa0fee6f5 | -11.7775 | -48.69601 | 2025-05-13 12:40:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c3ad0af7-9c93-384e-838d-34bc63459cbf | -11.07734 | -46.11303 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| eebd48cc-5422-39db-8aa7-38bc2115e9bb | -11.70619 | -48.82095 | 2025-05-13 12:40:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1b6c47d9-2103-39bf-9334-17fed0f6fbe2 | -11.51012 | -48.58369 | 2025-05-13 12:40:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9bb92883-9d0b-3db7-b749-7acd4b8610ff | -14.18972 | -45.47774 | 2025-05-13 12:40:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| e4b2841d-da6f-3de6-b9ef-e918d0b0b7f0 | -12.34956 | -49.95783 | 2025-05-13 12:40:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ccc7b550-a033-366b-bbf5-87f32fb99483 | -12.21318 | -49.61523 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d62127d3-973b-388b-b422-df694a338498 | -12.35085 | -49.94868 | 2025-05-13 12:40:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c8185ae-559a-3242-98a8-ba5cf3123875 | -13.57395 | -52.86884 | 2025-05-13 12:40:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| de8b6e06-1cdc-32a0-b412-cfb07672e60a | -11.40365 | -52.951 | 2025-05-13 12:40:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0fd63de1-9657-35f9-9c1f-f0a13f179bfa | -11.98045 | -49.69631 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 370.6 |
| 95cc7aac-6f6a-3925-af8a-ddb44aeba17f | -12.15331 | -48.017 | 2025-05-13 12:40:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a73e8337-98c5-318c-a378-43ccb2417522 | -12.29663 | -43.54995 | 2025-05-13 12:40:00 | TERRA_M-T | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 6360f5eb-e9f2-3b6c-8116-7d87e8b664f9 | -11.98306 | -49.67783 | 2025-05-13 12:40:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8a8f43a1-f914-39f9-8f48-f76104e09b1d | -13.04787 | -53.7299 | 2025-05-13 12:40:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 310490b6-09f9-3ce4-89a2-6abd2de41ef1 | -10.48691 | -51.67643 | 2025-05-13 12:40:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 575448f5-e5c4-3e30-92e6-2cd692f5b301 | -11.58304 | -47.61648 | 2025-05-13 12:40:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9b4a7afc-5aed-37b1-a21e-35a02f580356 | -12.18023 | -46.71717 | 2025-05-13 12:40:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9161352f-a7a4-3258-bb73-77eeaef09afe | -11.39576 | -52.93919 | 2025-05-13 12:40:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e910ec8d-e928-3bd4-b642-8fe3eeaf5f1c | -12.18194 | -46.704 | 2025-05-13 12:40:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d772c471-41ce-3b75-9ce2-3cebc01f5847 | -10.61982 | -46.27085 | 2025-05-13 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c83a287d-d7bf-38af-bf67-165a12a41ea1 | -10.62389 | -46.27726 | 2025-05-13 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 476daf0c-6c04-39ec-95b0-838e47abeba0 | -11.70485 | -48.83077 | 2025-05-13 12:40:00 | TERRA_M-T | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c726ef6-a53d-3acb-bb87-0090450a0859 | -10.63224 | -46.25913 | 2025-05-13 12:40:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bef3c106-d308-382f-8f7b-69cac7e44bad | -13.40684 | -47.63295 | 2025-05-13 12:40:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0c5958b8-0348-3578-acd2-ee1422309062 | -16.60436 | -53.4026 | 2025-05-13 12:42:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9afff24b-2d7e-3c5e-98cb-bf9d0d14e8a9 | -15.23569 | -51.04772 | 2025-05-13 12:42:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7d8318e3-c55b-3d30-963b-2cfa59224431 | -19.04752 | -52.85848 | 2025-05-13 12:42:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 69211540-cefd-33d6-aeb7-3a45ebde23ac | -13.98696 | -56.803 | 2025-05-13 12:42:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 557bf8d8-3d47-3404-8e54-3f49eb00888f | -13.96976 | -55.05859 | 2025-05-13 12:42:00 | TERRA_M-T | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 87898b33-5938-36ee-973f-30eb6ea4f675 | -16.60584 | -53.39278 | 2025-05-13 12:42:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 19daf3c8-ae54-3da1-8cbe-dbfe70f936bf | -16.95505 | -53.52425 | 2025-05-13 12:42:00 | TERRA_M-T | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6cead1c5-c81c-32d8-819b-7a0302a841da | -15.39266 | -48.43342 | 2025-05-13 12:42:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 950a5d71-23c2-37ac-9836-7bba5faa3b83 | -15.39504 | -48.4286 | 2025-05-13 12:42:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a153cf63-98e5-3fb9-96d6-79f4c82f5578 | -18.8084 | -51.63563 | 2025-05-13 12:42:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9a1b80a5-5e81-3b41-9f68-37bbd0863afc | -14.54084 | -53.84117 | 2025-05-13 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| cbc3db32-2ecf-33d8-886f-43547d291607 | -14.55041 | -53.84261 | 2025-05-13 12:42:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 7a015e37-67a9-3dcd-9891-43eb2c341476 | -23.13368 | -52.36951 | 2025-05-13 12:44:00 | TERRA_M-T | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5281fa11-5d52-31d4-9798-c9a35a3883fd | -30.66644 | -52.78476 | 2025-05-13 12:44:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 4.8 |
| 68346975-52b7-3b1c-b84c-17388d62ff46 | -21.72705 | -55.37548 | 2025-05-13 12:44:00 | TERRA_M-T | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d3569949-b8c8-374b-b17c-8c875cb021be | -22.64449 | -54.28278 | 2025-05-13 12:44:00 | TERRA_M-T | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| dfcc7b34-5f0e-35bf-8010-7d76b4f770a4 | -13.9902 | -56.8058 | 2025-05-13 12:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 54a5b5f5-b6c2-33b1-8c88-f4dabd79e452 | -11.8218 | -49.724 | 2025-05-13 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 9ee5a8a3-d946-3836-a9f5-cb6d1d28b803 | -13.971 | -56.8077 | 2025-05-13 13:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| d4918e88-64d5-3e41-84f4-3416243b66b9 | -13.9902 | -56.8058 | 2025-05-13 13:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 11af3ba4-9bb7-3144-b6e8-472ba88e146e | -13.5683 | -52.8783 | 2025-05-13 13:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 688c19eb-1ff1-3cb3-9890-4cc3f8111382 | -10.494 | -49.7022 | 2025-05-13 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 8f95a7b1-c668-3d57-bf71-86dbbbecb1cf | -13.5683 | -52.8783 | 2025-05-13 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 95ec2934-2ed3-356d-b9a6-c16da3793816 | -13.9902 | -56.8058 | 2025-05-13 13:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| e4ed0c4a-e075-3e67-ae48-cd3163933a4f | -13.9902 | -56.8058 | 2025-05-13 13:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ac01c751-19a9-36bf-b909-b5205f94d44a | -13.5683 | -52.8783 | 2025-05-13 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 30a76342-2512-3d21-becb-7dbe602f206f | -13.9713 | -56.7874 | 2025-05-13 13:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |


[Clique aqui para ver as próximas entradas](README14.md)
