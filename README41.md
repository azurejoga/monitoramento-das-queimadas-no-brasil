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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecaf0f78-c441-3399-ae8a-a8f6bd56e4d3 | -11.05751 | -45.16183 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a94543b3-36cb-3101-bdde-97343868de2c | -5.35325 | -47.21713 | 2025-11-16 04:08:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c832e725-33aa-3a95-99b5-d7d47d78c137 | -10.4467 | -45.08701 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a38b3c3-a2c0-3f5f-b9ae-ae51a1cd2bb0 | -11.15969 | -47.45668 | 2025-11-16 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d82e0023-b600-373f-9209-5946eafc1f35 | -4.84029 | -47.55821 | 2025-11-16 04:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 784591b3-1560-3695-a732-0eaa5bc60104 | -11.70655 | -48.40355 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ac56524-7832-38a4-9a0c-9d5d53d71641 | -6.71508 | -42.9483 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6ab164ac-3063-3b6b-ae9e-a129a3df0c8d | -6.70126 | -40.80299 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1e30054e-d079-3373-8559-5692bf802555 | -6.58997 | -42.89931 | 2025-11-16 04:08:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61123111-a2fe-387d-95ef-49cbaa0756b1 | -5.10801 | -46.22947 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed8d777f-119d-3fe5-9158-429d7720b8bc | -6.46076 | -42.0065 | 2025-11-16 04:08:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ce6223d9-3bac-32a5-a421-baf429863b8f | -6.08782 | -41.85147 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b248be7f-e527-3ffd-ab1e-5ac3aefd49c1 | -6.13777 | -48.05074 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 780c84bf-7fa8-3936-a3fd-8936bab21c61 | -13.00103 | -43.16777 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5fe543b8-e733-3a4d-bff7-073b29151593 | -11.99623 | -49.27137 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 053ec2dc-aa5e-3d86-8a18-62b5cef7a1de | -10.66983 | -44.26977 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1d6e2aa-556d-3b7f-9f53-70bb6c7fca07 | -12.42917 | -48.1588 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cbfb9882-19cb-331c-b9b3-ecf9ac714794 | -10.80082 | -47.99654 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5101486-db8d-3c30-900d-1869dfe71c24 | -7.02749 | -39.36923 | 2025-11-16 04:08:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d7eccf2b-bc88-37e7-a7fc-9cc6d55b1623 | -12.06194 | -48.20254 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d0ea238-5b9f-3481-bc58-cf2e1055109c | -9.60729 | -46.74598 | 2025-11-16 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e406f73-fe1e-32a2-a1d8-e48fe57bed85 | -12.39642 | -47.57393 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85c5aa64-25e4-3e94-b898-5effb3830507 | -6.71599 | -41.7461 | 2025-11-16 04:08:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10f2ab09-c821-3f6e-aaf8-1295913ea445 | -10.66543 | -49.36269 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| db73eaae-77ba-3425-9185-13e30f239e1e | -7.28596 | -46.71502 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b990c73-0a2d-3006-bdf3-21cdb212ab7e | -7.15289 | -41.75536 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bdcdc74-84d1-3bf7-bebd-06685a0d415e | -9.73493 | -43.95409 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ab17ea22-9483-35b5-8b24-83426e8f1020 | -6.65315 | -43.55224 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 482b4034-62dd-3ad9-973c-18030e960689 | -5.84432 | -47.68049 | 2025-11-16 04:08:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 449b2789-7905-3dfc-84fa-324bb4968348 | -9.24447 | -46.62713 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 485c4b1b-bbb9-3bc2-9f21-a347f9c4319e | -11.71001 | -48.40109 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fc439c7-d62c-3d9b-bf7c-48039fea685f | -11.71068 | -48.39723 | 2025-11-16 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15e92e9c-5871-33f3-9967-5982d28f1115 | -5.92428 | -42.26013 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6bfa06ca-5460-37cb-a897-c2cfc7e5efdb | -10.17044 | -44.49274 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98fc88b7-71a2-3836-b850-c5ac238d6fca | -10.4502 | -45.08762 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a022525-7ba0-34d0-b77c-d0e803eb730c | -6.36522 | -39.62449 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a08a1641-14a6-33a6-b680-ab37f9daef9d | -6.67693 | -40.80633 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7ea8a6d7-0ab3-38d5-b569-87228cf5fe1f | -10.43283 | -44.41072 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b6e802c-6091-3229-8cbc-503b6d173477 | -9.83556 | -44.17938 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b72462b-3cc5-3609-bf02-27fd282731af | -10.53812 | -47.92467 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d324dbda-a55b-302d-afff-c031fbec0791 | -6.50334 | -44.30597 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c66afc43-d95b-389f-90f5-71e3cc8d87a6 | -6.25625 | -47.08201 | 2025-11-16 04:08:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d550e004-09f3-37a9-9385-ae96d534f624 | -10.54631 | -47.92635 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59360dd5-67c4-34e1-bd13-2e36661deff1 | -6.67886 | -42.04509 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 89a1e909-40b4-38e4-a1bc-718f0138934b | -6.71647 | -42.12932 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5d979da2-bef5-33ad-a106-cef532ab7d01 | -10.00134 | -44.77327 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d931d0d-dfcc-35f9-a19d-7c37d83183bc | -5.75207 | -42.50638 | 2025-11-16 04:08:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4e11354e-8f51-39b5-ba53-bed972168e0c | -6.07182 | -41.54458 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f78b04a8-0abb-3075-906e-b0191aa9a701 | -8.31375 | -45.40676 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2622c558-f27e-33a2-b516-364e60224682 | -6.94885 | -46.70953 | 2025-11-16 04:08:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12ce5463-a825-3948-b462-9b09317b5e2a | -6.71261 | -42.13226 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7ac09b4d-7567-3898-abc6-a71473247bf6 | -6.36268 | -41.74602 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 85732ed3-f933-3c9b-9cc6-ba980ebb346d | -9.84762 | -44.16997 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b40e0e01-496d-3c73-9c7b-04b25eb9b1aa | -6.07869 | -42.86942 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b3b96d34-8b3a-3942-b3ba-e54d83971328 | -11.97031 | -44.9673 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5d67327b-a907-3c74-b0bf-4cbbd33d08b0 | -6.35731 | -46.1589 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b27ab6e-0634-3f30-9d2e-8d57d2bb9a35 | -7.01593 | -45.16323 | 2025-11-16 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f667543c-9634-3adf-b87a-c7070d86c30b | -5.48964 | -46.92028 | 2025-11-16 04:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51a8dd9d-4647-31d8-93fd-e24f7baf505b | -4.50182 | -50.11743 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c0624c1-fcf9-31bb-8771-58d4f6b76d45 | -12.65092 | -46.7513 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9c485f0a-69fa-3974-af4f-5f5549196d3d | -6.08951 | -41.60383 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 35af2760-7f7a-3930-b1a3-b3806633220f | -9.95383 | -44.93035 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0bc485e8-dbd0-377c-b130-6668cc50ea9e | -5.74961 | -43.01693 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 52ad0f1d-420e-3f6e-b19a-80c5351699a0 | -5.92816 | -42.25717 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68c0be67-6021-3200-8ec6-30e583dee4ce | -7.24939 | -42.56197 | 2025-11-16 04:08:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b1dd40e5-ed15-39f5-bcca-fad42d907ffc | -11.7971 | -48.08921 | 2025-11-16 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f030eefc-b858-3ff2-a2d5-1caa67d92138 | -5.99567 | -41.91845 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0ae96c3-d7a1-3511-a5dc-f494ed72b913 | -7.1819 | -39.43925 | 2025-11-16 04:08:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3fc43470-e8e7-3d40-8c01-33cbac4a85a9 | -6.07817 | -43.00257 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4b46dfd-4bd5-3492-877b-b8294143fbae | -11.17221 | -44.63202 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3a61076-f62a-3195-b461-eb5c4981c6cd | -7.14258 | -41.2396 | 2025-11-16 04:08:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f331809c-fdd0-3bd5-9413-5d7b2275b1ae | -11.10874 | -44.80614 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 621b23c1-459f-3a21-8af4-59e36faae26b | -6.31871 | -41.83115 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80a785bd-b98b-3800-8a90-9fb1b60276cd | -7.71489 | -47.28932 | 2025-11-16 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc40b89c-f35e-3429-96fa-e9d06b83e743 | -10.16612 | -44.51916 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 696fc028-730a-3acd-a8b4-7f07bb356498 | -10.66303 | -44.26865 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 546ef66b-d723-31c7-8a33-0446334dab0f | -6.30803 | -43.79531 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d57e84d2-3386-308a-b174-539fc9f3313c | -10.94054 | -48.69672 | 2025-11-16 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d59d7bb-cd00-3d57-b314-8e4ea2705c4b | -5.84364 | -47.68453 | 2025-11-16 04:08:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0a4dadc3-f003-3812-b25f-ade37984f4b3 | -9.73214 | -43.94982 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 692785b2-c997-31c3-aaa1-ebd81c3c1ab2 | -8.21926 | -45.98586 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff7c45e3-9274-3758-a9ce-46faa33b1813 | -6.66273 | -43.77314 | 2025-11-16 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22b706c8-a6bb-376e-9b64-4296b47dba77 | -6.71901 | -42.94524 | 2025-11-16 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ddad6ddf-42b1-3af6-8c2d-d3f54c3c88e7 | -7.71232 | -42.93972 | 2025-11-16 04:08:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5e79d45b-5ca0-32af-8d3c-dc94b7c83fe7 | -6.4041 | -41.46255 | 2025-11-16 04:08:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 045e493a-c1f2-31db-8eea-c790d6af717d | -11.42606 | -43.13655 | 2025-11-16 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 841c0d1b-7a42-3877-a360-059f1a2c1ed7 | -11.95915 | -44.94891 | 2025-11-16 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5cb2b67-f5f9-3eb8-8a25-8b8c0e3cf18d | -11.84069 | -43.32784 | 2025-11-16 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e367be8e-feaf-3a0e-b8af-cd7f0064cb97 | -5.48889 | -48.00405 | 2025-11-16 04:08:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3407b3a9-518d-3245-8844-f36e4857720a | -12.19936 | -49.54689 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20287500-3c0a-3e57-a763-b8492124a304 | -9.18506 | -48.84933 | 2025-11-16 04:08:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04dc4b9e-9fcd-35d8-a308-48f5aecd3f5c | -9.83837 | -47.62357 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b85aed38-8def-3ff7-8e9e-8d832a34fbca | -13.01047 | -43.12956 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 026220b6-6e66-3046-a51c-e3037073c88d | -6.77691 | -41.44794 | 2025-11-16 04:08:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6aaa30c1-f073-39bc-9cc8-df9ddd537d06 | -8.31742 | -45.4073 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8e9c52ce-76ec-3528-977e-79851dbe5ab5 | -7.37172 | -43.31915 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 237727ed-6294-3d26-806e-6d4faf24a10c | -11.17286 | -47.47468 | 2025-11-16 04:08:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 881f2fc2-22b7-3dd7-811c-a4c426faf068 | -6.3143 | -41.81627 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e92a588-3855-3f00-80d4-0947996600b8 | -6.51314 | -39.5284 | 2025-11-16 04:08:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b3899f9d-1a55-3041-b75e-5c7fbed7d204 | -6.93994 | -41.53353 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README42.md)
