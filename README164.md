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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d772624-52bd-35fb-81cf-f311f6de7c38 | -6.04477 | -42.59439 | 2026-10-07 16:03:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| fd7d6df8-7155-34d9-a256-9df8027cba84 | -3.94222 | -42.32436 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 930c4bbc-2e8f-3013-92af-f176c9a344f2 | -3.22474 | -42.6562 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c480b656-d85b-3428-91e4-ef4e9bcb1edd | -2.98522 | -45.00738 | 2026-10-07 16:03:00 | NOAA-21 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a21f52a1-1ee6-398c-8853-f3a2d72d13d8 | -6.92831 | -44.64735 | 2026-10-07 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dc6005e0-6053-319a-b347-8c654b2f14ac | -5.97112 | -43.29535 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3fe5569c-67e9-32ec-8589-2e4756301acc | -3.57688 | -39.14016 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 665dbe76-bafe-3431-a328-7fea94e2e391 | -6.42101 | -38.40106 | 2026-10-07 16:03:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f4ac0af-e1a5-3c93-b6ed-ae933cbf621b | -4.7649 | -42.59761 | 2026-10-07 16:03:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 921a97df-ef9d-3953-b5b7-49f55cb64483 | -4.05841 | -42.22289 | 2026-10-07 16:03:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b3408c0d-4385-3bf9-856d-ad5226b782f6 | -5.72411 | -41.72721 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| 80e63953-269d-3bd3-8419-059a44acb9b0 | -4.84449 | -40.40876 | 2026-10-07 16:03:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 64033fbf-ae8b-3a0b-a1d9-b84d574f0c78 | -6.3317 | -43.74799 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 4f8c6b55-6892-3f51-88bb-79da73946ed3 | -5.37194 | -44.16718 | 2026-10-07 16:03:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 1dd47a81-47ce-3ae9-842e-55952aedc4e0 | -3.74192 | -51.21411 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 062b6833-e991-31b6-bf1b-bea9f808ef87 | -3.89064 | -44.11957 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 4f5f1b8d-534d-3dcc-8890-9605682dc50e | -3.44159 | -49.26183 | 2026-10-07 16:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 8b8ec70f-9c0d-3ce4-9ada-b472efb652e3 | -7.37945 | -46.20403 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35533108-b182-3d9a-94e8-a63a9d0ecfd2 | -7.00075 | -45.11951 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 58ec06e4-c094-3bbc-845b-6a60749afd83 | -5.62172 | -43.04634 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| dc94487f-a30f-3b7f-9cab-6e230d357e60 | -6.67827 | -44.96259 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| dab93ccd-2cbe-321d-8f5c-c3396a0a8d25 | -6.4177 | -38.40155 | 2026-10-07 16:03:00 | NOAA-21 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9125419b-95df-3a77-a449-fea5254c0e64 | -6.57186 | -43.07645 | 2026-10-07 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 62bfd86d-d7d1-3bb7-ab27-ef5d283ba692 | -7.17501 | -47.80616 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9bc6b298-0a7f-3bb9-accd-c390ee215dad | -7.77666 | -48.23921 | 2026-10-07 16:03:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 3131db1d-d774-3434-ac2b-3782eee54364 | -3.26291 | -50.3997 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 063f0598-ff13-3914-a3d4-0edce55c2679 | -3.86843 | -44.14201 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 18c9b546-bff3-39cf-923c-2ce6c0b7fc7e | -3.89784 | -44.1108 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ac418ca5-2616-3906-b3cc-b6d3ba3661de | -5.72254 | -45.16025 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f58b8d52-5cc0-3f45-b7ec-218fa753cfbb | -3.91507 | -44.89926 | 2026-10-07 16:03:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1f79b15c-d5fe-3fe3-b3d8-6d2f5b2a2a86 | -6.6197 | -37.89543 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 19fb262b-3c0c-353e-9684-8c489468fc6b | -5.6201 | -43.04362 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ac2f168f-3fea-3d57-871a-45136add428b | -3.63961 | -43.12872 | 2026-10-07 16:03:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4016d495-f410-3065-bf07-08b035769bae | -5.71804 | -41.73693 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 96016d6a-aff8-3930-bcfd-a30d6a6cf332 | -6.03947 | -42.58519 | 2026-10-07 16:03:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.0 |
| ac149a61-2139-30db-a3f8-939b6db90119 | -3.80509 | -40.4667 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 02d2967f-adc9-3cf4-8930-551b1c2c70b0 | -6.71469 | -44.00582 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 00a01195-02e9-341c-ab14-018c899f059b | -6.42089 | -44.8358 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 86b88c77-0d68-32c3-b46a-3f01a9f8d94d | -5.24253 | -50.91191 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| fe3aae7e-ce9e-332e-9100-07c3f6ab799b | -7.57412 | -46.70257 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93274314-128e-3aad-b367-a94f2a9d746d | -3.67097 | -44.8004 | 2026-10-07 16:03:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 516099a0-37e5-322e-a407-284eb0a9f6d1 | -6.37277 | -42.92762 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 2baf11f5-a214-3c40-a08d-f2556da51323 | -5.97028 | -40.94845 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 849fa5bd-8ed6-3d0d-a806-f325a28014e9 | -5.63764 | -44.89695 | 2026-10-07 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 27237ad5-f69d-3d7d-a805-e887b9b46693 | -5.97795 | -40.95142 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 2f856c61-bd6b-3c04-bfb2-aa4371185031 | -6.59269 | -47.40672 | 2026-10-07 16:03:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dece0778-bce9-383c-877d-538469a05ea0 | -3.91614 | -38.62144 | 2026-10-07 16:03:00 | NOAA-21 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5743432f-0f57-3ca8-b2a8-bcecd9ee917f | -5.70555 | -43.0728 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8923956d-9053-3612-9635-7ed9b9cfc7c9 | -3.29634 | -42.28196 | 2026-10-07 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 0d007d6b-c5f3-3140-b839-474e69d0c284 | -3.32669 | -42.76948 | 2026-10-07 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e3dc104-971f-3a99-96f7-4db56f6a10e6 | -3.15303 | -43.91945 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e5c59a8f-fb00-3558-8aac-b4791a737b22 | -5.96719 | -40.92836 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 398e734b-6122-33da-8813-189a4dd3ff0a | -6.00215 | -44.12629 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a965c329-ddb2-3788-a0d2-1aee70339b09 | -3.55876 | -39.13231 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 29e8dbcc-792d-3e54-a434-bfb68f5456f2 | -3.83722 | -42.63617 | 2026-10-07 16:03:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ec230f4c-9d1f-33e6-ba9c-e40589c5fde4 | -5.27413 | -43.36443 | 2026-10-07 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f7221420-840f-3772-8a13-e36565d6def8 | -7.45885 | -42.99527 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6dc1b13a-6e14-3cdf-99be-ff81f0586d63 | -6.69016 | -44.94702 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9838f5c8-3c16-3e8a-b047-f2f0ca17929d | -3.20407 | -42.80375 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 8e3489b4-a649-33ad-852d-e53cfec2aab4 | -5.73564 | -45.15348 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1e9f4123-a1ae-3e2c-bccb-8962e0a9f3b4 | -3.7494 | -51.21893 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 786acfaa-8a55-3b93-b5a1-6ab83d814c75 | -7.86859 | -44.15174 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 59e43712-1254-383f-877d-7799b013060d | -6.99283 | -45.13075 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 73334335-faf3-3c58-9876-b94f29af335f | -6.21022 | -43.83385 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f3a5f512-ae62-3bc5-837c-39132eecaf14 | -7.2957 | -47.28508 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3fd7dfab-8e09-33c6-ac82-8409c9cb76a1 | -3.42347 | -50.43621 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 09cdbfa7-c773-3f9e-a13c-8e8cdd88e966 | -4.27727 | -39.54734 | 2026-10-07 16:03:00 | NOAA-21 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 20.5 |
| a9d7e03d-2a1c-338b-baeb-6f97ae00c057 | -4.62054 | -43.50454 | 2026-10-07 16:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9769d7a1-afc4-34b9-b0b0-abbc6f1efc9e | -2.50786 | -47.38208 | 2026-10-07 16:03:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80acda82-5f1d-3387-bea4-b0ab6fafeb9a | -8.4296 | -49.8755 | 2026-10-07 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| edc13ac3-b9f1-368f-b41f-b141b4530681 | -7.18788 | -44.29455 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c7697921-ec65-319f-b750-85e30b9f3b74 | -6.1751 | -35.42054 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DE PEDRAS | RIO GRANDE DO NORTE | Brasil | 2406304 | 24 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 6c17406b-5d34-3f1d-bc40-700175025a2a | -5.97569 | -40.91102 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 33.3 |
| dab959a4-b521-3f82-90de-0d72f493d474 | -4.85402 | -43.36668 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b9de88f9-98c0-3e73-b871-7d8df36bc820 | -3.41838 | -41.55098 | 2026-10-07 16:03:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c197655b-600c-393e-8f77-636944a56261 | -4.01007 | -38.99458 | 2026-10-07 16:03:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 246dd4fe-15c7-3280-bc3a-f3892642f3f7 | -6.94149 | -45.27675 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 39696207-b640-3f58-9604-77b5e25eff14 | -4.58376 | -40.77501 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 25ba06de-1033-3ea0-83b3-032ec374f319 | -3.80676 | -49.11591 | 2026-10-07 16:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 90ed2745-7684-3748-8ffc-01382ec152f5 | -7.75818 | -43.81349 | 2026-10-07 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| cd9aad6c-2300-3c1f-8a74-62269f64aa4e | -3.40249 | -44.00028 | 2026-10-07 16:03:00 | NOAA-21 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8efa335d-3a63-36b8-ad11-ffa34811cc18 | -6.99537 | -45.11523 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7025d127-3947-3e3b-a925-a21982af0596 | -3.23152 | -40.02626 | 2026-10-07 16:03:00 | NOAA-21 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| ec6e3f64-ae95-3dfd-ac8f-512cb5bcf526 | -6.93885 | -45.25744 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ccd7e8b1-b633-36c5-8a5c-df047e0ac0a6 | -7.81237 | -45.50225 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| df2384a3-5a51-3037-b3f2-2ebd9169155a | -6.57136 | -43.07296 | 2026-10-07 16:03:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6b3d9e98-adf4-3e92-85d4-05f5aab16413 | -3.16084 | -41.95401 | 2026-10-07 16:03:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a97b4af2-fd8f-3695-a21c-c01f879dc721 | -6.95102 | -45.27615 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f43b1a89-05b3-3949-804b-8cdb4ee2c911 | -3.59456 | -42.90495 | 2026-10-07 16:03:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 68132562-1955-30c4-8c32-d3129999cf45 | -7.3995 | -45.65108 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| dfeb694a-1e59-34ca-a54f-9476b21eccd8 | -5.73833 | -45.17265 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0e7504b5-7878-3438-932b-46d636d90441 | -7.18528 | -42.02864 | 2026-10-07 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 3332f1ed-f20b-3452-8b49-190f0a203fa1 | -5.96581 | -46.40454 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6dfebb9f-4ccc-3bba-bbd4-af5cd4e204be | -8.28935 | -51.23239 | 2026-10-07 16:03:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c3d04c71-6957-3c8d-9027-2cac4aced515 | -6.12851 | -47.92606 | 2026-10-07 16:03:00 | NOAA-21 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 37d0f195-0367-3ff5-8e8f-c7db7ce390a5 | -7.21948 | -44.29476 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 94e584c5-59d9-31da-b457-057cbb8ab302 | -3.98453 | -40.72867 | 2026-10-07 16:03:00 | NOAA-21 | GRAÇA | CEARÁ | Brasil | 2304657 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 3ddaf42c-6505-3137-a13c-404b0d98c5c0 | -7.01531 | -43.41635 | 2026-10-07 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0fe39eb1-3d99-3037-b0c2-c25862cfca68 | -4.74106 | -49.75364 | 2026-10-07 16:03:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 792fc284-a2dc-3d8f-8f52-028cdf90104f | -6.68491 | -44.94288 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README165.md)
