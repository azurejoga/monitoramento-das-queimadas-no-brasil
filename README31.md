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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb7dbcc0-c7d6-39e9-963b-3d3da5570b46 | -11.14985 | -47.20119 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1703ae91-8320-3cd2-89c0-a165e6725f9f | -10.77046 | -45.35995 | 2025-10-02 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7982c1f7-d607-36c9-a10b-5b19f9a23865 | -11.78819 | -47.55975 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97a1a5e4-cc01-3888-b80b-802c5f7d7bca | -13.00542 | -45.2054 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc6203d8-cdd3-3963-aa87-ec55879166cc | -12.79965 | -46.85396 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 309df98e-1baa-3118-bccb-cf2a07028ea5 | -6.96394 | -45.31849 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14979660-314f-3d90-8ab9-9298dd9e5a93 | -10.91155 | -44.31769 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 520e2a52-21ea-3bcc-b602-5cbe970a9216 | -11.6222 | -45.05017 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dab31972-03c6-3725-a85a-47894e1de4d2 | -6.69599 | -48.70808 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 3056f143-c81e-3074-9ab8-1cb2b93ffcf1 | -11.81263 | -44.90638 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0590da8f-ca38-36f4-9c57-45e55e1a1f19 | -11.35594 | -44.94009 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ce8eb37-ddd4-3d42-80fa-53815e8aefd5 | -12.18904 | -47.90457 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e96852ae-a715-3847-bdd0-bfb6dbaa6b25 | -6.69191 | -48.70113 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 86731a45-dc3b-3c78-9d86-c4ebfc14cae8 | -11.45245 | -44.96888 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d119ae05-2786-39d7-96b9-25e71aa5857a | -12.89643 | -46.91962 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fb7e2a5f-e640-3970-be23-882a902fd346 | -12.80156 | -46.86476 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 864c9019-9b7b-3b11-92d7-376be8341823 | -6.48381 | -44.287 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17533465-412c-3268-9ae1-f06e63523e9c | -11.35966 | -44.94069 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25df81ad-995c-3d52-9541-f1074365694d | -8.55156 | -44.73144 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85a7884a-b80c-31cd-8268-82a9399e8fb3 | -13.50241 | -40.09528 | 2025-10-02 04:02:00 | NOAA-21 | ITIRUÇU | BAHIA | Brasil | 2916906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d1ace55b-0305-3c72-a175-357dfec898ac | -12.25778 | -47.80124 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8663f23e-3358-3eca-a6ef-a7cee05db7cf | -7.29701 | -42.88794 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b04b6910-aee5-3c8d-9442-c5ef4addfd07 | -6.96796 | -45.31936 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8b38f7e-efc2-3f75-a7a1-0af13ce34c5b | -7.87598 | -45.27402 | 2025-10-02 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d47dc2a8-428c-38c9-bc60-228718f77f09 | -11.05402 | -47.81389 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 588e603f-9489-37ca-bc85-37ca7bc4c34a | -7.78279 | -42.53819 | 2025-10-02 04:02:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 15e70535-4f4e-3921-8208-54fbdc3035e9 | -11.80002 | -44.98166 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 404c4407-2fed-3cbe-9b3e-108b9050df3f | -11.0873 | -47.84855 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2475050-dace-34ed-a00c-3c081d3b85d0 | -10.24795 | -50.31815 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| dea45095-ec9c-3156-a500-22935e938de3 | -10.54643 | -43.64993 | 2025-10-02 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c6cf579-7554-3061-b46b-26368993788e | -6.78451 | -45.59441 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5c9ceda-f1ac-3479-b49b-97b190fe368b | -11.20477 | -47.19039 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8d8d961-653b-3541-909a-876e5aa93efb | -11.79108 | -47.56876 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22a4aea7-b351-3def-88e4-d0dbec2b359a | -9.9301 | -43.73035 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| f2f865ac-f3c8-32e1-a409-80a20a8d0265 | -11.80776 | -44.99507 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2a16f05-98e9-32e7-a379-1d1746ece74f | -12.89115 | -46.92992 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67e34635-3d7b-34ad-81a4-e358f08ac14e | -6.32558 | -43.03595 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c78f6edb-0588-3835-84df-2d98a83863f1 | -9.94852 | -43.72923 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b3bcdecc-df4f-3246-aa2a-a8ad421ca5b4 | -11.81358 | -45.00544 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02b1b810-5067-3e44-8b7d-eedf60fc8766 | -9.92432 | -50.49103 | 2025-10-02 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 559ccb41-9e81-3f3c-aa41-762c0f584526 | -6.33206 | -43.04128 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4688f2bd-13e0-3d88-b623-1eaeb2ffc56b | -11.8247 | -45.00731 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 39f7058b-1dd3-3609-a65b-527c1573ebd8 | -6.82725 | -41.62288 | 2025-10-02 04:02:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ce000eab-e721-391d-949e-185b70beb32f | -12.95328 | -46.43026 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb000489-b2f0-3196-b387-a750d747ed8a | -5.90103 | -42.52097 | 2025-10-02 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c9cb4dbc-e874-31d3-8eee-dddc635c5e15 | -10.20694 | -50.27136 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 61faa7bc-8c72-31a0-9d37-a30cd0911488 | -10.43062 | -47.47142 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ce59ef1-6184-3ab2-b0b3-36a500e69253 | -12.20474 | -47.79445 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10d59a00-5c02-369b-a109-404bfff9f8d7 | -9.93318 | -43.75613 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| e97888e6-e2b4-37d5-88cb-bb38d4ab333c | -11.86174 | -48.08382 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e7239f0-426a-3829-b463-52b3d7d10c8a | -11.35886 | -44.96823 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b27c8496-20db-31e7-88f3-75883733c32c | -9.03505 | -46.6772 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83554d5e-e571-32c0-856c-34dbebadb374 | -12.12707 | -43.42754 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 162c72a0-04a4-3dfc-b3b3-955c31301e30 | -8.51528 | -44.66766 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| caa2a54e-28fa-37ed-a1ec-4cb176f0fc11 | -12.11552 | -43.43346 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d942a52-3d41-3ec8-ae69-fdd60ce77b8f | -10.26403 | -50.32117 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f2a7a8a0-9c6f-3a6e-926b-96605aea400f | -6.50063 | -44.29719 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5afcd211-4346-3446-9b3b-18e81d5ebe1f | -8.90153 | -46.62582 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5dc6bda8-e19c-33ae-b274-76f49fa688d9 | -6.96407 | -45.34475 | 2025-10-02 04:02:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40ff7532-3704-305d-b245-d222a5407e1f | -6.48696 | -44.28496 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b76c5689-2667-3bff-b10b-9d5d5ead8820 | -11.86911 | -45.01505 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f106402-03a7-3d20-bbd2-bef742efbc1b | -11.09912 | -47.84608 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 525cd414-b43b-3238-a191-26ba35433645 | -12.81869 | -47.05249 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0b51312-62dd-35ce-8049-9c870fb1d8b2 | -12.65838 | -46.87079 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45c867b9-621e-352f-9967-63b76c6bc361 | -11.86449 | -48.01796 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bcbc21d-9f75-398b-bbae-b79dd1a9e2c9 | -9.38453 | -47.60601 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7628a272-151e-30fc-bf8e-a4af1378db0d | -6.77935 | -45.57432 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf2c42a7-e4ee-38f5-9e16-a8901b62f5b9 | -11.15059 | -47.19706 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc6f1f64-a76b-3ce0-b129-53c9231451bb | -12.89159 | -46.90322 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6422b41c-2d05-3c81-90af-9ee09d82a9d8 | -5.9661 | -45.70834 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37b9c15d-63df-3eb7-b9c5-bb071827d46a | -12.77382 | -44.9109 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 772c6b55-c5ae-31ab-9433-dc4cbcb29d73 | -12.65755 | -46.94791 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51f19565-410a-31dd-941a-bea8a3a74e86 | -11.6739 | -44.27584 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ae5432f-f6f2-326d-bfb3-2d70c9bb32a4 | -8.89868 | -46.61667 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50b55552-830b-3c0a-8a94-7e18e0363135 | -11.42977 | -47.28937 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d50c146-2998-3753-bab7-530204ccf275 | -5.83839 | -42.79408 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 24b2eb67-d140-3a25-bcea-1cefa4cc956e | -7.60218 | -45.40851 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7ed47ad-e139-395a-8227-e107d619e509 | -8.40882 | -47.75437 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 959d385e-6885-381a-8925-9fd773b7eb6f | -9.95007 | -43.67505 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68507c4b-b4e1-3645-b1fc-80021740b4e2 | -12.23952 | -44.04357 | 2025-10-02 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 603b00de-66df-3cf3-9082-234feedc28c9 | -11.47043 | -45.11938 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4476f346-c018-3b09-86fb-8b5fbe9e31e9 | -10.23461 | -50.32995 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5c9fa24-4eeb-3a6c-9e84-1d25049acdd6 | -12.27542 | -44.13247 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d78769f9-dea8-3fe1-8d01-edf85c7a5084 | -6.38095 | -44.29052 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 54accba9-9456-3e55-8ead-e455ee037223 | -11.43641 | -47.17957 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 346539f2-55f7-3f38-9f39-e987539bd338 | -11.53088 | -43.54344 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ea5bfae-d8b9-380a-8cf4-8cd56b6d7198 | -11.73968 | -44.42427 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c10c2aa-f062-3df2-845e-c37e10af8a2a | -10.8165 | -46.62331 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b6cdeab-18e8-377f-b0ad-58cf6ac118ca | -8.50898 | -44.70485 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52468703-53b5-3a5a-8dec-239f6a1881a5 | -6.4853 | -44.29479 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e7a8334-e93b-317a-b260-a878e2594b99 | -11.79773 | -44.99531 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a710c18c-714e-30a3-b46d-07ca33a242ed | -12.83842 | -46.87051 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ccca629-1438-3cde-946a-dad18c61a67d | -11.17747 | -47.27057 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 51a626e4-35b8-33ed-98c3-c4303e0d102e | -8.65859 | -47.09071 | 2025-10-02 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c93f2922-7be1-34c8-849e-c77496de1155 | -11.47329 | -44.98132 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b168d95-21af-3020-894e-647c50e123c0 | -12.81868 | -47.02863 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fc1af45-5f33-3e8e-a37b-8d2cfc05d140 | -6.89746 | -43.13147 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd8bd971-5898-3a03-9535-f731f32680b5 | -10.24469 | -50.33542 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3b5d96e-1b39-3897-bc65-31550002af5d | -12.66917 | -46.85738 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb5e8d3d-36db-33d3-8b3e-7938de11f28c | -12.85201 | -46.86509 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README32.md)
