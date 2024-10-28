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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f9337ee-667c-342d-a3a5-c05c746e4508 | -2.52063 | -47.44929 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d0f29ef8-3541-3dcc-a845-9b29f7a4687c | -2.51984 | -47.44931 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aec43021-794d-3368-813b-1a25ff4fddda | -2.37174 | -47.66962 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df338c95-39ae-31fb-9ef1-776cb3803514 | -2.37061 | -47.67646 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10f2ed4e-e54a-352c-948f-2876af62a826 | -2.36886 | -47.6675 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f9bfb05-3806-3c55-883a-03e62089652d | -2.36768 | -47.67433 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 20927a41-2753-321e-9d9b-42c3f1cb3fb8 | -2.3647 | -47.66846 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2173c379-6274-3d55-b1d7-96b9ff41849c | -2.36356 | -47.67532 | 2024-10-28 03:40:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 04015ac6-ed4e-3a3d-b846-ca481085331c | -4.48722 | -48.11639 | 2024-10-28 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a9c8230-f299-3c0c-9633-7ea36b161b62 | -4.48603 | -48.12311 | 2024-10-28 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fc42bf0-943a-393e-ba5f-a215cbd4d1b4 | -4.4852 | -48.11623 | 2024-10-28 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e35ef479-4c41-3d24-a802-9ae357d59401 | -4.48397 | -48.12296 | 2024-10-28 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bb36da3d-e4cb-3463-b94e-75cdcfc4a3cd | -4.24586 | -48.55085 | 2024-10-28 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b10c99-1a56-3e43-be0d-306281c2ccf6 | -4.24458 | -48.55796 | 2024-10-28 03:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4d54b3e-f5c7-3fb8-8a8d-7d2356d8ff7d | -3.93442 | -48.35058 | 2024-10-28 03:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fa68af11-e0ae-3ef5-8027-4482951c3c38 | -8.75952 | -44.71162 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7c633a1-518f-3a83-94af-96389d8a966a | -6.99626 | -41.32638 | 2024-10-28 03:42:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e327fcc8-2fa8-3a1d-96cb-868792e6cea1 | -7.47571 | -34.84405 | 2024-10-28 03:42:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 69542089-b33e-3169-ad9f-442cd60eb3f1 | -8.00185 | -35.13082 | 2024-10-28 03:42:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2b21ec26-5071-388a-8613-f1adb7c0ac10 | -8.0013 | -35.1343 | 2024-10-28 03:42:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6015048f-4edb-3215-ae53-dae967b65baa | -9.7557 | -36.40936 | 2024-10-28 03:42:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b2668f80-6df8-31d6-aaa0-98bf961d1d26 | -11.38946 | -37.67487 | 2024-10-28 03:42:00 | NPP-375D | UMBAÚBA | SERGIPE | Brasil | 2807600 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 34d976a3-cdea-3009-b289-1c7399423ebc | -7.56645 | -38.75969 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cd150940-0431-3f5a-95e1-41b2053eb664 | -7.56349 | -38.7548 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a515020f-9de2-3b88-95b2-95c1d459d2cf | -7.56277 | -38.75912 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7d0c3e7f-5436-39fe-8dc4-f665c330b1da | -7.55614 | -38.75369 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 233bca1b-2015-38ed-be1b-627e5237bfd4 | -7.55542 | -38.75804 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bb1a3e24-fec8-35a5-b268-3c48f125b0be | -7.55247 | -38.75311 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ada8e61f-f1f1-365f-b8cb-bed68956c0a8 | -8.7589 | -44.71495 | 2024-10-28 03:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88a10a18-9d0d-3fd5-b02e-07be2aad77e2 | -7.55981 | -38.75424 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f94ea6b7-bed1-31db-8dae-310827778a68 | -7.55909 | -38.75858 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2539561a-5384-3cf4-afc6-a05ec7236af7 | -7.56573 | -38.76404 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea326ac9-8a61-356b-a6ee-1b442135a224 | -7.55175 | -38.75744 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| de615410-d79c-3775-ad96-6ade5e3a5666 | -7.5488 | -38.75248 | 2024-10-28 03:42:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74426e7c-5a23-3e09-8fe7-10cc57897f1c | -7.24412 | -38.97813 | 2024-10-28 03:42:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ba31464a-e146-3b98-b268-aef905f684c4 | -6.89604 | -38.56696 | 2024-10-28 03:42:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b894af72-f768-3a4f-90e8-6697dc589e63 | -6.89755 | -38.56401 | 2024-10-28 03:42:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b0099a6-0710-3575-b52e-6776a1d89cfc | -7.45341 | -39.72749 | 2024-10-28 03:42:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2e5e3562-39b7-3bfb-bdda-393f5dc2acfe | -7.21661 | -40.08826 | 2024-10-28 03:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7a311ac8-8fcf-32bf-9240-6aa3c199463e | -7.45453 | -39.72481 | 2024-10-28 03:42:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 25369afe-3653-3486-b9c3-19a5a9dfba7b | -7.21572 | -40.09348 | 2024-10-28 03:42:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 67d82df8-9b11-3354-8b83-4512d2d81494 | -7.81472 | -39.77428 | 2024-10-28 03:42:00 | NPP-375D | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 02d68c50-e2fc-33fd-b2d6-0f739f25b1a8 | -8.07403 | -39.9252 | 2024-10-28 03:42:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5a337203-a466-3fba-ae93-69d364268521 | -8.91303 | -40.7067 | 2024-10-28 03:42:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 828fafbb-d8d3-3ad6-9be9-990d6f395c8d | -8.07411 | -39.92307 | 2024-10-28 03:42:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 306e9a85-e582-382b-9c5b-d997840d170f | -8.0733 | -39.928 | 2024-10-28 03:42:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 8bef5212-d832-333d-9304-9850c35bbeff | -9.48416 | -40.53948 | 2024-10-28 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f06fb6f-fec0-352d-85b9-2cdd9d83ccca | -6.28791 | -41.92081 | 2024-10-28 03:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e3f89031-e599-3d7d-90ba-20009acc4138 | -6.23338 | -41.25912 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0faa8afa-e130-3dd7-9674-1413af43df1b | -6.23194 | -41.26748 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d27f3ae5-a76d-385e-921e-629f17d7819c | -6.157 | -41.8616 | 2024-10-28 03:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4ebe5457-34ca-3624-942f-226511821e6a | -6.29862 | -41.91309 | 2024-10-28 03:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d155aa23-e5c0-332f-8d4e-35c03a963281 | -6.23197 | -41.26939 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4158ab93-fe2a-3211-a5e4-a68f4e15e9ec | -6.15622 | -41.86609 | 2024-10-28 03:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 50ccdef2-efe6-39ee-a412-8e8f740eea22 | -6.09435 | -41.87379 | 2024-10-28 03:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 467ee755-15a1-33b7-aa0b-01066c5581d0 | -6.09356 | -41.87848 | 2024-10-28 03:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 216b4a5f-b199-370c-8075-bf5e616b301d | -6.08899 | -41.8777 | 2024-10-28 03:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 12178a0d-bb0c-3226-8e90-20fb01353a05 | -6.57057 | -40.5569 | 2024-10-28 03:42:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5d1c1868-e2dd-3565-8e47-77d4579171dc | -6.22761 | -41.26854 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25c053a9-38af-39a4-8527-a9e2e9a9615f | -6.22686 | -41.27077 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dc86542-b2c7-3ab4-8f45-3d0c7a7379a9 | -6.29784 | -41.91773 | 2024-10-28 03:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 458e80b5-3711-341c-b52b-7e5a9385aa0a | -6.28869 | -41.91619 | 2024-10-28 03:42:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7f2ba3e2-b063-3abc-85d4-4701c30ed56b | -6.23405 | -41.25678 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6cde4bf0-2ae4-3845-aff8-d35a2a3f7d5f | -6.22758 | -41.26663 | 2024-10-28 03:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd6fc250-2042-305e-bf10-8fcc0d159b61 | -6.08977 | -41.87306 | 2024-10-28 03:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 86d26698-c22d-34c7-a7a7-12ced303a888 | -6.37321 | -40.47116 | 2024-10-28 03:42:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e117f6ed-e70a-3acd-bd9e-fbc0f6d694ec | -7.34 | -41.86255 | 2024-10-28 03:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 885fa96f-149a-3db9-8d10-d2925f2535e1 | -7.00636 | -41.34559 | 2024-10-28 03:42:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 177ea418-e181-33f3-be40-62d028958e42 | -7.34444 | -41.86349 | 2024-10-28 03:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1640859f-9893-3f31-b5ea-622f29684a8a | -7.00996 | -41.2987 | 2024-10-28 03:42:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3549338c-9c30-309b-b8be-3c9ecae68d44 | -6.94532 | -41.33089 | 2024-10-28 03:42:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e24b5a81-f504-39fb-8cd1-7c8be9f3b47a | -6.94464 | -41.33492 | 2024-10-28 03:42:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7dc8e3df-03f8-3b54-9c5d-1de8ddd8f149 | -6.93956 | -41.3385 | 2024-10-28 03:42:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f7b313ec-f7e3-3051-8de8-3e221948c3ed | -6.67267 | -40.8973 | 2024-10-28 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f4198967-84b7-30dd-a151-291e91b12600 | -7.33554 | -41.86167 | 2024-10-28 03:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59932735-5e0c-360f-bd83-305267c76944 | -7.00564 | -41.2979 | 2024-10-28 03:42:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2eaae36d-e8fe-3b04-96a5-6432a91235bd | -6.99986 | -41.33138 | 2024-10-28 03:42:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1e25c270-de61-3f34-8575-c4b2371110e8 | -6.99914 | -41.3356 | 2024-10-28 03:42:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7790756d-7c3b-3147-8ff1-51bb9d122cdf | -6.68243 | -40.89108 | 2024-10-28 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b8a5644a-11cf-3f58-bd9f-c91da2f10382 | -6.67201 | -40.9012 | 2024-10-28 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0d3a81c5-c9bb-396a-aaa8-89dc70d17b23 | -6.67755 | -40.89419 | 2024-10-28 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 85669172-9181-3965-a6b4-bf561ab40482 | -6.67689 | -40.89808 | 2024-10-28 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 13101aa9-a458-32e3-85df-42f25cb995cf | -8.86996 | -41.27056 | 2024-10-28 03:42:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8e6c94cb-b711-3a9e-b0eb-65b3fd2cf303 | -8.86929 | -41.27441 | 2024-10-28 03:42:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 94c34942-948c-3370-8c59-cbd21b2fa7f3 | -8.68682 | -41.22806 | 2024-10-28 03:42:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70ae6831-6b4a-3cb7-8b2a-442c3fd70048 | -8.28705 | -40.88676 | 2024-10-28 03:42:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f3803d0-dbab-3197-86ee-300cee5d751f | -10.75983 | -41.40918 | 2024-10-28 03:42:00 | NPP-375D | UMBURANAS | BAHIA | Brasil | 2932457 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28ca931d-2f22-3de2-adc1-24d26713596d | -10.16908 | -42.44414 | 2024-10-28 03:42:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f8a393c8-4341-3ec8-b23a-448a4cfc98ce | -11.99122 | -43.08488 | 2024-10-28 03:42:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 699f48d0-7714-3208-b6fc-0232190b9fa0 | -11.56697 | -42.92638 | 2024-10-28 03:42:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a9a3f47f-04f9-3a44-be7f-a7ffe768c3e9 | -11.28972 | -41.86343 | 2024-10-28 03:42:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| dcf49c47-1614-3876-84a6-e70c612ed73a | -11.14007 | -42.17494 | 2024-10-28 03:42:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7a8b6ba8-5698-3c9b-81ef-38b4a20e0df9 | -6.50569 | -42.3406 | 2024-10-28 03:42:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 36a8d49e-548f-3da4-86e6-6577709f14ad | -5.91594 | -42.86718 | 2024-10-28 03:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 221bd8f6-7824-340c-92ba-bda8575bd7c9 | -6.51247 | -42.35724 | 2024-10-28 03:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 67b5b462-79a3-317c-ae89-bfd11e6a414f | -6.51158 | -42.36236 | 2024-10-28 03:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4ca53d1-25a0-3f25-957d-dccd762953ee | -6.37146 | -42.72172 | 2024-10-28 03:42:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a2123f3-edc7-345d-96e6-9fd879a88949 | -6.34282 | -42.97676 | 2024-10-28 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6f62fd9-c55c-3305-b334-fb84cb54d539 | -6.62384 | -42.79604 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3b9fb3eb-2545-31ac-93c6-7c9cad01b8fd | -6.61975 | -42.78016 | 2024-10-28 03:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README27.md)
