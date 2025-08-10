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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7cd148c-1936-3d1c-932b-7de784f1bb7e | -18.98549 | -48.41148 | 2025-08-10 04:25:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9dd9f2f3-fa1a-3374-a56d-03478f8c4d4b | -17.74213 | -48.56912 | 2025-08-10 04:25:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0b585ae-2b6d-378a-8d97-878e8107239a | -21.30155 | -46.81474 | 2025-08-10 04:25:00 | NPP-375D | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6dc0841-fca7-37fd-9e1d-0f49b6f11f53 | -19.5797 | -47.23726 | 2025-08-10 04:25:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 502aab2c-729e-3d44-bbaf-1e50e5ac800b | -22.50769 | -46.80626 | 2025-08-10 04:25:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d1ca6249-5d94-3267-a66d-7debbb09a504 | -19.80144 | -46.03191 | 2025-08-10 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 815dcac0-648a-3f7b-b2de-558692cdfa0c | -18.16912 | -46.99955 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc7d753d-0bab-3468-abfb-8873aaa5a76e | -21.31815 | -48.56599 | 2025-08-10 04:25:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a11f2acf-d7c0-3745-9e86-455ee1c24ae0 | -21.31483 | -48.56538 | 2025-08-10 04:25:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4c48174-d50c-365b-89ba-a0f75e796549 | -19.40113 | -43.35735 | 2025-08-10 04:25:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 117c0179-79d4-32b8-b0ec-c0fe0b5e266f | -20.59798 | -51.60992 | 2025-08-10 04:25:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 75a21afb-18c6-3877-a06e-144a0503ad62 | -19.20472 | -42.02059 | 2025-08-10 04:25:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 19eb9c9f-da44-35f1-b71b-f6f18e2eb6e2 | -24.67682 | -51.05029 | 2025-08-10 04:25:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f388017-8fd6-3a25-b996-4e61e4ac7df4 | -21.08829 | -45.08006 | 2025-08-10 04:25:00 | NPP-375D | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2ebedb84-235b-3700-91f4-bf709bc5dc1a | -18.16968 | -46.99591 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2347f8b8-c109-3582-802e-f37cd68f37c6 | -19.20058 | -42.02005 | 2025-08-10 04:25:00 | NPP-375D | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 418cba30-df84-3ac5-b4b3-6af2b8cbfe83 | -18.17633 | -46.99707 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8a113c4e-1f8f-377e-a706-3a5c90dcc49d | -22.7235 | -47.39459 | 2025-08-10 04:25:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 80c148ac-ac69-3d78-b05d-63df4dc102a5 | -19.85281 | -42.30485 | 2025-08-10 04:25:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2dccce3a-391e-36b2-b069-2cfb14a62646 | -19.82368 | -46.60809 | 2025-08-10 04:25:00 | NPP-375D | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84d4df40-9f17-3238-bc59-4f365500bb35 | -19.8569 | -42.30548 | 2025-08-10 04:25:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb3db332-8c9d-3ea8-b6ff-84c6ee1c4e41 | -20.17065 | -43.71728 | 2025-08-10 04:25:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 3edcc619-6c1c-3067-8d2d-98dac9ce2539 | -22.81653 | -47.14294 | 2025-08-10 04:25:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9826533-7f0d-3ec4-9b77-ccf1fc76eb6b | -21.52873 | -45.23444 | 2025-08-10 04:25:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9d86ceae-0989-3036-b005-1ce1045d4f41 | -19.754 | -48.01595 | 2025-08-10 04:25:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5ebc502-a552-302e-9106-45a4cddd5b20 | -18.17747 | -46.9898 | 2025-08-10 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 573d042f-7875-347a-a2a5-68ad4cd3e8a6 | -19.89021 | -44.4387 | 2025-08-10 04:25:00 | NPP-375D | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 277251a7-215f-316d-87ca-a0668936579a | -19.83846 | -45.92277 | 2025-08-10 04:25:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f156d54-6461-36dd-868c-18242916eaab | -20.14285 | -52.83779 | 2025-08-10 04:25:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a387758-1f1b-3ef5-81e4-47440aff3981 | -27.45652 | -48.45341 | 2025-08-10 04:27:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d66f8781-e231-3ab8-8a2c-b1d97a16ad0d | -9.3806 | -61.5315 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 8d4b8d5a-63a9-33ff-b1df-74e63eab59fe | -8.9399 | -60.7481 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 5e0a6950-64c2-3e75-85e6-5803acfe4666 | -9.3622 | -61.5133 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 831f4b9f-eb52-3b40-a056-fd56d3226fb6 | -8.9215 | -60.7297 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ed99773f-64a4-3d43-9ac0-22c477a5451f | -9.362 | -61.5324 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ca3ff1a1-c075-36db-81e8-599f08900d04 | -8.9213 | -60.7489 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 87c80781-ff0f-3db0-8de2-2115371614e1 | -9.3808 | -61.5124 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| ee966acf-adc1-3609-99ab-120072089999 | -8.9401 | -60.7288 | 2025-08-10 04:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.9 |
| ab7f5493-f3f6-3b42-9c3a-c2ffa4d26fdf | -7.08 | -59.1771 | 2025-08-10 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 99d59d68-a21c-3d60-b425-efee2b1127aa | -7.0799 | -59.1964 | 2025-08-10 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| a85231e3-97f8-3280-aa28-cfd2e361706f | -8.9215 | -60.7297 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 3d01f723-9064-3b2e-a6b1-99b38c0bd133 | -9.3808 | -61.5124 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 0d62e1af-ec33-3248-8fb7-33797a25ecc1 | -7.0615 | -59.1779 | 2025-08-10 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 82630f5c-1293-3ad6-b26a-ac87dd0e30a4 | -9.362 | -61.5324 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a516bd8f-26b1-3140-b78d-9d0e57dfa821 | -8.9399 | -60.7481 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.3 |
| db959caa-e886-3717-b111-786141976479 | -9.3806 | -61.5315 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 3731e4be-9a55-37b1-b5a5-328ec6800f95 | -8.9213 | -60.7489 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| a8cee2e1-d9c8-3d78-b17a-c1a0fdec989e | -8.5605 | -54.6771 | 2025-08-10 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 72e9620e-6e82-3ec5-9b75-7b42573fb219 | -8.9401 | -60.7288 | 2025-08-10 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 0d6c2dea-4215-3ad0-b974-6176da42fc39 | -7.0614 | -59.1972 | 2025-08-10 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| d22e59ed-548a-3c57-9dbf-8d1bf794a0cc | 0.69536 | -51.44507 | 2025-08-10 04:42:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15abfb00-ef48-37d1-b99c-44b17c1e309a | -4.94101 | -45.44576 | 2025-08-10 04:44:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e5a92fb-1e14-3b2b-a12c-52215fe928e9 | -5.47444 | -44.70286 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 40a01ba9-92dc-3048-ad27-2237efefe199 | -8.11823 | -47.43273 | 2025-08-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3b2b14e8-c831-30b0-89f9-7b57523a05b5 | -3.83959 | -47.74614 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31375b66-d2de-3b19-be6f-31d86d27c8f4 | -6.05369 | -43.7488 | 2025-08-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 08225bd7-8dea-341b-8607-3b6312f5a22f | -6.19426 | -45.44667 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6ac7d7d1-7402-3144-b9b5-0f4525084b46 | -2.37328 | -51.90851 | 2025-08-10 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22923468-dae5-3e89-94e5-54f240fab298 | -7.87108 | -45.55062 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5611d67-221e-34af-a249-dc4cdc1c8e96 | -2.37269 | -51.91215 | 2025-08-10 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9792922f-e604-33b6-82f9-fbbc950d906e | -4.4723 | -50.6735 | 2025-08-10 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc7fed6c-9570-315d-8011-340323a4c945 | -6.9676 | -44.48994 | 2025-08-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a416ad72-89be-345b-83bf-232f4a32b543 | -8.10994 | -47.43623 | 2025-08-10 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b31c201a-f20a-34aa-9e53-cf8955fffee7 | -6.40935 | -44.56754 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f766079-7db9-335c-aa01-c56b61033717 | -4.07246 | -47.97364 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f472702d-e7b5-3310-aa12-80939d0fdab7 | -7.87901 | -45.55605 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 301c79be-bba6-3cb8-9ab4-e708c28e3ecc | -6.98326 | -44.79873 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96b2f607-2c7a-3a16-b674-6a1b77bf139d | -6.58098 | -44.56885 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b66242c-183b-3810-8500-ac5a8848ab36 | -3.18888 | -41.85395 | 2025-08-10 04:44:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 756f197d-e28d-3877-99a2-7fb952abdd55 | -7.88756 | -45.55721 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf03914e-a5b1-3570-bd5b-f1d8436ed08a | -6.97618 | -43.86184 | 2025-08-10 04:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48a9c06c-9dc8-3c64-9395-d8871d007f32 | -8.36914 | -46.98166 | 2025-08-10 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eee67faf-76df-3420-9042-3bbb9c4c110c | -6.57583 | -44.57277 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7f73cfe-d8d7-372e-871d-2358fdc24201 | -7.72999 | -45.54003 | 2025-08-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67ac39da-a00b-3af1-9af4-0b741432c618 | -3.42686 | -49.04648 | 2025-08-10 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1ab6817a-b22a-3aee-90a6-cb4a16ac93d0 | -8.51309 | -45.70662 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0966eff3-f6ec-3cff-8f84-7abd283aff38 | -3.58847 | -47.52586 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41d6edc-caf5-391a-af98-d0475dc4cacd | -7.88231 | -45.55582 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9b808d3d-33b0-3e4d-b338-83e3e48e3f08 | -8.09698 | -48.87426 | 2025-08-10 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a699ad4-b78b-3f5d-b1ab-6b4f05757416 | -7.88269 | -45.5607 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d6989d5-ed00-3084-938c-04b83e5eb60e | -7.43199 | -43.98656 | 2025-08-10 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| c040909d-1b1e-36f6-a471-4578f90e44b1 | -5.59289 | -51.1297 | 2025-08-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 154e42a3-e41d-396a-bd59-d34aad52e311 | -7.87415 | -45.55942 | 2025-08-10 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bec3e71-b75e-3dea-849d-d4688f71d216 | -7.15757 | -44.06725 | 2025-08-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b26741aa-37a8-3f4b-958b-72404a515d30 | -5.47506 | -44.69867 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 52da6a18-4dd9-3a81-887a-44254117eaf7 | -7.16224 | -44.06798 | 2025-08-10 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5e585396-93a5-3bec-bc77-26d620a6e295 | -6.19481 | -45.44285 | 2025-08-10 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a1673ac-12d1-305a-a218-8bc066cee736 | -6.05768 | -43.75444 | 2025-08-10 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a14f9266-15c9-351f-bbbc-7a2060cb32d3 | -7.03846 | -48.91342 | 2025-08-10 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 993cdf91-c40e-3363-babd-adb41dd5f5ca | -6.94962 | -44.55277 | 2025-08-10 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 01e15fc0-aa90-398b-9b0f-c71c54211ad8 | -7.57237 | -49.6081 | 2025-08-10 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61166845-f94c-353f-82c4-3bd710d5ada0 | -7.69888 | -45.54442 | 2025-08-10 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fdf92e7-a8d5-3c99-bb1e-f7b96ba50b84 | -4.07306 | -47.96968 | 2025-08-10 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bed3b39-c382-3fb4-a78c-e55c68e6d817 | -3.58803 | -47.51972 | 2025-08-10 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67e741d4-3cec-3017-9488-ce2b32b62547 | -6.96313 | -44.48883 | 2025-08-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76187d52-1a65-3567-b5c0-a7fef692cad1 | -6.96671 | -44.48679 | 2025-08-10 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9123dac7-2a77-3cf1-a45f-383c1fcff855 | -6.33527 | -55.56588 | 2025-08-10 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 096e5a32-314f-385a-9f73-16058743a415 | -2.37046 | -51.90435 | 2025-08-10 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbc6e2be-9286-31a3-b927-76831a3418a0 | -7.39313 | -39.68127 | 2025-08-10 04:44:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5eb6014f-dd9b-35b0-94ac-cdc75bcadbab | -6.67349 | -44.73572 | 2025-08-10 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README20.md)
