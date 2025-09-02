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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fba57ea9-e73c-3fe9-9481-7a2ba8fb53c0 | -6.84745 | -52.81058 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2b8cb07-cb4c-322a-b894-1ba76cf4bf54 | -6.84492 | -52.82727 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 356786fe-dd2d-3ece-afb7-332dde09bcab | -6.4294 | -55.61598 | 2025-09-02 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 398a5605-fed0-3fc9-b105-ecd1f126d26c | -6.75672 | -56.39361 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c98ea8e6-d1a2-3ca6-8669-335456614a24 | -9.21928 | -47.1061 | 2025-09-02 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ecd9ce0-0020-39cd-895e-9700205bad39 | -6.84555 | -52.82312 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe371fcb-b44a-30c1-b086-5b032c6bbd69 | -6.40021 | -58.20658 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6de32743-e5c2-37a7-b828-2c977b74321c | -7.28258 | -60.6517 | 2025-09-02 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 482694f3-96db-3c9c-9f5e-559a3cb1f377 | -6.78707 | -52.81863 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 582ebd00-ed97-3d51-a615-cfa334af43b8 | -6.85606 | -52.8102 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23dd644d-59f0-3b53-8e77-0a14faed00ac | -7.98107 | -46.46826 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec152f3d-b7f1-3af0-9bc0-ad4314481834 | -6.83706 | -52.83036 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5906458f-b693-36ad-907d-121b197ed35a | -8.14128 | -49.82906 | 2025-09-02 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7494778-3b8c-31a2-befc-2581487e99dd | -3.4303 | -52.79815 | 2025-09-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dffda344-05e0-3ce4-a64f-d22db5ac4181 | -7.98528 | -46.47953 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dcb82079-1f2e-3d02-b7a8-31ae0e7deee3 | -6.8506 | -52.82224 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 807f5c20-1a11-3da1-972c-956831174bc9 | -7.76763 | -49.48932 | 2025-09-02 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e6cc17d-0ea2-300c-9b4f-52863c71be0f | -6.83831 | -52.82205 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0009d435-dadf-3285-956d-5959769582cd | -6.53854 | -56.19923 | 2025-09-02 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 385c7774-5cd8-3dcf-bdab-185c40e682b2 | -7.84964 | -46.74359 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08bf1323-8206-34f1-adab-395f8c3a9e7e | -3.44806 | -49.49487 | 2025-09-02 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7110c695-d6de-3ec7-a3c8-d8aff78cde9c | -6.8633 | -52.8113 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ad7ad86-2cd9-39e8-ab58-5bfc437aba0f | -8.3551 | -52.53135 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 355b4320-927b-382d-a571-e20b05ec7e15 | -7.70633 | -44.60778 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2d5baa1-8b4c-30ab-a34d-8c89fb277f56 | -6.79979 | -52.80769 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c060d609-6db5-3952-a256-ab037b1f6486 | -8.7052 | -50.44546 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f943cdac-84b5-3501-9d2f-ff0cb7d673b5 | -6.80154 | -52.82075 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aba2beba-6218-3cad-b47f-10576fcd18d0 | -6.33843 | -58.17789 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ba7da1f-8f05-3984-a341-ac7ec1e7e045 | -7.79169 | -45.45645 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0468a75-c98f-370b-b2eb-6b5e68e09b5d | -8.07644 | -49.90422 | 2025-09-02 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d735e377-875a-3c56-8b36-451e9c3ccfc3 | -6.85595 | -52.80339 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0ffae5b-8633-3bdc-835b-683c161489cc | -7.06518 | -44.34223 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21b16b1f-3d4d-3490-bb08-2959d940541e | -6.7686 | -45.71679 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0895ae4f-c4d6-3d28-b222-e42ffa714a65 | -8.71379 | -50.44672 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7e38d1a-8be6-3da4-adb2-e9e88c82a67d | -6.84979 | -52.81956 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c269987-ef23-3db1-91ee-719cd38a6777 | -3.32955 | -48.70949 | 2025-09-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce373057-1fab-3c37-b7d0-3a462343cc2a | -6.78047 | -52.81331 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9286a7c5-0faf-3776-bce1-a4a3718f0b11 | -3.22955 | -47.12776 | 2025-09-02 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| c5d0edec-0927-3d35-96a5-7ee5598aca75 | -6.82496 | -52.83706 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e18f3d9-6f1f-3bba-8558-d6f5dd6961c7 | -6.85482 | -52.81866 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41070533-8308-3590-8ef9-26350fddee23 | -6.33558 | -58.17352 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7539c244-fda6-35cf-8d58-769d72ed6656 | -6.85468 | -52.81173 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e166e16-42b8-3dad-ac3e-b444e7e268ea | -9.12395 | -46.04909 | 2025-09-02 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fbc91618-e899-3192-9e62-4e1c759ab1db | -6.84682 | -52.81477 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11ac54c6-e88b-3f6c-991e-8dfa89f9ce77 | -5.31815 | -55.99858 | 2025-09-02 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02aa50cb-8bab-37eb-b612-d472fe88d0b1 | -2.74861 | -48.67598 | 2025-09-02 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8734e534-a8c3-3acd-bbe2-8d42f736611b | -6.84067 | -52.83091 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d93cd82-efd1-3062-bbdc-35d95fbfd988 | -7.30807 | -44.28207 | 2025-09-02 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba83fd4f-9ef5-3aa1-813d-5fd49d8fbc8f | -4.91671 | -43.20067 | 2025-09-02 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e050896-ca28-3917-98f0-e3efd526f987 | -2.55925 | -47.71134 | 2025-09-02 05:04:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 955b28fe-4e9e-37de-98ef-bdf760807ddf | -7.91752 | -46.44266 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088f2c45-e709-3f66-ae5d-9519a6f29e96 | -6.85851 | -52.79349 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b640e4-fbfc-3132-9724-31b713926149 | -4.31128 | -48.09434 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f47ca78-1f19-382b-85ca-1f61d2e282c7 | -3.59688 | -49.45497 | 2025-09-02 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 523a314f-f515-3317-b49a-c5dedb521e94 | -6.82685 | -52.82454 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6379c15-761f-3122-8c9a-ed16c051c731 | -7.9287 | -46.44406 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bab65539-928c-37d5-a5fa-4735f351b7d8 | -6.98809 | -44.31562 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bccdda9c-0189-3aad-a2f9-3e2aebdfba2e | -6.88097 | -45.85933 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57fcf013-7711-3348-99e0-2bd355228a9d | -6.85244 | -52.80964 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cac91503-041d-3ea3-b4c0-77a3ccb64770 | -7.31147 | -44.27665 | 2025-09-02 05:04:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ef7f265-c31f-317e-8b0b-6822dfe5fc83 | -4.31273 | -48.08421 | 2025-09-02 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51018119-e2ab-3ca5-b978-0cb1912f40e7 | -6.78346 | -52.81807 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9e4fc16-608f-3308-967a-f8c8d453af73 | -8.88095 | -47.97269 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4322daf-0767-3178-b581-3eadce5a0c39 | -6.98743 | -44.32072 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb9a6c7c-1105-36bd-991e-7dcbbb723696 | -8.13305 | -45.03249 | 2025-09-02 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 318242bd-c3fe-3fcc-9942-781007a788ab | -7.98811 | -46.45779 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24529202-40c8-3fbb-bef5-ff455be13523 | -6.78408 | -52.81388 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d1807fa-76c5-35db-818f-9ffe6e2cd8de | -6.33904 | -58.17407 | 2025-09-02 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e3da1db-73da-32e6-b7f3-e36f8467112f | -7.92309 | -46.44348 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4afbf101-2552-3914-ae43-7614583ca7d9 | -6.79193 | -52.81079 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad2f1ac5-1d6c-3019-ba40-bcd9fce1ebce | -6.7968 | -52.80293 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05ed7bf9-c79b-3887-a397-653d288b056a | -3.16923 | -49.47955 | 2025-09-02 05:04:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f18c7f18-f35b-3519-b818-d028de0fe660 | -5.15925 | -45.17192 | 2025-09-02 05:04:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a6ca857-80e2-3510-bf75-1b99cd90ae18 | -7.91699 | -46.44666 | 2025-09-02 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fac334e-4abb-3e11-8915-9b9a6a67a36c | -6.85042 | -52.81536 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 979dc251-70a8-3c18-9e98-9996faa24f71 | -8.85351 | -50.58369 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 21abf3a8-7b03-356e-9c8a-b4bc6bbe48da | -6.89673 | -59.79296 | 2025-09-02 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c756ae7-0544-3e97-9f82-3326af93c31b | -2.51643 | -51.9109 | 2025-09-02 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3df6de85-d2dd-30e1-ae46-8aa77ce0c79a | -6.72639 | -42.25478 | 2025-09-02 05:04:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6b30d2aa-2d83-3594-b9dc-ea640c1cf5e6 | -6.88775 | -45.85205 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41fb1315-f57c-3dc3-b6db-d8104fbaba9d | -8.06327 | -52.35559 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22d85ccd-ee1a-3944-bcae-27d5bc8eaaa7 | -6.8292 | -52.83342 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3652b91d-fa5c-3995-ace4-122040885dc8 | -2.16026 | -53.65398 | 2025-09-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c57d2d87-7791-3ab0-90a9-ef31f19041a4 | -6.88884 | -45.84385 | 2025-09-02 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb6993f3-576a-378e-a61e-f4b7bd8bcd15 | -6.84999 | -52.82639 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ce5ba2a-2f10-3ff6-82ab-881d3ed76572 | -6.2813 | -44.51707 | 2025-09-02 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de6b3a4b-833b-31d5-8d8a-a91fecf788bb | -5.69541 | -45.95002 | 2025-09-02 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da241fdb-de54-3560-ab73-54b44fb661b3 | -7.71258 | -44.6088 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ff46652-8067-3962-977a-61612dc1e03a | -7.876 | -47.96431 | 2025-09-02 05:04:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19548304-6d65-3455-91fa-facb06b5224f | -7.11168 | -44.76257 | 2025-09-02 05:04:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 49f8de54-e5fc-385f-8d5f-77e25bb7a361 | -6.81662 | -52.8188 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2c90b636-7ec0-30f9-85c0-1742adc6d43e | -6.83895 | -52.81786 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 109ddaa7-d797-3135-8c03-7fbc5462f7e4 | -8.7134 | -50.43655 | 2025-09-02 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de79e66d-20f7-31c0-9475-c768c4922feb | -6.82086 | -52.81516 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8df1b61b-09dd-3d6d-b109-04fd52fdb7b2 | -7.47259 | -44.82293 | 2025-09-02 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1701c3ce-01eb-3ce0-8271-6e697d9120fe | -7.48888 | -47.88063 | 2025-09-02 05:04:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aef76fef-ab48-3786-92b5-1e765a35b920 | -7.78924 | -45.44668 | 2025-09-02 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6db5da7-611b-3be0-9911-b2fa232f6bdb | -4.12102 | -56.34168 | 2025-09-02 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9351ed3-84a3-33e9-9b68-e652be7a8a64 | -6.85701 | -52.82071 | 2025-09-02 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c04547e5-c0bd-305c-b443-d73ca5f92c34 | -6.28196 | -44.51221 | 2025-09-02 05:04:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README56.md)
