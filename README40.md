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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eafeac88-f2a9-31d3-9c90-6b8f1c05ae6f | -7.13073 | -41.65973 | 2025-11-16 04:08:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 547e4ac6-a493-36e0-9ebe-c17f786826eb | -10.80287 | -47.99317 | 2025-11-16 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cffd0108-e292-39f0-a9a9-8bdb68c525fe | -9.74613 | -43.95592 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a382ab16-5040-3e2e-90b9-1b73a45ee63b | -7.3473 | -43.3413 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a3fbdaa-daef-3efc-970e-db31cc5fd0a5 | -6.67555 | -42.04457 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 43774e6b-4cfb-3cda-b912-16330d458837 | -12.20923 | -49.61913 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3c5b95e-9520-3f1e-bb7a-ac7303b5ed73 | -6.35338 | -46.15829 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 004679de-27bf-3c34-88bd-ba111d1bb19e | -9.95885 | -42.3176 | 2025-11-16 04:08:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df849c1c-3845-3af4-92b1-2a9e3256419a | -9.34426 | -46.58702 | 2025-11-16 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbde427a-66ba-3ec0-87c7-8708e60178ef | -10.76859 | -44.50409 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a907348-54ab-323b-9541-fc79e8894f8e | -8.53607 | -46.08693 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7b389f6-aeb6-3ced-84d1-30db6393d8f0 | -12.65463 | -46.75198 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32e22d3f-d034-345b-a8e6-7ae3719127cd | -6.71205 | -42.13573 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a3c1363f-f97a-3f54-823b-f1cf347bb031 | -7.21697 | -47.97968 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f5ee76e-c6b8-3295-bdb2-e93bce00e262 | -12.40214 | -47.5645 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd0f2d9a-476c-399a-8182-0f77aae9fb4c | -12.40963 | -47.54507 | 2025-11-16 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d17ccc8c-bb09-3f3e-9971-10802cdab8de | -11.67293 | -43.90631 | 2025-11-16 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4c957e5-9fec-3f39-bc15-89aacae5d62c | -6.81622 | -39.14367 | 2025-11-16 04:08:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e126fd1e-3be9-3378-a2a9-0c60a74d7780 | -10.00702 | -44.78225 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a53735dc-0067-38a3-8df4-5ba27c824832 | -7.57179 | -46.30594 | 2025-11-16 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34266c0a-df49-3feb-83c1-1ec95fde289c | -8.07984 | -45.68327 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cbfefb24-271b-3d7e-88dd-e0e7843bec1c | -9.74492 | -43.96325 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 741c6905-5033-3936-ac1c-40756cbf10a0 | -6.93008 | -46.00819 | 2025-11-16 04:08:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 998a82f5-7cba-3741-88dd-c05616e27cb5 | -11.15915 | -49.44638 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a682b44-356b-38fd-a776-64860da0f858 | -11.05052 | -45.16058 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca04a34-ad1b-37fe-bb8e-ebc17fd22c19 | -8.10253 | -46.03472 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ed27fda-43b0-31f9-b1b7-e8412f49a730 | -10.18013 | -44.49826 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c01a851-9601-3907-bb27-31ee2fded775 | -6.28797 | -41.72416 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 620f7f27-b917-324a-8475-1f60ca99a340 | -4.84098 | -47.55407 | 2025-11-16 04:08:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d60b48f9-f120-3c8d-9acf-8ae3209af111 | -7.21535 | -47.98542 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00b0de47-444c-36d8-968c-f60a53aba4a4 | -7.87024 | -44.94154 | 2025-11-16 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6ec9cef-1428-3443-9334-66b418fb3178 | -10.18871 | -44.40235 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b2989b79-a743-303b-a2c8-9aed89387a47 | -6.11664 | -41.5199 | 2025-11-16 04:08:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 15606dc6-0dbf-3044-9b27-24846f862142 | -7.38435 | -45.52021 | 2025-11-16 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 409f0c39-5779-3c77-b213-ff0604a6d463 | -12.65171 | -46.74682 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 97d9ef8b-03f7-3062-b5fa-aacb3aa52bef | -7.05006 | -45.9418 | 2025-11-16 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c2d295c-9983-37ee-bd20-3d0d8354543f | -10.05172 | -46.76188 | 2025-11-16 04:08:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45195e0d-eac2-36c5-8ff2-23c2b3fb7c36 | -9.84883 | -44.16254 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e16b34fd-f4da-3705-9b09-d519554036ee | -7.86233 | -45.98453 | 2025-11-16 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4b36dcc-d9a0-3b22-92aa-2e41b72452b8 | -7.71566 | -42.94027 | 2025-11-16 04:08:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9a50f524-55ca-3334-bcd4-b103dbc9961c | -7.29292 | -43.91113 | 2025-11-16 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2f73ff2-9420-3b2a-84a6-ed051d5a9373 | -11.42662 | -43.13304 | 2025-11-16 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8c6e4142-f47e-368f-bba6-89068210429b | -9.72858 | -43.9719 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 18e1cc11-b95e-3b72-b774-9a0678f54631 | -6.68839 | -39.09822 | 2025-11-16 04:08:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6b81a2c6-59c3-3dde-9d78-2f327a5a5d40 | -9.0614 | -44.7551 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f5626b10-3f7a-3790-8f72-7d35a335e418 | -12.20297 | -49.5523 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36f2fdd9-786f-3923-896b-e1752587b748 | -7.36775 | -43.32222 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd7aa4f2-e41c-3926-918f-760f02a1e8c1 | -8.75037 | -45.64413 | 2025-11-16 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1f3d53e-5462-399b-a57a-84b0fa920c60 | -11.85603 | -44.72192 | 2025-11-16 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7b5d867-5279-38f6-bda1-9a16475a5a62 | -11.16364 | -49.44724 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79a60131-267e-3eac-8db3-f66c0a88f5a8 | -10.76921 | -44.50034 | 2025-11-16 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 149d0b35-ebb3-37e0-ae6d-5c2824fcd356 | -5.69412 | -45.987 | 2025-11-16 04:08:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10065d7d-c30a-3939-a8d0-4c0e7eb26691 | -10.35584 | -47.33517 | 2025-11-16 04:08:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5db5ea4-c35e-33d3-a46e-6bedbdf0f10a | -6.87836 | -41.58048 | 2025-11-16 04:08:00 | NOAA-20 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbf1f5c8-d09c-37d5-b99e-e480af949770 | -7.05174 | -43.94714 | 2025-11-16 04:08:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 71d99452-132a-3dad-81b0-18ca616b9b0d | -6.67192 | -44.47221 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aedaeb3f-0cfe-36ec-aea1-0b6c736c58ee | -12.69133 | -43.42772 | 2025-11-16 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af917e4f-4c04-3fa9-b2c6-add093802992 | -12.68118 | -46.77528 | 2025-11-16 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67befeb1-66d4-3de1-8de8-381717311209 | -6.0748 | -43.00203 | 2025-11-16 04:08:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22aee52c-8a08-31ca-8f7b-040f5054866b | -6.30385 | -41.83942 | 2025-11-16 04:08:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50d87904-f2ca-3e26-ad93-d333ac3173f4 | -10.792 | -48.53309 | 2025-11-16 04:08:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8a5a86e-f51a-36f3-917e-d830ca62c2da | -6.66105 | -44.58353 | 2025-11-16 04:08:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4b17f71-7d14-3506-bb01-1411af9bef77 | -6.69903 | -40.79549 | 2025-11-16 04:08:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 00e2e7e6-d4e4-3f23-9a06-f9be58ff4e60 | -7.09139 | -42.74213 | 2025-11-16 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3b4a2d26-0c31-34e5-bb48-a6b2772a61cd | -6.05918 | -41.56026 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5bc6e5bd-d349-3a42-b91e-d6e341619ba5 | -12.51125 | -44.94285 | 2025-11-16 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c24acb9-a83d-3a5b-aef0-f3ebf938ae39 | -10.66458 | -49.36731 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26254e33-07b3-3ed7-991a-e33bb307cb48 | -9.84906 | -47.61033 | 2025-11-16 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02f7e21a-2998-3ea3-963c-3aa82f90e1a2 | -9.84177 | -44.18424 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9aaebc60-92bb-3e4d-a000-2b03d549465d | -7.22495 | -47.98535 | 2025-11-16 04:08:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21bbd0fc-0097-3911-9343-af482c78996c | -6.16517 | -39.92385 | 2025-11-16 04:08:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 12f4871d-7550-3d06-a8c6-7c2a9fbe3dfd | -9.8436 | -44.17311 | 2025-11-16 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8d41742-8edf-3cbd-97ff-56de49dd8538 | -7.1474 | -41.76867 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 03592590-9735-3be6-b865-b19543c012f7 | -12.05656 | -48.20921 | 2025-11-16 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a63b07c7-2490-3086-8b67-3302a891f085 | -6.00118 | -41.90512 | 2025-11-16 04:08:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 29a5e6cc-02ae-3948-bc23-f86b12926073 | -9.94205 | -45.08837 | 2025-11-16 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa728194-1002-3d85-9acd-9f9429c23853 | -7.36834 | -43.3186 | 2025-11-16 04:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24484d27-d866-38a5-a28d-b5e52f1b8f94 | -7.04742 | -42.24995 | 2025-11-16 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c28a08d4-1795-3f6c-a802-0a8dc2dad6d4 | -9.57886 | -44.60941 | 2025-11-16 04:08:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e634bc06-d04b-37fc-a2ef-24c09eae1f5f | -9.99851 | -44.76875 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 820d3e4d-eca2-3270-b9e1-7d23fc1fef0e | -10.66007 | -49.36648 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ddb2520-9689-3263-81f7-0be6de655c77 | -12.22378 | -49.64095 | 2025-11-16 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0d57c3e-f9de-3641-87dd-df8b75a3ae6e | -9.99915 | -44.76485 | 2025-11-16 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f8359bcd-82fd-3623-9e4e-3e06eb4d2756 | -8.10244 | -46.0326 | 2025-11-16 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cafa70f3-efa0-37e3-ba2c-0a22dd575fd5 | -5.45245 | -47.01289 | 2025-11-16 04:08:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa131cd7-3332-3ea8-8bae-040efdb76a1a | -10.65835 | -49.37579 | 2025-11-16 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe601c59-58e1-3319-a4f5-8d91c371b896 | -6.08721 | -41.53286 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| afaa7641-1c3d-3d34-af8b-a31f93d455b2 | -4.30744 | -50.88304 | 2025-11-16 04:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6efc390e-d246-33fc-a297-75a1e2c68ab6 | -5.73343 | -42.72919 | 2025-11-16 04:08:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4d5a677-29e0-368b-ab4d-ca672a5b6010 | -10.16453 | -44.50723 | 2025-11-16 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9a2c85d5-52b2-39d8-bb3c-8d82119d2ed4 | -9.13256 | -47.71278 | 2025-11-16 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a640ebc2-22f9-3f68-a485-5de993ea05b7 | -5.72133 | -42.91195 | 2025-11-16 04:08:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a836aa54-b844-36fd-81d1-7acdaecacd48 | -6.07364 | -41.66148 | 2025-11-16 04:08:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3631e60f-233e-3346-8904-58caa413a904 | -6.58921 | -43.79675 | 2025-11-16 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c9ad3d50-c95e-3c56-950d-06f883a4875a | -6.12883 | -48.04935 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f1a839b-d6c4-3fba-a4d4-677eeef410d7 | -5.91708 | -42.26258 | 2025-11-16 04:08:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9f3dc5c1-3a16-3a89-80d3-b24a8e57f9c4 | -6.14751 | -48.04748 | 2025-11-16 04:08:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc8c1af2-358f-35cc-a0c1-690a5376437b | -10.29848 | -44.92936 | 2025-11-16 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20c80dd4-cac5-3f68-9da4-81dfeb69bcd6 | -9.73315 | -43.96512 | 2025-11-16 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 73253874-ca02-3cd9-aae2-f953d860b8bd | -11.41609 | -43.32646 | 2025-11-16 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README41.md)
