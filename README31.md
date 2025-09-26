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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f5ec675-3aa0-3c3f-abb4-0125ac60a2fe | -5.73984 | -44.97155 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4eb9af99-4b2e-36f2-b6ce-d8a017eed98a | -5.22193 | -44.49013 | 2025-09-26 04:42:00 | NPP-375D | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1cd5dbbb-f0c1-3f36-ba7e-a182032e6a94 | -7.31528 | -45.76568 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d21b881a-eb71-3cf8-81c3-41b719a49edd | -8.62548 | -50.01561 | 2025-09-26 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e729e626-8346-3261-bad3-41740288fa4f | -6.87617 | -44.50566 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 325e2405-2c2d-396a-8be9-89cf8042e89a | -9.55481 | -47.51994 | 2025-09-26 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 11be5f39-230c-3c07-b3ba-9b7243f88664 | -7.46023 | -41.91891 | 2025-09-26 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 08576122-e894-3717-b13e-95b542ff0519 | -5.30151 | -42.76476 | 2025-09-26 04:42:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84ab23e7-3236-334f-9c96-b8db1e7610b8 | -7.115 | -43.74127 | 2025-09-26 04:42:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 807f7314-8f63-317a-a0a6-cca9ed288de7 | -7.58836 | -42.3256 | 2025-09-26 04:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb50cecf-1add-3842-9604-f031e5fd5780 | -6.26468 | -42.4888 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 17c9961a-51c5-3eec-96b1-908325bd8b03 | -5.75981 | -42.91004 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4f49222-2efd-3ae1-95ae-08e9bd302146 | -7.00747 | -46.99968 | 2025-09-26 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11521949-af42-383b-b33f-2f147fbc29a8 | -9.52554 | -51.31115 | 2025-09-26 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6518ee9e-f6e5-318a-96e0-c47da8247ae1 | -9.24413 | -44.26509 | 2025-09-26 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9894429-1429-3a82-9c8a-636ca4d2fcda | -6.26401 | -42.49337 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9ec68158-c86e-306f-b88d-a39d33134efa | -9.9523 | -46.27841 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08274464-8020-3d24-9824-0a404e8ffbbc | -5.62611 | -43.92566 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2866d513-0839-3273-bfa4-6a767db0ea3a | -6.82491 | -44.17269 | 2025-09-26 04:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6a65247-d222-330c-8f19-964efdc4a896 | -5.80346 | -42.80036 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1f5411ac-7a76-39d8-8687-3ad556c9bf21 | -9.10551 | -47.61831 | 2025-09-26 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f725e46-209c-3dea-a8c3-e818c65030aa | -8.49635 | -49.54772 | 2025-09-26 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ba8e3c2-910d-3e74-8e94-2282119e9577 | -6.04027 | -43.34512 | 2025-09-26 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4ec9084c-ff3b-3133-88ed-58893c75f738 | -9.86646 | -48.87677 | 2025-09-26 04:42:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1fc40d3b-64d9-3e92-ab1b-9a0da4a33196 | -5.97907 | -43.78339 | 2025-09-26 04:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a38b6401-4537-3c95-bc5f-37a43e7fdd5c | -3.68591 | -52.38684 | 2025-09-26 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59482c4b-88d2-3344-b0a4-d6e358cf912e | -9.11243 | -48.89938 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bb156e8-3921-3d4f-9f6a-83dd77d05e48 | -10.00371 | -44.17484 | 2025-09-26 04:42:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aec154f5-506b-391d-9b35-a2fc7566795a | -5.97531 | -44.13069 | 2025-09-26 04:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5e81a25a-0132-3f5b-a172-c045f5ac3bd6 | -7.31458 | -45.77026 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b8e4527-cb09-337d-b3ec-2ee1af431205 | -7.11367 | -42.17318 | 2025-09-26 04:42:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 293e73b5-05f0-3f73-b491-3f130567349b | -5.69213 | -44.44818 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9ee5bd41-756e-3663-bf85-bac4f5c8b61a | -3.66497 | -52.15162 | 2025-09-26 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f33ca49-0521-3888-8e8a-e2e55d806a33 | -10.39305 | -46.14407 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4a88a70-be00-3f08-896b-aeeb9298f91c | -4.48585 | -47.67303 | 2025-09-26 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 184ad689-3f13-3992-af4c-ea498052960e | -10.40482 | -46.18233 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 133a8afd-7efe-3c80-9bf1-6e2418c43959 | -5.31351 | -43.1419 | 2025-09-26 04:42:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6bfeb76d-206e-3638-bf5c-a85e9b54f10e | -7.19861 | -45.35726 | 2025-09-26 04:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8588e138-9058-3506-be5d-aa22903438a2 | -5.78828 | -43.32682 | 2025-09-26 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18163f2e-ee5f-330a-a13c-80c6eb4449a2 | -5.74112 | -42.56292 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| da6b6fc5-82e0-3a07-a433-eb4dba91d540 | -7.27493 | -42.9781 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3bb1ca88-5231-3df2-b98e-9ac76c7739eb | -6.26011 | -42.48785 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 10174ed7-c258-35ab-af13-b4e5cc3adff3 | -6.71748 | -42.74133 | 2025-09-26 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 288a50e1-5aa3-3609-9af4-184c92b41e8f | -5.52552 | -42.73164 | 2025-09-26 04:42:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d3fe8834-a5b2-3d9b-b417-d9862140a9ed | -6.13495 | -43.45835 | 2025-09-26 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6e756239-2d61-374c-9241-1e50e13f0720 | -8.8584 | -46.21051 | 2025-09-26 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d5b6772-e867-3e65-adfd-4039d1636d97 | -6.25622 | -42.48216 | 2025-09-26 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ba1e043b-c957-3368-9f89-186542ecfe25 | -5.1221 | -45.49688 | 2025-09-26 04:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e89e704f-7d02-3720-bf8f-c657d5064bf7 | -7.31231 | -45.75809 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f10ca28e-5b30-36f6-aeb2-76e87fd5c58e | -6.0921 | -49.86619 | 2025-09-26 04:42:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76b30218-5edf-3744-ad13-56dd6e7adf54 | -6.04091 | -43.34083 | 2025-09-26 04:42:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fba9ac95-b1fe-3859-80ad-74e9e70be039 | -7.45793 | -41.91743 | 2025-09-26 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d0dac70c-9056-379d-b104-75a8a0430ef6 | -8.61765 | -54.9956 | 2025-09-26 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95a5b844-a5da-3500-b8bc-9f7006852601 | -10.40233 | -46.17225 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8484e5e9-96a4-3bb1-8e71-12995576415d | -5.29106 | -48.1252 | 2025-09-26 04:42:00 | NPP-375D | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa1666a7-716b-30c4-a864-2ace91084383 | -10.18903 | -44.83812 | 2025-09-26 04:42:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 519132c9-8f9e-37e9-8645-eda428aea0dc | -8.51731 | -44.62537 | 2025-09-26 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 646db0c3-4ffa-34b5-aba6-bd17194406fb | -10.23824 | -47.03002 | 2025-09-26 04:42:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a63976ac-4b08-3b13-8930-5910d2365dc3 | -5.43092 | -45.13652 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54a2bff8-e235-364f-a6b8-e028a216c548 | -7.59509 | -44.43081 | 2025-09-26 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d22a38e0-1dc4-3f56-8dfe-8afba1676d43 | -10.40933 | -46.17824 | 2025-09-26 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1f61debb-cedb-33a4-b16b-0ab48d44dce9 | -5.46855 | -43.06363 | 2025-09-26 04:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3737c54c-4220-3a90-9a00-9651c9a708cb | -8.19521 | -46.39131 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7931a264-da9c-31e7-8a96-24973caced0c | -8.51678 | -44.62905 | 2025-09-26 04:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27e3b971-00a1-317b-b96b-ab04e18fe99d | -5.63385 | -43.93057 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8cd9519a-ba07-32b1-862a-cd74ad7aaf64 | -3.73825 | -51.18182 | 2025-09-26 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5df74f8a-5901-3ce5-b78c-1e3251aedf3f | -9.11298 | -48.89577 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ea509a2-d21a-3a34-a5a5-84efafeddbcd | -10.11549 | -45.32979 | 2025-09-26 04:42:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52329bc9-1e85-3a05-9f56-f8eb14a7293c | -5.7649 | -42.55846 | 2025-09-26 04:42:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 76602862-67e8-3cff-b01d-1b56356b3545 | -7.28398 | -42.9795 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c29476f1-d0de-3589-87e6-865951eaf930 | -9.36748 | -43.74586 | 2025-09-26 04:42:00 | NPP-375D | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f9a05790-45c5-3029-a466-1be958c609d2 | -8.84581 | -46.60926 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 88ba7571-7b88-3b95-b65e-1e7388954e77 | -5.7825 | -42.7559 | 2025-09-26 04:42:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 24ea1ccf-e6ca-3435-9efb-fb741a386320 | -6.95789 | -43.24508 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 33ce578a-ec29-3799-b14b-522276c12d22 | -4.81839 | -42.74295 | 2025-09-26 04:42:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6a2d134-e489-3379-a7be-1b1ba2f42c75 | -6.88022 | -44.50631 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 642b8c24-4172-3ead-a209-573997ecc4ad | -4.79836 | -47.28049 | 2025-09-26 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30033721-2630-36a3-8ff5-d7972b3c4cdd | -7.25612 | -43.0122 | 2025-09-26 04:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 310cf19c-656f-3f65-8a1f-caf729cdb5d6 | -6.6909 | -44.6119 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65d226bd-3990-358d-8d32-e0cf5756d15c | -5.73012 | -42.63641 | 2025-09-26 04:42:00 | NPP-375D | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ad3203ec-8157-319c-be53-6889f4e7b37c | -8.84947 | -46.60988 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7791774b-2182-3c0c-99ba-662b68a72193 | -7.31288 | -45.75597 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b00971d-469b-3b17-8ce3-2b74920b3dbc | -9.70737 | -48.2537 | 2025-09-26 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d17cfe0-3338-3226-9890-e75b9ce2b3da | -8.67161 | -43.99503 | 2025-09-26 04:42:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b5c4da0-247a-3556-b83d-13189e3a7f93 | -7.31165 | -45.76267 | 2025-09-26 04:42:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f08534cf-2736-3b66-b6e2-d190bf8f07c3 | -7.68673 | -45.98421 | 2025-09-26 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b20db0dc-0fb7-3291-9196-caf54a66e56c | -9.11353 | -48.89217 | 2025-09-26 04:42:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3705518-6fb0-30f9-91c6-2e5e81a7f1ed | -5.53638 | -42.81435 | 2025-09-26 04:42:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a9a052cf-8170-31aa-84df-81b6c88d7b55 | -5.74302 | -44.97691 | 2025-09-26 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 175c339b-4930-3b9c-a794-59f3f7a9f933 | -5.69331 | -44.44532 | 2025-09-26 04:42:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b0778244-6999-326e-8421-fc8f4e6a39c9 | -6.42537 | -43.07201 | 2025-09-26 04:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d811aef5-79ba-36cb-81f6-d70005a226be | -8.13543 | -42.37644 | 2025-09-26 04:42:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 64d3c0ee-a472-3fb6-87db-fd18dbaf1585 | -7.77688 | -43.92216 | 2025-09-26 04:42:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1cd9dbc-f07a-30ef-88ce-0d5a7a2c2650 | -7.17895 | -42.23029 | 2025-09-26 04:42:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 768b5df6-242b-3a78-95a9-8cb6901dab92 | -4.2637 | -48.55097 | 2025-09-26 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a22364b6-acac-3add-b1f8-baa1fa145d32 | -3.68221 | -52.38623 | 2025-09-26 04:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2670213-1ea7-3197-8374-39de1e8d1749 | -6.33193 | -44.01567 | 2025-09-26 04:42:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1271f7c-d722-3554-a5ed-f990536177fc | -5.61855 | -43.46529 | 2025-09-26 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32f8ac3a-4281-3ce4-8e61-99bf7f913923 | -5.53022 | -43.87787 | 2025-09-26 04:42:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5516b91a-f190-3bd9-ae59-71be39aa27f8 | -4.75291 | -43.26792 | 2025-09-26 04:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README32.md)
