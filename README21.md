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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7330552-5270-3520-a00c-34b3b59fe074 | -5.91295 | -45.83206 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66837fe8-c2a5-3e0d-9bcf-c97de392bc2d | -5.42186 | -45.88304 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19610ec2-1e44-34e4-ae03-2b526b42e180 | -5.91902 | -45.81687 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b40c95b2-2a40-348b-b156-17a4d1cf7efc | -7.88945 | -46.26861 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adae37f1-fa53-310a-9a88-3b6cb9a5d735 | -6.79452 | -44.64783 | 2025-09-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aa97fee9-cdec-3e9f-8db3-d980360e8278 | -6.7935 | -43.44774 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 28a9e553-7de3-3927-93ea-56b7c3037c28 | -2.74691 | -48.69669 | 2025-09-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ae8c6e4-dc1f-3b79-8314-2da099055cae | -6.24222 | -43.72843 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd413b2e-791f-3bea-af36-712b607f7402 | -5.66633 | -51.6367 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 567a5c85-137c-37c9-97fc-00bf9134319d | -7.78262 | -46.05018 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7b824943-ad63-3626-96c1-9e90226d2afd | -3.81507 | -51.28889 | 2025-09-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2abb913c-d9ba-38f5-8c62-ee18bcba35dd | -6.1867 | -45.79723 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e669c71-ef03-3775-8c0f-af64beaffabf | -3.96756 | -43.23993 | 2025-09-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7787a6e-e82f-33e4-a27d-f844fd368640 | -9.02086 | -49.78653 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31530aa6-897e-3371-9836-e8a3d189b507 | -5.42185 | -43.44904 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 66f1a15f-9d15-3703-b045-06a4177a1bcd | -6.13477 | -44.15034 | 2025-09-10 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daa96975-143c-3f3c-96ab-f87da898bda8 | -6.20891 | -45.61318 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1268cee3-a6d3-374d-9b4f-f6b1b4a884ac | -6.27642 | -44.48097 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6695323c-b573-3921-9170-4e54a791507c | -5.33287 | -44.14255 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b283d5f-e602-32ef-ab40-fccb43b579dc | -6.86907 | -47.89108 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bd6a89f-1c86-3fd2-aec7-0b248910bee4 | -6.1858 | -45.03037 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 151d2324-854e-3e43-922a-25683890607b | -6.03745 | -43.66729 | 2025-09-10 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a2167b-228a-386d-a177-fde40463b150 | -5.48795 | -42.65499 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c65eb9b-3151-3096-9dae-2b1766602434 | -8.49324 | -44.64348 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8111df5e-a850-3d7d-8f17-9223a11d0b63 | -7.39492 | -50.89465 | 2025-09-10 04:14:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9effa5ad-1c1e-3a59-adb6-d7a0b9739f14 | -5.72864 | -51.68886 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e83dba1-ef40-3176-baa0-4652cfbcae03 | -6.89012 | -47.8847 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3830b0e8-cd4d-3a9d-a12b-e327ac43e4c5 | -9.21116 | -50.55088 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 435720c3-d74c-34e1-a203-fe7b9f5f177f | -5.41415 | -43.45493 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 96bc5010-5ddd-3b46-a226-5c16133b9e91 | -9.89499 | -46.47738 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0637ea50-97d0-3388-94e6-79eff405f79f | -6.2033 | -43.30434 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a9d3e5b-6b91-3587-bfba-c5ccb7e0f88a | -8.27473 | -47.43507 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d52d916b-3cda-3dac-996c-1696520a7ac3 | -8.38267 | -45.01954 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36d9651e-39be-3208-93d0-168d93b099d5 | -7.54248 | -48.24724 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3650c924-f765-38d0-9975-836af3a07e1a | -7.81533 | -47.50964 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e8ab82d-dca7-3494-8ade-0177a7be6e03 | -5.99534 | -43.32817 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fb2ff449-6d53-384d-adfb-e7723f5bfc20 | -9.21329 | -50.54853 | 2025-09-10 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d83e3d7-73f8-3966-8099-6d16b923f347 | -6.85393 | -47.90968 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68dfe724-c136-396e-b0a2-eb05beb84b05 | -9.6126 | -48.03886 | 2025-09-10 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2a4d392-36d0-3335-a49d-8bb8766a6483 | -5.37525 | -38.79967 | 2025-09-10 04:14:00 | NOAA-21 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb6eb6af-2fb9-3009-95d8-79ce33977236 | -6.19304 | -41.04879 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70a09d5c-8012-3982-b00a-cbfcf5ff9b3d | -6.53309 | -42.43097 | 2025-09-10 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 751431b0-8f10-32e9-b334-0dcf8b0317ea | -9.08469 | -47.05753 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a92f8365-1ab5-36b4-90b3-df862121dbd0 | -5.71978 | -45.41524 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cc90cd1-4874-30d2-b025-d1e303d9a36a | -6.29947 | -44.22717 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b07e411a-4bf5-3a95-9368-4ec29edae68f | -5.55548 | -43.05363 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afed5490-2bd6-36e4-87e7-a0d7d3c61411 | -9.69509 | -46.8154 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1202b7af-ce98-34f7-a03b-57bb25a93466 | -6.31352 | -43.57655 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12cbae13-e5ce-31ee-ba12-289ddf35d77e | -5.58468 | -45.03477 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| f6ae8edd-e526-3171-a6a9-6bb5ce7a404e | -3.68746 | -49.57447 | 2025-09-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7cf9511-8952-3c12-a943-846cb0488b01 | -5.74619 | -47.47005 | 2025-09-10 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3a13bd17-900d-33bd-b9e5-30ba2da9b718 | -5.66536 | -43.91115 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb391003-9866-3261-bc53-71e1c61c4d14 | -6.35564 | -42.60999 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bcb4fea5-988b-3204-86c2-7189e04ce278 | -9.80233 | -47.79448 | 2025-09-10 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2292d3a-b404-3ceb-a84e-54cd49507447 | -6.85753 | -47.93595 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fb5f8e60-f0f3-347d-af49-6e2a0c5714f2 | -7.48522 | -48.23006 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ed07300-69bd-35a0-b664-aa46057274f3 | -5.91388 | -45.75953 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5db48511-752e-3b5b-a4c6-dd22f2c54260 | -9.43683 | -46.7083 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2dc04cd-d6d9-3012-94da-6794c1b5952d | -9.31594 | -46.71421 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 27d899b7-0953-3cb2-9bdc-307483e66d80 | -4.87167 | -42.76952 | 2025-09-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9ade6be6-11e9-331d-94b2-210d8d747428 | -6.21464 | -45.62201 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c58c8a12-a7e4-3ec3-9434-c457afff55b2 | -6.64312 | -44.07729 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 486d2a89-b2cd-3e72-9cd8-c09eda4d1fc2 | -6.25866 | -43.40889 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4eaece0f-82a3-3a8c-8f8e-feffb8e6c7a6 | -4.7354 | -43.35457 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebc8d7b3-e19a-3fee-aeb1-ef1162bdcdf1 | -7.07886 | -43.88285 | 2025-09-10 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b380430-31a8-3605-b151-f8cc11da2eb2 | -6.20384 | -43.30089 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e131ca21-cbd2-321d-b6d4-4d174c7835b6 | -8.0454 | -48.68138 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 444f75e5-20a4-33ed-8030-e32bc5e9a4bf | -6.41177 | -44.44407 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee84de69-f58d-3f35-8758-7211cafea665 | -2.91328 | -48.67067 | 2025-09-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f976db-8026-373f-9edb-31ce4321c972 | -9.07002 | -46.96831 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c79206da-e163-3121-afa5-2b607d500c67 | -5.53921 | -42.65584 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| a57d2507-9bd8-34c2-a033-5785544b94db | -5.67421 | -43.89821 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ede72a6b-08a3-358c-8c4a-b827fb289f34 | -6.84974 | -47.93456 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 669e566d-1f3f-3458-b251-b2c5643573ff | -7.31136 | -44.15532 | 2025-09-10 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b081129-fd9a-38f7-bdef-69a63f502a8f | -7.19113 | -44.01151 | 2025-09-10 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cc259cf-00a6-3ad9-894d-4567322fb3c6 | -5.6637 | -43.90015 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94b424d0-8536-3b85-a890-15a35c6b6c89 | -6.26521 | -43.38873 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28097769-ee6f-30db-84f2-b94e6e38921a | -2.38318 | -47.71713 | 2025-09-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39250ba1-981a-3100-904c-afb2c28f5ffe | -5.6681 | -43.35389 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0273174a-c98e-3ff2-8b35-89c7cf7a28c3 | -8.52098 | -45.71733 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c9814ac-b658-339d-b8cf-b19fd7740703 | -5.20071 | -45.43333 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00c31cc1-a256-3fea-921a-69fdeece422b | -6.8565 | -47.89446 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f4fc8457-ced0-3712-86da-6b8ca4a442c1 | -6.62154 | -43.99881 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b67de758-8b65-3005-876f-7b0d27bd52e6 | -5.94131 | -45.72341 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ee6a609-f047-37f3-8c6b-c4777ffd2a87 | -7.74409 | -50.72734 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f814e0ce-c91b-32d4-9129-075e34129e3a | -6.39951 | -42.61377 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6d645452-1752-3117-8cf6-345b8aa9330d | -6.87678 | -47.89276 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| adaee64f-8591-3e97-aace-0e49d455ca00 | -6.2625 | -43.40596 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7cf205c7-0636-3ac8-9f45-dfc541a5e347 | -5.93855 | -42.77874 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e2909de7-6667-3bca-8cce-f15507c5c91f | -6.34997 | -44.85745 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 760c38ff-38da-3c54-b224-c46a5e096bc9 | -5.78292 | -44.84695 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48106184-e9a2-3f68-bdb6-0facd587725c | -9.89151 | -46.47688 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca24f439-c7eb-3077-805b-f5705361ebe4 | -5.74209 | -45.25961 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b68558da-f49f-352d-acd9-a23bc0c6225c | -8.07025 | -48.65664 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aac3c630-f8c3-37ba-af59-e564ce5d1242 | -5.39595 | -43.44148 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32143780-c3bb-3151-b09d-af1af2d1988e | -8.72328 | -45.24774 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d85974a1-d46c-3f8b-9b1c-8a0d5fd6e8e5 | -9.13544 | -46.19667 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 744a300a-0557-3fb8-b675-c8a2877407f9 | -6.39057 | -44.44809 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfd93922-6972-37bf-b1a5-9e31f7d19ba2 | -5.7417 | -45.36773 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f7f1bb8-8f3e-3a18-80f2-19100089796a | -8.00273 | -46.3306 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README22.md)
