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
| baea6ca3-c71b-3e92-8623-1f6c6147a608 | -12.30945 | -37.88184 | 2025-01-01 03:46:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c603771b-b8f1-37f8-9f1b-66a03d519d4c | -12.87689 | -38.4184 | 2025-01-01 03:46:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b6c70c5-d9ba-3c82-a2d3-e2da2f023012 | -7.7492 | -37.10503 | 2025-01-01 03:46:00 | NOAA-20 | PRATA | PARAÍBA | Brasil | 2512200 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df89e800-9b03-3886-a9cc-556cdf1c25bb | -8.21029 | -35.47768 | 2025-01-01 03:46:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4d565bee-8337-35f5-abd4-ee337b12d6c7 | -7.86237 | -35.14478 | 2025-01-01 03:46:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 09195f3c-813b-3ccb-ba20-2e428c4012d4 | -5.10547 | -38.02423 | 2025-01-01 03:46:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b1d29ec0-5556-3f8d-9dd8-8894ed95be3f | -6.08024 | -37.45592 | 2025-01-01 03:46:00 | NOAA-20 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ec4cd9fc-9299-3494-b602-0a8e2193312c | -8.80065 | -35.12151 | 2025-01-01 03:46:00 | NOAA-20 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c406b4a8-0f9c-3c1e-9a83-f9d032adefee | -5.2124 | -44.90449 | 2025-01-01 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 00533829-124d-3715-a1b5-5d04f9bc7c6c | -5.18516 | -37.6359 | 2025-01-01 03:46:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2d47deaa-e60f-3004-a972-d9692d5cc5ce | -6.47841 | -42.68108 | 2025-01-01 03:46:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c000142d-29a6-39c7-bac1-244b4c46319a | -4.91078 | -37.41883 | 2025-01-01 03:46:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c43b2bcf-e0a4-3a04-928e-71b33026b124 | -9.07685 | -37.73071 | 2025-01-01 03:46:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c5e05fd-599b-3b3e-a89e-42a9ffd10efb | -3.50081 | -39.38235 | 2025-01-01 03:46:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dfe19ef5-a138-3b66-a246-a9bb4fcdb034 | -14.13494 | -41.69049 | 2025-01-01 03:46:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2a204ee3-a2da-39a4-b55f-61871060845e | -12.1412 | -37.98084 | 2025-01-01 03:46:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 38f22555-a2a9-3357-84d1-6780ec40b8fc | -8.20746 | -35.47349 | 2025-01-01 03:46:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b1c919b2-b854-3e67-91fd-bf42dfc5b7eb | -7.47624 | -35.26495 | 2025-01-01 03:46:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b1c7d41-ddb8-35ec-ab21-712b114f45ab | -8.79424 | -35.16337 | 2025-01-01 03:46:00 | NOAA-20 | BARREIROS | PERNAMBUCO | Brasil | 2601409 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 834c1a6e-53dc-34fa-a39c-0fb56e026a9e | -6.20743 | -39.3129 | 2025-01-01 03:46:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 14fa7a80-48ea-3818-b6e4-af4e3b710566 | -4.24614 | -41.92351 | 2025-01-01 03:46:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| af7e09aa-8a19-3fb3-b3b4-1504237cb533 | -6.4243 | -40.0182 | 2025-01-01 03:46:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| daba2426-b79c-3f10-81b0-76e450f53d1a | -6.77785 | -38.61324 | 2025-01-01 03:46:00 | NOAA-20 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| afa79264-ae32-3ade-95b4-91a2496cee42 | -6.02038 | -38.04517 | 2025-01-01 03:46:00 | NOAA-20 | PORTALEGRE | RIO GRANDE DO NORTE | Brasil | 2410207 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bbd7f442-3e2a-384a-8ae5-a8c633aead37 | -12.87587 | -38.36066 | 2025-01-01 03:46:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 39964aa6-3cee-393c-860f-137f8019b2e5 | -7.91832 | -38.47679 | 2025-01-01 03:46:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a0feacdc-ab64-3be0-8c67-8c179fab94af | -3.55649 | -40.84481 | 2025-01-01 03:46:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| da401e06-4f7c-3731-9d40-f124bcb1cbc1 | -5.10442 | -38.02404 | 2025-01-01 03:46:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9c9838bf-714a-3d9f-ab21-282180417b47 | -8.21085 | -35.47403 | 2025-01-01 03:46:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b0257eac-526b-3027-b24d-d3b978f39185 | -4.92261 | -41.30226 | 2025-01-01 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 06ddd6ca-b373-3b54-b00d-6829ebbef52b | -5.42863 | -39.46458 | 2025-01-01 03:46:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a2932f4-e0b6-3e4e-9c89-30e7ddffe2cf | -3.26811 | -39.26743 | 2025-01-01 03:46:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b26514d8-d49d-3540-885c-af32d840953c | -6.95176 | -43.00916 | 2025-01-01 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5a0c6396-4ad4-3c53-b38e-2785f42a311a | -4.24193 | -41.92281 | 2025-01-01 03:46:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2fe23157-1733-3a83-a612-58fb0fa2e2f2 | -6.81576 | -34.91612 | 2025-01-01 03:46:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a2eb4dfc-9218-390c-86cc-ef6f389e7c05 | -3.71921 | -38.57162 | 2025-01-01 03:46:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b558e5aa-be63-38b8-837d-c33ae24eac88 | -6.95247 | -43.005 | 2025-01-01 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| afe73923-6c55-3bd2-a667-2f7b10c4fbc8 | -8.02394 | -35.07337 | 2025-01-01 03:46:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 131a8bc8-338e-3304-836b-12e3ef082741 | -8.02452 | -35.06962 | 2025-01-01 03:46:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a22b00fd-927b-3b76-a547-fea117308394 | -3.27346 | -42.09181 | 2025-01-01 03:46:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8244ad4a-5633-3cb3-90c5-7f2eaa2ed98b | -8.64012 | -36.22865 | 2025-01-01 03:46:00 | NOAA-20 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6eac81be-29dd-383c-b83d-987001a2cc40 | -9.48014 | -35.9675 | 2025-01-01 03:46:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 59c5b7ce-dda2-3b1d-a2d4-ddc55b6c3200 | -7.21532 | -39.94916 | 2025-01-01 03:46:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 88d0f584-58d1-372d-ad72-2b0e9e583894 | -5.52487 | -37.7657 | 2025-01-01 03:46:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a851f4a3-b787-3ff9-b9ae-a7493411e3f7 | -13.67592 | -41.76427 | 2025-01-01 03:46:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 944696ac-6bc6-367d-a75a-92e9fb3471a5 | -8.26197 | -35.48512 | 2025-01-01 03:46:00 | NOAA-20 | CHÃ GRANDE | PERNAMBUCO | Brasil | 2604502 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 90eb0563-e0c7-3136-aa77-facdc8e5c8a0 | -11.97045 | -44.98526 | 2025-01-01 03:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cc2bdfa-29a9-3e58-affe-58e994eea514 | -6.75658 | -39.13908 | 2025-01-01 03:46:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| beda15da-a831-36dd-a7f2-b623aec125cf | -7.5422 | -35.31606 | 2025-01-01 03:46:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 35a444b1-7d51-3b1c-a1e2-2780618b93c3 | -9.28912 | -40.44543 | 2025-01-01 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3adac7b2-3149-3ef2-951f-362913a3abf9 | -10.6078 | -44.32886 | 2025-01-01 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 478ae7b4-a94d-31ef-82b0-457cc1a9bfeb | -10.97808 | -39.6387 | 2025-01-01 03:49:00 | NOAA-20 | QUEIMADAS | BAHIA | Brasil | 2925808 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e311694b-3d4a-3418-9184-2c4a6833df0d | -20.76306 | -46.77065 | 2025-01-01 03:49:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 744e861c-299c-35e7-8cb7-b520a4df280a | -10.74841 | -37.20627 | 2025-01-01 03:49:00 | NOAA-20 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| bd3c8a77-7b2c-3b79-bf84-952b9a8c31d7 | -9.37244 | -40.55225 | 2025-01-01 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e062cba8-5a2e-3257-beae-2764b0d000e9 | -11.29693 | -42.04707 | 2025-01-01 03:49:00 | NOAA-20 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0fb0b790-47a5-3548-a60d-ee7cc95dadbe | -10.71985 | -37.38899 | 2025-01-01 03:49:00 | NOAA-20 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b652e3a9-d430-3e77-98c5-7895510fe37a | -20.76235 | -46.77194 | 2025-01-01 03:49:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 01ba9eb7-ed70-3d42-a875-1d5622ce2cb8 | -9.44085 | -40.56392 | 2025-01-01 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0443754d-567c-37b0-9377-d8e06227742b | -9.39868 | -40.31614 | 2025-01-01 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2e28390c-439e-3d51-bf24-875b2152bc22 | -10.29613 | -37.53588 | 2025-01-01 03:49:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee53bba4-aaf6-3246-8ef9-85c3bcf452c4 | -9.87711 | -40.29078 | 2025-01-01 03:49:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 38d8cbf5-cd99-3910-a913-3ecb3c444ee7 | -10.64723 | -36.80603 | 2025-01-01 03:49:00 | NOAA-20 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8645b858-fa23-308c-b244-ab8cf484f5b5 | -10.29227 | -37.53884 | 2025-01-01 03:49:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60e2a0cb-4e80-3084-9776-3b3087fae774 | -9.37099 | -40.55351 | 2025-01-01 03:49:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dcbff3b4-16dc-374f-a6d6-93bef4ebe4a9 | -10.29558 | -37.53938 | 2025-01-01 03:49:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8ba2ae36-f32c-3532-802e-db121523ab60 | -9.32097 | -41.14833 | 2025-01-01 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 32d43319-d610-341e-b248-88800bd36869 | -10.91823 | -37.13883 | 2025-01-01 03:49:00 | NOAA-20 | NOSSA SENHORA DO SOCORRO | SERGIPE | Brasil | 2804805 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 247b6b53-e9db-367e-bb3b-43dd1f3b353a | -9.18405 | -43.12191 | 2025-01-01 03:49:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 076de1ab-7409-3285-8e6d-28d88679f8ac | -16.06976 | -38.94897 | 2025-01-01 03:49:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ddd6107e-0de4-3afe-b5ef-55aa4fbb4d9a | -10.29282 | -37.53535 | 2025-01-01 03:49:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 686dda56-0aa4-37e9-b326-0709f9cece32 | -22.67524 | -42.85676 | 2025-01-01 03:49:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 29e000d9-8d9d-3d87-b6f7-8d09f8a23647 | -10.64389 | -36.8055 | 2025-01-01 03:49:00 | NOAA-20 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 81d61ad0-dd27-3928-a51a-b3a1cb5a025e | -10.60229 | -37.42374 | 2025-01-01 03:49:00 | NOAA-20 | ITABAIANA | SERGIPE | Brasil | 2802908 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 114a033d-d96e-3193-b858-b62bf07f73c4 | -23.33768 | -46.77385 | 2025-01-01 03:51:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d90dfa85-8dff-3d44-bb5a-1ee151145436 | -22.5398 | -48.81443 | 2025-01-01 03:51:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed72735c-908c-3d7d-a777-103b94b6680b | -23.59332 | -47.43926 | 2025-01-01 03:51:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5cd496bd-9ebe-3303-b1a6-bdd5f77b441b | -23.98441 | -48.91911 | 2025-01-01 03:51:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acca83dd-c1c6-389f-928f-3caf9eb6185d | -23.13994 | -46.95562 | 2025-01-01 03:51:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9b888b54-f570-333c-8379-5a9939b78b88 | -23.13996 | -46.95781 | 2025-01-01 03:51:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d9d7f974-5877-3239-8520-6bb710eb7712 | -23.20116 | -46.24489 | 2025-01-01 03:51:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 62d1ab41-1e57-3199-8901-9716f31aecbd | -5.1357 | -38.1495 | 2025-01-01 04:38:00 | AQUA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c92df387-c2d1-345b-9290-47b2300985e0 | -1.68975 | -45.88038 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2568b644-bcf6-380b-b604-97f1b5660463 | -4.24627 | -41.92108 | 2025-01-01 04:38:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83c6372f-770b-36d3-a62e-4ea46e7c7eae | -2.26632 | -45.68916 | 2025-01-01 04:38:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 419535d6-eb99-3263-832c-3866cbe0d8d2 | -2.26337 | -45.6902 | 2025-01-01 04:38:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b9c67e6-2f07-3c29-87f2-2a6dbab1b02b | -1.69047 | -45.8801 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 261abf1d-1a28-3e86-bf99-032ee0ca4419 | -1.68696 | -45.87955 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 152bf326-621e-3989-a0b9-e479d7b0cd36 | -1.68815 | -45.87169 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a50438ad-f837-3ae8-84bb-6cbc8fcd4552 | -1.53119 | -45.85313 | 2025-01-01 04:38:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3d48bb2-5deb-35c8-a2ce-6ab2226d1b53 | -1.68755 | -45.87563 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e325613-b70b-3d81-93fa-2878da03b87f | -3.55776 | -40.84259 | 2025-01-01 04:38:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 517e242c-ff97-3932-bdd4-13544c77d3e1 | -2.1813 | -45.67765 | 2025-01-01 04:38:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7f81364-06ae-37f0-8715-9f56eca03a78 | -3.6295 | -43.18808 | 2025-01-01 04:38:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11f9154d-60cb-34fe-8256-b3a4dba8b7b2 | -1.68747 | -45.872 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 025ff150-0a56-38bc-8021-2af8de69d02a | -1.68685 | -45.87592 | 2025-01-01 04:38:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5526e73d-f905-3ff3-9eeb-fc6ca4819ab6 | -12.30938 | -37.8749 | 2025-01-01 04:40:00 | AQUA_M-M | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| e57a21da-be4d-3665-a1d7-01e7b532e3a2 | -5.21106 | -44.90313 | 2025-01-01 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58ceb720-6034-3594-b756-e2d6bf32e2cf | -4.30005 | -46.27236 | 2025-01-01 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b551e7e3-cdfa-37c7-b63c-ea291a128308 | -8.84327 | -49.90839 | 2025-01-01 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README3.md)
