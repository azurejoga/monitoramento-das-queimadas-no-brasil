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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f878460-f105-36c0-9b12-e8d81aa94bc5 | -8.4365 | -43.65825 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 046eacc9-100b-3985-98d1-f214943a24a4 | -4.40664 | -40.69361 | 2025-08-29 03:47:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6632b4d9-0efc-3d34-ae43-b8102bb74cc8 | -6.48907 | -44.40301 | 2025-08-29 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f0d6f494-4d67-3688-9a66-339b51590485 | -7.04276 | -44.38812 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6031040b-6416-3a11-bad9-7980d43f3235 | -8.47112 | -43.64029 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aba5e6c3-e30b-3c85-8241-fc5053193f2a | -9.64801 | -48.30177 | 2025-08-29 03:47:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed2af9dc-1d78-3dc7-942a-da90e5a503e5 | -9.9372 | -44.01869 | 2025-08-29 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 651dcb7f-85c1-348a-82a7-345e867486c6 | -6.72233 | -43.57402 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e0d1a924-ef1f-3ab8-92a2-8a133ff7ba58 | -8.44675 | -43.65115 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a971d95-ce37-3837-8fc8-c142cfedd07d | -6.4433 | -44.57777 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1076934b-b1cf-301f-bfa3-bf95ba05cd03 | -8.43213 | -43.65733 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7aec99a6-815e-37ee-8000-0ffb64cbefe1 | -7.41249 | -43.38763 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ed13ff9-db9d-36b9-9ab2-f96c5de68775 | -6.60771 | -43.6467 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39c0b8c8-9994-3b83-a1cd-87386450cf26 | -7.2188 | -45.3124 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36b96bad-1e40-378b-bfcb-03ab76038e21 | -8.90403 | -47.32359 | 2025-08-29 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e36ef18e-b0d0-3b28-a36a-11b8339e2065 | -7.63237 | -46.55313 | 2025-08-29 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83e1c94a-255f-3805-a742-6907644a155b | -9.84642 | -44.6824 | 2025-08-29 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1516eef5-a78d-33c6-8877-0626b3458f6f | -7.72446 | -50.27967 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3b03b601-fb99-3323-8b2e-475454edb469 | -3.97401 | -43.24654 | 2025-08-29 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d9ff3793-c130-3a21-9926-9705f5d0cae1 | -9.64295 | -48.29647 | 2025-08-29 03:47:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 263adc6e-e680-306e-9931-11322ab7aba8 | -9.93722 | -46.71284 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f992e4a1-4e0a-3a4c-9518-cd98e1712034 | -7.42075 | -42.06289 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a8c073ab-8ddb-32b2-8b1e-e31dfe353175 | -7.00013 | -44.37525 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8718bb8a-786a-3d60-ad7a-701d8ca73b77 | -7.04719 | -44.36301 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 51bb8125-2cc2-3ee4-962a-e5e50ec042ba | -9.93195 | -46.71194 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f41f141-65d7-3445-bf88-c78851ab417f | -7.04136 | -44.36148 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71628409-fc26-322f-9776-75fe74bb2027 | -6.40023 | -45.22882 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 056d5fba-93ca-339e-a3d9-b11fd641a905 | -6.64426 | -43.51727 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e451db12-3443-319e-a9ef-cf085253a57f | -9.59859 | -40.35421 | 2025-08-29 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1ffb580d-65ee-3d9f-9113-b87249edd9e5 | -7.6193 | -42.69704 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a74585a-6fd0-37d2-b763-ca53e5f0b76f | -7.62382 | -43.97585 | 2025-08-29 03:47:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44bd047-3e12-3c93-87c3-4e7f8c62f1eb | -8.44087 | -43.65916 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c4f7e21-00e3-3c72-aa17-405c06cf4032 | -6.87985 | -44.44531 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfaf9fef-b3cd-36be-a714-bf68e5b039ad | -7.16059 | -44.15363 | 2025-08-29 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c40a7f6-e2ef-36fa-b825-7b9cc66040ca | -6.70473 | -43.14357 | 2025-08-29 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9129bb79-aca8-3274-a5c7-dacafefb3911 | -9.51414 | -46.54419 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5698e609-12df-357b-b706-d5d0f43480c2 | -6.81218 | -44.32939 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f743c2c2-8209-346e-bd2e-1dfa71f39d9d | -8.44844 | -43.71719 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91b98c1d-135a-3f39-a99c-9632aa27a22b | -9.68508 | -47.06121 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cefca94a-f4c5-39d7-84b3-63c0b2bcbd92 | -9.6922 | -47.06358 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c10dade-bd12-33c8-8438-7f04e4e3ec27 | -9.9392 | -46.35414 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f962728-492e-3c78-8a52-be462c1d91c1 | -7.65042 | -42.69806 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c1561d4-39eb-30e0-afad-7fe072aa3719 | -3.97301 | -43.24852 | 2025-08-29 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a2e88b45-4c0b-34a2-b382-3a76b0dcdb52 | -9.68749 | -47.05891 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15888921-1486-3dba-9614-6bfb33be1d17 | -3.27674 | -43.52691 | 2025-08-29 03:47:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07cec7a9-910f-30a7-9b96-9d2d82c27c7b | -7.72004 | -50.3027 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b243b23-a399-3add-9f39-ca3973d5c9b9 | -9.81645 | -44.90367 | 2025-08-29 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e2e2c6d-0936-32ed-829e-b6cfd61f6e1d | -7.04833 | -44.38414 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3d363f9c-9644-3045-96f8-87c8864ad2f6 | -8.45362 | -43.71356 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9e1fb0d5-766e-39f0-aeaa-44296db6a588 | -7.61866 | -42.70087 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| baa34578-8e98-3d8c-bad6-100b296e2aea | -7.60857 | -46.24133 | 2025-08-29 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e68a001-4331-366f-b232-0820064dd944 | -9.93292 | -46.35932 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ea49ef-6f11-3b31-8cd7-87efb6677823 | -9.54839 | -45.84972 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7ad56fe9-43a9-3d0e-a60d-b04b23626c40 | -8.07765 | -45.02283 | 2025-08-29 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83452bb3-0d7e-37f5-97c8-8a2202a478cd | -9.97454 | -39.39308 | 2025-08-29 03:47:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 45c1a131-4254-3960-b792-5abb3d7c3c41 | -7.72211 | -50.29189 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b91ab34-5642-36b1-8d69-75a38b473e6a | -6.44033 | -44.5665 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9439e05-3b01-3a9f-ae61-a61957f7104f | -7.63759 | -42.66476 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cc7fda70-f697-3aa6-bc7c-853260340369 | -8.74303 | -47.39088 | 2025-08-29 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0107a60-1cd5-353c-8940-b9c3acd9e618 | -7.39492 | -43.38474 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c3590e-dd9e-3221-9bf7-952157b419ca | -7.65891 | -42.64918 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 91b7745b-8bc0-3ad4-9f4d-dde049ce9146 | -8.70595 | -47.86794 | 2025-08-29 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abd68c30-0ded-3467-a59f-71046655e0c2 | -6.72372 | -43.57654 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 373ff279-0345-37e0-86a6-e0297e404507 | -7.61738 | -42.7085 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 87955304-6b37-304a-8eeb-8fb2f53d37d5 | -7.40003 | -43.38119 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c848a261-191b-39d6-9b9a-12a469d44ee7 | -6.16492 | -47.28154 | 2025-08-29 03:47:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 68a6e51f-333d-3b9e-8ef6-f680dd3a4933 | -6.38118 | -45.58357 | 2025-08-29 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c09232c7-d08f-38f0-b21c-f4d839f991a4 | -7.70618 | -42.12958 | 2025-08-29 03:47:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4a25a428-408e-3a5a-9ee5-54c0345d8ece | -6.88457 | -44.44633 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1e35b83-5f0e-37e3-a8e2-a553bf6a6dca | -6.81078 | -45.00153 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59906c73-24fb-3139-9825-b1d573c57ca0 | -7.42536 | -42.06618 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2c9b5be7-0e9c-310c-a63c-7b18e4617857 | -7.07432 | -44.29134 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d5257311-b6ac-32cc-8665-b48df236a38c | -6.81495 | -45.00022 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4259b21-e2ee-3e75-a68d-669ba1c0b0e6 | -7.41673 | -42.06222 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 655d8ef1-2f88-3e4a-93c8-11b6c34ed0bf | -9.9366 | -46.71624 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a83d05d1-ed66-37ef-926e-a038c4ba7b1d | -9.43632 | -47.64145 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb7dc4e9-e7ae-3736-915d-25c7cd402b66 | -7.42998 | -42.0634 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| caa8cda3-1b04-3b9d-a69f-73928e5b4581 | -9.4996 | -45.37912 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a29e3c8-fac1-3d0b-be09-b1b429e2f703 | -7.64385 | -42.66187 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2d91691a-ca35-3810-91c2-fff9eb838749 | -7.0416 | -44.36714 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d394c3ec-3ea5-31b2-8219-57c1b1521537 | -8.46062 | -43.64938 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d60cbcaf-11ba-3b9d-8b02-8d92ac201917 | -9.69044 | -47.06242 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8b34b17-803d-3c6a-99ed-721d58d09af7 | -6.81256 | -44.3547 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10b1d2ec-0225-3af9-afe0-25d79f69bea2 | -6.80923 | -44.31859 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 826cf549-c570-33a7-8f39-970d4447da06 | -7.20732 | -44.06931 | 2025-08-29 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7cdd5e2-03a5-3e3f-93ff-f0232c1bf62c | -6.87478 | -43.62463 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef1e8536-568b-3326-ad35-c3e83ac88276 | -7.41271 | -43.38592 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a1925eb-76da-3445-9c17-1ae9ac16ad84 | -6.87714 | -43.6109 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c26ef1d9-3e41-3e0a-a322-6adf11dc0304 | -7.63302 | -46.54959 | 2025-08-29 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ca20135-5504-356d-baf7-ac70d723d59d | -8.48614 | -43.6835 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fb0dc93-b6a1-3afa-a2cd-4a2dc81920fe | -9.86025 | -44.68455 | 2025-08-29 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96598076-0ad7-3819-b4a1-fc5d92f5ad26 | -6.87636 | -43.61547 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce58d257-ddf1-3468-892b-4ed1b999c032 | -6.3817 | -45.58052 | 2025-08-29 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27a0cd23-8e92-3017-8425-0ca4416bc727 | -7.22138 | -45.44444 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b5bf788-8690-309c-b494-7c7cc684fa41 | -6.81 | -44.99939 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bbd039c-a0c8-340d-ae6f-38ee78e27345 | -7.63779 | -46.55407 | 2025-08-29 03:47:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc7c2c28-337a-3968-8044-9b74ba029527 | -7.03799 | -44.38146 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2c770dbc-3706-375a-883c-68313289b607 | -7.04071 | -44.37214 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f548cbfb-a896-398a-8777-a0ba2d4d9dac | -7.05361 | -44.35412 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 911f7dd0-c24f-3111-b228-b79607599ac3 | -6.7282 | -43.57737 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README27.md)
