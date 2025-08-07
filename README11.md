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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc06d6ab-0009-3ac8-9a6c-be7348d3ad2f | -10.63909 | -55.31721 | 2025-08-07 04:02:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b81a521d-202e-391f-89df-d84e531b459c | -9.10972 | -48.90438 | 2025-08-07 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17857cae-9157-362a-9b1b-f4dad42696c1 | -16.21554 | -41.34244 | 2025-08-07 04:02:00 | NOAA-20 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bbd57063-28c6-3646-a81b-c6fc035ea2eb | -7.91575 | -45.54471 | 2025-08-07 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44a192f-5cbb-32a5-9f3f-63f4b820534a | -8.24689 | -45.07052 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 135842a7-12a0-318b-8f80-a128b757105a | -11.74525 | -44.96109 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7df0168-f293-3c99-bc77-627adfdce014 | -10.48908 | -44.33657 | 2025-08-07 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93146752-2e29-38c6-b9b1-027afdc24653 | -10.63013 | -44.75054 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 123adf44-1850-31e3-88b0-f3ec00548c55 | -6.94644 | -51.63248 | 2025-08-07 04:02:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f73f74d-7e49-3818-8883-1f6b1595b3a6 | -14.82172 | -48.40881 | 2025-08-07 04:02:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bfa690a-b39d-3aa6-8d63-9b1840269d11 | -11.78694 | -47.54056 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed3808d5-ad32-3b40-8a91-34ef7759587b | -8.97541 | -40.61923 | 2025-08-07 04:02:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 29cd5899-4cdb-3aaf-ae83-a9b99097c441 | -11.7562 | -48.18752 | 2025-08-07 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e100ad8f-5ccb-3c04-83df-13b8c259e55b | -11.74449 | -44.96554 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9b7206c-b256-34dc-ac2d-6fe410165aaf | -6.92032 | -52.84889 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 383133f6-3d27-3df5-b3e1-6270b7c0642f | -10.44325 | -44.38688 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 020455ac-0e8d-305a-ab28-ecbcb63d5c5e | -11.78552 | -47.542 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c8c7fe72-71ff-346e-a45a-10cf16171d96 | -14.53712 | -45.59361 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96148df0-5d5a-31ec-a96e-e1ee1fc251d0 | -10.43668 | -44.40368 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 44c2953a-69bc-3c41-9542-97ba07851c49 | -11.17547 | -51.44617 | 2025-08-07 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc152518-73ed-36ff-acc4-b6e74ac47561 | -10.6374 | -44.764 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d41b5b1b-5890-3467-9037-af7b60c3e0ff | -12.55862 | -44.74515 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b750e3c8-2d3e-3d17-89f7-b9994463a6fc | -10.42427 | -44.38819 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3b16d9ba-332e-36b8-a7f3-8999b57f27cc | -12.7011 | -46.39593 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b5e7138-cd8d-34eb-a846-25d09d7dcfb3 | -11.18112 | -51.44735 | 2025-08-07 04:02:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a33801d0-f300-30cd-9f10-d7696e56baa3 | -11.78279 | -47.53208 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 983ebee8-d73f-30f3-8f7a-41df29a62be9 | -9.46943 | -46.30117 | 2025-08-07 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 653ac7eb-271e-3520-b595-1fa1fadc84f8 | -12.32926 | -46.05755 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41a3552c-a3bf-35de-8b56-0f96bed73f1a | -10.47244 | -44.39178 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fe3fb3f-92c0-3082-bc19-37b2f737f576 | -12.63776 | -48.11562 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01fd4f20-6459-3d83-b8e3-a0960a9d1212 | -10.4228 | -44.39688 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ede32f40-f81e-37d7-a17b-5eb37b73ccc3 | -9.55794 | -40.34796 | 2025-08-07 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 8a705115-6e52-3a0b-b41f-0261a61d870e | -12.34487 | -46.06038 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 17ff9160-e32d-39f9-ad66-72cfbfe08c68 | -12.34097 | -46.05967 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a75b955c-4591-34d4-b28d-fd2c684ad8dd | -12.54525 | -47.15302 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf3bb739-f3d5-33ee-b23f-e1c2eeb7a00c | -10.63163 | -44.74154 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c5466bd2-8608-3503-bc14-bd43d46732b8 | -14.5237 | -45.60503 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29c96666-f19e-301c-857a-84ccdbd3389d | -9.64829 | -43.84842 | 2025-08-07 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1438643-2d3d-3ce0-8cfb-4629274d28c4 | -12.51183 | -47.14727 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39da5b6b-c8f8-3d54-9b80-73b89080d348 | -11.75537 | -48.19209 | 2025-08-07 04:02:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b1b78bb-c884-3ccf-8dee-d378811f376e | -11.74975 | -44.95704 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 881c035a-fa16-3b43-9759-069e4a570034 | -10.63894 | -44.75505 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 67ee7ebd-11b3-31c5-8322-69dabc001c32 | -10.64126 | -44.75248 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 91f5eaba-d610-3e75-ab3c-1291b7d7a970 | -12.33229 | -46.06329 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb3ec5b1-5a64-3999-b84d-0c02f9128412 | -12.69909 | -40.17959 | 2025-08-07 04:02:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b02b865b-b2b8-3766-83dc-33bba4549350 | -9.65186 | -43.84911 | 2025-08-07 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 42e132c6-2512-3deb-b4b1-26662169f8da | -11.77119 | -44.96522 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b94e9927-1394-3396-8f2e-4667332fb112 | -11.28005 | -40.97496 | 2025-08-07 04:02:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17a24fde-6666-3e8f-9112-193b1b466414 | -11.40418 | -41.71432 | 2025-08-07 04:02:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8cadb6af-745c-34d1-b908-05999ba8cee5 | -10.64421 | -44.74669 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 295ef217-5444-3198-a392-1aa07a5005d2 | -8.41864 | -46.83575 | 2025-08-07 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29622929-526f-3c1a-8f99-25570a49f539 | -11.80906 | -44.26744 | 2025-08-07 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae0343f7-ac45-3dfd-b025-3e8b5fb6e2f2 | -6.95257 | -51.63376 | 2025-08-07 04:02:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1905090a-6dc6-39a4-99fd-dbb463a61897 | -11.18334 | -51.4478 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8de269a-7513-348e-80f8-b458831017c6 | -10.63755 | -44.75183 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fd7fda58-bb44-37ca-b9e7-a9c8b0207cdd | -14.5358 | -45.57951 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 034e450f-5852-35d2-b653-160b88088da8 | -10.6405 | -44.74606 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c7b77d63-0942-3424-bbae-cbe63391f76c | -11.73759 | -45.0059 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35c568f4-7e4c-3e7a-9d68-8a10f88df10f | -10.44913 | -44.35179 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4cecb07-06fe-396b-88ff-d6a2601caa8f | -12.71311 | -47.79679 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae37e12-7a62-3ba6-a192-53ddd4cafd73 | -8.42226 | -46.84097 | 2025-08-07 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 125be96f-f083-35fd-8e66-c1bb3c1501d0 | -12.795 | -45.45432 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2ad6f7e-ddec-3c5a-ac76-f9a1f6081fcc | -11.89691 | -44.97692 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d00b154-58ee-394e-aa3b-a6e330ee4047 | -12.52017 | -47.14878 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88aa9e5c-dc37-3ffa-92bf-988eaa1e796b | -10.63817 | -44.75952 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ecb34117-dcd4-3b0d-a207-d431d6cefbcd | -15.34584 | -46.34552 | 2025-08-07 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abb7c0b0-7eae-3470-a926-afb39c3cfd1d | -12.516 | -47.14803 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d69f053-5877-3c4f-9ccf-db7195353d1b | -10.63976 | -44.76144 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d86bb0c4-f421-3652-b61d-57b52f98a562 | -10.43742 | -44.37692 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe020a1d-7db2-3125-973e-7ea73cd7f2c0 | -10.42938 | -44.38013 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b15d7ca6-2ac7-3370-befe-05548438031b | -11.76353 | -47.51463 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 965bcf84-2146-35a0-a8ab-3a52ed8467bb | -12.52434 | -47.14956 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2554c52-d8ac-3961-92ad-c9ce55b9a088 | -8.51774 | -43.29822 | 2025-08-07 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| cb78282c-75c1-38cc-88b4-2a84a07d0bc7 | -8.24996 | -45.07618 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d42a1748-6069-3c83-a091-5fb9536741ac | -10.43375 | -44.39874 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd9237b4-922b-3d60-ad92-f12b923e2d4f | -12.63858 | -48.11106 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5bceb41-c58b-3d04-8050-44f940f3bfba | -12.555 | -44.74452 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70a58509-0c01-37a8-a9cc-daff7bdd8372 | -9.07857 | -45.05927 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d92b862e-ea7f-31b7-9f01-a353e2335070 | -14.35713 | -51.09715 | 2025-08-07 04:02:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79a3bbe0-fde7-3025-ae4a-8263a5c48f16 | -14.14401 | -44.74331 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 436545fa-3a7a-3469-89b0-e194c0d10ff8 | -10.63159 | -44.76463 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ae02ee07-5071-302c-960b-caae80f3a486 | -10.47829 | -44.3791 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 14a75ab7-897e-321b-a754-842087f4efbb | -8.51487 | -43.29363 | 2025-08-07 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 24601712-2cb4-39d0-bf98-3bf538183b64 | -8.51995 | -43.30683 | 2025-08-07 04:02:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 15b2dd69-694d-3575-b099-6a4d0fa78c15 | -11.77575 | -47.5213 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52e53e5f-c63e-31d2-9cd4-b148da6459f8 | -12.72854 | -46.37926 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ce1eca65-b6fd-310d-85ac-3183084f4e13 | -12.55428 | -44.7488 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 822c46cf-5eb3-3cc3-9adf-77eace98d246 | -10.63088 | -44.74604 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3f5a1778-8046-36f4-b46a-0dc3b02d7b3e | -12.33619 | -46.064 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c14fd269-87e2-3442-b69f-7d2ef935ae29 | -10.79751 | -46.49294 | 2025-08-07 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c48c4514-9ab1-3515-bc3a-6ddf3ce0c1ea | -8.1061 | -45.5034 | 2025-08-07 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07e6d1c-eec8-3818-bc74-3735338146dd | -9.08158 | -45.06482 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e83b98a0-764f-39ae-b92c-bfe1c5773011 | -12.70204 | -46.39058 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 00abeece-1057-304a-a052-0b29386abdc7 | -12.73248 | -46.38006 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f786a544-736e-3e47-915b-e999697421e1 | -10.27625 | -40.81356 | 2025-08-07 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9fc2848-b3dd-3ded-8425-e5b6e6c3fcbb | -13.00667 | -44.89 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51ad2383-b6a0-3644-9f96-1148d9884b90 | -9.06895 | -45.06004 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 959f2542-8c22-3fb3-be1f-22982186d01e | -15.77579 | -39.37433 | 2025-08-07 04:02:00 | NOAA-20 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 502443ad-3718-345d-b60a-aec15fe5755b | -10.42719 | -44.39314 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 797ac2c9-b865-33fb-92e7-09c9991e3d68 | -12.53685 | -47.15184 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README12.md)
