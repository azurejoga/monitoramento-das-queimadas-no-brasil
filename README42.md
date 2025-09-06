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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce12d98c-8d89-3aaf-8ce1-af32fc19d8d0 | -7.13341 | -45.49234 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc75690f-a4de-3ba3-808a-ddbd486dfd52 | -7.09218 | -43.88224 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54987b00-e371-359c-9253-9fb669ef085f | -13.05243 | -47.10629 | 2025-09-06 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2265c4c-b596-3c4d-830d-a744fe9e498a | -14.57219 | -48.02971 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3357f4a4-cce3-3476-91cd-b3218ab71350 | -7.0074 | -44.95097 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61e46f4a-02c8-369f-b072-d4838e0a366b | -6.87483 | -52.78736 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9cc1d0d-9a66-3091-abba-30177ff3d662 | -2.85138 | -49.50595 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ed98f182-d9d1-3201-927a-123a4ab10374 | -15.85238 | -52.28733 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f30e1a5b-0650-329b-b1d0-2e228af6c64e | -7.21415 | -43.98779 | 2025-09-06 04:17:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b88ef9-23e1-3f5f-a3a5-bc52f171b186 | -6.15489 | -43.18287 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7edd0448-186f-3b50-a010-7c496e969cc7 | -4.45119 | -44.13943 | 2025-09-06 04:17:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4998180-6808-3dc0-beee-5f471e7a1f9b | -6.87548 | -52.78381 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 328fe281-6e4c-3b28-bc50-daebfc220354 | -6.22875 | -45.12656 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20e81822-b1af-35ba-a23e-3ad49888088e | -5.97159 | -53.60156 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5eca922d-473f-36a3-b448-53c304315c4f | -5.55836 | -46.53868 | 2025-09-06 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61cecd49-46e8-32eb-aead-79cd1754c083 | -6.88413 | -44.71613 | 2025-09-06 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78347654-15ed-3e93-a788-a9e4f7aea797 | -5.8683 | -51.72067 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0a42ce80-5f43-37bd-ac28-0a271066ece4 | -5.94539 | -46.17506 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 054d3cd1-710c-3c43-ab99-8763d0f806a0 | -5.8768 | -46.0473 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18a89397-2543-38c4-ae87-45886a829ffd | -6.60357 | -43.98077 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2164e243-b7fe-3c91-90e0-8146c8835240 | -6.54275 | -42.93407 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9ad601e-c13c-36df-9f40-b36d82e8e8ea | -6.04859 | -44.93624 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83ec1ae5-ea45-39cf-973e-fb44b111a1d6 | -14.57491 | -48.07893 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8109879-7f54-3de7-84c9-c4f524424e7b | -12.92827 | -48.02544 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01b96376-a1b7-3954-9b1f-fe87fe95b297 | -6.88637 | -45.54873 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35d8a6da-9385-3a31-8874-4c41f8580b1a | -8.36047 | -48.27421 | 2025-09-06 04:17:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 62688b13-9f06-3d5d-8f89-602058a9f402 | -5.58167 | -51.91812 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f8c825b-8556-3c28-9f0a-352319976c4f | -13.46948 | -46.84037 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16bc31a1-35fa-310f-b0e7-a4132f896d71 | -6.2472 | -43.30407 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f60f7d1-ee49-321b-8631-8447f1a0c863 | -6.01573 | -43.69976 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb8c1074-5722-303c-93f2-86bb017bd2a8 | -3.69687 | -49.5681 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ea45c33a-8a67-333a-ba95-03dacfa88757 | -12.63918 | -56.98925 | 2025-09-06 04:17:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70ab99de-3158-33a7-9773-f39921660905 | -10.14178 | -46.23493 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5ac40dc-95aa-3e2d-a410-839f24533588 | -4.98633 | -42.07084 | 2025-09-06 04:17:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a71ba40b-2fd8-31e5-b5de-1b700f83f27a | -5.9273 | -52.00091 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 295080dc-b407-3b5d-9e47-affce4e25aa9 | -12.96943 | -54.82396 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08eb6bba-77a2-3607-8eb3-32f318c0af7a | -15.84788 | -52.28621 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fea9532b-5b7f-33e0-8668-4f7abd25071d | -5.94627 | -42.9611 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e1625699-ec60-3a8e-bde7-f5448d8b2c48 | -5.92754 | -43.015 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c6c8731-44d7-3442-9deb-2594c86e6753 | -14.58444 | -48.00143 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6da4b8d-88de-30ac-b7f5-25f28c15c08f | -6.0045 | -46.69804 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b07ee673-b3f6-373d-8ca5-f88007355a6e | -6.16542 | -43.18097 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f7fcf11a-e523-35a6-8943-d8545b869fbb | -6.51607 | -42.41637 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e0248b19-f153-3274-9be9-da72692f4dc0 | -7.98898 | -45.4705 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| af4d74f7-9ab4-3415-a74b-bc7f9d8c59bc | -10.31924 | -46.40808 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f1b1eea-7db4-3dc1-a4f6-df4a14a9ffc5 | -6.22365 | -42.63891 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7b37ada4-df28-3a24-8cc4-e91d7bf741df | -13.73284 | -46.91172 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67a5ab9c-c1a8-3e91-a4c2-45205ff104e8 | -5.33792 | -42.78716 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 839f735b-d962-3a96-a2e1-8ae4df255518 | -12.91438 | -48.0182 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 684a847a-82eb-31f5-b3e6-bb646d9fd5c8 | -5.74532 | -42.75545 | 2025-09-06 04:17:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 726de770-b949-3c48-8c12-820dcfa84bc6 | -5.93086 | -43.01553 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b81d6218-91fe-322e-86e5-acb03da75059 | -6.34827 | -43.54471 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41e9cadd-0f9c-3332-b9c1-7ac4b5ff5ff7 | -7.60466 | -44.67051 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75bf7afb-9f40-3948-b7fd-9d56295a9a99 | -6.06653 | -43.29293 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2fb5d1e-eb88-3134-bede-139b066a253c | -13.93362 | -53.99453 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53ebb05e-2421-3d1c-9c34-e1cc0620ffb0 | -12.9654 | -54.81476 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 198bfa9e-5d3a-364f-8afe-e27d155fd018 | -6.38874 | -43.81976 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4d49be3-3d01-3e91-93e8-db8d8ad1d8bf | -6.17287 | -53.50217 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 145d59d4-6496-3391-9207-5cc70b6e7298 | -6.30558 | -44.57916 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db6038a7-13b7-3a9b-bb3d-b0738373bcc4 | -6.24387 | -43.30354 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d633849-c8c0-3521-a85c-0eb3b44018e8 | -5.72354 | -43.91723 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca432ddb-69b5-3477-8694-eae7b3268f62 | -9.08307 | -46.99531 | 2025-09-06 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4219d193-c812-348d-90ac-3007dbe54d21 | -13.01048 | -54.82416 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ec96c0dd-7832-35d1-b2fe-9e562cf4f853 | -5.93072 | -52.00196 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b274d310-3db3-389c-b75a-f1542ed86b9d | -6.01273 | -46.69472 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fc6a920-0ee8-385f-b745-912012a2d298 | -6.83083 | -51.87321 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05392b9e-21e9-32ae-8c0b-dd4ae7cf52aa | -5.98409 | -53.59953 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed3a1860-1cdd-3cc6-90f4-5084500969fb | -6.2041 | -43.57555 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7f9b7cd-8025-33ba-bb74-79e0d106351c | -9.68981 | -51.10355 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e9fb994-62d3-3078-8608-65bbbeeec5c6 | -5.55894 | -46.54208 | 2025-09-06 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0909ba74-44df-3a56-b12a-5094751f6086 | -6.54886 | -42.93859 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edf5e3bd-5407-38a7-a1c5-185cc24fe7ef | -10.31638 | -46.40352 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f852a402-d281-37df-a956-b67ca465a4dd | -5.55474 | -43.06598 | 2025-09-06 04:17:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bccdaef3-da53-3b29-adcb-aec809ce9404 | -6.60862 | -43.97064 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7586287a-a79a-35d6-b8a4-c9a3b1e92f34 | -6.15733 | -44.245 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e9eba6e-b7d8-3570-9cbe-3ec1d16e998b | -6.81376 | -52.81361 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 9ef83679-259f-37d8-bf7f-c65467b61d31 | -12.95 | -54.79148 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6b6f52b-aeca-3bc3-9c5a-3b997b8596be | -7.23026 | -44.82356 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ed7ec4e-b86d-3efd-bd5e-2a22b1d5c6b0 | -7.59687 | -44.66969 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85669de0-5f14-3877-8eb4-2457fb5b6b78 | -3.1606 | -49.47585 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01e4fc89-97fa-34c7-a160-894f2032cbff | -5.46795 | -42.86415 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cfd761af-482b-3d9a-be03-ea6a614c6b0c | -8.81095 | -47.50514 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50c394b1-e8b1-3e5a-af45-213969709211 | -3.32103 | -48.70467 | 2025-09-06 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f982d1de-c801-3e0e-bec5-2060614a62e6 | -9.71345 | -49.49057 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 875a33e0-c7ec-32df-b72d-77ed80996896 | -13.74876 | -46.92303 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00dfc329-a150-30c5-a78e-136fc402be03 | -5.86406 | -46.02966 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b55a8774-1514-325b-8570-842377f26f31 | -15.36348 | -46.41834 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5685ccf7-a11b-33e4-9da2-a68526d08b9e | -3.16449 | -49.48142 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a157afca-bb1f-38a8-9308-df33e04fd17f | -9.6889 | -51.10855 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eea0c4a8-2500-3a58-a898-54cd424ff76d | -6.15709 | -43.16899 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d63dbb0c-0a73-376a-9a88-02989844b70b | -7.73892 | -47.42113 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5729afdf-ae2d-306b-b026-a93cee311811 | -6.60526 | -43.97014 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89e3ebd8-8529-3529-85ca-764b953adf7b | -5.88342 | -51.96992 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758fc64e-3614-33a7-8f3b-d943de60850a | -13.27838 | -46.8131 | 2025-09-06 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a88a8863-d61c-3bad-956c-045aa1044b56 | -3.42882 | -49.04702 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4650359-5197-39e5-99dc-2c11c06f2ebc | -10.06491 | -48.0644 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a461063b-c383-31e6-a11f-05e8d5e0d601 | -12.86496 | -48.00127 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 501a4b64-a286-3583-ba18-316eed6e884d | -14.80393 | -48.11602 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c00a4a05-8ea0-3017-9fb5-6477f274a9f7 | -4.82713 | -42.73916 | 2025-09-06 04:17:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae669f0f-ea70-3aae-85d2-b2fc18c288b7 | -12.93192 | -48.02618 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
