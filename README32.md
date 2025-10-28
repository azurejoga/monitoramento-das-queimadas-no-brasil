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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b9cf7e6-f1cd-3086-bc39-63280cae3ffe | -7.27587 | -44.97663 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea1445a5-8061-3144-8025-6618ed217600 | -11.31674 | -51.45727 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c7356e8-1535-3a00-a232-ec1788a97e9a | -7.61041 | -46.47454 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9374e99b-d521-389e-90f3-c48f394c786e | -10.42208 | -45.18629 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01643881-969c-3361-9f65-3687cb629734 | -10.60031 | -46.61779 | 2025-10-28 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d19a862-897a-3c42-831c-1980c32d3bd6 | -10.63134 | -42.31757 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 36d36af0-480b-325b-81f4-feadaacaf994 | -10.66056 | -45.25055 | 2025-10-28 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7436eb5a-d1f6-3815-93e5-2c73e3ee19e6 | -7.36663 | -47.79299 | 2025-10-28 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a362df1a-49d1-3dcd-bec2-488d1465cf7a | -11.52797 | -44.97566 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3660d218-2139-3956-bb25-02afdca55d2e | -8.08243 | -45.96103 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a7241f6-501f-3066-bfbb-b432bf41b53e | -10.95252 | -50.25095 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa5c8c13-6b98-3df5-aa8f-1b380b78498d | -6.63732 | -47.19749 | 2025-10-28 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 247a81a4-87f5-370d-a9b0-c54414ca01e6 | -6.23566 | -43.31849 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c01fffde-62cd-3d72-8748-1b2a51ff349c | -7.9455 | -45.50816 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 561906d1-c55f-333f-ab53-2340712e46fb | -8.18409 | -48.18203 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77ab1798-848d-3587-abe0-92cafc862951 | -10.88224 | -44.39009 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00a4fe0e-e7ea-3043-8987-a22dab7db9e0 | -7.89436 | -45.69144 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bdf62196-b108-375d-8807-d16813bf653c | -6.7385 | -48.1748 | 2025-10-28 04:14:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e927095-4215-33d2-8225-6617cce04795 | -7.81468 | -46.46646 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80e23599-b560-3390-8dfb-dcdee5f96678 | -10.56203 | -49.77615 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 12b21d49-e2db-3ae7-a698-96cdfa343d4b | -7.04051 | -41.64122 | 2025-10-28 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 102b2a44-6a17-3020-a605-7fb7111ea3e4 | -8.11814 | -45.48522 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3fc94c-6a06-35af-9011-05776a6a9e1e | -12.47198 | -44.49454 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8bedcd34-d3e0-34b9-bd22-8a821d0da3c3 | -9.2365 | -45.60989 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e84e815-177a-3205-885f-f16266d9d6fa | -8.34752 | -48.16731 | 2025-10-28 04:14:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f07f1c5-6fa1-3617-8f78-945d038dac60 | -6.16612 | -46.09599 | 2025-10-28 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 934838e8-e5dc-3f72-8515-a44ecb7eedf1 | -7.97427 | -45.50492 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8aa3cc8-a38a-3669-bf99-4304ecddc3f2 | -9.26565 | -46.27443 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc4399f4-d655-3507-a778-133910e0f803 | -8.64222 | -45.28559 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6768c168-65b3-3277-9120-5dd5f37d5bb6 | -5.3647 | -50.56626 | 2025-10-28 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ae78402-bfac-39aa-a60f-72b59280cba0 | -7.44816 | -45.12931 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55e21e96-8ff3-3159-bcca-40b5a5ef42b3 | -6.11958 | -42.45235 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 64d03511-9527-3721-838c-32365d942770 | -9.55366 | -46.92633 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a373051e-c40c-3b47-8d66-672d3e8a6328 | -7.39312 | -45.12023 | 2025-10-28 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c76faf65-aed2-3f38-b39c-b80164b3f853 | -9.25464 | -45.56285 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4e0f292-7989-35ea-be18-61273686741f | -7.9722 | -45.53973 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da4501a2-cd18-33bd-8ce5-36048a3b29ed | -4.85133 | -50.68052 | 2025-10-28 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 20cfd803-b2e3-30b8-9058-5c8973d1138c | -7.97095 | -46.75076 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 5df40c08-7ba7-3d2f-872a-f1a3e9cdd05f | -9.11365 | -48.698 | 2025-10-28 04:14:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6cef676c-5229-3d22-bec3-55e4dc576791 | -10.93318 | -47.65951 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 012b86ae-231e-3df1-86d7-6cc8cd284c42 | -8.00089 | -46.19332 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2cb26c77-289c-3281-a5ed-e44a4258c0a9 | -6.44387 | -44.60055 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 476d1ff3-ad17-31ab-be9c-143ef3d9bd76 | -7.77989 | -45.38116 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| be95242c-24ae-3077-8880-1abd2412fbc9 | -5.78786 | -47.72215 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d319b6b7-cab1-365f-bfc6-17fadec1e621 | -10.74224 | -47.58964 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 708a078e-7ff7-31a6-8ab8-391e07b0f1f6 | -6.40648 | -48.5901 | 2025-10-28 04:14:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e73f5fe1-b03c-31eb-9eb9-f792c8710c9b | -13.37312 | -43.46 | 2025-10-28 04:14:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a574e4fc-7685-37eb-b573-747bd1894416 | -12.55233 | -44.9338 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e3fe01cf-f743-37c6-a4d3-36e7c2db6cf6 | -5.49243 | -47.74789 | 2025-10-28 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a003825-de1e-32d6-8fb7-f434015cfc90 | -10.62906 | -42.30971 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 6aa2283e-a317-33f6-8676-b0247b3b6e74 | -6.13671 | -44.58563 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 611a577d-e3bd-3143-b77c-7a54bd9c52d6 | -10.3361 | -47.77514 | 2025-10-28 04:14:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa973201-9718-3f7d-b657-5f4778ac0203 | -10.19283 | -48.07006 | 2025-10-28 04:14:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63c419de-671b-3064-ac10-836793b3b648 | -5.67704 | -47.82191 | 2025-10-28 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0e80daa-c0e9-3ccc-a725-751e6d0128db | -9.58813 | -46.89711 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b32aa90c-a2e5-3b3b-9b20-d7a7d5765304 | -10.66301 | -48.49929 | 2025-10-28 04:14:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6adc573-ba12-351d-b095-15ee2fa682f7 | -12.55177 | -44.93733 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b50ab806-8f9f-3fa1-bd44-a1f544a9dc0a | -10.64465 | -47.90667 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b5c5a6f-e21d-3851-bbd2-fd1e76fa2ce8 | -6.10405 | -42.42158 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d6f63adb-64e9-30b5-a9ae-2a11fdd8a2ba | -11.67038 | -41.31905 | 2025-10-28 04:14:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7cdf19cc-ff08-3f0d-8ad2-7ebba27541fc | -10.22217 | -49.90014 | 2025-10-28 04:14:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84b7c0d8-125c-3305-a891-24e5e415bfc1 | -10.29519 | -47.18628 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73740667-58ea-3823-9a39-8c376939dd74 | -11.16084 | -44.67297 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 81780f7c-0b84-34d3-88ab-2ae6b96bde31 | -10.67789 | -47.25988 | 2025-10-28 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42cf8d03-2283-3e94-87ed-b92a6a29515e | -7.27392 | -45.01048 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0da0c8c-696d-3074-96f9-355d3a934f4e | -6.99165 | -44.00595 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f81c5180-6870-30db-851b-fe216cad3d84 | -9.33574 | -43.14133 | 2025-10-28 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3a4b9af5-da76-3082-9b80-7d2209aa9b73 | -7.96173 | -45.49516 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9125b6b-65b4-3280-83cd-c8ef92f368f0 | -8.19155 | -44.44397 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 404d1cb9-b10b-3352-8c20-3d26bed9881e | -10.31968 | -47.15086 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 469eedf6-aa03-395b-be91-b26eb61e0e03 | -5.61437 | -47.10955 | 2025-10-28 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 049f505b-542f-34b2-8702-38fc97ea2c6d | -6.9977 | -39.11563 | 2025-10-28 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08239aec-cf2b-33ed-9d1b-2b6af8523f60 | -8.09094 | -44.41285 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c84d250c-9315-3f6d-9e95-1a42863bc337 | -7.43395 | -47.20134 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d10de476-1b6c-33de-82be-3a505696c683 | -8.19545 | -44.44096 | 2025-10-28 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16ae8fbd-6227-32dc-b0e1-132fa29c4617 | -12.62224 | -45.07223 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aef5f33a-b0d0-36f0-bc14-3f7d6f73d795 | -7.42367 | -41.86821 | 2025-10-28 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6e6c4ffa-edce-3f32-b7d5-825a74eb6b38 | -6.22657 | -44.51073 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 940dbb95-6361-3000-86b1-d8f67669f0be | -7.94894 | -45.50872 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 918d143f-6e08-3f22-a9ce-8afb94a79554 | -8.2704 | -46.89345 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d557568b-57f4-39fe-bd7d-29faf8a9a0ba | -6.11574 | -42.4553 | 2025-10-28 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76bde894-29fc-36bd-a933-61d5cee04db4 | -8.53553 | -47.35612 | 2025-10-28 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8306108-ff6c-371e-8160-f2b4e45dc10f | -5.40933 | -46.82061 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d79a8d8-426f-3df6-a01f-e649a7c5019f | -6.97947 | -43.99686 | 2025-10-28 04:14:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 453c875e-c2ec-30e8-bd1b-a0359aba4501 | -8.66858 | -47.11945 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1041e44b-ab12-3a71-a378-e83ee42c2d51 | -7.1255 | -47.02368 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 552ee4d7-2b13-3c0b-a5ff-0df03455be92 | -8.19948 | -46.93675 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0c02001e-b27c-375f-80b5-a1b5a844337e | -6.58139 | -41.40463 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 57e1e7e1-b4b3-3278-918a-f61838f96e4b | -9.9704 | -47.17473 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dd91055-d072-39e3-823e-e7f206a3b73a | -9.279 | -46.39407 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f9d3765-32ae-3de9-bbdd-981a25488b93 | -6.30122 | -44.70164 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2c0d7c0-e52b-38f7-b42b-73d0a36f5c82 | -9.18558 | -44.61543 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f7cb921-1297-349f-b0ef-8eb06e475c25 | -7.9365 | -45.5418 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d8c187f-4a0f-3d1b-a701-5f484128751d | -9.34001 | -43.09196 | 2025-10-28 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 73647dda-e12d-301b-aa1f-1c9550ffd319 | -7.94797 | -45.49294 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 03b0634b-0cda-3543-9bb8-2c608bf5d3d4 | -7.98104 | -46.73488 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8228a5f-6335-3844-b452-0e2987e30709 | -7.33124 | -42.44702 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ded3b2be-b0a9-3e5a-9c09-a8705dc022c0 | -8.18379 | -45.71048 | 2025-10-28 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 365c7867-111c-3533-9d57-c2fd16527523 | -6.26783 | -42.71996 | 2025-10-28 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f3d204a-64dc-32f3-a1bc-a18fb6c0c368 | -5.48042 | -47.74597 | 2025-10-28 04:14:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README33.md)
