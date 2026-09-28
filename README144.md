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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9c13d294-39ae-3d63-beda-075bdf5048be | -10.9086 | -50.66068 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9baf82a0-d4a3-3070-9100-0b7dd67fc588 | -7.03326 | -45.81757 | 2026-09-28 17:09:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f08bc58f-722f-3df4-8e33-05ed13b28f14 | -10.81757 | -57.19406 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| c547a242-433a-3bc1-9b59-4b8e9d43467f | -9.44939 | -41.81553 | 2026-09-28 17:09:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 42.5 |
| 4adc94f3-0a6b-3788-8ec5-4152b5221a87 | -11.51064 | -47.40309 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9376ade5-2eda-3a78-bf52-862da3e6ba6f | -11.85943 | -50.88958 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ccdf72ec-beef-3d51-a565-77b564c76f9c | -10.86444 | -48.50893 | 2026-09-28 17:09:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15b32a4f-7d9d-3a30-8115-34a220974379 | -8.28649 | -54.74099 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 5d2218e4-851f-3d58-b67b-6cbb85a8652f | -8.27477 | -54.71133 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cdeb6b75-b98d-3673-b70c-3e9b628da975 | -11.52703 | -47.39004 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 41c7a3d5-8cd0-388c-a331-eeb0e8a7c530 | -7.68021 | -44.89416 | 2026-09-28 17:09:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 204a1c68-164b-3c32-aeec-8da348135061 | -6.41918 | -56.09781 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 09b2f330-71c2-37f4-b17f-9a81d9422c72 | -11.53866 | -47.39538 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 2d199eb4-9a73-3db3-892b-8a38634dfdf0 | -8.77124 | -45.83002 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ea0e60bd-7ef5-3f8d-824b-0d1e11c96afc | -9.8496 | -60.234 | 2026-09-28 17:09:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 197bc2cf-81f3-3bfe-94eb-21e37af17b66 | -10.09214 | -50.38588 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cf58124a-32c2-337a-bb4d-6f3e1dfcc0bb | -11.1164 | -47.71115 | 2026-09-28 17:09:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 01ce414e-be5a-3109-acda-f5b74d7e9e02 | -8.03389 | -42.86246 | 2026-09-28 17:09:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| bf1a84ed-08c8-346c-b604-08f17074b6ad | -9.77582 | -44.85905 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d7eeaa1c-d87a-3c9f-a3e7-5d3966b47bb9 | -7.68785 | -54.85097 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1966d268-7c80-3714-8bef-609a409810a5 | -11.59375 | -65.1389 | 2026-09-28 17:09:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 1bbafe85-c23f-30b3-944c-dc89cac49635 | -9.34391 | -46.53782 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a772507b-a18e-3345-8eda-c5ce2e1367bf | -11.78854 | -51.07497 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| aeee8230-eeec-32d9-85d8-1dd292efdab8 | -9.36019 | -45.85364 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a5255df-259f-31e4-a8a9-cb68ee6170fc | -7.35258 | -54.94684 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 884dcf83-73b0-3c8d-a26e-9dee0c8f56a7 | -10.99178 | -50.70197 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 688a3984-936c-3bd4-82ec-b1063e43a41f | -8.91946 | -49.77113 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9241e6a6-e08f-3206-ad2b-abcf7eea74fb | -10.49536 | -43.49361 | 2026-09-28 17:09:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| adfb447f-bdf1-32d8-8b83-2301f9ceaf0f | -6.8027 | -44.6353 | 2026-09-28 17:09:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 69fd4df2-d83d-33e9-bc17-8f5076c9a944 | -8.66541 | -45.37609 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 2d7cd5cf-1cdc-3a52-b9d7-37bb8d36bde1 | -9.16519 | -60.78517 | 2026-09-28 17:09:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 11097c32-dce9-3048-96eb-3fb95ff81a67 | -9.76839 | -44.84786 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| fdce3726-f216-3504-b12c-84baea90c697 | -7.10423 | -46.45846 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| ce37a806-26d1-3384-b603-d0f1dcd95cdb | -12.06583 | -48.54424 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| da18b825-2e39-3905-b952-87f8da06ead7 | -10.26883 | -44.63072 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 230.5 |
| d4c02c64-aade-3d2a-ae2d-cabe6dea0e73 | -10.29961 | -48.16624 | 2026-09-28 17:09:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f4ed6a6e-609e-3885-9c44-eb5834a15647 | -10.58268 | -57.32119 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bd52fc6d-ed75-320a-8f4c-a2e725dbdaae | -10.71057 | -60.73702 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e22a85d2-d628-37a6-a6c6-ddfa0115e34f | -7.5999 | -55.70258 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| deba88f8-1c3b-3acf-9422-2fd7935b7b0b | -8.73955 | -44.91431 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.5 |
| e9b33a11-95de-3adb-8bff-b902b96b3b44 | -10.70321 | -44.43364 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 53d8f76b-0420-3a88-9427-fe3a54f7050d | -6.45253 | -55.48623 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 410290a7-0390-3a7c-aaac-a9666328e7ee | -10.91097 | -50.70949 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 772b5ac4-0c78-393b-940b-ca6f6cb12e40 | -5.24846 | -44.9335 | 2026-09-28 17:09:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 754b54be-cdde-32a2-b42c-ddfb2c1cf8a8 | -8.6704 | -45.34233 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7d28a7bc-1659-36e6-8829-fbb1a7c8f995 | -11.47537 | -49.75121 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 857c2918-0998-3572-a886-f55910698153 | -10.0845 | -50.38717 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ac6ba175-1123-32f9-9321-2300efac7a53 | -9.33397 | -46.53973 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 447e8f09-83fd-3b14-8971-2d205bf02b56 | -10.76134 | -48.77085 | 2026-09-28 17:09:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4f507c9e-187e-35cd-bf7c-5d600cc47bae | -12.14551 | -50.36828 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 07c8dc45-00ec-3f94-8109-cc1826d7d466 | -7.00924 | -45.29818 | 2026-09-28 17:09:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 8d88ed18-2ef8-3226-a35b-9f43bcd734d2 | -10.92051 | -50.66329 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 99462372-de0a-3a03-9dd5-26edf9c7684c | -7.48516 | -46.9349 | 2026-09-28 17:09:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f81f07ab-1c95-3cbc-8bc7-60080e219c35 | -8.28222 | -54.71319 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6be5cc13-d732-3e92-8c0c-6e4081be3c3f | -9.76217 | -44.84507 | 2026-09-28 17:09:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 88b0c628-64e2-365a-a131-7816bfb13982 | -9.68116 | -45.56765 | 2026-09-28 17:09:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 35d03bd7-2ac4-3210-ab3b-22fd248cf8bb | -9.7819 | -45.82065 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fc36b55b-717e-348f-aa2c-2b637c069fc4 | -11.11956 | -51.18216 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0b8e31b9-7507-3b06-a4b6-dc46472a55b1 | -9.33937 | -68.77766 | 2026-09-28 17:09:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 32.5 |
| b2380571-4996-3926-a13d-fa7a1323104e | -8.23844 | -45.40628 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 31ffb15b-a429-3bb9-b806-e4dbf13ff644 | -6.70202 | -45.64936 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a6060e20-89fa-3af9-8876-a28011556696 | -11.21293 | -44.77927 | 2026-09-28 17:09:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f8d0be8f-e060-377a-a78a-f08ef2e0e828 | -7.43228 | -55.62948 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| b5627315-5d0a-398b-b512-deeaeae97e7d | -9.5015 | -46.40891 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| ff5f02d3-df03-3ac0-bb93-564d36bb39fa | -7.30709 | -43.30985 | 2026-09-28 17:09:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f03ad9fc-58eb-3389-ae6c-a357bf582994 | -9.3282 | -46.42239 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae5f9eb1-c0ef-3acf-a055-c8fa267aa2e2 | -10.26115 | -44.62019 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| b5ba5553-5719-35f7-baf7-5762f9ab7e58 | -7.32372 | -55.00513 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 436fe342-0434-3069-afab-dfdf2b970a25 | -5.41697 | -45.89151 | 2026-09-28 17:09:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c0208351-5059-34dc-a663-8b576bbe36fc | -6.6691 | -55.0808 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aa911c7d-f1ce-3c5c-ab1d-e5babb6783c9 | -7.45414 | -64.33871 | 2026-09-28 17:09:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fcd391d1-1758-3d9a-9eba-8796d1201e8d | -8.48587 | -49.60588 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e8c30cc0-d27b-3214-8dbf-01c2efe311eb | -9.0944 | -49.89467 | 2026-09-28 17:09:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 56202581-828d-3e6e-90b2-0f88f21a9359 | -11.53697 | -47.3861 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| b0058aba-4af4-3f52-8bc8-9ae7c6c96ff4 | -8.63164 | -63.81244 | 2026-09-28 17:09:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ee79e714-96a9-368a-abc8-99786cdae6e0 | -10.81826 | -57.22575 | 2026-09-28 17:09:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ea4841d2-df09-3d08-8191-65ac7102d420 | -10.01123 | -45.1798 | 2026-09-28 17:09:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b6591f16-4add-30b6-88b7-63e2c5caa207 | -9.43344 | -46.55073 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cf353afa-6461-3321-80ee-049ec9934d32 | -6.70732 | -45.67921 | 2026-09-28 17:09:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 891584c6-266c-357b-9c59-5d6231fbe400 | -8.77227 | -45.92398 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 389486a6-5209-3989-82c0-754fa5f5b09e | -10.27079 | -44.61696 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 56ead32d-c0c5-36b9-a421-210840337e31 | -10.24182 | -44.60901 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| df279391-1660-3fed-a255-b5b4155e47da | -12.77139 | -52.81504 | 2026-09-28 17:09:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a665cf37-6856-3db9-8a64-c3375f728636 | -6.19935 | -52.90965 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 605c8fd7-63a5-35d0-b122-089135d9f8a0 | -6.72232 | -47.78839 | 2026-09-28 17:09:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 38844dc2-b10b-3ced-a4d1-2b8205f05bdb | -12.26622 | -53.34411 | 2026-09-28 17:09:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33ba0795-20b7-3543-9b13-862494fc0296 | -8.48997 | -49.60515 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e1a40cd4-801d-3a94-bcd2-fa9f2f4d8e1c | -9.77952 | -45.98234 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 0a620c02-e70e-3888-93d2-0139b5944da6 | -11.10169 | -51.37833 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5bb91a14-38d1-38cc-a65a-8b7b0db302bd | -9.79231 | -45.819 | 2026-09-28 17:09:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eeea7b00-55e6-351c-89c3-76eb12f7d50b | -7.56162 | -55.02795 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 8f76c1cf-607f-3b64-821a-a8bad9c0a3e6 | -9.50097 | -46.40595 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| fee4cafc-c89e-34b2-9116-d2ae156abbdf | -9.81444 | -46.28596 | 2026-09-28 17:09:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6e6f0c6-35ce-3642-97cf-7014a0922844 | -11.5333 | -47.39161 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 3ad95fd4-e615-34ba-b795-936a62a84881 | -10.26188 | -44.6242 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c1ea55c5-aac1-3a33-a0ae-a8343a0642c2 | -10.40734 | -61.0194 | 2026-09-28 17:09:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 14118703-2a3c-3bcd-a8a6-74a188165a7e | -7.3927 | -42.63104 | 2026-09-28 17:09:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| c988cd71-be5b-3ec8-83e8-7c87f8812272 | -8.77188 | -45.83355 | 2026-09-28 17:09:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6bdbb31a-bcf9-30d1-8515-bda8619eb5ee | -10.26735 | -44.62265 | 2026-09-28 17:09:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 0ef1babe-6ae6-3d68-a666-7e1838d77a25 | -7.3353 | -55.25829 | 2026-09-28 17:09:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |


[Clique aqui para ver as próximas entradas](README145.md)
