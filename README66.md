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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2325184-0927-352a-93f6-cd8f75a5b6bc | -11.17295 | -47.27815 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9804149c-c6ae-3848-a47d-4710ec7696bb | -11.14632 | -47.1948 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 864dd216-3c9f-3cd4-9c56-dc18d3db3ec1 | -7.77324 | -42.54718 | 2025-10-02 04:29:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 0a2b1e2d-21d6-3d24-85c2-ae133ac040cd | -10.26142 | -48.07148 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 229e53a1-307c-339d-9614-ff807ef367d8 | -9.94479 | -43.71572 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 325256f8-430b-3d7a-82b2-442f3952b0f5 | -11.46533 | -45.01316 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80124b48-c8b2-3fe6-a2a1-d3287a165d0f | -9.07801 | -46.70967 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f0f1518-de64-3745-8122-a3008252b6f1 | -6.96305 | -45.34006 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e3ee267-9b9f-3bbf-8318-be7f89133246 | -10.68494 | -48.57936 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57b438b8-3b98-3bb1-8ef5-197d98a224a8 | -8.56968 | -44.66606 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9533e5a3-e65a-3661-a896-77e79a56d665 | -7.77599 | -42.5283 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 58f17574-7d35-3955-93c9-5f8937bf19da | -11.26663 | -47.82421 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b5e982f-1759-312d-ae13-85477788903a | -11.27498 | -47.81468 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 073360c9-4fd1-33bd-a624-8db338fdd174 | -6.71437 | -44.62699 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 240391c3-be44-3aa7-a3c2-4e09cafcee01 | -7.58029 | -46.81396 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d53e646a-3ebf-3f53-87d5-307b95c285b3 | -7.00588 | -44.50325 | 2025-10-02 04:29:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3b602b1-e594-3aff-ade4-f33dd0b6e3ce | -11.35235 | -44.97284 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 144c51fd-4040-3f28-ba51-f678ea1b8d8c | -10.26665 | -50.3313 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e045baf1-43da-39c9-996a-0c8e4847973c | -11.77983 | -46.83502 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27cb8595-24a8-3cd4-981d-070dae44b7fa | -9.93533 | -43.7539 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f3075421-26df-38e3-90f1-4046d9565496 | -10.70817 | -47.98721 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3035235a-0bb4-3225-93c0-e6d9be1fc82d | -10.89241 | -44.29393 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04f335e8-71d7-3586-a8f3-06609a58fd91 | -6.30029 | -45.92369 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70ba5056-e10d-327b-beff-ecdd14776025 | -11.16907 | -47.28114 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95a08d51-6352-3f35-b5c2-ef3b8668d71a | -6.96808 | -45.3299 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffa61949-862a-3a79-9f83-21d66c51520d | -10.92525 | -46.46669 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f5c768c-b16c-3fcb-98f8-4d93ba6c3226 | -11.48171 | -44.99977 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 101ff90f-be54-33e4-a653-7a9b1d0bfadb | -7.48483 | -43.04467 | 2025-10-02 04:29:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a3ece974-a92a-36b7-8731-eb54447667ca | -6.96416 | -45.33295 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0eddc8f5-99fd-3e94-a238-adfaad47e96c | -10.82276 | -43.66824 | 2025-10-02 04:29:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ecd2fe0-75b9-3849-b865-b811a737a081 | -10.82586 | -47.94866 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0a5eff5-3198-3e36-89d3-ae24bec60030 | -9.7118 | -48.95571 | 2025-10-02 04:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 48ccd8c6-f799-3a9e-8ba3-2351088c2847 | -11.15907 | -47.19292 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f442bdb-e3cb-3e0c-ab1e-5be74464c15b | -8.87989 | -46.59192 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57cf3e9b-07a3-3e3d-84cc-fca3afc9bd10 | -7.60525 | -45.4057 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 051b25db-0c66-34a4-86b9-fd5be419f30d | -10.26886 | -50.34032 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42813c3e-611a-3a60-85e3-2e2876536e94 | -7.29408 | -42.87605 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1e34ee68-1dc9-3263-a550-867ab14af84c | -9.40642 | -47.58445 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 3a35b3ec-e27a-3bd1-8f37-efae8c5c3159 | -10.21745 | -50.29004 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91296112-044d-3e2b-8588-817d57605418 | -10.81894 | -46.59931 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12decf0a-dbb3-3c81-b023-52f7c7a16a04 | -11.2672 | -47.82068 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98a39cfe-d17d-3e3b-9a6f-8ead4d461225 | -6.96249 | -45.34362 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36bc6faa-d229-3cb8-86ca-2a04b1663d11 | -6.67021 | -42.79778 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 29e7fd59-65b0-3500-a4d1-a838f82f1507 | -9.04356 | -46.65363 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 724bc05c-5e48-3ab9-b5dd-ae5d218613be | -10.86682 | -47.82119 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7bd29739-26a5-3d07-bbd4-0c35416dba9a | -8.4673 | -46.83044 | 2025-10-02 04:29:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 665b5362-e6ff-33e8-a100-ef3f6cb9b485 | -11.14577 | -47.19831 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2fa203f9-36e8-309b-81a7-64093445614b | -11.03325 | -47.82275 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 39a2ee15-9469-3b0d-85f1-d38166ebe43c | -7.77667 | -42.52361 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 0ec1d67f-a047-31ea-bdc3-c78f3cf0dddd | -11.81898 | -44.90955 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b823625d-05ed-3533-82b3-e3094facd521 | -11.17184 | -47.28519 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c2906ff1-fe91-33cc-b09f-8678623a1d0e | -11.22715 | -48.21114 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0635594c-9269-3892-88d8-d504cf1dea9e | -6.68545 | -42.82269 | 2025-10-02 04:29:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8ac13098-7466-37e8-b6ec-0e0b85efaca6 | -11.67352 | -47.4925 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a18d819-7c3b-3c77-8c08-bbcf50373d46 | -11.61411 | -45.05379 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f57b682a-bb49-3c6f-84d4-c1769882e48c | -11.81433 | -47.5874 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 547553bf-cfb0-3fbd-b060-6d5b3ddeaeea | -10.24205 | -50.32275 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dc21dc8b-44f1-31c5-9f29-032f416baa5e | -10.19287 | -50.2815 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54db3532-01ec-355a-945f-1d68dfb23d46 | -11.28528 | -47.82758 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3224694-f55c-3c21-b53c-427a75788062 | -11.05882 | -47.81248 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6185fede-be13-3c94-a716-49e89c0439a1 | -8.1619 | -44.1307 | 2025-10-02 04:29:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e93c20c7-2f92-3354-be0e-e42f3561b068 | -8.88877 | -46.6005 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de756a1b-1dbe-30b0-9a72-596f8e747ada | -10.43312 | -47.46896 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23627872-f44d-3994-b3bb-ceac926a573d | -11.18904 | -47.75349 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8408e18e-6a25-3ef7-baaf-eb09b88805a0 | -8.85616 | -47.66218 | 2025-10-02 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9306f326-68f5-3d21-b63a-1e3a11377858 | -11.82234 | -45.00723 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6f5d52fc-d55d-362e-ae06-f4edbb51ea51 | -10.27097 | -50.32772 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b2f19459-cfc4-376c-a032-477060ec7315 | -10.34752 | -48.19934 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14861833-d2cc-3aff-83c9-cc451a78a013 | -11.02033 | -49.81832 | 2025-10-02 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 869b4269-9432-3d76-8fd2-6ef8b0197ea5 | -8.84936 | -46.57655 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6d02f2e-91cd-3e03-a879-177841265fc2 | -7.11394 | -46.70787 | 2025-10-02 04:29:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8bb7965a-9fc1-3ce1-9f84-b5245a579a91 | -8.82417 | -44.79982 | 2025-10-02 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bc0b9f4-2c90-3bc3-9f3a-e311c782f56c | -9.9368 | -43.71898 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1347e570-6997-3c28-97e7-3df150f8b40c | -11.17572 | -47.28221 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0a760072-100e-3ec3-81d2-763e1efb9140 | -11.03602 | -47.82685 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2ce03349-7a06-318b-80cc-6336cff6f8ff | -6.27548 | -44.05545 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 104dbe6d-802c-39b3-8e88-5c6236bd6c34 | -11.14909 | -47.19885 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| db9acd7b-3ec1-3f8f-9e64-cdc00554a822 | -10.7563 | -46.13948 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3448889c-0c3e-3822-9f52-8c32cdb51033 | -11.82704 | -44.99974 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7356df8e-3bbf-3b17-8228-544f461bd9da | -7.77981 | -42.52887 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3e4a9722-c7e0-3ad6-99d9-fe12b94d6806 | -9.59393 | -43.07272 | 2025-10-02 04:29:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9231c42d-784c-308f-8b7b-ee6f77ac8548 | -11.4794 | -44.99127 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a22fa442-b0ea-3da9-b59b-3c1f8380d4b4 | -9.93873 | -43.70604 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f527f0a-e1f7-3036-81ee-1ad46a409ad3 | -11.35174 | -44.9769 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c68c416e-45f2-3b69-b4bb-2485e9db0b3d | -11.36066 | -44.94143 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94e9fecd-0c68-3609-bc3c-c755b55016c9 | -8.416 | -47.74793 | 2025-10-02 04:29:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd23e345-5725-387e-99bc-c8129c1a7ecc | -10.22601 | -48.21623 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd213b79-4857-34ba-beab-d0ed99c21043 | -10.68098 | -48.58242 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0fd8c8e-71c7-359f-9efc-6ce0962009fb | -9.96332 | -48.78557 | 2025-10-02 04:29:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8190eb80-70ec-325d-9b27-152de537cc72 | -7.77733 | -45.71265 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b118563-d5b2-3aba-a6b6-4e87a953e5d2 | -10.80343 | -44.23938 | 2025-10-02 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d9b3857-4ad4-392d-a674-76bf2f25f132 | -9.77309 | -46.22807 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7226a3c2-b1a6-330d-b384-67e0a898e284 | -10.82456 | -46.62931 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bfa657b-a937-3414-9476-523ff5c123ca | -10.79263 | -45.35225 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba716149-5b72-31e7-9003-22553833007f | -9.90263 | -43.69618 | 2025-10-02 04:29:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e080117-e34d-3c8f-b822-2fa01d63ab76 | -7.77079 | -42.53724 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| f4f4a98e-b244-30a1-ad1c-9d50893f02a3 | -11.58991 | -47.63803 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b89c5196-832e-3920-a4cb-0fc721eb9e48 | -10.6917 | -48.58047 | 2025-10-02 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f57573a5-7599-3fae-83e2-6566383a49f3 | -8.5135 | -44.6766 | 2025-10-02 04:29:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f725a7f-90a3-3f91-8d00-8d66de2979f8 | -12.0838 | -44.91668 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README67.md)
