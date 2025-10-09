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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9261159-886e-3565-b1e6-41aed0fd9d1a | -11.72454 | -45.35005 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56688fe5-e25e-3a12-8ca6-1d5fdfd253a9 | -14.7924 | -46.0887 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ea45206-9ec6-3027-a17b-b641837aa10f | -13.26943 | -42.50378 | 2025-10-09 04:00:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5a28f57f-f28f-30c7-8747-a8581160bedc | -13.80068 | -45.8479 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce414841-8427-37cb-9b22-5fe0fd99b47b | -15.05599 | -42.3337 | 2025-10-09 04:00:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| b699fb3f-10c8-31cc-a962-5487e2d693c9 | -11.65768 | -47.5336 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 010c1e37-488a-333c-8d26-a826968ff621 | -13.82335 | -45.79541 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea358ca4-36b8-37b5-847e-e90fbcb6c5c6 | -15.80369 | -43.78349 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8bf1dba-9b6e-3324-9931-6a0e3cb294e5 | -15.40019 | -46.27268 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 790c40ed-7319-3aa1-9c7f-7c3baaf781e5 | -11.48005 | -43.48318 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa0d9e9b-7491-3876-a21a-33ac8f6ae0a2 | -16.37132 | -42.30586 | 2025-10-09 04:00:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1c098e09-2caf-3f08-9792-916ad98db345 | -12.1417 | -47.75139 | 2025-10-09 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10e72d37-98ff-38f2-b49c-c2443a79d56e | -11.76095 | -45.14861 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb55301c-e8c4-3a4f-847d-600a6f1e0ebf | -13.82681 | -45.80009 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f69cc8d3-fac1-3383-9cbe-014c0cf1cc47 | -15.81154 | -43.8026 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 45b94c04-7bf7-3d52-83e0-3c8c71acb0d5 | -15.23805 | -46.35262 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a830b2cf-e515-3208-aee0-31261533e895 | -11.99671 | -45.18509 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c963c6f6-8d6f-353d-ba06-9060edc6ea77 | -14.84407 | -48.45353 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e43f3f6a-d1a4-374c-acc6-6670cfe7e702 | -15.29659 | -46.15481 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ddbc979-14a4-32a1-97c9-c8b480d64265 | -15.38332 | -47.29986 | 2025-10-09 04:00:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 013cfd85-2044-3911-84b7-e3a08d087991 | -13.8281 | -45.81664 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f277940-231e-3f84-bf2f-8138bbd7d21c | -15.28665 | -46.16186 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b35e9b4-7395-32ce-b2bb-d8d843549625 | -14.8418 | -48.36239 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f12fe1e4-6c3d-3e29-a13c-67aa88c173f4 | -10.85934 | -44.62735 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 204b61f8-16ba-341f-8e35-09a40bc4716b | -15.38444 | -48.05653 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9c49f9c-1a08-394a-b3ad-a0a93ee1a40e | -15.46949 | -47.96805 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf391269-20da-3060-b8f5-b4cbbd60eb28 | -15.78618 | -46.25189 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8d0d9f5-4e88-39cb-bc83-23f2b3ce199e | -14.41881 | -43.98987 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c95bf52-48a3-3cb0-b66c-5aa1f4c4e253 | -15.06006 | -42.3304 | 2025-10-09 04:00:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 52d2df6e-c991-317c-9edb-3a93d5a67c51 | -11.79396 | -41.19618 | 2025-10-09 04:00:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 098d9a78-4d0f-3463-a91b-9d7490482715 | -15.8007 | -46.24338 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35c8800d-1249-3680-bad3-5cbc0b301494 | -15.49226 | -47.95776 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb7d462-ece7-398e-8672-c42ed9cfc16c | -11.85143 | -45.07209 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53ba72c1-fcb5-3429-9eff-52dfc057b4af | -14.98139 | -46.28778 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62e94ae0-e8c9-3e20-b117-4811c1c1cf67 | -13.45854 | -42.62491 | 2025-10-09 04:00:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dbc9a34a-8406-3211-a8fe-4919a203feb0 | -15.49831 | -45.34281 | 2025-10-09 04:00:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c158507-a0fa-364f-bc45-8db83194c09b | -13.2701 | -42.49971 | 2025-10-09 04:00:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fa299958-6831-3709-9211-0e5657f69f0e | -15.29555 | -46.18381 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dded3143-1b49-31e6-a75c-277603f85dcf | -13.79377 | -45.83836 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 909e483b-1282-3907-a740-06b8a41cec97 | -11.32186 | -44.88419 | 2025-10-09 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fde06dde-f9a4-3c8c-a64b-deee3161c96a | -15.47258 | -47.95918 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab649b79-dfc8-3138-ac93-20547976e606 | -11.79311 | -45.04124 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f660f5a2-367c-3f97-918e-a1b107e24dc8 | -11.76166 | -45.14473 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af8f6e5e-6ca9-3981-be79-36cb219a8144 | -11.6636 | -47.52899 | 2025-10-09 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8f6e2c0f-5c7f-3dcc-9534-134a7d43682f | -14.84899 | -48.45427 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30e1d50d-33a2-3dd0-a1de-101995808490 | -14.45227 | -47.2915 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f98adfac-d843-3bc6-8f55-f7eda5e492b7 | -15.38913 | -48.05757 | 2025-10-09 04:00:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ddf9330-c5c0-319d-b4d5-0244f45500b1 | -12.23199 | -43.78807 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a72fd290-0fb5-31fb-bc2e-c9ec39d78b23 | -14.78803 | -46.11266 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2807f26c-7b9d-34eb-9449-597386981e0d | -11.25111 | -40.33723 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4963facc-8adc-3924-81cd-53f171a30b79 | -10.52369 | -50.03056 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 29797518-d8b2-36d1-90e3-93e410481809 | -10.89281 | -43.82138 | 2025-10-09 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc741c38-32d2-32fb-af65-129a7d6e178d | -11.24214 | -40.35027 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7f810617-8f24-38f5-b74b-b57afa23da8a | -11.24606 | -40.34727 | 2025-10-09 04:00:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8e44c7a8-3d98-3846-9fbb-e9da6f0c029e | -13.80357 | -45.83228 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba243ccd-5f46-3073-86c2-6f075d20dca9 | -14.08319 | -46.08454 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2bff032e-c424-3a8d-a980-d6ddef74e775 | -16.7479 | -43.97011 | 2025-10-09 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 8c99b322-9af2-329d-b9da-eda4fda8e08d | -15.74811 | -43.67391 | 2025-10-09 04:00:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd7763e5-e6a8-32c7-9611-a38e0e2db002 | -14.9359 | -46.78096 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f08484e5-ae2f-378f-8113-ffa535c02f9c | -15.23076 | -46.3681 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86a63bda-c00f-30d4-bdcb-a740cca2ccda | -14.93351 | -46.79356 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33f9ce12-755d-3735-98a2-a868c09a5e3f | -12.42819 | -45.71959 | 2025-10-09 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0fab950b-339b-3b38-8754-815632525667 | -15.63666 | -46.44714 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9f96c90-12ab-3ea5-9411-0c6ffa201364 | -15.78663 | -46.24634 | 2025-10-09 04:00:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da6c5d0e-5ebb-3bd1-9afd-c7a397e7df49 | -13.80133 | -45.84388 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a2440fd-846e-3a73-85cd-2ca51f5de9dc | -15.06443 | -48.08057 | 2025-10-09 04:00:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 60eb30af-930d-3d2e-afc7-109c3e5b9d99 | -15.225 | -46.37544 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73b10a00-7038-3fd9-b088-dfd665376327 | -14.41666 | -43.98011 | 2025-10-09 04:00:00 | NPP-375D | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| eec1a7a9-390f-368c-bcf3-403bce7ce267 | -12.64981 | -43.42996 | 2025-10-09 04:00:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1708ff98-0ca4-37f6-a2e8-72c7d95a6093 | -10.52529 | -50.02214 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7807e20b-7647-3d11-99ff-e23a1dc76d50 | -15.21917 | -46.3831 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89b23bb0-f6d7-36e3-8052-c7a4f86fcfd4 | -10.22426 | -46.0886 | 2025-10-09 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45c2d518-973c-37a4-96d1-4be6b354a0a4 | -11.79203 | -45.14249 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7311720f-760c-3ba4-8e40-f1bf3cb0ea9e | -15.29161 | -46.15842 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c438f1e-8216-3717-abea-8ca8774cc3fc | -13.79217 | -45.87038 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 961e3447-0af9-39c7-8d08-ceba730a40bc | -14.84526 | -48.44747 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 884fadaf-1151-32e2-905e-0a2c5b68b973 | -10.52815 | -50.02884 | 2025-10-09 04:00:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 089dd032-d7fc-3951-8a5f-d84f70f4d308 | -12.2459 | -43.77548 | 2025-10-09 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92fe503d-86db-33ca-ab82-9cd8fe475bf1 | -14.08622 | -46.08348 | 2025-10-09 04:00:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 913480f5-356e-36e6-bb59-f663444738cb | -15.06895 | -46.6213 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a82b3911-02e2-37b0-8535-ca4ba6a5986a | -14.97715 | -46.28708 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3721025f-2430-370c-8faf-e687ce5e8f83 | -15.07125 | -46.60863 | 2025-10-09 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2dfa09c-0e34-3d08-9aa7-0778cdb98d30 | -15.29084 | -46.16254 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bff0f74a-baab-32a1-82e2-5aac2f98598f | -15.63301 | -46.44665 | 2025-10-09 04:00:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c2bff319-434e-3edc-8faa-3f997f5eef1f | -14.39121 | -46.00623 | 2025-10-09 04:00:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d696158-9172-3fda-895e-cedba29ff779 | -11.98227 | -45.2178 | 2025-10-09 04:00:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11165704-e42e-39c7-aa26-e4b8c0d9e200 | -13.45922 | -42.62086 | 2025-10-09 04:00:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0098c7e5-90a8-3e0d-a4bb-d31f9ff20ef4 | -15.47237 | -47.9527 | 2025-10-09 04:00:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe7669c-f02e-3945-911f-efcc5e344ffd | -12.58216 | -41.28951 | 2025-10-09 04:00:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4b0f9e12-2b9e-3d6e-bf04-87d9e0f9683b | -11.76509 | -45.1494 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a6f5104-a9f5-3984-9728-942cdc87972f | -14.97639 | -46.29122 | 2025-10-09 04:00:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a8fc89c-b9ad-3440-a29f-92c16fe29746 | -15.63842 | -40.84395 | 2025-10-09 04:00:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1062fd85-0daf-30d1-9784-43902a6d4748 | -11.78362 | -45.04677 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b3cf99f-56ba-3c90-a464-d880a7f2092d | -11.63867 | -44.26458 | 2025-10-09 04:00:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e106467-0298-3c6d-ad72-a0bef06757af | -13.79438 | -45.85861 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7536cc96-4b0c-3a6c-8a69-fe86ab1e4586 | -12.07023 | -45.74499 | 2025-10-09 04:00:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53bc760-bbd3-3131-92d3-bd99b1bd6d1f | -11.78581 | -45.15331 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6536e13c-ccb4-374a-9a2b-3e4c2e1eea63 | -14.85012 | -48.44854 | 2025-10-09 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eb8ef262-35f8-38ff-8708-6068f22bf83b | -11.74775 | -45.14268 | 2025-10-09 04:00:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| abafdbfd-d1f3-3122-a4f5-c09c06f3ff85 | -13.79795 | -45.83923 | 2025-10-09 04:00:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README25.md)
