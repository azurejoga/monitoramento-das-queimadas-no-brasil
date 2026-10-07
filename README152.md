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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00f0fb87-e46a-38e0-8bb2-43ae2642e981 | -12.84301 | -44.62823 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 18f678c2-72dc-39b2-b303-0a1c46b21179 | -10.13145 | -46.00353 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 813f140b-156e-33bc-847d-7b316a271f1a | -11.08417 | -41.77149 | 2026-10-07 16:01:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| af1a1dc0-d65b-324c-b6e0-be8778f71bf8 | -11.84437 | -47.3796 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 38c7183c-363a-39b5-85d2-743a8cfb2449 | -8.9565 | -47.55638 | 2026-10-07 16:01:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d170f02f-2110-3bee-8852-33156435d983 | -8.43123 | -35.39814 | 2026-10-07 16:01:00 | NOAA-21 | RIBEIRÃO | PERNAMBUCO | Brasil | 2611804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 3bc8dc8b-6a77-3923-b02c-1bd8c99b4284 | -8.91528 | -44.55012 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eced91f7-c557-36cf-8dd1-716d6b6c2b13 | -13.65207 | -44.7909 | 2026-10-07 16:01:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d1392893-8b6c-322e-a830-de226ca1f7e3 | -11.08842 | -47.62332 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| c9b96960-6d51-30cb-ae32-0fed83238eb6 | -12.32351 | -47.94988 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 32fd5151-d87e-332a-b244-f87f59182203 | -8.6455 | -44.87041 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| d4b34ca3-f355-36a4-a2c7-f6a7f97a54f7 | -13.33525 | -38.98 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 63396453-d739-3256-918e-742c0e2ad8c9 | -12.22326 | -44.71365 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 293.6 |
| 1cb7429b-e55f-3ab2-9bee-2de05542d94e | -12.18267 | -44.74656 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 87e9d86b-b410-393d-940a-38d933a76419 | -11.09301 | -47.61877 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 89413d9d-6dce-3e62-b3b0-67c7d98d51a3 | -11.22695 | -46.2397 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| be2330a8-252c-3a06-9d65-d25f063dc2e7 | -9.87711 | -44.80214 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fabbc58b-f20a-3091-a520-9ec4dd25174b | -10.85405 | -50.68881 | 2026-10-07 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| cbb23c57-426e-3647-8d28-d677b1927fd0 | -9.16172 | -45.82086 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36ca5272-f03e-3e83-a299-17a977273084 | -8.3223 | -44.15195 | 2026-10-07 16:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 1671be32-5d1b-3f0b-aaa9-ead0b003e749 | -8.98884 | -45.94049 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d1c75823-a639-366f-a81d-bef1b0bb753f | -12.19507 | -44.64953 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 9047c732-9a8e-301a-86a1-784ccb74ea58 | -11.05923 | -45.84995 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fb695355-d8cf-398b-8d06-0d5a559f5b5e | -14.34532 | -48.80481 | 2026-10-07 16:01:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d935371c-2d99-39ef-b689-c0b9205b682e | -11.84878 | -43.56485 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 05cba731-7e4a-3ee2-8f8c-630f7b845aa7 | -13.39439 | -43.87182 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6b3b8e7f-520e-352a-b6b5-eddde71f1394 | -8.28118 | -36.06827 | 2026-10-07 16:01:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f2a443ad-2392-30b6-b73d-1ca9e2065f8e | -11.04393 | -45.81322 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0bded960-6d80-3f9c-9f9e-ea5d896d0717 | -10.57351 | -47.2874 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9b56274f-56e4-3938-8031-3eeaa43e1abb | -9.90677 | -44.80151 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| f578a7c6-579f-3f5a-9a00-40e83f78c334 | -10.97527 | -45.40067 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 97eb7a42-26f3-335b-bfc4-61ce37571fc9 | -9.96644 | -43.56659 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 36.4 |
| 8d642dab-3c23-3ccf-88cd-8087c9c667ff | -13.21603 | -39.13126 | 2026-10-07 16:01:00 | NOAA-21 | JAGUARIPE | BAHIA | Brasil | 2917805 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2ca82150-b487-3812-ba6d-777ee876b3fd | -13.33581 | -38.98397 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| cda37015-791a-31db-abb8-77837a203e72 | -9.39461 | -46.84517 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c86d4ec5-a742-3994-bd36-9f5629966845 | -10.879 | -47.6064 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 18e211bd-a3b8-3699-b853-caa717ecfbab | -10.17553 | -46.71611 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cd7b8c14-f807-3066-bbcc-32d963a3b37a | -11.72949 | -43.42709 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 071812e3-7967-301e-8b63-45ffb734842c | -11.06687 | -45.77443 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e5c2cf8c-a344-3ddf-9c3c-c215c039bee0 | -8.78049 | -47.57799 | 2026-10-07 16:01:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| afb862b5-4366-3867-ac85-4f8d42e0e8e0 | -12.82058 | -44.66613 | 2026-10-07 16:01:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 3fb36ce6-54d7-3446-b358-c5b409e42a22 | -9.56239 | -46.84658 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 32d4c136-8190-3c27-b150-22715d4ed73f | -9.14849 | -45.83015 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ef7f0bd2-e196-3430-8022-a4f83ffdd3cc | -10.98692 | -45.49124 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cebd14a4-64da-3db8-85e3-8e2e94285c87 | -10.78452 | -47.17839 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dee3d807-abad-31e4-91e1-4005d84e5529 | -11.60704 | -40.06765 | 2026-10-07 16:01:00 | NOAA-21 | VÁRZEA DA ROÇA | BAHIA | Brasil | 2933059 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6bd4c8d2-da5d-31b0-baed-a6d889958ff5 | -9.82681 | -46.24809 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb767f9c-04e5-32dd-9ba7-dc6848d761b2 | -8.72184 | -46.75298 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 81f52ffc-8dcc-3160-9995-449fa4398f70 | -8.75946 | -44.16358 | 2026-10-07 16:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3a19600b-4023-3f29-96b4-b2b3848ef507 | -13.33638 | -38.98794 | 2026-10-07 16:01:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 54f1e248-196f-34f0-8baf-fc6450042da4 | -8.45037 | -46.40949 | 2026-10-07 16:01:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 57e54164-b9d9-337c-ae8a-43bbb81787d5 | -8.75884 | -44.15905 | 2026-10-07 16:01:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 45cd6347-6bdf-30d2-b5c7-9a9d0ac4a3b4 | -12.44963 | -47.80689 | 2026-10-07 16:01:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 70d25ff8-0ece-3fbf-9430-1ab51297508a | -13.37789 | -40.86568 | 2026-10-07 16:01:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 060e77bf-5d9d-38cd-9d62-151bfb02a38d | -11.09381 | -47.61893 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 06c51133-6128-32fc-b1c0-6f9b4aaae2bf | -9.91154 | -44.8009 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| a80b3152-9fb3-3809-ada3-176b487a0946 | -11.11065 | -45.70451 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| abf8e5e1-8605-3d43-8ff8-837b42904688 | -11.6189 | -43.64228 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b68078d7-f4ef-3742-9325-ca388c5a17df | -12.36701 | -38.00788 | 2026-10-07 16:01:00 | NOAA-21 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0f7cc6e3-7595-3f3e-afa3-944a41857071 | -11.10197 | -45.67729 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| ce4ef548-9024-3abc-95cb-62c39ff702ab | -9.37952 | -45.92874 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9b77bdb9-aea1-335c-9ced-e7cd32339484 | -10.7867 | -46.57007 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| b9dd46d7-fd78-3629-b7f4-f08c0973d7d2 | -8.58762 | -44.86708 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| ab85f9f5-97c5-3776-aff5-b61200861405 | -8.28175 | -36.0719 | 2026-10-07 16:01:00 | NOAA-21 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 6066963b-b41b-3ab6-97d6-84122c389ec9 | -11.23179 | -46.25032 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4ef0519b-afeb-3f8e-88e8-101cb681e2cc | -11.21909 | -46.23524 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fde1062e-82b5-322e-81b3-a01833ef5704 | -11.23424 | -44.02074 | 2026-10-07 16:01:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 7d2aae7b-e766-312b-9955-46ca1846b992 | -11.3573 | -40.0028 | 2026-10-07 16:01:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 6b0ff61d-915b-346c-a801-71d9bf520b1d | -11.38411 | -46.67884 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 186473e6-f070-38ed-827b-b986c22458c8 | -8.9939 | -45.93959 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a8268011-19c9-390a-9866-e527b5d9d0f5 | -8.39036 | -37.03048 | 2026-10-07 16:01:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 25e7770a-5b9b-3ce4-b908-e0366f66df67 | -9.62244 | -45.86909 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7a42fbc8-b94d-310c-a094-8732f0dd5764 | -10.13308 | -46.00393 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a094e790-5aa0-321c-b374-18eea726d53d | -8.65022 | -44.86992 | 2026-10-07 16:01:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f3ee555d-a16d-3dac-b00b-718cc56afb1e | -10.99978 | -45.47102 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 3633ea6e-562d-3118-bbd8-a1393b48ae53 | -9.71204 | -35.92958 | 2026-10-07 16:01:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| b07a77a4-07e5-30d2-b0ef-e101e750584e | -10.78405 | -47.17459 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 66c0be21-6091-3370-94a5-28f230d07df2 | -8.07371 | -38.2297 | 2026-10-07 16:01:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 30.2 |
| d9ddf2cb-1c60-3da2-9de6-ff2770060664 | -10.98643 | -45.40765 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 347a1495-27c9-3597-aaf1-2216687caa33 | -9.03011 | -41.4638 | 2026-10-07 16:01:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 3557f44e-0a50-3d66-ad1e-ab5732fd8880 | -11.14058 | -46.15658 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 1857eec2-11f8-3705-8fde-4bb2131aaa3b | -13.39328 | -43.48232 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 186fdef2-0961-3250-942b-dc9e8c48afa9 | -11.01627 | -45.44786 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e2db2007-7957-38b0-a321-19dc98a938fe | -13.56835 | -47.24324 | 2026-10-07 16:01:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 9e0ab394-34b2-3454-9e87-280ab24e146f | -10.77689 | -46.53568 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6955f62b-23c9-3e3a-ac18-5b0af355f66d | -12.11788 | -44.96189 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53c6dbb5-a9ac-3ce5-b5bd-33305faa199a | -12.04307 | -43.38961 | 2026-10-07 16:01:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| ca5f19fb-7ab8-3784-98eb-803149186a98 | -12.17216 | -44.74228 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 555.4 |
| 104a5711-609e-3dca-bcc1-56ba977fe2ee | -10.03739 | -36.05384 | 2026-10-07 16:01:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4abc3e37-2379-3e26-9c5f-912f39c35e31 | -11.83767 | -43.56577 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| dbd9b10c-8a58-36cf-b9ad-95f4e0f5d242 | -10.86737 | -50.68058 | 2026-10-07 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 09e85aa5-cd37-3950-a6c2-74c71f1ec4ad | -9.2609 | -45.64098 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2fa4c3f8-7337-3715-a8c9-a1d29048b610 | -11.25441 | -47.58168 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 83b2c1da-2c68-32ea-bf72-c07b4db31497 | -11.83854 | -47.38018 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9f96d279-fb13-3865-b182-7889472404cb | -13.35835 | -43.86775 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 2f7ab881-b751-3cb3-9a57-846f30d870e2 | -10.99628 | -45.4838 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 194.2 |
| ddb3256b-d63d-36f1-91c9-8201fbf7a29c | -11.7745 | -43.53753 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 796a8adc-86f4-3424-b30d-4ab6b5d1428f | -9.92241 | -46.7981 | 2026-10-07 16:01:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9751db5a-1b08-326d-a079-0b07b1b5d073 | -12.21043 | -44.66906 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 5bd33884-debb-3664-a6bc-6de269880da9 | -11.10683 | -47.63504 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |


[Clique aqui para ver as próximas entradas](README153.md)
