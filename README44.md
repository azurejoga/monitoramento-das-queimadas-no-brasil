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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3183d849-5bdd-3e45-b45e-aa0dd8f40c55 | -12.91421 | -46.09866 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e18c0869-2d7e-3199-b5a6-df0abfcf75c9 | -7.29051 | -43.67922 | 2025-08-20 04:57:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9caf562-e613-3863-9d15-7f89b35ee1e2 | -13.40548 | -46.35256 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90cc8077-6eeb-3296-8263-e1e702472093 | -13.57078 | -47.02738 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d87f3e-ef2b-3b9a-ab7a-a13418edce23 | -7.65372 | -45.26647 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed59e68-2619-33b6-81dc-a5c148c5ab33 | -7.96749 | -55.29954 | 2025-08-20 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 006fc234-72d0-3947-9486-d01c5b958248 | -13.02694 | -46.80594 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79b6fb9f-211a-33e8-9652-291456b9a855 | -11.59413 | -50.53763 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd17df5f-99a8-34ba-9526-746e8386c677 | -10.4465 | -64.40961 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d4b9336-4a8c-3796-a3ed-0dfa971daa4c | -6.19353 | -53.5175 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc3dca51-2376-3b36-a5b9-1d3b073f737d | -13.48664 | -47.0575 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb23dd44-0f48-353c-ae07-c6f040a4dcc4 | -8.02805 | -47.67527 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1aecbe36-6a71-3368-b236-7e643cb708c5 | -13.17924 | -46.86931 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43cc54c3-2941-3dd4-b138-0417c4729794 | -6.46125 | -53.36934 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bce9aa7-61df-37b6-9879-f080e5bb332c | -13.17698 | -46.88773 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 758253a4-d86e-3d56-9ee0-e3057acff96e | -13.40108 | -46.37259 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ae3cf6f-2659-3325-9fc3-ea21621fb584 | -8.02346 | -47.67456 | 2025-08-20 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46508871-99d9-35fd-acf6-a57fa95240d9 | -13.2308 | -50.81404 | 2025-08-20 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35cafe15-b72d-38d8-8231-02a05e78ac5e | -9.22692 | -59.60256 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4747bf78-7eba-3293-b9dc-72cdff4a2b39 | -13.40824 | -46.35929 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da2a502a-96a6-3eb6-834c-07a8f68a331e | -11.56827 | -50.44734 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 018eba40-7355-3002-ae78-1d1fafd6e03d | -7.26638 | -50.1893 | 2025-08-20 04:57:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3140143-1cc8-35cb-a8e3-1b6f6ab9ca37 | -11.75142 | -48.18549 | 2025-08-20 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0988b1f3-5114-3735-a910-950634b9fb9d | -9.1983 | -60.82746 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a2e861c-6d40-3771-b552-df39630c61ce | -9.888 | -60.28028 | 2025-08-20 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f1d28f7-6664-35ed-b023-a393be1c6927 | -10.4406 | -64.41191 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44469e55-8211-3a9f-b3a5-2bda91d4b041 | -8.65451 | -54.58585 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ae607b2-fe25-3611-a31d-de9d0b623f89 | -11.31596 | -55.21911 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd858796-49eb-3613-a26f-e428ca5a3e69 | -8.29235 | -46.35225 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10e42906-688c-37ae-949e-aa6e1f68bcf1 | -12.98808 | -45.20964 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 16c1cb3d-badb-31b3-9f1b-d27dc8fda65a | -10.31361 | -46.67801 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32ab87bc-a459-3e85-9eb4-804d20d302fa | -7.58272 | -45.42538 | 2025-08-20 04:57:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e31be4c-8457-38b7-acd6-2899c931770f | -7.49984 | -63.83453 | 2025-08-20 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356052ca-d470-3eb7-a3b6-1cd5a948e85a | -12.95832 | -46.14827 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b52e82e-b8ec-3809-85cc-04f6eb8837f5 | -13.03179 | -46.80995 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70619997-878a-3233-b423-ee9291e9832d | -7.21332 | -60.38225 | 2025-08-20 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e94db49c-f30d-3c4e-8637-2b55f1bc4394 | -7.66251 | -45.25903 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74d627bd-0102-38ba-87a7-9d5b9381df62 | -11.3121 | -55.22208 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8243f90e-0e48-3121-bc4b-08735e0e82c4 | -11.56726 | -50.45442 | 2025-08-20 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 912da45a-c2af-36c2-8a04-932f87dca0b5 | -9.21527 | -59.69473 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4bc3412d-368f-3035-8560-b2f35ee78705 | -12.63802 | -46.88681 | 2025-08-20 04:57:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a834203-7f9b-38cc-be0d-573424fc14aa | -9.1903 | -59.6274 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 878fbe25-8899-3f8b-b0c3-6f042bad1515 | -10.31282 | -46.68404 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a08b5a3-48da-3f51-97b4-c127aa7d1e41 | -9.81201 | -46.88512 | 2025-08-20 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98628766-b0d1-3b8f-bff1-147e0e72d879 | -11.31637 | -55.12901 | 2025-08-20 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 648162b1-65ba-3a56-a7f6-fcc7ea767259 | -7.64499 | -45.28984 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ca0a039-124e-3b66-bb15-3ef8498ed3d4 | -7.63617 | -45.27424 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9991b9db-791d-3de8-955f-67fd289ca15d | -12.5189 | -45.60124 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 165ee7ba-bdf3-35b3-b272-26f2ecc75d12 | -9.1925 | -59.63811 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 88a6769a-4235-39f6-865b-158043be663a | -10.81705 | -43.28444 | 2025-08-20 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dbfa31fc-8411-3964-8367-dc9f05ffc1c1 | -14.15168 | -45.2899 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e51d7d3b-0252-31e0-b86d-dcde0b66597d | -9.17501 | -59.59881 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5d8d316-5e07-304b-8730-2e701a65b15a | -8.6512 | -54.58533 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac88f4f0-3028-3ce6-9c01-0d988284b533 | -6.19298 | -53.52099 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98a54c8b-911e-3050-9b51-edba14292c11 | -11.09537 | -44.8149 | 2025-08-20 04:57:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91975fe8-37a7-34c6-9901-b1f3d90ff129 | -13.48951 | -47.07693 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d478331f-60b2-35e6-8e43-fac2837f59e2 | -12.66418 | -44.9578 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4d53d73-01f5-348d-9002-5c58b9f8c37d | -9.92479 | -49.29366 | 2025-08-20 04:57:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd40aa93-eefc-38d3-9e40-4b8380d89b32 | -10.91491 | -57.50845 | 2025-08-20 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5795d6df-54d2-3678-a290-9ab8c0f923cc | -8.96489 | -60.49766 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05c6d3ed-49e8-3e0b-ac98-af6d9089a51b | -9.22694 | -60.33567 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| e2d28c87-e5c6-37a7-b5ca-6207dd89cd05 | -6.15056 | -57.71819 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0c3b805-ce7a-37cb-b446-4935ddd48c56 | -14.15662 | -45.28965 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa1c4468-d9a1-39b2-9e1b-5891fb24c9e6 | -10.69177 | -48.21955 | 2025-08-20 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 28aa4972-77bb-3624-8354-c1ff56636b25 | -12.14451 | -48.01775 | 2025-08-20 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eabf22a8-3504-37d4-96c0-8cfb7931653d | -12.98949 | -45.19708 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c47327b3-23ec-348d-b8b3-4664c104c490 | -8.78856 | -45.48331 | 2025-08-20 04:57:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0630465-a042-3d2c-9a6e-2d631d580f5e | -12.13971 | -48.01737 | 2025-08-20 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e3afa40-4a83-3c12-84ce-ba012744afdb | -12.9458 | -46.1599 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcbec691-c544-3843-8884-ecf6802f10c3 | -13.58756 | -47.01978 | 2025-08-20 04:57:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17efe6d5-80d3-31e1-806f-5c704b40e495 | -12.77511 | -48.265 | 2025-08-20 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49f6de16-429e-3b47-98bd-c987278805fc | -6.14393 | -57.71271 | 2025-08-20 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad2a5d90-deb5-36d5-99bb-f6f63baf346b | -7.63079 | -45.27338 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 215ccd35-26f6-3835-8878-8b8e424b2f38 | -13.00411 | -45.1771 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7afe825b-945c-3f6b-a4ef-3e4af6ed9786 | -7.65909 | -45.26737 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43d1cc99-3b0e-3a2f-97bf-588cb5f470cb | -11.74606 | -48.1899 | 2025-08-20 04:57:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e8144b41-2067-36a7-abf0-96ce209b7628 | -13.18586 | -46.9017 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84fe5e98-8b7a-3cc4-985c-0442b95c3493 | -10.24176 | -64.48379 | 2025-08-20 04:57:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 305ea597-2903-3b33-8d5e-f967f04a3d63 | -13.03415 | -46.79015 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b19d8d95-c921-3173-9181-545f7c572026 | -9.23782 | -59.60973 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea624b0a-d64b-368b-84aa-d84e1d5bd2d2 | -12.95161 | -46.1578 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ae5b920-573e-30df-8a5b-daf1f0814933 | -11.66645 | -60.1904 | 2025-08-20 04:57:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 213f7862-0587-37e6-adef-b1c5c9bbf8eb | -9.24088 | -59.61552 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 37f82ead-0ae6-30be-98bd-356cd76ca8cc | -8.2978 | -46.35003 | 2025-08-20 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af9cf2bc-33e4-3940-a9f1-dc533f6107db | -13.02867 | -46.79192 | 2025-08-20 04:57:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec75169e-4bf6-3863-8bab-570cff5e63dd | -11.1356 | -46.97708 | 2025-08-20 04:57:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af1b9167-67e5-3596-9edc-5eb7efe1c035 | -13.40151 | -46.36916 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7433af4e-06bc-3516-8181-bf8833607417 | -12.22442 | -53.60416 | 2025-08-20 04:57:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2eede92b-e827-319f-8350-f386609557e6 | -7.65421 | -45.26297 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 952b4dba-f234-3b15-ab83-831c4a6d203c | -13.49105 | -47.06445 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5005dcf0-7296-374b-a2a6-7f488b6a05f9 | -6.42458 | -53.36366 | 2025-08-20 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b368e51-a4e4-3f38-b421-2fd21e7d39a9 | -10.31322 | -46.68101 | 2025-08-20 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e37d0ec-140b-3b9f-b5f9-bbd7f36d458e | -13.49469 | -47.07757 | 2025-08-20 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0322aa0b-5502-3388-ab90-9dbfbe6da376 | -9.20738 | -59.69333 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ebc1d58e-65bb-3bf7-9cc8-43301b98ac3f | -12.99343 | -45.21453 | 2025-08-20 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26e83588-1333-380d-8433-3f487a5935c2 | -14.16391 | -45.28716 | 2025-08-20 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22e7343b-0ac5-382d-ad68-264bcdf99b5a | -11.19181 | -48.62348 | 2025-08-20 04:57:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d222c207-a1f6-341a-a2f0-e80ceecc065c | -9.17758 | -59.58694 | 2025-08-20 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52e7a9f0-3b25-37ca-95da-94d81689b74f | -7.63129 | -45.26978 | 2025-08-20 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc9d4ed0-aab3-35a9-bff3-5908617bb892 | -10.11956 | -62.16938 | 2025-08-20 04:57:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README45.md)
