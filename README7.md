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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 051ca10b-624b-31ad-a808-b72757613563 | -18.57054 | -43.5587 | 2026-08-09 03:34:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ce111421-82d3-3a28-be92-e32ac5e59b35 | -19.58038 | -42.59462 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a972dccf-3e60-3c60-b5d6-cc18012c9b26 | -19.57804 | -42.58523 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dab5601d-1432-30ca-983b-b79f8da7b93e | -19.93962 | -44.3762 | 2026-08-09 03:34:00 | NOAA-21 | JUATUBA | MINAS GERAIS | Brasil | 3136652 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 880249a3-cd92-354f-9428-6fe025fe7ba7 | -22.23378 | -43.0423 | 2026-08-09 03:34:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f8d4b5a2-9940-3e36-b710-b5a0cfd9c495 | -20.26916 | -41.64788 | 2026-08-09 03:34:00 | NOAA-21 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9b6c74ff-c6ed-3723-a4c1-e3ce45321805 | -21.32001 | -43.77673 | 2026-08-09 03:34:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 96da874a-4cfe-3c52-8fea-4d0523894d00 | -22.89699 | -43.6572 | 2026-08-09 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 151d9f52-6841-35ee-ab62-0bae923e7222 | -20.55118 | -41.02569 | 2026-08-09 03:34:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c43b471b-3955-322f-9747-e7630224ad3a | -22.904 | -42.93755 | 2026-08-09 03:34:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3fe475c3-4b66-33e4-919e-8109d1bcbee9 | -19.585 | -42.59537 | 2026-08-09 03:34:00 | NOAA-21 | TIMÓTEO | MINAS GERAIS | Brasil | 3168705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 36a0fa4f-2b01-3d4b-99d1-155e3c253cf3 | -19.15362 | -43.49878 | 2026-08-09 03:34:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f13a56f2-724d-3952-8a96-e6cf820aa727 | -22.22936 | -43.04102 | 2026-08-09 03:34:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| aa4c7083-6db4-32a0-b02f-04e3a8e9bb51 | -19.05423 | -41.01001 | 2026-08-09 03:34:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4655589e-470a-3b54-8604-fc89fedbf7a6 | -21.59905 | -43.46552 | 2026-08-09 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e7d51dfc-8b55-3401-863d-1f100a0ef5fd | -6.8388 | -56.4146 | 2026-08-09 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 09055fe8-71ba-3611-823c-ec0d91c39a4a | -9.4582 | -40.3143 | 2026-08-09 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 1e48a9d4-6725-3fdc-a430-03b6d0b48550 | -9.4769 | -40.3365 | 2026-08-09 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 157.7 |
| 765cc9ba-5c3e-3d85-b18b-a70a677e8676 | -9.4773 | -40.3116 | 2026-08-09 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 253.4 |
| 75507458-fcd3-3f56-b52f-e0c2a26c9cdf | -7.5736 | -45.2062 | 2026-08-09 03:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e0617478-96e3-3572-b265-f3e9c11218ba | -7.5924 | -45.2044 | 2026-08-09 03:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 14d5fd18-c0e0-31bf-9d83-9945fd8c46dd | -9.4769 | -40.3365 | 2026-08-09 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 156.4 |
| 32f3615d-4cfd-3075-800b-bb600cc1a550 | -9.4582 | -40.3143 | 2026-08-09 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 352192c7-6b31-340f-8526-f922565037ea | -9.4773 | -40.3116 | 2026-08-09 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 265.8 |
| d85e0d61-afdd-3b0b-abd0-0291a4d446f3 | -6.8388 | -56.4146 | 2026-08-09 03:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 67dc6659-e30e-3d06-ab25-30f5d4392cf7 | -9.4777 | -40.2867 | 2026-08-09 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.4 |
| 331fc275-fd78-33da-bde1-47feb3885e37 | -9.4773 | -40.3116 | 2026-08-09 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 526.5 |
| 05e794cb-7882-3a7c-8d99-1ee3e164d99d | -9.4769 | -40.3365 | 2026-08-09 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 295.1 |
| 8eb1a46f-1345-3c30-837d-6357ef290233 | -9.4582 | -40.3143 | 2026-08-09 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 250.9 |
| 1a5f7091-5dd6-37f2-80b9-847d1418bfc3 | -6.8388 | -56.4146 | 2026-08-09 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3c3a90fc-4280-382d-9ad3-2673affa0fd4 | -9.4578 | -40.3392 | 2026-08-09 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 146.1 |
| e264774f-be16-3b09-a789-0fbe41079b25 | -3.12349 | -40.11003 | 2026-08-09 04:04:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 683c2041-da18-3b7f-82c3-ea7e73420773 | -3.12411 | -40.10618 | 2026-08-09 04:04:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 260b7675-f041-3b03-b0db-50df26282984 | -5.73061 | -49.14038 | 2026-08-09 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eb6acd15-9f24-3375-9482-84418b6a76b2 | -5.8832 | -46.50326 | 2026-08-09 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67464a2c-1c82-3a69-82ec-334f71720135 | -9.4774 | -40.32418 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 42d45ae4-2b53-3bac-acf4-fed50774892b | -7.45418 | -46.8749 | 2026-08-09 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eefaad29-8637-394a-88a7-431552fd1fd8 | -4.95248 | -37.48973 | 2026-08-09 04:06:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e7d528f8-0460-342a-91dd-96202e84828b | -4.95193 | -37.49322 | 2026-08-09 04:06:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b6cc25ba-2a54-3cba-bdb0-3a4d330d290e | -7.62588 | -42.74938 | 2026-08-09 04:06:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 96d975bb-5077-3c10-9110-bef1ba1e7963 | -5.88321 | -46.50457 | 2026-08-09 04:06:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71d3c846-4803-3bb4-aab6-baca4afc641f | -6.30585 | -43.62018 | 2026-08-09 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 936ab362-fafb-332b-9481-74703147509e | -9.46398 | -40.32198 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 211.1 |
| d25bb1cf-92ec-31a7-b673-7f4fa6567211 | -7.5675 | -44.38762 | 2026-08-09 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3607423-da7b-3b76-9de6-47de5240ee33 | -6.87455 | -44.92521 | 2026-08-09 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a7d5bb95-b5ed-391a-9ed8-c50055e588f7 | -4.86302 | -37.45811 | 2026-08-09 04:06:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c25b8dd4-81ab-3e01-81e2-a924c7c8cce6 | -2.96221 | -49.27163 | 2026-08-09 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0c935c5-7e72-3314-a8da-1361a279ae6b | -7.57236 | -44.38447 | 2026-08-09 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 857667ca-b0bf-378d-9b49-55343c5238cb | -6.96441 | -41.50714 | 2026-08-09 04:06:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3410f4e7-7dcc-304f-ae94-1ef58985780e | -2.69523 | -47.36077 | 2026-08-09 04:06:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bec1902f-3992-369e-b8b6-114b6c3906fd | -6.98101 | -42.90358 | 2026-08-09 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 083eae50-5b7f-31b3-80f4-07057b491654 | -6.97357 | -41.49613 | 2026-08-09 04:06:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| aa245485-b601-36a7-b078-19ab39671945 | -6.98485 | -42.90427 | 2026-08-09 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 95dbd345-99ee-351d-9ac7-6292dc5f6726 | -9.47462 | -40.32005 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| ae5c5069-670d-3ef3-9d3b-5466f2848a5f | -2.37896 | -48.22838 | 2026-08-09 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d9e2301-135e-3346-942a-5dca5f8be03c | -4.45924 | -47.91781 | 2026-08-09 04:06:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7bafe65-c7b0-378d-b7d4-805c0d02add7 | -4.26657 | -48.19391 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| ce122137-3c88-3620-8bbc-75e63058292d | -6.86809 | -44.43227 | 2026-08-09 04:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d1120b5-92ec-3dee-b19d-c4a1189f378b | -5.73137 | -49.13612 | 2026-08-09 04:06:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b2236ee-20a5-3104-970c-65ba99479a0e | -2.95922 | -49.27048 | 2026-08-09 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 626a34d7-e853-3220-bb9e-33d60c9cb855 | -2.37641 | -48.23032 | 2026-08-09 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16ef054d-9e30-3af8-b217-270cc1661de7 | -4.90145 | -43.47245 | 2026-08-09 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d896be8-ffd7-3e15-9f2c-776daa47e512 | -9.4634 | -40.32556 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c652bdee-a46a-3491-8904-7babf947bfb8 | -9.46514 | -40.31483 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 80a4709d-24c1-3e34-bef6-1b02e2a0882a | -6.98407 | -41.47704 | 2026-08-09 04:06:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a4b54eeb-d7a3-35e8-a5a6-6153381821c1 | -9.47347 | -40.32721 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 02a69380-fafa-3c89-a179-20621ee5f7fd | -8.01324 | -44.48718 | 2026-08-09 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65c7ba9d-0559-3a10-9ccc-b3cc1d911b72 | -2.96004 | -49.26559 | 2026-08-09 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f741a057-865e-3e4c-83b6-1fe3725aae58 | -7.57169 | -44.38834 | 2026-08-09 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d03ee1bb-f1ab-3df1-ba8a-bc920ffba748 | -7.58978 | -45.21294 | 2026-08-09 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 995a7391-fb6e-3b68-a32d-10193306bab0 | -9.4612 | -40.31786 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c1b94550-8f59-3bce-8e81-acdde3ce3d11 | -7.08494 | -42.26163 | 2026-08-09 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ffe5634-f972-333b-ac1e-4aaf884f4e46 | -5.24208 | -35.51468 | 2026-08-09 04:06:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 444eec5a-2a56-313d-9fe2-d707b35314a7 | -9.47682 | -40.32776 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 93a6b654-1e5a-316b-ba8f-3db1caf5b732 | -9.46849 | -40.31538 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 45bd00b7-685d-3ffc-ba91-25888418d0e5 | -7.28894 | -38.93647 | 2026-08-09 04:06:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82921edc-b3fc-3bd1-9a0a-c7a80d410b41 | -2.37715 | -48.22606 | 2026-08-09 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b75d32d-b649-375f-af08-c5e7a8531b53 | -4.10475 | -49.2746 | 2026-08-09 04:06:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ce8fefa-7385-3e33-81d4-28a380d7c8e1 | -4.26085 | -48.19288 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 42756bce-f8cb-3d53-a380-0d870f45a129 | -2.96306 | -49.26672 | 2026-08-09 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 813f177c-7eb2-3687-9f2e-7237e8324b24 | -6.92517 | -42.42933 | 2026-08-09 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 924b8764-5910-343a-9c73-068f0ea52d30 | -7.58091 | -45.21146 | 2026-08-09 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| b992d5ed-f5cf-382e-afd9-22d8814e72d6 | -7.58608 | -45.20796 | 2026-08-09 04:06:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| f79024bf-deac-3eab-8ab1-d0118f1f158d | -9.47011 | -40.32666 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 53.8 |
| 0bef0b20-acce-3a91-9ad6-9915a5e6d0e1 | -4.90401 | -43.47231 | 2026-08-09 04:06:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e7376dc-e70c-318f-a667-5fbb701642de | -2.37826 | -48.23267 | 2026-08-09 04:06:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45b10679-ab40-34d5-9c8a-eae862d3fd60 | -6.86744 | -44.43609 | 2026-08-09 04:06:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 22b17f55-7a8a-3860-bafb-62df4e3c2024 | -6.92814 | -42.43453 | 2026-08-09 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1382266a-e122-33f3-9f1f-57f41274dd1e | -7.62583 | -42.74731 | 2026-08-09 04:06:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14c38c35-8d6e-3909-9818-a6fc2ace0329 | -7.0842 | -42.26604 | 2026-08-09 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1bcffd96-c473-3401-83f4-fa537a912353 | -4.27363 | -48.18715 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1fd3743f-7ad7-309e-a46e-a3a1a2b62f65 | -2.96391 | -49.26185 | 2026-08-09 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 343a54a3-fd75-3c51-88fe-b2c5a6ebcc4a | -9.46733 | -40.32253 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 211.1 |
| 26844212-0860-35a0-95bb-2b376f9f2025 | -6.87893 | -44.92607 | 2026-08-09 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| aec6bf17-f814-36a8-a7a8-8b92374e7cc2 | -4.26724 | -48.19 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 22108aa3-a4ff-396a-b4f7-10eb97e65cd3 | -9.47127 | -40.3195 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.2 |
| 5bb650b0-c920-3b60-a501-ec4ac880d176 | -9.47185 | -40.31593 | 2026-08-09 04:06:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 30adcfd7-56a6-3365-a503-7e7df286d93e | -4.27937 | -48.56599 | 2026-08-09 04:06:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 39d76cf1-fd2e-309b-a4cc-bbb27471b711 | -7.08716 | -42.27113 | 2026-08-09 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3d61b607-32f5-3d16-9ba1-3d89302747b1 | -8.91742 | -44.24281 | 2026-08-09 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
