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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 745518d4-418a-3538-b913-23c72cbf33da | -12.1468 | -48.258499 | 2026-07-22 01:03:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 293d8789-40fd-3f2a-bb7e-3ca58b394e05 | -8.7617 | -49.082001 | 2026-07-22 01:03:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1192fdc1-8373-3e6e-a4e9-7c46a8a0c4ba | -8.7326 | -54.619301 | 2026-07-22 01:03:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 750ef7d7-ff96-331d-b11d-a7d407dd8635 | -17.5748 | -47.4996 | 2026-07-22 01:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 2580acfb-bdcf-35db-9621-b749b8aecfbb | -13.3361 | -54.32 | 2026-07-22 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| f7d63efb-b784-3e03-9626-e543a078fc1e | -17.5748 | -47.4996 | 2026-07-22 01:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 648848fb-e4fb-3119-9046-3832745d7a0f | -17.5947 | -47.4956 | 2026-07-22 01:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 79fb3be0-92df-33bd-aa7e-814ebdace463 | -17.5748 | -47.4996 | 2026-07-22 01:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e298c9a3-79fb-31ac-a193-bd4eccea8bb5 | -19.5205 | -49.677 | 2026-07-22 01:30:00 | GOES-19 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.2 |
| 751a2780-c92b-30ce-83f3-c51e2bae2061 | -17.5947 | -47.4956 | 2026-07-22 01:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 04cbfef0-8459-3435-98ab-53036899ef73 | -17.5748 | -47.4996 | 2026-07-22 01:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 2955f6ca-9fc1-3309-9e4d-d605e15191e0 | -17.5947 | -47.4956 | 2026-07-22 01:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 7c2d4c1e-63ef-3213-9406-8bee859df73a | -17.5748 | -47.4996 | 2026-07-22 01:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 576ee6df-cad6-38f4-a879-177e294e2da1 | -8.7497 | -49.0782 | 2026-07-22 01:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 3ee01944-7b99-39bb-be2f-5cd5adc3b48d | -8.7497 | -49.0782 | 2026-07-22 02:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 356da216-c797-35df-ab21-892ff6d9b31c | -17.5947 | -47.4956 | 2026-07-22 02:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4d795bd7-4d36-32bc-b953-a7dea61a5741 | -17.5748 | -47.4996 | 2026-07-22 02:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4ccef073-de22-373b-bc1a-156e563685e8 | -8.7497 | -49.0782 | 2026-07-22 02:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 922a570a-d0e4-38e0-8af1-66e146d2c5c4 | -8.7685 | -49.0765 | 2026-07-22 02:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| a381053f-501b-350b-9812-9ba7aed053c8 | -17.5748 | -47.4996 | 2026-07-22 02:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9b13e23c-8a2a-38c8-8dbc-2a3d77413ee9 | -8.7685 | -49.0765 | 2026-07-22 02:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 17240be9-9710-3d95-916f-48bf5d636e1e | -17.5748 | -47.4996 | 2026-07-22 02:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9fdd3933-46dc-3ee5-bb5e-7cb82ccac8e0 | -17.5947 | -47.4956 | 2026-07-22 02:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| b4a619db-4f23-339e-a9d8-da1dfba2e923 | -8.7497 | -49.0782 | 2026-07-22 02:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 2a6ce20d-3438-3a25-aed8-b4b81f4b39bf | -8.7497 | -49.0782 | 2026-07-22 02:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 133.3 |
| 470036e1-d898-38aa-9a2e-9ad21fd99be2 | -17.5748 | -47.4996 | 2026-07-22 02:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 821cf319-fcd7-3c04-b6fa-7c708e23e7c1 | -17.5748 | -47.4996 | 2026-07-22 02:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fd2033f8-1cf7-351d-96d6-bb36f0a4f9eb | -8.7497 | -49.0782 | 2026-07-22 02:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 658e5e12-adf1-343d-8f70-eb0c7f78c7b1 | -17.5748 | -47.4996 | 2026-07-22 02:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 81246229-a412-3c66-b144-ab170ca6e70a | -8.7497 | -49.0782 | 2026-07-22 02:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1b7527fe-752f-3f78-82c6-53a24082d1d3 | -17.5947 | -47.4956 | 2026-07-22 03:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| ed3095ab-6a92-34c8-a842-ffcb4cbd53ba | -17.5748 | -47.4996 | 2026-07-22 03:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 5a5a2f30-139b-3583-88a7-88855c0b35a7 | -8.7497 | -49.0782 | 2026-07-22 03:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 80025266-d0b7-3c61-9a9f-193fded8b51e | -8.7497 | -49.0782 | 2026-07-22 03:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 82c43fbe-dde0-3372-9afc-4e2aff38d6dd | -17.5748 | -47.4996 | 2026-07-22 03:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 5c6e17eb-6911-3071-959a-876e6337f832 | -17.5947 | -47.4956 | 2026-07-22 03:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2574fe9f-0beb-3f04-a3f0-be8bf142525c | -8.7497 | -49.0782 | 2026-07-22 03:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8bfed864-18e1-3313-b00b-cb2de8ac8892 | -17.5748 | -47.4996 | 2026-07-22 03:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 2ffea4af-1886-3bd2-ab46-e00011ab2621 | -7.17915 | -41.4029 | 2026-07-22 03:21:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 117a0711-0de1-3741-ba99-85597bc6d52b | -7.17817 | -41.40544 | 2026-07-22 03:21:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d97b58c7-dd96-33ce-8f7c-f627d13813bc | -9.0087 | -40.99188 | 2026-07-22 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ac30d25-e0c1-302e-8d6a-4ab35c4e8a47 | -9.01479 | -40.99312 | 2026-07-22 03:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d5d01753-ce73-3078-927e-70e0540e0d5a | -7.17812 | -41.40835 | 2026-07-22 03:21:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4687c9a8-a431-3578-be86-519bfc6f75a2 | -13.44332 | -43.67555 | 2026-07-22 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e6aaff3-cef5-3977-b9a8-dbc0139b0f91 | -11.90907 | -43.84737 | 2026-07-22 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75e6fdcd-85ed-375c-9138-3ee9db617e8f | -11.89151 | -43.82977 | 2026-07-22 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e270c99b-5743-32e5-a1af-d42ca8a24f4b | -11.88327 | -43.83487 | 2026-07-22 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d21c75ba-2a50-3418-b540-b822a85f99ed | -11.90929 | -43.84743 | 2026-07-22 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1b6a9e07-62ff-3ccd-bd26-705ebff42e53 | -13.43673 | -43.67397 | 2026-07-22 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9a00e66-43dd-3141-98f3-9844695607d5 | -11.88466 | -43.82829 | 2026-07-22 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 48e0eab6-45b9-3163-8d15-fe73f2312e33 | -19.99426 | -44.25378 | 2026-07-22 03:25:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 498dec0c-f192-3130-98b3-94faae2335c9 | -21.97274 | -41.1147 | 2026-07-22 03:25:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2dd94413-2b58-356c-a4f5-ac5db6dae7d0 | -21.96793 | -41.11349 | 2026-07-22 03:25:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d2bb2c64-fb65-393a-8e24-e16f753b3a37 | -19.99309 | -44.25888 | 2026-07-22 03:25:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 30e2bd14-e945-3ac5-85ae-7013de2ca053 | -21.65943 | -41.32404 | 2026-07-22 03:25:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c9485527-8560-323f-9ffb-60313c1f4a45 | -23.27819 | -46.16245 | 2026-07-22 03:25:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1ab7689e-6b0f-30c7-803e-1e31d54bfd92 | -23.5178 | -47.21406 | 2026-07-22 03:25:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d9976c72-cc61-3a27-bdec-3388fb79d268 | -21.00512 | -42.57896 | 2026-07-22 03:25:00 | NOAA-20 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 90a7b3ea-37b4-37d7-b9b5-04ced4217075 | -22.25727 | -43.71081 | 2026-07-22 03:25:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7276721c-2007-3eb8-9848-681b4664bbe3 | -21.59795 | -46.06699 | 2026-07-22 03:25:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ec094cf5-8bc3-3a50-aea6-9bb6de77b8d3 | -22.25973 | -43.71111 | 2026-07-22 03:25:00 | NOAA-20 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 431b54fa-8dfd-3ba8-90a9-8d6efafd82a8 | -19.97863 | -42.70672 | 2026-07-22 03:25:00 | NOAA-20 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5356c00f-ce6b-3391-b026-9f369304a9fc | -21.5964 | -46.06697 | 2026-07-22 03:25:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 165ce203-d4e8-310e-8369-bcd37d617017 | -21.59777 | -46.06145 | 2026-07-22 03:25:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 850cce3f-f7ab-3586-bfaf-38ab60411d39 | -19.97717 | -42.70506 | 2026-07-22 03:25:00 | NOAA-20 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 19877125-7964-3f88-8452-790086d323bb | -21.97031 | -41.11599 | 2026-07-22 03:25:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9fae7679-1026-3296-a6a4-9c20a923f928 | -8.7497 | -49.0782 | 2026-07-22 03:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 6a783e3e-dad6-3c26-a60c-0cc91bc9b796 | -17.5748 | -47.4996 | 2026-07-22 03:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 77.3 |
| ca22c55d-2b14-310a-b68e-6b0377024804 | -17.5947 | -47.4956 | 2026-07-22 03:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 6d085cbf-7feb-3f40-8c5b-3e126a3bf497 | -17.5748 | -47.4996 | 2026-07-22 03:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d3b0c3c8-c28c-36e3-b106-90f6bbb4fcc4 | -8.7497 | -49.0782 | 2026-07-22 03:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 49.4 |
| be7ead6d-6bb5-3ac9-aac8-a855ec8cb643 | -17.5748 | -47.4996 | 2026-07-22 03:50:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b04f8d2d-9e39-3cd2-85ba-b7450ada539c | -17.5748 | -47.4996 | 2026-07-22 04:00:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0415c69f-bf83-3b6c-b47c-a9ba1f1bdf45 | -8.7497 | -49.0782 | 2026-07-22 04:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| d3da8711-f54e-3708-9bab-e20f27eab131 | -0.85889 | -52.7175 | 2026-07-22 04:06:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79d5cd89-bf03-313f-894a-ffba89619141 | -8.75096 | -49.08047 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| de0a802a-2e59-39bc-a667-c14019b3a8a5 | -9.22648 | -48.56085 | 2026-07-22 04:08:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 73cce4f5-23c7-30c2-a434-ce9796d7a09e | -7.83198 | -47.11248 | 2026-07-22 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17e70a54-ee4a-329b-ad80-4eea78534d37 | -9.69728 | -47.6983 | 2026-07-22 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c46f14e-0f37-3c7e-bc6e-7933303119f2 | -9.90048 | -47.87768 | 2026-07-22 04:08:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3628b783-c86e-3ca1-8c57-7cda7157fe32 | -8.11881 | -44.82325 | 2026-07-22 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83062a31-7707-3168-acf6-781f782c283c | -8.74719 | -49.07502 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 378b8ee5-65e2-343d-87ca-1368abff5910 | -7.90376 | -48.27951 | 2026-07-22 04:08:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2d9f96d-9ea1-37b2-890c-2976a7dfa07c | -8.75931 | -49.08675 | 2026-07-22 04:08:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e21415a4-a031-3ceb-91d9-e5731355d74d | -7.19723 | -45.49192 | 2026-07-22 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28031f78-e386-3026-8a9b-780f5ffaa8d3 | -8.7398 | -49.44674 | 2026-07-22 04:08:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e70408bb-b3a1-3327-8a36-3f0a08f596d2 | -5.94021 | -46.34926 | 2026-07-22 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a491f6e-96f2-397c-a98e-9cce21ead461 | -3.73126 | -49.27001 | 2026-07-22 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e722acea-e516-306b-9f01-2d5476b843ab | -9.22772 | -48.55526 | 2026-07-22 04:08:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| be38e8fe-703f-3117-85fd-340318aa32e8 | -5.74357 | -43.27064 | 2026-07-22 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2ca6c810-cdd4-36f0-8935-92e103a3c335 | -9.20619 | -49.82571 | 2026-07-22 04:08:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18a5ad0d-c353-3739-9fe5-79efa5af552b | -8.06571 | -42.2852 | 2026-07-22 04:08:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8a101165-798b-3eda-a84e-214e39a6d76a | -9.46378 | -45.6543 | 2026-07-22 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed5fd280-6851-30f4-a294-1a65c1377c8f | -7.8051 | -47.12275 | 2026-07-22 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1634464-4d25-3848-b766-db73dc302991 | -5.55449 | -48.72325 | 2026-07-22 04:08:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17668794-2b90-3921-8bdd-c5c532bfbd34 | -7.00478 | -45.43158 | 2026-07-22 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 889c7717-0fbf-3c3a-8c4f-6b313bfa0c50 | -9.23199 | -50.15253 | 2026-07-22 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f79e85-d0b0-3f01-b7fb-c2b4eaae9769 | -9.05631 | -43.95066 | 2026-07-22 04:08:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 844a50b0-c635-31d1-89e0-289ba5f30863 | -6.01332 | -47.10851 | 2026-07-22 04:08:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9f3b01e6-c737-3cfe-b8e2-61933714b017 | -9.01522 | -40.98842 | 2026-07-22 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
