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
| 0679b99e-df67-35f3-bb86-b15694b3ddb4 | -5.79606 | -45.08105 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64d27bdf-6f9f-32d9-a70c-c19c832d3925 | -4.29041 | -48.05991 | 2025-07-16 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f602f1cb-9b22-3235-b493-5ed0d6af6be6 | -7.20914 | -45.32903 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fab734b3-bdc0-37a8-a150-cd10224922e6 | -3.84246 | -47.75424 | 2025-07-16 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44be43a3-43cc-34f6-be0a-31e546177bb3 | -6.39776 | -42.45323 | 2025-07-16 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b26e4d5d-72be-3d18-b624-5cc8914417ee | -4.30372 | -48.10472 | 2025-07-16 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 527d66ca-ebca-382b-bb94-6a2b7c5ce357 | -5.7808 | -45.0932 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b95f0839-c0f0-3c3c-b04c-1cdc8ccea87c | -5.57232 | -46.52875 | 2025-07-16 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c57aaee-e2fc-3afb-a3bd-4f96565c9da4 | -7.18429 | -43.11901 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88665ed2-8ff9-3f10-a28d-3abc10af955d | -6.71719 | -44.33379 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09dd5bdb-bf59-36b8-b0d8-59ade65ef025 | -7.5093 | -46.69223 | 2025-07-16 03:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a4be61e-d71b-35f1-94e4-a29691d3f9c5 | -9.42609 | -40.36821 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e18b830f-71c3-308d-ab89-13c55b32feb7 | -4.78172 | -45.34178 | 2025-07-16 03:49:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0a5b804e-cd16-3c20-a30d-9af66575bddd | -7.94922 | -49.6565 | 2025-07-16 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc9d6084-a220-3ffd-bb98-0b1dc216b5d1 | -5.78798 | -45.08192 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e82d7173-8e60-3da5-8c5f-3f6448b20341 | -4.03025 | -48.06733 | 2025-07-16 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f0005000-8ecd-3d28-9022-8aa97ebde447 | -2.91772 | -48.23635 | 2025-07-16 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98fba4d2-c0cc-3221-b2cf-ef25b18b6044 | -5.79256 | -45.08589 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47eec62c-9697-30ae-a305-b6fd76cdbc8b | -4.3024 | -48.10414 | 2025-07-16 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 808f29bb-f80f-35c1-ae2d-9709e0359ab5 | -3.21968 | -48.97481 | 2025-07-16 03:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4a51ea1-f995-3c40-a70e-a2bb3c5a1e2b | -3.38979 | -47.49458 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2917844-8861-3061-a561-ab511ac76129 | -7.21872 | -45.33399 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fa332e1-e6d3-3d8a-bfa7-006d8a62d4d1 | -7.05776 | -38.85607 | 2025-07-16 03:49:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8db3238b-5df3-3f79-ae0d-c6152ab290d0 | -3.37907 | -47.48259 | 2025-07-16 03:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| affe669e-8a99-395b-ac03-9c1415e5f69b | -7.51061 | -46.68496 | 2025-07-16 03:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f60b48bb-328c-350f-945d-df42a2336419 | -7.27667 | -45.2928 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51eec94f-3f35-3447-98e8-7659730d2c01 | -9.42898 | -40.37291 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| abe3acd4-cb39-334d-8a33-8b741aa3f537 | -8.25158 | -46.36632 | 2025-07-16 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fec6486b-ac6a-3b8d-be18-1dbd43203174 | -6.73328 | -44.32606 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4e63c0b0-ae4c-3be9-9392-2d8536a6d12d | -9.59813 | -40.61176 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 61bc88a1-84d2-3170-9f1d-a4dcb845dffd | -7.95978 | -37.18948 | 2025-07-16 03:49:00 | NPP-375D | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 160e986f-2ecb-3296-8423-eff2fce5ddee | -8.24528 | -44.92673 | 2025-07-16 03:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2350dcd3-bdfd-38a4-bad7-033a10d17acb | -6.71241 | -44.33296 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5b5a92b2-95bf-3687-bdc5-483e927627ef | -7.20357 | -45.33097 | 2025-07-16 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f14d4a9-b3a5-3522-bd94-e2170d0569d9 | -7.18792 | -43.12403 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ded23539-6efc-384c-8617-eb7899f37f41 | -5.79551 | -45.08411 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21d6fc4b-579c-31e8-9de4-57139c956726 | -5.87421 | -42.40673 | 2025-07-16 03:49:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 71a6f809-ccd9-3599-9411-73451950718a | -7.193 | -43.12054 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 90e42859-1a3d-3550-bf7c-1b6109c1b3f1 | -6.73062 | -44.34142 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 46935d43-1915-38df-9b11-c3326436fb67 | -5.7936 | -45.07975 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1ba818c0-f3ae-348c-abfe-8f1d50b6e5ff | -3.84646 | -47.75152 | 2025-07-16 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d13a1355-2a2d-3448-8207-e6beab6745b6 | -6.66895 | -43.02903 | 2025-07-16 03:49:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bae14a5e-34a6-3e8e-a35a-1dcd0705a2c3 | -5.73216 | -44.50943 | 2025-07-16 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9701880e-9b0c-38a1-848d-1d579b10bd1a | -8.50085 | -36.58963 | 2025-07-16 03:49:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 00d77ed2-9fbf-3277-8847-977f5b03d430 | -2.92427 | -48.23746 | 2025-07-16 03:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bb9e558-5799-3d76-8266-fb3c6e6b113a | -6.9433 | -44.94684 | 2025-07-16 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e04d15d-93ff-3995-9e20-3a1337cd84a1 | -5.9664 | -44.17335 | 2025-07-16 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34429b37-9cb9-353f-bbc9-e351e7a7e440 | -6.43549 | -42.81557 | 2025-07-16 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a458bf2c-e18a-35f2-9af3-3e57bc5b372c | -4.29198 | -48.06073 | 2025-07-16 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b58e9e2-9cb0-35ad-af8f-414e853504ac | -5.07096 | -37.71554 | 2025-07-16 03:49:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 63814328-9a24-3092-8e94-7fa4d4fc27be | -6.63564 | -44.57095 | 2025-07-16 03:49:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b80551e-8f63-3e74-8850-f5caee962693 | -5.67139 | -43.71783 | 2025-07-16 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ffb7937a-4e67-346b-bd8d-dd9f707639b8 | -5.57299 | -46.52501 | 2025-07-16 03:49:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a0bd769-5ad5-3ae2-88a9-161979aca0cb | -6.12765 | -42.957 | 2025-07-16 03:49:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97bf466c-acba-3f03-8f1a-f1b9baa3246e | -7.05022 | -43.49195 | 2025-07-16 03:49:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b48568c4-cbc7-3073-9b98-21f3533a37e7 | -3.31985 | -40.00662 | 2025-07-16 03:49:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1f4245d8-90f6-3ec9-acc9-8c716ee953c9 | -5.78746 | -45.08496 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f71cab91-c42a-3004-b400-0243f5ff91f1 | -5.97142 | -44.17073 | 2025-07-16 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b670119e-9718-32f9-b955-d07ce6da0f43 | -5.35976 | -36.89377 | 2025-07-16 03:49:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 41fb9186-8508-324b-b4c1-bb30cda37b82 | -5.96726 | -44.16821 | 2025-07-16 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 821731d2-9a9f-3247-8620-df3f0f7c77af | -8.51217 | -43.30674 | 2025-07-16 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 234afd68-3146-3927-b41f-c053723510b8 | -5.72334 | -44.8308 | 2025-07-16 03:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85b88f0e-d4db-379b-8871-6e583d775f0d | -5.96576 | -44.17491 | 2025-07-16 03:49:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3086f5f-3736-36b3-bdad-1d25440d3bce | -7.83462 | -44.19612 | 2025-07-16 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 719708c5-755a-3cad-9089-67bda0338988 | -6.70854 | -44.32696 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 17a94b63-a6a3-3e37-9dac-1c26ab239071 | -6.34279 | -43.43671 | 2025-07-16 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78608c47-4de7-33d7-ae40-f313b4cb11d9 | -4.03663 | -48.0684 | 2025-07-16 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a76116b-2eb8-3c8a-8bdd-b22ee8c0b35f | -7.2721 | -45.29705 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64d9cd0a-3893-3e5e-97de-9827e16c2234 | -6.39294 | -42.45603 | 2025-07-16 03:49:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 69abc5ba-2931-3511-9b32-f3978fc753d6 | -7.19229 | -43.12476 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c7a1a6a8-4936-38dc-b90f-d5d837cc5866 | -8.50354 | -43.30523 | 2025-07-16 03:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 42d32f3d-f1cf-3191-9139-f727b961f401 | -6.34196 | -39.85796 | 2025-07-16 03:49:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1d95506-84cc-38a8-b84f-856c0dd486b3 | -7.94384 | -49.66013 | 2025-07-16 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 70a238e6-ee0f-3a02-a557-837768db871a | -5.46493 | -45.33889 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1e1fc90-d4e5-3274-be58-2606fde3e5df | -7.20861 | -45.33201 | 2025-07-16 03:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ad85f21-737b-3cec-99cf-e681524456cf | -5.79041 | -45.0832 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 32e7b1cc-516d-34fa-8061-8b3c9c5a5879 | -3.84557 | -47.75655 | 2025-07-16 03:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 290bc6cf-0ffc-3a54-a469-a99f343bbf9f | -6.70944 | -44.32185 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 493ca0d8-cc7a-3953-9e97-87017cf92dde | -6.72196 | -44.33462 | 2025-07-16 03:49:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01e317bd-9cbe-3004-8e59-6cd3f1820100 | -5.78643 | -45.09102 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c388db1e-ec12-32a8-925d-e119cc287c30 | -4.96665 | -43.22582 | 2025-07-16 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1f532f35-a8db-34c3-b704-928345d46ef7 | -7.34613 | -49.60338 | 2025-07-16 03:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afadd5c2-a551-3ee2-9e9b-48c515f6ab81 | -7.94143 | -49.66141 | 2025-07-16 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a24dc55e-6fe2-34b7-9229-0bb2cad18e34 | -5.05909 | -43.86377 | 2025-07-16 03:49:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27cb653b-3a11-34c5-8596-8f6336d9771d | -5.78287 | -45.08106 | 2025-07-16 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61c5d1a1-dcce-3b18-adfc-2b02186c9ec1 | -8.5014 | -36.58612 | 2025-07-16 03:49:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d20e7098-3277-3d8b-b42c-f7b7f1ef87c8 | -4.03116 | -48.06217 | 2025-07-16 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f9e33f54-9199-3d72-af6a-5ca38ed38cc6 | -7.185 | -43.11478 | 2025-07-16 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9bec1824-b4bb-30f4-8dac-4258e527be9b | -2.44628 | -47.32933 | 2025-07-16 03:49:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41077b83-0c00-3f04-8691-45b7ffb60b0e | -5.53407 | -43.89137 | 2025-07-16 03:49:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 977aecdc-9fe9-35fe-8d9e-a1ba6869296d | -2.28448 | -48.57864 | 2025-07-16 03:49:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36b21812-a263-32a8-8087-336e9ddc9b1b | -9.43036 | -40.3647 | 2025-07-16 03:49:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 46b4c18a-727a-3202-b180-0806e15b1ee4 | -3.21289 | -48.97356 | 2025-07-16 03:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06b802c6-0910-3e48-b3bb-e1724d6b0568 | -3.04956 | -41.12245 | 2025-07-16 03:49:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c6ed657c-7fda-334f-8c36-f3700364783a | -3.21865 | -48.97399 | 2025-07-16 03:49:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d288363-5ed9-3a65-807c-ca202581539a | -8.33135 | -38.08854 | 2025-07-16 03:49:00 | NPP-375D | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5136a4d-68c6-3739-a14b-5c55514c97ca | -7.35408 | -45.66625 | 2025-07-16 03:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecc92b0c-eed1-3f3d-9705-0ff321536bc3 | -5.35921 | -36.89724 | 2025-07-16 03:49:00 | NPP-375D | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 34ddcf49-f8da-3ff1-973a-106e42c8de43 | -7.46128 | -43.83392 | 2025-07-16 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c671e5a-d2b4-3125-b5b4-d429d9e9945a | -7.50995 | -46.6886 | 2025-07-16 03:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README9.md)
