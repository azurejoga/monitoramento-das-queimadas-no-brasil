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
| 450abb95-4d7c-3f8f-bffb-b5af7823b100 | -6.12587 | -43.48575 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 41c85e43-5ac2-3126-853e-09cf33240693 | -6.83137 | -44.82609 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a65b7d71-f10b-3c0d-96d2-1773e1535452 | -7.89571 | -44.59825 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3ba9240-df54-3693-82ef-261e6940e018 | -8.16226 | -46.39193 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a521c95-73e7-31db-b1cb-0ed14cc2d7b0 | -15.18805 | -48.47676 | 2025-09-29 03:47:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18dc080b-8bbf-3e35-a768-c2200d564e08 | -11.99415 | -47.09665 | 2025-09-29 03:47:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dfc52e6-f946-3dad-9811-04dbfc4b4cae | -11.43626 | -44.9579 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 167d0801-389f-3352-a443-a5d86204b4c4 | -7.56727 | -42.40632 | 2025-09-29 03:47:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a70a917d-4b19-3465-89fe-83b8cf8ef927 | -15.33558 | -47.91864 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ae214c2-c630-3d91-bab7-774bc52e43b2 | -9.63967 | -48.12738 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 866a0a44-a3f7-3b15-b445-70dfd0c59195 | -7.58795 | -44.77439 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89dd3153-c9aa-389e-a5c2-75ee5e4483ad | -6.26507 | -43.63263 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cd5e1ec-bb0b-3d77-8eec-f455e9846390 | -11.67079 | -45.34983 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ddb6808-14ea-3edf-8b13-b75037a3e593 | -10.28797 | -45.1968 | 2025-09-29 03:47:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cadde2f-483f-3e76-b9f2-dcb1fd179e80 | -6.82479 | -44.83082 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59a42190-1295-3050-a36e-1eb051a615dd | -11.93285 | -48.02323 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 96b172ec-971a-3b94-9183-050972772362 | -6.15177 | -43.88581 | 2025-09-29 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cc73e7fc-813d-3c2a-ad52-e77d4506c893 | -6.49704 | -44.24987 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 522de91f-cb74-3cae-a4c5-4d7bfe03f167 | -6.42508 | -43.51076 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8425ea4f-69c8-310c-bc9b-a43760fbb888 | -11.43413 | -44.95537 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9182013f-4728-3643-a9e7-5d898f05e31f | -8.3025 | -45.44046 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3970c7ad-1fac-31c9-a9bc-8dc2a4598362 | -20.05898 | -41.33219 | 2025-09-29 03:47:00 | NPP-375D | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 27.7 |
| a628ff9e-5974-35c1-acee-e850679326dd | -17.72005 | -46.6901 | 2025-09-29 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8e29888-28b7-3543-9db8-352b531bb8ef | -5.81641 | -42.82183 | 2025-09-29 03:47:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b9a8b6f7-0a7f-3703-a1fe-850b521efd52 | -15.53624 | -47.87687 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e588ceb-a265-3a9d-bb29-97ad8409c09a | -8.26526 | -45.48689 | 2025-09-29 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7b999cf-ad88-3722-b57b-db3b6f1c607f | -11.51182 | -44.85054 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 572c2e41-9a93-30f5-9644-2b7e475070f0 | -15.54201 | -47.87768 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d3f5dc9-0b6c-372f-abc6-ef92d9f1980e | -11.92301 | -48.04469 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc7cfab6-c460-3fd6-8c9a-a2fc91bc88a0 | -6.13551 | -42.65026 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cdccee8f-2504-3b88-be2c-350f4cb66659 | -7.31367 | -44.72164 | 2025-09-29 03:47:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ff23dee-7f2c-37ee-9b94-34ed8b33a91c | -11.36781 | -45.06963 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12078bfd-ab94-396b-86ca-43b78533dcb3 | -15.28825 | -49.51617 | 2025-09-29 03:47:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 9ccf99fb-bac4-3fb3-9fc6-d5dde239740d | -6.11736 | -43.47486 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c4f858cd-edc0-3bd7-93f3-93399765402f | -11.40977 | -44.90208 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11240bd6-e859-3e9e-a07d-5dd063d4160e | -6.57561 | -43.40609 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 5.6 |
| ae4cccdb-a4a8-39cb-9488-4c588ab38339 | -15.52431 | -47.93386 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba80d679-53e2-39e1-9d42-8c0ea25274aa | -6.06262 | -42.47088 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 802a5330-93fb-3002-b55d-692465b02007 | -6.13939 | -42.65182 | 2025-09-29 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aefa54ec-c4b2-3a09-8fe5-40c2350bd630 | -7.37952 | -47.04376 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc6f9321-52e3-3b70-9379-b8d80e3a71f6 | -8.71653 | -50.05976 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c6c54ae5-b14e-395c-8a0d-7ea08a5aeb62 | -11.44544 | -44.97897 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e128149-73e2-3713-8a06-a6b502dc58fc | -6.06651 | -42.4767 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 20e06f8c-2efe-3981-8e84-077b9a26e940 | -6.57163 | -43.42868 | 2025-09-29 03:47:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0b1f8bac-02a5-3066-8e98-1aecd0bc2777 | -15.50594 | -45.88039 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 68f26171-227c-3ccb-b023-3bf6460971a1 | -11.45005 | -44.98249 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2e4add2-caf1-3d9c-9451-6f97f3b95ace | -6.11602 | -41.81779 | 2025-09-29 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df8d162a-a770-35b6-a7e0-1c421916072f | -9.46673 | -45.50608 | 2025-09-29 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79e42443-28a9-318d-b862-2ade83664f12 | -6.61243 | -44.94205 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6781c9c3-e0a1-305a-a854-a6355ba2dbe2 | -6.21703 | -44.21665 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19560f58-9457-33ba-b3b4-c3872c39423b | -19.06333 | -45.79272 | 2025-09-29 03:47:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85a7175f-eb0a-31c9-a95e-8d23e3e19615 | -6.36509 | -43.9264 | 2025-09-29 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d0ce256-689a-373e-a06d-f84bc0716e44 | -10.92199 | -45.71978 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9243d83b-0609-3525-971c-eeaf24cc4699 | -8.78321 | -44.94835 | 2025-09-29 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fdbd823-c815-324f-8b4e-535f2e5a3707 | -8.71243 | -47.98256 | 2025-09-29 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e1cfd7b-e176-3790-89aa-799acaae3fbf | -15.28349 | -49.49625 | 2025-09-29 03:47:00 | NPP-375D | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e795e24-6477-3083-a9e4-2fa3f5e6492c | -12.66557 | -46.90632 | 2025-09-29 03:47:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b3f1be5-12a9-3859-b73e-ff8c5e7b5eb7 | -7.03204 | -45.18622 | 2025-09-29 03:47:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4087255a-eee0-30a2-afa3-ae85f06fa549 | -6.42051 | -43.00603 | 2025-09-29 03:47:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cb8b57f3-ea74-3db9-98d9-91a890e88233 | -15.08824 | -48.3372 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0ae49b7-2f1d-3a9b-b85b-9540e60f4e84 | -6.11233 | -43.45265 | 2025-09-29 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7501d90d-bee6-39b5-8ee5-4153e95253c0 | -6.62432 | -45.9001 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37cdb84a-0a58-3f82-be1f-b839698e5306 | -6.46493 | -43.94093 | 2025-09-29 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98aacd25-bb1d-3972-903c-3224f8e0e636 | -6.62576 | -44.96309 | 2025-09-29 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 094cdb29-0e34-32a6-bafc-131d1dc70f87 | -11.43624 | -43.5079 | 2025-09-29 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7bb4d25-8784-352d-850e-571e21e66dc9 | -15.50095 | -45.87922 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24875329-bb21-37f7-8891-dff3a5ae72d7 | -15.08022 | -48.33265 | 2025-09-29 03:47:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fa90b141-bf0c-3bfd-ae87-d7f9c246a9df | -6.06094 | -42.48087 | 2025-09-29 03:47:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 858803ce-2ec7-34de-a483-58bb9b9c34db | -15.61053 | -46.25222 | 2025-09-29 03:47:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19a3b28e-a4a0-30ae-b7f5-61ff873d8611 | -9.31325 | -45.69113 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 67729ea1-e5cd-3101-8295-1ab2e1922028 | -7.59152 | -44.7734 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b0aab1a-1e4c-3bd7-b5dc-7da845c0bcce | -19.77839 | -42.25819 | 2025-09-29 03:47:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73d3b611-3037-3aa5-8254-c1315a0e986d | -9.30982 | -45.70951 | 2025-09-29 03:47:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 992684ba-5ffe-3c04-93e2-205e444c2e5b | -7.58035 | -44.8051 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa493c48-ef77-3fb6-af1c-b69e89dddf62 | -16.48664 | -46.03441 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1100ecc5-7502-3181-b0f2-8e54470e6f09 | -11.9295 | -48.07098 | 2025-09-29 03:47:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bec07fe2-56ca-3ce3-b56b-083420df485b | -17.08892 | -48.57071 | 2025-09-29 03:47:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5a042574-940e-39cc-b8d2-c5f8434a0cc7 | -6.82593 | -44.82496 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cae80acf-37e5-37f3-920d-894ff8ae419c | -5.91147 | -45.8541 | 2025-09-29 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e2799f6d-6ec8-36c8-9929-1f9e645487e8 | -7.22987 | -44.77806 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a6bf01f9-29ac-3036-b35c-596716b315a6 | -16.49655 | -46.03668 | 2025-09-29 03:47:00 | NPP-375D | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51fb10a0-ce0a-3c88-be78-9e32ca4131e6 | -9.6343 | -48.12157 | 2025-09-29 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 355dba1a-1d36-3b56-91ed-9de4c17bb1b5 | -7.58575 | -44.80604 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a96db5ff-9952-3a3d-9904-f87cb51bd448 | -7.80912 | -46.89225 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a0762d96-3a72-3116-bd6b-540739dd9fdd | -7.38373 | -47.04204 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c4f50bc-3be0-3f3f-9527-000c097a92ef | -9.77271 | -46.20183 | 2025-09-29 03:47:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d8ed9150-dc4e-3272-8207-10f758f59bc8 | -9.0492 | -46.70497 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3e8e3d3-46a7-305d-b7ab-201efa03f890 | -15.27913 | -47.87435 | 2025-09-29 03:47:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f915641-9f81-30f0-a274-6c6bf42c9271 | -17.94724 | -40.20293 | 2025-09-29 03:47:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d0879b13-2d8f-3daf-b54f-dc99d8f3b823 | -7.89349 | -44.61058 | 2025-09-29 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f467a4f0-788f-3e1b-84bc-e4628e24b84f | -11.8032 | -44.90887 | 2025-09-29 03:47:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef7d0b7a-c0c4-32f8-afb8-abbabcfff6ef | -9.05284 | -46.70592 | 2025-09-29 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad229399-8f0f-3556-9437-e2e929b6d77c | -9.07769 | -47.60912 | 2025-09-29 03:47:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 447e21d0-677c-3cc0-8b1c-99d5057249b6 | -6.65105 | -41.39536 | 2025-09-29 03:47:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d31fa9a-1e4f-37db-8dec-9a69fe18773e | -15.5195 | -47.92838 | 2025-09-29 03:47:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5af20b11-3959-30b8-995c-e7d87004d0af | -7.02066 | -44.77858 | 2025-09-29 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e467e0a6-f3ae-35cc-aff6-c44099426118 | -15.91097 | -46.20484 | 2025-09-29 03:47:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6909dba7-f38a-3be4-8517-42978e32edc8 | -11.98309 | -46.58656 | 2025-09-29 03:47:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee7a2718-660c-3347-bd32-deb3ac40278c | -11.35695 | -45.07078 | 2025-09-29 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fafc6ffa-125c-32a7-8fc7-b5b31c7c895c | -7.38041 | -47.03889 | 2025-09-29 03:47:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README12.md)
