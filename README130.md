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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b095fd2-be82-342b-b1bc-8fb7d3951cc9 | -6.8985 | -41.6976 | 2026-09-21 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| a7179d33-19a0-3f22-b733-a15568d9711d | -5.804 | -53.5223 | 2026-09-21 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4cf50e81-8f33-3f96-9c28-9000eb4caf58 | -13.2787 | -51.795 | 2026-09-21 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 78e180ff-3fc3-35d1-8900-56356062ecc5 | -11.801 | -49.8345 | 2026-09-21 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d0cde822-02ed-38bb-9ebf-41f09c52f33d | -12.3018 | -50.7203 | 2026-09-21 14:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2be7e369-c2f8-3f9a-978f-f11489baca23 | -10.7463 | -50.6172 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 8d7cc1b1-d476-3ef4-acc3-d2bc9d529d95 | -10.9358 | -50.5972 | 2026-09-21 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 43df2264-5844-3a5a-8933-1bc40b4b5004 | -3.4461 | -58.0199 | 2026-09-21 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ca8a5f2e-f73c-3738-a8c0-8b20fcdf2485 | -9.457 | -45.395 | 2026-09-21 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 604cd94f-73ec-391b-b48f-9be9f17865ed | -6.9225 | -42.9088 | 2026-09-21 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |
| 08d56e11-fb8f-3254-8508-7b257f4694b5 | -10.3917 | -48.8915 | 2026-09-21 14:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| adbc4ec0-faad-3394-a51d-8b0dd8d79684 | -10.7655 | -50.5939 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 19c47e58-2afd-337f-ac90-c63f9286533b | -12.5415 | -50.046 | 2026-09-21 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1ce089f1-a018-30be-a6a1-8efa6393cb73 | -8.7267 | -44.8836 | 2026-09-21 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 39a2b09c-536f-3f60-8dd7-b63b9f81f568 | -6.0197 | -51.7686 | 2026-09-21 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 29a7d402-1773-31f9-8942-d66221f8d2aa | -3.8392 | -61.1682 | 2026-09-21 14:30:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| af8918a8-c831-3cb6-93ea-954df6ea35e2 | -10.5906 | -53.9918 | 2026-09-21 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3f88a3e2-7fe3-3ca1-aab0-dd1cf99f5f26 | -6.3195 | -60.0147 | 2026-09-21 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 9b25af5c-f2c5-331c-ba27-19a210e9971b | -3.6449 | -58.8647 | 2026-09-21 14:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 3b665c20-ad11-3990-abe0-c8e3d6940103 | -10.4297 | -50.2663 | 2026-09-21 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 8df2a45f-1568-378b-b8de-f71904712270 | -10.7466 | -50.5959 | 2026-09-21 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5fd185b3-b46d-3dd6-8e41-f6241189c3d7 | -8.7729 | -44.2568 | 2026-09-21 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 159.5 |
| 5e9f9e45-70a0-3666-80f4-41eed0a3d862 | -3.1698 | -58.5859 | 2026-09-21 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| ba45db7e-5335-3f94-a735-451ed82b3ca1 | -8.7911 | -48.7502 | 2026-09-21 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 150.2 |
| bb53c84c-c456-3e60-8bf2-b007652f77e4 | -6.4554 | -48.4423 | 2026-09-21 14:30:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f0ebdda3-385c-303d-9807-63d35509405c | -8.8736 | -62.4115 | 2026-09-21 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8501f227-4445-3763-a660-416b5f70b92c | -10.3728 | -48.8936 | 2026-09-21 14:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| f9bddf39-4e72-37eb-a183-852b1bef653d | -6.5634 | -44.9084 | 2026-09-21 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3edb9da2-d713-390e-a891-b55a804abe13 | -10.9547 | -50.5952 | 2026-09-21 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| c3e4eb4f-626f-30f2-9171-b23236b50e0a | -8.7726 | -44.28 | 2026-09-21 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 209.1 |
| 6f75e061-b39e-375f-871c-ee974644c159 | -5.6781 | -43.4125 | 2026-09-21 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 0ab3889b-ff1c-3ac8-873f-d9323fe23502 | -6.338 | -60.0141 | 2026-09-21 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 83eb491a-098a-3b7c-89a2-fc7dd4cd2d0f | -3.753 | -59.419 | 2026-09-21 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 40ad8f8e-fbcd-3a2f-909e-41ac57dac9ce | -14.1815 | -51.808 | 2026-09-21 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 20a076d5-3c27-3020-a52e-1466c83da2c6 | -10.336 | -50.2119 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9bc6c595-0ef9-3824-abf2-bda494b427d7 | -9.3679 | -47.7766 | 2026-09-21 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| e577d31b-09be-33ff-9a38-b62271a2f86e | -11.0412 | -54.1362 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.2 |
| c8b08668-f15e-34b3-856f-2242fb2bf2eb | -13.2596 | -51.7973 | 2026-09-21 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 211.4 |
| ea15d086-00ef-35b1-b756-cfe2b8c45a1f | -3.6632 | -58.8643 | 2026-09-21 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| cb0f2357-a876-39d3-9cd1-7fdbf47566c5 | -10.4486 | -50.2644 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| d29e5816-ef71-3317-ad74-cc2830d824da | -4.0943 | -52.1458 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e6d21016-513b-3bd6-9e3c-daa80ec8b99e | -11.4541 | -45.3662 | 2026-09-21 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 169.7 |
| d42f9840-f339-34c2-87ef-3596ab536fde | -11.4545 | -45.3432 | 2026-09-21 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 429eec8e-2469-36ee-b39a-3b968c525f8b | -11.662 | -47.7737 | 2026-09-21 14:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| af80038d-77ee-34fb-b051-48107982f1c4 | -10.3738 | -50.208 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 549cf9ec-e2d5-37d1-bc81-327766a11449 | -6.5761 | -45.5194 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| d26328cf-5284-3606-9385-c3d9cba92b60 | -9.8307 | -48.451 | 2026-09-21 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| e5d411a4-11f9-3d06-ac60-0142daf71334 | -8.1874 | -54.742 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 9b7f2e5d-a2a4-3501-b128-269744789c0f | -10.4917 | -51.3001 | 2026-09-21 14:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 80c49f54-7720-3406-8e83-a75e8ccd8720 | -9.5595 | -66.0172 | 2026-09-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 9e624ca1-c0d1-3720-84c2-2645be5b5abe | -10.7652 | -50.6153 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| a5f7526f-7138-3e16-b2e8-c1f964d6c994 | -6.9225 | -42.9088 | 2026-09-21 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 83e36ceb-5633-3f78-a077-9f198ad59fe1 | -5.7692 | -43.7077 | 2026-09-21 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d860a282-e559-376e-996d-891d3b0f7960 | -10.8853 | -51.5347 | 2026-09-21 14:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 2c36083e-19e2-3d0c-ae54-15a414303fc3 | -7.3291 | -55.1955 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 9a9c922e-0a69-3efa-aec6-cb24ef77d08f | -3.6631 | -58.8835 | 2026-09-21 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 2fd66a27-2922-3040-a2d3-1e90bfd285c3 | -12.382 | -47.0283 | 2026-09-21 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 33cb8211-9828-3b1a-9134-c3c4be3f8d6e | -9.043 | -48.1384 | 2026-09-21 14:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 199.1 |
| e7c33622-8e67-35f6-948f-778e042d08f4 | -3.6947 | -60.5645 | 2026-09-21 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 13ee3c25-60db-3c9e-afac-ff74bde63a54 | -10.3916 | -50.2916 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fd96a6b7-8c4b-3aa9-9998-574de45f4778 | -6.5451 | -44.8643 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 168.6 |
| 3b15628f-4baf-3416-96d5-2183a59a7540 | -8.0094 | -61.3633 | 2026-09-21 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 26dfa400-8a6c-387d-ad01-ec0cd15775b3 | -6.4741 | -48.441 | 2026-09-21 14:40:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b9a75a68-0636-3654-b0b4-e5be7918d010 | -7.5711 | -45.4333 | 2026-09-21 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 31ddeeaa-a6d7-38eb-b519-a4f0ecb5a532 | -10.4288 | -50.3305 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 47f0e17f-33df-302b-8480-1b19f6ed017a | -5.6411 | -43.3687 | 2026-09-21 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 163.8 |
| eb55c8bd-3df8-3a3f-a3d2-9772940ab0e7 | -8.1876 | -54.7219 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 969068b6-875f-32be-95b8-da9343e7612b | -4.5774 | -42.9512 | 2026-09-21 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 65c639a2-6197-3028-8f8c-c1c34462bc0a | -11.0509 | -54.9106 | 2026-09-21 14:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0b781a00-a4be-3d78-a52c-afbef62d131f | -4.8683 | -55.8457 | 2026-09-21 14:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 44d61635-38ed-3a31-b97d-313034515920 | -11.0407 | -54.1772 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c4276728-ea48-31dc-97b7-b36dd9f13bf2 | -10.7466 | -50.5959 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| dc1e6887-51d1-3697-8542-607997143e65 | -10.2787 | -50.2605 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9c4742bd-7da5-35f3-bbd1-1419390951a1 | -2.2619 | -48.7445 | 2026-09-21 14:40:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 53dbd37c-4b13-3ff8-bb9d-271b139f7f32 | -3.8392 | -61.1682 | 2026-09-21 14:40:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 17e53742-d59e-3811-85ca-07c438c327af | -12.3212 | -50.6965 | 2026-09-21 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5c00941a-dead-33e9-bda0-017adc33522f | -6.001 | -51.7903 | 2026-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| d0cce6f6-7c58-3942-956d-2538ce01a0e9 | -10.7463 | -50.6172 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 9062c7b3-ea56-3e47-bf0c-50cb3169d804 | -11.8359 | -50.046 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| c69d306d-e568-3839-b0f9-da0bcc5f2571 | -9.5594 | -66.0359 | 2026-09-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 97e12650-70fc-39a7-8e2b-a13491b60eaa | -4.2239 | -48.6127 | 2026-09-21 14:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 5869d5a9-26e1-34b6-9a80-279204996bf4 | -11.0221 | -54.1584 | 2026-09-21 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 7ce447e1-07ed-3643-84f9-03e2c3ca69ec | -9.257 | -46.1873 | 2026-09-21 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f9107f5e-6c76-37fe-a044-450dbb9c12c2 | -10.4672 | -50.2838 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 67654c72-2d23-3fdb-8246-4692ad60496e | -10.8002 | -50.8243 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| e54b3ef4-4c83-3b68-8fa6-9cdc11f0d413 | -10.4102 | -50.311 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 406d4d50-7fd0-37bc-ad04-3b6d3000d48c | -10.7999 | -50.8455 | 2026-09-21 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2ddf3ad5-19d5-34c7-b773-56d97df7c2dd | -3.6946 | -60.5835 | 2026-09-21 14:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 319d8d0f-fe94-3d1d-8140-4bf2b3029cb7 | -9.5593 | -66.0545 | 2026-09-21 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 491251db-a5a2-39c3-89f9-302e55325bd9 | -6.5569 | -45.566 | 2026-09-21 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 737b1355-1ed8-378f-b5ac-a35953aa5ef7 | -7.5661 | -61.3239 | 2026-09-21 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 800ebdb5-97eb-35ce-a80d-840465eedf43 | -4.9535 | -45.1374 | 2026-09-21 14:40:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| d8d639c9-dcfa-36e8-8f52-52ed94d7de04 | -6.5829 | -58.9851 | 2026-09-21 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d3e24fc8-acfd-3cb9-97a3-dab2181205cc | -6.0033 | -44.7247 | 2026-09-21 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8014bb05-2dcd-3732-94be-fc057638313c | -11.8715 | -48.9792 | 2026-09-21 14:40:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| c79dacd1-678a-36d5-b41a-f98ffbd06498 | -6.8846 | -42.9359 | 2026-09-21 14:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 2b744f14-beba-3f4c-82ee-f491e2e7701f | -11.801 | -49.8345 | 2026-09-21 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 42f629a7-2c08-3913-81f0-167f944befae | -11.3419 | -51.3606 | 2026-09-21 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 453cb500-6601-35f9-b0e9-e09cf22f05b0 | -10.4291 | -50.3091 | 2026-09-21 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 65f0f4bd-c3f2-3f5b-8899-c854ff663477 | -8.1686 | -54.7634 | 2026-09-21 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |


[Clique aqui para ver as próximas entradas](README131.md)
