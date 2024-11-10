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
| dfd7f79c-2205-38cc-8c89-9bca5c83b9f8 | -2.87414 | -51.47798 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| a6335d4a-9102-3083-a3d5-892d2bb34d8b | -4.51483 | -45.70231 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8c4fae3-ab00-3634-b294-5a9c60191d6b | -2.83615 | -46.6445 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 609057c7-74c5-3289-84d0-56cef800ffd5 | -4.43468 | -47.24762 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6388198d-db86-3b3f-a839-1a01361bd2bb | -1.87261 | -48.45431 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| fb483424-2828-3582-bf19-e058a8c5ebc1 | -3.03812 | -51.53151 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 560ceb9f-8a10-39af-a02b-0053102e44b3 | -2.2293 | -46.62331 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dba851a-3aa0-334b-8ce0-215896c9c312 | -2.65097 | -46.0331 | 2024-11-10 04:14:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5e56096-7520-3a8d-a0e6-f171bcd641ba | -3.203 | -50.63841 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 912b2c6b-7d5f-3422-a69c-5deaf516cb59 | -2.08774 | -46.5185 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bfe773f-87b5-3d68-bb77-46d2aa80d9bd | -3.23637 | -50.44558 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf053095-41b1-3854-91f1-92b0844baa36 | -4.94858 | -48.45003 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 931ad257-3a41-3918-99bc-881288760d40 | -4.90225 | -47.46693 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62a64570-7693-31fa-94b0-57287f37b9c2 | -3.34865 | -50.36106 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 05c5e873-650e-3bb4-8e2b-be8f3883399b | -5.37975 | -42.75478 | 2024-11-10 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5fa3b61a-a55e-3a78-9741-b8aa85bc73d0 | -4.62068 | -45.65208 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d32ad57a-fe32-3af5-bde6-d719ef02acd9 | -2.65836 | -48.47779 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0387faae-906e-309a-ac88-c4e8b3e71444 | -3.355 | -54.12918 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcbff300-197d-3e8f-a80f-0b7aeaa436c7 | -3.2698 | -53.70906 | 2024-11-10 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2912ee04-6f3b-30e0-82e8-8d55b1774988 | -2.24471 | -53.77498 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 37015706-8b18-3754-a5a3-bfe2d191cb8d | -4.43976 | -44.6231 | 2024-11-10 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6763af47-93a8-361c-8fca-bc6945fd549e | -3.10997 | -45.2989 | 2024-11-10 04:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3b8e9b1-f8e5-36c1-9468-8e0a74b68d9e | -2.23851 | -53.77399 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a284cd3-528b-3600-8fff-4cbfe1f55966 | -2.48727 | -50.27762 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 684c8a81-64b1-32ac-8cc3-4a55ef6b233d | -2.30247 | -48.50485 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e8dddeb2-aea9-337a-a267-9ac2c3ede2f5 | -3.24753 | -50.31951 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9901531-3a9c-3c01-bfd3-b45302f48bf8 | -5.25529 | -48.07993 | 2024-11-10 04:14:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7d71b96-a843-3540-a5c9-87654767f9d6 | -4.06231 | -49.21022 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5560f086-1ad2-3838-ae57-eed953126f78 | -2.07883 | -50.34727 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57589ad5-28f5-3f60-b547-ad62351d7c18 | -6.20496 | -42.05507 | 2024-11-10 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d3c99b7b-a833-323d-b606-c8d51de38ff5 | -3.3586 | -50.12648 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d3fad4f-fa09-3122-a19c-d1ac171b60e0 | -3.22201 | -50.38181 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 575834a7-e582-3956-86a1-90c98fdbcf06 | -5.8191 | -44.11926 | 2024-11-10 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56d0d0c8-6e49-351d-8764-5cc49ba4ad60 | -6.15337 | -41.14494 | 2024-11-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 429698cf-cae4-37ce-8777-eb3b213a4489 | -4.50321 | -45.72963 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f333778-a868-3257-b824-7b847535ecf8 | -3.95586 | -49.00341 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| df86e88b-b118-3cac-9403-ec30ae6f6694 | -2.95861 | -48.7231 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab3564c5-6b0c-33bd-87ca-61c1070860cc | -2.31851 | -46.48232 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd80e048-fcbf-3cb3-aaae-ce48a08c2125 | -2.62841 | -46.77047 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cc60e1d4-c836-3c2c-9034-75d009c68632 | -3.15013 | -45.93816 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35f52496-ba95-38d2-9dff-dd966e8fc86d | -3.04164 | -50.37717 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dab0572-a2de-32e6-ae55-b4ae670aa138 | -1.84832 | -46.28906 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49eae201-91e2-3156-b69c-ceac5de11640 | -3.96728 | -48.18841 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10cc4789-059c-31fc-a5c1-9a416c5fd16c | -2.17547 | -46.42879 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5e23c79-e2e6-3ce3-9d4f-9c3067b2e8f0 | -3.75443 | -44.64934 | 2024-11-10 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ff82ab5-e7b8-3428-baf9-40c55a0ca0b8 | -3.57029 | -45.822 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ebd71fc-345c-3ff7-8b07-d25958a5977a | -1.66961 | -50.49326 | 2024-11-10 04:14:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 348d1872-9aec-3f89-8ef0-171964cca24f | -2.40741 | -48.52533 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2dd6548-8c99-3674-aee4-ed2147f487b5 | -3.02389 | -48.03609 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5d398dd-387d-3a19-b7ad-883e0a76ce7b | -0.04523 | -50.78711 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3aa08b78-3502-38c7-8fa7-4451fbf1d7f3 | -2.38124 | -47.93195 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f0e45d1-05fe-35ee-8f84-3cf7f6495642 | -6.103 | -44.76004 | 2024-11-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc4db644-ca57-3327-8532-ed741263919a | -3.45658 | -50.18829 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6501d757-3bc1-3882-ba07-b883139d2f29 | -3.0975 | -49.41533 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 12a37852-2601-3a97-888f-0e5438da658f | -1.99678 | -46.35714 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a46f5a6c-370f-3a95-ad7f-6c6caca6e5e9 | -3.88861 | -49.98539 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 032bb191-4051-344b-aca1-43c53a850ba7 | -1.16495 | -52.08828 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 32fdd0cd-fc40-3ea7-a9fb-9b6fbaaa417c | -1.25727 | -48.32137 | 2024-11-10 04:14:00 | NOAA-21 | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 680fb543-2509-3864-a017-6bac0b25116b | -3.29239 | -53.25315 | 2024-11-10 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8264746-7adc-3a96-ad5e-22d0d7ca3254 | -5.41919 | -47.70082 | 2024-11-10 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c439b7b-d057-35cf-9f7c-ca52f1d5000a | -2.5314 | -47.38156 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98cd03ce-b018-39cc-9f3d-1ea5c9f51fe7 | -2.20076 | -48.37965 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b5f59ef-622c-3f7b-b44c-6f2a0502256c | -4.27559 | -50.66883 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9ce020b9-be9d-3550-80cb-2ed1e66e531c | -2.40436 | -46.50373 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf591601-bac7-3d47-9ed9-d7eb45f6244b | -5.59032 | -46.25404 | 2024-11-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 269e27ea-e053-3b6a-916b-bfdf83853653 | -5.59097 | -46.25 | 2024-11-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6722d952-199e-3f3c-b83a-572abcdeabdc | -3.23071 | -50.30936 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70988384-2daf-3128-b47e-413b7df8bd1b | -4.56467 | -49.59537 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd5ae0ea-ab97-31bc-af68-491dc4f5954a | -5.50244 | -43.79678 | 2024-11-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cf9ccea-2f34-3ba5-9e91-72158f898d60 | -2.94308 | -49.49474 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4dc98eb3-dd0c-3938-b1e3-d736e66dbea2 | -1.19665 | -51.99933 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21eca37b-ed21-3588-9dca-74535d0f6cda | -1.52811 | -52.21205 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 798a5ec6-3b32-3ce6-b0f3-e04b8daa03e5 | -2.93446 | -51.47401 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 340b275e-6c59-383b-9105-27639d4f1cc4 | -5.36984 | -48.24536 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89a4b8fc-dbc6-30e7-a73b-663a28739391 | -2.90067 | -46.82286 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0e460c6-8148-30d4-aae6-428502311167 | -4.19142 | -48.54398 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26213829-65ad-3d73-8386-bc6d6d5b768e | -2.45988 | -53.69014 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d852a177-66c2-3c55-9fe6-49de71f57fca | -2.2484 | -46.5051 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 529a671b-4f49-3ecb-adfe-8dbe10b99fd1 | -2.23697 | -46.55159 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b45505c-3932-3a3d-8726-6cf28caab7c5 | -1.0562 | -51.74734 | 2024-11-10 04:14:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6fd8d78c-9bcd-31ce-9abb-23f36c3ceafc | -6.13309 | -42.56798 | 2024-11-10 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1e8c6cd5-2d92-3fee-b28c-c61c76bdf436 | -4.45897 | -45.91528 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c2511a1-61d6-39c7-afde-1c08b4c4a7fb | -3.95959 | -48.18338 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e77d4f93-bbfc-378e-88d8-1067e0b5a8dc | -1.34716 | -51.4066 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 73e37268-48a4-3576-8dc9-1fd65b9469ab | -3.84012 | -44.13177 | 2024-11-10 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 075d9c38-f667-34dd-8a15-af0fac015360 | -2.42626 | -51.95595 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 28ae402a-53f4-3d13-a76f-b7ba995ee767 | -3.03296 | -50.30913 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d27a8363-0158-3e15-936d-f6d347927811 | -3.46223 | -50.1838 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6f14261-8a58-317e-9f0e-3e47308b3f82 | -2.61925 | -51.74821 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 422b9e30-1ee7-3a42-875c-80895ba64dac | -2.65358 | -51.87883 | 2024-11-10 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 98493f49-ef2a-3161-a5cd-e6be433a1eb7 | -3.29958 | -42.37192 | 2024-11-10 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f7d3a9c-e492-35f4-b289-713ebff1f35f | -5.47415 | -44.61625 | 2024-11-10 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82bbd4ea-f3a4-31c0-82f8-d789d3059765 | -3.35039 | -50.05662 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7960797e-9d59-3fc9-8dfd-c047fb94378a | -2.77309 | -49.35523 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19426d3c-07d7-3c15-9203-075668c918ac | -3.51966 | -44.02681 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f69d7183-dbae-37bc-b64e-adcff654e415 | -1.82838 | -51.3505 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 527a8134-4e6b-3e25-bf71-587aca43f154 | -6.41025 | -42.49011 | 2024-11-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 18f2fc8a-113f-3f1f-b21b-643c096a9eb5 | -2.62455 | -46.76987 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1c8f8b2f-b30b-3e87-b19f-a940fc268d73 | -5.58088 | -41.69757 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9fc4ad53-dc33-31f9-a95c-d9d69f79bca2 | -6.4519 | -42.74923 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README32.md)
