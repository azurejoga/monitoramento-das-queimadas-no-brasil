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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a6d684e-ee20-3318-9fad-4bdff8e289c8 | -3.44308 | -43.66882 | 2025-04-18 04:32:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 338fa0da-1a28-3869-b457-3a85b7f589ec | -5.42674 | -43.19684 | 2025-04-18 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c67ccfb2-6890-31cd-9092-d32d1ece7298 | -7.07845 | -44.3773 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e206d7e-8a33-3af7-8d14-dd8077406dbb | -6.54724 | -44.47715 | 2025-04-18 04:32:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de7e5a60-55cc-3ec2-8ebb-30acf4a825bb | -7.07477 | -44.37676 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cebc5a6a-dd3c-33dd-801c-a5ee2337e08d | -5.16541 | -45.10825 | 2025-04-18 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d106d3b-606a-3ee4-a5e1-53f0197c4152 | -6.95894 | -43.03685 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 913a9e57-9e73-3fe2-960c-98f65a254aa2 | -5.44078 | -46.28719 | 2025-04-18 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13330899-fe7e-38b9-ae9f-3308da7285cc | -7.07543 | -44.37233 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0d1b9aa-51ee-3e91-9100-bbb8c1251401 | -9.61791 | -37.03798 | 2025-04-18 04:32:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 16bde021-100f-3223-a7d0-d5b96c2221a0 | -6.9465 | -43.03856 | 2025-04-18 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| dc2414c3-eb57-3c12-ac4c-e35c38227ed4 | -7.0791 | -44.37289 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 77c07fde-09a0-3121-81a2-435ce99098df | -6.58345 | -47.53891 | 2025-04-18 04:32:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 33afee2c-5b7a-34df-af0f-d4be3499ecab | -7.08213 | -44.37783 | 2025-04-18 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 483f3df8-aaa8-36e5-9287-5380b7383b05 | -5.65191 | -43.70966 | 2025-04-18 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c799cd1-ff04-365b-aca5-2f5e1712877e | -9.61843 | -37.03818 | 2025-04-18 04:32:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 833e39e3-abb2-315d-87b4-2ea3dd642d10 | -15.7854 | -54.51361 | 2025-04-18 04:34:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d656330-55a2-33ba-9115-f7053bc80040 | -11.73224 | -48.71444 | 2025-04-18 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4389e287-1a2e-3545-9348-473ffc712922 | -9.92356 | -59.90641 | 2025-04-18 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9bc7395b-80e0-3ff5-9f0b-4516eabde237 | -10.96824 | -44.44708 | 2025-04-18 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5307511-3019-31a4-8954-20f9e3882f1a | -10.99098 | -44.42551 | 2025-04-18 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b087a03a-f1fc-32a4-adbb-0313e7f85370 | -15.07841 | -48.94313 | 2025-04-18 04:34:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48873c08-a226-3a5c-825f-c468f3f5265f | -12.15132 | -45.73395 | 2025-04-18 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c05d49b9-0c8c-3822-b195-84c5ff35805d | -11.39979 | -52.94271 | 2025-04-18 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8066aa06-9638-3b52-9ef3-d1a187b34502 | -9.92446 | -59.90168 | 2025-04-18 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a278c6c-ab89-3f05-8e71-34003fd510f4 | -15.57069 | -47.85606 | 2025-04-18 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd08b08a-aab3-3542-b7b7-1341ca1951f2 | -10.45372 | -49.08259 | 2025-04-18 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbc3e634-b428-3c1f-8af8-be43d5190bbb | -12.33692 | -45.63592 | 2025-04-18 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb5216dd-c105-3fb1-9076-c4dfea9e1ee9 | -19.73837 | -45.31938 | 2025-04-18 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb11e11f-e2a0-3732-869a-bb57eca70afd | -23.34033 | -46.77087 | 2025-04-18 04:36:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 33d12676-c22d-3a42-a7e3-65e49b163501 | -23.33944 | -46.77276 | 2025-04-18 04:36:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d2d832ac-0a82-3137-8cb0-2a62ce349f23 | -23.6325 | -46.42724 | 2025-04-18 04:36:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e07f81a5-5142-3174-9978-98091aa5ec68 | -21.19701 | -44.93878 | 2025-04-18 04:36:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3f508426-6293-3bc2-ba7a-d6c5fbf1ae22 | -23.0461 | -49.89621 | 2025-04-18 04:36:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b18ccca0-7b40-3771-bac0-7d39fbc0574e | -29.40599 | -54.03958 | 2025-04-18 04:38:00 | NOAA-21 | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| f57d3980-9b6d-3dfd-93f6-b0375c621bd0 | -27.08703 | -50.51569 | 2025-04-18 04:38:00 | NOAA-21 | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 956078d9-7467-365e-b381-f6730a8495c2 | -25.19379 | -49.32568 | 2025-04-18 04:38:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1571a004-b28d-3707-8dd6-c009f5726323 | 0.69446 | -51.4459 | 2025-04-18 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2382c240-5919-3372-854a-d277a717fff2 | -5.1637 | -45.11269 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe4477bc-8120-31f7-a333-d98aa7832ee9 | -7.08176 | -44.38392 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee9aab59-64cc-3781-9988-ecb44efcf854 | -3.48381 | -51.1894 | 2025-04-18 04:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ac4121d-c336-3006-9e23-747629f04e0f | -7.07097 | -44.37858 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 583c3167-43f1-3284-9e4c-ae9236eec2f7 | -6.95731 | -43.03807 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 97a4a973-bf15-3d96-be14-53547e9bda81 | -7.0772 | -44.3753 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe73090e-b34b-35c0-b21e-7b1e7b8ffb66 | -6.54636 | -44.47497 | 2025-04-18 04:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3e738b5-2446-36a0-bb31-b069f7d1fd99 | -5.7913 | -43.61907 | 2025-04-18 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 15a264f4-f196-3f2c-b919-72d23f7cdb0c | -5.64743 | -43.71345 | 2025-04-18 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b7bb33a-c857-379b-903f-1857b99bbdda | -5.7907 | -43.62326 | 2025-04-18 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e0497731-b6f8-3530-82a3-c7bf00e25f11 | -5.00964 | -56.17752 | 2025-04-18 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f9ed8b3-a53a-3b8d-82b6-2b9b7f8504c5 | -7.08525 | -44.37891 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3ed4b11-1ad3-3eda-bb30-3a8ad5d4bb3c | -5.15935 | -45.10558 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03a06aad-39aa-34f7-936e-44ebb3863c96 | -6.94435 | -43.04115 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8fca2104-d457-360f-b1a6-6e7eb2ab1999 | -5.42847 | -43.2017 | 2025-04-18 04:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d480155b-43d3-36fe-920e-0280256d8d99 | -6.95053 | -43.0419 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07a6097b-bf21-3144-b7dc-a6ef0f6584b2 | -6.94557 | -43.04232 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64b6ab37-0a31-30c3-9b52-3582cbec139d | -7.07903 | -44.38227 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0441d91c-3e3c-31f9-9f7d-0fa59b2e14ab | -7.07336 | -44.38159 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cae29ce-0663-3757-bbe5-6d10d5bd7426 | -5.15996 | -45.10575 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 48092ebd-a555-3b90-a249-8bcca847dcc6 | -6.95855 | -43.03924 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81e14f71-3276-3de8-a10d-0f75916eff1e | -6.9567 | -43.04271 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98381143-a0a1-3702-9b62-d6da0eb72b87 | -6.9462 | -43.03775 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a49ae83d-066f-325a-969e-257f0b7d3001 | -7.07664 | -44.37931 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8ae4ffa3-5415-31f0-811a-12d819d43be3 | -6.54584 | -44.4788 | 2025-04-18 04:57:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| edddb98a-fdb6-38c6-a979-5f7add2eeddd | -7.08232 | -44.37995 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a6811ba-70ac-39e0-a819-b9cc41fb5078 | -5.79561 | -43.62066 | 2025-04-18 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f1f3f54-1ca3-3192-8b0d-187a4d2f36cf | -3.7315 | -53.76541 | 2025-04-18 04:57:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c9436921-f2e8-3e05-9ef9-d72b3bc45037 | -6.95114 | -43.0373 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 11980304-c2f6-3ac9-8926-2faab20c3154 | -7.07154 | -44.37452 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4e2210b-44e6-345d-862e-8438e8f2dd79 | -5.16474 | -45.10965 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac597da5-7630-34cd-8f9f-295013e3c3df | -6.58023 | -47.53691 | 2025-04-18 04:57:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce698ddd-598d-3f2f-ae3f-b67732935f22 | -7.08288 | -44.37594 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c98ba42e-23e4-3f57-b183-7284a181add2 | -6.95174 | -43.04304 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5693e3d4-ea48-340f-9ce1-7d08b668494f | -5.78486 | -43.6224 | 2025-04-18 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d64462a4-6767-30db-a5d9-b360c4ab1e43 | -5.16044 | -45.10252 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b629af1f-019d-3bca-b8bc-ad3226a20ecb | -5.64802 | -43.70936 | 2025-04-18 04:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 874e645d-a1e8-3ca7-89ae-5e7d814696a0 | -5.44005 | -46.2899 | 2025-04-18 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7a65306-b6d0-3a6c-82fa-7720a81ae905 | -5.1589 | -45.10881 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba5f0d91-5aed-34f0-84dc-f84046209f1b | -5.15949 | -45.10896 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c3a854b-a431-3216-8661-07dca027bb00 | -2.53263 | -53.95668 | 2025-04-18 04:57:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| febc270c-4e3b-385b-935f-3b5a1bd6b068 | -6.95302 | -43.03387 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 80b53592-5f20-3862-b4a0-01c0dd29ca11 | -7.07776 | -44.3713 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3122b86d-0250-36df-b949-3d3a5067f2c2 | -7.07496 | -44.36952 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 09bd2496-372b-3034-8336-171e333f4d69 | -5.16521 | -45.10649 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a6564c8-1af5-3a58-aaff-ca7b6975fa97 | -5.7892 | -43.62397 | 2025-04-18 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e4641f1-94a1-3676-a7d9-8d152cff2ef0 | -6.95238 | -43.03846 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8735f3fc-52db-3d5e-b518-9e6a59ac236f | -7.07041 | -44.38259 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48f72d2f-e3cd-31c8-afea-fdc7157187a4 | -5.78976 | -43.61982 | 2025-04-18 04:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 15d7c4dd-df58-348e-ac7d-fbc43726c1fa | -7.07443 | -44.37353 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bb20f9a-594c-3075-9e2d-a24c42d2a01b | -5.48319 | -43.33172 | 2025-04-18 04:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 26dee64b-f765-36cf-aade-5f74fb1adf74 | -6.94992 | -43.04651 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8d53472-e990-3c07-9759-fdb3b8366a92 | -6.58477 | -47.53746 | 2025-04-18 04:57:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3e8aa4c-a75b-3064-bbbe-ae7f6571f0c7 | -2.38008 | -51.88305 | 2025-04-18 04:57:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c584659-f72d-3b4f-abd0-95d0ef1e0c9b | -7.07389 | -44.37758 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08f90fc2-e513-3856-b303-cb7ea3c7e182 | -7.07956 | -44.37831 | 2025-04-18 04:57:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 747b013c-16ea-3675-b388-dfd9dbb6bff2 | -6.94496 | -43.03655 | 2025-04-18 04:57:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6f251427-c598-3b4a-8437-ca285ab8cbea | -5.48258 | -43.33602 | 2025-04-18 04:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71d7aec7-ba76-307d-ae97-02632cb5af4b | -5.42248 | -43.20098 | 2025-04-18 04:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01ca8419-96dd-3e18-9d6c-d195eddd3971 | -5.16415 | -45.10952 | 2025-04-18 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89effe43-ec79-3b6c-a0e3-95b7a5abffe1 | -9.92631 | -59.9381 | 2025-04-18 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3c7d3c7-4646-3555-8ade-4d1cea97a772 | -9.97033 | -54.22625 | 2025-04-18 04:59:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
