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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a5b2ecb-06df-3bdc-a0c6-ddfafe605d7b | -3.5407 | -48.1673 | 2026-09-08 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 2821c114-8fe9-368b-aabc-4e02e56ca8dc | -3.5592 | -48.1666 | 2026-09-08 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 5df2feab-a1a1-3c17-9a3d-4082323bfef0 | -13.3 | -45.24 | 2026-09-08 03:15:00 | MSG-03 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 302abbee-6e69-35d9-8c5c-df07761e095b | -3.387 | -59.4266 | 2026-09-08 03:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d85f08ce-7ae8-3cdf-851f-72b14714d2c9 | -3.5592 | -48.1666 | 2026-09-08 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 7c7d5455-e729-3ae6-ab92-0f26cfd4d7bd | -3.5407 | -48.1673 | 2026-09-08 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 34f9ecd4-03f6-3fcd-a762-03f82623319a | -3.5406 | -48.1889 | 2026-09-08 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 153.7 |
| 80d714f5-28d2-3e02-a9ec-3a58eaf4be3f | -3.5591 | -48.1882 | 2026-09-08 03:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 2b86324a-3649-3e5d-897a-fed50c0a2f76 | -6.0281 | -42.65165 | 2026-09-08 03:21:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 1cce9820-0a82-3b67-97f5-0c48a277a6b1 | -6.02938 | -42.64481 | 2026-09-08 03:21:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 5bbfe80e-497c-3586-a09d-b1d272cf6494 | -9.73783 | -43.51986 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b700c8f7-e057-3e69-9235-0239a1dec61d | -9.70986 | -43.44302 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9937dee1-1bbe-3f4c-a172-63f594d008ff | -9.74028 | -43.49891 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 55691fed-e295-308e-bc05-8b80a4cf584d | -11.12865 | -41.8548 | 2026-09-08 03:23:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d280aa4f-2a4d-31e6-942a-fc6b23ac2f4e | -9.73357 | -43.50492 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd945939-c16e-35de-bc4e-789d46e47768 | -9.73193 | -43.50424 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 20606f00-e14d-396b-9dec-5fd3967fcba4 | -9.71401 | -43.45823 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3e42b47e-68e1-3576-9874-118fe4601a0b | -9.7237 | -43.48193 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dd1b63b2-3383-3ee7-820b-6de2953be50e | -9.7275 | -43.39127 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4e932593-e5aa-3e29-9a83-bc5ce6224c4e | -9.76106 | -43.47585 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c54840ff-50fc-3f47-8907-007e7c38b6d1 | -9.74318 | -43.49302 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 158ac589-28ca-3aa0-a579-a67c371416c8 | -9.75974 | -43.48254 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 594277a1-0a15-332d-9375-070cfc33ac69 | -9.0532 | -40.27036 | 2026-09-08 03:23:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 278adf18-cb7f-3089-83a7-12d7b75c8760 | -9.72505 | -43.47521 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a6fee990-69da-374e-8b36-de6605934ebb | -9.77051 | -43.4223 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 439c56a1-92c6-3512-ac56-60244c1ca380 | -9.73612 | -43.51906 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 15c53b65-f998-3203-89ea-b3bfbab699ec | -9.76368 | -43.45555 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd093a60-0f9c-3305-af83-0468225003ee | -9.74164 | -43.49232 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3c94067e-4c60-3b89-bcd7-43900a0879aa | -9.7691 | -43.42917 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50e25aef-911a-3531-b44e-b58599199222 | -9.73891 | -43.50555 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c1caad87-689d-343d-a3f8-afaf1a2e3eda | -9.71237 | -43.4306 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 31b2eda7-a938-39bd-8998-4b63710766eb | -9.73222 | -43.51168 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8697132d-b568-3de3-9989-ea5e8e068e5e | -9.71785 | -43.40342 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 8a93e345-d79d-3a9f-91e1-78e69279a89a | -9.74053 | -43.5063 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6598a52f-e78c-31a1-9b7c-f96ce4296361 | -9.75965 | -43.47514 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a62a851e-b7e9-3ab0-9b46-49355f525517 | -9.72237 | -43.48857 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17544e55-c9da-3701-94bc-201ed594cbef | -9.71111 | -43.43684 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a638b6a0-8bd0-39db-9d60-3630f46fad0a | -9.73919 | -43.51304 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 14276d16-9019-3c2c-a84b-a66e25c62f1e | -9.72629 | -43.39727 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c65368b7-052f-3a7b-9e92-3929aefa4d75 | -9.71506 | -43.41727 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7f7024aa-6cde-3023-a47f-c3f7093a57d5 | -9.75813 | -43.44743 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcc8cbb1-fa82-3b72-84cb-c86e6f53f8fe | -9.7349 | -43.49825 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 86f151ae-6547-3380-9c50-813f5b61075a | -9.70573 | -43.46343 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5317269b-d7f9-3d29-b202-d056a41a3438 | -9.70858 | -43.44934 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7bc1a61c-7111-31ab-af97-d73041769058 | -9.75828 | -43.48179 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f61b2c3-1a1f-3168-80db-0d86a19747bd | -9.71927 | -43.43215 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| df932cd0-a468-3117-abac-d2b250d63f2c | -8.27246 | -38.17872 | 2026-09-08 03:23:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fb2fa9f8-9c43-3fec-84a9-97be74a600fa | -9.71369 | -43.42403 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| aec5858b-e077-363a-ae53-e47b7320b6c8 | -9.70294 | -43.47725 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9a31ff8d-2be8-389c-b969-ac50f44fe186 | -9.70722 | -43.45607 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3397eba2-678f-3d3a-ba57-e92dbc3d6662 | -9.71919 | -43.39679 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 27b4ba70-35a6-343d-8f04-cfd7e7e565d1 | -9.76233 | -43.46209 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d3b3c22-8bb3-3667-ac7b-8fc57b531026 | -9.71645 | -43.41037 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1aff7892-d5c9-369a-b1e4-164dcfd8ab5b | -9.71799 | -43.43849 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0058147-e719-3762-8721-d18ba17e69fe | -8.273 | -38.1757 | 2026-09-08 03:23:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d648987f-6508-36b5-9f22-50caa985771c | -9.70433 | -43.47039 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 759fc7f0-7656-3435-8384-ea8b9987cf28 | -9.73752 | -43.51229 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6d5a733d-f9d0-331f-9c1a-e70dd20b5bc4 | -9.70418 | -43.43539 | 2026-09-08 03:23:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c7b5434b-d1de-34f7-872f-52d1755947fc | -13.43059 | -43.81417 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0d55d0c2-dd19-3436-992f-51e7fe680a4a | -13.43725 | -43.81556 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 946c50c6-7582-3685-bb3e-c20929397460 | -13.42931 | -43.82019 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4bd8bc06-8516-3b41-9e10-4deab212dff1 | -13.43456 | -43.81123 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f25fbbb5-04a5-3f28-b6eb-f431f7d4283f | -13.42657 | -43.81588 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 411f053e-4202-3df6-bf5f-60fc53df039e | -13.43323 | -43.81729 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 93d1b239-ed30-31b1-968d-81df26282ca2 | -13.42394 | -43.81272 | 2026-09-08 03:25:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 984991ab-6458-3a67-9387-e306dc136d13 | -3.5406 | -48.1889 | 2026-09-08 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 141.2 |
| 29306f64-3ec6-346b-84c4-f4d4a43c6cad | -3.5591 | -48.1882 | 2026-09-08 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 64a821cf-e888-3b17-93cc-7d4b39230eca | -3.5592 | -48.1666 | 2026-09-08 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a3bc9281-6663-3582-9100-3a343397dba7 | -3.5407 | -48.1673 | 2026-09-08 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 4f73650a-00f4-3c89-9091-2106ffb9468e | -3.5591 | -48.1882 | 2026-09-08 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| dcd06f8b-dc0a-3453-97ce-4331530bc049 | -3.5407 | -48.1673 | 2026-09-08 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 1721a388-22e5-36b0-8fd7-e2645ff8bd3f | -3.5406 | -48.1889 | 2026-09-08 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 709d4a0b-4287-3ead-8273-db8de5020a42 | -3.5592 | -48.1666 | 2026-09-08 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b8820c0d-13a1-3701-ae58-4dab2ac03bff | -3.5591 | -48.1882 | 2026-09-08 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 65f0b966-a9f3-37f7-a091-e7e6aabb3667 | -3.5407 | -48.1673 | 2026-09-08 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 2defb220-a5dc-31ef-9a86-61264cd9bb32 | -3.5406 | -48.1889 | 2026-09-08 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 180.0 |
| b6659733-a465-31e0-a240-fa76feccd781 | -3.5592 | -48.1666 | 2026-09-08 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 0e821c22-1aa1-35df-b6f3-7885e355265a | -3.5407 | -48.1673 | 2026-09-08 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 824ab0ef-ee3e-313a-a148-2d36ee88cde7 | -3.5591 | -48.1882 | 2026-09-08 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 5a459539-2433-3372-a930-9bce1d4a138e | -3.5406 | -48.1889 | 2026-09-08 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| b0103e90-e1d4-3c8f-bf9b-41676e96c042 | -2.06594 | -45.98525 | 2026-09-08 04:06:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 832cbbe6-07c6-3ff4-90f3-bbf2b1e73029 | -0.93695 | -47.1937 | 2026-09-08 04:06:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87f220a6-5419-351c-ac9d-19ff3716997f | -0.93874 | -47.19186 | 2026-09-08 04:06:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3bd524ef-e8f4-35e2-9039-4a73b459c747 | -0.93421 | -47.1912 | 2026-09-08 04:06:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c6e489-d017-396e-bb26-92f642e50dea | -9.76742 | -43.50855 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82b7e135-7ff1-3d96-b49f-5ce7ec70eed7 | -3.32871 | -44.58841 | 2026-09-08 04:08:00 | NOAA-21 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c543186c-a4cc-3284-b318-c4eedcf1faf1 | -9.7091 | -43.46629 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7f3a5816-2da7-39d4-be33-50cc25064680 | -9.74682 | -43.50888 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5c6041f-1fbb-330a-845e-0323ecd8e634 | -4.36874 | -47.78118 | 2026-09-08 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32fe33fb-3ae1-3504-9f14-61aa927519cf | -9.76701 | -43.44648 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 73ef7fa8-cd89-3a05-b4b2-00219fbcdb2d | -9.70576 | -43.46575 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5c8f9664-ae4c-3b02-a187-bc3dabdaa73e | -2.885 | -50.45856 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52009a3a-cab2-3d2b-a2f3-0230059fd2be | -7.29785 | -43.9325 | 2026-09-08 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de356f3c-54b1-3e1d-9ee6-52c59bb3f428 | -7.37181 | -47.02016 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9989d5a3-0d49-3bf9-a7fa-85bc754c12ef | -6.76518 | -45.48357 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fd78525-8e31-323c-87a6-6a3bd1ddfaa9 | -6.41873 | -46.20151 | 2026-09-08 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e8d764b-0b78-3811-89f0-c7913226f7f9 | -9.76753 | -43.46478 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 431d6402-d899-3fae-ad21-697c8148de28 | -9.7647 | -43.48255 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a16658e1-a2a4-3f15-85c9-b111d7038360 | -10.19875 | -42.21264 | 2026-09-08 04:08:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5cf146ec-ca1e-3524-9645-331e7e1a6a9b | -4.03825 | -50.88006 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README9.md)
