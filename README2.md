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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16ce446c-012c-3a42-8a16-789c0fb259d9 | -10.66703 | -48.25706 | 2026-05-20 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ae4ebf2-b1fd-3489-9c9b-123fec9a8529 | -12.05594 | -45.27349 | 2026-05-20 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48ff99c5-c0c1-38bf-bf46-1622e7c2eead | -12.60273 | -44.52527 | 2026-05-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0c788943-cde4-3d3e-a9e9-09dbce533889 | -8.61446 | -45.99649 | 2026-05-20 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36ed896b-fea1-3873-b512-9332377e78bd | -10.57836 | -46.65675 | 2026-05-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb854110-fbad-332f-bfd8-f9db9acee804 | -11.10159 | -46.50072 | 2026-05-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d6e7eb1-13ca-330d-a6b5-73bfdbc80bf5 | -11.59983 | -47.10514 | 2026-05-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dadf1bb-1faf-3a1a-9a5d-6c3135def318 | -8.70499 | -47.91041 | 2026-05-20 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d53a952-5120-3404-8e97-742c093a0e5c | -10.49336 | -49.36928 | 2026-05-20 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d067b94f-f57f-3f24-85c3-0cdbfee40fbe | -6.75313 | -45.0141 | 2026-05-20 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b2e1a2d-bf48-379b-b62f-7b2714d596ca | -11.21416 | -41.65025 | 2026-05-20 03:49:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b64fec6f-d9e0-3210-9a1a-4adec85530fc | -11.95616 | -44.19025 | 2026-05-20 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf22bf89-0061-3cf3-8f00-98f3e33c9080 | -10.48812 | -49.36312 | 2026-05-20 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25165880-703e-3091-bacb-24a312842bec | -10.49964 | -42.40392 | 2026-05-20 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cdedd1a3-73cb-3425-8e25-f2202a6a9f24 | -10.57313 | -46.65584 | 2026-05-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85593354-04c8-3ae3-859c-0f5287bc2d52 | -8.73505 | -47.97691 | 2026-05-20 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e033b5e5-804a-3f3e-8008-590887aba348 | -5.72796 | -43.43597 | 2026-05-20 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f0ae7298-7cd4-3a8b-8722-9d2ed0a00fe4 | -5.73255 | -43.43663 | 2026-05-20 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6d9a0ec-7fa0-3add-bef4-aac14d62323d | -8.55545 | -45.99013 | 2026-05-20 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 834048cc-f085-3ec9-9585-6e9963f33d67 | -11.01729 | -45.13008 | 2026-05-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ffde9cee-f923-38a9-9409-bfd328d2e427 | -12.226 | -44.248 | 2026-05-20 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe007c1-aec9-3aae-9ae6-deacbc2a3f4d | -13.02117 | -42.68276 | 2026-05-20 03:49:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 725799e3-320d-3c6c-9ac0-9314507022bf | -11.10227 | -46.49714 | 2026-05-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d499f35-7f49-3c43-809d-3197c1384982 | -11.04947 | -49.53476 | 2026-05-20 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4c9331b-369a-3468-ba1f-a615e0a7d57b | -12.44882 | -44.75014 | 2026-05-20 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7db42efa-306d-36a9-884c-4a655cb47ab8 | -11.94705 | -46.93058 | 2026-05-20 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b03352b2-bd30-32c2-97e6-a99b2d029ecb | -9.7458 | -37.16257 | 2026-05-20 03:49:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 858269d9-9a11-34b8-b2eb-fb28796fbeed | -11.07433 | -38.64424 | 2026-05-20 03:49:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 47e16fb6-28cf-3801-a0b7-37e3fb10efba | -12.22975 | -46.60915 | 2026-05-20 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7887a116-d199-34fa-80d6-bc590961d4c7 | -8.70343 | -47.91874 | 2026-05-20 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffd40f22-f214-3127-8a58-742dc3c21ba5 | -9.2205 | -46.67317 | 2026-05-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f28a16a9-3c28-318c-9f78-3791a7a1a04b | -9.21819 | -46.6687 | 2026-05-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b5bfb9d-60a7-3e36-8616-aecb924fb932 | -12.22448 | -44.25656 | 2026-05-20 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c59864a-4447-3f96-86c0-2d35bce7d961 | -12.06611 | -45.28801 | 2026-05-20 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8fe9b3dc-ab9c-3eef-b208-4040526ef333 | -5.75249 | -43.40152 | 2026-05-20 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29e95e3d-d84c-3bfc-8cea-6fd88cb8db0c | -8.71008 | -47.91558 | 2026-05-20 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffbc5d0a-1ef5-3569-b30d-8a01c72eaca2 | -8.09994 | -44.12524 | 2026-05-20 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 07887c85-9dab-3aac-8efa-667829b99bb1 | -9.22181 | -46.66621 | 2026-05-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ddaa808-c3d3-3964-adfe-f127f32cd3a3 | -8.09488 | -44.09995 | 2026-05-20 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6942ca3c-cacf-39b2-b739-8c04fcfe6582 | -11.01469 | -45.13169 | 2026-05-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e2322de5-e1f3-3887-bc33-0a6c15b58939 | -7.01434 | -44.99292 | 2026-05-20 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d2a9b19-81ac-387a-9ae4-c3f2819609a9 | -6.75263 | -45.01697 | 2026-05-20 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 945e9828-2142-3a3c-8b0f-0abd3f7cb0bc | -11.47231 | -47.3391 | 2026-05-20 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4350a451-c512-3931-a680-456c20588acf | -10.66782 | -48.25299 | 2026-05-20 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a209b1ec-864b-3d43-9142-6740dcc4fc5b | -11.60045 | -47.10182 | 2026-05-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a8007560-7701-3707-b20f-476e56301dad | -8.6133 | -46.00288 | 2026-05-20 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 35416502-721a-3389-9431-bbac5389ad62 | -9.22115 | -46.66969 | 2026-05-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3cb945-5e21-3cc0-a799-f3e5fbc8deb6 | -12.59836 | -44.52451 | 2026-05-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c8ce342d-401e-334d-9bda-382cc0d923a7 | -12.22527 | -46.60513 | 2026-05-20 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6785ddf-2c96-3071-a538-55170954f750 | -12.22524 | -44.25229 | 2026-05-20 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90cf5a58-a1f6-36bf-b235-de657a11eed1 | -8.73423 | -47.98134 | 2026-05-20 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 36a04998-dea2-35f3-bf39-85a72c331f67 | -12.06148 | -45.28711 | 2026-05-20 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67664ade-1025-322e-b612-0d8dbaa45fb0 | -6.64135 | -44.49548 | 2026-05-20 03:49:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a46dc47-40fe-387e-a672-3eb09ca262b1 | -10.40078 | -49.44495 | 2026-05-20 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 758df5bb-8270-3b00-beca-abac421c59ba | -10.39726 | -49.44203 | 2026-05-20 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 446d1e98-03c9-3cb6-925f-cb2184919dcb | -12.22728 | -44.26591 | 2026-05-20 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96345ee5-5676-3702-b7c1-6e209802a733 | -11.47167 | -47.34238 | 2026-05-20 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bd2a363f-5941-3848-b8fb-f343c00d043f | -10.66861 | -48.24894 | 2026-05-20 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c13052-6470-37f4-8e8a-b11a95fbf996 | -11.92714 | -43.87083 | 2026-05-20 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 71de8e19-612d-36d1-a479-7701324bc9b9 | -9.21757 | -46.67218 | 2026-05-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0615707-e192-3829-a8ad-f50dbb018ec3 | -8.69914 | -47.90937 | 2026-05-20 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee78f669-8eef-35f2-a6d8-e491f8443748 | -11.92786 | -43.86681 | 2026-05-20 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f48479ff-4501-344a-a05a-198051db3fa2 | -10.37957 | -45.13038 | 2026-05-20 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6243a984-531b-3f9a-9e80-a06cd2d5ce3b | -8.09405 | -44.1047 | 2026-05-20 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40688f03-4d56-33d8-a3a8-b5a1990128c2 | -7.40159 | -46.62596 | 2026-05-20 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 13cbc3b5-51d4-3a23-a754-84a99eb3a400 | -8.55026 | -45.9893 | 2026-05-20 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9931d8ee-ef5e-3fb3-9c86-d3489a6d6f0d | -9.73613 | -37.24663 | 2026-05-20 03:49:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 42318c24-b4e7-3b81-bd64-125db8ecb951 | -8.70929 | -47.91977 | 2026-05-20 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8b3356c-7ec3-3b33-ae40-c307822ce142 | -12.22804 | -44.26162 | 2026-05-20 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e8811a1-1b3a-31ee-9784-049c4eb45e28 | -5.94941 | -43.49192 | 2026-05-20 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 97cb14ab-a155-3813-87f4-d9fb873bb0fb | -12.59914 | -44.52014 | 2026-05-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 904f6173-1fc6-387a-ba6d-d5a49195ad5e | -6.75716 | -45.02055 | 2026-05-20 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd73c097-248a-3a46-a533-6e68dc77727e | -8.10077 | -44.12048 | 2026-05-20 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ccde094-bd06-3629-b404-bd5ec15abfef | -7.72496 | -44.55093 | 2026-05-20 03:49:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73479c6c-de57-385d-bd3b-68375821f9eb | -11.93682 | -46.92779 | 2026-05-20 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 953cb2d6-5088-3d6b-8f33-2ad4d18e9148 | -10.49753 | -48.10848 | 2026-05-20 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85b144e0-792e-31e2-9859-560314a718ca | -12.60867 | -44.51738 | 2026-05-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 83466927-a846-36c6-8d2e-6705d20b4aeb | -8.09782 | -44.11021 | 2026-05-20 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eed39e0-8b93-3afb-b2e6-5c12808a8c9f | -9.21881 | -46.66523 | 2026-05-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a595a91a-2bec-3da6-ad4d-62efd31c143c | -11.04328 | -49.53345 | 2026-05-20 03:49:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c75ef99c-a77c-37ab-82f1-1991c1b978a8 | -11.9522 | -46.93178 | 2026-05-20 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9961792-06ed-312b-9953-225c8762891e | -10.49673 | -48.11262 | 2026-05-20 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 58e58559-3360-366c-a351-6108e58d82bd | -5.9502 | -43.48719 | 2026-05-20 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d7221bd5-a722-351f-bad7-0f48980bcb2b | -8.61388 | -45.99967 | 2026-05-20 03:49:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d73f2fd1-08d9-33be-99df-ae5e7aabdb8c | -10.49569 | -42.40324 | 2026-05-20 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6be02ab0-62d6-374a-b952-6532e5444a7d | -5.75171 | -43.40618 | 2026-05-20 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 113397fb-fb4a-3cfb-a749-1ef84aa3b1c2 | -11.02183 | -42.85603 | 2026-05-20 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4a4663b5-f1d3-339d-b2ed-6d2bd912ca50 | -5.95398 | -43.49266 | 2026-05-20 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47888a2d-5490-314d-b8ae-9618bea2861d | -12.2235 | -39.29351 | 2026-05-20 03:49:00 | NOAA-21 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ee75531-fd28-3f5f-a482-dd20f3f52ff9 | -14.15941 | -45.30978 | 2026-05-20 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2fb95620-a8b6-390e-8b8d-5908de8a955e | -17.71323 | -42.22875 | 2026-05-20 03:51:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7c8fb32-b9a6-3e51-86a9-f282c53c7bd7 | -14.93176 | -47.7534 | 2026-05-20 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4f991c9-2643-35b0-b0f4-56f62fa65baf | -17.80192 | -46.71356 | 2026-05-20 03:51:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 687b2fb4-84d5-36ae-8ffc-b59b64b2b454 | -14.9324 | -47.75014 | 2026-05-20 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 870f03b3-7e13-3753-827f-c82c178f0f82 | -17.77308 | -41.74741 | 2026-05-20 03:51:00 | NOAA-21 | POTÉ | MINAS GERAIS | Brasil | 3152402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ca32b8fd-f5c0-318f-bde5-96b8dc998efc | -17.77375 | -41.7434 | 2026-05-20 03:51:00 | NOAA-21 | POTÉ | MINAS GERAIS | Brasil | 3152402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 952804e8-f294-3053-a606-a6981435d0b9 | -17.7097 | -42.22803 | 2026-05-20 03:51:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a0475c6-95fd-344b-b944-e0436d84e5c8 | -14.15856 | -45.31435 | 2026-05-20 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e98e348c-4f36-33e2-b9bc-4d58bfdde0ab | -14.91303 | -47.73911 | 2026-05-20 03:51:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 26b4a6d5-8f97-3437-8e6b-a0087dedb778 | -16.07154 | -45.89302 | 2026-05-20 03:51:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README3.md)
