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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8c52acd-b628-3da0-bae6-3df5365cff82 | -9.32294 | -49.80436 | 2025-10-07 04:36:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d178cf7-ce06-35b5-a02c-a3dace1d5db3 | -6.70419 | -42.18735 | 2025-10-07 04:36:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7774564e-c1cf-35f1-a8e9-a232ff193b44 | -6.5869 | -44.63018 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0620f226-c18f-3b68-86ef-18b6af21c701 | -8.8663 | -46.78779 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 8a8e4855-8754-3b73-a3fb-b6f49c924901 | -4.83108 | -45.4132 | 2025-10-07 04:36:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00b83b59-b28f-3941-97a6-738f6ea95690 | -5.03505 | -45.55928 | 2025-10-07 04:36:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8a48173-fa38-3ced-8bbf-5017c9c7040a | -10.25404 | -44.37948 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34237d73-9a23-3f2f-899f-d29f6cf19bf7 | -9.78835 | -48.28365 | 2025-10-07 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f36b7f07-b5cf-3dda-9950-2d88926d3fda | -10.26392 | -44.36599 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68949ed3-1b93-3631-bb91-f481200cedd2 | -8.20639 | -44.15019 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fd988d6-9839-3500-9516-1754922e7c8e | -6.96843 | -41.99997 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a1fe0e2b-c7f1-3ca9-93b4-6ff46cc7e3dc | -8.18107 | -50.29976 | 2025-10-07 04:36:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d994754e-2dfb-313a-a9c4-9367dfae545d | -10.22953 | -48.18776 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 508387b9-aed9-32dd-be1f-74c82cfda9b1 | -9.51589 | -51.36239 | 2025-10-07 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c305fef0-727c-3e9d-b97f-fca4257f71d4 | -6.16173 | -42.58957 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f7f2b0ea-f8d5-30bd-8b64-df84833bab53 | -7.88652 | -47.81767 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d986204c-4097-33e0-bef9-ce412a749eeb | -5.70007 | -44.82553 | 2025-10-07 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c4f8084-41fd-3392-9844-77890f061bfd | -4.69486 | -45.8424 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0665311-f616-3ef0-9621-8054a104b2b1 | -8.60139 | -44.91501 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b31eb875-0e51-3f1d-9775-523a621bef56 | -6.9448 | -42.07108 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c6dfebd7-5da4-3f6c-a5c3-203b3feb0eb4 | -8.41272 | -50.69707 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 85b55843-e789-34c7-9fd4-6a4120a5e9f8 | -10.25722 | -44.38494 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36bd7d66-45a4-3de2-a03c-abb019367f56 | -9.91944 | -49.96379 | 2025-10-07 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3f13ed5-9102-3eee-9064-ba81db920dec | -5.39152 | -40.98096 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 745944b6-dca9-3360-aa93-7b645df481da | -9.01801 | -50.68593 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de5887ad-49a7-359c-b8ec-9ec4333d1926 | -5.76609 | -45.74866 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d107ee04-4daa-3e41-848d-71118223c975 | -7.46504 | -43.09552 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc4d8901-22c5-34cf-8dfd-38df88cf99d6 | -4.91206 | -48.01727 | 2025-10-07 04:36:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3497165-ad0c-3e9a-9b9c-226407c68e3f | -10.84699 | -44.16349 | 2025-10-07 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27b405cc-739e-3237-986a-605b4014840c | -6.28639 | -42.94439 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0fd6ca1-4e28-390f-897e-302505b54a06 | -7.51761 | -49.90717 | 2025-10-07 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e890867-34b4-35b3-9d37-5c535556303a | -8.56223 | -50.08208 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8344e14d-ca00-31cd-aec0-8ee70f224ecf | -5.25141 | -46.56802 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1db0e20a-5b7b-3c5e-8b9d-22f1b28be942 | -6.98995 | -42.86084 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd01c5d6-3d40-36ab-9c21-e66764cd9eaa | -7.02161 | -42.75739 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b0a6271f-7ead-387d-8ec3-8a64a79c6faf | -8.9371 | -49.86074 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 222ed84b-8961-327a-ace5-d0bb8efbd515 | -6.72069 | -42.80714 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64565a93-b15a-3af5-afd2-482ca76e3612 | -5.57301 | -43.57087 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f93cc04-506e-373c-936d-3c1e4e48aede | -5.74264 | -49.13251 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 818c0f4c-b514-3031-9958-36741d10906b | -5.49374 | -43.06955 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| eb0e93f3-e962-3cc1-9caf-b0b7c6e44f74 | -10.92957 | -44.25553 | 2025-10-07 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1f7d180-6c4d-3dec-8e53-2f4f574911f8 | -5.71317 | -44.83577 | 2025-10-07 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2dcd580e-571b-37a5-98b1-2ebd7e55ac67 | -9.67473 | -45.66986 | 2025-10-07 04:36:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9dc04c1-1280-39f3-8dd4-5f2b6ac8dd6f | -8.61114 | -44.9254 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1c6a4a4-a27c-3aaa-94ea-14d6fed44f3d | -9.32624 | -45.9966 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63f8d40a-953d-370a-9882-a76f77af5d47 | -7.25402 | -46.9756 | 2025-10-07 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f28bf256-2537-3426-afd3-fd275c1faa53 | -6.71713 | -42.80295 | 2025-10-07 04:36:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 529e1808-919a-3f07-b84f-b2db256561c3 | -8.61549 | -44.9216 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9db62cc5-309c-3231-bb0d-3f71808882e1 | -5.41572 | -41.07314 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7f0d2990-e4f0-3d8a-8dfa-0d3f247ff811 | -8.41208 | -50.70101 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 584e0a3f-db39-304a-ae93-72783a38abe5 | -8.96852 | -50.80489 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a329f398-477a-3039-99de-0586f3c5d3fb | -6.72354 | -42.84444 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ef16981-4afe-397e-bdfe-e11009ee3c0a | -8.61362 | -54.96428 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e9e0005-caf7-3dc6-ad07-d4923be53ca1 | -7.89428 | -47.81173 | 2025-10-07 04:36:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a78e1e55-b13c-3f51-8782-75614451982b | -7.63071 | -43.06428 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0305f5f9-2660-3efa-9c08-141324d5401c | -9.02831 | -50.59041 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8277c3ad-a89e-3c48-a78c-c794a0148687 | -10.02276 | -48.29971 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1cfcfb1-121a-3133-8c7d-21a3460ffdab | -7.68511 | -42.59588 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bd6be091-6b8e-393e-bc98-60159ef8b5e5 | -7.06178 | -42.77062 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ddba2ad-4577-32fb-9709-d25b0785642d | -9.04575 | -50.69062 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08626990-0773-358a-b967-1e20ac5c22b4 | -6.32658 | -38.5241 | 2025-10-07 04:36:00 | NPP-375D | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f04e78d5-49a5-3c61-842f-cec1425d87a8 | -4.68461 | -45.84089 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7ffbcbf0-99c7-3229-89a2-2d5726a35daf | -6.37223 | -46.42766 | 2025-10-07 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0511a1d-adfb-374e-862a-e27691143f10 | -6.45775 | -42.79842 | 2025-10-07 04:36:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cafd5b0-96c0-3365-95c1-3010f59f0ceb | -9.04069 | -50.59195 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bac84c9f-5550-31ae-a1bc-482b4c387551 | -6.52833 | -42.4779 | 2025-10-07 04:36:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b7b0fe30-eb43-3ce8-9022-b37e0351338e | -8.06307 | -48.48232 | 2025-10-07 04:36:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86fbf2f6-6ea5-3a93-b1c5-170d7620390d | -10.26463 | -44.36107 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe019290-8059-3fb9-8193-c9656154fd8f | -6.71379 | -42.85406 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 6edefb5e-fdd8-3edf-932d-29887d5daf32 | -7.69787 | -42.39138 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1295715b-2b5a-3e81-a999-715f654f17bd | -8.49397 | -46.33092 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d40a99f6-41cb-3db2-b24a-304ef1b2b6f3 | -7.69611 | -42.40324 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d83b1584-2680-3c4c-b0f9-d7afeed3fe6b | -7.99028 | -49.73084 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1d340cb-e6df-34d9-ba4a-7377553c2ff5 | -8.63044 | -51.08126 | 2025-10-07 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69729656-00dc-3a7b-9cdb-c681a04ce293 | -4.69316 | -48.6226 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0aa05a6-db70-3745-a94b-463e94ea4755 | -6.36885 | -42.8652 | 2025-10-07 04:36:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 681a8f87-2c1e-3cc6-be02-dedcf6c567a9 | -9.31898 | -49.80741 | 2025-10-07 04:36:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700f0496-b4d5-3755-a430-46c87b901365 | -4.14381 | -47.66107 | 2025-10-07 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 959aa0f8-04bb-36ff-8405-9ca5ac67e968 | -7.73589 | -42.39138 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 010f4a44-2b80-355e-be0f-d8ecc4cc5a11 | -4.69144 | -45.8419 | 2025-10-07 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 7ad1575b-a07f-3470-b2d1-bcde95ee2274 | -9.61669 | -48.60141 | 2025-10-07 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfffe747-0085-3bb2-8f74-770f822bf33b | -8.58051 | -46.23845 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4db93d1-d88a-34b7-ab88-4dfdfef3d43f | -8.60508 | -44.91557 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b2a0b43-d9b3-3ff2-8515-13890702da78 | -8.86541 | -50.88487 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78d427e5-512f-385e-92ef-279953f0c838 | -7.68221 | -42.409 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c5613b65-75d6-38f6-86aa-6b785d006436 | -8.58419 | -44.33828 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc726df5-3fee-3353-a551-6c5c02a5f996 | -8.20719 | -44.19866 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f89f4a0c-af6f-39f5-badf-620dbba1fa38 | -5.73868 | -49.13557 | 2025-10-07 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 05751269-fc97-318d-9443-f81e4fa6f802 | -10.26958 | -44.38183 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7f53c52-38bb-36a9-9261-4810ed916c0f | -4.87083 | -50.89598 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4b3b162-9ff6-3f27-9b78-acdc77c2c9bf | -8.7345 | -49.48841 | 2025-10-07 04:36:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a6b65b6-13e8-33a0-b92c-2435574caabf | -7.46098 | -43.09491 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 615d8a1f-8277-3697-9381-3f96fc326195 | -5.95664 | -44.34228 | 2025-10-07 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ddbc314-4792-38a9-b960-08328ff8e310 | -6.71999 | -42.84029 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9462cd51-6f25-3c7f-9ef9-d23604ce8a8c | -6.15707 | -42.59252 | 2025-10-07 04:36:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 47c0d734-800b-3c81-8c3f-e1e14fabe191 | -8.64779 | -47.16367 | 2025-10-07 04:36:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a1592dc-470e-30bd-ad17-cbf3284bf09b | -6.6979 | -42.84876 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1f199e18-75d9-33a0-ab8d-e50f7b99d6ee | -8.74234 | -50.66662 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc2b728-83f8-353d-abed-1a86a9839f41 | -6.21928 | -44.33379 | 2025-10-07 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 315b3188-5351-3faf-8d12-5c06c212fee8 | -10.26321 | -44.37092 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README53.md)
