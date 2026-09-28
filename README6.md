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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6fa64aa-d276-3e57-9ea9-d3555127bb9c | -12.8643 | -44.816799 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89c95663-394a-31e7-8f47-053d83f2abc0 | -11.0737 | -51.327499 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 488b7400-7b9f-33c3-b251-a3d7b9f7507d | -3.274 | -54.265202 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a34f218-6d38-33f7-bb2c-450a4fecfff5 | -7.5554 | -61.330002 | 2026-09-28 00:33:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5ffa109f-811c-31a2-9b74-09610934cf6a | -11.8512 | -48.885601 | 2026-09-28 00:33:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdf7d0e3-6df4-3186-9cc6-7d13401b4e5a | 1.6673 | -55.922699 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f75b6ec4-7fda-3a9a-b4eb-0c5090926683 | -7.8703 | -61.177601 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8921042a-d963-3ba3-b8a6-1a2480734d14 | -12.8986 | -52.065201 | 2026-09-28 00:33:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14df7b18-4746-3236-ad6e-400bf3701d92 | -1.9222 | -52.142899 | 2026-09-28 00:33:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae9c84cb-ffc3-374e-a4cb-4e9f5ebe00bf | -3.4199 | -48.345699 | 2026-09-28 00:33:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85d3331c-dbae-345f-ad81-1efaf02bf3d7 | -2.8985 | -54.1105 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ec2ee6-01b3-3cd5-8143-1ad59c2e228d | -11.3345 | -54.1161 | 2026-09-28 00:33:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0cd1887c-271e-3036-8ae3-c68c186187d1 | -3.1977 | -51.029999 | 2026-09-28 00:33:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f71b0f2-c9ee-3691-8add-7ca5c9aa9c9d | -8.0356 | -54.891102 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 347737e2-f908-3f7f-8706-1a6b4214dd70 | -21.0201 | -47.251099 | 2026-09-28 00:33:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0101f326-2bb0-310f-9268-40812eda7737 | -15.1851 | -48.433998 | 2026-09-28 00:33:00 | METOP-B | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30382cb4-0441-3096-9ff7-a1d4c8e83c2c | -7.8605 | -61.179699 | 2026-09-28 00:33:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13efd3a0-b333-314e-8719-39858b08061c | -9.484 | -46.3848 | 2026-09-28 00:33:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 148835dd-c256-3354-a6fc-fd842a5f3c20 | -6.7848 | -59.366402 | 2026-09-28 00:33:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4d29475-91cb-3a59-96d3-64929680226c | -10.8276 | -57.230701 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 34176253-1f36-3283-b98b-5152cad22eb7 | -2.9793 | -54.148499 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff3a9249-c585-384b-b4ac-bc46499bda69 | -3.0145 | -54.212601 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bc2f580-f5dc-32a1-b6bb-0b5665e85720 | -7.6976 | -54.763802 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a600f6b6-e0ae-3338-90fc-742e6b5a659f | -12.6523 | -47.3242 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d46e55bf-1bcc-3998-9d24-b424092118dd | -15.1659 | -46.143299 | 2026-09-28 00:33:00 | METOP-B | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4bb99fd7-3c3f-313f-9f24-84adb061c1ce | -10.8013 | -57.203899 | 2026-09-28 00:33:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6706280f-33d0-3394-a944-49ea01b3cc3d | -7.273 | -55.576302 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf84e4f0-9344-33ed-8417-971bf7542b6c | -17.8277 | -44.396301 | 2026-09-28 00:33:00 | METOP-B | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d195445a-bb61-30dd-92e4-e4e29c85da3e | -12.736 | -47.286999 | 2026-09-28 00:33:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97c8bb3f-2fcf-3be9-a9ca-efb744bf993f | -8.6691 | -48.961899 | 2026-09-28 00:33:00 | METOP-B | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7dfc1cec-6c50-35ef-abf1-68d80b098864 | -22.3409 | -46.9655 | 2026-09-28 00:33:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 87778bf3-c7d8-38e9-ab75-adf48516f435 | -11.193 | -44.816799 | 2026-09-28 00:33:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a4f1e6e7-7172-39a7-8602-dda4fbf76598 | -8.3577 | -45.471802 | 2026-09-28 00:33:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 73da9da0-98e7-3e63-84ca-c0f705bfafe5 | -15.1054 | -53.8848 | 2026-09-28 00:33:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c89e329a-8118-3929-8479-f3ed99ffe24d | -11.4461 | -44.9571 | 2026-09-28 00:33:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c62e664c-6eed-3512-89dd-a58ddced739e | -21.5154 | -45.1222 | 2026-09-28 00:33:00 | METOP-B | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e55ae45f-1457-3a29-8718-85db06b906fa | -10.4263 | -53.793098 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4a8c5d4-8132-3703-9dd4-9823bdd16ba9 | -2.994 | -54.7551 | 2026-09-28 00:33:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 815c6f3c-0e5d-38fe-a86a-e706c60b2358 | -9.9776 | -45.372398 | 2026-09-28 00:33:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 99bd114e-983d-3992-8cbd-72eb126de225 | -2.7788 | -49.4991 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c34a3684-c0a1-3eea-a959-bb855c256f2c | -11.4502 | -44.933201 | 2026-09-28 00:33:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 67cbd800-38b7-3dd9-8d7a-eca380356368 | -3.0398 | -57.506901 | 2026-09-28 00:33:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43f439bb-3b36-38c3-8e57-6d730a11c0e4 | -6.7867 | -59.375198 | 2026-09-28 00:33:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d96a3fb-3666-3878-ab26-790594ab2bf8 | -6.687 | -45.682499 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41fb474e-ee3f-37cb-a3a1-f68fad6db045 | -9.9679 | -45.375 | 2026-09-28 00:33:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e50056d-c909-320f-a41a-d6f0eb8bd653 | -13.9673 | -54.000999 | 2026-09-28 00:33:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9703400-7e8c-3470-b4cd-15e0aef36bc2 | -11.1251 | -50.067001 | 2026-09-28 00:33:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf4728c6-f49d-3cff-b613-dd2a7ea78d4e | -7.2843 | -55.580898 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4e20c5e-0dae-3e2c-8e7f-043c623d996d | -12.6849 | -47.330601 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e595a13f-d9eb-369a-a222-440ce9f9ee2a | -2.8967 | -54.102798 | 2026-09-28 00:33:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a318aaa5-4783-3064-ad43-18f10dc02b66 | -12.2031 | -50.382599 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07c53b0b-1f5f-3aca-bf72-5bd31dc75f7d | 1.6559 | -55.9277 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 108d4d93-1d6f-39e9-abfd-5a070a9ddd70 | -12.6803 | -45.020401 | 2026-09-28 00:33:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa9c6b8b-d424-3b85-bbc2-6ffdb5ee1cca | -11.1071 | -51.337502 | 2026-09-28 00:33:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75cf8d94-4bbb-323b-afd2-37cdd2121c9c | -2.7691 | -49.5014 | 2026-09-28 00:33:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ffee58d-36e2-35d5-a1d0-28e82c33d112 | 1.6657 | -55.929901 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b661bbd-b3b0-3149-b241-b17d18bf89dd | -3.5068 | -50.3269 | 2026-09-28 00:33:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3674c0bf-e365-33e5-bb5e-458f2ac9393a | -11.6834 | -44.564201 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aeb00dee-3135-32b1-ac3b-c75f41c86c9c | -12.1911 | -50.375702 | 2026-09-28 00:33:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a8876a0-249b-30a8-b5a8-499cf81fc704 | -1.8218 | -55.312099 | 2026-09-28 00:33:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06480636-f4eb-3cbb-8fef-705680a3142a | -13.0991 | -47.4147 | 2026-09-28 00:33:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04c537fc-4403-3f62-bf56-c9d9d9e2caca | -9.9767 | -50.145302 | 2026-09-28 00:33:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34c64ab9-3065-3856-99e3-e45dd8e05b21 | -22.4541 | -48.5793 | 2026-09-28 00:33:00 | METOP-B | BARRA BONITA | SÃO PAULO | Brasil | 3505302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef168601-f1cc-3e58-8eb6-703fb63d862a | -2.5538 | -58.048401 | 2026-09-28 00:33:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f52cbce0-1b51-368a-95ea-045207c5a3c1 | -11.693 | -44.5616 | 2026-09-28 00:33:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da1a66e0-8711-30b1-97ae-3bb11d5462da | 1.6722 | -55.9464 | 2026-09-28 00:33:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c05cca5e-5c7a-38b4-b685-b90b97fd7a42 | -6.6491 | -55.095501 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68fce31c-0891-3574-923f-0ee0ebcd5b87 | -6.6755 | -45.636501 | 2026-09-28 00:33:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95e76a69-206f-3e8e-9b3a-752b3200d00d | -15.4052 | -47.901901 | 2026-09-28 00:33:00 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| df2fccfe-a5f3-329e-8115-96faee8b0c2f | -1.825 | -55.326302 | 2026-09-28 00:33:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7cda8d5-b54b-3349-9bc0-74a287af7882 | -13.4682 | -48.606499 | 2026-09-28 00:33:00 | METOP-B | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 280f1c05-2b7a-3fac-8522-bc5a682df7a8 | -6.2633 | -55.485901 | 2026-09-28 00:33:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 019b4817-3f29-3e6b-b94d-b416e4931f75 | -7.8212 | -55.127998 | 2026-09-28 00:33:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c35f466b-bc9c-3584-ae8e-7dd98d5bc67b | -10.4115 | -53.818802 | 2026-09-28 00:33:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3742d4de-62aa-3320-bcea-6590dc965c9e | -7.7204 | -54.7733 | 2026-09-28 00:33:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61e6cbdc-f016-3c1f-81c5-ad69911c1962 | -20.185699 | -48.5868 | 2026-09-28 00:33:00 | METOP-B | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 55589354-378d-3f83-babf-d675d6994225 | -8.2288 | -45.4829 | 2026-09-28 00:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 92f923da-eb0d-3cdd-a467-93e2bd1fa384 | -3.1953 | -51.039 | 2026-09-28 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 6db35e8b-eb3e-3226-8485-e74039d16690 | -11.4425 | -44.9303 | 2026-09-28 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| e2f18dc3-1eee-3093-a8c1-5e44db11ba7f | -6.6627 | -55.1112 | 2026-09-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 271b9673-0b96-3d35-9c2e-1cc0f12ba2f3 | -6.7064 | -45.599 | 2026-09-28 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| d5c0e8ac-5146-375b-8d8e-7b8cea46fd1e | -6.6442 | -55.1122 | 2026-09-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 4f92529f-5be9-38b4-b532-597fa68a460f | -8.0373 | -54.8926 | 2026-09-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 032c7609-e7e0-3dec-bf27-2e8822897803 | -6.7057 | -45.6667 | 2026-09-28 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| f23512b2-8301-3c07-ad32-15b881836868 | -6.6443 | -55.0922 | 2026-09-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| c0cf3ad5-b13d-3571-82c8-75cb79f61cf4 | -6.6628 | -55.0912 | 2026-09-28 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 07aad33c-ae91-3fdf-9b65-ce33f7b52afa | -6.6872 | -45.6456 | 2026-09-28 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 249.8 |
| 8c2423bc-c018-30e4-b683-2d202579bafd | -2.9082 | -54.1108 | 2026-09-28 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 232a08f8-81ef-38bd-bb0b-f2b0ed866238 | -11.3436 | -54.1086 | 2026-09-28 00:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 4bc88dfe-b8cf-33b3-bc44-b511f9005875 | -6.687 | -45.6682 | 2026-09-28 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 42639b8f-0e86-319b-b747-f84d5cd7fe82 | -9.9973 | -50.1393 | 2026-09-28 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| bd5e40c8-5131-3d06-ad82-d6a2e02b0aaa | -6.7066 | -45.5765 | 2026-09-28 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 1fb3b087-1665-38ce-9098-dda278754517 | -3.2137 | -51.0384 | 2026-09-28 00:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 1b514880-0fab-3412-b166-b1b88a8e44b1 | -6.7059 | -45.6441 | 2026-09-28 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| b80253af-a49f-34b8-b903-b8055d81e158 | -2.7767 | -49.4765 | 2026-09-28 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| d58cf902-fe83-32f5-8bcf-3660257d3ee0 | -11.4429 | -44.9072 | 2026-09-28 00:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 852779ed-640b-39c2-8603-93b692f7651b | -9.9266 | -60.7171 | 2026-09-28 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b6c1546d-7874-3925-a8ea-82369cd65053 | -2.9081 | -54.1309 | 2026-09-28 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ba6d0b34-63a1-3fa8-a8ef-31ae4faf2fd5 | -11.0959 | -51.3443 | 2026-09-28 00:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 02cff1a5-6f82-36ee-a307-fd3c39fb2a59 | -2.7766 | -49.4977 | 2026-09-28 00:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |


[Clique aqui para ver as próximas entradas](README7.md)
