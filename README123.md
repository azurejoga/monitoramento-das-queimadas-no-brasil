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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 522ad5dc-f615-3780-ad2e-f3999cb2c2f2 | -23.33437 | -47.31424 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbda788c-9170-33c8-a56f-786dc51c3631 | -22.58888 | -51.89412 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 31d0befc-b128-347c-ad96-f129cd84f8e6 | -23.33906 | -47.31482 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d568e7b-2a21-3739-a394-71bc18001a17 | -23.34475 | -47.21346 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2364acc9-6c2b-3c08-80da-b1d04df9bc0e | -22.66548 | -53.12729 | 2025-09-11 04:51:00 | NOAA-20 | SÃO PEDRO DO PARANÁ | PARANÁ | Brasil | 4125902 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bf3c7fc1-ae14-3ae7-94d8-dd76fc8c26f1 | -23.33288 | -47.30649 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5209c365-828d-3154-9009-b7ceb6614f87 | -22.59718 | -51.8866 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| 23dba447-bc89-3719-9316-eacde3f3b8e6 | -24.19968 | -51.76111 | 2025-09-11 04:51:00 | NOAA-20 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 30b5eee2-3ff4-3112-b2d1-a9ff88cdfbf5 | -22.59362 | -51.88607 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 39.9 |
| 5b752b2b-82cc-3bc8-9f56-74aa07162b03 | -23.39078 | -46.85591 | 2025-09-11 04:51:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 05332834-b57c-371b-a2e7-035ad936b7fb | -24.47541 | -50.81224 | 2025-09-11 04:51:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f8203ba-e269-3c23-a0b7-d4cb67e46214 | -23.2562 | -45.97633 | 2025-09-11 04:51:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1b5da933-ab15-3e59-ad5a-59e8f928a531 | -23.32931 | -46.55455 | 2025-09-11 04:51:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2634df78-ec3d-3135-abd4-669b4deb686f | -23.34806 | -47.21188 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 94649914-70bc-35c3-9329-fd074198c35b | -22.59244 | -51.89465 | 2025-09-11 04:51:00 | NOAA-20 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.5 |
| b7fccba6-932b-3661-867f-8f4edf826fd6 | -23.32771 | -46.55346 | 2025-09-11 04:51:00 | NOAA-20 | MAIRIPORÃ | SÃO PAULO | Brasil | 3528502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6c2bcf38-86c7-35fe-ba6f-c5bc4a610c44 | -22.97051 | -49.75068 | 2025-09-11 04:51:00 | NOAA-20 | CHAVANTES | SÃO PAULO | Brasil | 3557204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 0b9a3e88-db4e-3466-8521-a0acf4d253da | -23.34373 | -47.31551 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2bfe1323-9026-37ce-a54d-dcf0532a4eb6 | -23.34946 | -47.21411 | 2025-09-11 04:51:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 51f4f242-f251-3fbd-ae96-a909ab9b768b | -24.19946 | -51.7634 | 2025-09-11 04:51:00 | NOAA-20 | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8efcf646-7208-3c03-ac46-3cf4e9957775 | -23.59695 | -46.97438 | 2025-09-11 04:51:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f3866050-bfb6-3a69-9cb1-7bbfe0386495 | -23.22918 | -46.68961 | 2025-09-11 04:51:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4bdaacea-8432-393d-bfcd-67db38990f39 | -23.67363 | -49.83823 | 2025-09-11 04:51:00 | NOAA-20 | SIQUEIRA CAMPOS | PARANÁ | Brasil | 4126603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 929410ad-25ad-394d-a3ef-6a558b09c7b5 | -11.48234 | -43.63513 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7a32cc63-e1e4-3499-bb1f-359915bb8fee | -11.37901 | -43.51497 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bac1cde7-b13b-3ac8-b547-d08780ace4b3 | -9.06116 | -47.04691 | 2025-09-11 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 38720f55-6471-310c-9d5b-a7a9cbee431c | -11.02246 | -45.06597 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 24ec9d30-0e47-324b-9879-92dd31976ff8 | -14.39673 | -47.31728 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 416cb726-e31e-3c6f-b727-5ac65c06d4ae | -12.46877 | -47.48125 | 2025-09-11 05:29:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| c768b128-b8a9-3057-a948-220520224bb7 | -6.20579 | -43.35921 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4c90afe1-5fde-35c1-a0b3-b4f0447cea62 | -6.31346 | -42.21508 | 2025-09-11 05:29:00 | AQUA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| de3e80a3-9820-3c29-9ebb-f0fad2f3eb91 | -6.34984 | -44.07365 | 2025-09-11 05:29:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1b6e9f2d-a1e2-3804-892f-5df49b895f0a | -12.56274 | -44.64352 | 2025-09-11 05:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2d212a63-62a9-39f6-9d1a-4876be6c49b6 | -12.56463 | -44.63168 | 2025-09-11 05:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 7c667045-0935-3764-b30d-7c9b8c595aa9 | -6.39827 | -43.49499 | 2025-09-11 05:29:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 51f38c0a-8ee9-3098-b24a-4051b4752ccf | -9.29494 | -46.75534 | 2025-09-11 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 52f519f4-13e2-3475-abca-f8d06e80c3e6 | -6.1633 | -43.36469 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1c9edf08-7ded-31d9-8f58-65bd1f34566a | -8.16563 | -46.08099 | 2025-09-11 05:29:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0dc37805-804a-31d1-b9a4-3900544f487d | -12.13735 | -44.85924 | 2025-09-11 05:29:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a94bb397-56b0-3807-b59b-74d8a3305cc8 | -13.85966 | -47.35822 | 2025-09-11 05:29:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| be8cd61a-09df-38bb-b246-3fde01d84f49 | -6.37284 | -45.16107 | 2025-09-11 05:29:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 075a8b2c-6eac-30de-b9b2-4aafd6455cbf | -8.72453 | -47.09383 | 2025-09-11 05:29:00 | AQUA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 5132afbc-e622-31f9-bb52-b7de259b63cd | -6.07637 | -43.1284 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 668c3be9-9f0a-3ced-b53d-9564c975d5ee | -10.17805 | -46.18395 | 2025-09-11 05:29:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c23d8d11-4644-3f33-aa91-7fcaaf887ba8 | -11.71433 | -50.59978 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 8af33e63-5b9e-3c2a-beac-d5783bbcce8e | -11.34434 | -46.50696 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| a2b19a0c-e62a-3ae3-9d8a-50b6e89f9a03 | -6.33918 | -44.0718 | 2025-09-11 05:29:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 196449ac-6391-3d0a-87b8-94c21a88da7b | -11.98544 | -47.59734 | 2025-09-11 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| f9cd408f-4f50-3468-b948-8d47460a84cd | -7.5363 | -44.67491 | 2025-09-11 05:29:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3b44f1bd-2ac8-36da-83e9-35634b6f78fe | -9.00939 | -49.75354 | 2025-09-11 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 9bbfa928-ad22-3b44-8903-255bca926599 | -11.34737 | -46.48935 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| ba3b75f1-2cb1-378d-9569-7deac5b65b31 | -11.47107 | -43.64425 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ad7fdb57-abe7-3bc8-bfe4-06f3e36e1a43 | -6.37012 | -45.17749 | 2025-09-11 05:29:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 57c0477e-2be9-3ce8-abcb-1bf15a4a889b | -11.16273 | -45.30468 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2afb2048-52cf-37c7-9ec1-111d5bf04ae4 | -6.33708 | -44.08516 | 2025-09-11 05:29:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 6ba1c4d3-b161-3c7b-889f-e98be6f6951b | -11.41203 | -43.55265 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 25178a3e-f05c-3735-a44c-1405827ac5ea | -9.04894 | -46.95682 | 2025-09-11 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 5d368bde-0fb5-3277-91dc-51a1cfdaa3b6 | -15.2181 | -44.04809 | 2025-09-11 05:29:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4aff0349-50bb-3e25-8be3-b4fb2a7a1a97 | -11.48404 | -43.62444 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 57fff50f-ca82-3253-af51-11a2c14ba750 | -13.15777 | -45.27577 | 2025-09-11 05:29:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f481f47d-3b48-379d-b620-9de338e23f28 | -10.3069 | -48.80214 | 2025-09-11 05:29:00 | AQUA_M-M | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 2f85cafd-31d3-32d0-a78a-77bb66689f11 | -6.21414 | -43.49057 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c81e1788-7ef7-39ab-a72f-db46f6091c4a | -6.21292 | -43.36698 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 59eab37d-76d2-36e1-8185-e6014aba918c | -5.78781 | -42.67741 | 2025-09-11 05:29:00 | AQUA_M-M | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f2414dbb-7fda-33d6-a3a5-10ad23be7698 | -12.56437 | -44.6373 | 2025-09-11 05:29:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 3b9f0a46-6db2-3121-822d-5221edc6aa23 | -15.25094 | -44.02203 | 2025-09-11 05:29:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a294bf13-9b33-3720-924f-fb1ded197591 | -6.37594 | -45.15604 | 2025-09-11 05:29:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2892d4ae-b091-3f49-9e0f-69f495e5a882 | -11.47279 | -43.6335 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8a492535-558a-318e-8d73-1749d6b64278 | -15.32775 | -43.00335 | 2025-09-11 05:29:00 | AQUA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 2779c32a-50f0-39bf-8483-032ff923f4cf | -11.33545 | -46.48813 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 1c42690e-c209-353e-89c0-0c6926dc41b9 | -6.19699 | -42.48891 | 2025-09-11 05:29:00 | AQUA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 1e213fcd-ce55-39d1-b1b0-b809f1476638 | -11.36528 | -46.52658 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 71f66477-623f-37f0-be0c-d8512246c7f7 | -6.20389 | -43.48899 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 3b129c35-ba0c-3cd0-b4cd-6f7d7d4c6996 | -6.20762 | -43.34735 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 25d8f299-826a-38b1-890b-ddce05b5d22e | -11.33713 | -46.50023 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 0a45dfc1-cd42-33b5-9f1b-7a566e2e775f | -11.45883 | -43.59839 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 1ed8043f-6837-3f41-bf79-da96c281f47e | -11.70782 | -50.63432 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 756cb95f-9117-3481-9b00-080d2cc7de14 | -6.31078 | -43.80664 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c93a8a3b-8c21-3cdf-b346-b945133c4fb4 | -8.87211 | -49.58033 | 2025-09-11 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 7814d45d-49e7-37fe-b597-2a95e57b3890 | -9.07481 | -46.96625 | 2025-09-11 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d654cac8-fa4f-3d9a-91c8-3a2b004296b9 | -11.01954 | -45.04615 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| b6e99622-93e3-3df7-a669-1fa88a9cc3ed | -6.85441 | -47.85371 | 2025-09-11 05:29:00 | AQUA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4beb4e76-0d08-3929-9dae-0f15a4860b72 | -15.24932 | -44.03226 | 2025-09-11 05:29:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d84c32c3-2e57-3c99-b23e-b08fd7193dfe | -13.15564 | -45.28862 | 2025-09-11 05:29:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7f9f4a52-545c-32f7-a0ed-a83e38b465f9 | -9.80896 | -46.81767 | 2025-09-11 05:29:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 781fe7c1-1ffe-3afe-bc9d-e1482f14b5a8 | -5.57517 | -42.91922 | 2025-09-11 05:29:00 | AQUA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 16611d5f-8f55-3744-a5bb-85ed8e62479d | -6.31566 | -43.43801 | 2025-09-11 05:29:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 27789ed2-9ab4-3b34-ad1d-2223f9ad67a6 | -8.86987 | -49.554 | 2025-09-11 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 9b0320dc-a1e6-3a4e-9f97-e04cc71747f6 | -11.34285 | -46.46549 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| f8f31c9b-afe7-3ad7-89d6-5bb8dcfce7e7 | -11.72151 | -50.59641 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| ccf9d24c-44fe-3849-b6cf-e74e3d72a8f9 | -8.64776 | -45.72161 | 2025-09-11 05:29:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 9c050d48-e525-3e2b-a5d6-094827ba3fa0 | -8.19937 | -50.09695 | 2025-09-11 05:29:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 993a6878-f3d0-34ef-9631-dfbad3ca404a | -6.17532 | -41.07553 | 2025-09-11 05:29:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 4245335e-91ef-36a4-96f7-0fe3c911799a | -13.5791 | -47.69331 | 2025-09-11 05:29:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| fd579f30-41cc-39f7-a4a1-73b6b2f76db4 | -6.24674 | -43.48357 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cf739343-ace7-305b-80c6-b82602d27c59 | -11.71525 | -50.631 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| b4c5a6ea-9278-3838-a4c1-fa918a98fab8 | -6.17344 | -43.36647 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 31ee2778-c628-3bc0-b3d3-ec087e5a737c | -12.12711 | -44.85743 | 2025-09-11 05:29:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| bd3267d2-28bb-349a-8a41-982d20f6b569 | -11.33843 | -46.47093 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 15563d0f-e9b3-39c7-a116-dfe3afa1113d | -14.40849 | -47.31987 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |


[Clique aqui para ver as próximas entradas](README124.md)
