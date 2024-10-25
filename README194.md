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

## Dados Diários - Página 194

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1af84450-3c86-302b-b0e9-ba0948214c3b | -3.7285 | -44.2943 | 2024-10-25 18:55:26 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 189.8 |
| f41474ff-c05c-36ce-8726-f9c916c82198 | -3.8144 | -48.9729 | 2024-10-25 18:55:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 04558dcd-5643-3e57-984d-e5a317219edc | -3.9165 | -44.0327 | 2024-10-25 18:55:27 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| eac2e326-98d0-39f8-acd0-1e9344c9fd09 | -4.029 | -43.9348 | 2024-10-25 18:55:28 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 6c722719-93aa-3b8c-8d64-355025796b3b | -4.2922 | -43.6434 | 2024-10-25 18:55:29 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 08a69315-b821-3f5e-8b51-42428d195cfe | -4.1601 | -46.8322 | 2024-10-25 18:55:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 67a6cc2d-5bb5-39bd-83d2-937c2fb5b569 | -4.4655 | -42.9112 | 2024-10-25 18:55:30 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 3b0b682e-4a4d-3dab-8da5-2317a9a0cec5 | -4.5728 | -56.0931 | 2024-10-25 18:55:31 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| d2ec5be0-c6f8-3c0f-9c0a-953cca4da71c | -4.5912 | -56.0924 | 2024-10-25 18:55:31 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fc7f4cfd-aeb3-3cb4-9aae-59741b4f98cb | -4.7445 | -45.6679 | 2024-10-25 18:55:32 | GOES-16 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 7c38fde5-1403-3a24-a8c1-9bf852da0a62 | -5.0769 | -43.6644 | 2024-10-25 18:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 223.1 |
| c869b21e-e6dd-3d20-a33d-f52d125275c3 | -5.1129 | -43.8471 | 2024-10-25 18:55:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 458cd907-3491-3c9f-b653-32d4c7c9dade | -5.3553 | -46.2344 | 2024-10-25 18:55:35 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e770bd52-bcf9-3c99-a663-086a3ebd1229 | -5.2464 | -45.8617 | 2024-10-25 18:55:35 | GOES-16 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 6a44918a-2291-3203-ab45-c75ff4e742d9 | -5.3017 | -41.4526 | 2024-10-25 18:55:35 | GOES-16 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 434568ba-835b-3c56-9f3f-de301a0b1cb1 | -5.2877 | -43.0676 | 2024-10-25 18:55:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 0e94de03-4d1a-3c70-83c6-31b9d8a85e2e | -5.3025 | -50.9748 | 2024-10-25 18:55:35 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 497523bd-ec70-3ff7-a551-e2250c6cf05a | -5.299 | -39.6665 | 2024-10-25 18:55:35 | GOES-16 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 86.6 |
| bed743fd-03d9-3426-b367-3164031ebc32 | -5.4373 | -47.6833 | 2024-10-25 18:55:36 | GOES-16 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3ce8568a-31c6-3c5f-b816-90bd46efa582 | -5.7014 | -45.0199 | 2024-10-25 18:55:37 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 20aebb8e-7dc7-3709-98cd-8471ef0f54f1 | -5.5688 | -49.9941 | 2024-10-25 18:55:37 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| a9a04be0-af6d-3586-ada2-a56e5fb3b396 | -5.7225 | -49.3055 | 2024-10-25 18:55:38 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4225de28-ae89-34be-a48e-ceb941317dbf | -5.7227 | -49.2842 | 2024-10-25 18:55:38 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f4c3935b-424b-384b-aa91-dcca557b9e84 | -5.8016 | -44.2591 | 2024-10-25 18:55:38 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 64b60adf-e910-3b7b-b6f0-f18097214855 | -6.1935 | -50.8631 | 2024-10-25 18:55:40 | GOES-16 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c67b1ad5-05ae-3906-a884-a7b50a2395da | -6.2931 | -47.824 | 2024-10-25 18:55:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 245.4 |
| d1b96416-504a-3ee1-a840-9319dacc2f10 | -6.4165 | -44.6008 | 2024-10-25 18:55:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 45929e00-77f2-3d94-82d9-ff1bcae31dc8 | -6.2744 | -47.8253 | 2024-10-25 18:55:41 | GOES-16 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 6e6b5c86-7741-31b4-bbaa-e60d29897ecd | -6.7045 | -43.9554 | 2024-10-25 18:55:43 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 9aa08365-0a55-33bd-8dd8-e3f4f394f0c5 | -7.1092 | -46.5065 | 2024-10-25 18:55:45 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 874893a6-d7cb-3355-8801-af71b045d75e | -6.9275 | -60.0303 | 2024-10-25 18:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 2a51055f-b484-3448-aa47-89e4764e3d89 | -6.9952 | -46.6714 | 2024-10-25 18:55:45 | GOES-16 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 71c7c3af-d03f-3a7a-ab0f-6a4202d675c1 | -7.1861 | -46.3217 | 2024-10-25 18:55:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| fab01b27-478c-3cc5-83ff-658bba7c66e2 | -7.218 | -46.8527 | 2024-10-25 18:55:46 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8298a39a-0114-37f2-be79-c35574b54fd2 | -7.2943 | -44.9817 | 2024-10-25 18:55:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 9833b5b7-c57e-31f3-b489-2009905534d3 | -7.3131 | -44.98 | 2024-10-25 18:55:46 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a61e67a7-65b7-3707-880a-34966482cd23 | -7.3266 | -47.2192 | 2024-10-25 18:55:47 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 45216cd2-cd77-31ff-ab52-484d3d309b6b | -7.5289 | -45.8434 | 2024-10-25 18:55:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c58c83c4-ee75-33c3-9eaa-8b90c6046261 | -7.5477 | -45.8417 | 2024-10-25 18:55:48 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e6ea2fe1-d6fa-3e46-8569-7e71c1c42eda | -7.8727 | -45.3593 | 2024-10-25 18:55:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.2 |
| ea3e9285-458d-310c-b87c-92703a371a90 | -9.0635 | -48.0051 | 2024-10-25 18:55:56 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 896698c6-ba5a-334f-bfb1-46d76a6fe8b2 | -9.0824 | -48.0032 | 2024-10-25 18:55:57 | GOES-16 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| cfedb440-c714-35e6-9755-f556483d15c9 | -9.4699 | -43.215 | 2024-10-25 18:55:58 | GOES-16 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 248.8 |
| 722b8bc1-7492-3cd3-a37f-06ef56703f69 | -9.5073 | -47.2319 | 2024-10-25 18:55:59 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 536d886e-03c1-3c6c-a8d0-b31747c1ecb5 | -10.5087 | -44.8748 | 2024-10-25 18:56:04 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 70e8ac35-0264-378c-8985-735ddb32f7ae | -10.4493 | -43.8373 | 2024-10-25 18:56:04 | GOES-16 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 06c4b25e-f460-35c9-9db1-76c137e0bcc2 | -10.5091 | -44.8517 | 2024-10-25 18:56:04 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 06b6ef81-0253-33fe-a118-05bcef5e314e | -10.6292 | -43.3416 | 2024-10-25 18:56:05 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 75.5 |
| 1ea9d3c0-93c0-30a9-80aa-16ef14e91900 | -10.6249 | -55.9757 | 2024-10-25 18:56:06 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 151.1 |
| 039ad5b6-598e-3717-829e-65810ca860ee | -10.879 | -47.9599 | 2024-10-25 18:56:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 44aaf02b-693c-3621-9a17-0f4df0381b84 | -10.8793 | -47.9378 | 2024-10-25 18:56:07 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 3b42dbec-6cdb-35d7-8050-ffe0e708b43a | -11.5357 | -43.9853 | 2024-10-25 18:56:10 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 465ebe9f-0391-3623-b238-883c79679bf8 | -11.6711 | -43.9178 | 2024-10-25 18:56:11 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 29f7dd47-66b5-3a79-a985-e956dd8096ac | -11.9028 | -43.8348 | 2024-10-25 18:56:12 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 102.7 |
| c5fbf4f5-c135-3326-9f7c-33c6d232db80 | -11.9642 | -44.6676 | 2024-10-25 18:56:12 | GOES-16 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 84190710-dbf7-3ebe-bf66-c4f500f9f89c | -12.1179 | -43.6354 | 2024-10-25 18:56:13 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b922e4db-0951-3a7b-a21a-0f7470d4a3b4 | -12.6805 | -43.4235 | 2024-10-25 18:56:16 | GOES-16 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 01cad497-b7ea-3ccc-bd57-c527ea4909c2 | -12.6801 | -43.4474 | 2024-10-25 18:56:16 | GOES-16 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2b59947d-ef31-3722-9659-8d273d40d73c | -14.4169 | -42.1331 | 2024-10-25 18:56:25 | GOES-16 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 605213a1-425a-3f4e-b3fc-6c00af303174 | -17.7634 | -57.5937 | 2024-10-25 18:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 208.0 |
| dcc380c9-a73a-3f31-92f8-c2e499e07906 | -17.7637 | -57.5732 | 2024-10-25 18:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 148.7 |
| 139d2d87-8646-3c6c-8617-4a8b6e318f84 | -17.7443 | -57.555 | 2024-10-25 18:56:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 277.6 |
| ccc80a29-4dd9-34ce-b26f-fd8660ab8765 | -19.6028 | -56.8996 | 2024-10-25 18:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.5 |
| d97a7113-f733-32eb-8c3f-df17498e028b | -19.6639 | -56.8492 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 5f8ae1ae-f0e4-3516-9e00-560beb742a9c | -19.6457 | -56.7471 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 132.2 |
| 65ae0079-1c15-30da-81b6-82002177bbcf | -19.6225 | -56.9178 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 85662289-3ade-3446-b4b2-f32bc49ffce1 | -19.6253 | -56.7709 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| 96679536-fbda-3eef-8e67-aa8c35b66877 | -19.6453 | -56.7681 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 110.5 |
| f71d45ee-17e1-3fe1-8dd9-25ba2c485c4d | -19.6024 | -56.9206 | 2024-10-25 18:56:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 136d0bda-4d39-3342-9487-b706a86b601d | -19.6658 | -56.7443 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 107.2 |
| 2fa33022-7539-3123-a63d-5385f760b23b | -19.667 | -56.6813 | 2024-10-25 18:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 8f8adbe4-5862-3059-bf8c-213861c6fe44 | -1.0733 | -53.658 | 2024-10-25 19:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1434ca00-af14-3c10-b06c-a2bfe2432018 | -1.0368 | -53.5171 | 2024-10-25 19:05:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| 80e0ec21-ab57-3ce4-a6a5-f46ef8c61696 | -1.2907 | -55.7098 | 2024-10-25 19:05:12 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 539df68c-a1e1-33f8-b7ef-86f04c6aa9b6 | -1.2762 | -52.9275 | 2024-10-25 19:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 141.0 |
| ce0698e6-bace-3291-a59d-2ee162e41b13 | -1.1834 | -53.6569 | 2024-10-25 19:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| ef5c1799-eca5-3a3f-8bb0-c9fa4a253f04 | -1.2578 | -52.9277 | 2024-10-25 19:05:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 87a65c78-e0ed-3cd9-bf1f-c8f21e07c564 | -1.1834 | -53.6771 | 2024-10-25 19:05:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e3342470-3241-3304-a0cf-f6e3362d1891 | -1.382 | -55.847 | 2024-10-25 19:05:13 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 176.9 |
| 66c515b2-4faa-38c8-9c17-2e5cb2ab1577 | -1.4918 | -55.9443 | 2024-10-25 19:05:14 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 49c805d6-9343-3ce2-a0ba-50eeb1e7bda1 | -2.0484 | -52.6926 | 2024-10-25 19:05:17 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2f186f45-f89d-3339-8138-2b4696fb0f81 | -2.023 | -55.8981 | 2024-10-25 19:05:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7aed4009-f318-3aef-b483-7034eb077e3f | -2.0232 | -55.7798 | 2024-10-25 19:05:17 | GOES-16 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b49fe059-0282-3003-9edc-528bc563912f | -2.1129 | -56.6823 | 2024-10-25 19:05:17 | GOES-16 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 56b1b780-71a2-349c-8bc0-3bd2000bd964 | -2.464 | -49.1024 | 2024-10-25 19:05:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| b03fe4b7-4568-332f-a67f-3f936a11e789 | -2.3892 | -49.3807 | 2024-10-25 19:05:19 | GOES-16 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6853ab05-cd47-311c-9595-0306bd9a5504 | -2.6473 | -49.5225 | 2024-10-25 19:05:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 9afcbe8b-1084-32a0-bdbe-f7e607e3d006 | -2.6473 | -49.5013 | 2024-10-25 19:05:20 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a134fc43-ab24-368a-b4bb-b16760bf4571 | -2.6657 | -49.522 | 2024-10-25 19:05:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5e5a113c-4716-306f-b1f8-7d501eb8175a | -2.6658 | -49.5008 | 2024-10-25 19:05:20 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2ae38a2e-889e-3162-b48d-0ccfb9f7d9fe | -2.8144 | -49.2631 | 2024-10-25 19:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| aa5aec54-95b0-36ad-b9f7-31afa7ed241e | -2.8502 | -44.9905 | 2024-10-25 19:05:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 146.5 |
| bdc48117-9c28-3ef2-b97a-2b9f67b06cea | -2.9578 | -50.4198 | 2024-10-25 19:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 147daf97-8e0a-3e4b-b969-02df29af6b68 | -3.1281 | -54.266 | 2024-10-25 19:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7f57801e-47e3-3e43-909c-89c7db63e944 | -3.4211 | -54.5787 | 2024-10-25 19:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| e0073a2b-0ead-3ba5-99f5-4461564fc88c | -3.4951 | -54.4366 | 2024-10-25 19:05:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 251.2 |
| 8358de56-4972-364e-8c63-f27e5d44b02b | -3.4469 | -52.6386 | 2024-10-25 19:05:25 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| c146258c-3b06-3ccc-ae63-931008f86e0c | -3.5988 | -44.1629 | 2024-10-25 19:05:25 | GOES-16 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 5294de74-70e7-32d8-81ff-36f4b58bea67 | -3.5059 | -44.1213 | 2024-10-25 19:05:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| e663c2bb-711a-38b9-830b-68d185ea6710 | -3.7572 | -45.8081 | 2024-10-25 19:05:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |


[Clique aqui para ver as próximas entradas](README195.md)
