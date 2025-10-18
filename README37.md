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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15106321-56a1-3dd2-b815-d30e0e944502 | -4.4506 | -43.23751 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 58714720-089d-33fb-99e9-2c003fa81242 | -2.87132 | -50.73015 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fb6578e-10b7-3138-b68e-85c25013dc5e | -3.32357 | -42.78949 | 2025-10-18 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccee0404-72cf-306a-91ef-06a8c974753c | -3.06144 | -43.20685 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c7cb206-0257-33bc-8a3a-b42e17882b0a | -3.83509 | -47.4025 | 2025-10-18 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66b5152e-bc80-3dd4-a000-bce6de48d3f7 | -3.29505 | -50.01156 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc7563ee-e65a-33e3-a77b-54211db9facc | -3.94216 | -48.08551 | 2025-10-18 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf4dcca4-3efd-3de0-b9e8-b676208469f2 | -3.14534 | -50.24427 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| dcd92648-76a1-3681-ab00-1c385bd6f848 | -1.94602 | -56.65628 | 2025-10-18 04:27:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b8458710-d814-3f03-8462-d04af83d38da | -3.23971 | -45.97888 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52eb8b8d-c2fe-351c-baa4-06aff3a65f6a | -4.40635 | -44.36121 | 2025-10-18 04:27:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a4dc668-e133-3f4d-bb6b-8e130fc4602a | 1.76264 | -55.9814 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0773df7d-9d4e-34e9-901b-2ab936297032 | -3.23603 | -42.0719 | 2025-10-18 04:27:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 68a2f226-c58f-3b74-9e02-49ab9509e09f | -4.46244 | -43.23122 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d63899f8-9d24-3a27-81b4-30d59461c28e | -2.22582 | -48.37041 | 2025-10-18 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 817a9604-3847-3b28-a2c0-0faa5ce010e0 | -3.2419 | -45.96503 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0485e8e7-4cab-37e0-8e19-ba7bd72a3de9 | -2.86663 | -50.7331 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e92fd9a1-a430-3a6c-a8a7-b445cce12ab9 | -3.92317 | -41.73213 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9ee92e14-ad07-367c-90df-d2c69e18636c | -2.89565 | -48.06605 | 2025-10-18 04:27:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a8bf3f0-0ca4-3566-ba8b-6da4311137e8 | -4.45829 | -43.23464 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 546daeb9-043b-3318-bba4-01ca33929388 | -4.71404 | -44.36004 | 2025-10-18 04:27:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0cf89583-3777-3a95-973d-ae84ee641f1e | 1.75898 | -55.97781 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| cf67907d-fbbf-3ff4-b244-139566bdb87f | -2.87249 | -50.72289 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5906407-f1cc-3a48-b291-93bc5a20aa69 | -5.06589 | -41.21309 | 2025-10-18 04:27:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 71b95286-e37d-39e9-913e-80d3c95a1ca1 | -3.64683 | -45.26345 | 2025-10-18 04:27:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 366b02d8-8cdd-380e-a0e9-debdcc6a362e | -3.85161 | -41.57133 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 78a19aa1-2703-3507-be81-73c121b66188 | -3.05966 | -43.21837 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c04857fb-0669-3799-bfec-116e35c09194 | -3.06375 | -43.21509 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f463e8dc-4f5d-3ed4-8d62-e52ceb6b27f7 | -2.87893 | -50.7351 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae9e5bc-27af-39e9-8fc6-7e71f9412de4 | -2.8719 | -50.72652 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 220cfba1-7288-35d1-93ea-842797f70fd6 | -0.90492 | -47.54339 | 2025-10-18 04:27:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4d073f15-0aff-3fa9-9b3b-68dcccd92804 | -2.95336 | -49.33439 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 48c0d905-e35d-3cf5-bd10-1c04673149a9 | -3.45389 | -50.09452 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15465565-ed33-3e51-8c29-54f58a43ae77 | -4.0009 | -45.50359 | 2025-10-18 04:27:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b2369dd-33fa-34e7-ab0d-792b5ad4ac36 | -4.39835 | -43.43495 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15144f0d-8568-3dd6-889f-79830f99c2e3 | -4.40975 | -44.36174 | 2025-10-18 04:27:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45f17a1d-cce5-3de1-b7d7-23ca43a91087 | -2.734 | -48.30981 | 2025-10-18 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40e6abae-00a5-3906-9379-9f8edd2e120f | -3.2542 | -52.91653 | 2025-10-18 04:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86270f5b-6353-3b82-9a5f-242bbe9d8268 | -4.00813 | -49.02032 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 686e62a7-05c6-3db6-8d4e-4874a97db9f9 | 1.75565 | -55.97749 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d85f76cc-3bfd-3efa-93d0-c28de824b204 | -3.84948 | -41.58541 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 4c8b0415-ce9b-3d2b-b168-c4e9ff7841c7 | -3.76191 | -41.73195 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ecddf22c-bd92-335d-97ab-887e22470309 | -2.86897 | -50.74466 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 360eeabf-623a-3a02-8536-fac5b0636b49 | -4.93557 | -41.53077 | 2025-10-18 04:27:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| de05ef60-7361-3a4f-858d-6f488146f7a1 | -2.98213 | -50.29686 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 077e5a50-7298-33e7-a23d-c5a934ebe4e7 | -1.7621 | -47.26044 | 2025-10-18 04:27:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54cf7eb1-aa11-3e3f-8b63-081e182e885b | 1.77074 | -55.97095 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33ce8339-70e1-3199-a394-a13619985b83 | -3.65758 | -50.26564 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d246cc3-49ec-35a8-86cf-357fcd84c35e | -1.17906 | -54.21305 | 2025-10-18 04:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e9972e8-7376-344c-a7ce-6aaa13f91f9b | -3.54059 | -49.45095 | 2025-10-18 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba4b64d3-5f09-38d5-a2bd-e29d8d629d9c | -3.06085 | -43.2107 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a10d689d-0642-3543-b339-e454ffc8199b | -3.75792 | -49.04369 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 186d057f-6586-3a60-9c47-fb86b846b7eb | -3.84706 | -41.57545 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 405a6de7-9046-331d-84f9-c37aa15dfc93 | -4.44179 | -43.22396 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00b58738-865f-3b36-9b03-318b0bcae807 | -0.75506 | -47.76275 | 2025-10-18 04:27:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7894b5b-1252-3614-8fdb-194c312121c0 | -2.12415 | -56.60859 | 2025-10-18 04:27:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e197b51-8dc2-3c44-b87b-3f4b3ccfa48b | -3.40853 | -46.89967 | 2025-10-18 04:27:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 694df32c-d246-3eed-b5a0-23a4b941bdb5 | -3.85019 | -41.58072 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 08119761-fab4-387d-9ed9-155ddea4463a | -4.33136 | -47.22407 | 2025-10-18 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6a2f3a6d-7693-3acb-ba14-4695514f580a | -3.85403 | -41.5813 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f8591c78-a846-3fb5-8c10-f9fc8ab7f581 | -3.15325 | -50.24554 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7fcc9048-8d3b-316f-a820-14ca2c86e5e4 | -3.83168 | -47.40196 | 2025-10-18 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e9bf15c-1fd5-3e5c-a37b-6f199ba6185c | -4.4054 | -43.43916 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| bbd7de97-0606-3c88-87ef-ed678a9ac57d | 1.76784 | -55.93029 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 15afe3a4-36dd-3959-9c36-29c1bb35bb4a | -2.86487 | -50.74398 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 64dbd6f0-eb71-38a2-bf29-5e9d122d9b23 | -3.2476 | -45.96578 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f1f19b6-56dc-3779-b587-e4df4e8a1cbc | 1.77008 | -55.92576 | 2025-10-18 04:27:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55101880-ab6d-30f0-b832-3fdbd8edef25 | -3.24705 | -45.96924 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74d15d07-2faa-3b35-ab39-74616e823b08 | -3.25769 | -51.22106 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6daf1fca-e88f-3dc3-9af0-912ea524ca20 | -2.87951 | -50.73148 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe9f279d-c8db-3fdf-8232-f908cecdf727 | -1.619 | -46.66874 | 2025-10-18 04:27:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 70dcd5d6-eda0-3e19-8f12-c8f196ee98bd | -2.91343 | -52.72431 | 2025-10-18 04:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7a940330-014b-3d18-89b2-4e16c7a4f49d | 2.01689 | -55.83578 | 2025-10-18 04:27:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a779014-1cdd-3201-afbf-8c6d66bcbdbf | -4.76576 | -40.86348 | 2025-10-18 04:27:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e47c9237-d08b-3a3d-946d-38952f601c3f | -4.21589 | -48.35752 | 2025-10-18 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cda34f66-a689-37b6-b9c4-f3a68b413889 | -3.2465 | -45.9727 | 2025-10-18 04:27:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ff1daac-f789-328f-b597-d20f9d1ee77f | -3.52779 | -50.30657 | 2025-10-18 04:27:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02d8126b-5279-3f6c-8562-51ff4b17335f | -3.83909 | -47.39938 | 2025-10-18 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| abe53afd-5c84-3447-93fc-6acbe203ecbe | -3.42438 | -51.66963 | 2025-10-18 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f743b5b-554b-3fa4-841d-b7a792bea78f | -3.75427 | -49.04308 | 2025-10-18 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f459008b-d8a4-3182-8626-e8e6eb19f600 | -2.118 | -56.60753 | 2025-10-18 04:27:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 395bd45b-57d4-30e2-a7f5-70692e112a22 | -3.13047 | -50.21121 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fdccd24-1c4a-3970-8c1c-ec98736f7a55 | -2.9149 | -52.72664 | 2025-10-18 04:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b693e416-7695-3094-925c-729a08e76848 | -3.14452 | -50.24933 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7a2a0662-f844-3794-adb0-a7858c5ee13e | -2.42346 | -47.14558 | 2025-10-18 04:27:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d81168c5-da74-35b5-85ef-95288cbe7e01 | -4.44119 | -43.22792 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d83443e-0d64-3526-8e6d-054c4286a6c6 | -2.87366 | -50.74168 | 2025-10-18 04:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be220c78-affc-3d1f-abe2-4d3c04f10816 | -3.69985 | -49.56477 | 2025-10-18 04:27:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b877eb2d-d9de-313a-b730-741f3ba70d13 | -4.44887 | -43.22506 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1331e1c-988c-350b-b96d-c29e22c6dfe3 | -2.30213 | -48.56771 | 2025-10-18 04:27:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6f05100-9be6-39b9-98af-4a46ead18654 | -2.74818 | -49.3842 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7d3212f-181b-38f7-89ec-0af7fe9c4697 | -3.7657 | -41.73255 | 2025-10-18 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 507f4e9c-3ffa-3275-b510-af4cfd14716a | -4.53055 | -44.7986 | 2025-10-18 04:27:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a01959dc-528f-3427-87c8-b55dd09fa23f | -4.54547 | -43.76167 | 2025-10-18 04:27:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40df7f4d-f869-3c52-83f5-7c3c740e8873 | -4.76973 | -40.86473 | 2025-10-18 04:27:00 | NPP-375D | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7ca519ed-90bd-3df1-abe5-64e61f61a603 | -3.06025 | -43.21454 | 2025-10-18 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67453dd9-fa04-388f-87bf-bc3733601d08 | -1.61957 | -46.66515 | 2025-10-18 04:27:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2859963-c04b-31ed-88d5-288675d4089a | -4.45889 | -43.23067 | 2025-10-18 04:27:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6730351b-2297-3bc6-8c84-df5a03575c10 | -2.57261 | -49.10777 | 2025-10-18 04:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 456356f2-7714-32ee-a898-000531c10a50 | 1.00658 | -51.2 | 2025-10-18 04:27:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
