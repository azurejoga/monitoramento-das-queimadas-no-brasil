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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 508c18f3-3ea1-3e42-8ae8-37752ca1a751 | -5.86674 | -49.77574 | 2026-08-28 04:49:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63feac50-122c-3a51-ab8b-6799b7e2df4c | -7.26125 | -45.85847 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5affe635-9091-3f19-bdba-0bbc34be0642 | -6.76119 | -46.13751 | 2026-08-28 04:49:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 28f6c436-6498-36a7-8924-159ae31768a8 | -5.49271 | -49.216 | 2026-08-28 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df71edb1-f374-3b8f-934b-ccf863bdbb75 | -6.49114 | -53.50312 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25e0eced-7151-32c9-8cc3-0f0cbd2245fc | -1.95916 | -48.37951 | 2026-08-28 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72ae18ca-29ab-37f7-90d1-16c361905a4c | -6.25768 | -55.41224 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7b9216e-1f4e-3a18-acd4-424aa0e74f19 | -6.52674 | -55.25451 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95e13491-2d7a-3fb4-8529-3c368b7b89b6 | -6.93244 | -42.67585 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54da4117-1806-3e21-9bb3-76d9d198a424 | -2.72967 | -47.05508 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05d43873-d21a-3a8d-8d3a-e977a8022494 | -6.12519 | -53.53846 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d45d993-c79d-34a8-b364-ac46ce7994ce | -6.16827 | -57.80095 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16464694-d2ec-3e40-8f88-2fd76a163240 | -6.53648 | -55.24815 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a8b55ca-e3a2-3d32-aa68-33f8ab89b65a | -6.62927 | -53.1829 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d73e273-cd53-3554-944d-41e9bfffad13 | -7.2701 | -49.85001 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 169dc3a0-d1be-36ec-85ac-96f772772729 | -6.3733 | -54.95808 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d75f76a-31e9-355d-a3d3-34ced80d0e8d | -6.24571 | -55.43071 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd4ef48-f0ca-32c7-a7bb-538cbd3c3848 | -2.49915 | -48.13518 | 2026-08-28 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 305d1600-4c67-3f9d-b44f-594cfccad132 | -6.13515 | -53.52568 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dd74aa8-aa47-35b7-a537-b233134550a4 | -2.89102 | -48.80177 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c29c895b-7002-388e-afb5-530453f79af8 | -6.90248 | -43.64526 | 2026-08-28 04:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a67b3ce-91f0-3d1c-a239-5fb96d3c75cf | -6.27539 | -53.35863 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 679231af-cbfd-3115-803d-5212cc639354 | -7.24857 | -45.86594 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 14b7da15-e7ec-394e-8ebb-d6a95a6ed821 | -4.84863 | -45.39995 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 21aaae77-fd9a-34e4-9ffe-572a718d780a | -7.27627 | -45.35302 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d59be413-9ae8-3759-bbd0-b42235a50ced | -5.25903 | -50.96906 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 725cc08d-1086-37f3-8081-0c860ad58f12 | -6.23017 | -55.46987 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0440bcc2-3f84-36dd-84a6-3d13b085648e | -8.06446 | -45.86592 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64ab6486-1043-3490-b307-647a1795bae2 | -8.08404 | -45.8116 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fca47dcc-6f61-30e7-86ac-77c0ab9fe968 | -5.58697 | -46.24468 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 82f9c14d-a026-31da-80b9-d18649faacf6 | -7.27312 | -45.34762 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b28c94f5-4420-3723-aa0d-486f88057aca | -6.1703 | -57.78942 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94529de6-ada8-367e-81e6-c87737213448 | -7.33695 | -46.66605 | 2026-08-28 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b8f00d9-38df-33e3-ac4e-978d2500839c | -6.27612 | -53.37742 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 819cff01-1035-3747-9e2e-8bab3bd009d3 | -6.83671 | -52.49758 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 345b46dd-7aa4-387f-817b-c8d3150775c6 | -6.26259 | -53.36588 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9a5f284-3aff-30ea-93b6-09d4eb4affe5 | -6.56814 | -50.02687 | 2026-08-28 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31777408-dd90-341c-b746-179b2fe9a010 | -6.27239 | -53.35346 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da7cd906-d279-3db4-91dd-b0c28a3a2ab8 | -6.26367 | -53.12027 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acd1460c-9fe1-3d5d-af2b-e0ddb89eeacc | -8.06187 | -45.86338 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9244086-b497-337d-aff4-ad7985118714 | -4.84932 | -45.39547 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 8b57d3e0-c699-3855-b59c-b998ffa16c0f | -6.1587 | -57.79629 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 64c2b858-ecfc-3d10-b244-8a1984fc6436 | -5.89996 | -52.10984 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eacf139a-a1b0-3ab6-bc57-c7be30935801 | -5.93499 | -52.36388 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a90ea956-4529-3ed6-ba47-69816fd37245 | -6.27386 | -53.39104 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08630e26-a51f-395a-b67b-f0545aa1b1e5 | -8.16906 | -46.17518 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb0b1062-6b06-31a0-8d55-5d4323a3f0e6 | -6.27765 | -53.34509 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 008357c6-3cd7-3655-8b3a-ad8760ed0666 | -6.26638 | -53.34321 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0d2de0-25ba-365d-8234-51cd287c7ea2 | -8.09232 | -45.80835 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04fb47a2-9950-3fe8-a034-627724a5a74e | -3.76865 | -49.07464 | 2026-08-28 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7595f24-7286-3c68-b63b-ae38a6088bbd | -6.1572 | -44.6465 | 2026-08-28 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee884276-c0a4-3a54-adc0-d9b38daa980a | -6.06495 | -53.77424 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0167a8db-5aca-3dea-9d58-5ec22241e138 | -6.2784 | -53.34057 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ea059af-300e-3d69-8502-837b381fde31 | -7.26678 | -49.84948 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bd3aaae2-925f-35e0-9ab7-8f4934284c3f | -5.89572 | -52.11345 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d920d4c-bdba-3928-ae48-b696723a01bc | -6.25 | -55.43143 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0d89b60-920f-366f-81de-42f0d49924e5 | -4.92892 | -55.76951 | 2026-08-28 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5000703-e515-31da-87f6-a397bd084fd5 | -7.26365 | -45.86816 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 51285c4f-317d-3de8-b823-059528fc4e82 | -7.4039 | -44.67326 | 2026-08-28 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e14fe962-533e-3cca-ae09-2117c1a926cd | -5.93791 | -52.3685 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16b233b3-bdb0-3d5b-9e93-bc14d13a797b | -7.34825 | -46.68898 | 2026-08-28 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e4a01b-8bd1-31fc-bc34-7dd7777b0d5b | -6.41151 | -51.68081 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e3cd353f-b9ab-36f9-ab5c-87b13fc05591 | -6.53227 | -55.2474 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9012d309-78c1-3996-80ea-13e6748e7c0e | -6.227 | -55.61813 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b25f0b6d-1c64-3f54-ab17-c03cf09ec8d1 | -6.18153 | -45.91322 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f923b3ea-4dbd-3498-bd3b-7f38fca77b9e | -6.51963 | -55.24526 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1239c93e-5ee8-38bd-80e4-148e1391648a | -7.12451 | -42.77555 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 64757180-a9cf-3940-948b-7cec76fb0e66 | -1.74414 | -47.12568 | 2026-08-28 04:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23bac2ec-d4b2-3afe-b215-c9d61ef9ee4c | -1.36106 | -54.63017 | 2026-08-28 04:49:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1560cc9b-49dc-3483-ad17-293ac272ac19 | -6.22158 | -53.47411 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a54ee93-110a-391c-a871-d514b48c01bc | -6.25836 | -55.40828 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c0c84e3-f094-35e6-b0be-a62e133478b0 | -1.95971 | -48.37607 | 2026-08-28 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce659cf5-1b58-3fc7-b39f-9ec1f28b9159 | -2.88771 | -48.80125 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72d1393e-3859-398d-9b93-04b5e134544b | -8.17104 | -46.16186 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3acd2a5-003f-353d-bfc6-ff618f538874 | -4.84488 | -45.39938 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 90189c5e-088f-3078-84f5-fabb7ddc2d0c | -6.0307 | -46.75657 | 2026-08-28 04:49:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf8f1a7-997b-3c1c-96b9-a442c0c57ef5 | -6.82561 | -45.54793 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2af0c05c-59f8-3839-bde1-f3d1050a7ef5 | -3.53353 | -48.18315 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd96e661-030d-35e5-9149-9350e41f3d5d | -6.1876 | -45.92312 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a265c29e-1c39-3c9d-aae0-dd72622e5ce4 | -6.1622 | -57.8059 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 25c84f0d-122d-36ad-9027-6944cf9c3857 | -7.08611 | -42.20546 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69612c46-9deb-394f-95ce-abe45c06826f | -6.62429 | -43.73262 | 2026-08-28 04:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45276fec-430b-3c7d-af62-5fe5752de78d | -7.15424 | -46.5438 | 2026-08-28 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb111a41-e19a-3731-89df-bd69acd60eb6 | -1.96412 | -48.36969 | 2026-08-28 04:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 937eb567-f285-3608-839d-230e96aa1ce4 | -8.06567 | -45.86401 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1050b0e3-9e19-3221-92be-51bc192f1bde | -7.29227 | -49.94613 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c43d14c-7809-3b4d-a748-d2a313057e41 | -6.5956 | -55.43591 | 2026-08-28 04:49:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f758fbf-6943-3851-af67-0d78c6f29dbf | -7.87685 | -46.09555 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ce4bf697-c817-36a3-834f-89a458948046 | -7.16899 | -43.16766 | 2026-08-28 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9eb08552-6324-3132-a787-75fb312d101d | -7.20376 | -42.73983 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee6d153e-51f1-3771-8dc1-4f966df2f630 | -7.20305 | -42.7447 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a0ee9100-728a-305e-8811-d48ee8ce2388 | -6.27194 | -53.13974 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7bee2582-92a3-3564-9bd2-bdf857159937 | -6.64776 | -53.1861 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 83f4a145-5be5-39d4-ba01-632c7ad27316 | -8.08469 | -45.80716 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 02ee4bbe-c816-3db9-a073-ff0966dd09b8 | -6.52318 | -55.24989 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddf3ae05-afe1-3fbb-8ce7-635548398811 | -6.31979 | -54.73331 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d0e3476-fa6a-36ba-95ef-c92f30d88ba9 | -4.92818 | -55.77391 | 2026-08-28 04:49:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4900d9b8-15d8-388c-af1f-ba0151661d78 | -6.12979 | -53.53438 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 825597db-58e5-38aa-b5bd-60693fa4abfa | -6.12598 | -53.53375 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a64bbd1b-82e6-3f94-a869-555e5aaa57d1 | -7.03886 | -50.72411 | 2026-08-28 04:49:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
