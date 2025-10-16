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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78e55cc2-b55c-3e13-94f5-8719d211c062 | -4.37429 | -43.4032 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1faad5aa-0e7c-3b79-85c6-8400f0058e43 | -10.69848 | -44.42976 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9360fa12-ef09-35c3-bf31-2ac51f47c598 | -9.68135 | -44.5019 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 1056b320-0521-3563-99a5-17b21b5dd588 | -10.85444 | -43.64294 | 2025-10-16 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6414338d-5fde-3b65-a286-ab12fdce95d0 | -6.40554 | -42.55363 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4e3d4d35-18e8-392b-af41-11cc9b880f77 | -6.06602 | -41.9224 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6bfb7dae-0158-31b3-8d62-b6171c3c3802 | -5.89233 | -42.83559 | 2025-10-16 03:47:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1f0101d3-3eb8-3564-82c5-f2156ef93eb6 | -10.82078 | -43.9412 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45eaabab-defe-318b-b51d-abbfd027d350 | -5.92113 | -44.72987 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3daad0ce-d850-3718-ab3b-b3c66241c6e8 | -3.2261 | -43.45934 | 2025-10-16 03:47:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cd1f16c0-26f8-30e4-b12c-dfa90a819f3a | -9.71476 | -44.52071 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd0c1779-df05-3824-91b8-48e213381fa7 | -5.67109 | -45.10728 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4cfe022-071b-3934-8bd9-51bc35581f66 | -6.45179 | -43.3837 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26a3244c-8cdb-328e-87a3-fb2d7186795a | -6.22502 | -41.55127 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2edf620d-2499-3e2d-98c1-91992333f36d | -4.10472 | -48.02157 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6aee6a4f-646f-380c-9c9b-a2a97e09e86a | -4.92702 | -41.54738 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5df2a94c-1d10-3619-beb4-f356992e66ed | -9.22231 | -48.59057 | 2025-10-16 03:47:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d92f8225-d259-3882-ad60-edc4c2b9e530 | -3.59441 | -48.88108 | 2025-10-16 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 299f2026-ef86-3eb6-9844-9e8ec8a95b28 | -4.64374 | -43.13676 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04fde2f8-c8c1-3be3-b2e1-3e979f33bdd1 | -4.10368 | -48.02756 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 0f53913c-ae01-36e4-b84c-a21d87516e2b | -5.60036 | -47.49881 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4d7ed18-723d-3603-920a-9c0bb0e471df | -4.95526 | -45.09957 | 2025-10-16 03:47:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e4c3f267-55a4-3ea3-915d-d732c0ea8f0d | -3.67565 | -47.63584 | 2025-10-16 03:47:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 206d8d11-500d-385f-b5af-65bb4272b2da | -11.35676 | -45.27117 | 2025-10-16 03:47:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fee133e4-97d6-3521-b1f5-41c6230301b4 | -4.10905 | -48.03464 | 2025-10-16 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d788d62f-49b9-3535-9dcb-1d8b70e1c37f | -5.89799 | -44.2715 | 2025-10-16 03:47:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 232fe11b-7d00-3acd-b2df-342fa2d8c1f2 | -5.65169 | -45.9711 | 2025-10-16 03:47:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f6a257-3cc6-3ad3-b3b9-694b6a4c29b3 | -9.688 | -44.51834 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f5d6a233-5b63-3f06-8cd4-baa09e646318 | -12.77433 | -43.59775 | 2025-10-16 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c8e701b-a5e4-3f01-8da0-73760b8c5ac7 | -10.50618 | -43.36953 | 2025-10-16 03:47:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca3ee023-e85e-3dd1-8230-3cbc30110ac5 | -3.2309 | -43.46021 | 2025-10-16 03:47:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fb0ea0a-e8a6-3edb-9a1c-c3e5da9c4413 | -12.68479 | -44.39985 | 2025-10-16 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dda0579d-6b61-3e1f-b67d-534569775e07 | -12.73867 | -42.99798 | 2025-10-16 03:47:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fcddf744-6c64-392a-82ca-2a15c98e95dd | -6.0651 | -41.90281 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| db9334e9-2d45-3523-8850-f7583c0f57be | -3.61084 | -41.58221 | 2025-10-16 03:47:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3c0de80-669d-373a-b4c7-6b4b59e9043a | -5.72526 | -44.52223 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0acc3894-4e28-32e7-b790-345aa3f26244 | -10.80577 | -44.30502 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 77387b5d-5a63-3a4a-8705-497877678557 | -10.03464 | -43.83405 | 2025-10-16 03:47:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2dcfefb-99f2-3c78-818a-7a3a9a597b11 | -5.8798 | -43.89159 | 2025-10-16 03:47:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd92f1bd-a7c3-3955-b46b-c5596f689008 | -5.46889 | -42.93366 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 2c8e2662-39a2-3a1b-9d59-b5b501422d73 | -5.57031 | -41.31791 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0de505c2-1ee4-3be8-974e-2cc2f88cb9d6 | -10.65488 | -45.25447 | 2025-10-16 03:47:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 024c8122-4c23-3d92-bdc3-ad31c2931c6f | -12.83518 | -43.81694 | 2025-10-16 03:47:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 33276fd4-aa3c-3194-ad97-5cb7c8d23b37 | -10.13035 | -44.57043 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 18d7926b-be16-3f85-b434-ca294aa8c279 | -6.56355 | -42.97662 | 2025-10-16 03:47:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87209870-ea6e-3767-993d-04791c85dba3 | -5.1009 | -44.94706 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 5addd2b5-dfbb-3b2b-a070-8dd7367df23a | -5.41078 | -40.89407 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b94d5d9-b4cf-3d9d-9819-f412333d31b6 | -6.15894 | -40.91673 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| e7c811ac-09da-3a82-85cb-5d6190b428b9 | -4.91754 | -41.55349 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 914fef0a-442f-357a-a117-7aa9de3b1919 | -12.48115 | -45.48202 | 2025-10-16 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7554678c-f31d-3771-8401-d5825b2a9a22 | -5.40081 | -41.15312 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2587d606-3f17-3ff7-a252-671cc7a6d745 | -5.84883 | -44.67327 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fcfef04-8f9d-3dc3-8809-def0d5cfb868 | -5.43221 | -40.98464 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4749783f-4498-3458-a20a-75381d3ac56e | -5.42807 | -40.66837 | 2025-10-16 03:47:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3e6891ed-8b06-3710-9088-9bc378955822 | -7.65548 | -34.98743 | 2025-10-16 03:47:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 692c55ce-3eac-3e5c-8a6b-ed973d4d4442 | -10.05215 | -43.83596 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 73a74aac-222c-3e23-bbb1-f279c5f46026 | -11.57466 | -48.56382 | 2025-10-16 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5199c48f-d7e7-3bd6-871e-c020047010ab | -3.26775 | -45.84327 | 2025-10-16 03:47:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fb920c6-94f6-384e-91be-f91fd91ea7c7 | -6.13713 | -41.77616 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 865b4eb3-a45a-38a1-900c-9bd2b138ba66 | -5.45469 | -41.016 | 2025-10-16 03:47:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3ba2833b-1789-3332-9b46-f9668fd0200f | -11.00409 | -49.58254 | 2025-10-16 03:47:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58a3bed5-f53a-3cab-a57f-4db9535ebf91 | -5.91664 | -44.726 | 2025-10-16 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 51482bb7-925a-352b-ac63-905b52b3137e | -5.67733 | -45.10197 | 2025-10-16 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a473bf52-37de-31c9-b9d3-1d95342dad35 | -12.22376 | -43.30235 | 2025-10-16 03:47:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23c2d736-17cc-3132-97d0-46afc1a7d38f | -6.45785 | -35.25166 | 2025-10-16 03:47:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4e802cc-9349-3937-8959-95d0e438fbd7 | -4.39004 | -43.3955 | 2025-10-16 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 35b4f771-190c-3788-b400-0ee33985fe69 | -4.91691 | -41.55721 | 2025-10-16 03:47:00 | NOAA-20 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b96b18cd-e8c4-3079-a930-42d747280bd2 | -12.03223 | -47.66059 | 2025-10-16 03:47:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e834c843-e9d1-3392-be35-df467731677a | -10.85292 | -43.64014 | 2025-10-16 03:47:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3b7bbcd-d536-30ec-9ba4-a69f0b3ccfab | -4.35492 | -45.53584 | 2025-10-16 03:47:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6dccec8-f2a1-352e-97d2-e41a258382f8 | -6.19254 | -44.10476 | 2025-10-16 03:47:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df3009be-9c20-3c25-896f-4a79eb71addd | -10.05797 | -43.85657 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95230e30-700a-3ebb-8af3-cad658281401 | -6.06418 | -44.31195 | 2025-10-16 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afe263a5-df0b-3797-8dc5-1f2c6f0fb434 | -10.83839 | -43.99422 | 2025-10-16 03:47:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d290ff99-04ff-37a7-8fba-bcfffcbf31d5 | -6.10419 | -40.88757 | 2025-10-16 03:47:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 59e92e91-1a16-3517-a11a-2f0a999bb6bf | -6.51846 | -42.19389 | 2025-10-16 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 896db36b-e08b-37fd-9ca2-c01f08bf4967 | -11.58158 | -44.06549 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c56c6760-a8b4-3798-ab91-5b907ffa7fed | -4.83084 | -41.47454 | 2025-10-16 03:47:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5cfce885-ed53-3e3f-90ea-b96628911dde | -4.63984 | -43.12846 | 2025-10-16 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c264cb2d-7ba3-3c77-b574-b833a9b94389 | -6.39822 | -42.51912 | 2025-10-16 03:47:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 84753f0c-bad0-3b7e-a5f6-65154595e244 | -6.64491 | -41.73461 | 2025-10-16 03:47:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d5fc357-7bd0-329b-91e4-470b48520e4a | -5.24732 | -41.03009 | 2025-10-16 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 917f8b4a-e707-346a-b703-a89f8b51095a | -9.36613 | -46.96293 | 2025-10-16 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b30426fb-a985-386b-bb06-cffc02465171 | -5.42102 | -44.2375 | 2025-10-16 03:47:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b1ab2d6-6f50-3f06-b972-6e8372d92c1f | -6.0365 | -41.9331 | 2025-10-16 03:47:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a402845b-eccb-3017-b57e-47cecb9e88a6 | -12.67341 | -43.4341 | 2025-10-16 03:47:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e3ac6043-f657-39f6-977f-ca31ceb81b31 | -6.14817 | -41.78562 | 2025-10-16 03:47:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1edcabf-5252-395f-9a3e-4d364b4d3ef5 | -10.17875 | -40.95065 | 2025-10-16 03:47:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 67b95440-527d-3dd8-8c96-ceaff6a80e42 | -9.7112 | -44.52243 | 2025-10-16 03:47:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00c6f61d-de1c-3dfe-9a10-b0430d10c83a | -12.48201 | -45.48388 | 2025-10-16 03:47:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b91b089-3d93-35c0-a38b-36774de99d3f | -10.30451 | -43.9954 | 2025-10-16 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e024a35a-50ac-3410-898f-b9d9006aa3d2 | -12.63372 | -44.23293 | 2025-10-16 03:47:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38ef531d-acdc-39f5-836c-62763fde1fe9 | -5.44272 | -44.2743 | 2025-10-16 03:47:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16081a5a-e98e-327f-8ad1-a204fc5a29e9 | -5.23923 | -45.63915 | 2025-10-16 03:47:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abf34cd7-b16c-30a8-9159-31b7eac1ebda | -5.43475 | -42.90199 | 2025-10-16 03:47:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d18e2e6e-5196-3f5f-868c-c8f1267dbbe8 | -4.8376 | -42.79673 | 2025-10-16 03:47:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8b5ca651-9a2d-369d-aaa7-4be28d7f3de1 | -11.58207 | -44.08772 | 2025-10-16 03:47:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f390d0a8-b873-35ed-8fb4-3b5e9d230132 | -11.49236 | -44.10747 | 2025-10-16 03:47:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c19a8c3-9e60-3627-8724-527add79c898 | -10.14065 | -44.54514 | 2025-10-16 03:47:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0ef3e6f8-aa95-33c5-8561-8903d1c0630e | -9.08808 | -47.9511 | 2025-10-16 03:47:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |


[Clique aqui para ver as próximas entradas](README31.md)
