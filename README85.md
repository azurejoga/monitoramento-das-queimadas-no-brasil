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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44e163d1-e825-3e2b-aa3b-4bf9960be627 | -7.7684 | -46.2479 | 2025-10-03 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 301.8 |
| dc609acd-1044-3ccc-a041-81cc4169a995 | -7.7682 | -46.2703 | 2025-10-03 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 233.7 |
| dc0aa26e-46c4-360d-afd6-d32611fbe430 | -7.7496 | -46.2496 | 2025-10-03 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 345.8 |
| 8ae75c35-c0a4-30a0-b0be-60e3077bb346 | -7.7687 | -46.2255 | 2025-10-03 04:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8e33368c-7fff-3ac1-89c5-f5e6535f1b8d | -13.1345 | -47.882 | 2025-10-03 04:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| f1b7bc12-9689-35b7-b3e5-d2590120baa2 | -11.9163 | -46.2817 | 2025-10-03 04:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 31c532e8-92ee-3fbc-8f9b-4353efe4c61a | -10.9363 | -46.7068 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 1aadc3ba-3c93-387e-a129-786209ee4075 | -11.0147 | -46.5619 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| c75a7fa0-76c5-3a62-80ad-8dde57461ec4 | -10.9748 | -46.6794 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 3ea82198-4582-352b-a97e-d2186cf2d8ce | -10.9751 | -46.6569 | 2025-10-03 04:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| da158343-7716-3602-a358-c490396b007a | 1.78643 | -55.8334 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b4f87f-6b26-351f-bc38-e1c0a4bf0c18 | -1.07447 | -53.67747 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2c927a7-f5fa-3f21-88b5-ba8de40942e5 | -3.194 | -51.03447 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc0aa3ff-46fa-3f8f-b70f-7ad882a0632a | 1.5246 | -55.84313 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4cf52e25-8842-3925-9889-9f98f175dde3 | -4.43737 | -43.38346 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35237d9f-5a6c-319e-b88b-0d159d9c6484 | -4.43668 | -43.38801 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 125dbee9-8b9b-3267-aa95-9093f45f48ef | -3.68327 | -49.10444 | 2025-10-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 447d356d-03cd-3a37-b55e-b40fad6b597b | -3.84633 | -41.56969 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2f172336-2f18-367f-9298-5247ac60be8f | -4.93784 | -38.00319 | 2025-10-03 04:29:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 937eb915-b1cd-374e-9723-ed3ddf7c34f2 | -4.44828 | -43.23501 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 98a28322-fc51-3dcc-bcfb-548022ec6672 | 1.52343 | -55.83549 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 652d1112-c60a-3de5-ba04-498fd6f6245b | -1.13413 | -47.8031 | 2025-10-03 04:29:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 113b7022-4ebb-3da0-8d44-dcfbcaa6c751 | 1.78587 | -55.82963 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c847281-1135-3811-ab34-734732da6332 | -0.90999 | -47.54725 | 2025-10-03 04:29:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fafe0755-ad4a-3c07-8f6d-9ec8447ea8cf | -4.44043 | -43.38861 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d31a3654-3f1e-39b3-bed7-3c8fde70da28 | 1.75356 | -55.86442 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0873dfa7-7f26-3df7-bbde-80f03aab6d1d | -3.66813 | -38.81152 | 2025-10-03 04:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d554b95f-71c0-3395-b7b0-89fa8b600d7d | -1.1448 | -54.18937 | 2025-10-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9938c4ce-02ef-3ff7-a151-7c98ff98cb7f | -4.6508 | -45.79271 | 2025-10-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a3e44a3-c9cf-3459-a756-b6387b854e5c | -3.84214 | -41.56907 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f4f3ba1d-bc8b-3d28-a7f8-80f54b87e36c | -4.65475 | -45.78963 | 2025-10-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad0924e2-0ba9-3c86-92e7-496643c82f0e | -3.46412 | -50.09037 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a282fd-dca8-3576-9af6-6483700a5ed9 | 1.52108 | -55.82015 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 428208ac-35f1-39a6-aead-d65aa78f0322 | -3.75458 | -50.9506 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9082b14d-5afb-35d1-bf63-fb81c191c6a9 | -3.69456 | -49.01125 | 2025-10-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618175d9-1719-316c-895d-0a1ff8cbc592 | -3.09401 | -47.01086 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2c12f560-5836-35b6-8ede-43f00cd79834 | -3.32074 | -50.80646 | 2025-10-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c10ec859-a9d2-38bd-b542-6276488a2413 | -3.84519 | -41.57727 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bf4340b6-07ce-3089-b59f-8ac193043caa | -4.97311 | -42.70402 | 2025-10-03 04:29:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00c89df6-a65d-33f0-9b53-8e1a0b7d6b1c | -3.33724 | -46.5448 | 2025-10-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f560055e-36c8-30af-812a-79a8ab2fff91 | -3.09016 | -47.01377 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1161e16-4d04-37c5-9e66-ac954d12e28e | -4.27149 | -42.00612 | 2025-10-03 04:29:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 80423061-253a-3935-a240-a64feb2ac277 | -4.8535 | -44.51733 | 2025-10-03 04:29:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 326152cd-eb6c-3786-a75c-c03a3770a027 | 1.51782 | -55.83642 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce5a9341-1059-3b73-8063-a8a097ce2a07 | 1.5184 | -55.84023 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6708a531-9a4b-3e71-b816-7b4eaa8eb686 | -1.14455 | -54.18616 | 2025-10-03 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b98edb72-893f-3ce4-ac0c-9ac6c27592e4 | -3.66418 | -38.81132 | 2025-10-03 04:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 178c2bf8-f5be-3d1c-a789-58e744b030d9 | -3.32148 | -50.80199 | 2025-10-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b469f7e9-6e49-3e63-b228-5e67ea386119 | -4.43361 | -43.38285 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b880730f-2dfc-3cbb-9cc8-a9265f1702b0 | 1.52015 | -55.85166 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3561a5c0-ae3a-3dd4-9503-062c8d4ffc8d | 1.52285 | -55.83168 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa0b2252-9f8e-39eb-9b46-7f329bc27e83 | -3.70101 | -50.96713 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce89747c-a74c-34f1-a9e1-68975b1cd711 | 1.51724 | -55.83261 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7fb25a9-1940-3aa6-9b55-de579c5c49dc | 0.79061 | -51.96839 | 2025-10-03 04:29:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7018ae19-0a3a-3579-8f36-d4a1cbbdad8d | 1.52167 | -55.82401 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c5b5427-f2d9-3bca-9368-32621b720fad | -4.65361 | -45.79689 | 2025-10-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa58bb77-c0f9-3b7b-9a17-8d19d954f61a | -0.91259 | -47.54795 | 2025-10-03 04:29:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 36b5cc3a-3e6f-306c-b47e-afaf9114f323 | -3.83739 | -49.25798 | 2025-10-03 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9b68fd2-903b-3dd3-9e64-ccd9abc0a39e | -3.16955 | -48.61125 | 2025-10-03 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 802eddac-84e1-3176-9f67-233e618bb52a | -3.57723 | -49.4357 | 2025-10-03 04:29:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 156be350-ac00-324d-ad3a-65da4bc0d6bf | -4.43999 | -43.2385 | 2025-10-03 04:29:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e210639-d160-33ca-b7d2-79cf8d226413 | -3.93409 | -47.56328 | 2025-10-03 04:29:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 149f168a-1834-32c2-82af-a545cb9401f9 | 1.73663 | -55.86718 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acc19f3c-694f-3e0b-9faa-debb2baf51e8 | -3.09239 | -47.02117 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 8b84adb3-a64c-3c32-a477-fe7c70105034 | -3.49448 | -50.26879 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66e07517-84ab-312e-8daa-7dd3d3bc6560 | -4.9907 | -38.85674 | 2025-10-03 04:29:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 851389e4-ea0e-38b1-9286-fb43b75b4832 | 1.52402 | -55.83931 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72acf11e-9218-330c-91d8-d900e3c97ccb | 1.73437 | -55.89028 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c954bb72-8f4d-32fd-bcde-5d0862fdb6a7 | 1.49358 | -50.88587 | 2025-10-03 04:29:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 725ab40d-be4b-3909-b2d5-198b36a66ee3 | 1.72876 | -55.89151 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80177c60-b7a6-3b0b-bd6b-7b4f6829311f | -1.07834 | -53.68317 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3357344c-7476-3351-a416-009685701da0 | -3.841 | -41.57664 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b4d68993-0bed-3a66-8d86-91cc2c2aa7a1 | -3.22185 | -47.12632 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d215837-032d-3482-bdd5-b73154e36009 | 1.75411 | -55.86795 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 12124806-a850-3441-87c2-11bfd2db3336 | 1.51957 | -55.84785 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a2215c7f-4886-3218-9044-3a1bda0c0d16 | -3.49809 | -50.26938 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4989b139-ae1f-3710-b352-4a8809908691 | -3.69514 | -49.00757 | 2025-10-03 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81c04622-cc00-38f0-b73d-bf14db2da19c | -1.08839 | -53.68005 | 2025-10-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 097d459c-1f81-30ce-8301-e04b6ab1435d | -1.33375 | -47.57377 | 2025-10-03 04:29:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 308427b5-fba2-3874-bd0c-9317efa9a907 | -2.93285 | -54.17646 | 2025-10-03 04:29:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6838763b-1ada-31d4-ba1d-04f6efc43e9e | -2.25029 | -47.87962 | 2025-10-03 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 0c28d054-39c5-3f56-ade6-9e40a2c66bc9 | 1.78334 | -55.83276 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f922d60-1a39-3026-9444-de23ed4c6747 | -3.09293 | -47.01773 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 080393d0-e623-340c-a8f4-ea1b24dfa6f7 | -3.09347 | -47.01429 | 2025-10-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c01cc20d-57a4-3c99-8812-2cf2595e3f2c | -4.65023 | -45.79633 | 2025-10-03 04:29:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0586d51f-1c3a-328f-820a-ae2a71b29599 | -3.49584 | -52.46669 | 2025-10-03 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87205306-9b84-39dc-8618-e09dfefdafb7 | 2.27649 | -50.7285 | 2025-10-03 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a29c2e5-38b4-3c2e-8d59-ff1902b23987 | -3.31982 | -50.80377 | 2025-10-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 369f1039-d37e-3c27-b1d4-17b319508b21 | -1.3332 | -47.57727 | 2025-10-03 04:29:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35704095-605e-3d7e-a9c5-c5ff1913ef3f | -4.01168 | -41.79441 | 2025-10-03 04:29:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7cdade2d-660b-3d2f-8786-9ef322fb7d3a | 1.73381 | -55.88662 | 2025-10-03 04:29:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05091dc2-9835-3b9b-b22b-111cb7036d4a | -2.38033 | -46.47263 | 2025-10-03 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73de5b29-7d75-34ab-a636-3d0a17cd195b | -2.24695 | -47.87909 | 2025-10-03 04:29:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 4f689a1a-86bd-3818-b760-07833743e5b6 | -3.19098 | -51.02917 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1b11dc5-55f2-38d2-9922-2f404b9ae4b5 | -4.93283 | -43.73696 | 2025-10-03 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1cb00a8-151a-3aa4-a77c-41bdac0752de | 2.27704 | -50.73199 | 2025-10-03 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ea62d15-ba92-3817-9160-f9fee8415b66 | -2.92345 | -48.30359 | 2025-10-03 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a321234-1969-3e24-80cc-730f5c4e0588 | 1.78529 | -55.82577 | 2025-10-03 04:29:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8803361e-c19a-3aef-b250-ac004fd7692a | -3.55878 | -51.12815 | 2025-10-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7523f4e-2084-389c-aa6c-8a10e4b8a3c6 | -2.09877 | -56.83195 | 2025-10-03 04:29:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README86.md)
