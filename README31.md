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
| b97c37f5-838f-3f12-b6cd-ad3d4277f6f7 | -6.1037 | -44.35869 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb7088cc-bfa0-3077-8a2e-84bbe1643581 | -8.21483 | -44.42976 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c08e98c1-daec-3cdc-9622-fe828000d8db | -5.88358 | -50.15858 | 2025-08-22 04:19:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65255425-21db-3888-8269-dd6f4091d0e4 | -6.04302 | -44.44097 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 994b7689-9c7d-3e41-bee3-790b6119aded | -6.01054 | -42.85963 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4400a81b-9a87-3f7d-a98b-e6845e47ae3e | -7.75996 | -46.55326 | 2025-08-22 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5747ccbe-a07f-3dbc-89bc-8079c7298c7c | -7.8025 | -46.6195 | 2025-08-22 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b1e8e27-5aeb-3dd0-86a1-98f257fe23a3 | -7.04346 | -44.62374 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae1aba7d-7752-3f71-8e09-64966d54dbf8 | -7.22557 | -48.4907 | 2025-08-22 04:19:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5be04f07-0a3d-33b2-84f6-9b557c2305d4 | -5.87248 | -53.6346 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22c7cd5b-4a74-33b5-a94e-4ffb7e3a5da8 | -8.84425 | -52.03911 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| adb86e92-1fd6-3349-8f8d-4189d37cfcda | -6.44655 | -53.37778 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eab94fcc-ec71-3f3b-8747-bf694dd1e627 | -6.03512 | -44.12394 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9f1727c-f434-38d8-b95f-c7bb1e9861bc | -8.8516 | -52.04994 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 197ca484-7cd0-3597-b64b-2a6bd3297663 | -5.55876 | -47.68686 | 2025-08-22 04:19:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75a51e17-8bfa-3662-ba62-8cd872c89293 | -5.62872 | -45.83126 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29036af8-6431-3172-890f-3c9f284ad3d7 | -10.86281 | -50.8251 | 2025-08-22 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bffdb68-af96-3f5a-bb8c-9cf6d0ce2f34 | -5.93413 | -42.55885 | 2025-08-22 04:19:00 | NOAA-20 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f5e9b2db-9b6d-3bef-9a68-dbce83f01f68 | -6.89266 | -52.85995 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| af6bdd0f-4832-37c5-a744-2c648832beff | -12.52587 | -45.60662 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eacdfac4-c151-3d7a-a38a-b51b24d2da59 | -6.02356 | -42.82035 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86a9d0d1-686a-3680-9426-31ba75e26321 | -7.69132 | -46.93736 | 2025-08-22 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ec5a153-9dfb-3b65-bb3d-1cdeebd4f967 | -6.04561 | -44.35988 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23cdb418-d3c9-3125-8edf-a8b5dc3b69bf | -6.94564 | -44.5551 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35bf25d3-fc74-3bb8-8bc9-ecdeb1aa7b8e | -6.27282 | -44.96637 | 2025-08-22 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d2427ef-3591-390a-9cbe-130cae91ca8a | -7.95714 | -42.63581 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e4fe522-2cfa-3001-a0d4-c149c27d10c0 | -7.19189 | -45.16903 | 2025-08-22 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9084ce77-ea9a-334a-8798-802a45c7b882 | -7.13746 | -44.17508 | 2025-08-22 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd721be1-edbc-3964-ac12-8a7945fb0e0f | -8.2898 | -47.27092 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 511c4408-a410-3559-84fb-38d6be52efb8 | -7.26516 | -43.67727 | 2025-08-22 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0146559f-13fc-37df-9904-a0dff07541ff | -8.41537 | -47.9034 | 2025-08-22 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a6f591f-0b7d-3456-9dee-0f0eb7643476 | -9.9416 | -48.34174 | 2025-08-22 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 568e7641-1c60-33a3-baf5-52d25228b661 | -10.69557 | -48.21355 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f58df28-66e8-32f5-a530-a8736002794f | -11.04962 | -44.5956 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56d58c2d-a962-3976-870a-9c6be2d0c258 | -7.46818 | -44.44859 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48961d6f-7867-398a-9759-1dce2415f9b6 | -7.1552 | -43.22704 | 2025-08-22 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3aa58f9e-fc02-3a09-81fe-6351c54384f3 | -11.28557 | -44.94053 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b95cd1ca-21d3-3131-9575-80cced0b3984 | -5.87364 | -53.62795 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c960d28-1291-3083-9081-ede751c4341d | -7.85469 | -46.99004 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 289a2766-5d2e-3671-aebb-c68b4ffb49e4 | -9.59322 | -55.35351 | 2025-08-22 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82d74c57-3c09-3db5-bb34-3473f9d3321f | -6.29524 | -43.89338 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b650485-c290-3b0a-a309-dbba70d63e5d | -6.26474 | -53.67376 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64c4497a-fccf-3e58-abf6-6bc7120d1d46 | -12.58337 | -47.0914 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9aa7ffbc-e9ba-32be-901a-89d2ab741a67 | -8.50292 | -44.73727 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e5aad39-211a-3c71-a06d-c16ffd08f935 | -6.28749 | -43.7015 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5af9640d-4ed0-30fb-be5c-410144bdcaa4 | -10.22272 | -48.28755 | 2025-08-22 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5986a7e7-cf54-3ea6-8dcc-27c84ab194ba | -11.43287 | -47.31265 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef4dc80a-3693-3f15-967b-0c6ef175b8a2 | -8.57975 | -48.55079 | 2025-08-22 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 31615bc0-5ee9-376b-aed7-3cca0b073a6b | -11.28446 | -44.9477 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5070687-e001-3ce2-bf3b-14388eaad12f | -5.85933 | -48.16204 | 2025-08-22 04:19:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b621ff8-f829-35a0-bef2-dbef4f297ee0 | -8.90715 | -47.33492 | 2025-08-22 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3c6720c-03cf-34af-a52a-78705453c027 | -9.82906 | -45.95599 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd235dec-2aa0-34bf-bf6b-342eacd97e15 | -12.63611 | -46.86607 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9101117-60ab-31cc-9f7f-af6e25642520 | -4.8896 | -55.98703 | 2025-08-22 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f544168a-a28a-3ff3-acf0-59a0cc126d49 | -7.85002 | -45.19592 | 2025-08-22 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2069ead-cf77-377d-84a8-d021712259d0 | -6.20682 | -43.56577 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 47f240a0-d983-397f-8e82-3cefd05603e9 | -6.89168 | -52.86554 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb42917f-3288-395c-9212-5d09bb860c9c | -6.55706 | -42.99476 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dceb98ce-3c8e-3f50-a629-e1eca6bdd39d | -5.67679 | -52.21538 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 525f52db-71a1-365d-899c-56709e9a678f | -7.85628 | -47.00183 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2aeb8cd3-14bb-3db6-8c9a-bbc4938ea67a | -5.8805 | -42.40742 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ef4bf8a1-a0b1-398c-b397-b2e56ab0b1ca | -6.05082 | -44.00174 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfc3f006-9856-3809-a742-0d6d1201090b | -6.03405 | -44.36871 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aebafa7f-1bd1-369b-a8d0-7ff30dec86bb | -11.27335 | -44.95323 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3124fa4d-9b6f-395d-b32e-a25dacc2d4d8 | -1.09123 | -45.84954 | 2025-08-22 04:19:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 106c88fc-dc6a-3e62-ab55-26f4bf7f7376 | -12.00473 | -44.66875 | 2025-08-22 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae03e0a9-7feb-3373-a704-d50e3e94378b | -5.52321 | -46.41985 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1c7d5e70-195b-399e-8cf7-42a6f69cbaaa | -9.86377 | -45.95077 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca6944b4-6a8a-30ef-8828-dff4f70ffadd | -8.12917 | -47.15597 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cc1cb9a-095d-36d2-8032-ff4dcffebb06 | -7.85811 | -46.9906 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 708bfa61-4b40-3292-859c-ba570081f1df | -6.49298 | -43.45337 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4c97985-3377-32d8-a848-952503283c82 | -8.27825 | -47.27677 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57997c8d-0c4f-3215-a8e0-99ae966ff92d | -7.04069 | -44.61975 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 712b7d7d-6412-37f9-9483-ddf28ceed5e9 | -11.05407 | -44.58892 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60f8697a-5bd7-355b-a3ca-64897ce5df6c | -6.30135 | -43.89791 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bbbb2ab-44cc-3758-891f-1324837353ef | -5.87944 | -53.62576 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a1eeda3-ceeb-3103-8de9-bfc6e25b33df | -10.73206 | -48.23156 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ec9821e-6a71-3da7-a44b-a2c34bd78642 | -7.65242 | -45.24227 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6cded1fa-f590-3117-b6fa-347e4475f231 | -9.15348 | -59.6051 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| acfa8186-e56e-32f9-a896-5e5a6a541ef0 | -6.31099 | -43.74837 | 2025-08-22 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a6598eb-5fa7-3ae8-ab39-9606cef62c7c | -8.84801 | -52.04399 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 045452d1-2476-3eb7-b2a7-1a49f27a3db5 | -9.20515 | -59.45894 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 344b7bc0-652f-36fe-a78f-f643a6fd6ad6 | -5.88301 | -53.63638 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f95a19b-71e3-3c6f-b6c3-c4657aa88c2a | -6.45006 | -53.38781 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22aac63f-184f-38c0-b824-1091e035f078 | -6.01786 | -42.812 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dbd35f57-953d-3339-9fe1-b74131912de5 | -5.87536 | -53.61811 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb366a7a-8c36-3a8b-b1c9-62621caf72d4 | -9.13567 | -46.38139 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 8be0c394-61de-37ff-aca3-5e5edcef627d | -6.44467 | -44.522 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a55c78a9-3ebf-34cf-bce8-86140fa8b5cf | -4.73966 | -48.01817 | 2025-08-22 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2606a5e-8eaa-3fb5-8da6-3cffc9e68d7f | -5.83249 | -45.98092 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99171b16-cfd4-3da6-8953-482247c2a554 | -11.43682 | -47.30959 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 926e7229-d87b-3809-b062-ded46f635709 | -10.6785 | -51.56752 | 2025-08-22 04:19:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e628c397-cb07-3318-b576-6e6abef8018b | -6.84335 | -43.70745 | 2025-08-22 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 458c630b-749b-3aaf-bd94-648882eb5bdf | -12.64756 | -45.32736 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fed3228-29a0-34b9-bd6e-0a3756274dae | -7.25452 | -44.7071 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6fc306e-763f-37b1-b29a-7a5e0c5e31e2 | -6.02634 | -44.37459 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01e2adbf-3fa1-365b-91b5-84061a72cfc6 | -8.90723 | -51.04081 | 2025-08-22 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e544e765-25c3-3a70-85ab-a8219abd4328 | -5.79103 | -45.07025 | 2025-08-22 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 957a62e6-2fe7-34e9-9cc3-d94cce49f188 | -11.30647 | -44.95466 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e50c7ee2-30dd-372d-a88d-bcf12d2069f0 | -6.21227 | -44.12004 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
