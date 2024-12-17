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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 674583e4-bd18-380c-abc5-8197fb0a49b9 | -3.60532 | -44.91086 | 2024-12-17 04:44:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fe6deed-37d3-3e0c-85b0-ea3dee40fcee | -4.02634 | -46.80491 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b209fc5-9ec6-3acb-8abd-8913acc1496f | -3.68386 | -47.15104 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98d7c02c-f8f5-3fb4-a1ff-4bfb85fadfad | -4.00766 | -46.92924 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7abf7357-fde4-384f-8f92-d6c48702ee0a | -2.76633 | -48.28745 | 2024-12-17 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2433363-09f0-3959-854d-dc51b0671c05 | -4.97022 | -44.96388 | 2024-12-17 04:44:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19ba2dd1-e92e-3326-b6b6-5a41d067342b | -5.31086 | -46.48714 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e9b68f1-41b3-31a9-9e27-085004756daa | -2.95237 | -52.57767 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee33961e-d6e5-3792-b00e-691d4aa087bd | -3.31748 | -53.86528 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94614fda-e2b8-33ed-b37a-8923c7143550 | -4.59281 | -47.05408 | 2024-12-17 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e1a49d9-17f3-3c61-897a-7001bb46043b | -2.60645 | -48.25567 | 2024-12-17 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e7d3e23-835e-3756-826c-03adc15f7d99 | -3.86694 | -47.03222 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f0a2f762-f737-3c79-a83d-2ebb84a45bd6 | -3.87364 | -47.03776 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c0bb125-a8c7-3302-9f5d-2f6913ab18ab | -3.50127 | -53.9496 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8c387b8-e112-37e7-b7d1-1f3b71dd251d | -3.79181 | -46.84396 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d119c0f5-590b-33e0-a717-9694553a92dc | -1.40713 | -47.47918 | 2024-12-17 04:44:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4c85c40-5abc-345b-8e8a-3925ef0aba9e | -2.7645 | -47.39091 | 2024-12-17 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae756e19-34f8-396b-a2c1-753e8c723b5e | -4.1057 | -46.68778 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3c6a039-4cbb-304b-a6dc-adbd5a739d15 | -1.17813 | -51.77009 | 2024-12-17 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa3696e8-864d-3d14-9d89-beb05fb083b2 | -5.36559 | -44.04455 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3aa1906-918e-3a53-a457-aef0ce92ce55 | -4.04022 | -47.01508 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c8a1c12-e5e1-330b-b8f3-58d4cc93601c | -3.95544 | -47.03477 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e917c6e3-f2b2-3d24-bfff-f63e25589cc1 | -3.10226 | -53.764 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c13ccc2-f34a-3862-80de-f62b9ecd9990 | -1.22142 | -50.69291 | 2024-12-17 04:44:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44edfe66-7ea9-3984-a16c-954f725906dc | -5.67984 | -46.50371 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c788ac51-7b9e-35d7-a4ca-bb6664189ce6 | -2.62618 | -48.6469 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6fa70ae-3ba1-31e7-9a6f-0d34a988da4d | -1.28092 | -53.18823 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4004651-02e1-3780-ae8c-48b2e4685a69 | -2.62278 | -48.64638 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 311266a9-469e-30f2-b161-2d6d3a2ad615 | -4.01749 | -46.81279 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37660777-e387-31db-af36-125da1c17071 | -2.9309 | -52.71234 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7c094a0-6e14-327e-b25c-fd274da566f6 | -4.07018 | -47.09064 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ada4e585-a31e-32dc-b69d-6bdd768c8f5b | -3.30009 | -53.36522 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6109a08a-cd62-39f5-85c0-2aa2f478c259 | -3.9598 | -47.03102 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 616e4e62-f882-3cbf-ab1f-7a66abfd6a3c | -1.05776 | -46.83565 | 2024-12-17 04:44:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e0126d-af2c-3f50-a701-7f1a70fb2475 | -4.0446 | -47.0112 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 884e39c9-a1de-38b8-b016-c59b542828cb | -4.7968 | -43.78188 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6da435a-3a84-315e-bb28-0ddd46daee6a | -3.66879 | -47.12693 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6928612c-5b20-3394-9e87-63a104f7e3e1 | -1.63264 | -45.85079 | 2024-12-17 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3c9c549-59e1-3954-8ca4-6d896bda825d | -2.65639 | -45.56133 | 2024-12-17 04:44:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26c93d24-bda7-3b02-a400-7bb727d259f3 | -4.10357 | -46.70161 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5fa1964-7f64-3c37-be63-cba7bc7bae33 | -1.29594 | -52.83287 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab915d99-811e-3535-a92f-183a5a0d4815 | -4.7074 | -44.38098 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d115d4d-5d1e-3e1b-823d-8bd4d15abb2e | -4.02879 | -46.86496 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 484126eb-774e-3b6a-ae0a-ca23e8cacd30 | -3.52966 | -54.69303 | 2024-12-17 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 236b6394-fda2-337a-9887-71cfc1d43811 | -4.20567 | -46.48273 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e8cae7d-9fa0-3094-8123-c7dd46f97e51 | -4.04831 | -47.01171 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39160934-200c-3e61-88f4-58c23e2fc1b1 | -4.07347 | -47.10748 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fccc0258-edad-3044-9584-99d2fb5d6472 | -4.01401 | -47.03791 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe89ef85-f2ce-3570-ba3e-69079a83f875 | -2.93975 | -54.17801 | 2024-12-17 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 261faa4b-54ea-310f-a526-ad2e005e932d | -1.91762 | -54.34163 | 2024-12-17 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecac9f60-243d-34b3-ab72-af2f22a8068a | -0.92385 | -46.90419 | 2024-12-17 04:44:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe4aed65-2dd6-3d68-a079-557170823e5c | -5.10088 | -43.90612 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9f24351d-1498-359f-b7e0-5443a4844fc4 | -4.01681 | -46.81739 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42fe145a-70ad-3f61-a986-7300d5484e33 | -4.09497 | -46.73252 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4d2f599-4473-3d9a-aa24-321d1f001e40 | -4.22191 | -43.98736 | 2024-12-17 04:44:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bddcab4b-1016-372d-997c-7bbd91c9ee26 | -4.47949 | -48.11738 | 2024-12-17 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce53db24-638c-3e48-a2a6-47c7af78d68a | -2.51652 | -49.05956 | 2024-12-17 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47eab8cc-56e7-3233-913d-c96f22b9a49d | -4.01627 | -46.81482 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc64b267-8ccc-3631-a99e-bbb3f8a35ae9 | -4.02411 | -46.89595 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b66298c-949a-3e25-8339-42fe883a48af | -3.43992 | -45.59562 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04e93b73-6d16-3d72-935b-cac0aa89b214 | -3.78606 | -47.11687 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cbcb88c9-05fa-3b0e-a8f8-543f7c958fac | -5.98501 | -44.59895 | 2024-12-17 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea44c729-6396-36f6-aec8-49c9e8cb38ce | -3.8752 | -47.04041 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 81c1a9d5-3c5e-3d15-ba8b-606a2a2f8dde | -3.02231 | -48.03198 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 728b1c1e-9ee5-383e-bcec-86479f0baa79 | -3.86913 | -47.03049 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f8aacd17-1d1e-3cfa-a21b-e288fbb7e6ff | -4.07716 | -47.10805 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a56adcef-d0f9-3fed-b49b-cda2f278479d | -5.58209 | -46.14295 | 2024-12-17 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fa2ac86-80fb-3ad9-abbf-d4bcc65b58ba | -5.93935 | -43.78706 | 2024-12-17 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac9f56b9-3d7a-3de7-9b8d-a1c84cb27720 | -4.00681 | -46.8998 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 737b0271-4187-36fc-8a02-74a61a21526a | -4.12464 | -43.56978 | 2024-12-17 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a823367a-4a4d-3ffc-9e31-01c859008621 | -2.76388 | -47.39495 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16d24865-8d55-3030-8608-b476116e0626 | -4.37793 | -46.54991 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6801b6a3-cce1-3ed6-8255-fb7df5649973 | -3.87063 | -47.03279 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a8521aec-6bdf-3eaf-9376-6b37dad29ebd | -1.29952 | -52.83345 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 620efea8-8573-392f-87ff-db435ea0eb3f | -4.03821 | -47.02819 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec1abd6b-a9fe-31db-a524-236c461e2e82 | -2.57156 | -45.95636 | 2024-12-17 04:44:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e8acd46-6e25-3c22-aaf7-c1ba09315287 | -4.79867 | -43.78048 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2f45b8d-dbd2-3781-ad4f-b9b1ac616d2b | -3.84732 | -45.86324 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33578154-e918-3129-a73d-e9364291693f | -3.30303 | -53.36993 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1674f4e3-6de8-3fba-9a50-d3b45b0b0bf6 | -4.22002 | -43.98961 | 2024-12-17 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a355059e-8e76-34b3-89f6-b846fd32ecf7 | -0.92449 | -46.90012 | 2024-12-17 04:44:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b42ce50e-dadb-3d13-a457-2ebed223f1e6 | -3.84411 | -45.8576 | 2024-12-17 04:44:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d3e831a-51ee-3857-873e-203de223f1ce | -2.7728 | -48.57909 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7f57f51-a3bf-30ce-b9fe-5e398284bd0e | -5.31012 | -46.49203 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba0af1dd-6736-389b-9f99-8ff603a6ffa8 | -3.71714 | -50.1621 | 2024-12-17 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2380c79-db10-38bc-98bc-d395f7666597 | -5.98908 | -43.47931 | 2024-12-17 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17eddf12-d98e-35b5-910d-732a7f82ae52 | -3.79553 | -46.84461 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81755b55-28a6-31c5-a074-bd11a6c46ef8 | -3.43335 | -53.98474 | 2024-12-17 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c54e4b8c-bdc4-34d3-8d99-000f443afc48 | -5.57809 | -46.14243 | 2024-12-17 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 650dfe1d-ab37-3c43-80a7-0ce600a5273e | -4.10428 | -46.69702 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3a2b020-3664-3d7d-880e-29787d03e08e | -4.2389 | -47.59072 | 2024-12-17 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3e6b4cf5-c7b1-36d5-9cd3-56004a8fabeb | -3.89782 | -47.18892 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0394e01a-96b0-31e5-a44a-90c24305f87c | -4.06378 | -46.91093 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdc06840-cc06-37c9-9b93-66abd7dd2ecf | -3.42684 | -49.66474 | 2024-12-17 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee8ed0d4-8af8-35ad-a26d-3d1b4892f7fb | -1.30246 | -52.83807 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c548add-8495-3ecc-bfcd-1f0ba24fe934 | -2.58011 | -49.41183 | 2024-12-17 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78f8f735-b09c-387f-ba23-b4dba21651d3 | -4.06883 | -47.0993 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b994af-cac3-3fc0-875b-95e0ea0d6bbc | -4.59349 | -47.04964 | 2024-12-17 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eeed5698-550c-3763-9c06-3faffcfc7564 | -5.98833 | -43.48442 | 2024-12-17 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f743cd60-3803-3ac7-ab12-e5e950da31fc | -4.72132 | -46.50943 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
