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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4908f473-8626-3832-ac81-9bff525fbfca | -11.74766 | -48.18899 | 2025-07-31 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c89c36af-4ee3-3f1d-83d7-f2c156f0722a | -9.39589 | -45.4963 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2bad8e73-6dd4-3b3a-a1c4-ec15cc023ce9 | -9.39911 | -45.49644 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d936b91a-ff74-3f38-850f-ba33fb955382 | -13.50672 | -45.64493 | 2025-07-31 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61256711-f13e-3fcb-991c-a36f5e5032d6 | -9.39438 | -45.49184 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ea6b4e78-e5bf-31ce-95eb-adce185e3bb1 | -9.01531 | -47.97389 | 2025-07-31 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 303f0695-02d2-3645-b354-ac92590bfc06 | -11.02562 | -43.23801 | 2025-07-31 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c5da8639-2e09-3837-8dcd-6e4740c07154 | -9.43414 | -43.20756 | 2025-07-31 03:45:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1ec29eb8-5a21-320f-a18e-826c8174b12c | -11.74154 | -48.18778 | 2025-07-31 03:45:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9fa1f453-7675-3afa-86be-90dedbeb1fae | -12.55918 | -44.72156 | 2025-07-31 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c2fd0c1b-385b-3127-b508-62591484c3d6 | -9.38712 | -45.50117 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76bd4789-84e6-3ce6-9d71-cdbdba406129 | -13.54066 | -40.69714 | 2025-07-31 03:45:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d4c61884-b043-32ba-8f06-80ef637fe8b1 | -8.92102 | -47.33702 | 2025-07-31 03:45:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9b1cae0-6061-386d-8184-886b72d8028e | -10.63741 | -45.23693 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d40018aa-2782-386b-b50d-864afd97136a | -12.61864 | -48.09355 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f8cf170-a7e9-3fbf-8594-be9750119324 | -8.80427 | -45.64166 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fa44810-1055-3612-9afd-7354761ef21d | -7.59183 | -44.81059 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b3a56af-8636-3e7a-b026-ed795ef5f4fa | -7.34095 | -44.64483 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfc952e3-8190-3662-a900-a30858b54da0 | -8.05952 | -43.11331 | 2025-07-31 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 811005a1-2d43-3b23-b23f-bd4a79b3c132 | -8.17824 | -45.01291 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf7097a5-2a2d-378a-9872-cfb0710cbeb5 | -12.55435 | -44.72064 | 2025-07-31 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9d41b4b0-1e46-3dec-90ba-11ade64d0b09 | -7.5811 | -44.81809 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 417bb167-e745-3edf-a882-d5726fa139b3 | -8.18052 | -45.03094 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9275d571-352d-37f4-b292-705c4000ad02 | -10.6438 | -45.23154 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cb7c781-12dd-3ee2-a7c4-b5d24c22b4c9 | -8.16633 | -45.01798 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09ecde07-108d-3306-a1fa-1084082ba9f1 | -8.16695 | -45.01452 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fceafaf2-2d31-3dff-bef5-3947fadfdf69 | -9.63909 | -43.85319 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f8959d10-9955-360d-824e-9eea84fe119e | -13.6767 | -44.22274 | 2025-07-31 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2908701-8f59-33f0-ac74-e3bf6a20217a | -7.57995 | -44.8247 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 44094bde-bb2c-323a-b615-7495a38f7cfb | -8.87857 | -44.79001 | 2025-07-31 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb5ead4c-c8f5-3e53-ae73-afa8089fcca7 | -10.61106 | -43.30717 | 2025-07-31 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d2d889ed-17b6-3555-a6e2-79db778cf28a | -7.31925 | -44.67479 | 2025-07-31 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ac2230d-3df3-3f19-ab02-a41035ac51fc | -9.39501 | -45.4884 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f81f6535-0a7b-3866-aa54-7c83cd539a19 | -12.76111 | -44.4082 | 2025-07-31 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 447bd9f7-7cc4-35dd-a721-0e0b4f9d5752 | -10.22201 | -47.9861 | 2025-07-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d94dd34-d04e-3eac-91cf-ba551a35061d | -7.21025 | -44.7099 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08e8b94e-d66a-3cb8-ad12-5f58747b7c9c | -10.60517 | -45.25989 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3071a13b-ddbe-3521-9ff9-086ccf78a8ad | -8.1729 | -45.01199 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 400d6dd9-3291-35dd-95e5-7873408b54e9 | -8.95398 | -46.7494 | 2025-07-31 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dd5a2e2-2362-3281-9b72-452e7806439d | -11.52432 | -44.28354 | 2025-07-31 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 71be9653-9857-32d1-bc2a-e4d67a94a37d | -7.31981 | -44.67172 | 2025-07-31 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| efccdf2d-1694-328a-ba27-0f56fb231513 | -10.61556 | -45.26178 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a445742-8338-3308-8556-b54e324831ba | -8.16756 | -45.01109 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c649415-13bb-3172-9af9-01326895c4fe | -10.21346 | -47.9872 | 2025-07-31 03:45:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd210193-5b51-35bb-a7de-c70b3540d291 | -9.85041 | -44.70792 | 2025-07-31 03:45:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52f5f65e-6a1f-3ea3-b7cb-626635ec3c29 | -12.62572 | -48.08941 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| ffd500e7-ee8f-3550-8a8d-9f08ac5e99cc | -8.80491 | -45.63811 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7174a90b-9072-3fd8-8bd2-536660bf5ead | -9.59694 | -43.84291 | 2025-07-31 03:45:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 271fc1e8-b29d-3ee2-a6bc-0a218938520d | -7.49241 | -43.93687 | 2025-07-31 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1da4cc1e-8369-3d41-9dd6-93dcf06af119 | -13.52374 | -45.69233 | 2025-07-31 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbbbb308-79ef-30df-ae51-6568fdff2187 | -7.58475 | -44.81932 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 539616fe-a640-3db2-ae70-d0ecf739ea3e | -13.06091 | -47.39468 | 2025-07-31 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cadf635-3734-3eb4-be10-065729ec6b39 | -10.9355 | -44.50478 | 2025-07-31 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5979f98-abd3-3213-a3c0-8b5d4770c8a9 | -13.54513 | -44.14252 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 509a56e5-6c84-3e87-ada9-804b96f358a9 | -8.16097 | -45.01719 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b128b5e-14cd-354b-aee4-1bb9a0ea9c86 | -11.98389 | -46.6741 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8e40b363-e4f0-37bb-8c40-fb75e008c5f2 | -14.39124 | -44.37559 | 2025-07-31 03:45:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84399d53-8047-3f23-a938-c328464615ed | -12.55334 | -44.72607 | 2025-07-31 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a8522905-4fbd-32b1-b474-39dd5a99d281 | -11.91939 | -44.54984 | 2025-07-31 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a64ac697-a52f-3758-a1cd-fa87d7bd6172 | -12.76013 | -44.41336 | 2025-07-31 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 99078f47-2a00-39e3-97eb-a4d782e42301 | -12.63166 | -48.09084 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d7fab224-e4fc-3a1f-8ce8-6e34e1f955ab | -9.39655 | -45.49285 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 61291552-03fd-397b-b473-0ddd6605bedc | -13.67576 | -44.2277 | 2025-07-31 03:45:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd15690a-6948-3f42-b287-069e13a80958 | -11.53965 | -44.28092 | 2025-07-31 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a4c0b570-efb2-3529-acea-aaffe4cb38ff | -10.61497 | -45.26495 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6d86658-3964-3c30-8702-8de7bf95f7d9 | -12.62455 | -48.09517 | 2025-07-31 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b457398c-645f-3409-948d-9ecca3468db9 | -8.44507 | -45.1482 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae5630fc-4ac9-375a-84c2-53a200902f55 | -13.52878 | -45.69344 | 2025-07-31 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dd1f512-4a5b-361d-8d2c-3751066289ea | -8.05482 | -43.1125 | 2025-07-31 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| c0d50a16-6063-3693-ae9a-b9aab386cc2d | -10.61792 | -45.24895 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0728084-c4c3-3a02-91d9-11e101b44972 | -10.6432 | -45.23468 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 967b3ec3-6556-3918-9126-3e04970e9ed4 | -7.58052 | -44.8214 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0f87a6a7-850c-3d44-b540-fd16aeeef49c | -12.76408 | -44.41183 | 2025-07-31 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 03d8cbb2-3047-3e61-96e2-7f2300a6b9f7 | -12.76314 | -44.41702 | 2025-07-31 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| a74544fc-fa2c-3b4c-a7a8-d96eaadf55d2 | -11.9204 | -44.5444 | 2025-07-31 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7c9f957-b2e7-33a3-a0b8-7f68d4dcbd65 | -8.16571 | -45.02143 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c0c015c-06c3-311d-9d0f-660a791536a3 | -7.12629 | -44.89967 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0dee25e-a7b7-33a4-a6ca-74817ebae8fb | -11.13017 | -48.64486 | 2025-07-31 03:45:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df32f36a-a3e1-3606-823c-be353385ef4b | -9.39974 | -45.49297 | 2025-07-31 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 905a2192-48ab-3091-87c9-8210de74bdbb | -11.53688 | -44.24221 | 2025-07-31 03:45:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a6573785-25c8-3a5b-97d7-fadfeb83e5c0 | -8.0604 | -43.1083 | 2025-07-31 03:45:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 10eaeae3-0e80-376b-98b9-20dbb9149968 | -7.58814 | -44.8092 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| edb83196-3f45-3d30-9899-668fe78db949 | -11.13123 | -48.63952 | 2025-07-31 03:45:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbed6958-4cc8-3d55-a7b5-fe72a33b75a4 | -7.57943 | -44.81845 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7e7c3f94-a27a-3fe3-9409-a7a0a85182c1 | -11.97253 | -46.67952 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb87ce6-82e6-3b90-a634-52325b81500d | -7.587 | -44.81567 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5e412557-dc60-3808-8dac-30b146023e31 | -7.30412 | -44.39405 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8a39e0a-3585-3a2b-8ca6-4369447e6555 | -10.51982 | -42.55052 | 2025-07-31 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 268a5795-af8d-346a-9bab-aeb0d6e5fd5a | -8.16159 | -45.01369 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27b36b56-6ad5-3efc-9a0c-f84b515a6f24 | -7.58758 | -44.8124 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9e2124e3-d7c0-3eac-99c4-8f451b03f448 | -12.75936 | -44.41094 | 2025-07-31 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d69bee23-f180-3e7a-8707-49b05cdee8e6 | -8.44567 | -45.14492 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10de78c2-cdbf-394b-b44f-584296342d11 | -11.98982 | -46.67947 | 2025-07-31 03:45:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c53651f-fdd3-371a-9f65-3b63128cc5f7 | -7.12831 | -44.90596 | 2025-07-31 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1b9f607-fb1f-3c56-93b4-ddceac5588c8 | -8.16222 | -45.01022 | 2025-07-31 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39eadd16-f483-3542-b40e-dc6225ccbf79 | -7.59125 | -44.81378 | 2025-07-31 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c81c2d78-473b-3b06-a437-0b6ad4e91616 | -10.6386 | -45.2307 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d24a5e55-e0b7-35b5-b0f7-c68df220f3bf | -10.70232 | -48.8682 | 2025-07-31 03:45:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cfb6a03-3ce2-3f41-8cdd-89c0bcd6f63e | -9.01434 | -47.97898 | 2025-07-31 03:45:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 334a9c88-b688-34ef-87b3-0d713b43aa6d | -10.64793 | -45.23143 | 2025-07-31 03:45:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
