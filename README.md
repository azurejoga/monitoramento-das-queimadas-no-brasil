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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12f822a8-9279-3c6e-b706-830a1b51e7d9 | -13.0298 | -45.077702 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7dbcf71a-1583-3f17-8df8-4776ff244278 | -6.5392 | -43.0863 | 2025-04-04 00:20:00 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee864413-6fe9-3be8-ad0d-c29f1d560228 | -20.436399 | -42.9394 | 2025-04-04 00:20:00 | METOP-B | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d6e7199-818b-3173-bfed-9c9d642f6635 | -11.0306 | -48.803699 | 2025-04-04 00:20:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06088e15-eb65-3ce0-b4ce-b07303efe2d4 | -12.5074 | -45.499699 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bbcb5d4-e949-3987-a024-a95cd47dc274 | -13.0315 | -45.085201 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d663035-bda1-3914-9237-0ebf0eda6a2c | -12.2844 | -43.518398 | 2025-04-04 00:20:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac687fc5-0c72-3e73-811d-3c5a047bd847 | -20.438299 | -42.947399 | 2025-04-04 00:20:00 | METOP-B | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c258fb16-6f80-37e6-8aa1-eaf2127fc436 | -13.0395 | -45.075401 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e65611f3-2dc6-3e59-97aa-7e7671ef57e0 | -20.5406 | -43.123001 | 2025-04-04 00:20:00 | METOP-B | GUARACIABA | MINAS GERAIS | Brasil | 3128204 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e306b46c-26ac-33b3-81c7-0c6b769c8fa6 | -17.160801 | -44.781502 | 2025-04-04 00:20:00 | METOP-B | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9419a259-3b1f-3f5b-895f-f1de7f2e6b96 | -12.5057 | -45.492298 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96106c74-00b7-3e8a-968a-8d1cfab686f1 | -16.3113 | -48.345798 | 2025-04-04 00:20:00 | METOP-B | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c5a6c8cb-264c-3d88-813e-ebbf8b620f4a | -14.2258 | -41.5756 | 2025-04-04 00:20:00 | METOP-B | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 42afd4b7-1ffa-3829-8b70-5bb4a045993f | -11.0317 | -44.426399 | 2025-04-04 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a17385fa-fdab-3ab2-ab93-a868dc5e8230 | -11.0297 | -44.418201 | 2025-04-04 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 029df1a1-9cf7-345d-b3c7-fe8ea6e96f1b | -13.028 | -45.070099 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c6ac7025-daf2-3d17-b1db-3a7d67da8313 | -17.8286 | -42.619598 | 2025-04-04 00:20:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7c7f4555-1504-3b9a-ba2e-e6bf38b181df | -17.838301 | -42.6171 | 2025-04-04 00:20:00 | METOP-B | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d68ffd44-e02f-3c4e-965c-9058ce524524 | -17.1625 | -44.788898 | 2025-04-04 00:20:00 | METOP-B | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c3b9e3b6-b302-3fe6-8d4e-c5cfec8dfcb9 | -16.3097 | -48.3381 | 2025-04-04 00:20:00 | METOP-B | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4d40f996-deef-33a6-b543-69d4470dfa2d | -13.0378 | -45.067799 | 2025-04-04 00:20:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75166cfa-91b1-3c97-9264-9eaeb0782234 | -17.83412 | -42.62827 | 2025-04-04 00:41:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 64fb48ea-893c-3315-926e-f2ae41795055 | -12.28031 | -43.53456 | 2025-04-04 00:43:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| af427405-500b-3626-a594-c7dfb27eafeb | -16.46124 | -47.56092 | 2025-04-04 00:43:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3f211ea6-19b9-317b-8d60-c16effd89647 | -13.03634 | -45.09311 | 2025-04-04 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 37d88f34-7e1a-33bb-8067-94b2ab66d6fa | -13.0254 | -45.08429 | 2025-04-04 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| f2dede2b-53b2-3a17-9f15-6f48a7b424e4 | -11.03202 | -44.42382 | 2025-04-04 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4c2d74ee-7bba-3f45-b454-118bca245e23 | -14.92656 | -48.80714 | 2025-04-04 00:43:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 2f3b1455-1963-3837-9ab2-fe5f2e2a594d | -17.15867 | -44.79343 | 2025-04-04 00:43:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| fe7050cc-52aa-3f1d-9b3a-e4742f597da8 | -11.03377 | -44.43563 | 2025-04-04 00:43:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 702d29c5-69a7-3413-a913-110e3ba73a48 | -16.30844 | -48.35066 | 2025-04-04 00:43:00 | TERRA_M-M | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bdb0f1a5-2f36-3962-aa43-15d6333b3a2d | -13.02693 | -45.0946 | 2025-04-04 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 570545ca-1364-34b0-bd1c-89b362630042 | -12.50566 | -45.5033 | 2025-04-04 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5f059e76-e2a4-3874-ad58-fef9d7616e0b | -14.21956 | -41.58906 | 2025-04-04 00:43:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 4c060d89-c73b-3529-9f3b-5541cfea072e | -13.03482 | -45.0828 | 2025-04-04 00:43:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d44a34a6-9438-3a1e-a1ae-2ada06ecde9d | -6.54021 | -43.0902 | 2025-04-04 00:45:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8f049174-cf7b-3645-a43e-b4dfd8877346 | -11.26404 | -52.46301 | 2025-04-04 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cc0c75c7-97e7-3c26-8d2f-876e9c1e1616 | -11.26588 | -52.47786 | 2025-04-04 00:45:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1aff312d-9aa5-3171-a646-637aefaccf76 | -6.23796 | -47.00926 | 2025-04-04 00:48:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60524b96-8da8-3eaa-8d59-6ad52a3f026c | -13.0352 | -45.071098 | 2025-04-04 01:08:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53de65eb-0e7c-399b-8a7a-8b448c93686f | -20.621599 | -55.037201 | 2025-04-04 01:11:00 | METOP-C | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 996a5259-9dc6-3993-8d85-061ead59d395 | -11.2729 | -52.463501 | 2025-04-04 01:11:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39aa1889-b63f-3377-9b46-2ab43c5c6790 | -19.4484 | -54.7785 | 2025-04-04 01:11:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7a73d6-1757-33ed-987f-8bb4368c8d14 | -19.4468 | -54.771 | 2025-04-04 01:11:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d303668f-456d-33bf-9d9e-2fae4af30c86 | -11.2748 | -52.4716 | 2025-04-04 01:11:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fef43518-29a5-3d06-9bae-8d5dc591b697 | -19.450001 | -54.785999 | 2025-04-04 01:11:00 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7fa54df5-470e-3e50-b8e9-a35b94b7a49c | -20.578899 | -56.0256 | 2025-04-04 01:11:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ec49278a-c783-398d-a930-ddc36ff35fe2 | -20.5807 | -56.034 | 2025-04-04 01:11:00 | METOP-C | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e8fb4bf2-2202-324a-b3d7-f68f2b425670 | -10.34508 | -38.47854 | 2025-04-04 03:02:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e13ce7a2-f0a3-38fd-a7a5-ada7627040ad | -10.34615 | -38.47307 | 2025-04-04 03:02:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a9912644-a11b-3b75-b409-737ea381e08f | -10.34825 | -38.47374 | 2025-04-04 03:02:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c020f6f-8dbf-3479-b59f-01cd7914f313 | -10.34715 | -38.47916 | 2025-04-04 03:02:00 | NOAA-20 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf60577a-4357-305c-baea-54435dc8d9a9 | -14.22274 | -41.58447 | 2025-04-04 03:04:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 79cf999d-4938-3fe8-b689-9ea2e53545e9 | -14.22114 | -41.59153 | 2025-04-04 03:04:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1d56ea5-2058-35bb-811e-4846a6b461af | -17.8357 | -42.62852 | 2025-04-04 03:06:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a436a92e-b837-38d9-a5c3-cd1c646e132a | -17.82863 | -42.62706 | 2025-04-04 03:06:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 12752166-6e6b-325d-9371-022f8b986230 | -7.22708 | -35.79317 | 2025-04-04 03:53:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81776b40-a64c-3e9d-bac1-d31c7ee6ea3b | -5.02481 | -43.60049 | 2025-04-04 03:53:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cf73e30-c971-39ef-afa2-be9c700c5cb1 | -7.23054 | -44.76864 | 2025-04-04 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc87d7b3-df19-3eda-b03b-d113f6c1021d | -6.21177 | -35.79971 | 2025-04-04 03:53:00 | NOAA-21 | TANGARÁ | RIO GRANDE DO NORTE | Brasil | 2414001 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 96301df0-1fa4-3710-91a6-88c402ff7f1d | -5.63322 | -44.3222 | 2025-04-04 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba0e5f2-06da-3674-b5d9-75ebe1fbd5c1 | -5.66092 | -35.75552 | 2025-04-04 03:53:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47d293c7-22e0-3873-bf36-49ff840065d2 | -6.19866 | -48.04071 | 2025-04-04 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f339b62b-4c65-32f0-b5fc-b0bc57338d75 | -6.54146 | -43.09233 | 2025-04-04 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| da1fac36-8554-3655-8df1-685173311207 | -8.52396 | -37.00097 | 2025-04-04 03:53:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a3c5929-5c6a-3558-a854-2e57fedadaad | -7.22414 | -35.78866 | 2025-04-04 03:53:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 475e2e28-a241-344b-b5b5-55f173cc893a | -6.54063 | -43.09734 | 2025-04-04 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fd53bfe-3f9b-3037-beaa-589d47367e6a | -6.96847 | -43.01817 | 2025-04-04 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8d3ed1c5-965b-3342-9a63-7b3e10a43f6a | -7.79136 | -37.60589 | 2025-04-04 03:53:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 80a99781-0fc6-3156-b0c8-f3aac2f5f899 | -6.53669 | -43.09668 | 2025-04-04 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d30c7765-24eb-3597-b353-298b618161de | -7.22983 | -44.77281 | 2025-04-04 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 206f07d5-9c14-3e57-9068-91e652c73dd2 | -6.20974 | -35.79889 | 2025-04-04 03:53:00 | NOAA-21 | TANGARÁ | RIO GRANDE DO NORTE | Brasil | 2414001 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5612054a-0994-3caf-ae80-9afdd0b4c265 | -7.79733 | -38.20589 | 2025-04-04 03:53:00 | NOAA-21 | MANAÍRA | PARAÍBA | Brasil | 2509008 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 68b519e3-65d5-3f87-9b7b-a763a2d4029a | -11.03189 | -44.4255 | 2025-04-04 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48fdfa7b-5de7-3c6b-8a9d-b03d9a2c70ad | -13.03485 | -45.08414 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddb361c3-2e1e-35bd-9eac-e564a23e11d2 | -8.11166 | -43.12426 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 92dfc09d-7f81-3181-98e1-3ebaf73c5715 | -11.78949 | -40.93022 | 2025-04-04 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 33480c6f-d323-3e11-b20c-3179a302b24f | -8.82321 | -39.81899 | 2025-04-04 03:55:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 27eb4f05-5c90-321b-a2b4-d327bf86ae74 | -11.79285 | -40.93078 | 2025-04-04 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62608a6f-fda2-35ed-b5ae-0b8c47091b68 | -11.03002 | -44.43608 | 2025-04-04 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f34f5a58-8311-3987-9cc1-e556cffe0f3d | -11.55334 | -39.23903 | 2025-04-04 03:55:00 | NOAA-21 | CONCEIÇÃO DO COITÉ | BAHIA | Brasil | 2908408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 98743f50-d379-3bd5-9b8b-8580e3ed8483 | -13.43231 | -41.78257 | 2025-04-04 03:55:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 313759d8-f371-3cb4-b0d3-4f5883df9aa4 | -12.55894 | -45.33543 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d336cf01-e735-31a9-85ea-e1f0eb058352 | -14.22592 | -41.58841 | 2025-04-04 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e796da1c-bca5-31e0-9eb9-1f719aefdc21 | -10.66775 | -44.39524 | 2025-04-04 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07935ef9-2a58-3a00-ac1a-61fd4b74b57c | -11.27982 | -40.98138 | 2025-04-04 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ac06969a-af52-3faa-9b3d-6afb2a4440b8 | -13.64276 | -41.35764 | 2025-04-04 03:55:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6d078c3f-e8b1-3e10-a70f-43397b459a1d | -12.507 | -45.50598 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8302d312-918e-3d32-878a-d666f8df1c66 | -11.78613 | -40.92966 | 2025-04-04 03:55:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c88e75ff-3ddc-3043-a9a0-0746d172f3dc | -13.03081 | -45.08341 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78541f7f-d251-36c8-8e53-c839b1027f5c | -13.02483 | -45.09359 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8a1181d1-4aa6-3c8f-9fa5-22cc0a2f0ec8 | -10.92488 | -44.16528 | 2025-04-04 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac5a6555-23c9-3987-9c21-b7441a6f19d5 | -8.10393 | -43.12304 | 2025-04-04 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 34c700de-8019-3c85-a14b-1b2ec80092e8 | -15.65181 | -39.18765 | 2025-04-04 03:55:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e7540a15-58dd-303a-b27c-de56960baa03 | -13.02952 | -45.09068 | 2025-04-04 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 725e5495-ff70-3b3f-a492-a377786f287b | -12.28229 | -43.53095 | 2025-04-04 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1317a68-3925-35f3-9f68-a73baec0c9dd | -10.34949 | -38.47502 | 2025-04-04 03:55:00 | NOAA-21 | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c5eb2b55-89cc-33bc-8c4d-bb8fd1ef186a | -8.93389 | -44.23566 | 2025-04-04 03:55:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36a248fa-03b4-3105-bb0b-ed766e429dc7 | -13.604 | -41.70147 | 2025-04-04 03:55:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
