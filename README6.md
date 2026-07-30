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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b8338a8-77ed-3f41-a434-a34abc3a93c4 | -3.03918 | -40.12004 | 2026-07-30 04:12:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5cc6076b-88fe-3231-b1a7-d6116a83cb94 | -5.8278 | -44.13971 | 2026-07-30 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 015edcdb-a6dd-30ee-9119-9ee24515cf60 | -4.93624 | -41.98248 | 2026-07-30 04:12:00 | NOAA-20 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1fa9d42-0cd6-3cc6-87df-4d83a0ee93a1 | -3.67925 | -47.64587 | 2026-07-30 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 364d4d95-ea22-3cb5-bf08-607e4c62dec9 | -8.90434 | -37.96933 | 2026-07-30 04:12:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d0f9345-9670-3e7f-9039-0d398dab131b | -3.50115 | -42.33132 | 2026-07-30 04:12:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c14e0ee9-7eb2-36c7-9cb6-aa1f71eb1086 | -7.35798 | -47.03521 | 2026-07-30 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f282229f-c467-3af4-a043-99e43f80b54b | -2.60811 | -47.35669 | 2026-07-30 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4b270f7-8c55-39ee-b5f1-38e3e905ff4f | -4.90391 | -43.47129 | 2026-07-30 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 240ccb41-3c58-3ee1-8c1a-55ac8e63a02f | -3.11322 | -47.90733 | 2026-07-30 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e8d18e8-e1c0-3522-abee-68c49799210b | -3.96138 | -43.11753 | 2026-07-30 04:12:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2872fe43-124e-3e4e-8359-bc410e3ac82c | -7.34173 | -45.8518 | 2026-07-30 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 544afe3d-53e5-3e3a-8627-166c2755e03f | -4.44812 | -37.92905 | 2026-07-30 04:12:00 | NOAA-20 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0bbd02a-9175-3414-9a0e-7afd3e01811b | -5.50428 | -35.58459 | 2026-07-30 04:12:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 844759c2-abff-3259-b98f-6f28d0b7e9ab | -5.82079 | -44.13855 | 2026-07-30 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fdf65520-f5ed-3772-8af7-62d38e07f5ee | -6.33869 | -44.60558 | 2026-07-30 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70d5c958-2aac-30b8-b3b7-8e061e174703 | -6.86445 | -46.01033 | 2026-07-30 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7bbfd5c4-c256-3b0d-9535-26260266ec39 | -4.36838 | -47.76645 | 2026-07-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fddcaa31-6736-3b9c-9d2b-0ab8a0d13ce9 | -4.03188 | -43.27079 | 2026-07-30 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eaf9d439-98df-342b-971c-26dd4ba9e44e | -3.67477 | -49.48106 | 2026-07-30 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aad05d9a-fe29-3cf3-9325-05927b6e560b | -6.86064 | -46.00963 | 2026-07-30 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 343a456e-187d-3240-8d82-38c8687f5ee7 | -5.74898 | -51.70832 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5aa6d782-6170-371d-a6ff-a7f8a5a94587 | -5.14046 | -37.65009 | 2026-07-30 04:12:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 96b018fa-34c8-32dd-a78c-945d537f8e81 | -2.48573 | -47.08993 | 2026-07-30 04:12:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65eb518a-b056-3f03-981a-6b51d0671905 | -2.64442 | -47.98263 | 2026-07-30 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71cb972c-f081-39c7-aa98-4349f75c59ae | -6.30546 | -43.65644 | 2026-07-30 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd96b8e4-a257-3ced-9c80-c96cfc34c439 | -6.84374 | -42.89053 | 2026-07-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8bb9d9fe-50c2-3027-a5de-969c72dcb7cc | -5.17131 | -35.67516 | 2026-07-30 04:12:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 157f0a07-b2a2-327e-9b74-3c87b89184e0 | -5.75042 | -51.70042 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 697185e9-978f-3055-80e9-8526cda59802 | -5.47714 | -45.11705 | 2026-07-30 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddf0e5b8-457a-3d48-9664-7ffa5996aef7 | -3.16922 | -48.1361 | 2026-07-30 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e02c3afa-240e-3ac5-a6c4-b966de75ead5 | -3.16457 | -48.13524 | 2026-07-30 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f25e8ac7-8f6e-3f1b-8854-240665b7021e | -3.9671 | -40.05301 | 2026-07-30 04:12:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f06c61bc-8a28-3b5e-9a18-61151224da3e | -7.20045 | -44.878 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a1955fee-ceee-335b-86c3-a1b586c24079 | -4.90735 | -43.47183 | 2026-07-30 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 627dade3-fa32-3ce7-b237-f11dc31deaf4 | -5.47541 | -45.11419 | 2026-07-30 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7f48596-c9f0-3616-9fd5-69e22fbcec24 | -6.97432 | -42.88233 | 2026-07-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 33f41d25-ae8c-3e9f-b764-9c1b7ff5c7ed | -3.67526 | -49.47808 | 2026-07-30 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5380b2e-e526-3cee-9d8b-3364d7a04cf4 | -6.95277 | -43.45358 | 2026-07-30 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41c5639a-0693-3ec9-aeea-2df84c28563d | -5.7497 | -51.70435 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2be99f5b-6b4b-374e-9ef4-330b7175129a | -3.99667 | -43.29218 | 2026-07-30 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09485dd7-4c3e-32ea-966a-416d0c6a011d | -6.33801 | -44.60971 | 2026-07-30 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e043ae1-c47b-3765-a7a5-5a1c710aa73a | -7.50558 | -46.09968 | 2026-07-30 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b04f21f-7d46-3203-bbe7-ffd573e3bb96 | -6.95218 | -43.45721 | 2026-07-30 04:12:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 615876f0-84f0-371f-b362-e3b66f9b2e91 | -5.04633 | -43.26438 | 2026-07-30 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7941888-c8cb-3cb4-b189-0bfa7b3bf4a9 | -2.90394 | -40.39698 | 2026-07-30 04:12:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 681c80e4-55d6-3a46-8d6e-ac1e15655ed1 | -4.46438 | -38.30697 | 2026-07-30 04:12:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ffe44a89-0943-313a-b2be-f345f8d6270f | -5.74621 | -51.71178 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 70b5420e-3b59-3945-9db6-51cd40192ef8 | -2.48643 | -47.08569 | 2026-07-30 04:12:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaa58bb5-0c26-3939-a0d5-4491dc02372c | -4.38713 | -47.75369 | 2026-07-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8008345-bbaa-364f-8053-7cece79a152b | -4.02844 | -43.27025 | 2026-07-30 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c90f0ee2-4959-367d-97e1-9d91d813e605 | -2.6428 | -47.99242 | 2026-07-30 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3371840c-1eb9-386a-b7c1-5f98c7907475 | -5.77021 | -45.78231 | 2026-07-30 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d339e499-9572-3ffc-bf89-fc8d1c235c98 | -2.9078 | -40.39405 | 2026-07-30 04:12:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d5b7319b-ea03-3e0a-b564-490259f33ed7 | -3.54367 | -43.20667 | 2026-07-30 04:12:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6651fbcd-6634-339f-92f6-64a8e743205e | -3.18323 | -48.02348 | 2026-07-30 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df89878f-c3f4-3c32-80db-ab1f9045fb08 | -6.8404 | -42.89 | 2026-07-30 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71547294-6986-32b9-b882-cca5b7e66013 | -4.38841 | -47.75597 | 2026-07-30 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0b31ad69-dd0e-3bc7-a54f-ea1175588593 | -5.7469 | -51.70781 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2db4121f-fb92-30d1-a883-d44c5de1b642 | -5.74759 | -51.70386 | 2026-07-30 04:12:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd792c31-7050-364b-bbfe-18681738d888 | -7.24161 | -46.05709 | 2026-07-30 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5eae09c1-07a1-3dd3-a333-426209fb129e | -6.46316 | -45.78856 | 2026-07-30 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e38fb9b-5621-3299-927f-6d84af2161e5 | -3.67339 | -49.47857 | 2026-07-30 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d179143b-fe55-3817-ad7e-9c4ccb9c4510 | -3.17442 | -49.51933 | 2026-07-30 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f19e76be-dadd-340e-8987-8ca904de364c | -7.54674 | -46.90448 | 2026-07-30 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4b9d8b9-fcab-3438-b4c2-9f4b5c20f97e | -5.1386 | -37.65181 | 2026-07-30 04:12:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d0951bb6-bf97-3602-a7f4-29f3888550d3 | -3.1778 | -48.02752 | 2026-07-30 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6123a6f5-34c3-3579-b627-7a2ab5765ed4 | -3.68 | -47.64138 | 2026-07-30 04:12:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e193090f-1acc-3cbb-ab8b-3d563187a915 | -5.04573 | -43.26808 | 2026-07-30 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f22e1a68-7eb8-3820-8ab4-ea6f93f3f5d6 | -6.86523 | -46.00571 | 2026-07-30 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 133e26b4-d9ee-3b3f-90b5-fece2906c62b | -5.90233 | -35.72483 | 2026-07-30 04:12:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| cef41c3f-539f-3d05-8fda-c3871ec145e4 | -6.30888 | -43.65701 | 2026-07-30 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a59e913d-0d3e-3532-b795-6dc8e7253697 | -3.23661 | -47.92998 | 2026-07-30 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 244efac9-8f6e-3f21-aa5e-a51b38e436ca | -7.34548 | -45.85247 | 2026-07-30 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5bf3736-013c-3a70-9ced-7cccd325642c | -5.47343 | -45.11647 | 2026-07-30 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97a5f665-53ae-3ef1-bbf0-700974595ed2 | -5.28969 | -45.21239 | 2026-07-30 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcfbf3c8-b515-3b1c-b86d-fde8a7af3ecd | -3.63959 | -49.7063 | 2026-07-30 04:12:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bb67dfd-64b0-32b2-8497-c43405b928e5 | -3.03863 | -40.12351 | 2026-07-30 04:12:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 862adae7-fc85-325f-83c1-814396b03cff | -7.63056 | -44.81907 | 2026-07-30 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 36c2eafa-096f-3fa4-9504-e203d0a5a4db | -7.63121 | -44.81512 | 2026-07-30 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7887bceb-b566-3b10-9f8d-6a9e0e144596 | -10.89514 | -45.20454 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ca874d-8559-3f8f-9365-7dabace8d47d | -12.61818 | -44.62405 | 2026-07-30 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a16ddcc-b00b-3af7-a067-2f4e030af06b | -12.62493 | -44.62519 | 2026-07-30 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9b3878b-2b6a-334a-8e3e-cebc50c8ad12 | -11.38938 | -50.1213 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 673b71ad-993e-3e33-9c20-5dd5f36ca29b | -15.37353 | -42.65015 | 2026-07-30 04:14:00 | NOAA-20 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ba058ca2-554f-3cca-8e0a-7ff551ceebea | -14.28437 | -47.42258 | 2026-07-30 04:14:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccb1f6be-493c-300d-97a7-151ff75d64c2 | -12.42948 | -50.55113 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84c62777-9689-35bd-b09c-46bdd478cd4c | -13.7475 | -51.8937 | 2026-07-30 04:14:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62b11bd5-5211-30a9-8eb1-d2d0d03d7c1f | -14.18641 | -44.00504 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4080b4a5-3c0a-31bb-8437-1af7024c4646 | -11.62799 | -38.06197 | 2026-07-30 04:14:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 46f1d254-d48a-3cf7-b9a9-a382671743fa | -12.28345 | -50.34787 | 2026-07-30 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c94e5482-33f1-3704-ac13-323ec5af2ebd | -11.82767 | -38.26162 | 2026-07-30 04:14:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 96b42808-0d11-3899-99d7-e48b4fe63dda | -9.60959 | -47.76445 | 2026-07-30 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fec307ba-89ee-316b-9119-f8b47d9e1af5 | -15.14725 | -43.79662 | 2026-07-30 04:14:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ff7f9e4-67ed-3252-bd05-7bc6016cd7d0 | -14.18869 | -43.99079 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0347366-811b-3653-879b-b91972592fb0 | -12.62155 | -44.62463 | 2026-07-30 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67c28ff4-c253-3096-9b1c-e113e1a7fc45 | -14.19418 | -43.99903 | 2026-07-30 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6e90f32-58b2-3423-a5b5-6a7e30a5e364 | -11.0871 | -47.80321 | 2026-07-30 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac086862-4771-3e0c-afe1-d98ca4201b88 | -8.80336 | -49.15768 | 2026-07-30 04:14:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 339489f8-65ff-33c9-954f-5d9ccca8371b | -10.9564 | -49.80681 | 2026-07-30 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README7.md)
