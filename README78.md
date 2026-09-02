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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1259f611-e404-3022-9d93-47d0b82f3e84 | -11.0437 | -49.6635 | 2026-09-02 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3bce2fa4-05cd-34d5-a3fc-d343545bb4f6 | -1.5805 | -47.7462 | 2026-09-02 14:20:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| be655f0e-921c-3e54-b9ac-8c11deec8efe | -10.8815 | -45.3764 | 2026-09-02 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 983d8633-32dc-3d72-bcf4-90eb45806b3c | -10.8046 | -50.5046 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0acbc27d-9b06-3b3b-8a16-c6fafb102b49 | -6.3892 | -45.489 | 2026-09-02 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ef8ee37e-cccf-3b13-9a5d-df3a172b530e | -6.93 | -45.7157 | 2026-09-02 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 68787a9b-0201-3929-80af-2b93d7b5ee81 | -8.7613 | -62.5869 | 2026-09-02 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 139.9 |
| a3598f8c-982a-3105-a05a-dd13c315cbbf | -7.6149 | -44.8833 | 2026-09-02 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cf4e68cf-2dbc-3f0a-8cbb-634ad2978c34 | -3.2361 | -61.217 | 2026-09-02 14:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a73dc1bb-10af-3662-8e51-127b46dafd56 | -3.6215 | -60.566 | 2026-09-02 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 31c150b3-bb07-3eb1-a002-c83a70ff3a7a | -10.8425 | -50.5005 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1f9aeef9-bb6f-3a4b-89a4-363b9da37bf8 | -17.0878 | -56.8534 | 2026-09-02 14:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.1 |
| b90369f8-142a-3c05-a5cc-5bbc9d359dc7 | -6.9514 | -59.0666 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 49d8e714-4d13-3847-9449-b83c14a19966 | -11.5086 | -50.3204 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 39dda2b5-8646-30ef-94a2-4b7a7395c279 | -6.8568 | -59.4757 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7b92f3ef-5d9f-309f-956d-07706ebf2871 | -11.3388 | -45.4054 | 2026-09-02 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| a96a0de9-b381-3b15-826f-aaab561b9e82 | -1.0182 | -53.7189 | 2026-09-02 14:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| f24c6114-b661-3200-a1d7-8d2cdb81b68f | -7.2255 | -42.7616 | 2026-09-02 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| fcebb03d-da75-3449-ae76-ad3e59d39840 | -10.4148 | -49.9683 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 814504de-2044-36bb-b70f-750db5fbd793 | -10.6967 | -46.2193 | 2026-09-02 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0f8075fe-27c5-395b-923e-615f92eea43b | -6.7832 | -59.4401 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 89328641-8505-30c6-b468-1d301d344c0b | -13.9853 | -58.6919 | 2026-09-02 14:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 4c183b04-4d21-340e-abff-09df89d9398b | -9.1719 | -59.5017 | 2026-09-02 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6d81798a-c1b0-35af-aaa1-c8db8a3a3e51 | -11.131 | -51.5517 | 2026-09-02 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9bdc77ae-aab9-3031-a96f-370a98e88d4e | -1.5806 | -47.7245 | 2026-09-02 14:20:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 5406cd58-685f-3fa3-84df-6de559087c5c | -5.5832 | -60.2116 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 68bb6bb3-7f46-389c-93de-5362e3a7b8a3 | -11.025 | -49.644 | 2026-09-02 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 6abe51d5-ed16-3798-9191-7826d3d562d0 | -10.4145 | -49.9898 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 077afb6a-d054-3c90-b248-ae86be5a5a48 | -10.3007 | -50.023 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 75b33f1b-a5b0-31ca-9c6e-66ebdada7732 | -10.3196 | -50.0211 | 2026-09-02 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 60fe99ae-c887-36c4-8d30-6d1a6ecf7dc9 | -7.571 | -60.4643 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 057d6370-a990-301c-8814-760b4fd5c960 | -7.5845 | -61.3423 | 2026-09-02 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 81980ed1-edd1-3401-9a82-728e713aefc6 | -9.2144 | -47.99 | 2026-09-02 14:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 1e76ea6e-5d3f-36f4-b4d9-03eb1083a346 | -10.0635 | -46.6791 | 2026-09-02 14:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| dbcba71d-7efe-3489-8c6b-0f030ea7f771 | -10.7856 | -50.5066 | 2026-09-02 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 4eb76b6d-c1b2-3214-8b8d-929a41d68fb2 | -12.1504 | -47.1283 | 2026-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 46e5f0c5-2613-36a2-a564-5fa47c6358cb | -8.7628 | -46.4642 | 2026-09-02 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| e9889a72-84fb-3cec-88c5-d240d3868342 | -7.3486 | -60.6074 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 9d856c34-9116-3026-8d1a-58fe724f2a21 | -7.0242 | -59.2374 | 2026-09-02 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| f9bd2532-9817-35d9-ae2d-850928008b99 | -6.6949 | -58.7485 | 2026-09-02 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 83a0e7fc-7a41-36fd-b1f1-b8db760487a9 | -10.1008 | -46.7195 | 2026-09-02 14:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| de183a98-ad78-3282-bd20-d1b62850681d | -7.2006 | -60.6706 | 2026-09-02 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 9369e618-de13-3b40-afad-3138a4a35081 | -10.7199 | -47.1812 | 2026-09-02 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 9aeceee1-a718-335e-95ea-6bfc83c34ca5 | -10.7428 | -50.8727 | 2026-09-02 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 799551e3-fd65-3639-919e-5d56ffda683c | -12.0741 | -47.1164 | 2026-09-02 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 6cbb4479-fefb-3038-b81e-ab0c4f23648d | -3.3452 | -42.8067 | 2026-09-02 14:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 068a0af8-e94a-36ea-95a1-bcffac87d7e3 | -7.571 | -60.4643 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4313b360-5552-37c7-9e04-f75cdab33992 | -10.7431 | -50.8514 | 2026-09-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fbf5653b-d221-35b7-bfeb-ffba605790f6 | -9.1719 | -59.5017 | 2026-09-02 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| ac7d9bb1-66ae-3ee3-a5b5-70e4a36a4ce9 | -10.3013 | -49.9801 | 2026-09-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| cd7483bf-2b3b-377f-a088-3036c7ac6e87 | -12.1324 | -47.0635 | 2026-09-02 14:30:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b6582d98-4cae-34bd-878e-178d247fdf55 | -14.1083 | -45.5008 | 2026-09-02 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 4fbfc148-642c-395b-81d0-2d0d5853e530 | -12.1128 | -47.0886 | 2026-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 9cc0a0af-8245-3384-9911-0574a7bd5e35 | -7.3118 | -60.5897 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 282b268a-e42f-35ed-ae5b-2551ffa431f4 | -10.7618 | -50.8707 | 2026-09-02 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e20698b4-ae9c-3ad1-a102-f1a0cac05e8f | -5.2167 | -60.0507 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 9f1452fd-41df-322e-96ee-b283863e207c | -9.4349 | -45.625 | 2026-09-02 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 93b7311e-0f10-32c0-a5ee-dbe3e61197ec | -6.5645 | -44.7943 | 2026-09-02 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b4ed25fe-c576-3696-a11f-1f30e3f3834b | -9.4538 | -45.6228 | 2026-09-02 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 08e82781-5131-3bc9-ad63-3576551f2630 | -6.8422 | -41.6791 | 2026-09-02 14:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 118.1 |
| 63090741-acd6-36bc-8c74-bedcea042477 | -11.4895 | -50.3225 | 2026-09-02 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 424786ae-5788-3659-a9d6-bc938529c944 | -6.6542 | -59.426 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 01f4b54c-ce0c-34cd-99b4-81166f3bf60a | -6.8217 | -43.5271 | 2026-09-02 14:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1410b8dc-e597-3698-ae72-13699fc28ee2 | -11.6624 | -50.1954 | 2026-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 911dd932-68bc-3467-9404-f8e2357663b5 | -11.0437 | -49.6635 | 2026-09-02 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 179ba68e-1b44-3219-913e-f75b3a6aa934 | -11.0247 | -49.6656 | 2026-09-02 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 42d7ba31-371b-3ff0-9b38-cc95a92bd65a | -8.7613 | -62.5869 | 2026-09-02 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 121.6 |
| f35a3c32-6090-3fd7-831f-8e79373c2d93 | -1.5805 | -47.7462 | 2026-09-02 14:30:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 68323ec3-5c97-3446-9cb8-6763c5ef1352 | -1.0182 | -53.7189 | 2026-09-02 14:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 7a4bd008-e0ad-355e-9bad-92b0dd102fd7 | -11.5479 | -45.4676 | 2026-09-02 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 234.7 |
| eec0bbd1-8af8-3a7f-8084-5fea7b99b834 | -11.5086 | -50.3204 | 2026-09-02 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| ae6733b7-0f07-3b29-b0da-e18ee3ad4338 | -5.5833 | -60.1924 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 60214eb5-53ab-3424-8a4e-0e1af7d14366 | -3.6215 | -60.566 | 2026-09-02 14:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 5eab321e-7f9d-3ad9-a237-c357d3cbd723 | -6.93 | -45.7157 | 2026-09-02 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3a86bd23-9e73-3bee-8168-580822a48464 | -6.8568 | -59.4757 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| fc3b4c22-98f7-388a-ac79-edbce2d07d85 | -12.1504 | -47.1283 | 2026-09-02 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 78eab99c-3a22-3157-96db-7ac0f130f856 | -13.5724 | -59.7362 | 2026-09-02 14:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 9a540246-5b76-3bc6-be62-f32d01e83899 | -9.8806 | -64.9764 | 2026-09-02 14:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 53ca40bf-226e-31cc-9774-863974058468 | -6.6358 | -59.4267 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 5c31682c-a116-3735-8b45-6d216711e5db | -12.3818 | -48.1433 | 2026-09-02 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| bb30c760-2628-3ea8-bf25-9b7717927cad | -9.1718 | -59.5211 | 2026-09-02 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| fadb296c-bc9c-3d9c-828b-a96cfcb9c35d | -7.2191 | -60.6699 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 936d8c77-182d-38af-8e9a-2e98e17749f5 | -10.3193 | -50.0425 | 2026-09-02 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 169.6 |
| e8f42058-303b-30f4-af20-fb6ca5d1057f | -10.5788 | -47.7306 | 2026-09-02 14:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c621b33f-9b64-3741-ab8f-5cdaa70726a8 | -10.6964 | -46.242 | 2026-09-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d24849d5-b1cb-3586-ae9d-c57600f9408b | -11.6434 | -50.1976 | 2026-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 8c4fd3c7-94df-310f-85b1-87c19b9d99fe | -13.9853 | -58.6919 | 2026-09-02 14:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 39f0ca8b-e6ce-3c27-9e11-bb1fe431d574 | -6.7648 | -59.4408 | 2026-09-02 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 973ee32d-4511-314a-ba55-4b5de22c7bc3 | -6.3892 | -45.489 | 2026-09-02 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 08ddc246-449a-3032-984f-a284c44f19ae | -5.5649 | -60.193 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9799109d-2be8-3802-9b5e-4a5dc7cf63ce | -11.1634 | -50.5727 | 2026-09-02 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 353b6bcf-bd36-3ea6-a0ec-b524242e0c95 | -11.6621 | -50.2169 | 2026-09-02 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 33a21c1b-05ed-357b-a32f-dfe1969ddae1 | -9.2144 | -47.99 | 2026-09-02 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6222ebd8-82b6-3c5b-8cbe-d6a1587bec5f | -5.5648 | -60.2121 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 981dc25f-1124-3221-91e0-8966c989dd4e | -8.7628 | -46.4642 | 2026-09-02 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 99bc77ec-69d2-3672-a0a3-da5c14d45a6a | -2.9447 | -60.9002 | 2026-09-02 14:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| dbb72d7d-6a06-3e1d-b2c4-3a3c3bad5204 | -3.2361 | -61.217 | 2026-09-02 14:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 9a1a7674-9886-34eb-8903-59629f793b48 | -7.5845 | -61.3423 | 2026-09-02 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| fabc297e-a4d8-3136-b6c6-8a7d3409b3f6 | -10.6967 | -46.2193 | 2026-09-02 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| de827a4e-a446-3a05-b059-61e5c7689e7c | -7.5326 | -60.7147 | 2026-09-02 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |


[Clique aqui para ver as próximas entradas](README79.md)
