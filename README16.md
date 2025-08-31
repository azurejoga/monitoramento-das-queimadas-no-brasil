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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7405aabd-730b-32f0-8d6f-fc96a03d5429 | -6.19601 | -42.76321 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| feda74dd-d470-3528-ad1d-e20877a6a86e | -8.91573 | -40.43921 | 2025-08-31 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f91a3340-d1f3-373b-b8a4-87e731ca90ad | -6.22572 | -43.35854 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29bba190-2978-3caf-a850-392a36c889ae | -11.01751 | -46.87752 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7376ce22-800c-3e0b-8a2c-7a85ed7f582c | -11.02285 | -46.99687 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ec0d838-9c52-39b2-978e-17a5e8a51596 | -7.58417 | -42.70332 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cfe453ab-f195-3667-b5b7-7247ac251079 | -6.23884 | -41.80611 | 2025-08-31 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 58e74881-1613-3d13-8ab0-a4c83edf0814 | -5.80893 | -43.86135 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bfb4425-02dc-33ba-855c-a3e8d1cd8b51 | -9.69761 | -47.04364 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3570758-46b1-3f90-ae01-554c677baad4 | -5.70212 | -45.95672 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 28538863-12e3-3097-ab6f-8083c98bf570 | -6.09218 | -43.32214 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c749019c-5309-35af-82e4-296abddb9559 | -7.37396 | -43.40092 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eebe8a8a-e9c1-3b9d-a690-b42bbfa862e5 | -11.35173 | -43.62333 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8906f7c-13f9-3519-9b47-6920f5b111e7 | -10.60595 | -44.32713 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| cb9492a4-d3ab-3f5e-ac1c-9ac0ed42e12b | -6.17396 | -43.35162 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceebcb1b-5c9d-32a7-a225-cbac92a1a3ad | -7.41748 | -39.92823 | 2025-08-31 04:02:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 11dff1a9-8aee-35d1-a4f4-48e44f4cd326 | -6.16783 | -43.3204 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| bba5a541-86d0-3ea8-b767-9397c939039b | -7.64006 | -42.65679 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9dc75694-d5a0-3e28-911a-0017ac5a6333 | -6.58862 | -43.64008 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37e504c3-b990-3849-a7fc-fcba9d913d2c | -8.96593 | -50.01044 | 2025-08-31 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b66ab05e-b735-38c9-95a0-315e09216230 | -10.02242 | -48.36444 | 2025-08-31 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96eada9b-a454-34e3-b45f-a4a0710782d8 | -6.14142 | -44.13042 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3d53a25-3d5e-3ee7-87f0-5ecd09bc4836 | -5.69353 | -45.95533 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c1946c99-a25a-3aef-98ce-86b2c3da27d5 | -6.51258 | -43.13846 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd3caac0-53bf-35e8-a5e4-05fb3f5ac6f1 | -7.37755 | -43.40148 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6df2f62a-33db-3c3b-b4e6-b14dfa5a1235 | -9.03155 | -40.52498 | 2025-08-31 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ecacfdd3-3502-3064-8b36-f01c3690a879 | -11.2115 | -45.03541 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbc5fe14-06a2-335c-aece-febeeca2c005 | -7.10595 | -44.31404 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 101ffcab-d7e9-35d1-a100-b3444f888fc2 | -8.39055 | -48.27084 | 2025-08-31 04:02:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4355d88c-40e3-3ddc-9d1e-961166f77d54 | -6.28293 | -43.53629 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2c8249c-a31a-39c8-a17e-29f052b11a4a | -8.87863 | -45.10121 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc7befd6-0ff8-3684-8238-6c8a928e046e | -11.22652 | -45.0144 | 2025-08-31 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31a90137-362e-3664-81d9-d04fb9638a3f | -11.34918 | -43.6389 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 52c31d14-9630-31fc-afa1-b4a9e8ddb1f1 | -7.41074 | -42.05585 | 2025-08-31 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2b161ed6-8be3-3e36-9a7d-44e192d6adb8 | -11.32729 | -43.6635 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29eae747-cce6-3163-b355-41cd9e4e3187 | -7.12447 | -44.60019 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0727e11a-b408-3f7e-a2b2-1a3f36c27565 | -6.24444 | -41.81456 | 2025-08-31 04:02:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3998bb7f-b274-377c-be09-07d6985870bc | -7.57272 | -45.12435 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 678e9ecc-5659-321c-a357-07785e1dc7e4 | -6.9974 | -44.3602 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c18333d-76c5-3ba5-8fa2-b87aff15eca4 | -6.55174 | -43.68429 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17d9a5bd-5fd7-35b3-b691-5e69ae4e0580 | -10.02384 | -48.37294 | 2025-08-31 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 859252cc-e3a3-360b-8222-23092add5d6d | -11.41327 | -44.68457 | 2025-08-31 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 902f90fe-2ef3-3bc4-83aa-56bdbf051e18 | -7.08398 | -44.32954 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e16f9558-3d10-3e23-94fb-c7ce950b7efc | -10.60477 | -44.32755 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 634fdf18-3548-380f-b546-606b1419f475 | -5.81269 | -43.86192 | 2025-08-31 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47f1988a-165f-3be9-94ad-9b84d8a0d711 | -11.29856 | -43.64265 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b277fb2-4baf-394e-a75c-c406abd0d555 | -6.27927 | -43.53568 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 409e2703-c573-35f2-95b2-d02927bc7c4c | -6.17999 | -44.20182 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2e852f8d-40f4-33be-adf5-59e6f6358d0b | -11.35237 | -43.61941 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| feeaf288-335d-3b0f-8490-b0d3a4453f49 | -11.35521 | -43.62389 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6095677-a414-3857-bcc3-db4d82cc657e | -11.29751 | -43.67059 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e9a06e2-bc7f-3a93-84f8-d3c77d6bc9da | -6.53298 | -44.56679 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d4e3ff3-6902-381d-9e02-2314a1b939a9 | -11.29758 | -43.56243 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b133a301-8782-3ed7-b229-48c19387299f | -8.86866 | -45.74852 | 2025-08-31 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39ea6912-28fb-3bee-840b-248a3a826f5c | -7.11319 | -44.43264 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83123741-03a6-3485-b3c3-750f455831de | -5.91833 | -43.35599 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8745d020-628f-3082-bede-4ab4e81138d5 | -6.70612 | -51.42164 | 2025-08-31 04:02:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 2613cb9a-f261-3424-bb10-93252e1a70e1 | -10.42081 | -50.86165 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3f8aed8-b5bb-3e20-9a55-a2c58a48cdd4 | -10.48152 | -51.63109 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0861585b-16f0-30d2-b2d8-138c7e2406e9 | -5.48578 | -44.39645 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9188e03e-3036-3dd4-8fc0-6d890a9ca118 | -11.36187 | -43.56125 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea47e67-cae3-3ef9-a2e0-2c1e90cd1679 | -5.4772 | -44.40014 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d4e65e7e-5847-3344-b421-3098c69e3927 | -11.30105 | -43.56301 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f7464d6-b4fa-3305-a272-2dc80996b3a8 | -5.98934 | -43.3358 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df358ba9-602f-3a1e-9069-80c28ff7c4ec | -7.73237 | -50.26445 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 676873c4-3648-343f-b5c5-c010be338351 | -11.02235 | -46.87445 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 19022c9e-cd74-3d95-ba09-688ed770b363 | -6.29722 | -43.79476 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40dccbbb-8271-336a-bfd7-e9cf6e0c603a | -6.54606 | -42.75261 | 2025-08-31 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6449a33-dc7b-3ee6-8dd1-be2301266267 | -4.74129 | -44.44622 | 2025-08-31 04:02:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 17b3a63d-a45c-3cf5-a43b-8ecdd36973bb | -5.73295 | -44.11197 | 2025-08-31 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db0632df-8e57-36f0-ae74-9434fdc63b98 | -6.7813 | -42.84523 | 2025-08-31 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 378716c4-de82-3fb8-8d74-1ec075384aa0 | -11.06765 | -44.63967 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7e89f7a5-2ee2-3396-bcf4-74580695cf30 | -9.70374 | -47.04373 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddf3d46f-ffe1-37db-bb54-c11d5ce267ad | -11.00167 | -46.94376 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf4b44cf-4100-3bd8-9882-0462ee85d46b | -11.35393 | -43.63171 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e2b157d7-cb90-3ce4-b8fd-81e9276e2a73 | -6.19796 | -42.7513 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9b52400-9398-328f-9c49-2b28c5dcf176 | -6.44318 | -42.39417 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 85ca0045-5b19-31a9-b6e8-7951cddef2d3 | -6.57086 | -42.55586 | 2025-08-31 04:02:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2adff266-dc79-3909-a260-b5eb867dac1d | -10.03179 | -48.08237 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a1fa1b8-977b-3dc3-bfc4-a792379c0328 | -9.47342 | -47.60653 | 2025-08-31 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cb292b4a-9058-3bca-b12f-37db331ff759 | -9.03486 | -40.52551 | 2025-08-31 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 218e7532-eaee-3d25-80f5-7dfe0b478dcc | -6.17193 | -44.13333 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53b82ba1-e2f1-3893-a207-378a6d4f5965 | -6.37502 | -43.54734 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f11c8302-5b29-313f-afe7-2f6d895cd6e2 | -9.24985 | -47.06919 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 193c27f6-4e99-3956-b1c8-bfb94388b93d | -5.4811 | -44.40074 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 18279028-0d2c-3edf-8678-655dff2cdaad | -9.95806 | -46.34563 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0087df7f-f03a-3515-853d-8fbb94f4c516 | -6.53948 | -42.97206 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90a7d386-0319-3e3e-b8be-5f90aa8d6d81 | -7.40445 | -44.08618 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3fde2f02-6351-3e62-896c-dfeb6d575a4e | -8.33088 | -47.42319 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 672bc564-e7dc-335b-958c-059ac0c4d974 | -6.20436 | -42.75639 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7a185ac3-7ae3-304d-a9b8-fe59474d584a | -8.85044 | -45.73417 | 2025-08-31 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 551b268a-2a5d-3bce-ba1e-15812afe0767 | -7.08098 | -44.32416 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54e20d84-220f-39ba-af17-3556e60322ad | -10.41599 | -50.8569 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9d51f58-fe37-302c-8ba0-613a7ff9e602 | -11.31983 | -43.47097 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fae98dc7-0f31-3987-9b92-58d09b3504c5 | -6.00454 | -44.7209 | 2025-08-31 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7708aad-1717-3444-a6a9-d235a7519b65 | -6.09837 | -43.33535 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9467d41-f38f-3411-987f-bfbff15c434e | -6.9335 | -44.70378 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6e32c13-f365-3f4b-a3e3-c952a9909b03 | -6.95248 | -44.06173 | 2025-08-31 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da459c3f-25b4-38a6-ac25-9725ff13bba3 | -11.35109 | -43.62725 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fc462b7-b245-322c-acad-0d95133bbab1 | -6.27441 | -43.17374 | 2025-08-31 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README17.md)
