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

## Dados Diários - Página 106

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57d5d96e-4428-36d5-aec7-031c2635773c | -9.52823 | -50.20483 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a368843c-4a37-3abb-b981-b8907589e16e | -9.5272 | -50.18944 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5db0a62-11df-3159-aac7-86ab856f4269 | -9.52481 | -50.20427 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8bd73dc9-f056-3541-99e8-8f0ece45f87f | -9.51355 | -50.18718 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9d58dbe-b29d-35f3-b71b-65334240b042 | -9.49749 | -50.19976 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52867ba9-ffec-3d82-9771-913709e6c74b | -9.49408 | -50.19919 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cd29d8c-efad-360f-af5d-0830ee10a52b | -10.49736 | -50.25899 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12fe54fd-286e-3aad-83ed-2b60a2332aa6 | -10.49455 | -50.25475 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88dcb19c-9f89-3c8b-bf01-706b53f7d50e | -10.49396 | -50.25843 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f03d4c4d-aa6c-3ead-994d-e15c2b066375 | -10.48836 | -49.79861 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2846fc35-83ee-3ce2-a395-8a689a6ae977 | -10.48499 | -49.79805 | 2024-10-04 04:32:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c67d542b-2145-3022-a297-cb7ee53abc0f | -10.9538 | -49.57733 | 2024-10-04 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cce431a-dd1b-39a0-81d9-1a822aa83bbe | -10.91577 | -49.72838 | 2024-10-04 04:32:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7135ffe4-d28b-3aea-80e5-d990e0f5b6a7 | -10.87355 | -50.11719 | 2024-10-04 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2f4579f-daa8-3590-ab77-4f939155b992 | -10.87194 | -50.10573 | 2024-10-04 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65027b1e-1c58-3d7a-8bde-fb03cdd3fbc1 | -10.87076 | -50.113 | 2024-10-04 04:32:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dde50197-3eb2-35ce-89e0-3c8f85986452 | -3.32216 | -50.07354 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e8a96f8-96b8-38b1-8e1f-61f5db3dfeda | -3.3215 | -50.07764 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| baa76e3e-df44-32aa-aeca-c6dcb1d4bd7d | -3.31856 | -50.07297 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fca9ce6-f684-3f5b-a3c1-3c77d937a13e | -3.30926 | -50.45797 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9c22808-bc94-347a-91d4-bd8f2e306770 | -3.30422 | -50.46599 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ff27a21-ceb2-3b5e-95ca-ac5c8956dfe3 | -3.30328 | -50.44823 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 75879289-38cb-3d29-a685-12c61c646171 | -3.30055 | -50.46541 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da18ee21-0d02-3d24-8c40-7d8ae52c1b9b | -3.29688 | -50.46482 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9db819-3bc2-33d7-b19e-9ecdabb4b0ab | -3.29593 | -50.44711 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d73d9e49-ea21-3f83-a71a-e0f88a54be97 | -3.29525 | -50.45135 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0d9d9af9-2066-3726-bf06-9baada2560ef | -3.29457 | -50.45562 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d663962f-d448-3cf7-9a44-a592eb6c8d9f | -3.29226 | -50.44652 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 2cff809e-341d-3127-92c9-b0877e0edc81 | -3.2909 | -50.45503 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| e29a911f-33f7-32a4-84f9-8b1b1bf4b2bf | -3.28859 | -50.44593 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5b94e3fa-8c80-3939-88c8-4e61b5ef68c8 | -3.28424 | -50.44959 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c273b886-f908-3b8d-b12d-327936d87d18 | -3.24815 | -50.13865 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c342db78-df9f-3262-8a43-fdcd27f5620f | -3.24762 | -50.37376 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1d29507-cb8f-3285-b840-4c5a0a261c38 | -3.24693 | -50.378 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b393f3e4-0491-30fb-ab87-e77ec1cca28f | -3.24496 | -50.48299 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab78289f-80a2-3ae9-9252-38b33c150281 | -3.24465 | -50.36893 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fa75bb07-bad5-3702-a1ef-911cd00e7c2d | -3.24396 | -50.37318 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| c906fa61-e661-3f9f-be3f-a52ab22ac85e | -3.24099 | -50.36835 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d0a94bd5-6875-3795-af4c-d5a19b38be7d | -3.23664 | -50.37204 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49382e22-828c-392c-b38b-4add3ec08ce4 | -3.11233 | -50.4718 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 440a5538-d795-3256-bb7f-759544784834 | -3.10794 | -50.47555 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59bc1004-de12-33a1-9480-6113c228e9c0 | -3.10568 | -50.47261 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dba7a561-65e7-3e2b-88df-22748c6186a4 | -3.10497 | -50.47063 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d600364-1342-38dd-a935-568d41faef8a | -3.10267 | -50.46772 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77a65588-b184-329a-a3c8-1b6afa1b2f9d | -3.03708 | -50.45283 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9e814bae-06e3-37f0-b209-43ff60817588 | -3.56308 | -49.44844 | 2024-10-04 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc3c4c9e-31e8-3266-9b5e-fda83ab09a87 | -3.28773 | -49.52498 | 2024-10-04 04:32:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94d35a6a-49db-3cf3-bbe8-12001b8b24d3 | -3.2871 | -49.52888 | 2024-10-04 04:32:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd34dbfc-4f0c-3a70-8769-7716710f74fd | -3.27081 | -49.10818 | 2024-10-04 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 976fdb08-f06d-3e7f-b7dd-cb02a89f7cba | -3.26675 | -49.11139 | 2024-10-04 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efd0a6da-d44e-3736-b7fb-27622f12c2ac | -3.25714 | -49.44149 | 2024-10-04 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f35cc1b3-5ac5-3b4a-a971-8ebabe2b755a | -3.3179 | -50.07708 | 2024-10-04 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 446cd63f-444c-3c23-83d4-d3931d415c22 | -3.31062 | -50.44938 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8b802126-3b44-3354-9298-3689daa27901 | -3.30994 | -50.45364 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 56d9e017-90be-37f3-998a-a9de8b850019 | -3.30857 | -50.46228 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3ec8a70-5975-3cc9-b3c9-2ea5f2805273 | -3.30695 | -50.4488 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f721b46c-27ef-3a05-a857-94f2be656fa3 | -3.30627 | -50.4531 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ec39622d-1949-3274-a1d2-ed3ff3b7173c | -3.3049 | -50.46172 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 09e0bdc0-a6f1-39e9-9c47-2e75add2f935 | -3.30259 | -50.45253 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 19f83897-c8a9-38cf-a91d-77060bbc8e87 | -3.30191 | -50.45683 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| a987d8d8-4f27-3f00-923b-aa9ae3843e77 | -3.30123 | -50.46113 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 92c59acb-7a6c-340e-a0f8-2d86c5acb204 | -3.2996 | -50.44767 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| aa8d0f3d-eb5e-3d5f-91c9-95d80bc66e0c | -3.29892 | -50.45193 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 09b22eb1-9271-3ade-91de-160997dd4684 | -3.29824 | -50.45622 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| cfc6ed33-4317-35de-8c3d-a563239cb548 | -3.29756 | -50.46054 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 82e66e5d-4aaa-3fba-949f-75232c6c08e0 | -3.29389 | -50.45994 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ec481202-08c2-3fce-9b37-ccf8506692cd | -3.29158 | -50.45076 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 78472acf-0065-314e-b554-cf4520111bd6 | -3.29022 | -50.45932 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 258eafab-c984-3b3d-b5d9-9e1fa68109b6 | -3.28791 | -50.45018 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c39175cb-aace-3288-94b4-c8eb02df3088 | -3.28723 | -50.45444 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| f31a16ed-7829-3557-bbf9-abcff895ca76 | -3.28655 | -50.45872 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| b358f4c4-2c6f-3591-9075-97e09b5380ff | -3.28357 | -50.45383 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e55fe99f-f6e9-3e75-b242-4292a808af1c | -3.25699 | -50.10618 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c260ca4e-cf14-3722-a5da-4f5225fc9a79 | -3.25538 | -50.1398 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 295ff36d-41d5-3834-aeaf-9216c358260a | -3.25338 | -50.10561 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 236de828-394e-32a3-a8a0-d68382deab48 | -3.25177 | -50.13923 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fa72352-312a-3130-a67e-5a3310735e92 | -3.2483 | -50.36951 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42ba5e5b-5cde-3eb7-872e-12f165a8454c | -3.24603 | -50.36045 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2019c769-c24c-3fa2-8c41-2ae974290066 | -3.24534 | -50.36469 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7a22c3b-9ab2-3e3c-b094-8e89fc8f8068 | -3.24327 | -50.37743 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4a731f9d-0bee-36e1-8d88-cb7a395c656c | -3.24168 | -50.36412 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9833ecb7-92fb-3352-bfa1-f2e48f105c04 | -3.2403 | -50.37261 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 2fa64b32-18d7-3c3a-9032-5ca08d20763e | -3.23733 | -50.36779 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6896840d-867f-3e34-bdf1-34cb7647aaf3 | -3.12927 | -50.18091 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4ff1aed-a2d7-39df-81f9-bddc5c0c4570 | -3.12631 | -50.17612 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58c09b33-fa00-38d5-ba65-ef484f4eeb93 | -3.11162 | -50.47613 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdd18b15-3bc5-30cb-b207-1acc352d7e0c | -3.10936 | -50.4732 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7554d645-7ed2-31c8-a6b5-cea3711e3037 | -3.10868 | -50.47755 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 212d8b37-2a3b-35cd-8b2c-be55064cb294 | -3.10865 | -50.47121 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1edf1abe-eca0-34af-9ab9-82988f13b1c1 | -3.10636 | -50.4683 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27baeb72-9f6f-377e-8a3e-cdc3e0fe0166 | -3.10567 | -50.46635 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdac3a5d-d855-3cd3-9aad-97f0adf6b758 | -3.27021 | -49.11193 | 2024-10-04 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6909833b-8dd3-3d58-a026-bfcc5b5201e6 | -3.39464 | -50.60264 | 2024-10-04 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4837e4ac-a53f-3868-8324-b21aba555d57 | -5.06274 | -49.79489 | 2024-10-04 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63c74061-63e3-3874-b031-368eb89fd8fe | -3.99298 | -49.67129 | 2024-10-04 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f20cec68-bb6c-34ce-a559-4cefb5d83c92 | -3.92938 | -49.68579 | 2024-10-04 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4fc2703-352b-3c72-8309-6b4cec473040 | -3.92587 | -49.68521 | 2024-10-04 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2403fd03-4653-3a07-91df-4a54994cae15 | -3.92525 | -49.68909 | 2024-10-04 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec751d43-fb06-35cf-890e-015ce8a699cc | -3.84582 | -49.39751 | 2024-10-04 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 660a0c27-6e7d-33ec-8b29-ab6f05795f2b | -4.6527 | -49.5332 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README107.md)
