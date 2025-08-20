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
| f04e86c8-d049-3771-bdaf-03fd94084708 | -11.02762 | -44.59398 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f32b5723-c652-35a4-8794-a33095600afa | -13.71016 | -43.89546 | 2025-08-20 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22cd4396-9900-3866-8d0d-c3bd02cdf8c7 | -13.03928 | -46.80614 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d630e8a9-d15d-391d-a045-8e1ad23f700f | -12.14453 | -48.01711 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b75b7b63-8678-3eea-817a-a90b1a25aa47 | -10.99815 | -45.60581 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6684d0c2-19b7-3b57-b27d-6623bb807df8 | -13.61149 | -46.88568 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5845773-eafb-30a1-b1e6-235c93b81f16 | -15.00031 | -54.82401 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 228935c8-f2e0-39e6-863b-3da3fb8c6c5f | -11.44408 | -47.31063 | 2025-08-20 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0809c307-35d1-3ced-87a5-3034c14ad505 | -14.50317 | -45.95717 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c98903fb-c958-3d99-8676-43c8634ceb04 | -14.16614 | -45.28001 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c5277f2-0d75-3e6e-ae66-362b7b1581d7 | -17.5562 | -44.48293 | 2025-08-20 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d9b9e2-6528-3194-9240-51496e472e49 | -13.00805 | -45.18269 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f0333f5-7daf-3073-951f-51e68bcd3cbc | -15.54808 | -42.28853 | 2025-08-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f865f17-8f9a-30a0-83ce-26c1bbedb580 | -17.16598 | -43.97779 | 2025-08-20 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 562cd233-73af-3059-aded-a7769e529c76 | -11.13144 | -46.98507 | 2025-08-20 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9190400-b485-32e5-a80a-c98b6996b2cc | -13.14311 | -54.92494 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f677006c-97af-3d54-bb0d-f99ce6bb4e43 | -11.44323 | -47.31552 | 2025-08-20 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d82f6774-e255-36ab-8b9f-bf4b7f9ffaab | -13.41161 | -46.35525 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82f260ac-9c7c-33d0-a18c-fa6534f3142c | -15.81101 | -45.34491 | 2025-08-20 04:10:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24f66a84-2049-3d81-bf5a-631b4645c5eb | -11.73807 | -48.1885 | 2025-08-20 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 849e8cc9-5a3b-3dc4-8b4d-f69aac70ab89 | -15.5734 | -50.3103 | 2025-08-20 04:10:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55fb15d8-a666-3793-ac58-3ad640ea0da1 | -11.97598 | -46.77875 | 2025-08-20 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7d88e13-dafb-3fdf-a27f-6e14d1022027 | -14.62072 | -54.88883 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c888bc36-d36f-34e7-856b-c13a021302e5 | -14.15083 | -45.28483 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63f5b27b-b7f9-3fa7-b54b-662e525bd7f7 | -12.99556 | -45.21569 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57b86d56-8c8b-3567-9832-39df28bb711b | -16.48464 | -45.09686 | 2025-08-20 04:10:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc1b1930-cc55-3e33-a84e-a85458b85738 | -13.73785 | -52.01593 | 2025-08-20 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dab831fe-b171-3a77-9dff-933ec0d9624b | -12.91292 | -46.10172 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc23fdb9-bc4b-3f70-81c8-80380326af70 | -15.75274 | -48.29294 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8d3af482-69d7-36c5-9841-43c17c2a1c17 | -17.67625 | -50.48315 | 2025-08-20 04:10:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbece7c1-5ed8-3a4d-93d1-586f8bba53de | -14.88938 | -48.08546 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bec0ee97-cc49-3eed-bc91-7b6b6bc8228c | -11.09366 | -44.81289 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a67da074-2f73-36de-a71e-3331264b0b7a | -11.13681 | -46.97647 | 2025-08-20 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f4ce943-29bc-3670-8cfe-8300c2f9b886 | -14.99345 | -54.82738 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86a0b946-e5aa-3ecc-9d8a-9896accbb6aa | -15.05401 | -54.83125 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 483c4804-74f8-30ae-a7cc-6abf5c981045 | -14.16212 | -45.28317 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c4f920-e8ba-3090-be7b-25530dabe52e | -14.37139 | -47.69166 | 2025-08-20 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 411beaa3-9242-3ee6-9aee-fc9ff916b9fa | -13.57521 | -47.03052 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 94a5dc35-9658-3f3d-9998-5da0e6433faa | -10.60264 | -48.60096 | 2025-08-20 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3266620b-c452-37bb-ba39-88dfc003a61c | -12.96946 | -56.84875 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 909fea51-174f-3ba5-9122-270af6657f33 | -15.00126 | -54.81952 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4bf961f2-ec50-3bb3-b2a0-3a8344e93f2f | -13.15023 | -54.92125 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1025f1e7-548f-380e-b8cb-a2e4371c4f33 | -17.05585 | -48.30716 | 2025-08-20 04:10:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5fbeceb0-1ecd-3359-b868-f4f6eb0290c1 | -14.99839 | -54.81368 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b3ad709-e671-307c-95e4-4df134e9ccb7 | -13.15888 | -54.94048 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1caaccb4-6c8b-314b-a880-b302b2801f32 | -23.40216 | -46.50751 | 2025-08-20 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5f7eef68-d888-310a-953e-6416eebc5429 | -21.21261 | -46.95495 | 2025-08-20 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb9ab637-268e-3570-8d9c-ece5eb5e76f0 | -21.31618 | -48.67507 | 2025-08-20 04:12:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2bfbed29-cf39-3b2c-82c8-0758f095345b | -20.34472 | -51.70437 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 764b377d-f9e1-380b-9754-d3952b29f3f7 | -19.12218 | -46.60294 | 2025-08-20 04:12:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9861c1a-14df-3a10-b99f-1a44920eb14b | -19.76705 | -46.04034 | 2025-08-20 04:12:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1facfda1-3805-3998-9c40-1cb496d71d60 | -21.89561 | -48.18848 | 2025-08-20 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fe2a60c-677e-37e8-9ba0-487eb121ffdf | -20.3342 | -51.71146 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 34871925-a537-3e7a-ac4c-92fbee856a9c | -17.66491 | -54.06191 | 2025-08-20 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c4b630b3-14ec-3dd9-b00c-cdf144a31f05 | -21.90181 | -47.24875 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9de65d86-4b78-31ca-92f3-e0502ec3aa05 | -19.45645 | -45.3074 | 2025-08-20 04:12:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fe3d5f28-5beb-3bde-af51-07ea9a6096db | -17.66563 | -54.05853 | 2025-08-20 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1851677-6cca-310e-805b-db2d2831cf72 | -18.82947 | -48.56559 | 2025-08-20 04:12:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 679e81d3-74b6-341a-9591-aef35bda46f3 | -19.88705 | -49.8386 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f8a9ea56-a854-3cf5-bb79-b0e3c69e5a97 | -20.33936 | -41.42037 | 2025-08-20 04:12:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 261ea1f5-522a-35cf-8d0c-66a41b7a7ad3 | -19.86547 | -49.82299 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4bbfe381-166d-3b68-90d9-1a4e1ccf653c | -21.8928 | -48.18372 | 2025-08-20 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0d181cb-54f3-3a90-8968-5b0c905a6c55 | -22.55915 | -49.77594 | 2025-08-20 04:12:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8900076e-83e8-367b-a7ed-701b1bafa167 | -23.76773 | -48.8681 | 2025-08-20 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8c2941a1-a283-3d5e-b4bb-091f3e0f4e5d | -18.67546 | -46.98394 | 2025-08-20 04:12:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0d5e42b-75ad-32bb-85c8-4d07cb70f29b | -19.01184 | -46.65238 | 2025-08-20 04:12:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9a9e1ca-258e-3ff7-9cf4-b7f635396917 | -22.41008 | -46.62108 | 2025-08-20 04:12:00 | NOAA-21 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c2dc9923-f572-3275-a761-912961df1d52 | -19.87824 | -49.84214 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 13c8d07a-7545-37bf-8210-b874bcd12127 | -20.75654 | -48.87638 | 2025-08-20 04:12:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 39165037-c6cc-3344-b6d5-e3e6fb968cde | -19.55185 | -47.75219 | 2025-08-20 04:12:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43c3df82-aca3-329f-ad5b-cb3ba7d82d56 | -19.74642 | -46.04008 | 2025-08-20 04:12:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37f58032-2675-3deb-a80e-61c6f19b9385 | -21.31163 | -43.258 | 2025-08-20 04:12:00 | NOAA-21 | RIO POMBA | MINAS GERAIS | Brasil | 3155801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| d5b957da-797f-3b72-82e4-7b4ee47891fc | -23.49539 | -46.15995 | 2025-08-20 04:12:00 | NOAA-21 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f716a372-0312-32a5-b589-bf57c5b26133 | -20.29433 | -44.27477 | 2025-08-20 04:12:00 | NOAA-21 | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d505281-d423-3b99-adf2-4293e27c9a05 | -21.20856 | -47.06237 | 2025-08-20 04:12:00 | NOAA-21 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be58a734-391a-3be1-b88a-e4c3a2bc247f | -17.66215 | -54.06084 | 2025-08-20 04:12:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45038786-a113-3a79-a9b5-543b628d5d4d | -19.72676 | -48.97937 | 2025-08-20 04:12:00 | NOAA-21 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 8837d7c2-0de0-3dc3-b0ea-85ae3e88619c | -20.33857 | -51.71241 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| a3f53010-91dc-39d2-b87f-863fba093518 | -23.23462 | -47.29559 | 2025-08-20 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6d993159-59d0-3621-8f82-8a76a20dfd0c | -21.35297 | -41.91894 | 2025-08-20 04:12:00 | NOAA-21 | SÃO JOSÉ DE UBÁ | RIO DE JANEIRO | Brasil | 3305133 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 46b77340-d63a-31f8-a0c9-305ce4243efa | -23.08782 | -49.93751 | 2025-08-20 04:12:00 | NOAA-21 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1a08d58b-3601-3c33-9daf-40cfd6976dea | -20.3351 | -51.70695 | 2025-08-20 04:12:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 564cc186-5b9b-3f23-a8a1-51fc48792238 | -21.50393 | -45.46046 | 2025-08-20 04:12:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 96583a2b-8a8b-3aff-9a2b-b3a591383b50 | -23.70443 | -50.23478 | 2025-08-20 04:12:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1051cf8a-7246-3d62-88e8-5ba6732bdf41 | -19.56693 | -45.97338 | 2025-08-20 04:12:00 | NOAA-21 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0481626-782a-367a-956c-ae8267114fcb | -19.87528 | -49.83606 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3060cbb-4b8f-3178-b809-89e0810acb47 | -22.45165 | -47.55607 | 2025-08-20 04:12:00 | NOAA-21 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 726cf5db-12d3-331b-ab85-d973a14939dd | -21.89208 | -48.18784 | 2025-08-20 04:12:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b44f380-aa42-398b-b63d-2db5d90eeadd | -20.21816 | -44.12929 | 2025-08-20 04:12:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c20940fa-8e29-3bf1-92f4-ce5727b2942e | -20.95131 | -41.14046 | 2025-08-20 04:12:00 | NOAA-21 | ATÍLIO VIVACQUA | ESPÍRITO SANTO | Brasil | 3200706 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 25fd387a-a634-3eb1-a30e-2410e6c0f1f4 | -21.90233 | -47.22456 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a52c9e3e-d1c9-36fd-8aac-63e3cbf542c0 | -19.45859 | -44.73412 | 2025-08-20 04:12:00 | NOAA-21 | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9b5424d-de91-3932-be67-3792dc670900 | -21.90508 | -47.22915 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 7d9543cf-15d1-3da7-8212-973bda4ac549 | -20.95262 | -46.09861 | 2025-08-20 04:12:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a831273d-c1cf-3817-a5e3-0549dfd5d552 | -22.5554 | -49.77514 | 2025-08-20 04:12:00 | NOAA-21 | SÃO PEDRO DO TURVO | SÃO PAULO | Brasil | 3550506 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| fb7e4006-963a-35f4-a45e-d2d46c8d2ee9 | -19.45243 | -47.18904 | 2025-08-20 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d13ced95-ed1c-3beb-9592-73671815f40b | -19.88119 | -49.84827 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8f98646-0125-375c-a353-a222e9c6077e | -19.80652 | -49.83281 | 2025-08-20 04:12:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 684f9da5-5c0b-3213-82d9-f8129dc02d44 | -21.90209 | -47.24793 | 2025-08-20 04:12:00 | NOAA-21 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 312c7b5d-a024-3a81-aeeb-a1ad6e4f94d6 | -21.72192 | -46.49413 | 2025-08-20 04:12:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |


[Clique aqui para ver as próximas entradas](README23.md)
