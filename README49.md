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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32f8edfa-ee62-34fc-80c3-6330cbf6fc66 | -10.4146 | -53.7769 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 867b7748-cb8e-31df-a087-2efaee74fd6e | -12.63496 | -47.25664 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a743e66-e924-3b83-a86c-558db8a980a4 | -12.0114 | -50.93893 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca762992-a156-396b-8797-fad0351d3105 | -14.12147 | -46.28977 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6fde6e5-2509-3ca5-a17b-730b77da2583 | -12.7367 | -47.26999 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 438d4853-05ed-31e9-a700-a39ab9b23e37 | -11.43016 | -43.4592 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c8265ba-91a6-30a5-8ce8-2152e91debff | -12.01243 | -50.97532 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7778e99-ec81-367b-869c-fe8f0543793b | -12.00945 | -50.9351 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7033ce0b-f90e-3cd4-bc40-aaa9cb4e26d9 | -7.47833 | -45.81714 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 778b9d9d-523f-3679-9a61-1baa782ca477 | -8.24815 | -45.44926 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 94146b9f-56cc-3837-bb67-e8ef1d531267 | -6.51941 | -54.95759 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c11d9646-a2ac-395b-a259-9061dfc5a1cb | -12.90309 | -52.04782 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7940309a-b737-3fb3-a488-94d11f432dda | -13.52774 | -46.90238 | 2026-09-29 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee856862-d81f-3b13-b1b0-da3f6c0ae219 | -8.24605 | -45.46355 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7516d3a9-bc84-3ded-bdfc-da5cbba26859 | -12.90704 | -52.04476 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 537a24ca-3ced-3f6d-8c03-88fafc48318f | -11.93452 | -50.91188 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60ef528b-c348-37b5-8163-7c35a75a3ccd | -10.81869 | -48.73972 | 2026-09-29 04:51:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f3c418b-38e3-3710-bdd4-762477ece149 | -11.99986 | -50.99517 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ec1d19e-52b2-3ee4-ba7e-6d7d3d897169 | -10.78284 | -48.74544 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44865907-3179-31ef-a6a7-f291540c0521 | -11.17849 | -44.80214 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 596389cb-8769-3502-9be2-080cc182bf3d | -11.9667 | -50.92443 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 213c9c98-491f-31bf-95f3-12fc54000833 | -12.7185 | -46.99833 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16280e01-d81f-302a-aabb-41788881b524 | -9.77053 | -44.82607 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af57d323-ab31-31b7-88e6-92e2a920bef3 | -12.01972 | -50.95111 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6aec7e8-37a6-30a4-8f2e-081b22ff9e6e | -11.95891 | -50.9304 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea0c7703-b5d3-398c-81af-5a5605227d8d | -11.42347 | -43.43838 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9d666ad0-69ba-39a8-9053-8b48b8bc3abf | -12.01406 | -50.98648 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8986bf20-5617-30b4-b602-d59615bf4884 | -11.82898 | -55.21643 | 2026-09-29 04:51:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fb3103e-8b02-3d43-af80-e3ac13b9da2d | -12.55676 | -47.15586 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 734a282c-5dca-315f-8b7b-2620b886d5b6 | -11.43814 | -43.47025 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05cbdc5f-429b-3647-9405-559f8e80cc9c | -11.3478 | -54.04602 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f424145-3637-3786-93ac-bf5437373979 | -8.8549 | -49.88077 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 49b88f55-07d2-3c94-b5ad-4d6b3b83d8d6 | -7.89369 | -54.7264 | 2026-09-29 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 809c17e7-95d6-39ba-825e-c778491266c0 | -11.3634 | -47.43705 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5838111-6925-3574-854b-5178fe53cc8b | -12.01796 | -50.98349 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14bdb833-bd5a-3168-9fbf-e7bb358faa5f | -6.13886 | -53.05931 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0548347-fbe7-3de7-8b51-3023eed6eb5c | -13.08905 | -47.43497 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb0729f-cad3-3d2a-ab41-4565309a0ced | -11.35368 | -54.05614 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 068b6581-1712-3cbd-9af1-7501ced5a5df | -9.07217 | -49.87582 | 2026-09-29 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85445dca-3218-3397-987f-e01f727d26ee | -11.18017 | -44.79025 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 8857b1c0-2ff5-3595-af6d-a499db3031ee | -7.56825 | -47.3693 | 2026-09-29 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33e222cd-ad65-3a92-9985-3f871a75ae98 | -10.42347 | -53.8367 | 2026-09-29 04:51:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60451875-daa9-3706-8461-c5c901e3bfab | -7.76346 | -50.12837 | 2026-09-29 04:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ec6cb2a-4f47-316d-8bff-f430d8e1bac9 | -13.48595 | -48.60425 | 2026-09-29 04:51:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 305bb45c-5b6f-3ed1-9bfd-b72cfbf6e196 | -10.79705 | -48.74401 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57dcae73-b992-332e-ad6f-ef0f15f35c46 | -6.15886 | -52.91268 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5fc9c39-a4ad-3f69-abe0-4043afc8e0c7 | -11.07318 | -48.8989 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9ac3f56-4c80-37f0-87f9-53ce63101b20 | -11.86918 | -47.10072 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46915bcd-a3f9-33b9-9acb-2465b29aeef6 | -11.62843 | -46.79758 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82bb67ee-9e78-35d7-bb2c-168aa69a9032 | -13.17186 | -48.56281 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db8d3b4e-0338-3f81-ac44-ffc93a4d9727 | -11.50255 | -47.40122 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7823b78f-dd95-3df7-be51-64250967e5b2 | -7.53849 | -47.11758 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb688a23-8bbf-3b14-98cd-f03575a7b0da | -11.44742 | -43.4715 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 39687653-a04a-3e4f-b8f4-f20900156e6e | -8.02967 | -43.33798 | 2026-09-29 04:51:00 | NPP-375D | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 60b69088-908a-3aa6-9487-f972b81da64c | -12.44291 | -48.21655 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a14c472a-4f6f-3b9a-9e2e-a539f3af95a6 | -12.76721 | -52.81471 | 2026-09-29 04:51:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7709e709-61cc-3f36-87d7-5d535231c9a2 | -11.19107 | -50.05299 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa4db085-e27d-3733-ad7c-0addf60103be | -12.04641 | -50.9338 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23a472e0-0ec3-3984-8093-8c018f40e61e | -12.00181 | -50.99898 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83fdf138-6e00-353b-92e1-dfba8d5d1bd6 | -11.34532 | -47.33246 | 2026-09-29 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ca85464-4086-3fa7-be06-b116f49b0e02 | -11.36622 | -54.04926 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd22d6cf-6aa3-373a-9fc0-1e1999577770 | -9.78229 | -48.22348 | 2026-09-29 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7b6eae2-9e28-3b5d-b638-49721e7f3ba4 | -12.1538 | -50.4073 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dba94ac-6e8e-3d3a-bae2-e93f75e56bf0 | -6.15958 | -52.90825 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 962f998a-9d5f-373f-bc2d-4b3006ba3c01 | -11.40952 | -43.43649 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed37636c-9c31-353a-a924-72fdab7f613e | -8.35639 | -45.39269 | 2026-09-29 04:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0c9009e-5dc0-30b6-b04e-429335ca51f3 | -7.47901 | -45.81268 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 917d7609-0700-3eed-9aeb-f39729137b09 | -10.79193 | -48.75457 | 2026-09-29 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e2baa66d-5c5f-3a5d-a04a-fa8a52c1a9b6 | -13.18058 | -48.55234 | 2026-09-29 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f84b77e4-10db-31d7-9fc4-b0982672d8bc | -6.15144 | -52.91146 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0afb6635-4065-31be-8fe5-b85523caa281 | -9.80426 | -49.28122 | 2026-09-29 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6185c527-9d27-36f5-9e5e-e34f506358d7 | -9.96689 | -50.12352 | 2026-09-29 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 979b958f-9c6c-3f1e-9f6b-bb545658be02 | -11.19775 | -50.05406 | 2026-09-29 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dab49b99-ecf3-37fd-8893-02e20b793e9c | -12.16258 | -50.81827 | 2026-09-29 04:51:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe218a6c-36d5-3997-a772-58f72cbb6e95 | -12.38838 | -50.22637 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bdf040b-7053-3e89-8a48-88d29c1e983f | -12.0153 | -50.93594 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc8b338b-45c1-36a0-b70a-67b6fd3ff582 | -8.64328 | -45.34241 | 2026-09-29 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f33afd14-2c33-3042-9869-8f4d119698b3 | -7.46637 | -45.8199 | 2026-09-29 04:51:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89abb49d-cbf4-33e7-b2f1-7987bfcae7d2 | -9.81866 | -44.94535 | 2026-09-29 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb683eec-9d4c-3957-bbe1-3b258eab822e | -11.17174 | -44.78894 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 14c43ff8-3cbc-3de4-82dd-176f519e1a52 | -6.31391 | -52.62284 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| cee8a9f7-e1a4-3166-95fb-cd8e881ee12f | -11.41882 | -43.43774 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01b70cc6-db72-379f-b41e-bf87c0e38bb8 | -11.14755 | -49.04954 | 2026-09-29 04:51:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2fc5834-2c39-3cb1-9365-6330c9e4d682 | -6.32119 | -52.62406 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d29348a9-f1eb-3ca5-82e3-b3c69ff4046e | -12.0091 | -50.97477 | 2026-09-29 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1fc3756-d188-3bd4-b0b9-f12486befdc1 | -12.47853 | -47.48528 | 2026-09-29 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60c77abc-6bfe-3a66-8bee-68ba522bf0d0 | -12.6804 | -45.01244 | 2026-09-29 04:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a484357-3166-346d-90f5-5a4875b4b792 | -11.61918 | -46.78209 | 2026-09-29 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 171c17c3-5b03-30db-9728-62179e2a7e16 | -11.17062 | -44.79689 | 2026-09-29 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b5c75805-c1fe-3ee8-957a-602336eef420 | -11.47771 | -49.73424 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8b663ee-c3a3-3067-820c-7c0d4d02febc | -11.39195 | -54.04315 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6af27c6-12c5-3d2e-8ecd-22f56c6f27cb | -11.35811 | -54.05238 | 2026-09-29 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b8c6e5-e6aa-3391-9377-bebc90f48d82 | -11.40151 | -43.42539 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41ff5325-4f97-3171-86a3-0d25153fbcb0 | -14.10945 | -46.28827 | 2026-09-29 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9b13781d-51a7-3fd9-ac04-bcf0ac15f3d3 | -11.40551 | -43.43095 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bda1ed9b-0226-391b-af9c-b5c7d7cc98b9 | -12.1527 | -50.39259 | 2026-09-29 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 803da903-2a54-3122-9f09-28eaad27fc4b | -11.40887 | -43.44141 | 2026-09-29 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30c49491-ae97-3d05-8862-18ffc8f95867 | -7.60777 | -46.45885 | 2026-09-29 04:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 91991ea6-949c-33f8-acca-4c18b51ad605 | -10.27874 | -44.63568 | 2026-09-29 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dcf64a2-9e14-348a-839e-6fbc47d7cf56 | -12.56049 | -47.15637 | 2026-09-29 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README50.md)
