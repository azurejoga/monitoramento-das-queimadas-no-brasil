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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b16de580-ec47-3a37-af7b-d3ca248fc9e1 | -8.05 | -46.2663 | 2026-09-20 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f0efe8fb-c868-30dc-a1f3-2dbf3dccace8 | -11.9678 | -50.1379 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 8754a6b8-c32e-30ee-87ec-2bcab472b9e1 | -11.041 | -54.1567 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 9dc62c57-deb8-3f4f-a902-d1cf9acf182d | -10.8909 | -54.0882 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 15b81052-d196-3826-94ba-4d0db394d550 | -8.4797 | -57.6282 | 2026-09-20 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| dc17bead-6bcf-384c-ae4b-802b22a5023e | -10.8757 | -57.1554 | 2026-09-20 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2cd36834-f4c5-39f7-8d93-7c90839c2f20 | -3.2361 | -61.217 | 2026-09-20 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 94455741-8ff9-390d-a786-e28e20cbaa10 | -12.3404 | -50.6942 | 2026-09-20 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| fdba498b-a93d-3590-91fe-33f50edddf1e | -7.3259 | -55.6153 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 196.0 |
| 7b091b32-495a-3e12-ac12-abcd22c2b2f2 | -8.0892 | -55.3511 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 3348b545-4df9-3751-af90-99f19382a0ec | -8.1688 | -54.7432 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| b067b1d3-8880-385c-830b-2ee9f0a235fa | -11.0259 | -48.2944 | 2026-09-20 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ea286bae-db49-3608-b70b-260cc89e8752 | -7.0098 | -45.257 | 2026-09-20 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| e1fd2999-31c5-38bd-8923-4195646627f8 | -11.3603 | -51.4009 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 71e9d1e3-ff5f-3e66-b329-bcc795a8b4c2 | -8.1378 | -46.7933 | 2026-09-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 9ecac082-8049-336d-9a3d-1003aa552162 | -9.784 | -45.059 | 2026-09-20 14:20:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e0eee070-8d8e-3df9-a038-c902b3ad1d0c | -6.3382 | -59.9566 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 11401848-8d13-304d-a854-77c84463ce53 | -8.3774 | -47.1917 | 2026-09-20 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| b5336d2a-aaa4-3c72-8d37-f310d5126157 | -6.5763 | -45.4968 | 2026-09-20 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 0e276f52-4126-3309-b4a4-68ed52e5172e | -9.5539 | -46.5807 | 2026-09-20 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d524cb2c-7885-3695-9e9d-17f7a41b1638 | -11.1222 | -49.4818 | 2026-09-20 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 162.5 |
| f87c7c32-c6d5-320c-ae98-2a91beb9ef53 | -8.9269 | -49.9843 | 2026-09-20 14:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d3437d49-ebc9-3f75-a214-3ce2734306d2 | -7.5525 | -45.4123 | 2026-09-20 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 82f62b7f-2878-3144-afba-1e958509147e | -11.1225 | -49.4601 | 2026-09-20 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 326365b2-f6e8-3979-90d4-7a93d42ba846 | -5.9151 | -59.9522 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ab84c00a-f82a-392f-ac9c-c90f52daf224 | -10.9694 | -57.1881 | 2026-09-20 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| ecfb0859-8c33-3441-b957-79134fd2cbea | -6.7185 | -55.0684 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1dd08b3e-2b85-39f7-a419-5731e108b83c | -13.5911 | -51.458 | 2026-09-20 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 217.2 |
| 6eeaecfe-a053-3581-a887-b2c20cf0ebd3 | -8.4737 | -47.0053 | 2026-09-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d842bcce-926a-3e8e-9275-ef6c2b7ec5e5 | -8.0464 | -61.3618 | 2026-09-20 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 72930810-e8e5-3dc1-8a08-89ca4be56d19 | -9.2603 | -45.939 | 2026-09-20 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| b0b0a976-36ad-3fdd-8e22-e00f3cbcaba3 | -11.3813 | -44.0554 | 2026-09-20 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 6ef882ba-fbd9-32b3-8333-ca9dbc34d78c | -6.3199 | -59.9381 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 117.4 |
| cbf54c70-c466-3151-b882-dcaf70f68a41 | -10.7708 | -46.3453 | 2026-09-20 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 4d8d9370-65e0-3bff-b22c-ae578b1eeb41 | -6.4301 | -59.9916 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| a1566114-3b8e-3e22-91e6-a5e8b1eaa7d5 | -8.4312 | -45.8693 | 2026-09-20 14:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f14866d0-004e-36e8-ad52-2f7f6bf0f765 | -15.8856 | -49.9145 | 2026-09-20 14:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 62479c01-d9fa-3b9c-9f1d-878f58b84b52 | -11.3612 | -51.3374 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 686205f6-3db0-3ffc-9ee8-7831c2993135 | -3.1079 | -61.408 | 2026-09-20 14:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 1b65f87c-79a9-366e-9158-6f8360511074 | -10.7115 | -60.7312 | 2026-09-20 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 7c57b09c-9716-3080-b299-d096f4403f9b | -11.75 | -50.6993 | 2026-09-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 764feed5-e60d-3dc6-bdc7-66022b558a0a | -10.4544 | -51.2616 | 2026-09-20 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 07cfb080-6f9b-331e-8a5c-ca7556f81d7f | -12.5415 | -50.046 | 2026-09-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 95771f67-e0ec-3b65-965b-931f79aa282a | -6.737 | -55.0674 | 2026-09-20 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| b708c789-b029-3be1-9b55-cdacf6cfa12e | -10.41 | -48.933 | 2026-09-20 14:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 16e0a738-84c2-370a-ae46-11fa5ce499ec | -6.4671 | -59.9711 | 2026-09-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.1 |
| e7a8880c-6f33-37db-bf69-a95fbbcfd2c7 | -12.8896 | -50.991 | 2026-09-20 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 100dea3b-8e59-3011-82d1-4de44ee3ae3b | -9.3609 | -48.3251 | 2026-09-20 14:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 59b2d9a8-cb70-39ac-bd57-a4361e67a499 | -11.0596 | -54.1755 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 29891b87-3bd5-31dc-92c7-3cb52d44d2b2 | -11.6429 | -47.7761 | 2026-09-20 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2fdc8cb2-72a6-3d01-9a49-6792585219be | -12.5419 | -50.0243 | 2026-09-20 14:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 30cdb263-c054-3266-af25-ecf82af49586 | -7.2519 | -55.5994 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 806eb624-b3e2-369e-b432-445726701c2c | -11.0994 | -54.008 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 4a1cd686-9819-32fd-82c5-d2fc11d0e9e4 | -7.0262 | -42.0685 | 2026-09-20 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| af791fc7-3238-37ba-b3e2-de394e7e99c2 | -8.0708 | -55.3321 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 872845f3-416e-33e5-9585-a58c910e291a | -7.0455 | -43.6928 | 2026-09-20 14:20:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 658b653e-3f0e-3905-bae7-1f3b7b415347 | -17.5795 | -44.9765 | 2026-09-20 14:20:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 23bb10c7-1f6a-3e60-9d03-ee5a72c1af8e | -11.1183 | -54.0062 | 2026-09-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| f035aa95-6307-397c-b3fe-c2e1ee1e521f | -8.0894 | -55.331 | 2026-09-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| e9e8dba3-dcbc-32cb-b22c-62baa087f599 | -12.1516 | -47.0608 | 2026-09-20 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 90dae82e-e815-3f31-bd77-427a1546c1f5 | -2.8974 | -57.7987 | 2026-09-20 14:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d027dc5a-622d-332b-83fd-56a7f45f6771 | -11.3787 | -51.4412 | 2026-09-20 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 169.6 |
| 43653772-90f4-30b5-a7aa-2dd337e560db | -7.0262 | -42.0685 | 2026-09-20 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 132.5 |
| bb016cc0-7234-35d4-a286-fae909b5a6ba | -11.379 | -51.42 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 232.2 |
| bc186ecd-29e4-305f-9aae-4d44b66982da | -6.7185 | -55.0684 | 2026-09-20 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| a33f4a3f-0b15-3b9e-a5d2-f14a8a196d6e | -12.0263 | -50.0447 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 38085405-1233-3e97-953d-0f5a2d121687 | -7.1392 | -42.0811 | 2026-09-20 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 0d369204-2b7b-361f-a71f-8c7b001bf756 | -9.8502 | -48.4053 | 2026-09-20 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 1db74315-bbf8-32b5-bbb4-888a3e4186d7 | -12.0072 | -50.047 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 70d6a55c-63fe-36b8-8cef-5381b0dd4840 | -13.5911 | -51.458 | 2026-09-20 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 9fd13f77-729b-3c67-b3b6-66e4ba4923fc | -12.7653 | -52.8661 | 2026-09-20 14:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a42914c8-523f-3088-ae90-ebdc507081fa | -11.3612 | -51.3374 | 2026-09-20 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| bc3a020d-806c-3d1e-a693-377331f67905 | -3.1079 | -61.408 | 2026-09-20 14:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 6cc43b84-5ce6-3b34-80e2-bd3a64fd3494 | -9.784 | -45.059 | 2026-09-20 14:30:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 246651ef-1e6f-3982-bbd5-2bb655ea1a04 | -6.9414 | -42.907 | 2026-09-20 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| f6bb78ae-d071-3d4b-a2ef-f6607c493dbe | -11.4345 | -45.3919 | 2026-09-20 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 1abeb064-f746-3c88-9062-4b65ed497482 | -11.6433 | -47.7539 | 2026-09-20 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c7768f4d-4c11-3cd4-8177-6e5b88dc460a | -7.3259 | -55.6153 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 0f31a679-a0e8-31fd-bd16-783c995f116d | -10.2793 | -50.2177 | 2026-09-20 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 7d74d882-89a5-3878-9d09-815dc3540229 | -2.9157 | -57.7983 | 2026-09-20 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4dacc232-ba66-3402-aef3-400e82a53cfd | -11.1222 | -49.4818 | 2026-09-20 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| d619cd27-ddae-3e77-ba88-16c9d1ea9e73 | -11.6624 | -50.1954 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5d012a8e-06c7-329a-bc6c-e3785678161e | -10.8364 | -50.9479 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 288.1 |
| dffe01a4-cb7a-360d-84b9-1c5716638a7d | -9.0353 | -48.7704 | 2026-09-20 14:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 900a0204-5d0c-3eac-840e-e1a3ad54641c | -6.9225 | -42.9088 | 2026-09-20 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 87a96cbf-16fe-3d08-90eb-9edd04d50745 | -8.1378 | -46.7933 | 2026-09-20 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| d15ff6d1-4c78-364b-be5c-14812815a6ef | -10.9692 | -57.208 | 2026-09-20 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| dd482406-0810-3378-b383-d91bbe59b578 | -12.8708 | -50.9719 | 2026-09-20 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| be64fdb0-8bc8-39d9-adc5-9939155d7838 | -12.1524 | -47.0158 | 2026-09-20 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| cd3bee35-a71b-3fa4-8b86-bd88aa10454b | -10.8028 | -50.6326 | 2026-09-20 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 7f28492d-361c-33d7-851b-13d477c76049 | -7.7489 | -44.6873 | 2026-09-20 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2b0120cc-26e5-3f03-b153-f96bd1c7a540 | -2.9157 | -57.8177 | 2026-09-20 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| c6b5c896-7c14-34bd-a9c5-9948acd7149d | -7.2704 | -55.5983 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| b61a4725-cb09-3300-83c5-c88a9e6760f5 | -11.8744 | -50.0199 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 329.0 |
| c79a3843-14ad-3266-a7e8-0ca738264dab | -12.1328 | -47.041 | 2026-09-20 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4891700e-d72e-3de4-997c-9c223c0545fb | -8.0464 | -61.3618 | 2026-09-20 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 20cec268-60b8-3f2c-b70f-afac6ebd7c4e | -12.8701 | -51.0148 | 2026-09-20 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 192.3 |
| d824ef4d-257f-3ad7-b0ba-b68ffb034eb4 | -9.8404 | -46.3911 | 2026-09-20 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 23fb52b5-c095-311a-af14-15aa466e404d | -12.027 | -50.0015 | 2026-09-20 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 7db0798f-04f8-3ce2-8e36-dbdfab45c1d0 | -8.0892 | -55.3511 | 2026-09-20 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |


[Clique aqui para ver as próximas entradas](README128.md)
