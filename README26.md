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
| ee45c21b-6a97-397b-a22e-a28379781ea3 | -6.14758 | -41.7892 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 992abadb-ea88-3413-9774-b7e0374a1d27 | -9.37368 | -46.95312 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96a326c3-58a9-3b97-afa1-140cc0986b88 | -5.46812 | -42.93818 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 626ed5ed-c5c3-3ce6-aa80-1262743b82dc | -3.01595 | -45.38987 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 78bb34ef-3375-350c-921b-13f7d5ab11cb | -11.53469 | -43.5027 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fb0ecf3-3e43-346f-9564-7a937c6a464f | -6.17224 | -41.78698 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 927b44c8-023f-36bc-9d1f-412e7bf973a3 | -10.81048 | -43.99821 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780885dd-e18b-393d-bd6d-627606861cb8 | -4.36017 | -43.4009 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 34bd26fd-4fad-39a5-960b-a7e24c14e93b | -11.05519 | -44.78311 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea3a509-4f97-353a-a78c-805b76c2954f | -11.06301 | -44.66056 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c02e9fcd-3af1-3498-b32a-b1b27fbe316d | -3.84742 | -41.56731 | 2025-10-16 03:47:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e7d6a15f-7df1-3659-b92f-a98566d12600 | -5.60084 | -44.25893 | 2025-10-16 03:47:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2bbc3c66-00e8-35c7-9249-d151ba372b26 | -6.12108 | -44.29003 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 222e18be-c813-33a7-ab53-7ae505973876 | -5.89816 | -42.82768 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 01d47faa-56b1-3480-a008-b5e34ac2675f | -6.19676 | -42.61013 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15041d15-4577-34a8-bbf9-6cdf31be8132 | -6.01228 | -35.32162 | 2025-10-16 03:47:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 43d836a5-361f-36bc-9330-f58f25f0ab9a | -4.92764 | -41.54364 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8cb25e8b-a8c2-30a7-8088-f27f15c06cac | -5.45385 | -41.02105 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ff7dbaf8-0a48-306e-93d8-22a405c03bc0 | -5.87756 | -43.8762 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 943d308d-0315-3922-af85-34cbb90c960d | -9.68538 | -44.53312 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| e08009fc-7948-3d13-bcbc-d133a03e8525 | -3.74611 | -39.27181 | 2025-10-16 03:47:00 | NOAA-20 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b6dade1c-745c-3200-9494-a205bb5c6b5c | -4.96049 | -45.10047 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1b92744-bbbe-3af6-910f-5abb2596ddda | -4.10564 | -48.01625 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 48442fdc-6262-3454-a484-d3b1e1c84deb | -6.22223 | -44.60077 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6337a4af-a535-30be-b7b8-5e50415d4aa3 | -5.32265 | -44.8378 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 789f0c1c-b88b-34b3-9809-6cb4cc7062fe | -10.61755 | -45.2419 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a69916a-ad8a-3caa-81c0-047e18fb19a8 | -10.0486 | -43.83204 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a6f7d24-d94a-39a8-a3fe-ad6246c0c9df | -4.24362 | -45.75998 | 2025-10-16 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 289a1637-09f0-382a-8408-3ac294f500c1 | -5.42687 | -44.23288 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b1f4e25-28cb-3fe6-8a11-8ffd898678ca | -10.67099 | -45.32549 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f60f0d9-29de-35bd-a415-266d8c570aea | -5.96583 | -44.8009 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fad2735-013c-36b5-b62d-8ae4fa5ac0f7 | -4.95169 | -41.70469 | 2025-10-16 03:47:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aec6d8c4-d78c-331b-9d82-c0903a7a210f | -5.32564 | -43.94263 | 2025-10-16 03:47:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aaa0b34-ffd6-3e44-903a-e03ae951238f | -6.22348 | -42.50436 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 828b8bbe-cb50-3a19-91da-2b8242e22c6f | -6.32172 | -42.77676 | 2025-10-16 03:47:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8876f16f-774f-395f-9f01-999f600a340f | -9.71297 | -44.53047 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a96225e-78a0-3d4f-ace3-7808805ef80b | -5.39117 | -41.16219 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3fddffa4-9faf-3afd-8fd3-565bae2f4e3e | -10.1216 | -44.57213 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 132a202e-c287-3ac1-9b2d-08b934eadfb7 | -11.5711 | -48.55716 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81239046-8656-36f6-aad5-d84fe256755c | -10.84775 | -42.75961 | 2025-10-16 03:47:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| df693720-5004-371b-b00d-1dd084306aae | -10.70217 | -44.43534 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 921dfa33-62f5-3fa4-9334-3ef6c555cd05 | -4.10076 | -48.04448 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 523a486b-11c8-36dd-a6e1-9601ff6b407c | -7.01645 | -38.83055 | 2025-10-16 03:47:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7c3eff74-8167-3c41-8588-cf5f966f0915 | -5.87339 | -43.90055 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfcee3b1-20c6-3650-a3a3-b0e3dc60f39d | -9.69528 | -44.50423 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 74f1a958-4232-3445-a2b0-d97bbadc391f | -12.34581 | -44.2445 | 2025-10-16 03:47:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7893be8-546f-3b4f-8def-90b89440b5e5 | -5.87425 | -43.89552 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56efd818-6836-39c2-b1f0-6163380162e8 | -10.13676 | -44.56152 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e1b14aa-e5be-34df-94b3-021b204cbc72 | -5.85108 | -42.89234 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| efcec090-aa16-316c-9f5e-c063a95346b5 | -3.28641 | -40.90012 | 2025-10-16 03:47:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a24cb9e-4775-3dc5-a833-30ed066dd20f | -5.24969 | -43.22486 | 2025-10-16 03:47:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48960cd5-1168-31f7-ad06-882caa96c5be | -11.49504 | -43.48027 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b29cc7a-f6ab-3ef3-ac88-a38cc5a8a4ce | -7.15372 | -38.45881 | 2025-10-16 03:47:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6d1c5b78-661a-35b4-aeaf-c46060a20725 | -9.7167 | -44.51834 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44ab5397-69df-3024-b630-4c7a3fe19261 | -4.35483 | -46.78093 | 2025-10-16 03:47:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 649827a5-a15b-3377-bf07-b7df95da5836 | -5.32214 | -44.84082 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f6cecce0-8f8b-3324-b70a-88ef140bfe40 | -2.44508 | -49.37789 | 2025-10-16 03:47:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bf815ed1-974c-3a6c-8bbf-885ee2975ae6 | -10.60608 | -47.4103 | 2025-10-16 03:47:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd906562-9379-3893-992b-3f863c61ca91 | -9.71842 | -44.50852 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f16bdaf-e0ff-34a8-9d56-7abd6e7c2325 | -5.6882 | -45.10069 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4746a021-8d15-382c-b18d-d446e7e502ef | -5.9149 | -42.83376 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b5333a30-104e-3b41-bdab-a0f15f942341 | -9.69177 | -44.52409 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2649535d-efa8-3d34-bf65-9e42cd204cb0 | -5.25297 | -41.02055 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4cc4f5e8-5efb-39ce-95ee-cf382b0fbf5f | -4.37123 | -43.39246 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 553e1475-8d26-3cac-971f-aef7e949035d | -5.87246 | -43.84904 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 489e3f5f-f8c1-32c0-9a52-0604110ed677 | -5.39204 | -40.88602 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| bb768c7a-2296-37f0-b70e-947a52862196 | -6.24314 | -45.38641 | 2025-10-16 03:47:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 251ca4c1-ac7b-3611-ac17-1d1c06d72a5c | -4.83687 | -42.80106 | 2025-10-16 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 8382e94c-9b4b-38b0-bd9d-60af0902a004 | -5.59993 | -44.26427 | 2025-10-16 03:47:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d049e098-4aa1-3b8b-96f8-6ba2e7c9c276 | -11.60052 | -48.55585 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bb8bbc0-9b41-36ae-bf4e-c6d4f606087c | -6.1784 | -43.43729 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da1f353f-f8eb-39c6-9830-8a3476b531b4 | -10.17108 | -39.08706 | 2025-10-16 03:47:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 13ca85c5-22fe-30f3-b239-a5407995ed51 | -5.79511 | -35.60126 | 2025-10-16 03:47:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0240aeed-e5f3-363c-a533-b430a1326c19 | -5.06169 | -40.47067 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b86c98a4-d1eb-37cf-9a49-fdfe3973271f | -5.87842 | -43.87112 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a54cecec-0692-35ff-86c0-faeeaf0243cf | -6.14811 | -40.91011 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d83de4fd-e0e8-30c9-8e30-3322bd065c52 | -11.71206 | -44.27156 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3121feb3-5dc9-34db-bef0-60416f7dfec2 | -6.25972 | -44.34467 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7531202-088d-3050-9dbf-ffc70df9590a | -4.59117 | -43.57992 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d24aa288-7b83-398c-be4c-2e6cc1571f26 | -3.07229 | -49.51776 | 2025-10-16 03:47:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5afabd6b-9dd1-34dd-9a3c-0c4fbaeafb5f | -5.95224 | -42.31259 | 2025-10-16 03:47:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dfc543be-74bb-3590-9503-f1d76d6e6902 | -5.32343 | -42.92131 | 2025-10-16 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 649fa68f-2b67-3eff-97ff-a567069caf1b | -9.67672 | -44.50103 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 83dd039b-d8ed-365d-8265-d2271cc740bb | -5.64012 | -45.97272 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05a74313-b81a-3117-90de-213ac063c59d | -11.578 | -44.06041 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dbe43108-b13d-30d8-a6c8-27cda84f1cb8 | -3.67862 | -47.63751 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| da20b417-1cff-389c-8f87-71c42233a025 | -6.06348 | -44.53436 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fbeffdf9-159f-367c-861d-90a34cebb070 | -11.23224 | -39.44368 | 2025-10-16 03:47:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8fc18f45-ef50-31a1-ab33-aacd1e1d0ee8 | -6.16525 | -40.90266 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 5ca094ab-f9f9-3c54-9745-ba6ddce80bb8 | -11.57723 | -44.06469 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b3fc2df2-bcaf-3000-8078-f9fcb246885f | -9.37437 | -46.94947 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe7a07cf-66c3-3bd1-aa95-e09e1e9b9296 | -9.24753 | -44.36869 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 275b7700-5b8e-37a0-829f-09181cc560a6 | -6.46581 | -41.85741 | 2025-10-16 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6b7979d5-e667-3fbf-9085-4a73d5c52732 | -4.38064 | -43.39392 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c38eabdb-1a3d-33a4-b2d6-4e855164bb59 | -5.97856 | -42.80541 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 89e9fbba-2e35-3b23-b9e3-261a8a169ebf | -11.56968 | -48.55834 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e8f9197-24c3-3dc8-bfbe-a3055c791ec7 | -6.13198 | -41.75658 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b60dbcc1-8733-31b9-88a9-cc80682db432 | -6.02106 | -43.39445 | 2025-10-16 03:47:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b78c5bfc-d240-371a-a405-5fb8ff04fd1f | -6.13664 | -41.75389 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e1caf28d-558b-3fb5-ae7d-bbf47fc26f24 | -4.87232 | -44.57919 | 2025-10-16 03:47:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README27.md)
