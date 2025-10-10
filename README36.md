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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffe6086d-035c-3501-a1fc-d08fe9c4ff2c | -7.26149 | -44.09672 | 2025-10-10 04:51:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12b4f377-606a-3b64-b2d2-e18d34a90cd5 | -7.60253 | -44.03033 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dfeb06ad-6b71-36a4-82f7-b60c65da10ad | -7.83918 | -44.54823 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3762fb4a-f61b-308b-b74e-f5b50d8fa864 | -12.62914 | -45.06347 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3f5b1c38-1492-36dd-83ad-c1c7da392745 | -8.51439 | -46.12518 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c711bf85-46fe-3527-a51b-f4948753f2fa | -7.77729 | -44.04403 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0a0f7d3-6d6f-3f2d-830c-d2da30f7fe68 | -5.58137 | -49.74491 | 2025-10-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c7c33f-a066-3c1a-9aba-003d1ad6f8b3 | -7.14612 | -42.20213 | 2025-10-10 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7b4d8b55-4d06-33de-97fc-efdf7049d7f4 | -7.49544 | -43.10326 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ec77ea3-a910-39d7-8281-896c7674ffd2 | -5.1289 | -50.71312 | 2025-10-10 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0cde78f-4a10-302a-802b-0f8799f75fe6 | -8.50129 | -46.11845 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8b19039e-bc26-3bd3-a17f-027d72090451 | -6.58104 | -44.62073 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 835d40f2-8cc7-3c56-8672-1b2ecf6f84b7 | -6.82221 | -42.79904 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d2a4298c-67b4-3a0b-acb2-c42331fac046 | -7.53419 | -44.30454 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2e2f481-ad31-3454-9e10-7bdb3ac7a810 | -12.15024 | -47.92038 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1c1430c-9ce0-3d8b-9e49-b170c23036b4 | -12.62837 | -45.06976 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 197903be-0276-3c6f-b81e-0e17319e1034 | -10.98352 | -59.06466 | 2025-10-10 04:51:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcec3285-9dfb-31d8-a293-db37d5712b71 | -8.18635 | -43.32514 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 53c7a0b9-5da1-3c2c-ba83-fd7e28dd3369 | -7.99406 | -44.46341 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef99dba7-f08b-3bf6-b947-c8875f29e9c7 | -8.18083 | -43.32431 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d8541a9-fe4f-392c-b07b-7d8943a583c8 | -6.59605 | -44.7971 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c8ef7e7-4796-31f1-a525-de3b1c8c997a | -12.15452 | -47.92101 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ff5a08c-a484-303d-ad0d-4e5aefa69dbc | -7.78163 | -44.05124 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4bf0320c-483c-3e55-b5d6-704379db8917 | -8.52422 | -46.12175 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f0ce1e26-9817-3cd4-8337-11ccc6123970 | -6.59093 | -44.62212 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c511cad1-f711-3eb1-a0fb-379df9f42e6a | -7.24815 | -49.5147 | 2025-10-10 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 00ba0b41-0712-3cb5-9863-6a8a1c6eb115 | -6.66321 | -47.74925 | 2025-10-10 04:51:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2c2c561e-74d7-3163-8627-f9ae7af7eb78 | -7.54529 | -44.60472 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a88ad676-798d-32e0-945e-4e70d27c3493 | -7.50768 | -46.63729 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 452f7b91-32f2-34e9-afee-4dfcbdbe9a8d | -7.4631 | -46.57467 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a93d6869-01da-35d7-a037-eb4670ad372e | -12.63359 | -45.0705 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a954c022-79c3-34fe-a52b-56befe4c6152 | -8.19714 | -43.32837 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 7c3ddcce-3775-3ebe-8484-ccd839abec26 | -12.98327 | -47.94153 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74551fba-9eb6-3f46-a179-2c7816b52b4f | -8.14701 | -47.08667 | 2025-10-10 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ace693b4-61b7-3b6b-8c13-bd120abd5091 | -10.16095 | -44.6096 | 2025-10-10 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cd7e366-0235-35ca-9eb7-c72468b56e03 | -8.90032 | -46.01194 | 2025-10-10 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89753c5f-0957-3fc9-a12c-d11a7a6d19fb | -6.82375 | -42.7877 | 2025-10-10 04:51:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4e80cd6e-bc62-3731-97ff-9535869f3f64 | -12.64197 | -45.04571 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 793a1b2b-7955-312c-8f3d-05dd9ccd6a7e | -7.33144 | -47.81863 | 2025-10-10 04:51:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3769532-2b3c-317e-a988-91258c4b28c7 | -6.19939 | -49.03968 | 2025-10-10 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f4ed5bb-f75b-35da-a6d8-f3a2f1a62f74 | -12.72216 | -45.83633 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f004e45-280c-3d59-9f56-9de7ce351ebd | -6.46315 | -44.58622 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 638c2dc5-7ed0-3160-8003-03baa05fc019 | -8.19188 | -43.32591 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| d0c557c5-3629-30a9-ab6a-ecf25570bebf | -7.77642 | -44.05033 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e4e12f0-12c7-33af-b9fa-fca0883cc75e | -8.50522 | -46.12386 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 46b15c98-bbb3-3bd0-a890-ab0b4bde6f2c | -7.9217 | -45.49312 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5d38c649-3c31-3228-97b2-04c5b75b6ea7 | -8.52029 | -46.11635 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4ce933e-3537-3392-b35d-541fe647520b | -8.53996 | -46.10951 | 2025-10-10 04:51:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 219c0f0b-58b9-3e1c-9fa4-04502d2b0710 | -12.72287 | -45.83064 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 620fd867-44e7-3bc4-a661-0511c691302a | -6.45976 | -44.5743 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 898a997a-9b57-358f-8f58-e69ea23876bf | -7.14725 | -42.19378 | 2025-10-10 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| def6c049-bcf0-3c45-8bd1-84ab04cd4da0 | -7.01636 | -49.71283 | 2025-10-10 04:51:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df7bfcc4-ff42-314b-8829-903902fcc519 | -8.18608 | -43.3269 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| c05d6e13-d417-3a35-af14-d92dcecc8c4b | -8.52814 | -46.12716 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1831feee-0051-36dd-8899-dfd1a974e8c2 | -7.67687 | -42.39601 | 2025-10-10 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 27feb2ce-69e4-3a28-851f-d7945f28c451 | -8.00546 | -44.4561 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98bab24b-905a-3ae4-a27d-9c1502bce410 | -8.50915 | -46.12925 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| ac57be5a-270f-30c3-bf48-d98028507e46 | -7.1114 | -44.08775 | 2025-10-10 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 55a8fa88-ddd9-3085-adbc-7439dc166a3b | -7.60207 | -44.03376 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c79aa8c1-4923-3dcc-a04d-a09e8506a5f7 | -9.86345 | -59.87446 | 2025-10-10 04:51:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa12f197-fdac-3052-98ee-b36b4deee691 | -7.24452 | -49.51414 | 2025-10-10 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf349f61-f9f1-3882-8261-735db97e17ae | -7.90574 | -45.49498 | 2025-10-10 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 442cefe3-ca8e-3633-8984-f336b3f5ea53 | -6.5936 | -44.79878 | 2025-10-10 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 60f71f62-f5fc-3f60-ba45-786518214f82 | -9.65947 | -43.8518 | 2025-10-10 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ae5206e-4452-3f10-ae64-4c2570730aa1 | -8.51832 | -46.13056 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 85207452-5b43-30e2-8db9-935b93747a3f | -5.64212 | -50.31775 | 2025-10-10 04:51:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e9745c2-03e5-34bc-924d-f781ed01a8ec | -7.77175 | -44.04892 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4af6fc3e-c014-374f-ba35-25d374d69060 | -8.50064 | -46.12319 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c706e445-69dc-35bd-9d17-f65979d2eba2 | -8.49935 | -46.1326 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c18190b2-fdbf-30a5-b38d-a34b00b0b0fa | -8.51309 | -46.13462 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 61519723-34c7-341f-8e36-a61b18cfea00 | -7.8891 | -44.85403 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d49f896b-827f-3033-83dc-af70b3514000 | -7.77207 | -44.0432 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f01c7f6-b26e-36d8-a2f2-564e2f1a5ebe | -13.06654 | -43.84072 | 2025-10-10 04:51:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2ecae6bb-64f8-3c4f-af42-5f965304c56b | -8.2056 | -43.3504 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e5d4cf11-c0a0-3d98-b697-43d072839cc2 | -8.00982 | -43.756 | 2025-10-10 04:51:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ada62ca7-d1ad-302c-9380-4af706dc831d | -12.64157 | -45.04892 | 2025-10-10 04:51:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9563a340-54d2-3471-971b-2999874d38da | -6.4315 | -47.82497 | 2025-10-10 04:51:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 782e91a8-431a-3eac-9fc3-8d36cd2570a8 | -9.66033 | -43.84508 | 2025-10-10 04:51:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| be854336-cef6-3c0c-8f70-bb7b7b1629ff | -8.1813 | -43.3206 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c4918bce-3618-3ba4-9b4b-465f94ab7cbf | -6.59183 | -46.68915 | 2025-10-10 04:51:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd08a35b-cc08-3813-9076-fcdabb2cb338 | -7.5507 | -44.60262 | 2025-10-10 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 021af28d-0fea-30cb-8722-706379073219 | -6.81606 | -42.8022 | 2025-10-10 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 04b6c1ca-87f7-3e3c-a69c-4f2ff12e8843 | -7.67739 | -42.39198 | 2025-10-10 04:51:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2bdb070b-5b4f-36d1-bb40-e9fb11041f34 | -7.14668 | -42.19799 | 2025-10-10 04:51:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| aad49c63-8f1e-3d34-b80a-b1844ea2b774 | -7.77164 | -44.04631 | 2025-10-10 04:51:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3b6b46a-900b-3926-8923-faf5965c31c6 | -13.04954 | -46.80369 | 2025-10-10 04:51:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2ea4095-1473-38a5-83d4-f471e990b20f | -13.02996 | -47.88828 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7ebff18-589b-385f-ba5f-7fde2186c264 | -11.82913 | -47.09457 | 2025-10-10 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6d5d09f0-8e25-36c9-9213-6bc521589357 | -7.63144 | -43.05582 | 2025-10-10 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6da0769-9806-3611-9355-972071f7b516 | -8.51963 | -46.12109 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f241e0fa-116e-3fd5-b522-7ad06805521a | -5.98352 | -45.91566 | 2025-10-10 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3e5a396-ba5c-3248-882a-e2e36d026209 | -13.02571 | -47.887 | 2025-10-10 04:51:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2f52d37-fa5b-38e6-9903-9b427e4c2ef4 | -11.63712 | -47.52768 | 2025-10-10 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb1f1174-cfb0-33b2-ab3c-97633dd9e61a | -11.77048 | -45.04448 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2214b95f-423f-377f-9a2d-ac2dc767af7b | -8.50264 | -46.1426 | 2025-10-10 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 66b8dda1-fadf-3371-beca-0a30d453461c | -8.19646 | -43.33407 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| a20da492-4a6b-366a-837c-06fd34260521 | -10.77324 | -47.60518 | 2025-10-10 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4d57665-7e61-3ebf-9638-cf82fbee3dec | -11.86159 | -44.91712 | 2025-10-10 04:51:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e361a13e-907a-3d95-87ea-657e5dc87817 | -8.21013 | -43.35876 | 2025-10-10 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1707a76a-9094-32ae-80f7-4dddc413ed70 | -7.05346 | -45.0504 | 2025-10-10 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README37.md)
