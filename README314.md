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

## Dados Diários - Página 314

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d11eeedc-e14c-3ec5-9f98-ddca9e487d14 | -8.59807 | -44.87185 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c284bad7-879f-380f-b657-ecae63ac9a74 | -8.1863 | -45.77185 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9caea49-8402-3ec9-95c0-6a2c6bf5fa24 | -12.96826 | -51.00226 | 2026-10-08 16:37:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| c0ae73a6-09e2-38e9-ac3f-42850d675ff0 | -7.18324 | -44.32334 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 42c612b2-76b5-3d09-bae4-c6659fb8cc45 | -9.10167 | -45.123 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 9729ea59-a714-3f7f-bce9-b77b2b288785 | -10.87258 | -45.54764 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1b2e4d9d-24c9-30e5-b6ea-5b2cad8122b6 | -5.96422 | -43.89696 | 2026-10-08 16:37:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f92e0f0d-e4f4-39f2-b913-ec96e7e02f19 | -7.7199 | -50.42866 | 2026-10-08 16:37:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 63fd54f3-9aef-36a3-8952-3c75efe8cc5f | -11.39518 | -47.56734 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 98c56034-be14-3978-be80-384dff78da7d | -8.19093 | -46.36444 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 0fa8a50e-e99b-3e14-864a-1d72961bcdc5 | -6.93016 | -43.06924 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f5d057d7-bfbf-3072-8b91-74c871c4b18d | -6.79126 | -45.06293 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 894b693d-6413-34c9-ba6c-0538e07a229a | -11.77789 | -47.74438 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3069c00-3b2b-30b0-8dfd-7bc6b7a9f838 | -9.78611 | -44.78364 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4723e82-6275-3b67-878b-03b787df6d1c | -9.8124 | -45.69127 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| abbb078e-12a5-3f7b-9b25-f37979e4fb3f | -10.44308 | -47.27882 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b1e7ca4b-f20b-305c-90f4-051bcf08561c | -12.22754 | -43.93302 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| a3475f50-a08b-33e1-a037-8c444aba6b75 | -5.71624 | -41.6476 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 17beac85-6836-3b4b-857c-6bb9289d0ad1 | -8.0439 | -49.40599 | 2026-10-08 16:37:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4d4efc15-8f1d-3f4a-b0c9-14753701881b | -6.69563 | -44.92694 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2153eed7-3698-37d2-ad81-96484e725f09 | -7.53687 | -40.01019 | 2026-10-08 16:37:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| d72275ac-0ac9-3d60-89f0-9cb9f8e1f922 | -6.4549 | -46.01279 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b1097460-7506-37da-a4cf-9a3640868eb5 | -6.22027 | -44.86187 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 84725e4f-1c58-3bb2-a4a7-818c7a22e2b3 | -6.88683 | -43.70459 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 45.6 |
| e161d477-98c3-3ea8-9b7d-75d0e879d64f | -9.83471 | -47.46668 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 1b8a97e4-aa18-3315-9af9-748eba45647f | -6.8499 | -39.5471 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ce718d5f-cd79-374b-b7b1-60ba7aba2f97 | -6.67587 | -45.37113 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 38e2fa73-3bcd-3db8-835c-ede5493878c1 | -9.27899 | -47.44667 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 976b5682-9b65-38b6-98a5-1fab9f83a9a2 | -9.90228 | -44.81134 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 37.6 |
| f2a9b3c6-d9c8-3d08-bb0e-afb513609f48 | -6.15749 | -39.42368 | 2026-10-08 16:37:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| d8d377a5-b374-317a-993a-be85343abe06 | -7.1897 | -44.33289 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b237e388-60c2-37eb-bf4d-510d3ffe7f5c | -14.66684 | -51.45014 | 2026-10-08 16:37:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| aba39fc4-9b1e-3100-a21a-91dde8e5d872 | -17.69691 | -39.16809 | 2026-10-08 16:37:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 17514d6a-18af-38eb-ae04-667602c967a6 | -9.6256 | -57.88047 | 2026-10-08 16:37:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3a6e4245-94bb-3362-97a6-44ea3cbc3733 | -11.01079 | -45.42852 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7ccd8d60-45f2-36aa-9387-d7a5f669812b | -7.02994 | -45.44556 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 9d65e1ff-fa51-3d7d-a623-83175e106e1e | -10.03913 | -45.59804 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 75f9bf2d-50a7-3185-ace2-993bf489266a | -9.43911 | -41.74075 | 2026-10-08 16:37:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d71e1b4b-97d3-3792-b3ed-9ca55b7b1a5e | -11.0825 | -44.01558 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cdba5309-5e8d-3192-999e-e00917232067 | -7.39021 | -46.20478 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5724f4ee-b25d-31d2-97c3-1492e8092102 | -10.88155 | -47.60812 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 51182aab-d3ea-3f36-967a-7dfec7bfe814 | -12.41389 | -46.4399 | 2026-10-08 16:37:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 3b57fab9-2977-3554-b660-549c804fb81e | -9.89826 | -44.85133 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a292ad49-2639-33ce-b75e-55d48d4bbb83 | -9.84167 | -47.47768 | 2026-10-08 16:37:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ecdaa5f3-92d7-314d-b92e-b49001d35e7e | -6.2423 | -43.85704 | 2026-10-08 16:37:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0b8d54f1-29fb-34f3-b16a-4d1ea42739d8 | -17.96356 | -42.77213 | 2026-10-08 16:37:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 70924f20-fbad-3b5f-820b-a2642bf36e62 | -12.22359 | -44.74692 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 15e9a048-9bf9-367e-8ee3-3d6d70020bd9 | -13.16941 | -54.32753 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 38a823bf-2cd0-3acb-be15-b1cf79d67345 | -12.03616 | -43.44388 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 15fca354-e244-31b7-a801-7c885d2915e3 | -6.31837 | -35.15557 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 51bdbc8f-fea9-3bea-954d-6df89fd6bf65 | -13.7051 | -49.08853 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| e4aff4ba-927d-3073-8941-8a6c0c8f5a5d | -8.31205 | -50.37989 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 899a565a-97f8-3239-893f-9c7f33de687f | -8.28309 | -45.71724 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b7423f04-b10a-32c9-9dff-668332c0e8d1 | -8.95609 | -45.16829 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3a3ecbe8-dfd8-3eb1-9d4c-707a7cd48cec | -5.73854 | -39.6464 | 2026-10-08 16:37:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c55fa8cb-b2c3-314c-b02d-46564e055ca8 | -8.68725 | -45.27538 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38962de0-31fb-3598-b564-f54c3e1ce9c5 | -7.75163 | -54.94586 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 14ccafed-5d41-3a3a-b0f2-57f754ae6d7b | -9.43107 | -41.73763 | 2026-10-08 16:37:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 1cbdcd28-ef55-3ecb-83e2-ba41a51f0442 | -7.48072 | -45.95219 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0ba584b7-a6ec-37c3-af73-1c55b97ee4be | -5.75202 | -41.72142 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.9 |
| fd5175f0-7eba-3643-97c4-f1208bcc0dc7 | -6.95639 | -45.27559 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d74ef9db-f10b-3692-bac5-79bd9fbf88ea | -11.22351 | -45.26511 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 151011aa-376d-3258-a6e7-2fc7e6f0f322 | -7.03047 | -45.44903 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7495d0c0-cadb-300b-a232-9e827ff27350 | -6.40838 | -44.9551 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ae07546d-e5eb-38e7-9e33-d8912138fc59 | -11.83556 | -43.52867 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 8f64dd77-7bb7-3873-bd0d-ceea27c8b212 | -6.21747 | -44.86591 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 45637e3f-916f-3b7b-8d5b-3b8001341d89 | -12.75063 | -53.85664 | 2026-10-08 16:37:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d13bb968-6bb7-3e55-85b3-64c4f9f30b60 | -10.98833 | -54.219 | 2026-10-08 16:37:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 99dfa0ce-794e-316b-ad07-f224d27bf03f | -12.57359 | -45.08733 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dbee1403-7cf3-3b5b-bc8f-1b878a8bff7e | -6.01393 | -42.26286 | 2026-10-08 16:37:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c41c7879-814b-3ea1-98d0-8ac73ec642b1 | -5.71424 | -41.75695 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| 7d0bbef3-940a-3bfd-869d-9e3ccbd02185 | -5.9841 | -41.36756 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 03003cee-fa99-30e7-a5ef-c6376ad4332e | -8.30625 | -45.71368 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 71202c1c-c15b-3351-83ee-63ea48eeecc5 | -7.88294 | -55.00881 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 289bf662-8e8a-357a-b207-7fbbe03f09e9 | -8.27978 | -45.71775 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 009f5cc6-c8d2-3efa-908a-3ecae468e2ec | -6.7591 | -45.13997 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f7231b63-ba08-30f5-b77c-79c59164ba37 | -11.75887 | -44.94759 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 186eda34-196f-3e5d-b8ce-efc607a4321a | -18.18807 | -42.3432 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 261ae3ba-1dcb-3490-8ab5-36659d1c7069 | -7.30676 | -44.53151 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bd75ad8f-c32d-359b-9072-7d272f5b830d | -13.67907 | -48.63865 | 2026-10-08 16:37:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9ec2dafa-7917-3802-a767-d71a48e492b5 | -11.30399 | -44.83459 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| e4d73aa6-bfbd-392a-aee5-bb3d2af40694 | -9.44573 | -44.60207 | 2026-10-08 16:37:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 613b00df-cbf4-3889-bf27-5ded6e8dcace | -11.8555 | -43.53265 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| ab6b053c-d06a-337c-ae0c-a355eea66e6a | -11.13999 | -46.12985 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 51cabd36-b09e-384a-ae38-16eaffa8117a | -6.04444 | -44.38582 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36dd8f21-f022-31be-a96a-425232b3bc7e | -18.3887 | -40.31779 | 2026-10-08 16:37:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a05dff43-23b0-37e3-8ac0-248adcc02e49 | -8.94691 | -45.13052 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0c8c389a-cfb1-309d-be62-c0f8989d14bb | -11.8511 | -43.57005 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 01e5156c-eadb-34ac-af35-9ffba26b184c | -7.78133 | -43.81856 | 2026-10-08 16:37:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e527375a-2d9a-353a-8a6f-bd4dfa86058e | -11.62274 | -43.68925 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 9cab00a1-9af2-3a8c-89db-ed1dd1fd83fc | -8.26851 | -46.90617 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2b92fcbd-eda9-35dc-be51-be95154c245f | -14.00398 | -48.76141 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| cf32f9ed-2242-3858-917a-460e1e8cedc5 | -11.21662 | -44.86294 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 41d94c49-291e-3836-bb14-9255db700619 | -7.60552 | -44.64325 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 40bda1eb-6c73-3992-9f7c-3b1e5c750ec9 | -6.52746 | -43.53935 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9afb7717-c3b4-3520-b6a9-666310fcb010 | -9.82558 | -44.84188 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6bf58378-8888-38c9-99c8-0be0c3632217 | -9.5279 | -45.62624 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 453fac91-eede-39b0-b6d9-cdf9011cac69 | -11.24381 | -45.2428 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30dbb250-b2f8-3f9c-a4c2-e9c445c382f3 | -12.02275 | -43.44603 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| df73597c-f125-3198-b3e8-a16c90682539 | -8.65517 | -54.53286 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README315.md)
