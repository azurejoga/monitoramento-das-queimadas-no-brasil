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
| 31c5ea6c-1fee-35b9-9b81-16f8f446278f | -11.39629 | -44.23148 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8d4039cd-56fe-32bf-9a51-29d456d2321b | -11.47305 | -44.19067 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f07073ca-5211-3a84-9b92-c4a1cfd10e0f | -10.2881 | -44.02764 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 687820b2-a73a-3425-b5b2-c2d3fa559213 | -13.92807 | -45.62495 | 2025-10-17 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06c05d69-4add-327c-98de-c70968da0b2c | -13.00483 | -43.22392 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0a2145d8-2a1f-3c02-8266-d435f79a6c0b | -11.40817 | -44.22577 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c145a01-2eb2-3b64-90a0-b05f4d72ab11 | -11.39286 | -44.20819 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 12033318-06c4-3250-b4de-94a9b5193319 | -10.10221 | -44.62687 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7276a3aa-bcff-3309-8b6f-d8175e0252b2 | -10.10951 | -44.62291 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 204435a4-1c5d-3cd1-b934-66970cf82463 | -11.45656 | -44.0238 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1061c553-d264-302d-8490-ea3e84c05e11 | -11.39857 | -44.18917 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f596131-f4ea-3101-bd27-b65451ca256b | -11.45117 | -44.23833 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f06c416-d8d0-3980-b15b-48721dbe0eaa | -11.40829 | -44.234 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e23149d6-9d1e-3cb4-b123-9ebc88477a6a | -9.70833 | -44.55609 | 2025-10-17 03:30:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 353770f2-e707-3ca1-b837-5847a93cf0ae | -11.47902 | -44.19193 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7d2b003c-9dc3-373f-bca2-12bbfa5e8dfe | -10.25956 | -44.04489 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f63b8958-582c-3591-add6-df265047c9c9 | -10.12793 | -44.54547 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 698f6a38-6d9b-3e7f-b062-9158b2b3ac22 | -11.26802 | -45.29189 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77e3e840-1e9a-3f05-87cf-112eb1cfc9e5 | -10.83111 | -43.94414 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6bd5194-c3ad-313b-9ed3-af0c2aba1274 | -11.47304 | -44.28606 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65205307-f98b-3667-9641-5c27c1ae0007 | -10.64435 | -45.25127 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9734419e-f762-3664-97e1-bc8f702c7f0f | -10.11362 | -44.56815 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e414777-2e08-3656-8412-af9656b51650 | -10.10114 | -44.63234 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a80e393d-1534-3561-bad7-ebcff3186720 | -11.40661 | -44.20163 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 280eab0c-9509-3e9d-9a63-40dc4ebc730b | -11.45387 | -44.22466 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3bf03f21-eb53-3943-969a-0d1d591f9f3e | -10.71465 | -44.53136 | 2025-10-17 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77821765-4c5c-3a07-8469-3c16b7a9dfca | -11.49362 | -44.05465 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ac3a9e4-86b6-3195-acfb-d8fe33afab1c | -11.26685 | -45.29753 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ee8bd98-1753-39bb-8246-3a98a2345fd8 | -12.32212 | -41.4074 | 2025-10-17 03:30:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c2784b01-0d87-36b1-a1bd-2e7ea9ec6ef7 | -11.39213 | -44.2211 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 47238ea5-8502-3fe8-bdc9-a19ca0378e0c | -11.49692 | -44.06926 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb297c84-3a64-32d3-8a8c-272bb415aa72 | -10.15708 | -44.54515 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c82a1bc8-5772-350f-bbf7-0332142c62a1 | -13.2708 | -44.48632 | 2025-10-17 03:30:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6d4a6684-0da3-3442-b463-d0623282a58d | -10.27687 | -44.02084 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97518589-d952-3136-97ce-3f5e19ae09e7 | -10.50524 | -43.43558 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b188872-ea98-3437-a03b-a9c5ebdaa64f | -10.80457 | -43.93989 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fba8bd20-004f-3ea4-9ea9-92a5e26c5fc5 | -11.59201 | -44.07084 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ce701a5b-4824-3f53-a8d2-fb47fbe8fb5e | -12.91 | -41.84922 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ee0194ea-9a38-3672-a2d4-a756d249e85c | -11.40063 | -44.20033 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4f2463f-51db-3e2b-bf68-a89c6f1b5f18 | -11.39197 | -44.21276 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e51fb14d-fd2d-37f6-b6ca-5ffece92e747 | -10.05288 | -43.86524 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b6edd9b-8207-344e-99a3-cf6204a9f136 | -11.36402 | -45.2794 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94b96c26-9600-3ca3-915c-f863a1be6512 | -11.38509 | -44.21608 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df45f6ae-1df7-3d55-9cc7-1528771f3705 | -10.10349 | -44.63453 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e829896d-b85b-30e3-9dd9-f96a0e57ffa0 | -11.38706 | -44.21525 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 99525354-7467-3c34-b500-2d32c1571e0c | -10.61899 | -42.31039 | 2025-10-17 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 789b3a3c-7858-3e8b-a782-845c6035a3af | -11.09611 | -45.86902 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f452570-81e0-34f3-8618-1c6bd87cef6c | -10.6131 | -45.23922 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51e92c29-6103-3f60-81c2-233c5fd4c0b9 | -11.39707 | -44.21865 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3afee42a-ba64-3c96-9a7b-26bf954c5a45 | -9.15953 | -46.61938 | 2025-10-17 03:30:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d6e6bd7-031d-390d-a8f3-955c8f4fcc57 | -10.65572 | -45.29292 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a1572170-62a0-34bc-b58b-154b25c4da62 | -10.05298 | -43.8722 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2285190-47cb-352f-a607-e95256d1c863 | -10.29638 | -44.04968 | 2025-10-17 03:30:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9eeed8c5-f62d-3bec-94e4-dc151cc96b76 | -14.99286 | -42.64442 | 2025-10-17 03:30:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c00d6659-9fd6-385b-b153-27269f2b803f | -11.39812 | -44.22236 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 57e8a2ed-5337-3ad9-9bc8-3c050f7f9015 | -10.10516 | -44.57813 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ff8174d-d270-3f4f-bdff-5a19cc165eaf | -11.4004 | -44.23365 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 208ebc4b-573b-3ab8-a26a-f0f1ba15b5f7 | -10.50116 | -43.42553 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c44efde-9ece-3c25-b923-5892f108126b | -11.96875 | -46.55997 | 2025-10-17 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4ae03175-9bf0-3a43-a2d1-6949f3302c9a | -11.48767 | -44.17958 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52001353-4149-3e49-a856-1121e3582fa4 | -13.75952 | -43.12329 | 2025-10-17 03:30:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57f4d9e6-c961-3945-a774-23246a59ac1b | -11.5249 | -43.49468 | 2025-10-17 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a42cf86a-f62f-39b9-9b7c-641514952ef7 | -10.65024 | -45.25359 | 2025-10-17 03:30:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d14b128-9190-365f-8085-d9cb9355dbb4 | -11.39019 | -44.22195 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e073376b-cdea-3ddb-a723-b348057fe59b | -10.16096 | -44.54296 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a68ead26-cb04-387f-9901-054dfc33f91a | -10.13122 | -44.54448 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 941068e9-1a64-35a9-98df-0df21407bd3c | -10.13906 | -44.58752 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| acecd8f7-39a3-3fef-a705-4983704204b9 | -11.09487 | -45.87507 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a304e57-bc28-3870-89e1-ab08fd604c83 | -11.4683 | -44.28468 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e09787b9-fa8e-3230-a530-5399f519affb | -11.48232 | -44.20684 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b905b2f1-86c6-3c58-812c-e7ce6cf06508 | -10.505 | -43.40576 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afc00c05-6c1c-3337-97df-5b024ee20955 | -11.47815 | -44.29197 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3b8299f-079f-3af7-9b44-17ef17aee5bb | -11.41286 | -44.21122 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ccf81cf-0995-3fc7-95bc-1dc7359bbdfd | -11.09361 | -45.88123 | 2025-10-17 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80a92f3e-721c-3b76-af25-1b67358e28d6 | -11.58193 | -44.05946 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b556355f-1371-34eb-a204-6067f496878d | -13.82492 | -42.34759 | 2025-10-17 03:30:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5effe7c0-70b9-3776-9547-b669b039b0c7 | -10.052 | -43.86988 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3e89a57-6707-393b-84fa-88ccff007953 | -10.27606 | -44.02496 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd8dc71e-6aed-3b77-a8d8-8d42d080d854 | -12.91851 | -41.83175 | 2025-10-17 03:30:00 | NOAA-20 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ac42d45-bdf1-35c7-a4a1-ce95c22b7623 | -11.49955 | -44.05589 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 536414d1-3459-3c31-ad33-748f1fc16ad7 | -15.17337 | -43.53365 | 2025-10-17 03:30:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0d1b0ae9-9dcc-328a-ac9b-35c77785498b | -11.382 | -44.20941 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43163ed1-dc97-38f9-853d-252d13775a37 | -9.25603 | -44.35535 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e04234ea-5f8e-377a-9094-22b631ecac96 | -11.45297 | -44.22924 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a813623-6be0-3b95-8a4b-cad14364c7ea | -9.69886 | -44.57074 | 2025-10-17 03:30:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fc01635f-79e0-30cf-8e67-460fb09eea96 | -10.50314 | -43.41534 | 2025-10-17 03:30:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e77779c-f0aa-3867-9610-db1264d7c4fe | -11.4024 | -44.19122 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61cb27ea-3aa5-3082-b636-3dba1732747b | -11.57601 | -44.05824 | 2025-10-17 03:30:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9fcf3df8-c9f5-3cc6-884f-b33fcb72cae0 | -11.39331 | -44.14201 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc7c38ad-fef7-3d17-be62-2bf0c771fa5b | -11.39121 | -44.22566 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d58a3a7-1721-316a-89b4-3c2607d3a5d2 | -10.14563 | -44.53715 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ec22193c-dc14-366a-b0a6-137982db6254 | -10.11675 | -44.61925 | 2025-10-17 03:30:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac5720e5-28ea-3d55-8bd8-6ec18074e7ec | -10.26999 | -44.02385 | 2025-10-17 03:30:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b2fd12b-6d29-3a8d-8740-b52fd6aafa18 | -11.39766 | -44.19371 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 201154cf-ba04-36c4-93d9-82fbe19f781b | -11.40994 | -44.21665 | 2025-10-17 03:30:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8955fb83-6b88-35ef-90a2-5a273378a38e | -11.49867 | -44.06036 | 2025-10-17 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 915d06d2-6bc6-3647-802d-56fa59f27e53 | -13.50831 | -41.00156 | 2025-10-17 03:30:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eb54071e-5e32-3bae-ac65-a3ef43d01ebf | -10.61765 | -42.31746 | 2025-10-17 03:30:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01c9865b-5063-38e4-b725-47095bdda8a4 | -12.99935 | -43.22277 | 2025-10-17 03:30:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3c9c8564-29d6-346f-99a0-f956be138d60 | -13.92466 | -45.62396 | 2025-10-17 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README32.md)
