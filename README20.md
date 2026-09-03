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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0897134-2941-3cbd-a700-39d362995f7d | -11.31608 | -45.12144 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d62688c1-6e01-3d9e-84df-058b5c459476 | -11.20737 | -45.02936 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 42aef137-2b9f-311f-9b4b-c0359eb7099f | -15.89499 | -47.682 | 2026-09-03 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66e39b81-cfef-3a40-aa22-c1edfdcd386a | -13.09998 | -44.50051 | 2026-09-03 04:04:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee6b54c4-da30-39b1-9939-269b3d5c8e0b | -10.48899 | -48.64935 | 2026-09-03 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2b333dd-249b-3a24-95ed-44e0752790a1 | -12.1418 | -47.14066 | 2026-09-03 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8f9a342-e162-3ef2-bd23-b214116bd819 | -12.09026 | -47.05944 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f2b09f27-67a3-3f3e-85e3-d5177e11f109 | -12.08675 | -47.05486 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 251d38eb-52c9-3678-9a27-f185fcd55f67 | -11.29398 | -45.18404 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bf5701c-8139-3f17-8332-5ddd0f5cfdfb | -12.09798 | -47.07222 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 869287cc-e055-34de-b8af-55219c1fb7f7 | -15.89431 | -47.68579 | 2026-09-03 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ac8f742-e64c-3f24-9f41-054793e9402b | -12.41349 | -44.80269 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfa6d1f5-2750-31c4-9f76-d5a9fd6611d1 | -12.12074 | -44.18967 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67a2931f-3f57-3aa3-9322-5d73917fa89f | -11.30189 | -50.5217 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a9ace037-07e8-3c5f-bde4-c1ddef1893c4 | -11.29178 | -45.1742 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4349d25f-b224-3aa4-a548-92760553b467 | -11.33591 | -50.54576 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 5858a2bc-b164-39f7-9eb6-e983b4eca433 | -12.08756 | -47.05843 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6acbcdc7-e7fa-323c-9d30-4510d81ff936 | -17.52611 | -44.61301 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc5fadcb-2c03-3e6f-8391-3982fc7cbc6d | -13.38508 | -51.37915 | 2026-09-03 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4cb10d6d-2c4a-3b24-af6d-8682b68531d3 | -12.09173 | -47.05915 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 889eaa2e-a637-3c3c-9295-4fa03dfba207 | -15.54093 | -46.19692 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14df7c44-f018-3e1d-9971-921e1223a496 | -10.20859 | -50.28259 | 2026-09-03 04:04:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 328d8a34-562e-3863-ac12-9ef08ad1821e | -13.75033 | -43.82914 | 2026-09-03 04:04:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 249c7818-9b70-3ecd-acc4-6a762f0e18df | -15.5895 | -43.80529 | 2026-09-03 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 125317d1-e825-3cf6-b064-367821b1243d | -11.33798 | -50.55367 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c997410b-c19d-32c1-abad-1a93a0394428 | -11.28726 | -45.17804 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83549ef6-9c34-3b33-9664-68083463bd5f | -11.3191 | -45.12644 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1653c46-98bb-3b93-bbf1-99cc8a8a0092 | -17.49179 | -47.84871 | 2026-09-03 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9789f8b-2968-38dc-9814-3c39b8536e51 | -17.63251 | -44.33118 | 2026-09-03 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4be158f-9ef2-32ba-b158-cb9eb3c68798 | -15.02471 | -46.85233 | 2026-09-03 04:04:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1018a548-bdd3-3252-b985-dd409b41f327 | -12.14599 | -47.1414 | 2026-09-03 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 494de21c-fcfe-363f-aa7f-4d1d3eaaf1c1 | -10.75899 | -48.97823 | 2026-09-03 04:04:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f647c92e-7fa0-3a48-966e-55ea840c20e8 | -12.09308 | -47.06793 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0eefdf34-fb06-3194-8319-3e6d58fdd5c4 | -11.33485 | -45.12435 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df0c2c9a-292c-33ef-9f52-8f41ae1ef62d | -11.3072 | -50.52272 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c44cc92e-d4dd-3413-a0a6-783e81a7d5fc | -10.75608 | -48.97553 | 2026-09-03 04:04:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eea913a5-c606-3248-b3c6-0b364b63e0df | -14.04995 | -48.40672 | 2026-09-03 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 64e64729-1381-3c34-8122-37e0dcf5f63e | -12.09092 | -47.05559 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1068b9cb-76cc-3015-84ff-211d39d6d88e | -11.32186 | -50.53254 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41b872a7-0dad-3b2b-8692-8f6e80074b80 | -12.19221 | -47.08184 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bcfd57b-78c7-3ecf-9477-892a025dc68d | -12.13334 | -44.17938 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5cb3933-315b-36ed-9f7c-11d8967bf4a6 | -11.29713 | -45.14243 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d62d6fa-680b-3df7-acff-59cdbef4382e | -14.90918 | -44.67624 | 2026-09-03 04:04:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b23880dc-a095-3c25-89cd-9d30e48897aa | -12.05424 | -47.09325 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e41d394-56ea-3a40-ba48-2317023fc3bc | -12.09576 | -47.05245 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8c48c86-6c8e-3da9-b99e-6433cf493915 | -12.13421 | -44.19615 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e57efe73-27b9-3335-843f-fe63db63b334 | -12.13001 | -44.19961 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fda202f0-bbd6-31c1-8537-9ec8147a5bdf | -11.24741 | -45.16227 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e248d102-ee9b-3985-a90c-a04d1b97b407 | -11.3266 | -45.12765 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37050ad4-38bf-3606-88e1-3592d015c13e | -12.09104 | -47.063 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 660ac0fb-d923-3c3f-91ab-a82ff27c02e8 | -13.88194 | -42.00248 | 2026-09-03 04:04:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a792578-a6be-38f3-b5e1-f73521f88da0 | -14.61129 | -48.8748 | 2026-09-03 04:04:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08f767b6-80ee-336b-8f75-2f89b177a44d | -11.69416 | -46.73606 | 2026-09-03 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93eca032-50bc-3b3c-9268-27abda7d5760 | -9.62435 | -54.31292 | 2026-09-03 04:04:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70bc780d-d6bf-3490-b3a6-1d17c2d620a4 | -10.5718 | -47.71157 | 2026-09-03 04:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4df35f9e-dcf9-38fe-b24e-535e14dc24bb | -13.81823 | -42.17004 | 2026-09-03 04:04:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3c090034-f306-313b-9236-f29f8d0ecda1 | -10.48995 | -48.64643 | 2026-09-03 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cb95a9d-faea-3233-9ac1-5f324f0901de | -12.13068 | -44.19554 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b19ffc5-74a0-3fab-9eb1-7bef14f3a89c | -14.95509 | -48.11002 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7cd954e4-0811-3cb4-9b8e-22d5082ce9a6 | -14.2123 | -42.04244 | 2026-09-03 04:04:00 | NOAA-21 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 19e148aa-8171-3976-a162-368bc5362095 | -15.67808 | -45.89111 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e740aefd-c529-33e9-8fc7-3035d095bc18 | -11.32123 | -50.53592 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9fd6de48-8b48-3be3-a330-bbf2ac2bbda0 | -11.33995 | -50.54353 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 12adbd1a-80db-3573-a8c4-be9bab56e9c8 | -11.31314 | -50.52036 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 338812ad-3c83-3a28-83fd-856baf0ff439 | -16.07672 | -46.07767 | 2026-09-03 04:04:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f735d2d4-a5e5-31b3-bf99-db443d9be9a5 | -15.89565 | -47.67828 | 2026-09-03 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97fa09a7-c400-32b1-a489-eaca8e987f61 | -15.58899 | -43.8018 | 2026-09-03 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 380822cc-bffb-331c-9990-432360a34efa | -13.38928 | -51.35794 | 2026-09-03 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e55d2ee5-7c8b-379e-a46b-673b220c2796 | -12.19516 | -47.08187 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e36650a-efca-327e-b5f4-71ee36df92e8 | -14.0229 | -41.77503 | 2026-09-03 04:04:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e5d6f12a-52cd-37a1-aac9-1302292c0682 | -12.40113 | -44.80947 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 12711a29-6392-37d4-a367-4e7b4988784e | -12.09033 | -47.06689 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8566d17a-cbd7-3dca-b067-037270948aa4 | -17.57654 | -44.96809 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb3a325d-2148-3a9a-8524-10e152793593 | -11.33397 | -50.54591 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8129762d-a050-3d93-8672-1347b4933498 | -12.08958 | -47.06331 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a5ffbd28-3a49-3803-ae6d-54d1011c6a09 | -14.95406 | -48.09211 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d24bbf71-133a-33f3-b5e8-246202856064 | -12.12428 | -44.19028 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0070ff0-11f9-3535-8155-2672385c2bc8 | -15.16552 | -44.07197 | 2026-09-03 04:04:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c19b8d47-bd0c-38c2-b4b5-b6266234bc0d | -11.28052 | -45.1722 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9265141f-d9c3-317d-93a8-eaa4e7235574 | -10.49472 | -48.64722 | 2026-09-03 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b666e873-c0d8-36bf-9a84-5e79f9179b30 | -10.56859 | -47.72929 | 2026-09-03 04:04:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b18e29dd-39d8-3e9c-9e11-7b9d53c049d1 | -17.57802 | -44.97226 | 2026-09-03 04:04:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12c5a89a-1b1b-3f35-9a32-a91879b376f6 | -14.96328 | -48.0897 | 2026-09-03 04:04:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c415b91e-d94f-3bfb-94a8-bc46da27ae96 | -11.33654 | -50.54237 | 2026-09-03 04:04:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4259d92e-17aa-3ffd-bca7-90457d86e6ea | -12.4004 | -44.8138 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b713fae0-102b-3a79-bda0-70bbbd7a07cd | -17.62851 | -44.33439 | 2026-09-03 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8027f6f-21af-3de0-970c-7c27642de101 | -12.19151 | -47.08572 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8ef1e5f5-399e-384f-912f-b241019db39a | -12.13288 | -44.20428 | 2026-09-03 04:04:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57031a44-9755-3ddf-b48c-8358e49ae739 | -17.63991 | -44.32857 | 2026-09-03 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d1a9f8e-9c7e-3784-bffe-ab7569fa2f51 | -12.40913 | -44.80636 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 6206d1c4-1b7a-3768-a273-4e66d2f885df | -12.09376 | -47.06403 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8db3af19-6d2a-3ef2-9a47-1eeda56aeca5 | -11.29105 | -45.15563 | 2026-09-03 04:04:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1bd4e11-1237-3312-9496-a687ef4a396e | -12.41276 | -44.80698 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6937fed5-e83a-3360-959e-1235814849ef | -10.49463 | -48.64528 | 2026-09-03 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4f1d29c-1814-378d-a7b7-54e86bdc93d0 | -10.48986 | -48.64449 | 2026-09-03 04:04:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06cedf9a-c498-3cc8-bcd5-0f967e527fd9 | -12.40623 | -44.80145 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 74de7e62-d853-3aee-b189-4e657320b1b7 | -13.38438 | -51.38269 | 2026-09-03 04:04:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8b3bf6a2-636c-37dc-a9de-d1456e3561f0 | -12.08826 | -47.05458 | 2026-09-03 04:04:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22fbb496-82de-3f4d-ab91-51f7982fd20c | -16.54028 | -49.56461 | 2026-09-03 04:04:00 | NOAA-21 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e641c99-68fd-3b76-8458-545e087c6b8e | -12.4055 | -44.80575 | 2026-09-03 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |


[Clique aqui para ver as próximas entradas](README21.md)
