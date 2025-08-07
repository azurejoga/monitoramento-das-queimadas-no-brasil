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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 547b06f6-6edc-33ad-b258-1d2622ad6846 | -7.89069 | -45.08125 | 2025-08-07 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a596150-6e61-3775-8615-a84e6de36515 | -3.84064 | -47.75126 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06bde4b1-74a8-3b69-abce-4ba0285ec907 | -6.84097 | -46.39291 | 2025-08-07 04:00:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ec4771c-bf64-3b22-ba2d-f9ef0aaf4ca2 | -4.77709 | -45.33146 | 2025-08-07 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a00e6b5-2007-31ca-8a7f-dea8101b2f50 | -7.58383 | -44.89717 | 2025-08-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12b84c3b-94a3-326e-afbf-f494a54b33b6 | -4.77351 | -45.32695 | 2025-08-07 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e01cab5-ed91-3642-8420-055b3e27bcbf | -8.66875 | -40.53827 | 2025-08-07 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5eb090a7-4691-38f8-99c5-2e48aa5c2de8 | -3.84055 | -47.75549 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d265063-a621-3b8e-925a-ed1cade5067d | -4.02365 | -48.06458 | 2025-08-07 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8cdc8145-dae5-3ca7-a4d9-b52e61772609 | -7.854 | -43.85775 | 2025-08-07 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f755da38-4d25-3d6d-82d2-cca6f779ee63 | -5.72709 | -49.09806 | 2025-08-07 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0a36c53-599d-3937-81c2-07b140bf509c | -3.84012 | -47.75424 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f742ddbc-2291-355a-857b-db8ceac0675a | -4.29533 | -48.07565 | 2025-08-07 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ed2ddea-2d96-3da4-b86c-1d2a97a5c140 | -7.24152 | -44.63589 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9f9337b-7894-3140-89af-46719f11543c | -4.31014 | -48.08128 | 2025-08-07 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24362d98-2225-3ece-859b-e9e05e00278c | -5.53187 | -36.80379 | 2025-08-07 04:00:00 | NOAA-20 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cc8a171f-8ea6-33dd-958d-04317ea9f128 | -4.77287 | -45.33087 | 2025-08-07 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b1c46e8f-b6bc-30ab-87cb-4555b4fd502b | -4.18843 | -38.37169 | 2025-08-07 04:00:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 83671b5b-4540-3122-a583-b9d06ea2d23c | -7.40634 | -44.65537 | 2025-08-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9c130ed6-a1e1-3761-88d0-336d2d1e5b06 | -4.78229 | -45.35252 | 2025-08-07 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50ab62ea-6080-3492-b379-a3f4e34e85c3 | -7.39368 | -39.68214 | 2025-08-07 04:00:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5d166af0-9c25-3df1-9cb8-1954b41a31c1 | -8.32908 | -38.09446 | 2025-08-07 04:00:00 | NOAA-20 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 57fd2644-5bf6-3d82-8201-33f317bbdaec | -7.36788 | -44.62407 | 2025-08-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f982281f-76f1-3181-b73b-28751d9b3423 | -6.44117 | -46.11505 | 2025-08-07 04:00:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 470ecba9-50ac-30f8-a3c5-0f781c565546 | -4.77873 | -45.34787 | 2025-08-07 04:00:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e050c57b-4f4f-3b13-a703-df7be7608462 | -3.82192 | -41.57171 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e329708b-79c4-3376-b913-8f106ffa894b | -7.24071 | -44.64075 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 422d79e5-9446-3718-9d05-ba29e6a0a2af | -7.86354 | -43.86823 | 2025-08-07 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 338097e0-201f-3363-a47a-e55841d4879a | -3.84104 | -47.75253 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fc9da0b-d418-3332-9f6a-e38324c7eef1 | -3.95154 | -41.4845 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9b055f81-d684-3be2-bf95-3e001791793e | -3.84566 | -47.75216 | 2025-08-07 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5f46d18-c0ce-3941-8a76-6496a37e71fa | -7.75592 | -43.59017 | 2025-08-07 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1df709dd-5a08-3e09-abaa-6b91a8bca382 | -7.35971 | -44.15752 | 2025-08-07 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f2f69fd-a97a-3014-867b-d650d61b9d47 | -6.5244 | -45.57318 | 2025-08-07 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| d0bd5e15-de76-3f8c-80f2-1434b150f9d8 | -7.25025 | -44.60736 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f0fa61e-0f3e-3db3-b9a4-398e228a54a3 | -7.53414 | -45.15025 | 2025-08-07 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eb4f3ffb-e58f-3ab8-aaac-0466d0ebec05 | -7.53616 | -45.15285 | 2025-08-07 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85edbc7a-83ac-373e-b682-d1db123b9075 | -7.75814 | -43.59925 | 2025-08-07 04:00:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cdff8d4-d01a-38ec-bad1-265dde5125b1 | -3.95214 | -41.48078 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aad5c148-7713-3e34-85b8-cc220ed9b464 | -5.72116 | -49.1005 | 2025-08-07 04:00:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 061150f7-e86b-3f86-84a0-a3baa7836d05 | -4.02416 | -48.06158 | 2025-08-07 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc93b087-82a7-3c37-b5cf-d1c7027c66f3 | -5.59581 | -37.8317 | 2025-08-07 04:00:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91c27686-f871-3197-91e6-855588a27589 | -3.82373 | -41.56044 | 2025-08-07 04:00:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 56b3df1f-4fea-3a7b-b0ec-ea2b00d8c94a | -7.23763 | -44.63538 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8b93f8c-cb88-3bb2-bba9-023050c6bea4 | -7.36795 | -44.15421 | 2025-08-07 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da236be5-7f44-3d1d-acdc-b8a0c221a5e9 | -7.39556 | -44.6244 | 2025-08-07 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e4ed6b3-084d-30f8-aeca-3bb776bd76bb | -4.03337 | -48.06935 | 2025-08-07 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbc0e0b7-68c2-32fa-b11e-6d0040f2e318 | -3.64996 | -48.32716 | 2025-08-07 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 22fd8d1f-c8b7-3916-ba17-786fce2f36ce | -6.49542 | -39.49761 | 2025-08-07 04:00:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7c577717-42b6-346e-835f-eeccb0adfab5 | -7.35575 | -44.69713 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c37e128-638f-31df-a72a-d17e3fc4a23f | -4.64686 | -42.50134 | 2025-08-07 04:00:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b37d388e-24c4-3718-bf15-10fb52a4dcc5 | -7.53218 | -45.15223 | 2025-08-07 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7003884a-3865-3e02-80d3-cf48bb71aadf | -7.23457 | -44.62996 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f6aa7d-20d4-3030-bf21-cac851b0c2b7 | -6.95636 | -41.58113 | 2025-08-07 04:00:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8fbb1e81-8111-34ea-ad96-3abe482e6630 | -3.87732 | -38.54002 | 2025-08-07 04:00:00 | NOAA-20 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e54b8468-e89c-3995-b72d-d3696587f58f | -6.83662 | -46.39213 | 2025-08-07 04:00:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0e2beb5-c3d2-352c-ac0e-fc56edbfe74d | -7.21848 | -41.8499 | 2025-08-07 04:00:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d1a12ef6-94c9-3a9f-9a19-f3368cc09ff5 | -7.1474 | -44.08041 | 2025-08-07 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f880eb6a-dedb-3741-8d87-f383079f1bc7 | -7.24716 | -44.6021 | 2025-08-07 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2897efa5-f525-357a-b80f-bd0e3e159555 | -9.56179 | -40.34499 | 2025-08-07 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4423782d-273a-3891-b454-8f07e6480167 | -10.51057 | -42.40662 | 2025-08-07 04:02:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e137bd33-34f2-3566-8801-0e337f236d0f | -7.91295 | -45.53677 | 2025-08-07 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37c587a6-7092-3b1e-8e2c-873d8ea5cce6 | -8.88533 | -44.7864 | 2025-08-07 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 989c10f2-96d9-35f1-b57a-88fa80dcc5cd | -11.57499 | -47.708 | 2025-08-07 04:02:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48cf8c8e-57ea-3817-8d00-e37714edb144 | -10.45205 | -44.35674 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7152ca5b-7430-33d0-b81b-80fce44129f4 | -10.4323 | -44.38508 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eaa44254-ad17-3b21-a2f3-124e0e69ab27 | -10.44252 | -44.39127 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acca50da-2dec-3a0d-849d-a16bbfffe076 | -11.92094 | -44.02978 | 2025-08-07 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb2bc89e-855a-3ccf-8156-89cbc8a4bc3c | -11.37491 | -42.5281 | 2025-08-07 04:02:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d22d4c7-dcb3-3976-856e-373cd39df7a1 | -10.43594 | -44.38572 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c2cc0f8-6b8f-3028-a9ae-3f087d3dedfb | -9.46079 | -40.38326 | 2025-08-07 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 63351f3b-b9cc-34e1-b1ef-83dc74600ca6 | -14.52818 | -45.60123 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee529743-ac03-3646-88ca-ac5683c15abd | -11.78357 | -47.52765 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64cfaa5b-0945-3552-8901-4fb4cdeb23af | -10.42062 | -44.38758 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 505e29a2-c4c2-31e1-a45d-00bc4838f281 | -10.43741 | -44.39934 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6959fcf2-9f83-377f-b349-36414ea043f9 | -12.71972 | -46.38295 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea53c554-228a-3962-a916-ee7ed9222225 | -8.423 | -46.83666 | 2025-08-07 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e0964f7-e9fc-32a4-9515-702e24c6e1f9 | -9.61672 | -39.01508 | 2025-08-07 04:02:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 094825ef-3cc0-39bd-b7d4-55152ee305ab | -11.8055 | -44.26682 | 2025-08-07 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6a7de66-5997-3d29-a327-93415dcc77ea | -11.73606 | -45.01487 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7ed5e97-5445-3c2b-8cf3-4da6c402d37e | -8.90925 | -50.03817 | 2025-08-07 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab81c773-ad9a-3db2-889e-179d28020c50 | -11.739 | -45.02 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25aa425d-4dd8-3f4b-a0c0-76b5aa9b241b | -12.71388 | -47.79249 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d47150a-65ef-36e7-836f-d2f7cfd7b5fd | -14.52464 | -45.60812 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00df9e56-cf3c-36e7-ae5e-5a4cfe17912d | -10.69566 | -48.86977 | 2025-08-07 04:02:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ede1eca4-dabd-3497-8857-2a4184cbe531 | -15.543 | -42.64831 | 2025-08-07 04:02:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bde4563b-623f-3d89-a673-108ff4de8fb5 | -12.33794 | -46.05393 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07ef478e-8f48-3c7e-ab72-99f55b4ddd3e | -12.52851 | -47.15034 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82e3606d-b152-3969-80ed-aac79e5ec3ca | -10.58739 | -45.25518 | 2025-08-07 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da188ad6-bb25-3db1-98b2-d6b06525da31 | -11.78345 | -47.5352 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07900664-cb97-32ce-a8da-45cb32cd5cde | -12.3401 | -46.06471 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 855599f2-d9f3-3de8-b093-4bd6aebeb9cb | -15.6904 | -43.20713 | 2025-08-07 04:02:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0a4e4f5d-8ab2-3a74-abb7-5d420066a580 | -12.71744 | -47.79764 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97e9a706-ffe1-38cf-99ef-8e1d4166eb71 | -6.91091 | -52.84749 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed06eb8e-c6c5-3f44-a7c4-8005e7ba1c75 | -11.73682 | -45.01041 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74b2c7ba-f674-3889-a298-bfd05e3c2643 | -10.64343 | -44.75119 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4196d5d3-4db5-3b96-b436-7a0637d8d04b | -12.70693 | -46.38597 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| de52f77a-c7c7-31e6-aa3d-21a4ab46acba | -8.51061 | -44.74979 | 2025-08-07 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cde750e6-f174-3c7b-8522-3f00e438e6bd | -12.706 | -46.3913 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 849b4a0f-441b-33ca-84f2-d2494b5100a0 | -10.48544 | -44.33597 | 2025-08-07 04:02:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README10.md)
