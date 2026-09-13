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
| 03cdfd72-00f6-31bf-9a5f-5cbd3d198029 | -7.48934 | -49.57701 | 2026-09-13 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38787962-5f5b-36cd-92b3-eeaa310f33d1 | -2.26425 | -47.01412 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38111707-6c8b-35fb-b8bd-002019ee7ebc | -4.39707 | -42.33957 | 2026-09-13 04:14:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c0ab0d82-9818-3bd9-8bf7-84a48e51aeae | -6.96425 | -42.55829 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3324affc-1c06-3251-8a90-26e993627279 | -5.81675 | -53.80194 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4537a69f-97a3-3ff5-86d7-ac8b472a4730 | -8.97385 | -44.39376 | 2026-09-13 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4847e916-0346-38a7-b27e-8f8c5cbf43db | -7.60496 | -46.11353 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac4b8bd7-f1fc-390b-be73-bafdedbafe22 | -7.96537 | -43.99254 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0dee996d-e311-3df7-bc02-47937d3ca9c0 | -6.07817 | -51.75621 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fc98740-dd9d-3e86-a459-668786606baf | -3.16536 | -48.61222 | 2026-09-13 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2dbd284-829f-30bb-9257-393c198db595 | -7.01623 | -44.61775 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b1acd68-e9b8-3364-b733-0f7f79c138fa | -2.61356 | -54.75736 | 2026-09-13 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f51c2b9b-8a49-33df-811a-16ae26345b92 | -7.10849 | -42.10973 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 768720dd-4c40-31d0-9f47-c7402b992f4d | -5.70947 | -44.91107 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb6124ea-0430-3cb2-9567-11aafdf6a213 | -3.21897 | -48.97114 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8573e7a8-f6e9-3fcc-8d48-6fa52aa27329 | -3.04799 | -51.26265 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19524e77-d065-3dab-9164-666edde8e50a | -7.38312 | -45.35992 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d391f2a4-e771-3c42-90e1-8b97bac290ad | -2.94047 | -50.39213 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3bd863b6-3e7c-35d5-a872-5658d576b59b | -5.12028 | -41.08109 | 2026-09-13 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0f7b8c8a-0b51-3299-aba1-30a243703c05 | -4.40423 | -42.33714 | 2026-09-13 04:14:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4799d259-f12c-3ddc-8b8f-4c91748aa367 | -7.64217 | -47.18605 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dcbac8f-5e69-3598-9f08-eb1ceaa41dd8 | -2.82818 | -49.22815 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 38078d28-7c5c-3b34-918c-ee4c505a7663 | -6.76256 | -45.46147 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d7c50b7-b280-3ec0-b819-9f796e1db2dc | -7.37351 | -45.35117 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fd2ba60-9e96-3c4a-8d7d-0641ff4e81e8 | -8.28694 | -39.97108 | 2026-09-13 04:14:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ebae8121-246c-3418-a85a-4f5327733e86 | -7.29041 | -46.23927 | 2026-09-13 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0973950f-2e0e-3582-a2c5-8396fb202b00 | -7.15291 | -44.71699 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b62b11c0-2803-3dd8-bcf8-36a7daacf569 | -5.79522 | -47.77187 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 443e9b8f-e1fe-367f-bd37-856d140fa388 | -5.86303 | -46.22483 | 2026-09-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 37f8f0e7-7bb5-3a5f-b01e-da75c525435a | -6.15328 | -43.6831 | 2026-09-13 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 179f4198-968d-30c7-a69b-e14b3f7a8e83 | -1.87834 | -47.91059 | 2026-09-13 04:14:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d243141c-d568-30a7-9360-6c7760b28e52 | -1.87896 | -47.90675 | 2026-09-13 04:14:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c4e15dc-efad-359e-a8d3-299404f30671 | -2.11957 | -47.11339 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 75661319-141c-3c40-8d1e-ee3b1835ea76 | -6.24526 | -51.70671 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861f96ba-9978-3dbb-859a-ddbbc3e575c5 | -5.1226 | -55.97078 | 2026-09-13 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ed2f98fd-8f1e-3850-b8cc-a1b73d89bdfa | -6.08377 | -51.75413 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5e740e9-82ff-3ea7-8941-3639f1bcd5ea | -6.50495 | -47.59684 | 2026-09-13 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a3f3d17-9b26-3800-8dbb-8e7db7281fe7 | -3.87482 | -51.18475 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d56297e4-0bc9-35d1-a73d-cf9e739cb3f7 | -6.23669 | -51.69596 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1854c29-712b-36f1-a562-adcab9809877 | -6.85959 | -47.42639 | 2026-09-13 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 420862c5-0d89-35aa-96a5-f62f1e1f5c1c | -5.61019 | -44.85071 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bca1cfd8-2fa4-3505-af1e-eb971f21c55f | -6.51266 | -47.59793 | 2026-09-13 04:14:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 427f9106-178f-3be9-af16-bd84a3a55271 | -3.22277 | -50.5856 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb063732-98d9-38f8-9ffe-e5789e15ce31 | -2.72339 | -49.78704 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd144656-5088-3fb1-a65f-5d9b294225d9 | -2.11522 | -48.9975 | 2026-09-13 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a4cf78be-708f-3c5d-b787-bf7c73ce06a8 | -6.22761 | -51.68819 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56428901-24dc-3b09-ac58-7380a050b481 | -6.22657 | -51.69414 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e15e5078-2a6d-3a18-831e-ca65adfe0ae8 | -5.55523 | -43.43964 | 2026-09-13 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 778cfa7a-e6da-34eb-a494-7f8d38c526e8 | -7.28623 | -46.24269 | 2026-09-13 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82525be4-732b-359b-94ab-d9e045779f66 | -3.40777 | -48.8937 | 2026-09-13 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31822f88-bd1d-3361-abca-fb06a8c130b7 | -6.22552 | -51.70012 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ffb921-0e02-323d-96db-6b5b2d8102fe | -7.52422 | -47.33277 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3a3a1a5-ee6a-3234-a625-256b9ac5ccd7 | -7.01958 | -44.61829 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d2524b8b-75a7-3ee2-9bad-22b82f28c751 | -6.08096 | -51.7578 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8cf73aa-56c3-38ba-9bea-128ec5f78b42 | -6.85503 | -47.43047 | 2026-09-13 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0183a2e8-78c4-3b6a-abc4-e84175a62ece | -5.04698 | -44.43868 | 2026-09-13 04:14:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a159d23f-7de2-3d1f-9da2-0ae0a46fdf4e | -7.37048 | -45.37315 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| abc2435f-10ae-3fb4-a806-302ed5d25262 | -3.23009 | -43.03788 | 2026-09-13 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 553c1c28-101f-3ac5-8b36-d40d72379960 | -8.63577 | -47.35425 | 2026-09-13 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 330d44ad-85f2-3d14-bc6a-f8a102bbfa35 | -4.87008 | -44.90955 | 2026-09-13 04:14:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ff058fe-5374-3364-b5a1-5fe50727862b | -6.86337 | -47.42702 | 2026-09-13 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cab301b5-911e-37fc-b75b-cebe9795740b | -7.01845 | -44.62539 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f997099-434e-30d2-a137-2465cc0bcd68 | -2.02012 | -47.55228 | 2026-09-13 04:14:00 | NOAA-21 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9960044d-67fc-3052-b25a-7251146809f5 | -1.37789 | -49.41372 | 2026-09-13 04:14:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b758e4e0-4927-3a24-83f0-bd6914c9a0ca | -7.96207 | -43.99202 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df165881-235e-33fb-bc96-b74812c17cde | -2.96092 | -50.40433 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 488fb6b7-e91d-3f17-a340-d2ab46a0ad80 | -5.50501 | -44.01962 | 2026-09-13 04:14:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b301744f-4f38-3907-85ad-c6e7bda85d60 | -2.86697 | -49.62573 | 2026-09-13 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf56b717-4331-3974-8520-58eed90d89fd | -2.95694 | -50.39812 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c5a47fc-57c6-34a3-88f1-b8c2b36a06d3 | -7.3745 | -45.36996 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38dcc00f-27da-3162-8bae-597fbba6bde3 | -4.92869 | -45.83245 | 2026-09-13 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a3a80786-bfc2-304a-8a64-07f2ea0a8561 | -7.55708 | -41.84076 | 2026-09-13 04:14:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ec295181-0a78-360e-a0bd-001ffa324590 | -5.80942 | -53.8093 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d394a75-bf89-35f2-9b2d-a7e8c7330771 | -7.19995 | -45.9259 | 2026-09-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ecdc9a8-e876-3dbf-94e3-327c70e34670 | -3.79365 | -48.93788 | 2026-09-13 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 676f56b9-c0d5-31b2-a642-c0c7282082f2 | -9.6057 | -40.35552 | 2026-09-13 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 7e7ee308-f278-3683-a314-09e2a0090124 | -6.79149 | -48.66217 | 2026-09-13 04:14:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 305d20c7-150b-320f-b434-47529b214147 | -6.00163 | -44.25727 | 2026-09-13 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 354bf5fe-8403-35c1-b826-2fb61b8341f2 | -4.40038 | -42.34008 | 2026-09-13 04:14:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 093434b1-26a8-3d63-be6d-0419102301fc | -7.59553 | -46.96991 | 2026-09-13 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4624d914-873c-375f-bdf4-3b6f5f527f01 | -7.18883 | -45.88437 | 2026-09-13 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fd2a12b-f775-30d2-a284-cce104abff1e | -6.6592 | -44.96307 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e9d2957d-44b0-331a-aaef-e2ae6a61509f | -7.54573 | -44.90728 | 2026-09-13 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d46887be-27f7-37a1-95ef-c4eaa9c41010 | -7.46936 | -46.14495 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dbc2d36a-997a-3f28-a95b-190d33b0ea73 | -6.69513 | -45.90336 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fa38850b-c875-3b11-b74b-abd3ea6a1f24 | -7.60431 | -46.11747 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd46a16d-00ec-3cac-beb0-b00f6dc7c63c | -8.60071 | -44.42978 | 2026-09-13 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d081ae2-13d6-3708-95c4-9fc189855c37 | -3.40339 | -48.89299 | 2026-09-13 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8f4b021b-bcc1-3931-8708-67577892e2a8 | -9.60201 | -40.35497 | 2026-09-13 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 35.0 |
| be00a5b0-1495-30a7-8530-d16b879b76b3 | -7.36999 | -45.37344 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 2a915d34-ca0d-37b5-9b3d-73d71d1ab018 | -9.3187 | -40.60828 | 2026-09-13 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d9900761-a5d4-333b-85c4-7bc750902f7b | -4.39322 | -42.34251 | 2026-09-13 04:14:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 40d33bc5-c479-3260-8807-7ca93910e02d | -6.83338 | -43.51116 | 2026-09-13 04:14:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afd67f7a-a5fa-36dc-ba11-1f29a63c46e5 | -7.1124 | -42.10667 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0d1ab2d-77f0-32cb-9fd6-12625536f276 | -5.61418 | -44.84758 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ea6d7f3d-a339-31a8-a7c6-1f7f3dee6dcc | -6.95947 | -44.54333 | 2026-09-13 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a6a76c2-4d57-3f65-a73a-223d21443fcc | -5.18521 | -49.34767 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eefc04fd-a76f-3783-a6f5-b965f0af665a | -6.22605 | -51.69712 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87eab3af-3b4c-3064-841a-b8922fe0b51c | -2.11875 | -47.11854 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 869db218-6f29-3070-99f9-ab379a8c0878 | -2.86499 | -49.62778 | 2026-09-13 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README23.md)
