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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb661cd-9528-3071-81ff-4be471c0cb01 | -3.29957 | -49.19341 | 2025-07-30 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87e41194-47fb-3643-bc2e-a30dce3ffec2 | -3.88857 | -41.03212 | 2025-07-30 04:00:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 941b627b-92f6-3a08-85e3-91d798e0b4f3 | -4.24742 | -40.39845 | 2025-07-30 04:00:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 42768c2b-cf34-32cb-a438-0bd707a10437 | -3.5097 | -43.2512 | 2025-07-30 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c8d8fd3-5ca7-307b-9b00-115d95567904 | -2.5176 | -47.71226 | 2025-07-30 04:00:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7faabf93-7eea-38e1-98ea-16267ebeb5bc | -3.82384 | -41.57122 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4f4e169f-d9f3-3e60-a656-57cd95b36d00 | -3.51344 | -43.25179 | 2025-07-30 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53555005-2bd9-3812-a0d8-c149d0767287 | -3.18883 | -48.80682 | 2025-07-30 04:00:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61db3ee8-de6f-3ab0-84f6-fe6dc84b9d2a | -4.38761 | -41.90907 | 2025-07-30 04:00:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16b0a8ea-c751-3241-bbd2-331578c1c871 | -3.50898 | -43.25566 | 2025-07-30 04:00:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84535409-4f90-3255-b4d7-1bb38a58e5b7 | -3.11326 | -47.01167 | 2025-07-30 04:00:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aff5a825-ed04-3be2-9c49-430735a1efa5 | -3.58821 | -47.51961 | 2025-07-30 04:00:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a59e09e-6d93-313e-be0a-8714f7d69851 | -3.95279 | -41.48825 | 2025-07-30 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 706f1f3c-92ab-3ffe-9333-3e6f7cdc1b66 | -3.888 | -41.03571 | 2025-07-30 04:00:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fdd480d0-862f-317d-b458-50d7efb0df70 | -9.57176 | -43.88291 | 2025-07-30 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6630247d-5647-3e1c-82d0-f0f1e6f93cab | -10.92522 | -44.19168 | 2025-07-30 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdc71fb7-4afb-3ac4-a1d7-065e3460ec1a | -8.01639 | -47.67793 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff05e53a-894b-3a42-a0ce-dfcb39984370 | -6.28277 | -39.89095 | 2025-07-30 04:02:00 | NOAA-21 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f78e121d-416e-3391-b2aa-ca66cef8d288 | -4.84991 | -42.99504 | 2025-07-30 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be60c345-3cd2-3598-a861-ae4164ea5300 | -9.04932 | -45.06826 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e386ad2a-b433-3eb2-b753-4512f00a70be | -11.46764 | -45.11681 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f7259119-cf71-3f44-a7f8-1665b8883f03 | -6.95026 | -44.23013 | 2025-07-30 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6efa51c1-3d44-3a71-ab05-9eda258abeb4 | -8.02019 | -47.68353 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22c3f713-905b-306f-b8d4-27cd029af1ef | -6.95404 | -44.2307 | 2025-07-30 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32fe1e09-600c-3927-9943-49ab41ba6abc | -7.85531 | -46.73226 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f539829e-c74b-35c1-8b66-a8d904ebd654 | -6.41811 | -53.31485 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cd149a2-9d9a-3bf7-aa6f-fa310beff0fc | -9.04385 | -45.07736 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ba8f464-4579-3390-9ba3-ba05d8e0fe41 | -10.93663 | -45.77926 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16d6d72c-9486-3485-a4ba-894aa1cfef80 | -5.48321 | -42.15277 | 2025-07-30 04:02:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3b3a1de8-bb40-3efd-aeff-df73bb670e1b | -9.1824 | -48.84738 | 2025-07-30 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e81e31f2-4ae8-3f5f-9647-f67a6a2ca96f | -10.09597 | -46.97157 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb97b7ad-f785-376f-866d-e8630b614ac9 | -11.4602 | -45.11544 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7fbf62a0-b78a-3b8b-8a41-693d5a760663 | -5.18919 | -44.9557 | 2025-07-30 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f20943b4-82ee-345b-93f9-43375196e47a | -7.79027 | -37.59981 | 2025-07-30 04:02:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 452280ab-49fd-3616-92e6-c95c77aa043c | -5.82153 | -46.35166 | 2025-07-30 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f452214a-257e-3da9-8182-9e7db2616919 | -9.19445 | -43.15369 | 2025-07-30 04:02:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0cabf620-52f9-3b5c-8aed-9a12bbcfa21d | -9.26254 | -50.22586 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76a7111a-94f7-3b4d-ba9f-bb0194cdc7c1 | -5.68351 | -43.68373 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93c0042b-6666-377d-97ea-5e2045149a4b | -10.51408 | -44.89112 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 382ea298-9f5f-3a55-8879-b7eb66a0e89c | -7.15113 | -44.04595 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6db4004-ae5f-3471-8cb4-f716275e767d | -10.7046 | -48.86239 | 2025-07-30 04:02:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4d2bb40-0466-309d-8876-d3f23eb2349b | -5.83161 | -44.04012 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7851782-d5bf-3086-96a4-4848a1c03343 | -4.92483 | -45.09012 | 2025-07-30 04:02:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee5a072f-5b0c-3f3e-8c05-ca6bb8a14389 | -11.53724 | -44.26444 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8bff626-fb60-35e6-925a-f2b7f8ad871a | -12.36521 | -40.54262 | 2025-07-30 04:02:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68b415f4-af58-357d-891a-cfc05abcbdd2 | -11.56357 | -44.26044 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e420e2ad-260c-3491-8b3a-5435b81731b4 | -9.15943 | -49.852 | 2025-07-30 04:02:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d64c12d7-56e0-3896-b025-dbc2996a927b | -9.39707 | -45.49368 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4821e476-33d7-3866-b5cd-31440c17a23e | -6.25358 | -46.11868 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aec02435-d0a6-35da-a01e-e03fc680b132 | -10.97612 | -47.40209 | 2025-07-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9b8f62e-196d-39b7-93a3-e7c8b3b2cad9 | -8.95873 | -46.73663 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30e3d82f-7ffd-33a8-a807-50ffdab471c1 | -6.25786 | -46.11954 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1723da9b-4531-36ef-9c3a-d967ecb64f30 | -7.77574 | -45.00009 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| cc63ad71-4f84-39c4-9f6a-f17a92ce8995 | -7.30827 | -44.69149 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6e6906a-c358-3581-aa16-f73b395d39ea | -7.76963 | -45.86579 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bdd27e5-cbe9-3ea3-b8bf-020e71d3d86c | -9.63878 | -43.84694 | 2025-07-30 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f6beba74-6bdd-35c8-a586-c122fdd7fba7 | -7.77876 | -45.00888 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8f66738-af9c-3d3b-815e-4cb5e44e1380 | -12.06539 | -40.00788 | 2025-07-30 04:02:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5c274941-cd91-3168-b53f-1fbcf7d3f276 | -10.71039 | -48.85793 | 2025-07-30 04:02:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3d04f94-bf7c-3e7c-95f7-78d4e6713ec0 | -6.47994 | -41.63319 | 2025-07-30 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f4181728-db0b-30e7-b7c2-022653cf92f1 | -5.83236 | -44.03548 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a3a0b0a-a5de-3abc-9140-2d51108f9207 | -9.63212 | -48.54856 | 2025-07-30 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dacd34e5-be0b-3784-95e3-5b1da4f2d0ae | -10.61023 | -45.23733 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f3c95859-e69b-3619-9737-c9caa6865e2f | -8.95445 | -46.73587 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 23d975c4-18c8-3810-a7e9-10a15eb53914 | -9.04466 | -45.07249 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60d7c409-c917-3ca2-b471-77d434d331a7 | -11.81318 | -44.26737 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86a39fa1-aa63-3b2d-9cab-dda9520178bc | -7.77375 | -45.86648 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d6af318-c1c2-39a0-9d3c-36b5fa66525e | -9.01995 | -47.97694 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c27091f2-2b29-36e2-b8c6-8416e094462e | -7.77883 | -45.00573 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf72191a-7053-3fbc-931b-d1b78a427d05 | -5.42255 | -44.00124 | 2025-07-30 04:02:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd948a03-8ebe-37f7-b56e-8a20af5d4c09 | -10.49757 | -44.86698 | 2025-07-30 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ceb87ee1-0527-369a-948d-8e2f4ffd5d1b | -10.60942 | -45.24207 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 19bb28b0-785e-346f-87ed-9ce869ad8d36 | -4.59143 | -47.97902 | 2025-07-30 04:02:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfe82ef4-871f-333e-94ab-09ad3c83a8ee | -5.76054 | -43.90319 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4ca697a-2fcd-30cf-b2c9-3e2d43898fba | -8.95733 | -46.74474 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0ff1d9e8-4ad0-3876-903c-623153d73689 | -11.47214 | -45.11295 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a9e901e-ba1d-3d4a-873d-60df2442070b | -7.35343 | -43.7708 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b87aaa1a-afdf-3f35-9ded-8764175c4d02 | -8.41874 | -45.68784 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a49383eb-a838-3730-bc0c-30c013e14de9 | -7.1534 | -44.05547 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9228b610-2f5e-37e2-aa64-103b266c61ef | -6.91294 | -38.56351 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 259a65f7-24e2-361d-b27d-866b3692edc8 | -7.94357 | -44.08191 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9c68383-d35f-34a7-9ccf-6574bb539545 | -9.14951 | -49.84673 | 2025-07-30 04:02:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f7e9dce5-d2da-3902-9a52-618335c207c3 | -6.62406 | -44.03728 | 2025-07-30 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 837353d0-70dc-3870-9179-cf85b23dd171 | -9.19097 | -43.15313 | 2025-07-30 04:02:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 880db9ae-52db-3e29-99de-161c3ce0d8e2 | -6.16885 | -44.41984 | 2025-07-30 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1848957-e686-3e3d-af2f-8ba4fbf41725 | -7.15485 | -44.04657 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cb473f0c-164e-347d-84bd-eec362942a71 | -7.05357 | -44.95913 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e5fcd34-b84f-30a7-bf2d-27c8023b97fd | -8.88651 | -47.33857 | 2025-07-30 04:02:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15b3568e-8024-3266-9441-b5fb7058c742 | -7.85458 | -46.7365 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| acac94be-ff09-3598-a34c-5387e9d1d71a | -9.33268 | -37.98018 | 2025-07-30 04:02:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40176ca6-1507-36a5-b4d0-e2a9fe49c728 | -11.46219 | -45.11716 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 149c5c23-5f64-383f-a340-48d12b4b5281 | -7.15184 | -44.04158 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07b80641-7ce3-3509-a725-93759aa9331f | -10.69988 | -48.86475 | 2025-07-30 04:02:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8b3a2484-9e13-30d1-9504-8b236f490651 | -7.58822 | -44.81775 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90329b30-f912-3899-934b-6e79cac137a7 | -11.53437 | -44.25972 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f499274-e3c3-39cd-82bc-2ffbf5c65f40 | -6.71537 | -44.35687 | 2025-07-30 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1be36448-f680-338b-9a29-bc9c37c1243f | -11.46313 | -45.12069 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4690c712-cf64-381d-83b1-705aa2143e8f | -10.69979 | -48.86155 | 2025-07-30 04:02:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 942ffc7b-a459-3f12-9e7b-f16aedcc5288 | -9.04546 | -45.06771 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50b41bdb-05f7-312c-a688-36a2060879c2 | -7.35851 | -43.76284 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
