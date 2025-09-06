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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a06bef2e-a031-3a3e-8670-4d5607323c6f | -6.64201 | -43.41645 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd98d327-7a83-3679-9d93-f0e4c1551693 | -12.97588 | -54.82108 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d623851-5356-3ea7-b8d0-4147797821a1 | -8.88174 | -47.91656 | 2025-09-06 04:17:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7db08225-bdc0-38de-b74d-656fb0bb7799 | -6.00973 | -46.68969 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed16d29a-a1c3-33af-ac7d-7ef1fa8b57b6 | -5.69436 | -45.11373 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce8bb1d2-07ed-33d2-90b0-8438e3f3b7f3 | -7.76319 | -50.74018 | 2025-09-06 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b7d14379-60b3-39db-973f-3d18710c5d29 | -15.60831 | -48.24568 | 2025-09-06 04:17:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2564c150-edc3-3932-9a37-b9fd2ad9ff0c | -10.59784 | -44.32582 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4ecd799-4fbb-314f-bbf1-2ff0a7778340 | -7.80549 | -45.42929 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e33f5a9-ae67-3214-ad4e-570210af2dec | -15.35854 | -46.40612 | 2025-09-06 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e6d500f-016f-37a5-9866-9690cf7d42ad | -4.48546 | -47.67846 | 2025-09-06 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9341b544-c847-33d9-ba46-cb5dfd9e3afc | -6.64534 | -43.41698 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48f81667-a6fa-3238-a073-e45fccabdb0b | -14.90255 | -49.4502 | 2025-09-06 04:17:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71949016-681a-3568-b5e3-5ad418016d4c | -7.42323 | -44.94852 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e5437cf-a4f0-32a5-890c-20df3a6308d4 | -7.59406 | -44.66558 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f0b1db6-40de-37d5-befd-5e37c21b5ffc | -12.95415 | -54.81232 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eae34d0e-cb24-3801-b245-73dd8a0a9778 | -6.36658 | -43.53691 | 2025-09-06 04:17:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f50af30-d8aa-3bf2-8f50-813903711736 | -7.80083 | -45.42551 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25b7ea1a-e0bd-3a2d-ab83-4e7eb00cb191 | -2.55072 | -48.39057 | 2025-09-06 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49d8df65-51f2-34e4-8755-e5ed4af20b38 | -3.24876 | -50.80353 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c746b752-4e1c-3c28-bc4a-976e068886e4 | -6.42308 | -45.89523 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2abdc46-0cde-3337-a9a7-1646aee7e254 | -8.03676 | -44.0689 | 2025-09-06 04:17:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7a9d758d-499a-3343-a19c-5bf85e2d2eb5 | -5.94714 | -45.66519 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| af837f20-e92b-3edf-a15e-be4ffaab522f | -5.63 | -44.99874 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fdeec11-85c9-37da-bd28-f34cc5faa84f | -9.84197 | -48.83381 | 2025-09-06 04:17:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27aa4178-dc24-39bd-8234-876234b3d10f | -6.17108 | -43.2744 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60a34581-0293-3d0a-b3af-9eab5d41cf37 | -5.94636 | -53.79238 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1f385e3-d4e4-3bc7-b331-539fe26d05c3 | -5.17452 | -43.11233 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc238e17-59e2-32db-9f55-b5438fdcf927 | -7.72758 | -50.312 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 89dc03da-b47e-348e-9d59-a5daf5558bd6 | -7.02233 | -43.23812 | 2025-09-06 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 13e84369-66c4-33eb-b866-7070c1cb79c8 | -7.72409 | -50.30901 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e001fc4a-9b91-3280-a4ff-45de0a75f636 | -9.17937 | -46.02982 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 753b2563-8b42-3a83-8f50-8105ef059ed0 | -7.58372 | -49.2851 | 2025-09-06 04:17:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e300ceed-5df8-3b6a-9d4f-327d1cd65420 | -10.0407 | -48.12564 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dc5f24c-d3da-37ad-a53f-efb757883744 | -6.59388 | -44.5468 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 89dd8af8-41be-3cf8-9ad0-f21d1f766b11 | -5.68222 | -48.12901 | 2025-09-06 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482bf330-cdd6-3e34-9479-31b94f22f1fc | -12.95171 | -54.79536 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 419cf6eb-b91d-3c1c-a092-f6cc0954a3db | -13.01081 | -48.06644 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33cf4efb-cf51-378b-92a7-4e4538e47cfc | -6.20308 | -44.19702 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db39641-58f0-35dd-b220-952f9b88ac5e | -12.48397 | -53.85989 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85992bbb-8860-37be-b62f-a5e43bf16547 | -6.20283 | -45.04487 | 2025-09-06 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc4ed837-7a32-3966-b818-4745f1864c92 | -14.83009 | -48.18438 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 87bb9a0b-ef7a-37f1-bfc3-fa0320370bec | -6.38809 | -43.01315 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53562ba7-67e5-3c01-b28d-ba9e67b51656 | -10.31443 | -46.41538 | 2025-09-06 04:17:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4842525-1e49-3cfa-aba3-686fb64627fe | -13.0058 | -54.8478 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1bfbda1-f7e4-38de-bcf0-0a3bdbea06fa | -6.01722 | -46.69085 | 2025-09-06 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a61e758-71af-3cdf-a3ce-73d8b073d231 | -5.92629 | -47.28778 | 2025-09-06 04:17:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fbfd392-4409-3342-b68f-8fbf7250bc86 | -5.20477 | -43.69053 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bebcbd27-9df6-3e06-bfbb-c3772064e9ad | -7.73812 | -47.42586 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7529b4f3-5efe-3519-882c-7b07421fbe24 | -6.8206 | -52.80722 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0ed7ba88-63da-314d-bcc8-0b2be49f121b | -5.81303 | -46.27716 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d8cd87a6-b3c8-3704-bee4-d0afb3ed9de4 | -15.17637 | -52.39711 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33e3dde8-4e1e-3958-ba3b-bedb9ea3c4c9 | -6.2739 | -53.43342 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52188fc3-c687-30fb-977d-371f68d76d50 | -8.47134 | -45.07801 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1198d83-8ad3-3469-9e40-bfb87897e479 | -8.0211 | -45.42506 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 220aaf1e-185b-31c0-ad93-e0298bf959c9 | -13.00075 | -54.81404 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c34478a3-e2ee-3da4-9657-a70325e56e9b | -14.53788 | -53.13363 | 2025-09-06 04:17:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a02a4e28-c631-32f2-8a9f-56f01c5b23b2 | -8.36885 | -52.56052 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2685dde8-9612-34b8-9833-49513ebc939a | -6.81442 | -52.80993 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| abfaee3a-9d1e-366f-83fb-3445360acf58 | -6.50203 | -43.08421 | 2025-09-06 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 418a6997-a30a-3d2c-b5e2-116b1a33b0b8 | -12.99766 | -54.82959 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d7c2be1-6404-371e-bfe1-d1086040a22b | -9.68331 | -51.11269 | 2025-09-06 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db846a48-bb6f-3212-84bc-44d7803caced | -5.68033 | -43.57499 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14c09910-2217-392d-b99c-2fe9baade546 | -3.24824 | -50.80657 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d2a11194-c8a8-36cb-9294-e16d760167cc | -7.23874 | -43.8551 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a456aca2-5759-388e-b987-bbd9b2ee8dc6 | -7.59399 | -44.68771 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a763f057-2232-3c59-9c98-46b141b41749 | -13.73908 | -46.917 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2db0e6a-5947-3fba-8d1c-31f7e6a9e51b | -7.3423 | -43.95047 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cdf3eee-b6c5-3609-ba79-d88dbbf397a5 | -8.51429 | -51.31917 | 2025-09-06 04:17:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 262fcd8c-f366-3478-9867-8b3f81d49f5c | -5.7269 | -43.91777 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e028059-1420-3db4-9879-84467bc6c338 | -5.86557 | -52.16677 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab597d44-5629-3143-9ca1-71a905dd0002 | -3.37475 | -50.84862 | 2025-09-06 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1701bcb2-65e5-3068-ba2c-d995158bc20d | -12.51656 | -53.84675 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d8632ef-86ff-3000-aece-08a6ac3732fc | -5.84823 | -46.10723 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b522dde-e56f-37d0-aefd-41e9b6fcd92a | -8.01987 | -45.43276 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c214ae87-7168-307b-bf67-e791bae38d95 | -8.09386 | -44.81953 | 2025-09-06 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3653290-f645-3761-bce4-d5757d08bd78 | -6.87593 | -52.78378 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00abc501-fa52-31a9-b5fe-54b631330cea | -8.87571 | -47.25615 | 2025-09-06 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79141c5d-fac5-388c-bb08-4eebe11217bc | -15.21819 | -52.35406 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d13af00e-32e7-3602-9be8-b3b0c95a64d6 | -5.82551 | -46.35671 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a72a185d-5afb-3585-bdb8-51554eefa452 | -5.66028 | -43.61492 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bac78418-962c-36c7-a954-9292756ce22b | -7.80203 | -45.42875 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b5bd966-58bd-3c70-93c0-af1adc80b63d | -9.68336 | -49.29088 | 2025-09-06 04:17:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9d70977-2a3b-33d0-b859-02f5b88973a5 | -3.24733 | -50.80273 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e36559f1-bbfc-3b10-85bc-c2dfb90966dc | -7.23485 | -43.85806 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bf31d6cb-645c-3898-81a5-b287527da386 | -5.63474 | -42.62402 | 2025-09-06 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c3e22650-5722-3af8-a255-bc19c4ec8da9 | -5.74667 | -43.7076 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d15283b-5e73-3960-959b-e24f8387d06c | -4.19771 | -43.34376 | 2025-09-06 04:17:00 | NPP-375D | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e0302c4-84a0-3186-93eb-896832744748 | -6.99599 | -45.64992 | 2025-09-06 04:17:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39feb5cb-67a5-3a8a-8985-b78dc3d4b61c | -12.84793 | -48.01246 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05b3252e-f8c5-3688-94b0-1d3eee7b0cd9 | -9.68402 | -49.2871 | 2025-09-06 04:17:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86d8415b-0e09-3cac-be76-118d7d94531c | -3.68672 | -49.57135 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c346c7c3-b9de-3724-b910-d525d70ffea8 | -5.44901 | -42.81147 | 2025-09-06 04:17:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b561a99e-98b1-34cb-a9e4-e882aece3eae | -7.63966 | -46.56012 | 2025-09-06 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcc4cf66-da66-3367-9355-0ac598b6d02c | -5.21091 | -43.6951 | 2025-09-06 04:17:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8faa908e-f6e9-3200-a30c-4e373f907598 | -6.60583 | -43.96658 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b63ef0bd-5d11-399b-8fd2-3cb071e9cb41 | -12.99938 | -48.05231 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81c35081-3a32-396e-b6a9-fbbbd207b233 | -11.64118 | -54.54449 | 2025-09-06 04:17:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 06faa1c7-18c2-386d-8125-0fecdf2f3a45 | -5.95874 | -44.73993 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51b72655-ac8e-39bb-88b6-54b56ec57b80 | -14.57561 | -48.09657 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README32.md)
