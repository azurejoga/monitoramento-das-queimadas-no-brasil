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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ee1c555-e47f-35cd-b9e4-1ee0a884b540 | -9.37798 | -50.20068 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f268a893-e963-3d39-a7ac-83f4911bb3b2 | -6.17792 | -43.34644 | 2026-09-14 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f5a2aad-1a66-3475-ad10-7290da83164c | -7.09257 | -41.81345 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ba4d360c-0c1f-3510-ac48-37a69c30f227 | -5.84975 | -52.10291 | 2026-09-14 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d89010d8-f58f-3249-9c17-c6112d13937a | -7.0973 | -42.10787 | 2026-09-14 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e17ab302-dfc7-3257-b227-ff8d930fe0ed | -4.26598 | -48.64056 | 2026-09-14 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cb1551e-02bd-3c92-baf3-52fdeef93aca | -11.5977 | -46.77785 | 2026-09-14 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ba171d6-0c4a-38e3-b374-e14008c094f1 | -9.44461 | -47.87383 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aff5aa1-8d64-3f02-834d-d6802068d5e8 | -9.41018 | -50.19305 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4325a55-1175-3116-aca4-6b50e46af0e0 | -7.29138 | -40.12212 | 2026-09-14 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6542beff-48f3-32d7-ba7b-0ed78c6c3a5b | -5.11363 | -41.0811 | 2026-09-14 03:55:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f3f640cf-e4ea-39dc-8041-a65b98ecf64f | -7.10579 | -41.77732 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 192c308a-4c7d-34ed-9d0c-2b6eed010dca | -9.45067 | -47.8568 | 2026-09-14 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f85b6c0-e5a1-3157-a57b-68cab79b499a | -7.96059 | -43.98746 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b568d800-b3c5-39fd-99b1-9880bef86692 | -7.09391 | -41.80519 | 2026-09-14 03:55:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab4c3d00-6ce9-3cb5-b54e-abffe343dc7e | -9.44034 | -50.13065 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| de06b7d4-e953-325e-ac75-6ef38489d6d8 | -3.35276 | -51.29371 | 2026-09-14 03:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 956d871f-07c6-32dd-a4c3-926835bec80b | -7.96614 | -43.98463 | 2026-09-14 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f938cc10-af64-3b7f-b710-f155de3aca78 | -8.99952 | -50.82446 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| de1be6e4-f8eb-37dc-95dc-27f85c7c0958 | -7.20392 | -45.92352 | 2026-09-14 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 849b162d-ec71-31b9-8ca5-09a73ac9c20d | -9.4875 | -45.46713 | 2026-09-14 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c44ba27-d2ea-333f-999b-4b084e5c4f15 | -10.068 | -48.78372 | 2026-09-14 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b15beaf8-8401-3c11-8be2-c6e01d1a05a1 | -5.81893 | -42.73958 | 2026-09-14 03:55:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 972e4fd3-8a2e-319d-9542-2ef4d9dc1810 | -7.19788 | -45.92102 | 2026-09-14 03:55:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c94331de-0f4d-3941-85cf-75638213bf3a | -11.19016 | -42.80807 | 2026-09-14 03:55:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0160129c-78f6-3f74-ad5b-5b86983d4b70 | -4.59587 | -47.17522 | 2026-09-14 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1fe04953-3d91-3b5a-aff7-5bf3de92ebb5 | -7.07815 | -43.54596 | 2026-09-14 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db85338a-22fe-3c14-82dd-28855f389dcd | -9.41847 | -50.14923 | 2026-09-14 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1affa38d-6884-3f19-9e3e-0687d6369a71 | -7.01477 | -44.63327 | 2026-09-14 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec260693-91dd-3406-a838-75402757e455 | -10.76778 | -48.97463 | 2026-09-14 03:55:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8724471f-0161-350a-93cd-56253103d54c | -15.04354 | -48.53514 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ecd089c-90df-329b-af5a-4a4f6e3c4fd6 | -13.46493 | -48.47414 | 2026-09-14 03:57:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1feb68c8-4e39-361a-b374-a4b5003eade6 | -14.18162 | -47.4114 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05351d1a-e01d-3d67-b0ff-aadde41769e7 | -17.37221 | -42.61837 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8828e2aa-2b6c-3b9c-81a3-ca15edc10fa3 | -12.85373 | -44.38572 | 2026-09-14 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f103350b-6ce6-395f-b7d3-1d0f3a5d4b96 | -14.17295 | -47.43275 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9ce8144-f393-3a53-9d2b-dddf51eb77f0 | -12.17517 | -48.96187 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 65a6b4b3-2528-3147-a875-e6f3548f2784 | -11.7762 | -46.40973 | 2026-09-14 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ce642c70-4c5a-3e11-ab3b-3b8f123f9687 | -13.30695 | -51.31496 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b09aaf8f-8682-3cfb-abcd-dc6ea30d94fa | -17.37097 | -42.6259 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5db1cb40-c9f2-3628-974e-34bcfd8a2351 | -14.83558 | -48.14476 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bcae16cd-11cd-39a2-9fa5-77d4ce0ce4ed | -14.82206 | -48.14507 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e457bc8-86f5-3752-ab94-75a7e4f66725 | -15.27799 | -42.79898 | 2026-09-14 03:57:00 | NOAA-21 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75d1e7da-2a6c-3d76-bd3f-2f562eaff34b | -14.82601 | -48.14357 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc5f9957-a241-3d75-92ce-3e8523faa0c1 | -13.78407 | -48.80995 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 369ec260-c56c-3e90-8bfb-ad009da8f2be | -14.83942 | -48.15039 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b528c07d-cbaf-3d9c-9c90-72ecfa71919b | -12.17053 | -48.95776 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94000ebf-a98b-35cb-9e84-739869f61908 | -16.05604 | -40.48247 | 2026-09-14 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a0bf3974-de7c-3014-a9ff-f0001acbd9e4 | -13.57097 | -51.46075 | 2026-09-14 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b93c1de1-2bf2-3160-9308-acdb1f99725c | -11.77781 | -46.40059 | 2026-09-14 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 56477d59-e0ec-3635-aa36-2d60b3716ccf | -15.06861 | -48.55342 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50a8b862-02f1-3486-ba12-13afafcc16d2 | -13.62617 | -47.90038 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c28e262-e5c7-39d4-ac79-1dc6b39a3021 | -13.29507 | -51.31252 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7fd818df-4614-3402-ae3e-d5779dd48b35 | -14.83079 | -48.14418 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0e0f13c0-b0dc-3363-8c41-f3ef1ba5db5d | -14.83265 | -48.14104 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3aa54641-b770-34ec-874e-c66d96e9a084 | -14.17984 | -47.39559 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d4765e47-6f52-3700-918f-9c4c4f7963b7 | -13.58915 | -47.8848 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2e3e5db6-5eb5-39ee-8e0c-db415bb3c5c9 | -12.17505 | -48.96265 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5a5e582-d39b-3929-aeb4-a6f82bd96373 | -13.78957 | -48.80843 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66fd7f29-bb2e-3851-bd97-ad17870a0cad | -14.8442 | -48.151 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c66248dc-3981-3d04-806c-47b5fc2a122e | -13.28822 | -51.31578 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 33daec39-b792-3545-ae19-3be1fab7a0d0 | -14.18895 | -47.39723 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb31a8ed-8779-38c3-a0c9-e2f8252e61ab | -16.19533 | -40.48313 | 2026-09-14 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a0015b5c-88d5-3071-ad74-e7a3a93855db | -13.58735 | -47.89459 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| da967143-7c18-36b7-9547-81d78a2c5a0a | -13.32065 | -51.71835 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70a5960c-e592-3c55-a426-53a7a4402de0 | -11.51087 | -50.25225 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a041955-48ea-3610-ad4b-11c1957ae572 | -14.16923 | -47.42741 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c3546cf-77ae-3ae4-9078-16bb999c7c0c | -13.5952 | -47.88211 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25fccec9-faa8-3d3d-9be5-ffbbbf708b40 | -15.05876 | -48.56038 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ecc76f60-5701-3434-be46-9b5dde4c269b | -14.17462 | -47.42375 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c12bb921-6405-3651-8240-5f5071d45381 | -12.16988 | -48.96136 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7eb89603-534f-30e8-a8c3-8674ff217c46 | -14.17619 | -47.41531 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5e4ccc7-0861-3f61-8567-34738c15d53e | -13.30011 | -51.3182 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5cba17fb-820f-3d0b-832c-143ffbc566d1 | -14.82024 | -48.14824 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74b7693d-7373-370a-aed4-91cdbb6025fb | -14.1721 | -47.43739 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f9e427c-8c7d-329b-b07b-14797fae233b | -14.84514 | -48.14593 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 483f5613-d921-3770-9d8b-3a53dc17067e | -14.83544 | -48.15186 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7617b2fd-300d-3aab-b772-cbe12367338e | -13.58364 | -47.89111 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bdc00f19-31b1-37c9-85d3-9c6812c9f332 | -12.17573 | -48.95889 | 2026-09-14 03:57:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96889eee-c4d2-3ae8-adbf-794fbe2c599a | -15.24985 | -42.79765 | 2026-09-14 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb8e5ef7-9e40-3f60-a121-146a6cc5b8be | -15.08359 | -48.32611 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d68ab55d-48d2-34a0-90bf-e744a39e3ac1 | -15.03234 | -48.51536 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7369ac5-6da0-3d19-b40e-e57bb7f1c04e | -15.04242 | -48.54099 | 2026-09-14 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d553561-3eae-3636-b2fd-1d707d0ac794 | -14.81364 | -48.15732 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c627494e-2e85-3837-876f-00ebf78b2f7d | -14.19796 | -47.42693 | 2026-09-14 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a4dec43c-cf0b-3218-87fd-fdee21d0204e | -15.21237 | -41.07003 | 2026-09-14 03:57:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d8204e4-e003-38f3-a76a-51c0f0f2c707 | -13.58821 | -47.88989 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7e5d84b2-0455-32e8-a5f9-eee0ae05c977 | -12.39777 | -44.41031 | 2026-09-14 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7093d14-c130-3635-b0e9-a9d529442400 | -17.36884 | -42.61779 | 2026-09-14 03:57:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f775810e-84d0-308e-8a78-67e94b89da4c | -13.77857 | -48.8114 | 2026-09-14 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c98c8042-c3cf-37f8-8b94-931a531f4951 | -15.00706 | -48.51669 | 2026-09-14 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25a9d8f9-9551-3c74-a009-341d04ca5a75 | -13.55297 | -42.41402 | 2026-09-14 03:57:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 035fb95d-c952-3a1c-b199-3c7e73b478a5 | -15.20412 | -44.07307 | 2026-09-14 03:57:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38f93af3-df1f-37b1-991b-111ba4a99c1e | -10.98371 | -51.4325 | 2026-09-14 03:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d4138003-2bc6-3cc6-9222-2eea47172ade | -12.39863 | -44.40535 | 2026-09-14 03:57:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ef68c5d-2732-3abe-8674-578c363603f1 | -14.61987 | -42.5296 | 2026-09-14 03:57:00 | NOAA-21 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a6599cb6-0274-3d23-89f0-3584c0eef655 | -11.777 | -46.40518 | 2026-09-14 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b37bfb62-d3f6-354d-8c85-db2a10534751 | -13.5911 | -47.87415 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c258313-2e64-3630-8961-7f2f257ce8f9 | -13.5962 | -47.87691 | 2026-09-14 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4f4be98b-bb89-34e6-8dfd-dadcdaefbc1d | -13.31457 | -51.7171 | 2026-09-14 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
