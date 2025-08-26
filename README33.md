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
| 32f61aa6-87cd-3937-a843-5db373eb8729 | -13.48324 | -47.01038 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c110256f-2ac9-33b6-be48-f332cf5fb74d | -19.92226 | -44.61941 | 2025-08-26 03:57:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 7c557c24-a7e2-3e14-ab74-84e66b1e000f | -13.44804 | -46.98871 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f163b62-1af2-35d7-908a-0930552530cc | -11.51315 | -52.14079 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| ec1c74b1-c464-3e5d-9b54-056ef03c316a | -12.70668 | -47.88074 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 563fd6be-3b38-309a-9ea4-99d1a2c0c925 | -18.34466 | -44.96463 | 2025-08-26 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14742773-1a8c-393d-8f0f-53c010545d47 | -12.70567 | -47.88616 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d06045a2-2b5e-3df0-9576-8b5b4956b9e1 | -14.27318 | -49.13467 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd1725b2-d93a-3e6b-8c2f-ae191ebc3712 | -14.28335 | -49.13668 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 878f9288-f287-334b-9cbf-ed2682b0d56f | -11.53576 | -52.1284 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1638dc05-8f00-3de7-93d6-9261a24380be | -12.76202 | -48.13878 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a00a8536-fbd5-306c-bed4-52f399157bbc | -13.0557 | -46.30581 | 2025-08-26 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 681bd94f-a436-32ae-be20-43e8ef21a7a4 | -12.74014 | -48.09368 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f97d145c-b5e9-3801-858e-a313eb493cb0 | -15.17978 | -48.18806 | 2025-08-26 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59ca8af7-8755-3e59-abcc-cc92f0abb5b9 | -14.27256 | -49.13779 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6aa4db9-8349-316f-8556-747b9547191d | -19.03562 | -46.9162 | 2025-08-26 03:57:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 72090ef4-21fb-3997-818e-18259ee9a5aa | -18.49366 | -40.33443 | 2025-08-26 03:57:00 | NOAA-21 | BOA ESPERANÇA | ESPÍRITO SANTO | Brasil | 3201001 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 01f3fc26-9c64-366a-bfcb-801b79cc36d1 | -15.11484 | -48.65184 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3170fde-670c-32df-89f0-713c80ae4a62 | -12.75884 | -48.10186 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a82dfe50-ff9a-343b-95d7-5ce0b0d2d14c | -18.71533 | -43.81606 | 2025-08-26 03:57:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34dc653f-044e-37e0-8f21-fbb80937a81b | -13.4876 | -47.0119 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1f36a570-3c77-3c91-9913-8d4856d85a1a | -14.24825 | -48.04366 | 2025-08-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9ab14676-372a-3de9-992d-f156670e2a5a | -13.52605 | -46.90433 | 2025-08-26 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94e5bbd1-3a68-347b-bbc5-675aa0822bdd | -15.02422 | -48.51382 | 2025-08-26 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30001115-0060-3c25-9010-09c9a114bfff | -17.60372 | -46.69099 | 2025-08-26 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0eb27cdc-b654-3353-bcae-260e90fd1a6a | -12.66145 | -47.85581 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4400d812-735a-3562-9807-d7d5af1299a3 | -14.27379 | -49.13156 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a98c4426-74f1-3f3c-b23f-0ec90fb014a1 | -15.82499 | -45.76862 | 2025-08-26 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee3859df-52bc-3039-a591-b724c550d31a | -20.38016 | -42.19813 | 2025-08-26 03:57:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| c5ffc2c0-fe57-381b-828f-04985a1c8de6 | -20.18718 | -44.58119 | 2025-08-26 03:57:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93038f8f-3ea8-3a84-921b-dc31bf6b2fe3 | -19.16641 | -47.67039 | 2025-08-26 03:57:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cb52b21-6524-3b12-a50f-9856e6827041 | -12.93365 | -46.32015 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbb99afd-ab99-307c-b204-abb73bdc36ee | -19.17596 | -44.51673 | 2025-08-26 03:57:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3bb845bb-bcd4-3bf3-8ff5-e404bb6a4248 | -13.61253 | -48.15969 | 2025-08-26 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3a6b1e8-503c-34e1-b4fa-5cb945ef04e0 | -15.05327 | -48.69456 | 2025-08-26 03:57:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b11afd6-b36e-3611-9a8e-75552bb5114a | -14.27888 | -49.13258 | 2025-08-26 03:57:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 953b6197-f966-3cc8-a0b1-179b9ed3fd86 | -20.4586 | -43.87313 | 2025-08-26 03:57:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 183d7b6d-ada1-38d7-9230-04911473a8e5 | -12.93191 | -46.30471 | 2025-08-26 03:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29021391-b552-3d53-87f2-f4475d5f8179 | -19.17926 | -48.72981 | 2025-08-26 03:57:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 638c5eec-e67f-39ea-b0be-c30024aad57c | -13.05761 | -46.31967 | 2025-08-26 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eadffb03-7b37-3e93-a279-d43562cae55f | -15.63075 | -52.7263 | 2025-08-26 03:57:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b48ec2da-8a0b-337a-995b-73d201c1b0d7 | -12.74813 | -48.15857 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6bc4904d-402b-3e2e-a31a-dece67ace030 | -13.82355 | -45.89434 | 2025-08-26 03:57:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 872e8ba4-9294-3438-b10b-433caf7ae38d | -12.75 | -48.09507 | 2025-08-26 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e9f4351-4587-376d-9a6a-e70eac16307d | -11.56474 | -52.1174 | 2025-08-26 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb53b1f4-c576-34e1-a564-ab7656990776 | -11.559 | -52.117 | 2025-08-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 52b33c2b-0a1a-3fdd-ae7c-9d52336d26b0 | -8.8548 | -62.4503 | 2025-08-26 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 178.5 |
| b36e3774-b699-3d29-800a-2812f7933b70 | -9.0415 | -65.7349 | 2025-08-26 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 0f8c4267-7adb-3cb3-a849-a1e73c401840 | -11.521 | -52.1209 | 2025-08-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 598ce169-def8-30e1-8459-19032e9b9f21 | -6.8044 | -58.9568 | 2025-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| d246bf7c-33e0-3429-9c4c-3e6102dcd825 | -8.8734 | -62.4495 | 2025-08-26 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 7f774ffd-d780-317d-9cb6-6fb33e47061f | -11.5207 | -52.142 | 2025-08-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| c0f07de8-0426-372f-90e1-802c714d45d0 | -8.9874 | -65.4192 | 2025-08-26 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.1 |
| c6ff0d43-4438-391a-a03c-5d74bb339c84 | -4.9605 | -55.8226 | 2025-08-26 04:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 4c56bc92-59bf-3300-8074-97adbbed56f9 | -6.8043 | -58.9761 | 2025-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 28e5f9b9-d612-3ded-a8de-69a977fb0a8d | -6.7635 | -59.6718 | 2025-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 436f1e56-8349-3fdf-92a5-f59be4381f51 | -9.023 | -65.7355 | 2025-08-26 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 32ee1a49-deef-3a17-8981-8348e42593d8 | -11.1587 | -44.7627 | 2025-08-26 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 0a28ac72-df83-3e13-a2a9-51082e8c8632 | -6.8228 | -58.9753 | 2025-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 6242585c-45d0-3f8f-8703-732fadbaddb0 | -9.006 | -65.4 | 2025-08-26 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| b3dc0d26-63a5-36f7-bf5b-69023cc3efbe | -6.2459 | -60.0174 | 2025-08-26 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| b47277ae-e5f0-386a-954f-0b9c9171dba8 | -6.7819 | -59.6711 | 2025-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 3750af2d-e1a6-33be-957b-c683e01d76e1 | -11.1591 | -44.7395 | 2025-08-26 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 09553411-fb6c-3e7f-bd3e-d2989f15ed74 | -11.54 | -52.119 | 2025-08-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2447702a-814a-3bbe-8617-49fa3b69b52d | -7.3854 | -64.3662 | 2025-08-26 04:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 275d7626-ef97-3323-8d23-f26a709f12d5 | -7.3854 | -64.3475 | 2025-08-26 04:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| cc7bbd6f-b2a0-37b6-a0e2-f7de3dee50c9 | -8.855 | -62.4313 | 2025-08-26 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 7b202bf4-46d6-3275-ace4-4f21a95f8e93 | -6.2275 | -60.018 | 2025-08-26 04:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 125d251f-dc26-3608-ab99-b66909d2dfad | -9.1722 | -59.4629 | 2025-08-26 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| dc90b8f5-ca9e-306b-9be0-fc59556ced3d | -6.8229 | -58.956 | 2025-08-26 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a48d578b-5e8f-3be4-b2db-f09195d4d64a | -8.9873 | -65.4379 | 2025-08-26 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 31.8 |
| cbcabba4-51f4-3f15-89fd-07ab2363baf1 | -8.8363 | -62.451 | 2025-08-26 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 985a6432-78ea-3530-89b0-0db57e4d8875 | -11.5017 | -52.1439 | 2025-08-26 04:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ee3dbf26-79e6-3c02-bbdc-23e3b2832112 | -8.8364 | -62.4321 | 2025-08-26 04:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 8f342e62-d677-3255-81db-9d273cb3fbbb | -20.88682 | -49.02964 | 2025-08-26 04:00:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 81c0ce44-46f7-3791-84ae-983e25436375 | -21.42776 | -45.47757 | 2025-08-26 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 7bfc5b8b-8f72-3c58-a623-813c9cd53d44 | -21.12298 | -45.87511 | 2025-08-26 04:00:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fba7242d-48b6-38e8-acee-e4f0f975fa57 | -23.36535 | -46.16774 | 2025-08-26 04:00:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf36ea09-3929-365c-8e0f-bda8ba994036 | -20.00235 | -50.11641 | 2025-08-26 04:00:00 | NOAA-21 | MIRA ESTRELA | SÃO PAULO | Brasil | 3530003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 774de1bc-939a-3459-984c-afa191b1793b | -21.09101 | -43.41749 | 2025-08-26 04:00:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 139ae72e-2ce1-329b-9285-430336dbdab6 | -21.13676 | -43.75499 | 2025-08-26 04:00:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c7adebf3-619e-3da8-8353-164b90b27555 | -20.73079 | -49.38379 | 2025-08-26 04:00:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91a9e910-0c3b-393c-bbec-44e14c46c84a | -22.15429 | -48.76897 | 2025-08-26 04:00:00 | NOAA-21 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2d07300b-fb17-3b36-9524-d70a71af85ff | -21.47878 | -43.58332 | 2025-08-26 04:00:00 | NOAA-21 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 22a8cb50-d3f6-3f36-9d60-e9209ea1688a | -20.88238 | -49.02856 | 2025-08-26 04:00:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dd592073-0cdc-3850-ac02-6fe817a0a9d9 | -22.88224 | -46.37745 | 2025-08-26 04:00:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 534ef6ee-59a4-398e-81b4-549d09c59dcd | -21.09165 | -43.41365 | 2025-08-26 04:00:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b749bd0-7e3f-341b-9598-95715176d1d7 | -21.35228 | -43.75005 | 2025-08-26 04:00:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f0f4c507-43c1-39ea-afca-641cb0917cb8 | -21.16071 | -42.90959 | 2025-08-26 04:00:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c553062c-98c8-3a83-a41e-149181a51f05 | -20.87699 | -49.03224 | 2025-08-26 04:00:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| f08490ec-451a-3eb5-a4ae-252148a7f06e | -22.27435 | -46.45314 | 2025-08-26 04:00:00 | NOAA-21 | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed3af59c-a1c3-331e-9631-8b2cf5e8bef1 | -21.61292 | -49.69897 | 2025-08-26 04:00:00 | NOAA-21 | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2b178371-6f0d-3b56-a57d-120ea3cca8d0 | -21.35163 | -43.75391 | 2025-08-26 04:00:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 993e273b-b2a8-33e6-b2eb-6ff4427dcbd2 | -21.57683 | -46.36261 | 2025-08-26 04:00:00 | NOAA-21 | CABO VERDE | MINAS GERAIS | Brasil | 3109501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e77462fe-875b-3d81-9efa-b9efcc48d56b | -20.8833 | -49.0239 | 2025-08-26 04:00:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 2f19f02c-0dc9-3920-8510-c9ea9d2dd556 | -22.25648 | -42.50881 | 2025-08-26 04:00:00 | NOAA-21 | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f6b9d5bc-9b77-3305-91e7-0ff861449f5c | -21.43134 | -45.47847 | 2025-08-26 04:00:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| c2c2a6ce-4dfb-3d28-a08c-c938efbe7f76 | -21.28982 | -42.55385 | 2025-08-26 04:00:00 | NOAA-21 | SANTANA DE CATAGUASES | MINAS GERAIS | Brasil | 3158409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6b8c3f79-fbec-3c2e-aaf3-768cf7bc56bb | -22.89685 | -49.05498 | 2025-08-26 04:00:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bf8fe6ed-6ce7-3637-a291-516298d51a92 | -20.36536 | -50.70076 | 2025-08-26 04:00:00 | NOAA-21 | SÃO FRANCISCO | SÃO PAULO | Brasil | 3549003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README34.md)
