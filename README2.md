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
| c08456b7-9df9-30dc-8e63-bcca11be9215 | -6.95859 | -42.90913 | 2025-06-05 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 2f47de25-501b-3658-89d2-a96458084f64 | -8.72478 | -47.9821 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 91e2cd74-382e-34d8-8668-e87e5dc2866a | -10.81258 | -56.94614 | 2025-06-05 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 4af2d65d-6977-3e95-9778-20859a1253fe | -9.2209 | -48.84929 | 2025-06-05 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c2bde91b-c094-3b44-b719-f8c939e7a35d | -11.54097 | -56.46235 | 2025-06-05 00:39:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 32dc4294-d32e-3343-9d7f-f71fd9a330e5 | -5.64274 | -43.58419 | 2025-06-05 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 88b3c909-44fd-3668-a846-bd813877f73d | -7.61701 | -45.75525 | 2025-06-05 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| bb0dc74c-3af6-37e4-8a8f-c882126f5a37 | -8.74095 | -48.03405 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1f462b12-0964-35f5-9a34-0db7409a0535 | -6.21685 | -44.50703 | 2025-06-05 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 60ceb4bd-7736-3440-9819-89e745da469b | -10.85452 | -46.85738 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 95e2421d-8d30-34bd-b653-0fb470939d59 | -6.20542 | -48.55631 | 2025-06-05 00:39:00 | TERRA_M-M | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4b8692a6-0620-3083-947f-bf2eaecc12ba | -7.88049 | -45.99437 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2cc4caf9-dee3-38af-88e2-da63f4aa487e | -6.97639 | -47.08748 | 2025-06-05 00:39:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e9432739-ff9c-3d9e-8953-a9fd79b8167d | -7.53479 | -45.82541 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a1143ac6-7f5a-3c31-8195-f8d6be33d359 | -7.01777 | -44.59565 | 2025-06-05 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8a9468c1-be69-3d1a-8935-5c07c5b00559 | -8.69576 | -48.30922 | 2025-06-05 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 41e1fe30-3438-30a5-8e80-e51c271f3a90 | -9.38119 | -48.40696 | 2025-06-05 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dc0b3382-6281-3ba9-8350-fe688b2c83a4 | -10.85199 | -46.83942 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.6 |
| ae6ba0fb-6160-3acb-9f45-daabd9ce42ea | -8.94226 | -47.29855 | 2025-06-05 00:39:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5c85006f-dca1-3138-a38b-2df605077044 | -6.59763 | -43.89288 | 2025-06-05 00:39:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 92111f3b-13a2-31eb-8d9c-1635b96ba099 | -7.55501 | -45.83285 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2a8e5deb-3fc1-3ba8-a81c-4797a467865c | -9.35716 | -47.69457 | 2025-06-05 00:39:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6159683c-d67e-3d40-8054-c7a371a462e9 | -11.21612 | -48.62384 | 2025-06-05 00:39:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bc7148bd-fdc2-3ae0-a164-266482e71146 | -11.53734 | -56.42926 | 2025-06-05 00:39:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 9e06838b-d89a-3952-b1dc-b24e43643dde | -7.69347 | -45.77972 | 2025-06-05 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d5aaa927-7a4c-3ae3-a1ed-87434c7a7e2d | -10.81659 | -56.98153 | 2025-06-05 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 0ab5f6b0-56e0-334d-82e2-b76864a03927 | -7.54418 | -45.82404 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3e8bd771-4f38-392f-9367-206083556617 | -7.90569 | -50.35312 | 2025-06-05 00:39:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 34936be7-4120-35b1-9a52-ec747b6b82d2 | -11.43065 | -45.10225 | 2025-06-05 00:39:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 803d73d5-6ed0-3977-bcad-b03984a282a1 | -7.70286 | -45.77834 | 2025-06-05 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 0e865081-0848-3a9e-99cf-58e79b538e15 | -9.39006 | -48.4057 | 2025-06-05 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d779d0d9-6471-377e-853a-87c6ca1f812c | -7.61555 | -45.7451 | 2025-06-05 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ff8d9133-14a3-3cb0-a762-582898b28f1b | -8.96165 | -47.97213 | 2025-06-05 00:39:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 34.1 |
| e69035df-c50b-3e53-8d5a-ef1a9bdf8060 | -6.98534 | -47.08619 | 2025-06-05 00:39:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 5fc00029-02cb-38d1-8d2c-f3c95feaf4c8 | -7.58473 | -45.86328 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 306d0e59-9f51-3a2f-9f1d-05d40402d80e | -4.81254 | -45.26569 | 2025-06-05 00:39:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b19d1f63-655a-3689-8942-6a7e4bcdc0ca | -4.81118 | -45.26003 | 2025-06-05 00:39:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| be58a548-badd-3ad6-8e75-48846bb5c727 | -8.44974 | -46.48603 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8358dd74-b647-3d59-bd41-fbc7e0986e9b | -10.65113 | -49.43219 | 2025-06-05 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 913e6681-7860-38a4-840c-2a3a619ae828 | -6.96614 | -42.90159 | 2025-06-05 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 870ed6bf-f3ec-3d44-a029-6222866a02a0 | -10.67385 | -44.37914 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 8b76e2b0-6d80-342e-9417-9ce63daea1d9 | -10.85072 | -46.83044 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fc5bd9d8-f425-3e9a-8f43-66a1664d08f6 | -9.22214 | -48.85847 | 2025-06-05 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 1893660e-2bf4-37d7-becc-a020ea57933d | -7.53625 | -45.83557 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 93e0f400-f80c-398e-918c-25b395331e5c | -8.95743 | -47.27813 | 2025-06-05 00:39:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 86678b50-c513-3596-8a2a-7a5cadd7bbcc | -11.83569 | -51.28892 | 2025-06-05 00:39:00 | TERRA_M-M | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 768d236e-a0d1-31a4-a462-1a238f325ed1 | -6.95699 | -42.91951 | 2025-06-05 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 156e41c7-00b6-3130-a552-758d6c52d671 | -4.42078 | -47.66328 | 2025-06-05 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9551ba1c-77e7-3533-ab93-81fe4bc15bb4 | -8.07866 | -46.99325 | 2025-06-05 00:39:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e108d739-85ac-31f9-b824-a3a22bc93bf6 | -9.22338 | -48.86766 | 2025-06-05 00:39:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d5f7d1c2-53b7-3c57-9ce7-1e5ad15546da | -8.72601 | -47.99097 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ff04d96c-f9bf-332f-a13a-f554bddb5eb6 | -10.50422 | -53.67258 | 2025-06-05 00:39:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 1a99c0ed-721d-3d24-a02e-9847ee28947c | -8.94985 | -47.28835 | 2025-06-05 00:39:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e24d470f-4958-3250-ae6c-3ced7b24fabc | -7.19904 | -43.14223 | 2025-06-05 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| b4fb1e1f-b7ce-358c-89e5-3b8d5171811d | -6.47105 | -48.02403 | 2025-06-05 00:39:00 | TERRA_M-M | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 694fa8aa-26be-307a-ab08-b44372c91007 | -6.63359 | -47.33737 | 2025-06-05 00:39:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2ea3590f-8f7c-39e1-a310-e6999961c197 | -10.65243 | -49.44213 | 2025-06-05 00:39:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.8 |
| b4f86997-09d5-337e-bd14-9db33fbf68a8 | -10.82322 | -56.97431 | 2025-06-05 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| e029aaa8-c7b4-345c-8c79-885092a4a83e | -6.98661 | -47.0953 | 2025-06-05 00:39:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1f5d61c5-a11b-3cd7-80f3-9c553e46cdfc | -8.69453 | -48.3003 | 2025-06-05 00:39:00 | TERRA_M-M | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 322f01af-bd79-31bd-a517-dcf73d168e53 | -8.73482 | -47.9897 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bca63e2c-62e9-3abd-8baa-e71908d95a2d | -8.45877 | -46.4847 | 2025-06-05 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c63f6135-2960-34a9-a39b-f1156d587b21 | -10.85326 | -46.8484 | 2025-06-05 00:39:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| e4d5b802-88c2-39d7-b086-e69c8d9b1728 | -9.82086 | -48.04231 | 2025-06-05 00:39:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7a0cf728-8731-3bbc-9a6f-be5a3a545b2d | -7.62643 | -45.75393 | 2025-06-05 00:39:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9d18b4f8-03c1-3094-8444-e02310893000 | -10.6766 | -44.38386 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bdbb55d6-0bca-3c3f-b9fc-e08f10ccc38c | -10.6749 | -44.37264 | 2025-06-05 00:39:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| d051d45e-b0b0-3215-8f9c-f0bd7d2208eb | -7.06543 | -44.34825 | 2025-06-05 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3763091d-58cb-3c3c-80f8-d0ef606ac296 | -10.8389 | -46.8537 | 2025-06-05 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 66b13870-0520-37bb-bec8-abddcd0cbd10 | -7.8929 | -50.368 | 2025-06-05 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 30afd5a8-ec82-3bc1-89f3-f140864f6c3b | -10.858 | -46.8513 | 2025-06-05 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 7ae31143-5d95-3b1e-98ea-0f254faf5799 | -18.8479 | -53.6251 | 2025-06-05 00:40:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 29820e72-1cdc-32a3-ad44-37691c6332c6 | -7.9118 | -50.3454 | 2025-06-05 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 111a2deb-39a0-308f-a375-f4e481a4acd3 | -11.5428 | -56.4237 | 2025-06-05 00:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| c9cba8a4-181c-3bd3-ad03-7ec026e7bb56 | -11.5426 | -56.4438 | 2025-06-05 00:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 7ebb3c5f-1987-3afd-9fa3-24260fe7e2be | -7.9116 | -50.3666 | 2025-06-05 00:40:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| e7cffa53-133e-3692-a1ca-65e4c4fa6cc6 | -7.9118 | -50.3454 | 2025-06-05 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3ffe4393-54ab-39d9-9449-929d7e240506 | -10.8389 | -46.8537 | 2025-06-05 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 98f7880e-1f01-3810-97fb-8b3b5710bbd7 | -18.8484 | -53.6035 | 2025-06-05 00:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fc6fb365-63d7-31a2-8aa0-593ca07fe0a7 | -7.8929 | -50.368 | 2025-06-05 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1ccccaff-958a-3c58-b6e3-3219f6e29c70 | -11.5426 | -56.4438 | 2025-06-05 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 1cafe99a-f225-3d57-912d-35848bbe3c04 | -7.9116 | -50.3666 | 2025-06-05 00:50:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| f5010ccf-b1dc-382f-9459-ff478da92990 | -18.8479 | -53.6251 | 2025-06-05 00:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 52f7c96a-7ec2-31e1-926b-581851b22357 | -10.858 | -46.8513 | 2025-06-05 00:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| fddf4247-3d09-3c03-8af2-4508a11dee41 | -18.8279 | -53.6283 | 2025-06-05 00:50:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 2abd8a0c-c3c4-3708-9375-36f998ba06f6 | -11.5428 | -56.4237 | 2025-06-05 00:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 18f77460-5898-3eb6-bfcd-64e10b96ceaf | -7.9118 | -50.3454 | 2025-06-05 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 311603a9-c020-3298-a6ea-1cf2ea07a6e9 | -7.8929 | -50.368 | 2025-06-05 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 1436d1b7-4703-328a-94a2-8c8b79b173de | -11.5428 | -56.4237 | 2025-06-05 01:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 715d8242-f134-3d9f-88d0-d429d27ffdd3 | -7.9116 | -50.3666 | 2025-06-05 01:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 7ea653ac-a568-3b32-a713-8d9fec7ac1fe | -18.8479 | -53.6251 | 2025-06-05 01:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 963e6c29-cb2a-3f8b-b6f7-729df3ba1e3c | -11.5426 | -56.4438 | 2025-06-05 01:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8054dbe5-ec8e-3d1e-b58b-8fab3405041a | -11.5428 | -56.4237 | 2025-06-05 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a058f595-c39f-3fb4-af3e-e0e6bc3328c1 | -11.5426 | -56.4438 | 2025-06-05 01:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e1ae3b0a-1b96-30a6-adeb-16d4355b4ce9 | -7.9118 | -50.3454 | 2025-06-05 01:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 5d4ade45-19bb-3674-a6a5-6b7dd5ac49ee | -18.8479 | -53.6251 | 2025-06-05 01:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 60d0855d-ee4e-3781-9ad7-28da35c698b4 | -7.9116 | -50.3666 | 2025-06-05 01:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 95974573-b4cf-3465-b5f2-7a54d27ec379 | -10.8576 | -46.8737 | 2025-06-05 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 32d88c1f-37d6-3c3c-8e62-b612f4190af2 | -7.9116 | -50.3666 | 2025-06-05 01:20:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 1d636eb0-5064-3b74-8122-ae70512f03d0 | -11.5426 | -56.4438 | 2025-06-05 01:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |


[Clique aqui para ver as próximas entradas](README3.md)
