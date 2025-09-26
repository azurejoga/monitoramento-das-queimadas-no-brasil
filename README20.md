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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b8e10aa-a3fe-35c1-9987-cb692d0209f5 | -11.23585 | -45.55051 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c116c69c-39b6-3f36-83b9-01f3971da26a | -11.0096 | -44.34126 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe3c1e5f-7664-34a9-bb10-7b1dc4329efa | -15.51683 | -50.42932 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9045e924-f877-35f2-806e-34b642469f97 | -20.97592 | -50.01882 | 2025-09-26 04:17:00 | NOAA-21 | MACAUBAL | SÃO PAULO | Brasil | 3528106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 44a7a305-fd81-3895-a0cf-ed0169712db4 | -11.00741 | -44.35521 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19dd2d6b-3463-3852-9333-3d3d369f9db3 | -21.04341 | -51.1143 | 2025-09-26 04:17:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 9f3d19c1-131b-39bd-ad8b-5cf7e3b3c369 | -15.02814 | -46.93902 | 2025-09-26 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18c59822-198c-3d2b-ab1c-02fd20ad8449 | -12.61734 | -48.13316 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 935345e4-2533-30b9-9af9-f311b3d6e4ea | -11.78291 | -44.91908 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff8284d6-e66b-3074-a24c-5c7685f9ffc2 | -11.68515 | -44.45799 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 08819b68-57e2-3379-a12b-620e77a2a47b | -13.24648 | -50.6925 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f53be9d5-ee49-3283-a2a8-275589b9375a | -11.42156 | -44.9212 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| defa6031-f134-3de9-8699-3050a17d35e5 | -11.01895 | -44.34633 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5d68308-3074-3f3b-859c-2917986a13df | -21.00033 | -50.02821 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 19f9f473-4f25-3c76-a730-133170675950 | -13.85437 | -45.61391 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9da774bd-eb3b-3e83-bfd4-31805e10a02c | -15.8814 | -59.33484 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2899006a-c0af-3662-ba80-61e3a858de7a | -10.1835 | -49.51295 | 2025-09-26 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b0f7d8db-eeee-3196-9c74-89fa6d60b739 | -16.22241 | -48.79936 | 2025-09-26 04:17:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b6e10ea-36ac-3e60-8432-f5039603a6e9 | -15.06612 | -44.98538 | 2025-09-26 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 177c5080-5025-3639-8e7e-db6979ccc673 | -11.22174 | -45.57408 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d553f342-0144-3c2a-be2f-f4a5af4d5aed | -12.13419 | -47.94669 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 132b1155-9cf5-3ffd-a9d3-36afa22e1734 | -13.80306 | -48.38913 | 2025-09-26 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e84ce807-88b5-3b54-99f0-09917b3e5d74 | -12.73976 | -46.82462 | 2025-09-26 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 484b284d-84f1-336c-b932-87a771ff6059 | -11.63067 | -44.39544 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1324f64a-407a-31b4-af11-59693284f933 | -20.75175 | -57.89608 | 2025-09-26 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| 2f3fd50d-868f-31ae-9d85-d23835b27cce | -13.84889 | -45.60569 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8aac4ee-3b9e-3782-83d7-ec1656eec98d | -12.13997 | -47.95667 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6ea50b1-7881-37b5-928b-0e6d690f1bd7 | -11.23803 | -45.55826 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| e0ba3c81-11ac-30b0-a5bb-ae1031eff094 | -13.8522 | -45.60624 | 2025-09-26 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc3b3206-7420-34ca-aa19-f44dcd040418 | -20.9888 | -50.47127 | 2025-09-26 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2caf50e-ca4c-3500-b35b-46e747aade24 | -11.22683 | -49.91914 | 2025-09-26 04:17:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f3519fde-b316-3f7b-be54-a4e4515a1b5f | -12.8431 | -44.71111 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3e4b924-36ba-32b0-b870-3ad505c74917 | -11.40776 | -44.92266 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a58c339d-599a-3b5f-aba1-ba07576ca21d | -12.55586 | -45.83531 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c2dc463a-1aa5-3703-9299-9a9456ba6362 | -14.82513 | -52.92097 | 2025-09-26 04:17:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2f08fcb-456c-3535-94c7-391b18da2d93 | -15.59859 | -46.45564 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ba35b4d-aec1-371e-bf5d-255dbffb3542 | -11.25039 | -45.5455 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 390491f5-b06d-368f-b285-1b95bffd4340 | -12.56081 | -45.84726 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3e86a8f3-c9c0-3a62-8c66-4b1098099178 | -11.00411 | -44.35468 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec573f7a-9b5e-3775-b1a2-8c70b8e32ca1 | -15.25953 | -46.44606 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdc31988-a7e9-39d3-8c96-fe6107058e41 | -21.38814 | -49.72711 | 2025-09-26 04:17:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0bba2197-7ab7-36a8-a3da-3c34045cba76 | -13.68737 | -44.29128 | 2025-09-26 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a38005c2-03e8-3d55-a5e1-0879ac01ebb9 | -11.21562 | -45.56942 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 5626b4c5-e066-331a-94a8-ed44e11dd586 | -12.85025 | -44.68704 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c44a3c8-190a-3981-8716-8de376c49506 | -15.52604 | -49.63052 | 2025-09-26 04:17:00 | NOAA-21 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c829ffa-5099-3728-990d-b480646da429 | -14.12995 | -51.20435 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f3d5fb4-f9fb-327b-884e-a756cab9a9b3 | -11.22742 | -45.56021 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 271751a4-bee8-39fb-9260-1ffb37af7ec2 | -21.0027 | -50.01478 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9e8eb1b0-f403-394f-a21a-8e92e8c08957 | -14.46754 | -46.34962 | 2025-09-26 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b57634fa-5af7-3cb9-8da2-ebb3f4c024d8 | -20.60601 | -56.73764 | 2025-09-26 04:17:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 56e6ba16-72ac-37d2-b161-577c34262c42 | -15.01032 | -48.03492 | 2025-09-26 04:17:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 231efa57-2414-3982-81c4-d6f3337ae373 | -14.14929 | -43.31083 | 2025-09-26 04:17:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac595600-f5a3-34a5-9806-21f3ee94de56 | -16.13118 | -50.76346 | 2025-09-26 04:17:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d66cdec-993c-3a14-9ac8-abad9d449d54 | -11.24981 | -45.5491 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 968b875a-b49b-30bd-90a6-e10b825f8198 | -11.21956 | -45.56632 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d91a81d9-5539-386d-8db8-93375d89228e | -11.23251 | -45.54996 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a394e77-5d0c-3e92-adcd-b9cebdeddb93 | -11.2296 | -45.56796 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68096862-66a1-34cd-b45c-6ee4a897aa11 | -11.23644 | -45.54691 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47bf42dd-d1d7-3652-b438-c1b911dd57ba | -21.00471 | -50.02448 | 2025-09-26 04:17:00 | NOAA-21 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f2f28409-78cc-3801-bf88-5b0d2c5ffded | -11.68293 | -44.42894 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e7f30689-9448-3d59-9311-67b9db437178 | -15.27653 | -49.47451 | 2025-09-26 04:17:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ee34b1e-d3bd-3629-84e0-f8bdcb368a08 | -11.23978 | -45.54746 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 048a09ed-b03a-31bd-b782-f4fd12aaa9ee | -12.04928 | -44.82603 | 2025-09-26 04:17:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9fabfbe-e666-37f8-a4a9-e07cec0ed16e | -21.33538 | -46.72824 | 2025-09-26 04:17:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5eb530ba-3b28-3e6a-82b3-b6069137a0ff | -12.13709 | -47.95162 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 45313f7c-69be-3f96-901b-c13458fefa7f | -15.25735 | -46.43832 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93aa2d2f-33d4-3689-ae7f-6903f10e875c | -11.66646 | -44.46933 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09853ebb-537c-339a-a2c3-4456b1e55526 | -15.25282 | -46.44506 | 2025-09-26 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74bc6579-2ce2-34e4-aa92-a1cdbc716c8b | -22.1986 | -54.83789 | 2025-09-26 04:17:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ef872b73-9c26-31bb-8876-9186b9869a98 | -11.6692 | -44.45184 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 177dd1c1-024d-3062-84a6-1dbff13d5fb8 | -11.2437 | -45.54441 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa5cdd1d-fe2d-385c-bf51-02fb6ae7db62 | -11.96559 | -47.87569 | 2025-09-26 04:17:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e9ce3346-f3ba-31b2-b637-808c95318c17 | -15.13612 | -46.42899 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8562d122-3982-3962-a4a4-f39f0c42b3b2 | -11.97721 | -46.6073 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 678ec4ee-d554-3012-a93f-2ad7f2322c11 | -15.5175 | -50.42562 | 2025-09-26 04:17:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0cb616e-12d9-3096-bf99-3c0832bc117b | -14.10761 | -51.15684 | 2025-09-26 04:17:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b09b913-434e-3d86-9a65-dddcac227e2a | -12.13282 | -47.95181 | 2025-09-26 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f0d8bd3-31ce-3a30-84d7-4e1edf0b6bbd | -11.42557 | -44.98318 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a8e5f22d-7d3d-3090-95e1-124a60fb6603 | -11.22625 | -45.56741 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f4ba98c-5b6a-379f-bcfc-79fb9e229b66 | -15.72845 | -59.4968 | 2025-09-26 04:17:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25588e3c-ae77-339e-9ba2-32f4fa01825f | -11.40605 | -44.97637 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 08ce2f86-a31a-3b46-b40f-ced7d6747bcc | -14.93438 | -45.45514 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 539e8343-8a85-376d-a757-1e67d6ccfa56 | -11.4402 | -43.51599 | 2025-09-26 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 016e5694-d2ea-3e5c-82c9-114f5746ce95 | -21.84006 | -50.58014 | 2025-09-26 04:17:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5616b35-8985-32b3-ab95-81d3c6387855 | -11.00794 | -44.33027 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ba7b38a5-05de-35d4-93df-d34871b22bde | -11.02115 | -44.35383 | 2025-09-26 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72efbee3-7e1c-3e58-91ad-258a83658831 | -14.82628 | -45.40745 | 2025-09-26 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10a02b47-429c-3d35-a3ab-cad542bcea8a | -11.98064 | -46.60789 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92871c12-7cfe-3fbd-adc2-2ba428cbc83e | -22.41003 | -50.63997 | 2025-09-26 04:17:00 | NOAA-21 | PARAGUAÇU PAULISTA | SÃO PAULO | Brasil | 3535507 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ba5f4a3-6f28-3ade-867a-ef8008d3461a | -15.38121 | -46.11351 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3e74feab-95d8-3272-a38a-a7708e2da558 | -11.66975 | -44.44834 | 2025-09-26 04:17:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1cd8c86-3dac-3784-a1f6-62695632a1af | -15.40136 | -47.06114 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daaf37fb-4a70-334c-b5f6-c24f28570abb | -13.9474 | -50.10327 | 2025-09-26 04:17:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b435da25-9ff9-3c96-a4db-b6e010035c45 | -22.38087 | -49.48358 | 2025-09-26 04:17:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 345db495-c2a8-3f29-b161-a4f97b4900ac | -14.95155 | -47.50225 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfb10bdf-9061-3fde-8ec1-15cf3e8a35d7 | -16.8476 | -50.5186 | 2025-09-26 04:17:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 0e74bc54-bff3-3894-9a97-d3f770172d9b | -12.87171 | -44.67971 | 2025-09-26 04:17:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee682961-93ad-310b-94c3-8ecf16bfcfcd | -11.97847 | -46.59961 | 2025-09-26 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50c91571-2d2a-3ef0-901a-2a3dcc635f42 | -11.63435 | -45.38104 | 2025-09-26 04:17:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 881a657e-dc6c-3d53-a20d-b7706875e97b | -11.2392 | -45.55106 | 2025-09-26 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 265.9 |


[Clique aqui para ver as próximas entradas](README21.md)
