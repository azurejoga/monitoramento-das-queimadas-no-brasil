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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e52ebbe-a003-384a-a0a7-b0c7ddf7ba98 | -10.69548 | -48.22224 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cdfd4336-e6e6-3813-9bba-1a4dc77c0125 | -11.47016 | -47.30153 | 2025-08-20 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83a244b8-fa6a-3899-9ffd-6abb398b25ba | -9.27015 | -44.53609 | 2025-08-20 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bf91359-1a69-39cb-868f-11aa7a3977c6 | -13.4899 | -47.07382 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82246e7e-ed01-3431-866a-cf1e321adff7 | -7.56013 | -63.85275 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8f077a3-1bc0-33c5-8c89-25e0b7635006 | -7.04592 | -59.63076 | 2025-08-20 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4b276a04-9d51-37e9-9f45-bc6e2e69ac9f | -7.97025 | -55.30356 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ba0340fc-820c-3596-8e0c-5749b08f0303 | -10.69611 | -48.21742 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8657cdc1-0b77-348b-a006-7edac46098f7 | -13.03215 | -46.80688 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8e9905f-8542-3667-bee4-cd507bdb3eb1 | -11.59861 | -50.5347 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a19a3c0-8e43-3d00-879e-bc408d76178e | -13.19253 | -46.89071 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2d2a781-cf3d-3236-8add-09d30f0e5337 | -5.45129 | -60.16295 | 2025-08-20 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9708f0d8-7838-338b-9ffc-7779e40edadb | -9.92533 | -49.28972 | 2025-08-20 04:57:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 532c7609-9921-361e-bbbf-9d85008aa3a6 | -11.44233 | -47.32118 | 2025-08-20 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b85178e-e48b-32ab-9cb2-308e9f492028 | -8.29788 | -47.62101 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3a043c3-46b3-3d23-b6f6-edad9da42b3f | -11.31306 | -55.12848 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a433332f-ba16-327e-9331-b62f7421edfc | -9.31708 | -48.93334 | 2025-08-20 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86f205b7-5364-34f4-938f-dc50912040f0 | -7.38866 | -44.27324 | 2025-08-20 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a2e8237-8ff9-3e0d-8343-555e3f214f98 | -7.12814 | -44.64027 | 2025-08-20 04:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2701573f-d0d6-36d7-8861-af7a5b1950ee | -14.16343 | -45.28187 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abd10e0e-a492-38f8-9735-58443b0b2b39 | -7.55273 | -63.84789 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c711e1b4-0008-376c-949c-5786313edab0 | -13.02816 | -46.79567 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1563ffea-9ca5-3fff-981a-c4a64f1399d1 | -7.64594 | -45.28299 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2015c642-0ca8-3c28-b5ed-65765eb70b0c | -7.64153 | -45.27517 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 70a9d9ba-6b58-3558-a987-ef1108042b12 | -8.30779 | -55.10428 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1b637e8c-4bfe-3558-8d2a-f3904a275580 | -6.63274 | -55.2734 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d25c8f0-7ab2-3da1-a594-67656ac5867e | -8.82402 | -52.03117 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6baff361-8e94-3a0b-8d16-4db3885b681a | -12.99375 | -45.21408 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ca631af-be05-35c9-95db-41f84cdf038b | -11.3292 | -55.22124 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a3e074e-e3b3-3b35-8ba2-340a4666ccc4 | -13.86732 | -45.55747 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34ef0226-8f1b-330d-8b20-b7beea7fc2e5 | -6.46293 | -53.38041 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abffcc4c-d13a-3071-bc0e-62b055590959 | -13.0347 | -46.78644 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a6c1af-ddb0-3ab2-be8d-a9165eb33f48 | -8.5617 | -66.94872 | 2025-08-20 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ef4634e1-2351-3c61-bff2-c7f851e40690 | -9.23169 | -59.59824 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a8cfe72-58c7-321c-b14e-c4c41af20718 | -8.02937 | -47.66581 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6b9306ee-9f31-310f-a131-4bab4d5328fa | -6.46682 | -53.37741 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5106842f-14b7-3dc4-8580-fe2c1f95f76b | -7.22487 | -44.70475 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6054f157-2fed-3f7c-ac0f-1fd9255e2de0 | -9.72911 | -63.40673 | 2025-08-20 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72cd5f30-a7b3-3ef5-b547-6243aa134a9a | -7.64642 | -45.27954 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19734091-16ac-3fb3-81f0-06979e311b66 | -7.65179 | -45.28036 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c883123-7184-3342-b962-0509f1006772 | -5.45059 | -60.16711 | 2025-08-20 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a65becd-709e-388f-9ea5-d765f19038ff | -13.02692 | -46.80567 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a9db9c3-2662-3ccb-85a0-7110217bbacb | -8.69827 | -62.10652 | 2025-08-20 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65f07b8b-c182-3d4e-b937-27be3a5d0348 | -9.17543 | -59.61972 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d36fded-3e46-339a-b9b1-35aacc468dc3 | -8.30747 | -46.35472 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 274a6fad-fbb8-315e-9c25-872a3a292905 | -7.66053 | -45.25703 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92c7e8c0-0e93-3295-8bca-9c2e9ede9d8b | -10.91774 | -57.51286 | 2025-08-20 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 63ceabbc-5a46-3fcc-8bc6-b8c3c7a5e0c4 | -9.17251 | -59.61738 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| becf85dc-958c-3b01-b1e3-d91fd75852d8 | -8.0333 | -47.67128 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 61a85109-eddf-31b0-a809-482f6b75359d | -8.30245 | -46.35376 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3c0af21-251b-3bd6-b96a-27e3dff15638 | -9.18069 | -59.58936 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebedac48-5b4a-369b-9bcb-20dcd7b83bda | -7.78167 | -45.16572 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0c42a2e-a5d2-381e-9e5f-49e918e670f5 | -9.24174 | -59.61046 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 393f8888-25d2-38f1-85c9-04c90ab3490e | -8.29721 | -47.6257 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 485fdff2-61a2-3281-a444-5e58eaa8c51a | -13.40362 | -46.3521 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d269c05-95b5-3cb2-860d-446592c49d61 | -13.17626 | -46.89357 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9559746f-926c-3a2e-b0af-8d973fd5533f | -7.59639 | -55.47442 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad59ef6e-3da0-3b0e-b90a-a800a3bbcc26 | -12.52409 | -45.60583 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8be9c252-967a-332b-b7a9-f3ee4c12350e | -13.03747 | -46.80693 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 036b2d07-1f17-3a68-a6f6-59464a1a9816 | -9.81227 | -46.88626 | 2025-08-20 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07c8d31-8dae-3d62-a0d0-1e67bfdd8c30 | -7.59748 | -44.39326 | 2025-08-20 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b5bb6b3f-dfe2-3048-9c57-41a3f5418d10 | -8.81734 | -47.47873 | 2025-08-20 04:57:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1e540e02-261f-3a0d-a2ef-104ca32480f3 | -6.1476 | -57.71331 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 15054e2e-441f-3334-8c41-df91a36319a5 | -11.96928 | -46.77461 | 2025-08-20 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4904e6d4-5cc6-30bb-8d85-1a96553f97b7 | -8.2873 | -46.35149 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9160014c-1f4e-325a-befb-409ee830b378 | -12.99043 | -45.1925 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 064ee920-35eb-3caa-8b98-0876165cd121 | -12.0943 | -47.91498 | 2025-08-20 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad87a3aa-db6e-37a3-8a1c-e2218ec6aca3 | -13.19422 | -46.87704 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cc80c0d-93c7-3c92-99cc-c8f0d3602857 | -10.27594 | -46.76895 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 366f5ac2-4c30-3125-a40f-0ac92d77e7c2 | -12.98361 | -45.20016 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d48afb6d-7620-3a39-a353-dd4ced0baca3 | -9.18855 | -59.63751 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6591c937-0b85-3085-9bae-c6ce5d64752d | -5.50264 | -60.98078 | 2025-08-20 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bfc2b91-9823-36c0-9fa7-96c80463c4d3 | -10.43998 | -64.41524 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6253e21e-5ff9-31cc-a8e6-30399a452c63 | -7.63766 | -45.26341 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cde416ec-dbf7-3f82-9c11-41f518cee5a9 | -13.39201 | -47.49059 | 2025-08-20 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97e75688-9dd6-36fc-866f-9767d427da3a | -7.27552 | -50.18082 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c0daeaf0-de14-3fda-adfc-d5225a474b93 | -9.17149 | -59.61907 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95341413-3a00-3f79-8329-20d4bfdcb850 | -12.42903 | -48.70306 | 2025-08-20 04:57:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1894110f-0f6f-3fed-b2b0-7399e791d410 | -9.2339 | -59.60901 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f43f3cca-67fa-37cd-b002-539be97f6761 | -12.86815 | -46.0613 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5c51979-844a-3f99-aba2-84b8d0d67ab8 | -7.65227 | -45.27692 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85025ee7-af20-3c98-8cad-dbcfa47ddae9 | -13.17661 | -46.89067 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3114fc3-57c9-3be5-a94e-eb8a94694fd2 | -5.4511 | -60.13751 | 2025-08-20 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d83d430e-0fc6-39f0-839d-3637c4e7de6f | -7.27023 | -50.18989 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91097f4e-10dc-3882-833e-7c7e5158960e | -13.18617 | -46.89917 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 799ba663-765a-3d76-9b02-879ddd09a06b | -13.48587 | -47.0638 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 177edb43-7f02-30b9-9d3c-3e66afea03ef | -12.19342 | -50.21947 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f681c30c-b626-3f1d-bf78-c8e69832b4e0 | -8.87722 | -62.40348 | 2025-08-20 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebe3ab44-2104-3986-a9b4-382f14a216b4 | -10.90926 | -57.49961 | 2025-08-20 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac2cf881-c903-3959-a6af-fd57eb281d85 | -13.11059 | -51.91231 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b672e661-f771-3dc6-8feb-4d91940b1d8b | -9.21614 | -59.68964 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f1839c7-82cc-3126-a4ea-ded51d2cee0e | -7.226 | -44.70261 | 2025-08-20 04:57:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02de856a-d4a1-365d-b396-c1ba6b8ecfd1 | -7.29588 | -43.68445 | 2025-08-20 04:57:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46077a6f-2b49-37af-9a11-65ecd83949d5 | -12.9033 | -46.09675 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45c608ee-4662-3b20-9993-284b22bb4fef | -8.03004 | -47.66106 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68b911b9-b3b9-3050-a3fc-308ebe4067c7 | -11.67049 | -60.18785 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b6d15e4-d657-34a3-91bd-d9c0edd36850 | -7.78552 | -45.16577 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7247dfcb-6193-3d0a-9b03-eb08fd110589 | -13.02823 | -46.79541 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d1495497-5134-381f-880e-2f62c4e959b7 | -10.314 | -46.67502 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4adae22-7407-33cd-9af1-2dc66592eb9f | -13.03457 | -46.78669 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README48.md)
