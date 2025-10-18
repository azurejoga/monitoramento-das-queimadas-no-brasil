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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc5ac5e5-2b4f-35ca-9c0a-55ca610ea490 | -11.36935 | -44.29328 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e40bbbab-5443-32b4-9217-a98592327aab | -9.61744 | -55.11809 | 2025-10-18 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac6e3439-4a9e-3472-b629-7260916dabb0 | -10.95434 | -45.45732 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 57e86677-94b0-3b6d-9e1a-af5baba97ca1 | -13.76168 | -48.24081 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4a62812-1694-3825-8db0-e7cda39e3cf8 | -12.30602 | -47.26492 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcb76167-bc58-3ed2-9f73-8f0e718ec70a | -11.37065 | -49.37749 | 2025-10-18 04:51:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d948c12-2269-3abf-b359-1f13e6b8f632 | -13.42087 | -47.98617 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52a59ce3-9a08-3a88-a13b-93d3c3f734ae | -11.34622 | -44.21727 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e36c7d4e-9cbf-3622-bb5d-81c2dbdd1cb1 | -10.49989 | -43.45101 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7abec765-1324-3334-896d-a81daa237006 | -11.20341 | -47.82614 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 37dc66b5-7704-3575-9e47-4146ecfd6c58 | -10.50453 | -43.45922 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef462d92-23c2-3843-b77f-cd742636a0a0 | -15.7993 | -43.57438 | 2025-10-18 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 658c98ef-52f3-3cac-98e9-611b7fee2e7b | -12.17303 | -45.07861 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2a297a07-5845-3f51-a2c4-3a541f1522b2 | -14.09202 | -43.63201 | 2025-10-18 04:51:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9571ccd4-6ca4-31e4-8c4e-a4fc72ea6332 | -13.45648 | -48.11039 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e04a6ea5-71cd-33b4-b68b-12460274d917 | -10.62987 | -42.31089 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| df8be792-d28d-3a87-aaee-eb52476986b0 | -11.94238 | -44.23914 | 2025-10-18 04:51:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9711934-b79d-3fbd-896b-596250e2e9a3 | -10.01487 | -48.08027 | 2025-10-18 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 759ee3bd-2315-3617-88bc-3ed6a3ecf572 | -11.85209 | -45.44886 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2721d60-e96d-3b6f-9026-319dcd6afa4e | -10.11263 | -44.55499 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0db533b3-ed30-303d-8634-eb44f739929e | -12.36214 | -47.18185 | 2025-10-18 04:51:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d31877c-5d24-34ed-ad04-fd082be67012 | -14.90496 | -52.40955 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82c1d9ce-7c24-3c92-88ad-494291b3b62d | -13.04546 | -48.18886 | 2025-10-18 04:51:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65b1a5f-e82e-3d81-b1f3-9253c13c79a5 | -14.1502 | -44.24667 | 2025-10-18 04:51:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a8dedcb3-7486-37a9-b86d-e364d5309bad | -14.93243 | -46.71406 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b009ad9-8268-3c44-9281-7bf94be140d9 | -10.80827 | -44.0182 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d3ed4b2-ec0e-3b2e-a0a1-bf278a1f420a | -9.91555 | -47.6632 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f4a81ab-8521-3268-b7f0-bebdbe73fc43 | -10.96271 | -45.47 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1231e0b9-fa04-365b-b7ea-dd8fa965498f | -13.77008 | -48.24248 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c29b3e5d-8b12-3139-9cfc-d81d40f1e023 | -14.90687 | -46.7634 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af57c055-9d21-3f1b-ab8a-24526096ecf9 | -12.66358 | -54.77051 | 2025-10-18 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81a1ea2c-78e7-38cb-a5d1-425df9a04e12 | -13.76534 | -48.24566 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd5adf52-bba5-35fb-afca-c774c746c2c0 | -10.96698 | -45.47558 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a0cbde21-3e4d-3cff-8553-913b14d4a91a | -12.92159 | -48.59529 | 2025-10-18 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d57b0868-6485-34d8-9248-c137b4e2ebea | -12.24131 | -49.37368 | 2025-10-18 04:51:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f82d8e76-a431-39a5-b477-bae7c2d6ffdd | -11.20762 | -47.82666 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5b80de3c-9ca2-39d3-86d4-a1b09c14fcde | -12.17743 | -45.08522 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c3579cc-82a3-3e98-bef2-4bd8a5aca1f8 | -14.92766 | -46.71342 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7c15bbb5-88e4-3aff-998c-29b4008155b8 | -11.35501 | -44.2776 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e1d1f63-b45a-36b9-a447-4de8e9a01d76 | -11.28416 | -57.2726 | 2025-10-18 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b857feb0-61a0-3962-b5c0-d1f38031da85 | -12.4918 | -45.50642 | 2025-10-18 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0545d9dc-c9fc-3608-8d48-8e61c46b54cc | -8.05448 | -61.27692 | 2025-10-18 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6ba3e79-4f52-32c3-80cf-89137ee40588 | -10.49665 | -43.43166 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c096a3a5-9fbb-30d4-b8dd-49b5261bb1be | -11.35458 | -44.28101 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f76f015-d95d-370e-b9b2-9803da565011 | -12.59177 | -52.85262 | 2025-10-18 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a95d0246-cd46-3b66-997c-6de090b5fc87 | -11.38399 | -44.26401 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f3603f0-83c6-313c-bc0c-77d8ea892740 | -10.94831 | -45.4485 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e91935fa-f659-31b5-a985-49a9e1876612 | -10.13056 | -44.53836 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 736c17d9-77eb-3cf8-ab06-06cfea45aae1 | -13.45726 | -43.76389 | 2025-10-18 04:51:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 399cfafe-286e-3a47-a250-4c3d9351adfc | -10.95925 | -45.45806 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f47e7b0e-aea0-3e0b-ab3b-93b9fe4f7c18 | -9.32122 | -56.27163 | 2025-10-18 04:51:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e1f758b-b9df-35c7-aecf-441fb012197b | -14.90666 | -52.42155 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b35c1ef0-dd34-349d-950c-6086223d6920 | -7.86244 | -61.49697 | 2025-10-18 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4df7d8ba-ea55-3d31-a4aa-cd21219ab587 | -10.70367 | -44.56791 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8adae14-de9b-3f8d-af4a-dd8216554c90 | -12.59455 | -52.85674 | 2025-10-18 04:51:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b9a36c4-22ce-35d2-aa31-7d99eb444e6e | -10.91955 | -47.98422 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5db81fd-04c2-3151-b59f-ed6402681f10 | -10.12543 | -44.53735 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2b4ea259-6a5f-3fb6-95ca-9baa41044a83 | -10.7001 | -44.55468 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90f38630-26fd-3f0a-885d-ee4e4e730701 | -13.48567 | -48.11273 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a79687c5-7055-3933-b2d8-d8b08e1ea5e8 | -15.52869 | -45.69975 | 2025-10-18 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6b6bacd-cb5c-3366-b5e5-b7f1c96f37be | -10.23763 | -44.04648 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab42c4d8-2418-34c2-acd2-f6c808254534 | -10.55948 | -43.82195 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de13781c-4d29-396d-8cb6-d604f46295e7 | -12.17228 | -45.08476 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58044942-d633-3b25-87b6-145ccd55e70a | -11.58562 | -44.05109 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb1096a1-74a9-371b-899b-6553c4627cda | -11.00165 | -47.88016 | 2025-10-18 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f5da8d7-775c-397c-be48-008f7d8bec70 | -11.37071 | -45.26877 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ab1adff-381e-39c4-bc64-4c8d64946130 | -10.49012 | -43.43828 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6ebe52a6-2099-3c3b-8bda-08a6a6bd190c | -11.35951 | -44.2851 | 2025-10-18 04:51:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5a6e5bc-b8ac-3789-a8ba-f91b2e0e3d08 | -11.60889 | -44.08648 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 063c142c-a637-3d77-9344-6ab1f5990ce9 | -13.46465 | -47.40545 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 078d2325-74ad-39b1-8e42-2ab00a1b68e0 | -14.91144 | -46.72679 | 2025-10-18 04:51:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e1afb36-9fe8-3fc9-9aa8-3252f8e79ef2 | -10.49478 | -43.44643 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71b21c62-b601-3a96-b3ad-3da9ea9c81ca | -13.92132 | -45.59849 | 2025-10-18 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb4c990e-2538-3b1c-811d-7a0b019bccbb | -10.50037 | -43.44725 | 2025-10-18 04:51:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aba64c97-9355-3380-9516-79af7a0a4f98 | -12.15539 | -45.07572 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7119990c-41fc-3c54-9391-9b50b6fc0552 | -10.71948 | -48.14501 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fa768d7-b0c4-38e7-b558-bcdbc29ce6e0 | -10.68283 | -44.5653 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65a1c6fb-d477-361e-8988-99c833772566 | -11.25154 | -43.21167 | 2025-10-18 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84162840-107e-3529-881e-215c53729097 | -9.89575 | -55.39198 | 2025-10-18 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3fe5625-cab8-3b07-8e83-db77bdf0a09b | -11.60934 | -44.08292 | 2025-10-18 04:51:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 07d5c177-adf4-3e2e-9a56-94a8eadff6f0 | -10.62383 | -42.31011 | 2025-10-18 04:51:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 44f125e7-42bc-37d1-8046-a04cb75e5bbc | -13.77915 | -48.23926 | 2025-10-18 04:51:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 571cd4fe-d2f6-3b77-94db-be18e788e3b2 | -7.6839 | -61.04665 | 2025-10-18 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cc6c937e-966f-37da-a1bd-f914ff0c7849 | -12.16441 | -45.08656 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9475b7b5-e96f-3a6b-90ed-07a3951372b5 | -10.16217 | -44.53825 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dcbb3a2-4a4c-35fa-a941-c010c8e87aa8 | -10.15818 | -44.52854 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b71cdabf-059f-3e0c-83d7-b36fea3cb5cb | -10.99811 | -47.90549 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a67f2b55-7a7a-3f9d-af32-2982532f231d | -14.90896 | -52.40626 | 2025-10-18 04:51:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6baf2d35-42a4-30f3-b4fb-aa3369f4048b | -11.36267 | -54.32219 | 2025-10-18 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 329dafdc-a55e-35e0-a8e4-90606ec567ab | -13.72692 | -48.11164 | 2025-10-18 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d5a33ec-c1d2-3754-8455-c3a4d08863b2 | -10.69845 | -44.5673 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37cedfeb-97bc-3708-870c-e125caebfbb4 | -9.6658 | -48.52868 | 2025-10-18 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c04d3022-3852-35b2-a576-c18f6171ac8a | -10.95467 | -49.77115 | 2025-10-18 04:51:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 91628f37-dbe4-3c1f-9ddc-9fd61c9c140a | -12.16997 | -45.08396 | 2025-10-18 04:51:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f9c0320-1b91-3d26-8f10-3bc0866be365 | -10.14176 | -44.53325 | 2025-10-18 04:51:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1553154-b5c3-307a-a232-96fbb29f1659 | -13.53062 | -48.00171 | 2025-10-18 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0f6dd60-1c1c-3492-b025-ea791f6fd502 | -10.25014 | -44.03427 | 2025-10-18 04:51:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02f70227-2ead-37ce-b600-4e1489a1c39f | -10.95787 | -45.46877 | 2025-10-18 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 11de4b05-eccb-3960-84d4-349c492c42e6 | -10.97414 | -47.92523 | 2025-10-18 04:51:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9ff2a9d-eeb5-369e-8d9d-6896bd1b70ac | -9.81244 | -47.75121 | 2025-10-18 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
