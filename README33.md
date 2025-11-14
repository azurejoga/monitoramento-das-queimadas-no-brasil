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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74d96d8b-aee7-35ca-b331-e0f3bc91a48d | -4.11012 | -50.05536 | 2025-11-14 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c160ff31-b906-312a-b220-b53421fae9c3 | -6.07295 | -41.54911 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8506cd90-7006-3ce3-b203-97f553e77440 | -15.03361 | -46.65304 | 2025-11-14 04:25:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c66905ef-78f5-3f9c-9fe0-da2c5434149a | -7.05279 | -45.06071 | 2025-11-14 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 944b4f2e-f873-3d30-9bc6-1925d314251c | -12.4304 | -43.17727 | 2025-11-14 04:25:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2270b084-61db-3286-ad94-bdef575847ab | -5.30414 | -45.07495 | 2025-11-14 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb244002-fb0b-3659-83f1-6ff0c93b8d5f | -5.2542 | -46.17778 | 2025-11-14 04:25:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fad42865-a7bb-3ccf-81c8-1094979e1937 | -5.8907 | -42.26546 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4473140f-145f-3799-b613-8689a01ebbaa | -4.80216 | -45.0561 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d31b1849-06b9-3e04-9a2d-e816419c0605 | -4.77496 | -46.44685 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e78a94fa-97ab-3033-9d84-1f927bb86bae | -11.07095 | -44.96006 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b75993a-4966-3783-b409-a00b21154fe5 | -12.41224 | -54.19079 | 2025-11-14 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e27a1d5-20a7-330b-8c5d-8d00d0f247bb | -12.40042 | -48.11789 | 2025-11-14 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1ace134-5a58-3b6e-a997-000361318020 | -12.682 | -44.14786 | 2025-11-14 04:25:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2057a07-e628-3216-9344-aa8927b475be | -17.54628 | -43.93325 | 2025-11-14 04:25:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c826788-a6a2-376f-98da-e16041b10fff | -13.68829 | -48.42186 | 2025-11-14 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0900ab6-44d0-3916-a52a-3af952c9f599 | -5.52984 | -41.7489 | 2025-11-14 04:25:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb606b4e-f270-356c-8a04-5bf6684962c0 | -5.16065 | -44.6569 | 2025-11-14 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ef71e0-651a-3dbc-83ae-06f01c998864 | -5.4202 | -43.25869 | 2025-11-14 04:25:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 361cc1cb-5793-393f-b49a-190fc384c18a | -6.10801 | -41.56628 | 2025-11-14 04:25:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3cd0350d-3648-3816-a916-1881e25b1d81 | -5.02052 | -44.34079 | 2025-11-14 04:25:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3c44247-2a6d-3b17-8b2b-1a7f70d3ecf3 | -15.1412 | -42.93458 | 2025-11-14 04:25:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b479bf7-3d6c-34c9-8624-9a7ed8467df1 | -14.84061 | -43.88617 | 2025-11-14 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e4ed290-a8a8-3767-93a6-117c56a451a4 | -15.07679 | -46.45848 | 2025-11-14 04:25:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eccdd96a-fe18-30d9-a494-4e6d070e359d | -15.60885 | -49.14734 | 2025-11-14 04:25:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21640c7d-bba9-3f64-92b3-88627f4c504d | -17.2124 | -47.65356 | 2025-11-14 04:25:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 749fc698-74f9-3a85-8741-8b36d73bd3e7 | -12.71928 | -45.42615 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c6b50ec2-882d-38d1-9ad7-885dc56a735d | -5.58573 | -44.89514 | 2025-11-14 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 891309e7-2d9b-3c2f-ab61-00e8390b8212 | -12.71372 | -45.41794 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 960c72df-5a64-3a48-bf50-de97ea01eaf7 | -3.91043 | -50.0369 | 2025-11-14 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 458cdcbb-61c4-3e23-93e4-394989ed15ba | -5.97957 | -42.59734 | 2025-11-14 04:25:00 | NPP-375D | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e2252e9c-40b3-3111-9580-5c518956b70b | -16.96232 | -52.38679 | 2025-11-14 04:25:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4050ed73-fa52-3a0a-acc0-1da3e57627af | -6.15982 | -48.04719 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 35528f90-693a-3e6c-b801-a8187a898f4d | -6.81184 | -41.51476 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ac14106b-9de1-39dc-91c8-3a0f1d58f9f1 | -5.75665 | -42.73125 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1244c8f5-2598-3415-821d-8ee107b684f2 | -6.09524 | -47.92015 | 2025-11-14 04:25:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59f42656-8b8e-3057-9440-3d334baf7517 | -5.02747 | -44.5119 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 662967dd-f9a6-3963-b8b8-2984f89632df | -5.84696 | -38.40366 | 2025-11-14 04:25:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1d540c12-0537-303e-91f9-3fd0019bf601 | -7.1033 | -41.82713 | 2025-11-14 04:25:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f8a9ad3-6e88-340d-bd23-962675266966 | -4.96332 | -47.72013 | 2025-11-14 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dd5a877-8eed-3170-82d5-ac08ce3edeff | -11.29237 | -45.16252 | 2025-11-14 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b4dd9f4-ea64-3a60-82f9-b7a5070d7e49 | -12.69038 | -45.43611 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f70c8354-47a8-32a8-bd33-b2d94b501d1e | -3.80133 | -52.01054 | 2025-11-14 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b657af1-4510-375a-8b80-f62e7cb9aee4 | -13.77131 | -43.62084 | 2025-11-14 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eb254884-3aca-30d5-b45e-6d41a0f454ec | -11.9319 | -43.94522 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b09ff88b-2873-3d57-bab0-c1ed30c8fdb5 | -4.98757 | -43.88527 | 2025-11-14 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6046297-a6cd-35eb-94b3-7f73aea41f30 | -6.24062 | -42.11813 | 2025-11-14 04:25:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1f98c28-d432-3433-9eb6-db00f8a94bd8 | -6.16715 | -48.04845 | 2025-11-14 04:25:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 051d60c8-6d52-379d-8160-6a1ad76d7f91 | -17.30168 | -46.8301 | 2025-11-14 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9fdcaee-7c96-3c72-8a48-84d5944446ed | -3.41635 | -52.7347 | 2025-11-14 04:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 504e6a10-83a8-3edc-85f9-7f35a53632a4 | -6.24279 | -46.24326 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a776d13-f7c1-3499-8f9e-790cb6ab0f2b | -4.63701 | -45.16298 | 2025-11-14 04:25:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4da59f11-53bd-3dd6-8db0-508867295c6a | -4.77515 | -48.68034 | 2025-11-14 04:25:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca1248a7-3718-3c31-9919-03d08fd9d35e | -6.81084 | -40.08932 | 2025-11-14 04:25:00 | NPP-375D | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 83095318-7004-3cbc-8cc7-d7a05c6dccef | -5.70594 | -42.76492 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6134627e-bbc8-3422-8bbe-d2c1fc5d7b64 | -5.48931 | -47.69938 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10bd3986-3ad1-3289-aa4a-9f84729119d0 | -11.57445 | -44.87089 | 2025-11-14 04:25:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9133aaf-7fb1-377c-9552-f9d55dd8956a | -16.54469 | -49.35803 | 2025-11-14 04:25:00 | NPP-375D | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54d42c48-e479-33cc-b526-71114cb9f214 | -5.60375 | -41.06361 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5cf9d07-69ac-358d-88df-6af7033c30af | -4.70332 | -46.45094 | 2025-11-14 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 512f4b3d-fa25-33d2-aaba-aa75d2abb0c2 | -6.4142 | -39.74974 | 2025-11-14 04:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ed9efcd8-cd6b-3681-9369-464092ca70da | -12.70594 | -45.424 | 2025-11-14 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 05ba5aa7-08ad-3339-a82c-ab17bc45bf10 | -6.10278 | -41.52738 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b39f9c92-3db8-3594-ad73-76d0dc886b0b | -4.81329 | -44.87938 | 2025-11-14 04:25:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36de6706-ffbe-3362-a8f1-7578cd43cae3 | -5.90134 | -42.74554 | 2025-11-14 04:25:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c6602817-64b6-3332-b624-d12198816946 | -14.70205 | -46.60888 | 2025-11-14 04:25:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cda82996-d864-3f2d-ae36-d7e5dc846c2a | -16.51694 | -43.54372 | 2025-11-14 04:25:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 055b3a33-669c-3075-914f-2e539966743a | -6.44116 | -45.66542 | 2025-11-14 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d16afc32-1be8-3feb-87a0-4be30b6a37f1 | -4.99035 | -43.88926 | 2025-11-14 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0daa19f7-da64-313b-b650-c081f249746e | -4.9837 | -43.88823 | 2025-11-14 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf859214-bdf6-3bab-94d7-f5417d0f67dd | -15.55057 | -43.17412 | 2025-11-14 04:25:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8168dbf5-2c2c-35d8-b841-b02a970e73ad | -14.94291 | -49.79186 | 2025-11-14 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5133d28-e064-3d15-89ac-b203eb7edbca | -7.28265 | -38.81071 | 2025-11-14 04:25:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 979d4253-49c8-3d64-ba29-10de0e04e6ef | -4.918 | -43.29753 | 2025-11-14 04:25:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c9d7203-2242-3872-943b-ee904fd3fba5 | -4.21526 | -49.12238 | 2025-11-14 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 02cd60ab-6aa0-3688-b5b0-2ee7094576e6 | -4.98425 | -43.88475 | 2025-11-14 04:25:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8f754c2-bf21-3974-8cc6-542fe4cff806 | -5.69639 | -45.96767 | 2025-11-14 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e82575bf-7505-374c-ae0c-9c34da634b7f | -5.49466 | -41.90974 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa2906d8-2d02-3052-b6c5-cda947611d20 | -12.43225 | -43.17481 | 2025-11-14 04:25:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19dc26a6-2a26-338b-a12b-08a260cb478d | -5.42508 | -42.57482 | 2025-11-14 04:25:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9b64119-3101-3729-a1a9-8b1a70810efc | -11.85879 | -49.22039 | 2025-11-14 04:25:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a1b7ec34-6d2d-3384-89a7-e9160d6b463c | -6.87892 | -42.84988 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f1305f10-2de0-30a6-bdbb-12f110e4d82c | -5.02415 | -44.51138 | 2025-11-14 04:25:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bec05bf-c7d9-3b08-a4e7-2f12b346d140 | -5.57682 | -50.40115 | 2025-11-14 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73c39076-4b41-3b41-a8f4-339aa29b43bd | -13.50292 | -43.64215 | 2025-11-14 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 67be7474-7776-302d-8d22-ee0dd891899a | -6.01758 | -44.32782 | 2025-11-14 04:25:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e6829a0-7535-39e7-bebb-2c55822f2933 | -6.83086 | -43.16389 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8b8d21b1-0d65-3c3e-b1cc-16f134f417a7 | -13.60318 | -43.56874 | 2025-11-14 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c331fb1-73de-3aa2-87d5-c59b5a8c42cd | -6.57033 | -42.13003 | 2025-11-14 04:25:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 9c101ac9-20a8-38e7-ac8f-bfef69288c14 | -12.67184 | -46.75116 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9826fa33-82a1-3e57-addf-e8930b2291af | -7.09966 | -42.36656 | 2025-11-14 04:25:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c57be3e-d847-3709-8d63-692d4a0ba496 | -6.72066 | -42.9515 | 2025-11-14 04:25:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 14110fcc-8b45-3ccd-87c4-5f13ac7c3f32 | -11.93534 | -43.94576 | 2025-11-14 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f38a9e32-0455-396a-a152-9e69a922fcd6 | -6.006 | -38.99059 | 2025-11-14 04:25:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 51f53362-d3f6-3761-9a00-fa04832b4e81 | -11.24956 | -47.50146 | 2025-11-14 04:25:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3e32f38-f791-3be6-8b8e-3f0afa0622c5 | -12.66404 | -46.75716 | 2025-11-14 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eae9aba-0219-3e51-87e2-029ea5c05c8c | -6.46971 | -39.8555 | 2025-11-14 04:25:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f6cf0486-7a4b-3116-b8a9-81c423d7f990 | -6.06744 | -41.56094 | 2025-11-14 04:25:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7269e0f9-1288-37de-b72d-545e48c3f492 | -16.30647 | -45.09624 | 2025-11-14 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 13bf3fe3-9ce9-3af3-9087-d5756ff16bb8 | -3.90976 | -50.04097 | 2025-11-14 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README34.md)
