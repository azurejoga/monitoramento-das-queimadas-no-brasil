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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e15f3a5-addd-33e6-8478-cdd9bf9493ec | -16.97984 | -41.1521 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3bd5824-d43c-3313-abee-35c3f5b574c2 | -12.46108 | -45.4378 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e43736de-eb93-321f-b5bb-e980e6af1838 | -14.28225 | -42.33158 | 2025-10-19 03:45:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 7e286f29-e32c-31c4-8c34-083e476ed098 | -14.92083 | -41.42065 | 2025-10-19 03:45:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bacaf4ec-3303-38a6-89e7-ecfa0cf2c91a | -10.45349 | -44.46785 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7a8f33-fb8e-3f4b-a711-93210cf660fb | -14.30341 | -44.01452 | 2025-10-19 03:45:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cd8a9c7c-cce5-3784-ae27-2cf06d33b13f | -11.68633 | -47.30227 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9108d23d-a4cb-3278-896b-9e023844d481 | -12.1436 | -45.07706 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc5986f-9157-3e28-b434-12b63da6d0a2 | -13.94294 | -45.60154 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaba3ae7-ba5d-3a3e-92df-58dbae47ed5e | -12.41248 | -40.92481 | 2025-10-19 03:45:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa9afdfa-91f6-3255-a1e5-124bb41f12ba | -10.45488 | -45.02288 | 2025-10-19 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f14a93c0-53d1-3370-b0d1-abd1572c8a17 | -16.78353 | -42.76549 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 33aa156e-2e3f-3f5b-ae54-02674a2cb6d0 | -10.68058 | -44.55269 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0915480d-9a0d-381d-b0bc-f5abebfd17f7 | -11.62788 | -44.08914 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0eada1ae-91cd-3826-9fb5-c1725c0c5b72 | -10.45428 | -45.02614 | 2025-10-19 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2d44301-17a0-3541-82e2-4ec844aea2d3 | -16.75412 | -42.76762 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c26c4d4b-f7ec-32d1-b4c2-c8938cfcc35c | -11.65336 | -47.31413 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f202efe0-4473-3ab2-9d9a-7237e64e66db | -10.78302 | -40.31046 | 2025-10-19 03:45:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d623cfd1-8363-3c9e-b31b-76d27f08d62c | -16.77621 | -42.76005 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5780caee-5563-3bde-8791-3b55936c262b | -16.75476 | -42.76406 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1da83f40-7548-3132-8f93-a1821f87c315 | -16.98266 | -41.1574 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| badadc5d-2e94-39bd-a6cd-732c0130e469 | -11.47662 | -42.22466 | 2025-10-19 03:45:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 6e7077e8-7c2c-38e8-b8de-1a8ec8cfab38 | -13.86175 | -45.45813 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfc96a4b-3b08-3f03-a347-bc3fe79f6df8 | -14.74978 | -42.46118 | 2025-10-19 03:45:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c4b58fc8-d156-3a3a-93a8-2e05e7a7ea02 | -16.51573 | -43.547 | 2025-10-19 03:45:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dd57e52-1b3f-3327-bcbf-a439e95defac | -12.14645 | -45.0621 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8135862e-2778-33d9-b79c-4c17d5a1d506 | -15.51118 | -41.5399 | 2025-10-19 03:45:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a2f9ec49-134e-3680-b6fc-11f96147e6b4 | -13.71529 | -40.98412 | 2025-10-19 03:45:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 98c57a0c-e0a0-329f-be76-5278d35b7767 | -10.77913 | -40.31217 | 2025-10-19 03:45:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 725d0563-b94b-38e6-a5bb-b2f5aac73976 | -14.98071 | -47.07648 | 2025-10-19 03:45:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e3f2f7b-4388-3839-bcb2-2906d1bb80bd | -16.80866 | -41.01156 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3cb4180-69d0-3c85-9468-8f037f18d9c8 | -13.69977 | -43.15808 | 2025-10-19 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 21584f65-330d-33c9-81fc-893d52927362 | -14.55291 | -43.50469 | 2025-10-19 03:45:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39662e1d-0df3-3959-8379-b59da5938aa2 | -13.89194 | -45.51278 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce918eb3-9296-309e-bed9-5a7c4deb57f1 | -11.64857 | -44.084 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9e58533-37fb-3ec6-bf28-323143866bf8 | -16.82258 | -40.17191 | 2025-10-19 03:45:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f08e266-d4a4-335e-b698-22f307165b3f | -10.10059 | -44.56255 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6486fad2-4384-3882-afe0-68e1a4327c94 | -10.6817 | -44.54676 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 636313da-fc8a-37b2-b4e9-b64a3cb4f2a1 | -14.28159 | -42.33527 | 2025-10-19 03:45:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3e0579e0-b0f3-307e-ae0f-d64ff7075faf | -10.86651 | -43.93232 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f01dda65-4f4d-3281-a386-3bb89f39c3cb | -11.47734 | -42.22066 | 2025-10-19 03:45:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 8cc80a42-f3fe-3746-a1fd-18a38c18ab1f | -12.66094 | -41.25252 | 2025-10-19 03:45:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c20ae1c-f244-3a51-be02-d9a8920188dd | -16.74413 | -42.77695 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee60a92-811e-3b1d-9845-a86975aedd5f | -10.58188 | -41.50226 | 2025-10-19 03:45:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 14b3018b-3c1c-3ef8-97b4-eff83086eb0a | -16.7501 | -42.76689 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9484a6bc-0c45-3904-9a9d-88a55f61f26f | -12.33884 | -41.20175 | 2025-10-19 03:45:00 | NOAA-21 | WAGNER | BAHIA | Brasil | 2933406 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 228eb75e-4adb-365a-ac91-23d127ed264a | -12.02098 | -46.48304 | 2025-10-19 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c114112-8f4f-3825-a4a9-09326b5977c9 | -15.54022 | -46.44569 | 2025-10-19 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b03ac1a-d771-33e5-b255-8b6f8df25a98 | -10.77835 | -40.31685 | 2025-10-19 03:45:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 56dfb6b3-3241-3fa8-b6f0-10c638217f1b | -14.98096 | -47.07817 | 2025-10-19 03:45:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 65eda252-8a3c-394c-80da-5f0677b3ae40 | -12.46046 | -45.44096 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbd6c39f-eaa0-3715-94e7-ca69612ff2f5 | -16.75689 | -42.79825 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f73bd33-ae42-3f5a-a912-a6b932c4a54a | -11.14491 | -47.71594 | 2025-10-19 03:45:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4213d0e9-5793-3660-a8f2-2ef7e53361bc | -15.76842 | -43.27036 | 2025-10-19 03:45:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0db07169-4588-3bb2-9b96-f313cd4a3a6d | -12.49543 | -46.93081 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3d0ccef0-c6df-305e-9dd2-58554a9cf211 | -13.93727 | -45.60371 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f25cdabe-003e-3c7b-9042-311aacf39cfb | -16.75813 | -42.76836 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5d1bcf5-9f84-3257-98d9-ecee7f1aa8d5 | -13.01789 | -46.95581 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e47a729b-ba84-364c-8a5f-1aed9efe0e0a | -16.74546 | -42.79249 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b918bfcd-6771-34d6-b9aa-27ea294dc086 | -11.45094 | -43.46888 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39caadbf-c434-3275-a7c7-abcd373426ac | -10.95265 | -45.46668 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0fa6d55d-e234-343f-9bf1-924318b520ef | -16.75348 | -42.77117 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c030288-53db-327d-9652-a92bf1d8c27f | -12.9845 | -47.27623 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c36b825a-dd83-3ba1-941b-3a66f9155a40 | -16.74336 | -42.80408 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 66f42d0b-741f-3dd2-bec0-55854768675a | -12.49314 | -46.93074 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 107f3780-12e2-38b5-a276-16db22fc37a3 | -10.1534 | -44.52313 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34247582-cd2b-32c8-bc7b-96898b6f0ad9 | -10.68726 | -44.54477 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf91f474-fbeb-3b2d-8e60-988a3d9a06b8 | -13.0866 | -41.083 | 2025-10-19 03:45:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e934f033-1451-3b4d-ba6f-e22874bd4ff7 | -10.72044 | -44.53358 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf80c44a-ea27-3025-97bd-2c2d768ea06d | -15.01587 | -40.45865 | 2025-10-19 03:45:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ed34f54b-8286-3a55-92bd-1109e3f09a0e | -16.76359 | -42.7841 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37b9b0d6-4dc9-3556-a22d-8cdad8d8fd52 | -12.98216 | -47.26375 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24a38051-9f87-3555-9d6a-43dc0da47516 | -10.87128 | -43.9333 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ec59e8d-9b6d-34ef-a305-735b01fc2f17 | -12.45559 | -45.42924 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 422f44cc-bfb3-3b54-9b82-21580f18a300 | -10.87981 | -47.4565 | 2025-10-19 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb0de28b-6abe-3e70-8968-cd8ec3e29beb | -15.25711 | -43.57952 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5030a5f8-3785-3427-bae9-10d9a2f936b3 | -14.98492 | -47.08665 | 2025-10-19 03:45:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f648673f-947e-3a4c-99a6-8b8c8cdfd340 | -14.98416 | -47.09032 | 2025-10-19 03:45:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f759b5f-5212-322d-ba7f-04d7aed7dc83 | -15.25631 | -43.58382 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b3fdc26-d2e1-3bcc-a6c4-97e3fe7f28ca | -16.97822 | -41.16126 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4c2e7b83-532c-38b2-b890-fc5943afa261 | -11.65564 | -47.31189 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba35bc55-3aaf-395b-a52d-2aca5a016305 | -17.62676 | -40.10332 | 2025-10-19 03:45:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ad2d01b6-802a-3891-95b6-672a460edb55 | -14.13575 | -44.688 | 2025-10-19 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80ecefc1-6c15-30a5-b5b8-ea19d0c0a50d | -9.98605 | -47.05883 | 2025-10-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b6da647b-9a35-37d3-9b24-0cafa354ea71 | -11.63745 | -44.0909 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 808c2902-5d71-31f9-ab16-8c5f62fd3e54 | -15.97944 | -41.20932 | 2025-10-19 03:45:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c05ba189-4f77-317c-b3f5-9fca07d6fe69 | -11.63266 | -44.09001 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c03d698c-7906-3bb4-939d-9d02dc5386c7 | -16.20569 | -43.68498 | 2025-10-19 03:45:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92aa3fe9-36ab-3699-b0b5-3ad8c5fc1fe7 | -15.70386 | -41.26415 | 2025-10-19 03:45:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e101b337-b125-379f-9f76-659eeab2625a | -13.21398 | -43.15721 | 2025-10-19 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8fd48892-14e8-3685-a4d1-d0ba872b4282 | -16.20499 | -43.68869 | 2025-10-19 03:45:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8ff9f08-07a3-3263-9a01-678ee3b911c2 | -16.30733 | -41.88304 | 2025-10-19 03:45:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 96483694-a507-301b-ae47-b2568406c557 | -12.9886 | -47.28572 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 488c8ffd-c0f3-32ae-9a58-bc581fe6d658 | -11.65334 | -44.0849 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41c917e9-fa07-3c89-af2e-ba21431faad4 | -14.18974 | -44.79593 | 2025-10-19 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aace0d8f-2a31-3201-b76c-1da38acd9de2 | -11.14552 | -47.71571 | 2025-10-19 03:45:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97c673db-93d7-3809-b5a4-8b02df419814 | -10.6881 | -44.54088 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71dfd872-2ffa-37d2-8ca7-bb12920c1c3c | -10.91024 | -43.82677 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 124589a3-df46-3884-990f-d2b691a89c9c | -16.74142 | -42.76902 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1098319-3ef5-3a31-8fa6-bdeba6030f5b | -11.45006 | -43.4737 | 2025-10-19 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README17.md)
