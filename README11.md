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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c78fcdb3-f3d9-3152-b616-9a213af899a5 | -7.29728 | -48.42393 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 061fc665-fb90-3e32-acb5-9e51c246356f | -1.73912 | -52.02645 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e17c2ac4-c9cd-33f8-9f12-aeee51512ca7 | -1.31949 | -53.14833 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1f13062-dd99-387c-814d-4ba403ae66df | -2.89415 | -56.94075 | 2025-11-23 05:16:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c8a36c5-1aa4-3174-a556-e72d6cdebc63 | 0.5843 | -59.20869 | 2025-11-23 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bab7b8df-dd89-3a2e-a921-955b5bffcfea | -2.95892 | -53.27778 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0719653-ba14-304d-942d-76a1be86daa3 | -1.755 | -52.14269 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00c99bdb-7894-3774-8d1c-bc6864f73de1 | -1.73422 | -52.02096 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 95135166-4db2-3f54-bb30-54bf52590a1a | -2.9568 | -45.43392 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4712ad33-cc94-3b1a-897d-5a74d4345c64 | -7.29791 | -48.41934 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a55371f-6b1a-320b-be2b-dee741e20030 | -2.63182 | -47.29989 | 2025-11-23 05:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88699c59-140e-3fb8-9d8b-5a77c937dea0 | -2.6378 | -47.30081 | 2025-11-23 05:16:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c60e51f-a3b9-3b61-970b-5c417a8ddfcd | -3.46593 | -52.2309 | 2025-11-23 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e5a177-8d84-370c-af7b-74bc31e51bd8 | -1.3124 | -53.14202 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9a7aacd-eada-3113-b685-caee49cf4708 | -4.71033 | -46.46512 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f34ef6ed-a2af-3f89-a6c7-06a57420775b | -1.67471 | -46.45741 | 2025-11-23 05:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdfb637b-3e99-3989-bd75-09026478661e | -2.9584 | -53.28125 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c837145-6bee-3f48-bcf0-642dd0a2a14f | -3.17863 | -52.95504 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbb3105-d03a-397f-9429-a48ae5d935af | -3.86298 | -51.14132 | 2025-11-23 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b44a6b9-5c33-3edb-9905-bd4f3c1c9bdc | -3.17451 | -52.95447 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0ca4a4d9-b7e3-36a5-9e91-e7e0076d2b88 | -2.95787 | -53.28477 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d345c8d-a497-3ad6-9811-8f0ea2a8f0b1 | -4.71759 | -46.46077 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2d903f0b-c623-32a6-bae0-ab4d498fe41d | -1.74217 | -52.02633 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ff06bfb-93d0-30c1-98b5-ad7b254d6a4c | -4.71746 | -46.46338 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 50569b52-d367-364d-9f91-da7da9af807b | -1.7404 | -52.01843 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 921cf1e3-5467-396c-a0ba-108dc5f2422c | -1.73789 | -52.02564 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d17514b7-0941-335d-a117-69721c4a07f8 | -1.74278 | -52.02229 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f24f615-f6fd-3da0-9190-8566f8ac8516 | -1.32818 | -53.14457 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41a37668-60ea-32b4-9e4f-7046d25b1c34 | -1.30845 | -53.14139 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28fed747-1fc4-35e7-a6c9-566ff1533918 | -1.31161 | -53.14702 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 295c84bc-bc2d-3383-94f5-99198547c07a | -4.55495 | -45.49473 | 2025-11-23 05:16:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4f430c8-6ef0-3774-acb3-be86b4bea772 | -4.56145 | -45.50155 | 2025-11-23 05:16:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7e20cd1-dde0-3d2c-9e9a-4c7eba040175 | -4.55536 | -45.49504 | 2025-11-23 05:16:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d81542a-d198-3f1b-9b11-48c74c87aa00 | -7.30692 | -48.39802 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0e156d1b-237a-3f4f-8b4a-a24765e09d9d | -2.89189 | -45.28407 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1832c139-32f0-3637-ad37-475b2a7a61b8 | -2.95355 | -45.43723 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3226cd94-b3fe-3102-a7d0-e72424eae7a6 | -1.7385 | -52.02162 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 420c9766-36dc-3d2b-a9ea-a1456d406a02 | -1.64892 | -55.56037 | 2025-11-23 05:16:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ea4acf6-9011-3a0d-a8ae-05ee19cc68de | -1.73361 | -52.02499 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a374ae6a-c50a-3180-bb60-579a7587c5c0 | -1.09225 | -54.10456 | 2025-11-23 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caac8acc-d8d2-3120-a976-fb11b3d5bdcb | -1.73548 | -52.02179 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2e9056a1-f6a5-3027-93e0-6d0867736dd7 | -0.85544 | -52.70908 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c2c6148b-bfbb-3063-b8d4-302f70e80a07 | -7.30097 | -48.39714 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5bc398f0-1932-3447-9868-15040dd93de6 | -2.87732 | -45.28845 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a36cb032-3440-345a-9a53-7a119dd8ee51 | -3.26406 | -53.26315 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9811bd10-3a52-3148-9ce7-d3800ad773b1 | -2.89324 | -45.28505 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9142af0-3653-35c3-bbee-2f26f5740b33 | -1.73848 | -52.03046 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ab07128-486d-3438-9cd9-45c3e7a7881b | -4.71606 | -46.47119 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d27184a-4517-3b00-b044-12e2bb02d3e3 | -1.25056 | -52.63472 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| de03b0a1-b1f9-38a9-9f0e-239e12ca3889 | -4.71683 | -46.46599 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ebfae2b6-e2b0-32d6-80fa-2b26ef5c3265 | -1.74584 | -52.03102 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1aef727-dbfd-3d90-a3e3-b31883696511 | -2.88733 | -45.27795 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| eb3d1407-a794-3246-979a-4b03adb22994 | -1.32423 | -53.14397 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 265164cd-bc1c-3917-b08b-931236f415a6 | -1.73976 | -52.02244 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c5a34c15-a220-3071-a4f1-cf90af0acf6a | -3.75577 | -50.94116 | 2025-11-23 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e380c8fe-b163-35c7-a078-9c0daff606ab | 0.64249 | -59.73002 | 2025-11-23 05:16:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61eb958b-8905-3ea1-bb10-abbf6695592a | -2.95593 | -45.43987 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c1ff00c-3589-3249-bd7c-752cebd0752e | -0.85949 | -52.70964 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fcd9778-8b37-363d-a261-a7f2f102c5a2 | -1.73484 | -52.02581 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da19bb33-964f-32e9-b493-0ac2d64dcbec | -1.75075 | -52.14205 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 427f13e3-b12e-3664-bbd1-2304d517c443 | -1.33371 | -55.39975 | 2025-11-23 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b36bb43c-deb6-319c-aa42-3d5fdacd709a | -1.88711 | -50.97531 | 2025-11-23 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b22f432c-d65d-3c57-b628-1d8c992c8117 | -4.71023 | -46.46775 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6e8c391e-7c5b-3c67-9daa-42a33d313809 | -7.30366 | -48.39994 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fb725b88-307a-3074-825e-fd4b2d02c09c | -1.73729 | -52.02966 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b2e0236-da35-39c8-b176-c96050fe79e6 | -2.95447 | -45.43116 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78b5b5a2-7c90-3c50-b748-8528b4ae0b7d | -4.71096 | -46.46252 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 85a36804-b4d8-3d18-bb8e-7832f0e31bc9 | -3.46655 | -52.22682 | 2025-11-23 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 874ba8e7-71a8-344e-8f8f-be0fc2c094c0 | -7.30074 | -48.42227 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dabfa20c-256e-3f2b-981a-f083a3f12c70 | -1.67397 | -46.4622 | 2025-11-23 05:16:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 190f675c-1791-3fc5-8deb-9472fe176d4d | -2.88508 | -45.28317 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| dadeeaae-4674-34a4-8fcf-3522dc2592bf | -1.19409 | -53.71999 | 2025-11-23 05:16:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87b9d852-f901-3941-9a22-2b90710bfe6f | -9.54792 | -47.77427 | 2025-11-23 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9093dd38-5f0a-36dd-bc59-f9887a7a0a1d | -11.87734 | -57.00929 | 2025-11-23 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc6fabb9-e03a-3ca4-9e2a-76d35cd80aa9 | -11.49207 | -58.44152 | 2025-11-23 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1588db7a-7e6f-3b10-888f-ddeda7cec9f8 | -11.49547 | -58.44207 | 2025-11-23 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28b7ad0e-5d8d-39ac-975d-a3db75fedd27 | -11.49151 | -58.44524 | 2025-11-23 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eaf0a8c3-2a78-32ab-b1e8-d8d7e62a0cfc | -11.20716 | -57.96421 | 2025-11-23 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 45b8bd13-b4ba-3ffd-a609-12614f0c5b33 | -9.5543 | -47.77506 | 2025-11-23 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31ceffd2-30d0-3a77-887b-3b8702df83e6 | -20.88224 | -52.33304 | 2025-11-23 05:20:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c41e48b-a83b-3121-9f28-c375a04da21a | -18.50248 | -55.52847 | 2025-11-23 05:20:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1c6b401b-0d66-37ed-8b6a-0021f0b95d3e | -18.503 | -55.52417 | 2025-11-23 05:20:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 61068653-3ca2-3509-ab76-e7fbc084f9bd | -20.8826 | -52.32928 | 2025-11-23 05:20:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d18a9b5c-6641-3809-941c-560b6ad11dcc | -20.88296 | -52.32559 | 2025-11-23 05:20:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae36ec97-2dc2-3a51-ada5-d789f5c72e7b | -20.88739 | -52.33727 | 2025-11-23 05:20:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42b35ce0-ae78-32bc-bad3-c90f5dc9f907 | -20.88188 | -52.33681 | 2025-11-23 05:20:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba44d83e-6f07-38fc-b929-1e1a095d58e2 | -16.95775 | -56.46833 | 2025-11-23 05:20:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 21553ae3-e9dd-3616-905f-d12c161f4d33 | -20.88775 | -52.33356 | 2025-11-23 05:20:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f08024e6-3da7-3cde-91bb-3c9188720c63 | -1.74651 | -52.02383 | 2025-11-23 06:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b5b141df-5a70-3c5a-9b0c-d4dbcc694560 | -1.73629 | -52.03146 | 2025-11-23 06:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 352950fd-b8ae-3c02-b29a-4443443fa59d | -1.31132 | -53.14773 | 2025-11-23 06:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5d0a10aa-2cf9-3426-9b75-791fe588c6b4 | -1.73898 | -52.0136 | 2025-11-23 06:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a3eab72a-e40b-304e-bae5-fee0b885de8c | -1.31264 | -53.13901 | 2025-11-23 06:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a360f356-894b-39a5-9274-47da4d325a58 | -0.85016 | -52.70501 | 2025-11-23 06:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 57eaaf13-1ba4-39d1-b02a-2af447adcfe7 | -1.73764 | -52.02253 | 2025-11-23 06:31:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 758db15c-70ee-3831-932f-483434f75ba8 | -4.70504 | -46.46247 | 2025-11-23 06:31:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4b7b5be2-3f20-35c1-a7dd-93da97a6c42d | -3.05857 | -45.03164 | 2025-11-23 06:31:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| e48faa8b-d756-3770-8cad-cb82844c33e0 | -2.88718 | -45.27642 | 2025-11-23 06:31:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 15976ef3-761c-334e-bd61-e9a3fdf0419c | -0.85892 | -52.70628 | 2025-11-23 06:31:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7b4d2a35-b883-34c3-bee6-543fb8553948 | -20.87766 | -52.32738 | 2025-11-23 06:37:00 | AQUA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 14.2 |


[Clique aqui para ver as próximas entradas](README12.md)
