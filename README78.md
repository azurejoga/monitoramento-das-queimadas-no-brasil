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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44155dbc-8422-328a-bb22-59e106c8b3ce | -6.78628 | -43.78118 | 2025-08-30 05:55:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 29.7 |
| c7924a98-9042-37aa-888d-d781c58f80d7 | -7.71846 | -50.27288 | 2025-08-30 05:55:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 03e991ec-32c3-3138-816e-5c04fa6f3096 | -7.15164 | -44.91207 | 2025-08-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d190340b-3bc6-3e23-9fca-a43464f5dd77 | -7.09939 | -44.31032 | 2025-08-30 05:55:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3c867171-8239-3f2d-97a1-ef0745748d01 | -6.18274 | -43.9978 | 2025-08-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ac137ea6-2823-3fb7-bcd5-47a48194c4be | -6.08778 | -43.99421 | 2025-08-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d0ece7da-f369-3c07-927f-399066401531 | -6.41233 | -45.6042 | 2025-08-30 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 81c84ecb-75f3-3693-a63b-4f074ebbdfa4 | -6.49287 | -43.5396 | 2025-08-30 05:55:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 74cc4c50-67cf-3017-8760-8ab2f355a0f3 | -6.18353 | -43.33345 | 2025-08-30 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 8f367de6-f258-3516-99a7-a40c0411858f | -6.19242 | -43.99923 | 2025-08-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 81e13b96-1c4d-3fb8-81c4-13c0ef74baf6 | -6.41368 | -45.59497 | 2025-08-30 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 062101da-1273-34b1-a74b-825eb18e4f5c | -4.9885 | -38.59404 | 2025-08-30 05:55:00 | AQUA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 30.8 |
| f6f0e43f-a97f-3baf-8eba-903947ad1525 | -6.77636 | -43.77976 | 2025-08-30 05:55:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 4c3afc41-3cc1-3844-ace0-13e8e25454b6 | -6.78789 | -43.76981 | 2025-08-30 05:55:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b752e8c1-a698-3a06-a9a9-a98156eb9ba3 | -6.77796 | -43.76839 | 2025-08-30 05:55:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 04c064c9-8f98-3dfc-a17a-1884ec5abc1b | -6.17455 | -44.19318 | 2025-08-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41625270-4cf2-3218-a0e3-f19cd4f37c9e | -6.42131 | -45.60548 | 2025-08-30 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| b05b0f2d-971b-35a8-8852-1cbd2c8be98d | -6.41098 | -45.61343 | 2025-08-30 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b8cc3dd-405f-377d-aba5-0d1a9bc55460 | -4.98944 | -38.60131 | 2025-08-30 05:55:00 | AQUA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 27.7 |
| 6d2daf4a-0196-3033-abdd-e2d1a6c8b4f6 | -9.5336 | -45.84602 | 2025-08-30 05:55:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| f8855c54-f429-3f3f-997d-5f6d7a0fed8f | -5.81713 | -46.36717 | 2025-08-30 05:55:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9e060253-7d26-34ba-aaf9-f9598c4fa94f | -6.18418 | -43.33896 | 2025-08-30 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 28520a46-8681-30d5-8daf-157c6b4da2b6 | -7.58227 | -45.1251 | 2025-08-30 05:55:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 86e2a17f-5675-34e9-b2bc-05d5bf7a8973 | -7.78001 | -45.46875 | 2025-08-30 05:55:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 10abcca3-b7dc-3861-8958-b0370f63e8e1 | -6.52236 | -44.84557 | 2025-08-30 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 405dafe2-e7af-3d2c-b176-270f3ffeefe2 | -7.1531 | -44.90215 | 2025-08-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c26545ff-b25a-355d-b182-434435eeae95 | -6.764 | -43.7838 | 2025-08-30 05:55:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d755025c-64f7-3b13-b3a0-17849e12491b | -7.3994 | -45.92733 | 2025-08-30 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8b3d6ffc-f487-3892-83fb-7fcd5a5e8c4c | -8.45374 | -43.63308 | 2025-08-30 05:55:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6d0038f1-7ead-3ba2-a466-1ac6b723ddf7 | -6.1852 | -43.32143 | 2025-08-30 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| a7b8b2fc-7a5b-3ab9-a20c-eb7c03819908 | -5.82724 | -46.35968 | 2025-08-30 05:55:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 61b24c12-6082-32d4-b99a-4175673df0ba | -6.5302 | -44.8568 | 2025-08-30 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 64cd95a6-aeff-301c-ab0e-6164a174fde4 | -6.52094 | -44.85543 | 2025-08-30 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 214d36db-1a9c-3b23-a254-ca04b0d01667 | -7.73004 | -50.26328 | 2025-08-30 05:55:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 17051a86-a727-3a62-8829-618c8e37227a | -14.02226 | -44.54592 | 2025-08-30 05:57:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| b22a1fde-2442-3720-8798-71f319684056 | -11.82545 | -46.45776 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| af97ec24-0994-3f21-b5d0-e3bd6f75a6f8 | -12.84884 | -48.16103 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b6f64261-a041-3a28-a40d-b0e19e186747 | -11.88276 | -46.44642 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 52a86b1e-c699-3c34-94a2-62a627b7ee8b | -13.67389 | -46.88313 | 2025-08-30 05:57:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 17120169-3874-305a-8fd2-7ee40d3e828a | -12.93077 | -48.10691 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a3d9b96-5a0c-3189-8f0a-38591595ae59 | -10.66498 | -48.73546 | 2025-08-30 05:57:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 072726c4-e5d9-34db-8618-0e13b119348e | -12.92009 | -46.35712 | 2025-08-30 05:57:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| bef0bce1-41d0-37d4-bb49-b55a25ddd006 | -13.38685 | -46.95754 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 89ad252c-1de2-35b6-883f-f9185eb617f8 | -9.69771 | -47.05222 | 2025-08-30 05:57:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9af628c8-2140-3c91-a458-2026319035db | -10.022 | -48.04516 | 2025-08-30 05:57:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7a63f646-ef32-3f0c-aaa3-17a3b2ee0618 | -11.83591 | -46.4495 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 74991f44-8567-3c61-87b7-49ded6a7f2b2 | -15.16707 | -52.32674 | 2025-08-30 05:57:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 78d858c8-1844-3551-a387-38e6f876e507 | -9.70783 | -49.47093 | 2025-08-30 05:57:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 12410544-484d-346f-aa62-b54a48d432a3 | -13.57968 | -46.90051 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 78c7b520-4cb9-30b1-9252-b59c4e99e37d | -13.36197 | -47.00199 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 196.3 |
| 72f3b84f-5e2e-3843-ab5d-7ad04f4715d5 | -13.6034 | -46.86478 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a036b5e5-9616-36d8-8aa5-6c42a0cda50c | -11.84405 | -46.39261 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 983fcf74-d5db-303b-9609-cbf7b5a93d06 | -10.64816 | -48.65274 | 2025-08-30 05:57:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3da1c14-877c-3540-a5eb-9b192a646729 | -11.86366 | -46.38553 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f18924c1-b4b9-3f1b-a703-cca40247e3bb | -11.82682 | -46.44818 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 55d1eb4c-b6e5-3d54-b63a-6b2afd9181a9 | -13.38547 | -46.967 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c7278a1e-f902-3826-b512-61632e1621d8 | -11.87416 | -46.37718 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 1996362c-7d43-31a1-82e1-1ee56661ca82 | -10.36629 | -46.091 | 2025-08-30 05:57:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4d0e2eb1-976b-374b-b575-d693f7c32952 | -13.46932 | -46.95776 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c54746aa-3749-36f6-a258-d6e380f97f92 | -13.36962 | -47.01275 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 131027ea-bb27-3df5-ae68-db87c8890e93 | -10.02406 | -48.09092 | 2025-08-30 05:57:00 | AQUA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d2c59116-3732-3226-bbc4-b47b86a6ce20 | -13.36937 | -46.88681 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 242.5 |
| e549004d-3d47-3d82-84f8-e60ba1092b7c | -13.98407 | -46.31991 | 2025-08-30 05:57:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a2ae8ace-f75a-3c9c-b200-5f5c5bac14e5 | -11.88197 | -46.38762 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| e94791cd-51c6-37ba-92ac-0a12869b732b | -15.16464 | -52.33325 | 2025-08-30 05:57:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 105c1647-4813-3719-82e4-9c4fd614b9a7 | -13.35395 | -46.86539 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 0fdc6ff9-b00e-3c68-b76a-e2a791426d94 | -12.01331 | -43.97561 | 2025-08-30 05:57:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 2e7a2943-71d2-3b44-96df-b98cd2eacd6e | -10.0329 | -46.03695 | 2025-08-30 05:57:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 97bcf744-b891-397e-93ea-6ccad60144f1 | -14.0205 | -44.55876 | 2025-08-30 05:57:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 1888f4a9-5e9a-36cb-9d59-7433e40a9732 | -11.83455 | -46.45901 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 9bcbcec7-0b8c-3a6a-afb3-90d9f1ac5cb5 | -15.10288 | -48.1632 | 2025-08-30 05:57:00 | AQUA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 718de358-963f-3893-8494-c59e7c32af6d | -14.62557 | -48.07162 | 2025-08-30 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c00f37cd-8c83-3fd3-b811-f07cb5f51a15 | -15.1667 | -52.32107 | 2025-08-30 05:57:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6e20b9e2-7735-345d-b86b-e041cbe2ab53 | -13.4152 | -46.9491 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c7ed5be7-1029-3d6f-9d19-01aa7cc89d03 | -12.69589 | -48.14107 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 76194452-97d7-3b81-996b-b0d84f3ae42e | -13.47068 | -46.94835 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7a7b1d5-9a1e-3d9a-8d31-b70b4cce5dae | -13.97477 | -46.31825 | 2025-08-30 05:57:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eb034184-d145-3abd-85bf-e071497531d5 | -13.39584 | -46.95913 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| de5a846d-fcab-3d0a-84e3-5ec4170aa397 | -12.93688 | -48.12619 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 44142f77-6528-33b5-afc2-3ababe00cb30 | -11.87282 | -46.38652 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 7c5c2e7c-01fc-3ef2-8c4a-f9e8f0c02fe5 | -9.70936 | -49.46123 | 2025-08-30 05:57:00 | AQUA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa36643c-0fe9-3afd-9582-8f6861e3a84f | -9.69347 | -48.30817 | 2025-08-30 05:57:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 394d25a6-3a43-3cb9-9ad2-3a11cc319b69 | -12.92943 | -48.11589 | 2025-08-30 05:57:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ace1d76b-59b3-3f82-a8aa-7112d2e93715 | -13.3849 | -47.03427 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| fdff1d35-7bbd-3d31-8802-8637a7cf853e | -13.39177 | -46.98711 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 967c0330-59db-3a8c-955d-108e1c823551 | -13.6317 | -48.18119 | 2025-08-30 05:57:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| af20140d-4cee-33a3-82c0-cee9bad45f1f | -13.37233 | -46.99409 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 454980db-94a9-393d-9556-52cd8cc2dc3f | -14.61678 | -48.0701 | 2025-08-30 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6769fd4b-642f-3324-9fb6-6d390b2f2bd9 | -13.36606 | -46.97371 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f1c2611-cff7-3403-83ed-e5ab19b8c363 | -11.85318 | -46.39377 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebbe380a-6671-32f9-aca0-b67241d1f79b | -11.00391 | -46.96495 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 483ba1cd-3c8b-32c6-9373-e450e585f404 | -13.36163 | -46.8763 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8a1bc500-3906-31b8-86fc-ed3ee1214b66 | -13.38412 | -46.97633 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 689b27ec-c4d3-3b65-8d3c-12dabb99e853 | -14.61543 | -48.07918 | 2025-08-30 05:57:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 866aa805-9882-3038-b357-092954398638 | -13.3647 | -46.98311 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 70c76e61-559d-3f12-b5ba-3e6e300b7450 | -13.96259 | -46.33731 | 2025-08-30 05:57:00 | AQUA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 9bf89356-f918-3dd6-890a-9dfc0349edac | -14.25432 | -45.23573 | 2025-08-30 05:57:00 | AQUA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d4e2a9f8-3942-30bc-96e8-cbfcc7634a32 | -11.83727 | -46.44003 | 2025-08-30 05:57:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 24f3e25e-2cbc-33b0-a419-f4011b4bc57c | -11.07006 | -52.03928 | 2025-08-30 05:57:00 | AQUA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b61e5690-be7a-3855-850f-0d99d09ab478 | -13.37071 | -46.8775 | 2025-08-30 05:57:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 48.4 |


[Clique aqui para ver as próximas entradas](README79.md)
