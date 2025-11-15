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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f232365-05d2-3a86-b760-c8f6c03b0b28 | -13.5477 | -43.72374 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a3589f5-e09c-319d-9e1a-99c610bec56a | -7.53845 | -45.8599 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31156325-03d7-3f6d-809d-1333d770fc9d | -11.91651 | -46.2016 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aff6fa65-2516-3036-8064-cdc98ba41ae3 | -10.10718 | -47.51957 | 2025-11-15 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de09728d-108f-366d-9f48-880559deae41 | -9.73954 | -43.95067 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7e039e90-dec6-30b6-be4a-7c2b2ed65cec | -12.23812 | -49.39454 | 2025-11-15 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bdc4d974-b665-36c7-bc25-6a5b3ddcb829 | -12.67966 | -46.7629 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55265d0b-5d35-3f8a-9a23-c0cb98a4bcc2 | -11.855 | -49.21624 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d2420116-ed69-39eb-9ffe-676dc8b3d0ce | -11.06605 | -44.97042 | 2025-11-15 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4bae37d-cfd5-325a-9d16-b8a024ed0f3e | -11.71339 | -48.87582 | 2025-11-15 04:06:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 939f06f7-4e14-3000-a7cb-d96bd006f12b | -12.79676 | -46.38307 | 2025-11-15 04:06:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33c688a3-f854-39b1-aa92-23d78c013918 | -9.44388 | -46.97406 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fdc42e8-c63d-3388-ae81-4591229e27bb | -7.55201 | -47.25398 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c437b5c-83d2-3678-99d8-7bca0a6f6bba | -10.10937 | -40.89136 | 2025-11-15 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3ab8faef-0efc-3a86-a2fd-4f5e16ac3067 | -10.3603 | -48.73282 | 2025-11-15 04:06:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cd9dea52-0bd9-3870-bb47-45cb02f39c88 | -9.35586 | -50.73987 | 2025-11-15 04:06:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c663b5c8-8aa8-3715-ad1a-e527c9a6fafd | -12.84084 | -46.44201 | 2025-11-15 04:06:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 62ba23fa-0207-3f17-a6fa-ae692f50521b | -8.30037 | -43.84296 | 2025-11-15 04:06:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 189ceed2-0f56-3d81-8c63-53950f49f372 | -9.85408 | -44.17914 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48008f2d-aee9-37c5-93ba-613042152dfc | -12.38681 | -48.11537 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7dc767c2-1de3-38cc-97a8-0de36c6327af | -12.9084 | -45.10135 | 2025-11-15 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98ee5d55-9261-3e78-9688-5da9f4813db8 | -12.75767 | -43.65538 | 2025-11-15 04:06:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9700c493-2495-3a5d-813e-d1decbc5f098 | -13.16704 | -43.23357 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe937009-7a7e-3e89-a7a0-f1d5b78f9245 | -9.96795 | -44.94216 | 2025-11-15 04:06:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8482fec4-03eb-3cff-8ecc-9b856b0ee14b | -8.7582 | -45.66145 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8dfe5b05-26bc-335b-98d6-dccedb033711 | -12.20893 | -47.44863 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f47bffd-d535-3d87-a7b4-4f47d24a4e50 | -8.3102 | -46.22315 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0da7bf03-3083-39b8-9e6d-8668831130bc | -9.44904 | -46.9706 | 2025-11-15 04:06:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 261090e9-5739-36ff-85f1-91fb5f099418 | -11.92333 | -46.20989 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6da20318-e0dd-393c-a579-28a3b03f46c9 | -7.528 | -47.20021 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1845c33a-8f47-3205-a24c-14ebcd1aadf1 | -8.73251 | -45.66446 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0fed32f-0a13-32e3-ae92-0a60e12be8ce | -8.5618 | -45.51992 | 2025-11-15 04:06:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a86605dc-6c88-313a-af9c-33034fb687a8 | -12.79228 | -48.81663 | 2025-11-15 04:06:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94e1b66d-f64c-3877-8a9a-3e3919a9c450 | -12.52853 | -49.59916 | 2025-11-15 04:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 083c0450-c98b-3755-adfc-a63cf4d8e617 | -12.51021 | -39.52464 | 2025-11-15 04:06:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dd085c46-2e4f-35ab-a8bb-3a3d11026df8 | -10.32115 | -44.27048 | 2025-11-15 04:06:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8d0a395-ebd7-3635-abd0-e4fd003c9c06 | -11.00694 | -45.27098 | 2025-11-15 04:06:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 970d882e-d72d-3a93-9810-ba0cce7967b7 | -8.995 | -44.17849 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d0c3f2c-223b-311b-bcdf-36109983f574 | -12.67079 | -46.7651 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d21e4f30-da4f-3e47-b454-ecb539a3ab3a | -9.5273 | -42.93741 | 2025-11-15 04:06:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 36e691ec-d9f5-3a58-96cf-fd17de477a53 | -12.90394 | -45.10516 | 2025-11-15 04:06:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c77e8986-0e34-327e-8bb1-b14cff26db99 | -9.74246 | -43.95559 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 114cf7d9-4fb7-3d41-9dfe-3d5138bc44fe | -11.85309 | -49.21923 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| abbb2207-efa1-3e8f-b3d1-609d01d5d763 | -12.78235 | -46.74629 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be2f94a-db80-3a6e-b737-ac2281e7ed0e | -9.02416 | -46.88122 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2d7522b3-7bba-394f-8284-a9e864ed7cf7 | -8.45889 | -45.14191 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b4527db6-7555-3792-8e3d-74d552220963 | -11.95623 | -44.85411 | 2025-11-15 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b303477-aa56-303a-b84f-331bb59382ca | -12.78643 | -46.74709 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99fec5e2-8683-3028-be40-343636fbb0f2 | -10.68584 | -45.17744 | 2025-11-15 04:06:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9295958d-a529-3dd8-8db6-9f37d3f883b8 | -12.23847 | -49.38806 | 2025-11-15 04:06:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37c435bb-3ef8-3706-a5a1-df5eae68c348 | -12.3939 | -48.10878 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a76fe8e4-05b8-32c3-ba18-2b0ee9d2c11a | -9.26341 | -45.19269 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70247b55-a27a-3608-b565-8e01e62a3bcc | -9.0054 | -44.18471 | 2025-11-15 04:06:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1bbd06e0-2516-398e-827f-8cdab1396ee9 | -7.5234 | -47.19938 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fea91ad9-f36b-3336-a90c-152f306d2a5d | -9.45803 | -44.87162 | 2025-11-15 04:06:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f641a208-6db0-32b1-9b0a-bc7666e6f614 | -8.30595 | -46.22237 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e2528ed-2e2f-35f1-ac6e-11e2ab7dec7d | -13.79727 | -43.25042 | 2025-11-15 04:06:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d15c5539-6dd6-381a-ac6d-a300ae2d0588 | -12.4238 | -43.18324 | 2025-11-15 04:06:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e5aead-6f12-39b0-b624-5ea467a7e652 | -11.8433 | -49.21739 | 2025-11-15 04:06:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| ccd3f6db-1b04-3397-8db6-d45050863675 | -12.96927 | -48.83905 | 2025-11-15 04:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66dfcf15-4d1d-3ca3-9d1a-694d4749fe4c | -12.20539 | -47.44354 | 2025-11-15 04:06:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78505e4a-32f3-3536-a7de-032da47cc8a0 | -9.81708 | -45.33162 | 2025-11-15 04:06:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| afe0e9fb-3e5a-3ca2-b44a-c5ea644d763d | -10.45003 | -45.08246 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7982e98-4738-36f3-8efa-427d66cb95d6 | -9.85554 | -44.1705 | 2025-11-15 04:06:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f6810ae-72ce-3e85-863a-4b9d8c6ce187 | -7.06078 | -48.3217 | 2025-11-15 04:06:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29bfcd74-67b7-3233-838f-d50a24c7fab0 | -12.59686 | -48.33347 | 2025-11-15 04:06:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5828dc67-1913-3d5d-b3da-b603bd31a24b | -11.80159 | -48.07853 | 2025-11-15 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dcfd7d6-349f-3d4d-800c-84612c9dfd1f | -10.44702 | -45.07706 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7e82b8fc-a651-33a8-b1b6-e7befabf0533 | -8.38589 | -45.81335 | 2025-11-15 04:06:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 040cea01-150e-3c81-bd19-d0cef44881e2 | -13.52863 | -43.41392 | 2025-11-15 04:06:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82d36917-0227-3264-acc2-1c24fcca62b8 | -12.48336 | -43.73552 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55df252c-e09b-3de4-b2bb-2b827a11843d | -10.42736 | -40.54733 | 2025-11-15 04:06:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 05b2a2b9-5564-3187-8de6-8d7445de9d86 | -11.95698 | -44.84967 | 2025-11-15 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6d0c42d-8f3a-3167-beef-d7112b748313 | -8.94686 | -40.84028 | 2025-11-15 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9254e92a-70f6-3ea6-90b5-1a4e3d6af023 | -7.69509 | -47.18803 | 2025-11-15 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 852c58ea-80a4-3a32-990f-9048ea6f81a4 | -11.97958 | -44.6494 | 2025-11-15 04:06:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5714549a-ad62-31d5-9981-b1da6131ad6d | -9.80752 | -42.20935 | 2025-11-15 04:06:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 57d8722e-2cfe-3910-9bff-563b34d4c0f1 | -12.39762 | -43.81791 | 2025-11-15 04:06:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aab7602-d288-3e7c-93de-17c53dafa19f | -9.75056 | -43.97443 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86323c62-3a62-3671-a2b3-b4384ba66a26 | -12.52842 | -49.59785 | 2025-11-15 04:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9895d92f-f3a2-30c0-b88d-1e6d1cc69c9f | -12.69688 | -44.47783 | 2025-11-15 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 744cf410-b3d1-376f-809d-c04f2d0014c3 | -11.80613 | -48.07935 | 2025-11-15 04:06:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 525f9691-85f5-34d3-8315-8f951a2ac1c0 | -12.39842 | -48.10954 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f3ee7b9-fe5a-360a-a0d0-85810e4ae0e8 | -13.291 | -44.19968 | 2025-11-15 04:06:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55af8006-f92b-354d-aa77-3f0131757f04 | -7.72352 | -45.81506 | 2025-11-15 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e642d64d-e712-366a-a89e-39dee7c4e0fc | -12.67622 | -46.75844 | 2025-11-15 04:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8e18b60-b6b1-3c11-bc81-71e3bd87aa8e | -11.39533 | -49.19386 | 2025-11-15 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a0d937c-38b9-3f0d-aeef-cbbc93f50ce0 | -12.3884 | -48.11327 | 2025-11-15 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 36dfc05e-0e17-30cd-9799-2df15182223b | -12.69598 | -44.47863 | 2025-11-15 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4dfad29-0870-3f97-8b7d-a78e1874ef27 | -11.75459 | -45.33132 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1afd10b0-8a6b-3dc6-9be1-2526f44faa36 | -13.7413 | -43.62918 | 2025-11-15 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc26fd56-6d5f-35dc-9743-38feb16b3bc3 | -12.15006 | -46.67058 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b77550e3-65be-3b0c-a76b-58cf938ab700 | -11.75292 | -45.34106 | 2025-11-15 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1f5014b0-9361-3f37-bec2-49099c597c7c | -9.80413 | -42.20879 | 2025-11-15 04:06:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1828ee85-6b79-3af9-a1c5-e978da31b275 | -8.32297 | -45.40834 | 2025-11-15 04:06:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f51f2cb-2847-3dc6-8fd9-a56aae72b823 | -10.42669 | -44.95474 | 2025-11-15 04:06:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0faa3082-7f5d-3ea2-a0d4-44878c6fafd8 | -10.37975 | -47.75206 | 2025-11-15 04:06:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e42fc901-2751-3e2e-ac8c-7806e9f27773 | -10.37419 | -44.71403 | 2025-11-15 04:06:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cb70084-7ce8-39de-9843-cc08515d4ec8 | -9.74317 | -43.95131 | 2025-11-15 04:06:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e545987-3f67-3d72-99a7-aae7876043f4 | -11.91991 | -46.20579 | 2025-11-15 04:06:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README30.md)
