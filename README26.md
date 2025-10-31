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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d45a4e8b-f12e-36be-bcf1-e56f40c85345 | -14.23764 | -47.31049 | 2025-10-31 04:08:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d705d51-0aa6-368e-83ea-848dae79f313 | -8.08814 | -45.13221 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 12bfd5f5-b155-33e4-85a2-8a8f59e844a8 | -9.85836 | -44.84678 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a26b9fc9-dead-31a9-a541-2fae080a9b54 | -10.84223 | -44.92802 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c38c51ac-7ce7-30d4-a89e-3c02ade8d5df | -13.48639 | -44.09093 | 2025-10-31 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b51c0a7-ee17-3357-aca6-4f22057c957c | -9.72841 | -48.02185 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0060e72-54a0-36c8-91b8-dc25d04aefb1 | -8.08237 | -45.14446 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c576c9f3-e3b4-3013-92cb-033346d0df55 | -12.06246 | -47.34107 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cbeb17b5-eb75-349f-ba0b-ae5395c422a9 | -7.64838 | -43.582 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b61c3e1-0d9a-3717-81fe-15fc79c88444 | -9.85787 | -44.87132 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e7163d0-09bf-3780-95d1-e9d4f80d53f3 | -9.32009 | -43.09379 | 2025-10-31 04:08:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ca5243e-cec4-3986-95fd-f5bd00890a6d | -8.08671 | -45.14079 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b918929d-16c3-3f88-8785-98ce577129d9 | -10.0853 | -44.89935 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afcf5b82-798c-393c-ae77-4e5461598d4e | -11.81888 | -47.23317 | 2025-10-31 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17a66e67-e92d-3b67-bc40-a8946eeca94a | -10.64455 | -45.24466 | 2025-10-31 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82fb2976-aa53-30de-a46c-ddc51f43648c | -13.43118 | -47.35851 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9edd32c9-5b23-3fca-a570-622f55e2082d | -8.16567 | -45.5004 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dea5ddf5-7178-3d8e-8588-92d54a4ab51b | -12.15349 | -45.21873 | 2025-10-31 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc779ec3-2d46-3ef7-90b8-816790f4112f | -7.66117 | -43.59153 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 7a3b005d-1e23-3ab0-85a1-6d6f4a91edcb | -12.54129 | -47.0481 | 2025-10-31 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1a0c5bc-fa60-389e-946a-5add84fb9b4f | -9.43384 | -43.60932 | 2025-10-31 04:08:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fa3d03c6-b83a-30f8-a3ee-29c9a8770099 | -8.18516 | -45.69101 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2452d91-7011-313e-9337-e2ab8deac43d | -12.52714 | -47.53991 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9149f94b-26d7-33f9-89f0-4ecfce57e675 | -9.36077 | -40.69534 | 2025-10-31 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 374a6109-eb20-3902-9c62-579111338563 | -12.82845 | -43.49061 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95a107b2-295c-3b0c-88dc-7a5da6075669 | -11.87807 | -45.32864 | 2025-10-31 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f0fa588-25cd-302c-8b5e-1803cfe39338 | -12.28125 | -48.06736 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 748fb97e-a41d-31f1-8c3d-7c8dc0a27d2e | -11.5599 | -47.08021 | 2025-10-31 04:08:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 5af3f5c4-d896-3073-847b-40b9a1544d8e | -8.10328 | -46.75456 | 2025-10-31 04:08:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b3ee242-520b-3c08-a261-f911a460c3b8 | -11.71744 | -43.91256 | 2025-10-31 04:08:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d02df7-0be2-3700-a758-9c9a80b23d54 | -8.09398 | -45.14198 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a8d81d6-b26e-3d5b-9434-3f0e295b9e95 | -14.00159 | -44.01482 | 2025-10-31 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b1df25f-4331-3b6d-a7b2-5cf8ccf49cc3 | -8.47204 | -45.7817 | 2025-10-31 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddf23cc5-6a64-3d85-85d2-911061d8c958 | -10.92991 | -44.16526 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 11ede92b-8ab7-3753-9673-73cba0dc3cb6 | -9.27968 | -47.6569 | 2025-10-31 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d05b353b-86be-3231-ada3-1c84c201392a | -10.88476 | -44.35312 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a79c82b3-2a83-3359-897b-f360fdae43d8 | -8.15609 | -45.46666 | 2025-10-31 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c11dfb5-a66b-3d66-b2e8-33b800f1ba46 | -8.09469 | -45.1377 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63daa339-895c-32ad-a4c6-22f628826042 | -11.02375 | -44.34123 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94605ea7-766b-3c1f-9f2f-7c546256467e | -9.20039 | -46.32274 | 2025-10-31 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47ae7d19-45ef-3b2c-9c46-afaa54632fc4 | -10.75134 | -44.64955 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90aaa77f-7a59-3091-8923-fa021553e42e | -8.086 | -45.14508 | 2025-10-31 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f43e249b-bef9-38fe-8f8b-5084ef4aa40e | -7.61277 | -46.47132 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b2e94109-cb7f-3975-9303-8bf051c73ecd | -13.80894 | -47.06734 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3b0a13f-7351-3bd8-b5a8-a0b28286353f | -10.74291 | -44.63631 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c8686b7-65b5-3430-85c6-ba0c00769914 | -7.64376 | -43.58899 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 850fadd2-24d1-3463-97ec-6f080b723ac9 | -9.97991 | -45.16313 | 2025-10-31 04:08:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| baacfc6e-8dcf-3f50-a1a6-331c3d983806 | -14.21281 | -44.39173 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ceb3a84-f39a-3491-90cd-29dcc9e468e5 | -10.53465 | -44.92295 | 2025-10-31 04:08:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26b0cf20-0e28-3cf0-a68b-71b9dd2b8dae | -12.04903 | -43.54022 | 2025-10-31 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea8b0928-3df7-3d08-80dc-e17a2f27d052 | -10.50651 | -42.4084 | 2025-10-31 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2700aceb-b865-3f06-9770-dbca139816b6 | -13.52514 | -44.30949 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb041059-b44e-32ab-84c7-743cfad7660b | -10.53307 | -53.71298 | 2025-10-31 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e52f447-efda-34bd-92dc-60e0fe6cef9e | -10.27625 | -44.55355 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4a3c2bce-a522-387c-b170-e385f2355b6f | -12.8418 | -43.471 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fcbb83fc-ddbe-3ac7-8ed4-5314812e6eca | -7.61948 | -43.63109 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54a75f2e-1f96-3a72-ab03-7490ca753508 | -13.1138 | -47.75821 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a4113330-0dcb-3b23-be14-57a94c06d25f | -9.73614 | -48.02736 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 286d19b1-6936-318e-a114-b3ebdef3983a | -7.76971 | -46.47341 | 2025-10-31 04:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4c70e4c-99a5-37aa-89d4-9f88258c0b55 | -9.51754 | -47.20234 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e41e7e67-ebba-3dcf-a865-fb68624660ca | -11.12064 | -54.64602 | 2025-10-31 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ebf04f57-8c5c-3e9b-83f6-8ad2adf7502f | -9.84017 | -44.15243 | 2025-10-31 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 79999b39-0488-3d22-a02f-47c35bd7a010 | -11.94153 | -43.27878 | 2025-10-31 04:08:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47aee43d-3eaa-3034-9d1e-3277aadd3f38 | -12.23485 | -47.25082 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18fce8a1-8032-316c-8d75-d6e83ee58973 | -11.35173 | -42.26169 | 2025-10-31 04:08:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fc29414c-3f83-3648-8331-7474006185e8 | -8.89952 | -37.9671 | 2025-10-31 04:08:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8db47717-286d-3a71-b36e-e00ec1617b31 | -14.08114 | -44.15755 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c3f6fd0-dc13-3a20-b91c-04fc7582f3da | -7.64215 | -43.57725 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 277e79fb-64de-3fa6-8e95-0af911532eac | -9.85921 | -44.86331 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fd95377-064b-392d-add0-0b0614fdd9ed | -9.86121 | -44.85131 | 2025-10-31 04:08:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fa9206b7-d125-3264-963d-f47cfa26b2fe | -7.55798 | -47.4137 | 2025-10-31 04:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e403428-072e-3dae-9cd3-c8c2d12583cd | -11.69496 | -46.70644 | 2025-10-31 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2eda96a-4d2a-3ea3-b83d-9410ba29d8c1 | -7.64941 | -43.59742 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ca897c8d-bae3-3412-ad6d-1af3f3c524d9 | -12.06158 | -47.34611 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1c1ec7f-cabc-3ad9-a8f4-622ff37b0798 | -11.35781 | -42.28781 | 2025-10-31 04:08:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66cabb3e-c4ac-32ef-a7ec-e34544bdb09d | -11.12638 | -45.16069 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7907b1f-02aa-3a47-886f-cf37d280c7fc | -13.67986 | -44.71284 | 2025-10-31 04:08:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 314716a0-4273-3b17-ab1b-9184a551f526 | -9.73193 | -48.02654 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24afa1df-a8c6-3d6b-99ec-96056e1288bd | -10.09768 | -36.19837 | 2025-10-31 04:08:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| c2f806af-5ef7-3597-9cc4-2ea542e08157 | -12.93463 | -47.92449 | 2025-10-31 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7ab4e22-c5f4-39b1-94d2-64613d5a6da8 | -10.74821 | -44.73232 | 2025-10-31 04:08:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9725a0f0-9188-3a89-9325-5f8929481758 | -13.33916 | -47.64531 | 2025-10-31 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bc03996c-8ae2-3a6e-be73-f06543c424b2 | -8.55052 | -47.77777 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7032fd10-9594-3bf4-8fb3-83eec0f3ed84 | -12.11463 | -47.11089 | 2025-10-31 04:08:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caaa40f5-18ad-3d1a-906d-c6865342cad9 | -8.0268 | -42.50948 | 2025-10-31 04:08:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c74d7a8a-813a-34ff-96e4-5d929cb8da3d | -13.81406 | -47.0663 | 2025-10-31 04:08:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf709c9d-d8dd-33a0-99c4-3108cab93844 | -13.04373 | -43.37691 | 2025-10-31 04:08:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff37dfe6-c1fe-3002-8d41-9cb3098a985f | -12.80582 | -43.48321 | 2025-10-31 04:08:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d843a9c-0e18-3563-9c70-7d1b953af878 | -8.32114 | -47.92756 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 354edfac-52a3-389b-860b-3787fd9d97af | -11.12989 | -45.1613 | 2025-10-31 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5174fe18-a8a2-33d8-9ecc-fcd787873986 | -7.66797 | -43.59279 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 906f528c-554a-337a-b578-fd76252105bd | -7.33801 | -47.63113 | 2025-10-31 04:08:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00aa345f-3d5d-32e3-876e-11f6fd8c2317 | -8.3314 | -47.93235 | 2025-10-31 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24d1aeef-521f-3ab8-82a4-20492302bdb4 | -9.7362 | -48.02789 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17ccadc4-0002-3dbc-a0fa-f660b1996984 | -10.248 | -44.55264 | 2025-10-31 04:08:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5d6787f-e035-3725-8cdc-16528bed9a80 | -14.13026 | -44.18825 | 2025-10-31 04:08:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92202852-8b3a-3540-91d8-173a244ce2a1 | -7.64436 | -43.58525 | 2025-10-31 04:08:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 939f4fca-7fbb-356d-8eca-6ae3a1d07a2d | -10.75921 | -44.1979 | 2025-10-31 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9396368c-b180-3786-85fd-a18eec2ad177 | -9.92198 | -47.18674 | 2025-10-31 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a946fadf-7587-3e6e-b1dd-0ad03919d807 | -9.72701 | -48.0297 | 2025-10-31 04:08:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
