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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81975f21-60ba-3f5c-ad26-c2e7dec89be1 | -14.65543 | -48.35251 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d813bcae-ccdb-3d52-99cd-345e463579e8 | -10.68086 | -49.27918 | 2025-10-05 03:55:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f3c1219-29eb-33f1-9cf0-8936eb0a24c3 | -11.01924 | -46.70801 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f64a42c7-f4f9-37b7-a8f7-24b61fa9d579 | -17.20205 | -44.45152 | 2025-10-05 03:55:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba77519c-da86-3957-98de-7481e98e6b55 | -11.23796 | -47.78968 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e1f7f75-ca23-31eb-bc16-6619b50e453f | -13.30261 | -47.79725 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4de92ce4-fd27-3acc-9b2a-2d8aed83b9e9 | -11.81436 | -45.06647 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76dabf25-649e-37e2-af58-9f13412ba1a1 | -12.92155 | -47.30799 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ddc31d1-f2c1-3ed1-a2f4-113f4efec333 | -14.69097 | -45.17382 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c9aea54-3367-34dd-b38d-013f78c98213 | -10.80362 | -48.82321 | 2025-10-05 03:55:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 708f431f-51e5-3617-a0a0-74f9fca86980 | -13.29121 | -47.62193 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61b0f131-54f0-3efe-93f0-fb0aac0a2510 | -16.36827 | -51.47393 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fecbec59-0557-3dc0-a702-635c2a98d9bc | -11.88975 | -44.97872 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4b0646a8-e22e-38fe-aa3d-f23bf5f838f2 | -11.82749 | -45.08888 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53a811c8-8b57-3116-83ad-0571a469c589 | -16.35204 | -51.46491 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f134334c-a043-3723-975a-62c761c1c9cb | -15.60025 | -52.50156 | 2025-10-05 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 84bace03-fafa-36bf-b0e3-b0ea60f80248 | -12.55554 | -48.16483 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 765cb7f0-7d63-32b0-bc69-95f85f3319aa | -10.84481 | -47.98405 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e204228-fa5c-3aca-be83-fcc03dc35fcb | -16.1241 | -47.30269 | 2025-10-05 03:55:00 | NOAA-20 | CABECEIRA GRANDE | MINAS GERAIS | Brasil | 3109451 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b15eae3-52b5-3daf-a2d4-cb66ef1bc451 | -11.4545 | -51.52014 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44c851d5-039a-3d02-943b-b3ff3c1d9d70 | -11.81639 | -46.85721 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bae45ae8-992e-37e4-b0cb-78c0c3847d19 | -16.07552 | -50.91454 | 2025-10-05 03:55:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8864256-da16-32f0-ae4a-28bd56812094 | -12.38423 | -44.45136 | 2025-10-05 03:55:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4be62772-52d3-3e2f-a427-5bf0dab925f2 | -15.1398 | -45.75312 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8cac2df4-a4a9-390e-8917-01c5f980050b | -11.81733 | -44.89231 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ca1bc97-732e-3fe9-9a49-b49cda401771 | -14.29798 | -45.86374 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc71b295-9111-3690-a6c1-f37185abb8e1 | -11.8073 | -46.84265 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 755bf79a-d095-39f5-b0e8-0c32a074a4af | -16.38115 | -52.16175 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c50b93c7-af51-3268-a426-2bb84f18719b | -15.21112 | -46.39013 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40b4f9f7-a7f7-38f9-9216-673b5ee00248 | -12.11063 | -50.89547 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fc6c5358-cb20-3a81-b1d4-00b5260e0d78 | -13.27329 | -47.61447 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5be43fa7-58a7-32ac-8ac3-f402d81eb50f | -15.2967 | -47.95608 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 079d3a0a-6b59-3376-8f86-5400d36433ab | -12.10318 | -43.45634 | 2025-10-05 03:55:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 374c2b6b-6b02-3ba1-9806-8b305bf25ad9 | -13.25607 | -47.81464 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b4ac84cb-1a63-3bd6-927c-4ebe5966da34 | -13.14551 | -50.92352 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 26164b24-a590-3549-9708-acd867223d3b | -11.1089 | -47.13868 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c13c813-b55e-3a13-a1a4-440a4e8f088f | -13.85316 | -43.98796 | 2025-10-05 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| def24eee-a903-3f10-9ac8-75979483c65a | -12.391 | -51.10859 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9702aa86-e889-3704-807e-59f5249384de | -14.74952 | -54.66676 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 07801907-d187-3baf-abce-100a3a553199 | -12.10307 | -50.89665 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 256a6d06-a5ae-3468-a497-6dcc17f15368 | -15.1186 | -45.75298 | 2025-10-05 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e3a06d0-dfdc-3a07-b700-9a8ec3dd9106 | -16.33937 | -51.46759 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0bb75f10-f133-3798-a078-7246f6f6cdbe | -13.13846 | -47.98167 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c78be518-ba3f-3c7c-882a-cec1688b52a2 | -13.05599 | -44.93359 | 2025-10-05 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2c186eb-e300-38aa-afbf-fd6ae95990af | -14.23763 | -43.11768 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a9e678b-91bc-3ae5-b5f5-b74601dbc108 | -13.2625 | -47.61913 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7f5eaf8d-153a-3203-8b36-30055a2f3bb9 | -12.45528 | -44.73458 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 704e76fa-9e61-355c-a187-946df2ae28e0 | -11.10713 | -47.88218 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99c0f000-5dc6-35b6-b58d-9afdcea9ff99 | -13.71923 | -48.10315 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cabdb74-54f8-3ad3-8c4d-40ddf98123ce | -13.95242 | -43.07056 | 2025-10-05 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 103dd88e-9345-3161-a1f5-cfa53e74098b | -10.7401 | -47.8956 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5d6bdbb-6022-3504-8e8b-ce3331e92a5f | -10.54113 | -47.80033 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7375b484-7a5a-3e7e-bdcc-b8a1dfe101fe | -12.92005 | -47.31056 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78aba3ed-21e2-3281-a48d-e811c2de0232 | -14.19692 | -46.68017 | 2025-10-05 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03ffec20-ee54-3de2-a7ed-928c27318f5d | -15.30564 | -47.32581 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0b375996-7e29-3c38-a5a7-58039aa3119a | -13.9753 | -48.12134 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e30b707c-2483-3f8d-b70f-b2830547214d | -12.59242 | -48.16289 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71a56dd0-2a0e-3dd3-9f80-41fc37238b26 | -11.44982 | -51.522 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e523d8d9-79ed-332a-8246-4302a635dd93 | -16.00981 | -50.84989 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1565448-0b12-37ef-b3fb-7ec94ad2c044 | -13.29862 | -48.09136 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fac720c3-b51c-3104-be56-6f2c5ce12593 | -12.82208 | -46.86129 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48b3cab0-7b59-3e64-98b3-a2e2dff6e17e | -13.68881 | -48.04936 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3a30f7aa-d41e-3bff-b102-59eb8a53bbd9 | -13.27634 | -47.59807 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a5fc4c7f-a46c-3c9b-9f44-fb8d7f11dc71 | -13.48253 | -47.26631 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f9580d-34a3-36be-a9ef-c898e7a2befa | -11.09633 | -47.7501 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b3c8b36-76c2-3083-9c60-1f823d4fa705 | -14.3297 | -52.97732 | 2025-10-05 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c658a449-b116-36f8-8dde-da6f0fbf37cb | -14.68009 | -49.61006 | 2025-10-05 03:55:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9110f066-3b38-33d8-aae5-3e616f0f0561 | -15.29742 | -46.32227 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1268e78-8c99-3021-8915-a8e54c6b7d14 | -16.36355 | -51.46765 | 2025-10-05 03:55:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1416ede0-5da6-3034-9abb-677ce1204723 | -17.72837 | -44.40496 | 2025-10-05 03:55:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54236ed5-d8b2-3833-87dd-93c23a1fb456 | -12.60239 | -48.13778 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8df6650f-d94e-30cf-8e0d-80c09d92544a | -12.94184 | -51.01701 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f08e2916-cad7-3984-a8d6-3bfd8554045f | -15.53813 | -46.80313 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a23628d2-a79f-3d77-ad6a-c7d455832e43 | -12.823 | -46.85631 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48962831-2e65-34ab-94b0-ec7478b62cfb | -13.28981 | -47.57888 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef51938a-e34c-3935-9cac-cd1a1eef386f | -12.58791 | -48.13186 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cd45d82-426b-314e-870c-e1538bcfca7e | -11.52836 | -47.67096 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fb433520-7166-30fc-b4f4-39088f86b0af | -11.07061 | -47.90855 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4df8639e-771a-3bf9-acee-3f2770088b6d | -11.54123 | -47.68776 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6bb66c4-8d70-3b1e-aabf-0c30ba8a4810 | -11.90536 | -46.22853 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6e88579c-5646-367b-b85a-3ba3944d2446 | -11.79977 | -46.81707 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb2ba515-4116-3b80-ba45-3645d5451947 | -14.19774 | -46.67567 | 2025-10-05 03:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9fe08370-ba61-35cf-855b-2ce8a2aceb00 | -13.20438 | -48.53084 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dee47ae6-293b-3e7d-971a-7f649ee2694c | -16.34674 | -47.06143 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a002906-de44-34cd-8d8f-b2de98e67ec3 | -13.30191 | -48.09686 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b6bc9051-e1d6-3da0-b57d-1488f574eab5 | -13.6433 | -47.2978 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c1e2ba1-e820-3796-968d-50ece5b14ec7 | -13.73014 | -48.08156 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f70c8ec2-977c-381c-bce6-55690151e3c1 | -10.94378 | -47.06659 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b171ff52-1e30-3a77-9b71-ef787dc6b7f9 | -13.83856 | -48.04528 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2847dece-86ef-35e5-ac03-f6bff193a257 | -11.52227 | -47.67617 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ec3a50f8-9b6f-34c0-afef-e6a71082678d | -12.60633 | -48.11698 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8de46c80-d918-3fb5-b5c1-c7dfa1726d5a | -11.10561 | -49.86327 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b8747d64-7993-343d-8a50-c7e074676e40 | -13.50239 | -47.2891 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cbc8b67c-189a-30e5-a470-6c93209c634b | -11.09575 | -47.75328 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66746105-b1c3-3c34-b98a-a36173229457 | -14.90871 | -46.87187 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b3f322e-6029-364e-aa53-0c2a272c0024 | -11.53347 | -47.23472 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26ce136f-e1c0-3413-b0c2-9a8167bed65f | -13.35412 | -47.57772 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16cbf624-68b1-3da1-9546-a43176512d30 | -13.36228 | -47.69297 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1ff21204-16e7-3d99-8928-3fa87eb0c2dd | -11.81007 | -46.85413 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06c8272b-3c7a-30a4-9a47-02a4ff29252f | -14.65238 | -48.33217 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README64.md)
