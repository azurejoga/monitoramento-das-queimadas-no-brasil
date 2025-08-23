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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3dfe756-8034-3786-bbac-dd35652a8b88 | -9.0494 | -47.6332 | 2025-08-23 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| cd314d7a-5896-3f1c-89cc-0fa808930d80 | -10.4784 | -46.831 | 2025-08-23 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 7f2039f6-05eb-352e-b539-7d258d1816f8 | -5.8309 | -45.1693 | 2025-08-23 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b721f754-5aec-3177-99c7-1007b10400b9 | -14.3704 | -52.0386 | 2025-08-23 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 647165b2-caac-37d1-8380-c21eb73c99b7 | -13.4349 | -46.2573 | 2025-08-23 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 0bb2837a-67a5-3d8a-8d56-b9567a83b1d7 | -5.4365 | -60.1588 | 2025-08-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 31c368c7-f692-3093-8981-03aade402326 | -14.37 | -52.06 | 2025-08-23 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 187.3 |
| 7204dc88-6ee2-34a2-bfdb-76f2d7300d23 | -6.5858 | -44.541 | 2025-08-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 4f33b9e4-ab91-3622-87f2-b610967c9930 | -8.9388 | -40.6336 | 2025-08-23 14:20:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 169.6 |
| e8f253d6-bbff-3080-a817-2de3bb4dcdc2 | -15.0183 | -54.8942 | 2025-08-23 14:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9a3d13a3-a1b2-319e-9ef7-d7562eb9478d | -8.853 | -49.8843 | 2025-08-23 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| d7c77019-478e-3b96-8a8d-94e6567a4aae | -14.7892 | -45.4954 | 2025-08-23 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 8a69e3cb-2069-39e7-b000-0c2112035cb9 | -9.1897 | -59.6171 | 2025-08-23 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| d929cf48-0e96-366c-b77f-192bf4aa411e | -11.1396 | -44.7654 | 2025-08-23 14:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 209.9 |
| 046f7e8c-ed80-3f10-9d69-aa2815026f19 | -8.5943 | -62.6315 | 2025-08-23 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| bd754933-1698-3ca0-9a20-c81738c1fdf6 | -8.5944 | -62.6126 | 2025-08-23 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.9 |
| dabe1f23-e23e-33c6-9abb-031eb4001016 | -6.0972 | -44.6947 | 2025-08-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| e20c9447-c6a7-39ca-803f-743450a4660e | -9.1712 | -59.5987 | 2025-08-23 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| bb664437-64ad-3860-8ed8-55333c542656 | -13.4775 | -47.0453 | 2025-08-23 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f4186a6b-1310-3564-9e4e-e3fdef3e2203 | -6.5781 | -59.871 | 2025-08-23 14:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 1fab6134-1029-3fef-8713-2ee7b33aa9c1 | -6.37 | -45.5356 | 2025-08-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 772d18ba-0d85-34f4-89f8-b8bf38c2645f | -8.9579 | -40.6311 | 2025-08-23 14:20:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 133.2 |
| 9393f35f-13eb-3bf8-a6df-28e6f13a45c6 | -5.7615 | -57.5807 | 2025-08-23 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| adad566c-e180-33ed-98ee-f4f71950a053 | -12.7078 | -48.1206 | 2025-08-23 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3adaad5f-660f-3890-b713-be4be1702eb1 | -11.902 | -47.1177 | 2025-08-23 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 78de390a-3258-3178-bf73-86b3c8d94a4d | -12.1949 | -50.2397 | 2025-08-23 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 6314cdda-272b-3da9-b8f4-45c66deccb9d | -13.416 | -46.2375 | 2025-08-23 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 09b293e5-36ba-3836-82e3-1dd080471e7f | -6.3887 | -45.5342 | 2025-08-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a4a9b282-a9dc-3843-9d83-9dc6ca93fb5e | -9.9495 | -60.1754 | 2025-08-23 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 91615ac8-2651-3c38-8ed4-5fc647365f4a | -10.6201 | -50.1609 | 2025-08-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 17d3d95f-7ddf-31dd-b66b-5a216e209972 | -7.9447 | -63.0528 | 2025-08-23 14:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 08bf6d94-17a1-37a7-8c7c-217d17278195 | -10.6393 | -50.1375 | 2025-08-23 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| bf97de81-7cd9-3559-9b1b-9b235861a654 | -5.7429 | -57.6009 | 2025-08-23 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 008db4f4-cfc0-3ba9-afe0-5c886ec616ed | -6.3964 | -44.7396 | 2025-08-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| a593b1b8-008e-3a0e-9018-6272f3383ad8 | -5.9062 | -45.1185 | 2025-08-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a601e45f-f642-3c4e-b99b-65b563a893e0 | -8.527 | -48.8609 | 2025-08-23 14:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 80c9bea4-171b-3321-8ec4-29c36f9ea0e5 | -8.5272 | -48.8393 | 2025-08-23 14:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 77.9 |
| f60344ae-a11e-3f2b-bffa-4d2a0caf5bdb | -6.1189 | -44.3726 | 2025-08-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3d04325e-db9d-3e0a-822b-f4b2f7a017de | -7.6366 | -46.2823 | 2025-08-23 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3d869318-512e-31c7-b361-1385828db58c | -6.1187 | -44.3955 | 2025-08-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 69c64f8a-db67-33ae-ac45-4e7f44c3ac75 | -15.5385 | -51.7064 | 2025-08-23 14:20:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 77514774-f3be-33c9-a8e9-35e3a49f232d | -5.4364 | -60.1779 | 2025-08-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 865b3ce1-8241-3f5f-835f-a94c15241a53 | -7.0352 | -44.6396 | 2025-08-23 14:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 768cd589-4d10-3a0e-8f0c-fe622393ddf1 | -6.9649 | -44.1864 | 2025-08-23 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 71c937f3-9ade-3e06-b968-13063dc7ca3c | -10.8568 | -50.8396 | 2025-08-23 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 4ba00d5d-46c2-323a-9272-494f775a2b66 | -5.7431 | -57.5814 | 2025-08-23 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 294.0 |
| 82cff078-afb5-374c-9cf5-e6fa5f658b23 | -6.1187 | -44.3955 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| a4be0183-9bcb-39cb-aab7-50174d67cb1a | -11.1208 | -44.7449 | 2025-08-23 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 5e490d85-3286-3869-9e28-41e61db12e63 | -13.0481 | -46.3183 | 2025-08-23 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 88.1 |
| fa3c7b00-802f-38da-98a5-94011e783dae | -13.0477 | -46.3412 | 2025-08-23 14:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 39c9d79c-9bf7-3ae7-9297-f54a63a2904b | -6.5781 | -59.871 | 2025-08-23 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| b8e05fe5-ac5d-3ab8-9858-9b33255497ee | -11.6981 | -51.6603 | 2025-08-23 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4756ac79-64fd-3d03-aace-8f9e18f8ac07 | -10.6393 | -50.1375 | 2025-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| e84c6468-55d6-3506-ae3b-e9b6356033d5 | -8.8921 | -62.4297 | 2025-08-23 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 050ac2a2-d650-31a3-a6df-1b183499484f | -6.0972 | -44.6947 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 0334a7c1-529a-3ef5-b2ff-7bec700b5015 | -14.5079 | -53.0365 | 2025-08-23 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 122.6 |
| cc523b7d-7222-342a-9898-2b22136633d3 | -13.4775 | -47.0453 | 2025-08-23 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 74690c04-f936-3021-a7e2-1e7a562bc313 | -12.1949 | -50.2397 | 2025-08-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 1596701a-162d-3147-9505-faefb02cdd51 | -14.37 | -52.06 | 2025-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 161.3 |
| f41c2b9c-9fd3-3175-bfef-0c977f238fae | -14.6899 | -54.912 | 2025-08-23 14:30:00 | GOES-19 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| cf32e67b-70a6-31de-ab23-df49b2419881 | -5.4365 | -60.1588 | 2025-08-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 1d3ea14c-6a2e-3340-a9fe-aa2ba9c4558d | -11.1204 | -44.7681 | 2025-08-23 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 308.3 |
| dcb19462-2ce1-35d6-9a6a-2955cabacd39 | -15.5385 | -51.7064 | 2025-08-23 14:30:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 99a9a562-f800-325e-9592-5161171cdb20 | -7.6296 | -45.2464 | 2025-08-23 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 7e829ac6-4d6b-3815-a9df-3235f6280971 | -9.1898 | -59.5977 | 2025-08-23 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 92adc117-c1f8-33c4-b595-df8234494f90 | -10.6962 | -50.1314 | 2025-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 38b6de05-ccb8-35d6-98e1-87a4aa4adcb4 | -12.7082 | -48.0984 | 2025-08-23 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| dff4d8e3-bf61-3983-b84a-460b3df87641 | -14.7521 | -45.4091 | 2025-08-23 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 4228b580-86b3-3b39-95c0-b3435c62091a | -14.3704 | -52.0386 | 2025-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 9d5eec38-5089-37e3-8ce8-0038e3b4852b | -6.0784 | -44.6961 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a7457f3b-843c-33e9-af19-407c18fbed6c | -7.9447 | -63.0528 | 2025-08-23 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 126.2 |
| bc7ada8e-ea22-3697-8df9-0151c6006455 | -10.6772 | -50.1334 | 2025-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1c663f46-27c8-3c61-bd78-43dd668e22bb | -5.4364 | -60.1779 | 2025-08-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d4f6184e-6565-3cfa-b56d-256cd024949d | -9.0494 | -47.6332 | 2025-08-23 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 1974d754-5ca8-3b75-bf39-f405fe177be7 | -9.9495 | -60.1754 | 2025-08-23 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6bad4b46-18c2-3629-a5fc-0620b31943c7 | -6.6044 | -44.5624 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| df98f271-ed3b-3795-8d18-b2911228e5fe | -9.1895 | -59.6364 | 2025-08-23 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 985ca385-ec80-3a0f-8d9a-9fbd13625cdb | -8.527 | -48.8609 | 2025-08-23 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 117.1 |
| db4af32a-1248-3f77-af06-78d636baf884 | -8.9388 | -40.6336 | 2025-08-23 14:30:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 152.4 |
| 051ca963-b413-3990-a163-b98948f0f39e | -6.097 | -44.7175 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 1e75c4f7-14cc-335e-ab0e-faeaa5570360 | -7.9448 | -63.034 | 2025-08-23 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 4b06d744-ca8f-3fce-9038-b6a0b051bcf9 | -14.3893 | -52.0574 | 2025-08-23 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 68e30889-fb7f-3623-a5e1-9758dade3c74 | -9.1712 | -59.5987 | 2025-08-23 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| be71fe97-c887-3d67-9f3a-b81cad0f9c8a | -6.9837 | -44.1847 | 2025-08-23 14:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 55507a0e-f250-3728-8567-b924dbbca130 | -3.1347 | -58.0459 | 2025-08-23 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| cff989e6-3f9b-3463-a841-3432a39ece38 | -8.546 | -48.8376 | 2025-08-23 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2687b6b0-a608-3ed7-9c99-76dddb37bb47 | -8.44 | -48.2612 | 2025-08-23 14:30:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 50b19644-d0da-3d6d-a761-e4a5f88a9609 | -14.3523 | -53.1191 | 2025-08-23 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| d1ffb8a9-00e9-3b07-9f56-8ee6433dabc2 | -10.6201 | -50.1609 | 2025-08-23 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| abdd2ff1-6d72-3a4e-895d-41b0109c4acb | -13.4155 | -46.2604 | 2025-08-23 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 2d5d8a85-6442-3918-b1f8-4a40484e2212 | -6.5858 | -44.541 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5cd90dc2-ca6d-30f0-aa98-0891a17209dd | -8.5944 | -62.6126 | 2025-08-23 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 5223037a-56cc-38a4-b784-ae6bddfc79a9 | -11.1396 | -44.7654 | 2025-08-23 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 239.1 |
| 8e7b8371-df11-3649-a33f-c63d9adf23e4 | -6.1687 | -45.0534 | 2025-08-23 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b3bdc36d-705b-3dd2-af96-493ff89a5c05 | -13.478 | -47.0227 | 2025-08-23 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 75310fa5-878d-3dfc-9646-a4fab9102278 | -6.5578 | -45.4757 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| fb8fbae8-e7fc-3f7f-9b94-68635e673af5 | -15.2288 | -53.8481 | 2025-08-23 14:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 159.1 |
| a4b6d674-7e61-33e0-b58d-a9ae667571bd | -6.1189 | -44.3726 | 2025-08-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 189.9 |
| f05494e2-f4a3-3a57-a39e-c3504d3d0b63 | -8.5272 | -48.8393 | 2025-08-23 14:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 141.7 |
| f8a2b827-e888-3862-867d-3d0d361f222c | -15.034 | -56.3928 | 2025-08-23 14:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |


[Clique aqui para ver as próximas entradas](README92.md)
