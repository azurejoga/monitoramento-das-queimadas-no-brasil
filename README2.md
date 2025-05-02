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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 055a5025-1cf1-3508-baf4-5c183d2246a1 | -10.36792 | -39.8714 | 2025-05-02 03:55:00 | NPP-375D | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 64e2abb2-ffa3-3385-8ec7-b640569bb09e | -5.16526 | -45.10766 | 2025-05-02 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ecdfaf2-b7a4-37e8-a50c-ad6db635269d | -9.88456 | -37.07536 | 2025-05-02 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| dac22f35-7273-3ef9-b9bf-e2d583bcc773 | -8.4321 | -36.20597 | 2025-05-02 03:55:00 | NPP-375D | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 328793ca-4d43-3120-a77c-89a5beff91b0 | -8.07279 | -34.97755 | 2025-05-02 03:55:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6af59f48-0d74-3518-88c9-7c28575ddaf6 | -8.37577 | -37.2513 | 2025-05-02 03:55:00 | NPP-375D | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 81576c44-635a-314b-9f62-f40f85dd30e1 | -7.99187 | -44.39288 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb32e796-0983-3a4c-b3e8-9da9615afe2a | -6.70047 | -42.12676 | 2025-05-02 03:55:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 601345b5-8cc5-3523-b8af-afd0c26166b9 | -10.38426 | -37.13272 | 2025-05-02 03:55:00 | NPP-375D | CUMBE | SERGIPE | Brasil | 2801900 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5e551f47-dc4c-31fd-9bf1-84e26981be2a | -9.88802 | -37.0759 | 2025-05-02 03:55:00 | NPP-375D | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a08cbb8a-aaf1-3a23-b3e6-7e44ce1c285e | -7.99961 | -44.3982 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c10b174-2c09-32d6-b978-0607eabbefa2 | -8.00029 | -44.3943 | 2025-05-02 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddbfaeb9-09e1-334a-98ee-d338fe44c956 | -9.60802 | -37.03044 | 2025-05-02 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1e55043a-8c8b-353c-a731-88d275b60102 | -5.16141 | -45.10209 | 2025-05-02 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f17d66df-0572-31f1-a4d5-ab89cf674034 | -9.60688 | -37.03806 | 2025-05-02 03:55:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e97c1b45-a960-39fe-80b1-ba0292b74822 | -11.39383 | -52.95163 | 2025-05-02 03:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e39f0fa-75e9-3a21-9f65-b6f69726375c | -11.39515 | -52.94524 | 2025-05-02 03:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d21b83c-628a-34bc-ba75-f67e729d9e4c | -15.49806 | -45.92609 | 2025-05-02 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e91b51dc-1da7-3b47-ac9c-05d04115859a | -13.05163 | -53.71148 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb4861dd-7b06-3efb-9b34-c5d1a40a4228 | -13.04953 | -53.70972 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 649267d8-6bc1-37f5-8a55-4085a954a259 | -17.62152 | -50.91726 | 2025-05-02 03:57:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cf2f896-5691-34f0-8f8f-da8e14792273 | -15.50217 | -45.92684 | 2025-05-02 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91996e4a-6763-3846-8127-ff8e33faabaa | -13.04474 | -53.70972 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e73fa39b-0194-370e-abf9-63d80ed80b7c | -13.05023 | -53.71806 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 43a0720b-ea91-3bd4-b8f8-66ee10670332 | -16.31676 | -53.82404 | 2025-05-02 03:57:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ced6c157-0099-38ec-9fee-617c2985b25a | -11.39475 | -52.94849 | 2025-05-02 03:57:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bf26501-e5c3-30c2-9f5c-7a057d365304 | -13.04518 | -53.7294 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 58a5ef39-c9e6-39bd-ac86-1d3adff12cbd | -15.50033 | -45.92729 | 2025-05-02 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acda9e11-c034-35b7-9c9f-346b5be45a73 | -13.0481 | -53.71622 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 56c2eb4f-64cd-3d72-a8ab-d389403cf30a | -13.04741 | -53.73121 | 2025-05-02 03:57:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 898f81f7-edc1-372c-a4ea-ec3cea65e9d5 | -23.60921 | -49.00742 | 2025-05-02 04:00:00 | NPP-375D | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae373433-8a19-354e-a26b-5d5ea14e51f6 | -22.54108 | -48.81233 | 2025-05-02 04:00:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba1a15b9-8e25-32af-ace3-2354de988a6d | -22.54049 | -48.81494 | 2025-05-02 04:00:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a9e2f2a-9035-3636-aa67-97bccf27db40 | -23.59355 | -47.43953 | 2025-05-02 04:00:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d0b72909-79d7-3475-8e48-5af50dc86ecd | -23.9852 | -48.91991 | 2025-05-02 04:00:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6084ae44-f0e1-34ce-a4d1-9bfd204a07fb | -23.34014 | -46.77401 | 2025-05-02 04:00:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d10da6ca-bf30-34c7-8033-d68442af538d | -23.4037 | -46.55621 | 2025-05-02 04:00:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8bf1ae7b-97d9-35ad-925c-6ff74fa55b41 | -22.85789 | -42.98093 | 2025-05-02 04:00:00 | NPP-375D | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 362c8bfb-ed1b-3c05-9cf4-f173a39a5f55 | -22.90125 | -43.75283 | 2025-05-02 04:00:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a1800475-d139-35b6-8ea9-b105365a8aa4 | -23.98605 | -48.9157 | 2025-05-02 04:00:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d67d336-4387-3490-a024-3436689b657e | -21.62685 | -43.46701 | 2025-05-02 04:00:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bdfa267a-e9ac-300b-83a1-bda832b64d15 | -23.40743 | -46.55713 | 2025-05-02 04:00:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 63ea1a3e-7ae0-3b53-b526-e7be8e3f00da | -20.76269 | -46.77112 | 2025-05-02 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 148a7ad2-850d-36e3-bd0e-55f03be12cbc | -19.71661 | -40.35394 | 2025-05-02 04:00:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d24a4d60-4923-39d3-bafe-13c7da75faad | -20.76533 | -46.77028 | 2025-05-02 04:00:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1ec32b91-5845-3576-be5d-91d93438770e | -20.41643 | -43.55293 | 2025-05-02 04:00:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 77af9535-47e9-32b4-82d4-a1799a48a89c | -19.97004 | -44.21698 | 2025-05-02 04:00:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2b9c1c6a-48a0-3647-9ea2-2dd60ee0c31d | -21.17975 | -43.97951 | 2025-05-02 04:00:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e3dc7c88-a441-33a6-9d0d-191cd85c1ca9 | -29.77694 | -51.17712 | 2025-05-02 04:02:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 35c4ebfe-05ba-3c42-a124-03e60ba11b4b | -9.60954 | -37.03129 | 2025-05-02 04:17:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2cfaf94d-0bfd-3335-bd9f-ba6003f054fb | -6.6967 | -42.12848 | 2025-05-02 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f1816f4c-11f4-39c8-9c62-87200db14534 | -6.69759 | -42.12701 | 2025-05-02 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0531bc7a-9480-3cc8-bfa7-629c064cdf94 | -6.7011 | -42.12754 | 2025-05-02 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d2b50dcc-0011-3c06-b6a8-3be7b0f6d721 | -7.9934 | -44.39214 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ad0f2b2-7b45-3fe7-a897-a54874d7bac0 | -7.99726 | -44.38917 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afc307cb-48a4-32a2-9a6b-5e665c1d1850 | -8.07836 | -43.10938 | 2025-05-02 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 380a8a30-d14d-37f4-a854-69acec81efb8 | -2.59824 | -49.0632 | 2025-05-02 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 296b147b-8f84-30e6-bb86-202fe0024632 | -8.01765 | -49.62935 | 2025-05-02 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9e02a7f-66bf-34cd-89b1-c06a5a223b12 | -7.99285 | -44.39563 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b95f116-6042-384b-bc24-e94c7be05e04 | -7.99617 | -44.39615 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b018bbfb-b8e4-37d8-ad5f-04ab307e1892 | -9.60915 | -37.03424 | 2025-05-02 04:17:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7e7db159-664f-397f-8173-3a334017b1bd | -9.64784 | -35.82794 | 2025-05-02 04:17:00 | NOAA-20 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7dc9df43-ff5b-354d-8723-4f412f5beed7 | -8.00281 | -44.3972 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f81a951b-3ba7-3143-a02c-9ba4684b434e | -9.88893 | -37.08019 | 2025-05-02 04:17:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e8ae8e6f-aa6f-304b-9acd-67d021516a62 | -7.99949 | -44.39668 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2ea66e9-833c-3deb-bbc3-ff3bd80cd8ce | -8.79737 | -39.77167 | 2025-05-02 04:17:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0e453fca-a883-39a2-8838-07a0d4740984 | -9.60411 | -37.03358 | 2025-05-02 04:17:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5fee9c23-7b6e-3243-98f2-f4d024475739 | -7.9978 | -44.38568 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285b0e06-bac2-3fd6-84c3-71e54b0ffbb2 | -7.99671 | -44.39266 | 2025-05-02 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8a54e21-c6e6-3aff-9d20-e040ecc02f43 | -9.64738 | -35.83154 | 2025-05-02 04:17:00 | NOAA-20 | COQUEIRO SECO | ALAGOAS | Brasil | 2702207 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5ac28e8b-998c-3bbf-a87e-c4c77488d66d | -9.60876 | -37.0372 | 2025-05-02 04:17:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 939d4ce1-3c75-31d5-9eb6-0e3922289f7a | -9.88389 | -37.0795 | 2025-05-02 04:17:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 1d554d46-284b-37ba-b16b-5330efd2e1b1 | -9.88428 | -37.07668 | 2025-05-02 04:17:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| fac31847-d7dc-37f3-96fc-693abf4cd1f1 | -9.60837 | -37.04014 | 2025-05-02 04:17:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37ccc98b-9f35-3ea6-bebe-6744579bdf1f | -13.0477 | -53.70932 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d9bfeb58-a7cc-395f-9145-1aa8dededcca | -13.04383 | -53.72972 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f693532f-0ca9-3737-bebf-a5752c27fad0 | -10.97596 | -42.18243 | 2025-05-02 04:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70541221-1cb3-37f4-93e8-4060208e23d0 | -12.5544 | -57.71183 | 2025-05-02 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 628f5c40-872e-3d23-97a7-d01881a2e693 | -4.65051 | -43.18953 | 2025-05-02 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 861632d6-b968-397a-b16b-aee1dbaaa29e | -5.16086 | -45.10231 | 2025-05-02 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4a16695-54ad-3000-80b8-b1d37a7177c4 | -13.04674 | -53.71438 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 03b0128c-56d7-33ef-914c-23418cda82dc | -11.39626 | -52.9494 | 2025-05-02 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3571e18c-677e-3817-a8eb-01e986041018 | -15.07969 | -48.94409 | 2025-05-02 04:19:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53c7e027-c7d7-37b8-a701-e290b3bee48a | -12.54323 | -44.45148 | 2025-05-02 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c934b95-dc9f-3947-a0a9-3f3f7fd9f23f | -13.03912 | -53.72875 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 507c3fa4-a043-3460-bed9-825684ded11d | -3.83554 | -47.80994 | 2025-05-02 04:19:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 215ee70f-cdb2-3646-8563-67eed1f5c59a | -5.16363 | -45.10632 | 2025-05-02 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a6842e7-54c9-3ca3-b1f0-3c924675f70a | -12.54825 | -57.71067 | 2025-05-02 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb59b921-a190-315c-84d2-9dd7a51b6acf | -12.54662 | -44.45201 | 2025-05-02 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e260a899-981a-3075-867f-3ed1a38453ad | -4.89612 | -37.52731 | 2025-05-02 04:19:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| db98572f-a1ef-3fb2-9416-cabd451f6e34 | -5.79282 | -43.61495 | 2025-05-02 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00d24abd-32d6-3762-b8fb-e08a349d04c1 | -15.49951 | -45.92661 | 2025-05-02 04:19:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 124d2538-3122-3bcd-898b-4bec79c7501c | -12.54859 | -57.71224 | 2025-05-02 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a509da8-91d3-3685-b4b8-3ecef2044691 | -4.89458 | -37.52876 | 2025-05-02 04:19:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54830cd4-0b81-3cce-afc5-44811206f58d | -13.05143 | -53.71539 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 590823e1-4122-33c1-80f8-c7798c9f64c4 | -5.41974 | -43.20013 | 2025-05-02 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6819e6e9-f825-399f-b02f-a0f2363bb70e | -12.54956 | -57.70741 | 2025-05-02 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 876ae121-ed2e-3742-956c-eb25186634cc | -12.55474 | -57.71342 | 2025-05-02 04:19:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bfe395c-2d54-39d3-8126-6e56f10c0dc1 | -13.0448 | -53.7246 | 2025-05-02 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f668354d-280c-37eb-b557-c49745844bce | -4.64996 | -43.19305 | 2025-05-02 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README3.md)
