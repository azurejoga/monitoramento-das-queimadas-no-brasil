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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 146a4a33-f311-3b93-8866-2252ea73c2eb | -9.85101 | -44.70768 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77ebb5ee-13c6-375f-bd43-43f1ee89e733 | -12.2688 | -45.06421 | 2025-08-01 00:26:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 190cc815-3783-3765-aca0-f9524460a1c0 | -6.69339 | -44.34779 | 2025-08-01 00:26:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ed5f66c7-9101-39af-98ea-4d30300c003f | -7.57386 | -44.82423 | 2025-08-01 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e019e33b-b209-31ec-81e9-b6a09efd334f | -10.7316 | -50.47311 | 2025-08-01 00:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 721fd288-d69b-3809-817b-806d62b3680c | -10.79231 | -47.26014 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 09d26ca1-897d-35e6-aaa1-4deead97ae9a | -11.51953 | -44.32322 | 2025-08-01 00:26:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8263e50d-3032-341d-8b6a-5c322122e855 | -9.35345 | -40.31334 | 2025-08-01 00:26:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| b9f7e3f1-e314-3230-ad4f-434ec0f5e2c8 | -8.51588 | -43.30737 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 37e461e6-b0d8-3752-af5e-79e7b91e130d | -10.43585 | -47.27589 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1a5c1852-aafb-3c15-aa9e-e360e7003a3d | -8.04555 | -43.10168 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 4f40711a-46b5-3de4-96f9-9111b0397b15 | -11.76122 | -44.98563 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9ca07a5f-10a0-351f-928c-36b2e1cdce39 | -11.76502 | -45.01267 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f506a672-23db-3cb0-9202-d5a77155a629 | -7.53085 | -43.83797 | 2025-08-01 00:26:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 28e77654-16af-3407-b0c0-cb384ef5ff4c | -10.44371 | -47.2651 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a0c7d44c-735c-3b9e-9d2c-a768ebbd345c | -11.77136 | -44.99339 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 35cc26a0-b143-3608-b75f-baae73037810 | -10.44243 | -47.25555 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 036598ea-3fad-377b-a2db-864e44125317 | -10.73214 | -50.47869 | 2025-08-01 00:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 4ff24bac-5e48-3dfa-a702-564acbe21e6b | -11.77263 | -45.00241 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 764c1eb3-799d-31c1-ab7a-1713a7f3f7d9 | -11.76249 | -44.99467 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0e26d55f-2bf1-3ba2-ba34-d9abd6d4edf7 | -10.80146 | -47.25891 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 910bcc2e-c814-3a0b-aea2-57e6b5bdf8e4 | -9.86001 | -44.70636 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d404dd6f-012f-3f5a-90c9-d235470e99dd | -11.77738 | -47.40064 | 2025-08-01 00:26:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d94080e0-e7e8-32ac-90c4-6ab25862459c | -8.04885 | -43.12444 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| eb51cf6c-a0cf-37b2-9221-3c64e0b632be | -9.40006 | -45.49709 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 6ba02bd3-224f-3ff4-b756-be9f4d077c5b | -12.74868 | -44.41783 | 2025-08-01 00:26:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e36feee4-58ad-38b6-9471-829e335844e0 | -9.73885 | -48.65989 | 2025-08-01 00:26:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 153f8a29-487a-3f19-8739-99ba8a012404 | -6.96723 | -44.508 | 2025-08-01 00:26:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94000e41-2359-3b11-b0f1-1baed69bdebe | -10.45412 | -47.27341 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ae2cceb2-8259-3b6a-8c7f-bf9d7394f62a | -9.86983 | -44.70805 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 946f7ca1-19e4-3796-b428-8cb044bee4fb | -9.40893 | -45.49578 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 165697dd-0648-3ca2-a478-ace307481205 | -8.32696 | -50.56821 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 0b0408f9-9f0f-3780-a456-adeab38daad3 | -8.24713 | -49.57495 | 2025-08-01 00:26:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 30d0ecf8-6322-3c2b-86e3-f3afdd73ff76 | -11.77389 | -45.01139 | 2025-08-01 00:26:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cc489734-f810-3897-8870-78d2d123f3f1 | -8.05548 | -43.1002 | 2025-08-01 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 84befd84-51c7-341b-9635-77250d5cecad | -10.73023 | -50.46381 | 2025-08-01 00:26:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| f54403dc-4940-3fbb-bb3f-d36365dbdeed | -12.09462 | -49.20739 | 2025-08-01 00:26:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 58a11099-90c2-3fac-b1c1-d0d8521e81b4 | -12.81753 | -45.44028 | 2025-08-01 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce3a643e-26ce-30af-b77c-c4b6256e6464 | -10.4333 | -47.25681 | 2025-08-01 00:26:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 971c08a3-4f2c-374e-9db2-01cec5bbeaea | -7.13056 | -44.36028 | 2025-08-01 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 97ca4851-f088-3083-ab5e-58dc201db736 | -8.5207 | -45.73112 | 2025-08-01 00:26:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 394c4f1d-c50f-3eb1-8be5-7cced4c0d372 | -12.55401 | -44.72954 | 2025-08-01 00:26:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5b965302-50a6-37fc-bc6a-80b4fedcdc5b | -7.13199 | -44.37038 | 2025-08-01 00:26:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e23c2cee-c45f-3482-8985-dbfd917cdb1f | -12.10022 | -44.98163 | 2025-08-01 00:26:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 05f9eced-c4e8-33b6-bd37-4ae5c952659e | -6.50749 | -56.20575 | 2025-08-01 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 22b9b1ff-996f-3c6e-b947-9a8639e89b5f | -3.81945 | -41.57094 | 2025-08-01 00:28:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 8ec8c0be-f3e4-3eba-bb36-fb06669187ff | -3.51485 | -47.21867 | 2025-08-01 00:28:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bdb79869-b0f3-3d69-a72a-1f1aa78e8126 | -3.69266 | -43.43163 | 2025-08-01 00:28:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 7d403c53-5e41-330d-8ee4-86635e743549 | -6.51763 | -56.23641 | 2025-08-01 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 2e4f2953-aa8a-3538-afcf-774d8f2b40bb | -3.50182 | -43.2404 | 2025-08-01 00:28:00 | TERRA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73809893-9220-3759-be74-b6d95c477c5b | -3.69464 | -42.2068 | 2025-08-01 00:28:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 8823c862-1f9a-3cff-baf8-005f32b3860f | -6.51329 | -56.20022 | 2025-08-01 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 47c8bd1a-0714-3bca-bb51-aecc5f37ac12 | -3.69666 | -43.43691 | 2025-08-01 00:28:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 137335cb-5303-30c8-b358-6647715a4ea9 | -6.748 | -59.1523 | 2025-08-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 3f57c439-8301-3b79-9f9e-028b835311e4 | -23.5242 | -47.8109 | 2025-08-01 00:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.5 |
| 1b07b862-9310-330f-86dd-c5fb93e0a631 | -8.0324 | -43.1022 | 2025-08-01 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 230.1 |
| 7d01ee6b-9610-36b0-827f-b9c6ff2f636c | -23.5446 | -47.8293 | 2025-08-01 00:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 4fcd18fa-e701-3276-8596-86f910d89d69 | -18.6708 | -52.5756 | 2025-08-01 00:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 145.2 |
| 33a0c4eb-088d-3251-a57f-c348c81f34e0 | -11.7666 | -44.9986 | 2025-08-01 00:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.2 |
| c4712d6c-913e-3150-9f19-8c0b865f848a | -6.7109 | -59.1731 | 2025-08-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 96bdb438-d077-35ec-ac59-8423a81cddbc | -6.7478 | -59.1716 | 2025-08-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| e0461886-5333-3efb-8a6a-0da764ac77ab | -8.0321 | -43.1257 | 2025-08-01 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 336.9 |
| e71487ac-8c82-3207-9ae2-02d34fa52a01 | -23.5029 | -47.8166 | 2025-08-01 00:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| 7ff2ccdd-9a2f-3033-9294-aa6635b8a424 | -8.051 | -43.1237 | 2025-08-01 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 233.9 |
| 7694d134-197b-3d3b-a96a-13eecd998e81 | -18.6904 | -52.594 | 2025-08-01 00:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f2b17368-1af1-34ef-bb59-ffc1af458f01 | -6.7294 | -59.1723 | 2025-08-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| e24fc7c5-cab0-3e48-ac9d-e13605c02f1e | -9.3989 | -45.4928 | 2025-08-01 00:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| eaa7a433-31a3-3b2b-b2fc-562724356f24 | -6.7293 | -59.1916 | 2025-08-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5b773f59-d8ad-3fe8-830b-1926cfc6b236 | -18.6908 | -52.5722 | 2025-08-01 00:30:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 0bd5a490-c7f4-326f-b37f-b8270cce0fba | -10.434 | -47.2601 | 2025-08-01 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 2e8ff203-94bf-3ff3-a7f5-b0ee62b6dc91 | -8.0513 | -43.1001 | 2025-08-01 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 208.1 |
| 9ffc19cf-bbaa-3d44-94bb-52778636b3ed | -6.5445 | -56.1915 | 2025-08-01 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 36a69305-d7b6-33e1-921e-4dd3d9779811 | -18.6704 | -52.5973 | 2025-08-01 00:30:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 7b0b022d-f71e-375e-a958-3968e6b01bb6 | -7.7444 | -45.0762 | 2025-08-01 00:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 586a64fd-4eb4-39ef-a0f3-497a4dc62edf | -6.7295 | -59.153 | 2025-08-01 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| dd2c45c4-56e3-32b4-903d-700893c9b4f9 | -23.5234 | -47.835 | 2025-08-01 00:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 315.7 |
| a6377abc-9ebc-36d5-b470-1675a46eed15 | -23.5022 | -47.8407 | 2025-08-01 00:30:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.8 |
| 6c147bd4-0381-3b1a-8512-cd4bf566e3f2 | -23.5226 | -47.859 | 2025-08-01 00:30:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| a03b94fc-2f30-3b0d-8e53-d80a19a29979 | -6.5443 | -56.2113 | 2025-08-01 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9c40be58-19b3-31e6-b9d9-4ed682219391 | -6.5074 | -56.213 | 2025-08-01 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| ae4d9fe8-c65f-3fbe-ab97-f0af2f058a57 | -7.7444 | -45.0762 | 2025-08-01 00:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| facf2cb2-5f33-338f-b75d-d0c860a38fb4 | -8.0513 | -43.1001 | 2025-08-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 251.7 |
| 8f57d56a-457d-3428-a024-35578cf5bf4e | -23.5242 | -47.8109 | 2025-08-01 00:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 137.7 |
| 7d95a39c-1be1-3c5a-b5f5-1b3a24b58948 | -18.6908 | -52.5722 | 2025-08-01 00:40:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 0137ac8b-8030-3c7e-9d2d-4fb2fde64054 | -18.6708 | -52.5756 | 2025-08-01 00:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 66081966-a400-350d-b61d-371757e30fbd | -18.6904 | -52.594 | 2025-08-01 00:40:00 | GOES-19 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 9a4d00cd-7d80-3d79-84ea-bc78335b229d | -8.051 | -43.1237 | 2025-08-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 379.9 |
| 05567915-e93d-370a-897a-1b5ac16ab243 | -8.0321 | -43.1257 | 2025-08-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 255.2 |
| f8043add-302d-3b2b-9faf-95bce4597b1b | -6.5258 | -56.2121 | 2025-08-01 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| fdcc1477-4056-3b8b-8cea-efe9ad847811 | -8.3394 | -50.5863 | 2025-08-01 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 85e21a0c-17d8-31dc-aea6-501c0b6a2398 | -8.3396 | -50.5652 | 2025-08-01 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 0574d017-8c52-375e-a88d-88b1ecc3fcf2 | -9.3989 | -45.4928 | 2025-08-01 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e967c9b3-936b-3b98-b7fa-ff1f70690772 | -23.5022 | -47.8407 | 2025-08-01 00:40:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.5 |
| 457d5b1a-629a-3aae-bd2f-79d9d9831824 | -6.8395 | -59.2643 | 2025-08-01 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 640fbe00-ec3f-3f97-880a-304f1f84d181 | -8.0324 | -43.1022 | 2025-08-01 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 2265fabe-a475-32c5-af8c-145ec499833c | -18.6704 | -52.5973 | 2025-08-01 00:40:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 4c5eb6f6-81af-342e-ba65-8bf699407f84 | -23.5234 | -47.835 | 2025-08-01 00:40:00 | GOES-19 | ALAMBARI | SÃO PAULO | Brasil | 3500758 | 35 | 33 | nan | nan | nan | Mata Atlântica | 378.9 |
| 480434d5-9f42-3625-a2e4-08f6f925c036 | -9.3989 | -45.4928 | 2025-08-01 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 5c81d093-fd8a-32bb-b61b-95aee45b2556 | -23.5022 | -47.8407 | 2025-08-01 00:50:00 | GOES-19 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.9 |
| d695e767-b9d7-3731-a7e8-efc1728ede6c | -9.629 | -63.422 | 2025-08-01 00:50:00 | GOES-19 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |


[Clique aqui para ver as próximas entradas](README4.md)
