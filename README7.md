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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 933ecafb-02e6-3d7f-b24f-7d2272e09983 | -13.80139 | -53.29897 | 2025-05-20 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03a1e80c-2003-37ae-a641-eacddd2451f5 | -12.30252 | -52.47549 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fa70403-3f61-36d7-a975-4a812e69b508 | -10.36241 | -47.97184 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7b085f1-34e5-3c7e-bf96-af2b614fecb9 | -11.08929 | -54.77687 | 2025-05-20 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 164bcb86-02c0-33ad-a2e4-bd412e1d36d5 | -11.69562 | -47.78894 | 2025-05-20 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4290e5d-cbde-3dab-8858-cafdbe092b92 | -12.98395 | -46.32383 | 2025-05-20 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8aba5a5d-9bdc-3f0a-a47a-ea358934436b | -13.3678 | -54.257 | 2025-05-20 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f167c29-e7cb-3d1d-abfb-0de35279a8e2 | -11.79285 | -44.27351 | 2025-05-20 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93577cee-2b1a-3c27-9193-0359744d3b87 | -12.13103 | -54.66751 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094959f5-559e-3850-9e72-b1ca21356cd2 | -10.36133 | -47.97887 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb044e0e-6f12-3f14-b627-f8dfbdf0f943 | -12.27311 | -57.27043 | 2025-05-20 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb46a31e-0541-364a-8af6-3177c54e6d24 | -11.89215 | -46.94488 | 2025-05-20 04:34:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1dbd573c-19ae-37b0-89e8-aeb65f1411dd | -12.9824 | -51.93888 | 2025-05-20 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4b8e29b0-6b9d-36f9-ae70-ba4a66b1a8a8 | -12.43519 | -48.11095 | 2025-05-20 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6525276d-9f70-3bff-a75f-9f1e4e1a5a83 | -10.36573 | -47.97236 | 2025-05-20 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fcfcf5e-75d1-3552-a5eb-88900ccc30f6 | -13.03292 | -45.06787 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cadd544f-db7d-3d6f-a906-1538f076cf8c | -11.66515 | -54.9431 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 181de81a-4ecd-3a34-9d7c-43bb7478daaf | -11.23815 | -49.4892 | 2025-05-20 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcbde23b-d309-3b76-bbcf-09865a31581a | -10.60203 | -46.97333 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d240757-c9a6-33a1-a924-0cc2e22361b7 | -13.90526 | -43.79834 | 2025-05-20 04:34:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf2ce816-bc08-3f3e-a7e3-d74128a24c08 | -12.98455 | -46.31968 | 2025-05-20 04:34:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0036a8df-371e-3d44-88b3-86877532cf7e | -13.02909 | -45.0673 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6fd2f9a1-dbec-3f04-b377-f35ea3c9242b | -9.03841 | -47.75994 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e70b15b9-047b-374a-a6a3-f3ebd02bb563 | -9.04864 | -49.517 | 2025-05-20 04:34:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a068f38-5284-3ba9-97bd-66e498e7bfe2 | -9.41606 | -58.32775 | 2025-05-20 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87a0e4e2-77cb-3ba3-b33f-759163029ba0 | -9.62138 | -49.48959 | 2025-05-20 04:34:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f381fca5-2dd4-35d1-9a79-e1e6c8166474 | -16.66967 | -44.55647 | 2025-05-20 04:34:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 983e4df5-2928-3064-86b9-8fab40c34800 | -12.6859 | -58.12867 | 2025-05-20 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a4e59fc-cf1c-3870-82e8-7a6fe0d130c8 | -11.66584 | -54.93909 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4acd775-1a52-394c-9549-2bd22b0c7a1f | -10.55021 | -55.62282 | 2025-05-20 04:34:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc3b7e2a-158e-3a1c-9575-a62332376d73 | -15.21227 | -43.82553 | 2025-05-20 04:34:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34a84a62-0d84-34ef-be1f-41099efaaf98 | -13.03225 | -45.07274 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48880d83-b76f-34bf-a684-3ff8a57a7e54 | -12.08682 | -54.58249 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44c0ecd4-e478-3ab7-b485-b71687685adf | -10.34584 | -47.81345 | 2025-05-20 04:34:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28731393-9642-3603-96dc-cdf91f4b9308 | -10.54995 | -42.43054 | 2025-05-20 04:34:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e757b62-01d4-398f-aa68-234451d65f59 | -14.13603 | -41.69497 | 2025-05-20 04:34:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 90f0ec5b-fea0-3575-a609-91d3f79d4230 | -13.03159 | -45.07758 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 620d8212-f433-3eb2-8617-efc4994e9d19 | -12.06741 | -47.32325 | 2025-05-20 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40f910a3-97ac-3051-841a-ff61898f92c2 | -8.7495 | -49.74668 | 2025-05-20 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4a9c1074-d075-3ae7-9d57-50eaa18f07ee | -10.56993 | -48.52189 | 2025-05-20 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09af373c-a895-3f30-95d8-6e96c30dbc34 | -10.55164 | -55.6269 | 2025-05-20 04:34:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50223ea8-3c8e-35f8-bf1b-65bf6f24f2ba | -11.23428 | -49.49218 | 2025-05-20 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8d1e91c-0c4c-3b3f-b127-e52c35beac67 | -11.69062 | -47.79929 | 2025-05-20 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2662297b-14e8-36d4-82c0-ae907eb91b0d | -11.52011 | -48.58049 | 2025-05-20 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9f0eafa-49c2-3704-8f0b-de71bdf8f121 | -10.60773 | -46.98178 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5c6e371-3da5-3b5e-8629-bbdd61ce26bc | -11.08086 | -54.77546 | 2025-05-20 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 436ca52b-cefe-37e1-a233-d5fbd74bb06e | -13.79985 | -53.30134 | 2025-05-20 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd79ab5f-2b62-364d-88ab-578229b4c266 | -11.87838 | -44.37674 | 2025-05-20 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa65f8f-ef7b-397e-86b3-2f971c83852d | -11.69172 | -47.79205 | 2025-05-20 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b7102c8-acfd-344a-8577-14833ee781b2 | -14.68484 | -47.29006 | 2025-05-20 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7e968cd-c4c2-323e-b764-e7e8b6f88e29 | -12.41023 | -54.41483 | 2025-05-20 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f72161f-ba6c-34cc-8a3b-1488879b12c7 | -14.03459 | -55.1283 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 80a7498b-27e5-3324-a0ad-e284953e226c | -11.56689 | -54.56216 | 2025-05-20 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7195a0ef-ea58-33fc-ba95-704103ca4859 | -14.0249 | -53.02179 | 2025-05-20 04:34:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25d00550-561b-3843-8e4d-001b1654a210 | -12.24843 | -51.44838 | 2025-05-20 04:34:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79d52d39-7641-3c36-8b9e-94444946aaea | -9.4154 | -58.33136 | 2025-05-20 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd4bb175-64cb-30a1-ac25-f2e132b41498 | -11.66944 | -54.94422 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63e6ba69-0e4b-3155-bea7-a788b24ce7d6 | -12.12757 | -54.66305 | 2025-05-20 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da63cc02-ccb7-35da-81cb-0aed840baa3f | -11.4186 | -44.70717 | 2025-05-20 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ecbd625-2688-31ee-af48-a58f3c8a503f | -14.68136 | -47.28952 | 2025-05-20 04:34:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 795adbfa-ae2a-319c-91e0-cedc9f244da1 | -11.07779 | -55.06712 | 2025-05-20 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f48b1637-fc5f-378e-8ab8-5ee631fb4058 | -10.34693 | -51.68448 | 2025-05-20 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ca117c5-9555-3821-a0a1-c18dc67b2551 | -14.04904 | -45.51661 | 2025-05-20 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5eacd8ae-62cf-3e3c-b4b4-f6419e5924c4 | -15.56917 | -47.85375 | 2025-05-20 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e01f880-2ed5-37ea-a152-6ddc3d1b88ba | -11.41546 | -44.70176 | 2025-05-20 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57c79447-c0c9-39c1-ad5f-da5204485a74 | -14.02708 | -55.12307 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12e8f1fe-0106-3fe2-aacc-8d29e0e79d55 | -14.02084 | -55.14064 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7738af51-0c58-35aa-88d0-f06984f89bdd | -11.35888 | -55.12371 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02e6b668-e855-3afa-985f-4d15ee5f8b7f | -11.7968 | -44.27411 | 2025-05-20 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41772bbf-4e18-3fdf-b2df-0d9e613006a0 | -14.03323 | -55.13577 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6a3ebbc-5924-33d8-89b1-81380391c310 | -9.98185 | -52.1467 | 2025-05-20 04:34:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1e72ad0-98b4-3e32-8a11-da787e64efce | -11.35252 | -55.10976 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5fdba46-c630-3eae-a010-93118a7eb193 | -8.74557 | -49.74973 | 2025-05-20 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94a6a79b-ad52-3d91-b125-a6a55ac1cc01 | -10.59862 | -46.97279 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f91eb88a-4100-3f2b-9abd-015573d072d6 | -12.12089 | -47.98801 | 2025-05-20 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2b66a5b4-439b-3f39-b0c0-6c95d2f3440f | -11.23759 | -49.49271 | 2025-05-20 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bd149b2-e51a-3146-b048-071babb954fb | -12.07081 | -47.32379 | 2025-05-20 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4d7a739-823a-367a-9764-ff7ff7579f14 | -12.2767 | -44.59365 | 2025-05-20 04:34:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31dcdadb-4cb1-3964-8d30-cb73ba988a76 | -12.40876 | -54.41737 | 2025-05-20 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15627be7-e956-3bf2-bfb4-928219b90d6c | -11.69842 | -47.79309 | 2025-05-20 04:34:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfc07189-ef4a-398e-8c42-7b9eabc3df3e | -10.61113 | -46.98232 | 2025-05-20 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ad9af4a-c27b-3fcc-88ec-5659c6cd28fe | -12.43673 | -43.72586 | 2025-05-20 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 15a2c459-fb24-312a-86a8-016d27ed078c | -11.3475 | -55.11312 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d60e5595-3e59-378b-924b-ebc7a5922829 | -14.03186 | -55.12009 | 2025-05-20 04:34:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f50a20f6-c5b3-3104-9e5a-458f294dc754 | -12.29805 | -52.47168 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79e43ca1-4da1-3b26-ba2d-3e47a913c4b2 | -11.08577 | -54.77224 | 2025-05-20 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f99e2bf3-6bd2-3e18-94e7-1cbe62d05417 | -12.34557 | -49.97526 | 2025-05-20 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11aa66d1-3ddd-3924-a2ee-44d5d9c7ce29 | -12.29444 | -52.47106 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cf44dfe7-1d90-3e7f-ad3a-9080b3c10952 | -13.31 | -50.01102 | 2025-05-20 04:34:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e01649bf-55c8-3956-abe6-2a8228ab252c | -14.66371 | -50.1886 | 2025-05-20 04:34:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b160ab0-588e-33d3-8218-da2018dd3164 | -11.23704 | -49.49622 | 2025-05-20 04:34:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d222be1-1131-31eb-956a-700d0b9c07d4 | -9.51434 | -47.69386 | 2025-05-20 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e8aeec4-7e22-3685-a5c5-79950a660da9 | -9.19655 | -45.33908 | 2025-05-20 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b1667b-5367-3372-9ab6-e817141084d7 | -13.02842 | -45.07217 | 2025-05-20 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0fb08197-9ade-3a1c-9793-b9358bfbfaee | -11.56133 | -47.61636 | 2025-05-20 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94ffb192-4776-3104-8af1-fa918131236d | -12.30165 | -52.4723 | 2025-05-20 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca5c5394-1f2f-37a7-ab01-72a0ee8af5e4 | -11.35962 | -55.11956 | 2025-05-20 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 985e0ff0-77ff-301a-bf7e-684ae64dc35e | -12.47974 | -57.19442 | 2025-05-20 04:34:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98c2b103-8cb9-3d95-9c42-ea776045fd99 | -8.74892 | -49.75027 | 2025-05-20 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa837db9-59dd-35f5-89e9-677176a10b04 | -11.08508 | -54.77616 | 2025-05-20 04:34:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)
