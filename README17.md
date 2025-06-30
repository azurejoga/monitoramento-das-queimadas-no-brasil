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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dabdfc50-50b1-3639-bf70-5cb7813668a5 | -9.23521 | -58.74679 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3ea7709-03da-3fd9-99de-c09568d131b7 | -9.53201 | -63.57494 | 2025-06-30 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| abf6978e-2217-3021-ad67-e0fe09897acb | -9.23582 | -58.74422 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e341c28e-587b-3986-8b87-900772b36b43 | -10.30006 | -57.05061 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee9a0f93-8216-3a9f-94f8-044333319401 | -9.11195 | -59.04845 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 783916d2-2de3-3db3-9c5f-91b9c1579df3 | -9.7126 | -56.18291 | 2025-06-30 05:53:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3b7dd4c1-1893-372c-b820-573a18ed9b0b | -8.72581 | -64.16266 | 2025-06-30 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ce8fd54-2bad-3895-9a2d-3b4a2f0fed98 | -9.23429 | -58.75644 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab65bb6c-a17a-3849-a0a9-764cd88ccd8d | -9.23414 | -58.75491 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cef83e3d-29e2-3e16-a384-16166d764bfd | -9.2406 | -58.7532 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb668b47-dcc6-3d14-8987-b23acf2b7a9a | -10.30091 | -57.04834 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d5fd4a0-370d-3e57-94bf-2a24ea6a8dd7 | -9.24156 | -58.74347 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5daa3f4-e614-37ab-ac2f-db0e81bcd516 | -9.23633 | -58.74009 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6182e15-1833-326e-8b77-2e82635c297f | -10.2978 | -57.12661 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 294836c9-078f-3284-922b-95f40400aff7 | -9.25734 | -58.75801 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 571e21a2-7732-36db-bffd-8e7a5cf6bd7d | -10.12712 | -57.77996 | 2025-06-30 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3ba88a5-b909-3255-8c4b-8c8f96ffa9af | -9.23959 | -58.76125 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62c4a82a-669a-3ac5-8b0d-0df3915d361d | -9.2353 | -58.74831 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d4067a6-48b3-3ee6-b97f-5d0f5bf4b1fc | -11.20212 | -55.92223 | 2025-06-30 05:53:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3de66f96-8eb5-3e37-b0f7-4e4fbde2f14c | -11.02776 | -56.268 | 2025-06-30 05:53:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e760230-5606-3492-a63a-10d7894e1959 | -9.11143 | -59.0523 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5818c42e-d50a-3443-a1e8-2b4bc388da0d | -9.24537 | -58.76216 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a6835d7-3570-35df-b68e-fe3848ce7bb9 | -9.25064 | -58.76712 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e0edd36-9839-3c25-b9c9-ccef53efb909 | -9.08538 | -59.49241 | 2025-06-30 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2071529-f664-3acc-9d04-2c287ec46366 | -10.3002 | -57.0541 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d3ffcf-79c6-3868-9530-b8cdc73c149b | -10.30073 | -57.04489 | 2025-06-30 05:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dafd6da4-1ad3-34a3-8544-69682e1d643a | -9.24101 | -58.7476 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c08564ef-fb3c-32c6-bb8c-691030e68e7a | -9.23575 | -58.74269 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a27e1a53-655e-39b3-808d-b3858f594136 | -10.12087 | -57.77916 | 2025-06-30 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a519091-cfa9-3d3b-8a71-991bf963c0fa | -9.24486 | -58.76626 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7ad2859-0a4a-328a-a031-2d3de23991d9 | -9.24211 | -58.73931 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 65673a97-c3d5-3cdc-bb96-4b82bbfaa5fe | -9.2363 | -58.73856 | 2025-06-30 05:53:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 415db080-f87d-3868-b04f-839d1d772377 | -10.12772 | -57.77496 | 2025-06-30 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fb2e077-eccc-39e8-bd1c-0f39b4f8ea64 | -11.93426 | -57.45564 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4ab1467d-8518-341a-b12e-1e135116428e | -11.94137 | -57.45105 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a763fd21-8a53-3349-8279-736f0a0b1d2f | -12.61173 | -57.87233 | 2025-06-30 05:55:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3e2ff7e-d48b-3ac7-992c-e4e1a2aade70 | -12.61312 | -57.87378 | 2025-06-30 05:55:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 031fd4fb-be50-394a-b224-15159c6c0537 | -12.61253 | -57.87924 | 2025-06-30 05:55:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4356132-ef3c-361f-a087-2903737041c9 | -11.93486 | -57.4502 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43482a4c-c586-328e-accc-6f6df200e1a2 | -11.93452 | -57.45332 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1daf1913-713b-3bbf-81ee-99ee58ed7138 | -11.93547 | -57.44473 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6024d01a-426b-377f-ac1f-5a129c2c3b99 | -11.93515 | -57.44793 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a027b7a4-838f-30fb-a0d9-9e77e847bd34 | -11.94166 | -57.44876 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2abf2647-6ca2-387f-ba90-116e3634ce9b | -12.61111 | -57.87779 | 2025-06-30 05:55:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16f24eea-e62c-3e2b-b35a-65e80788be25 | -11.94102 | -57.45416 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7be1ffd-4dac-3667-82f5-2adf99bdb339 | -12.60472 | -57.87692 | 2025-06-30 05:55:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c422816-16c3-3ed2-8317-1d455ee62c23 | -11.94197 | -57.44563 | 2025-06-30 05:55:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f39e6cf3-cb83-3876-9abc-1e0eb866a330 | -10.7859 | -44.2346 | 2025-06-30 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| ea8e4f0d-0a50-3685-8876-b177190d7d14 | -10.8046 | -44.2553 | 2025-06-30 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| c7914009-1d25-34a6-bde5-1f7c07c12f23 | -10.805 | -44.2319 | 2025-06-30 06:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 623b268f-b5ec-3618-b52c-d157b22d2561 | -10.8046 | -44.2553 | 2025-06-30 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 8eb91b92-3441-3c27-a494-4127fca199e5 | -10.7859 | -44.2346 | 2025-06-30 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 1df854cb-7368-3e30-8134-afdf1b8c0463 | -10.805 | -44.2319 | 2025-06-30 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 238.6 |
| caea2d6f-e0f2-3eaf-9129-7719f00d27d0 | -10.805 | -44.2319 | 2025-06-30 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| a4cdfbc3-7e71-3802-8e2e-1cce583cdcfc | -10.8046 | -44.2553 | 2025-06-30 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3ba45cb2-6ba1-33d7-8d1a-44bd228bb03e | -10.7859 | -44.2346 | 2025-06-30 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 4ff2bb54-8e9c-316c-b82f-542e0cc05dd7 | -10.7855 | -44.2579 | 2025-06-30 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| c0d6b338-5831-33c2-b5ee-091f461f8eea | -10.7859 | -44.2346 | 2025-06-30 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 0b67d676-364a-3265-b2e0-d8f27611a299 | -10.8046 | -44.2553 | 2025-06-30 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 58166f79-fc52-3447-9e91-6fdcf82a8e47 | -10.805 | -44.2319 | 2025-06-30 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 2c9a51a2-5068-38fd-a5f6-2bca7bc09921 | -10.8046 | -44.2553 | 2025-06-30 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 473ce1f0-fdbf-31aa-be5a-d967080cbfbb | -10.7859 | -44.2346 | 2025-06-30 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| fedd27a1-45d0-3b58-8f5c-c4003c5b6f3b | -10.805 | -44.2319 | 2025-06-30 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 845bbf05-2876-331f-b410-a829d1c7eb0c | -10.8046 | -44.2553 | 2025-06-30 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 6893d09a-61bc-3583-a410-f17f2260f6f4 | -12.6319 | -54.2087 | 2025-06-30 06:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 828279e4-f068-38b5-a475-35989fc19df4 | -10.805 | -44.2319 | 2025-06-30 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| fdc64fb6-ff81-3ded-b6cb-5ef1c139cc2e | -10.7859 | -44.2346 | 2025-06-30 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 5c6ccf41-7670-3eb0-8fd2-effbe0b57ecc | -12.6319 | -54.2087 | 2025-06-30 07:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 427b81cb-82c4-366d-8806-84667a5877e5 | -10.805 | -44.2319 | 2025-06-30 07:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 9861bb39-69bb-3aa3-b971-e31dbe7bd65e | -10.805 | -44.2319 | 2025-06-30 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| e7337b38-54ad-3904-8541-388f17dab875 | -7.7346 | -47.6025 | 2025-06-30 11:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 9b849f20-1a96-3a1c-b558-f731f6cf2dbe | -14.2052 | -45.507 | 2025-06-30 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d2c78e3e-ad61-3785-91cc-51b82c1b7e7d | -12.5175 | -57.2231 | 2025-06-30 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| c3513c73-6cd2-3f97-b27a-91ee3c1c49d3 | -15.32805 | -42.05753 | 2025-06-30 11:30:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 5fa6ee67-b2f9-3af5-bfc3-d7e701c86b2a | -14.2052 | -45.507 | 2025-06-30 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 63d38334-da0e-3df9-86cd-c10410220f79 | -7.7346 | -47.6025 | 2025-06-30 11:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9191a6bb-32ba-3c07-b986-0c917d481cd9 | -8.5722 | -51.5761 | 2025-06-30 11:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 01c0a4f6-cb87-31c4-bb99-0e614a1b320f | -7.7346 | -47.6025 | 2025-06-30 11:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 5dbaed7b-73d6-346f-8c6c-9df9bbd68618 | -14.2052 | -45.507 | 2025-06-30 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 2667964b-d660-348d-bb18-c66aabd3f449 | -8.5722 | -51.5761 | 2025-06-30 11:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 142.2 |
| 061889ef-929b-3e83-be57-32469560419b | -7.8711 | -47.128 | 2025-06-30 12:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 633186c5-ed1f-3761-be79-a849ce0dce58 | -12.5365 | -57.2215 | 2025-06-30 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.8 |
| d958f286-f94d-3853-a114-b51b5a780538 | -12.5175 | -57.2231 | 2025-06-30 12:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 513d9f23-b563-3cca-bb1b-f2aa0800cab7 | -14.2052 | -45.507 | 2025-06-30 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| a243cf0c-3ca5-32b4-8ae9-32a953d70854 | -7.7346 | -47.6025 | 2025-06-30 12:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 8e43cd41-abd2-3b1d-8751-e86cc858db7e | -8.5722 | -51.5761 | 2025-06-30 12:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 8174f078-c967-3842-9104-a5086349ec12 | -14.2247 | -45.5036 | 2025-06-30 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| b96af90f-aba7-3138-8ca3-6c87c04cbf4f | -8.5722 | -51.5761 | 2025-06-30 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 187.7 |
| 8dcf0227-2076-3c86-aeca-cf48ebba3949 | -12.5175 | -57.2231 | 2025-06-30 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 16bf2dbd-e346-3364-b819-ded6f856e287 | -14.2247 | -45.5036 | 2025-06-30 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 3c9720b2-c3c1-3087-bf7a-1cce2572a012 | -14.2052 | -45.507 | 2025-06-30 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 023d4077-203e-3f66-b485-cd4cc4f3539a | -12.5365 | -57.2215 | 2025-06-30 12:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 82b349b8-dba9-3bdf-9f81-3d7733f26524 | -7.7346 | -47.6025 | 2025-06-30 12:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 91f2d3ac-ea71-3692-acb5-f9b027907392 | -14.2242 | -45.5269 | 2025-06-30 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 7f0276e4-30b0-31da-8b63-6d99f2036682 | -8.5535 | -51.5776 | 2025-06-30 12:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| ee5a4ac5-f0e8-3a89-8b97-f2d5119c8b59 | -8.5535 | -51.5776 | 2025-06-30 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 162ccd9e-6ccb-325c-beb4-f3792fd10c50 | -14.2052 | -45.507 | 2025-06-30 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.7 |
| e7ecb3a0-7c25-3fcb-9d92-b10fb66ecfe9 | -12.5175 | -57.2231 | 2025-06-30 12:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 68fa31d8-4920-3ffb-8b7c-5e21824afb03 | -8.5722 | -51.5761 | 2025-06-30 12:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 144.0 |
| fb8e6bd0-a00c-3aed-893b-40871128cb51 | -7.7346 | -47.6025 | 2025-06-30 12:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |


[Clique aqui para ver as próximas entradas](README18.md)
