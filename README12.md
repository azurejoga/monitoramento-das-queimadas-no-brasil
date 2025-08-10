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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6937a574-b427-3de8-b8a1-fa49cee00ead | -8.9213 | -60.7489 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| dc02302b-96f2-3fdd-afd3-4c7e8101b449 | -9.362 | -61.5324 | 2025-08-10 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 39c25a7a-8084-3e99-8af4-1e22ad79bdcd | -21.31645 | -48.56829 | 2025-08-10 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ec669f1-d084-33da-9272-8ef57eb28756 | -21.6791 | -46.95139 | 2025-08-10 04:00:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e1f1d48-8902-3e5d-b08d-2882a1f60dac | -22.52364 | -46.81442 | 2025-08-10 04:00:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5ca37666-24dd-33f0-bd4e-96776e92e797 | -22.52172 | -46.80361 | 2025-08-10 04:00:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0b6d5a46-7293-39c8-9a2a-14fc9a9b692d | -21.31519 | -48.5652 | 2025-08-10 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a1a8b52-74c2-3cf6-852b-8710c3ff24aa | -22.79808 | -51.74399 | 2025-08-10 04:00:00 | NOAA-21 | CAFEARA | PARANÁ | Brasil | 4103404 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a4d22690-0261-3266-84f9-84a7a2695164 | -21.38374 | -44.12767 | 2025-08-10 04:00:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 76fb8958-4233-30c7-855a-e77b00b4e4ed | -22.51792 | -46.80285 | 2025-08-10 04:00:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e626368-1195-3b27-9df2-c1ada1ec641b | -20.94486 | -46.6988 | 2025-08-10 04:00:00 | NOAA-21 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ca153f8b-afef-32ed-bcb5-1c3217cc485f | -22.51854 | -46.80518 | 2025-08-10 04:00:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d3ea509f-2fa0-3789-99fd-1f68a082728a | -23.39855 | -47.00542 | 2025-08-10 04:00:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d045a1ba-d812-3760-a2c6-a8c3bb35765e | -21.31214 | -48.56743 | 2025-08-10 04:00:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0e78d809-1acf-31d8-93bc-d9db7173686f | -22.83928 | -47.24263 | 2025-08-10 04:00:00 | NOAA-21 | SUMARÉ | SÃO PAULO | Brasil | 3552403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 60462804-6af9-3bda-ba6c-ed22a9cbe98b | -22.72251 | -47.39134 | 2025-08-10 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| eb3b5943-157a-3595-a73c-14f37b64c386 | -21.48194 | -47.74998 | 2025-08-10 04:00:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd1d43b-93e4-3c90-85bd-92fda2f31e63 | -23.3601 | -46.58026 | 2025-08-10 04:00:00 | NOAA-21 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7404a5bf-aade-3f4d-af79-4df90ca1b61a | -22.68543 | -47.37229 | 2025-08-10 04:00:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45135d55-6acc-3b06-ace8-7e11a7abbfaa | -21.17093 | -48.65343 | 2025-08-10 04:00:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aa85da68-db8c-3c64-b0f5-5513bffb793d | -23.86444 | -48.18349 | 2025-08-10 04:00:00 | NOAA-21 | SÃO MIGUEL ARCANJO | SÃO PAULO | Brasil | 3550209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5059cca1-a451-3295-8d78-288292dd3043 | -21.44782 | -47.01932 | 2025-08-10 04:00:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 514655f8-145e-3946-9081-daf138176b35 | -22.9099 | -45.50279 | 2025-08-10 04:00:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| 220e3674-26f2-3c65-8ea3-7f6d2f5e5983 | -23.19987 | -46.77158 | 2025-08-10 04:00:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6bc420f9-081b-3ebb-8316-462f1d56259c | -21.17179 | -48.64902 | 2025-08-10 04:00:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e16ed6a-1cf3-38ed-8a9b-73bbd256ec33 | -23.19705 | -46.76583 | 2025-08-10 04:00:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ef500255-a07d-3ad6-acf8-c30877f702ab | -21.52988 | -45.23648 | 2025-08-10 04:00:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 02cc9401-b670-3f39-a988-8d7a1c909c08 | -22.51093 | -46.80365 | 2025-08-10 04:00:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3905f717-5351-3c95-ad17-cfd445d75023 | -23.19613 | -46.77076 | 2025-08-10 04:00:00 | NOAA-21 | CAMPO LIMPO PAULISTA | SÃO PAULO | Brasil | 3509601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f67f5273-ff25-33d0-9333-d79fe4fff198 | -22.52051 | -46.81601 | 2025-08-10 04:00:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 23ced311-6df9-31d9-a91a-692379db304c | -22.72151 | -47.39674 | 2025-08-10 04:00:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fb999283-5656-38e1-8de7-b0fca31c96f6 | -8.9213 | -60.7489 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 09b1280d-e256-3165-b5e5-0b89864f8c86 | -8.9399 | -60.7481 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 781ae34b-4331-38ed-bd9f-2fa6e63ed52b | -7.0614 | -59.1972 | 2025-08-10 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2dae5abf-8f10-39e7-b916-5afbd8c11a2b | -9.362 | -61.5324 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 00eae3a1-bfb9-311c-8cd7-c5e8b7d9b15b | -8.9215 | -60.7297 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e9227a76-a3f5-310b-a536-0a92fcd5dfec | -9.3808 | -61.5124 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1b944a28-0b52-3618-818b-eceaa5b21452 | -9.3806 | -61.5315 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 5cc77dc8-81f6-3132-92bf-b3004b244488 | -7.0799 | -59.1964 | 2025-08-10 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 71bf7530-1203-3be5-8138-98ab68766678 | -8.9401 | -60.7288 | 2025-08-10 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1e247fc8-c432-376f-9f28-15c1f8ef6573 | -16.3731 | -42.5425 | 2025-08-10 04:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| f446cf84-cf00-3ebf-937b-a207490d8e10 | -3.18991 | -41.85391 | 2025-08-10 04:19:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de4ffdd1-74aa-3778-a4b6-b97401dc9ce4 | -3.22785 | -49.33747 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38ff547a-da67-3196-90f7-cd72d546c5c2 | -2.58389 | -51.92247 | 2025-08-10 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8f96066-b1cc-3a8c-a6b6-ea17cd2bcdff | -2.3742 | -51.91336 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99250ea1-264a-3d85-a7ed-76252fce9486 | -4.17264 | -42.44621 | 2025-08-10 04:19:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3246cb14-d801-3bd1-a85f-5d189525ab45 | -2.37099 | -51.91105 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d074470d-8af4-3295-b7f2-b30a511f4f09 | -3.27909 | -48.80899 | 2025-08-10 04:19:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f5d399e-89c4-3d7a-94ce-a29a71de0240 | -3.58705 | -47.52041 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2704add8-7118-3bcf-87fc-5f5b01f135b3 | -2.58436 | -51.91958 | 2025-08-10 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6990b4a8-a36a-32a9-88f4-2f776d4484b4 | -3.22665 | -49.34497 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbc31346-995f-3d2c-851e-1164cea8db57 | -2.37652 | -51.90885 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b11cf32-246e-367c-8f36-c8cf72c72254 | -2.37146 | -51.9081 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 720a56fd-9ced-355c-aa48-de421e94d08a | -1.93933 | -48.79628 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4100da0f-4f7b-35d4-bb7e-de6a9f5a417f | -3.27852 | -48.81248 | 2025-08-10 04:19:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 129451b1-2534-33ba-8c48-aecf8e8fd9da | -3.66606 | -43.39092 | 2025-08-10 04:19:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a094be7-16b6-3735-ac9a-10157ef5d6a0 | -4.11092 | -38.17107 | 2025-08-10 04:19:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 0eeecd85-9530-3da7-ba86-15fb2c731c83 | -2.37558 | -51.91469 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334b1feb-36a3-3bd6-8a1a-7ef91e3a97cd | -5.3477 | -36.13708 | 2025-08-10 04:19:00 | NPP-375D | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8a755a7d-d125-37a4-b3fa-3fd726646d3d | -2.58762 | -51.92338 | 2025-08-10 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b75bcb3a-57f6-354b-87c4-ee7beafd946c | -4.1103 | -38.1751 | 2025-08-10 04:19:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| dbc370d6-59be-349d-89c0-db8a786e0a58 | 0.69621 | -51.44749 | 2025-08-10 04:19:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c40ff69-653f-3fbe-8011-33d9a2e221aa | -3.59005 | -47.52542 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10d9cdce-aea6-3f99-8442-a4e00bb77bc5 | -3.2338 | -46.79649 | 2025-08-10 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e32d7f0a-44b5-3c52-b2b2-ed53c6df328f | -2.43952 | -47.33039 | 2025-08-10 04:19:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba992436-05e5-3b30-9fe4-94bccffe0132 | -3.3105 | -42.53284 | 2025-08-10 04:19:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af285a3b-cdd3-3fdc-a68e-1811b2d1c509 | -3.62109 | -47.5214 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f710c20-32c8-30ed-97df-8d5ae59af7d6 | -2.37605 | -51.91177 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fa0e71c-17c9-3f4d-a91a-bcacbad2dc94 | -2.96241 | -49.06671 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dcb7877-0a41-3739-b3ba-bf2471e6df68 | -3.23088 | -46.79186 | 2025-08-10 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bc225b0-e3e3-3026-839f-bf5c815bcb1e | -3.42329 | -48.89417 | 2025-08-10 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0435f2bc-9dc0-3b10-a14d-939b3606e2fb | -5.05837 | -38.13247 | 2025-08-10 04:19:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1558fe15-17cc-390e-9c12-68077b51fb12 | -3.42823 | -49.04095 | 2025-08-10 04:19:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aa94eb2-1cf9-36eb-a196-c84c180e1a48 | -2.37469 | -51.91045 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81da2398-41c4-3c0f-b4cd-49e9768c8d4c | -2.37518 | -51.90752 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a52de0e-4a9b-38d9-acd1-a9ceb9b12a3a | -2.44022 | -47.32597 | 2025-08-10 04:19:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 064d6abd-9636-3e6c-8f93-c36f2bb7880c | -3.6248 | -47.522 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e191c1c-b820-3501-8788-ab96bfd9b37a | -3.30769 | -42.52874 | 2025-08-10 04:19:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b713b6a-13f2-3336-991d-de43425cc33c | -2.58811 | -51.92048 | 2025-08-10 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2542f2a7-1c12-3843-b731-a20d5e8d2fd7 | -3.22747 | -49.34422 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c72a43b-aeed-3bee-85db-2107a100ebeb | -5.34833 | -36.13276 | 2025-08-10 04:19:00 | NPP-375D | JANDAÍRA | RIO GRANDE DO NORTE | Brasil | 2405108 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2a92f29-9c1b-3b89-9b9e-49dbc75de979 | -2.37193 | -51.90517 | 2025-08-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50da89cb-4bd5-30b5-aea8-09a2d71e4ef6 | -5.17103 | -36.54818 | 2025-08-10 04:19:00 | NPP-375D | MACAU | RIO GRANDE DO NORTE | Brasil | 2407203 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7735da7e-fd6f-3095-b975-f3e169aa259b | -3.23446 | -46.79244 | 2025-08-10 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7258a762-3d22-3326-b456-bae8d1870885 | -3.2281 | -49.34048 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39186aa5-6e06-33a2-a603-0406369358a4 | -5.05775 | -38.13665 | 2025-08-10 04:19:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bec592d2-8cac-3d30-9ec7-1d1bb9c6f59c | -2.5894 | -51.92037 | 2025-08-10 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f659c100-0ff5-3e6b-86f7-3f430fa9b5a1 | -3.22725 | -49.34122 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f2bb78e-152c-3c72-9bd6-276f87856139 | -3.59076 | -47.52102 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26d0611e-44d2-3190-bb09-bf29646031d2 | -3.62409 | -47.52644 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6d371da-8fbc-3d61-8576-62bf11eeec4e | -3.2745 | -48.81181 | 2025-08-10 04:19:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34256891-4594-3df1-a7ed-3964ba68616b | -3.21975 | -46.81508 | 2025-08-10 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66273c7e-a5aa-3ada-8061-e2cda4f8d741 | -3.58635 | -47.5248 | 2025-08-10 04:19:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7030fcf9-6e83-3655-a3ec-a8c3d3a022d1 | -2.66621 | -47.40784 | 2025-08-10 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bac2ac3f-6347-321d-aa38-cca75a6d3f29 | -3.43172 | -49.04515 | 2025-08-10 04:19:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8fec798b-e01e-3f72-8174-ef7b50d50390 | -2.58893 | -51.92327 | 2025-08-10 04:19:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a42bd064-6a35-3c74-b1b9-234404a2fae4 | -3.22369 | -49.33673 | 2025-08-10 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 79c4d839-6a4f-3dd8-9354-f435ffb58584 | -3.42765 | -49.0445 | 2025-08-10 04:19:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd3b6a92-d4c5-3452-b1f3-3a403addacfa | -7.08 | -59.1771 | 2025-08-10 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b7f686a8-64f4-391c-90f5-e39cf6d49181 | -8.9215 | -60.7297 | 2025-08-10 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |


[Clique aqui para ver as próximas entradas](README13.md)
