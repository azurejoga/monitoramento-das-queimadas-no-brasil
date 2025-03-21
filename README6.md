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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 171288b1-c414-3f36-8086-228a02e138c5 | -30.71371 | -54.1819 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 4.7 |
| cf8dd5fd-95f3-3181-8854-b8dba73056a8 | -30.73155 | -54.18454 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| b846a516-00b8-3724-9127-8ccb60fe7154 | -30.72915 | -54.18927 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 1f85cf0f-4794-3335-8de8-6073559478a6 | -30.71453 | -54.1682 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 1a0c9109-268e-3ae9-b98d-57a4e62d9c2e | -30.71164 | -54.18184 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 39298146-4c18-3198-833e-4764e5d7e4e1 | -30.71344 | -54.18645 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 2da21a25-d9d3-3eb9-992b-b75079fb3e9f | -30.71135 | -54.18633 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 271f9275-b129-3cdc-84d0-01cc4abc483a | -30.72884 | -54.1939 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| b88bdd52-178b-3bbb-b3a5-74cb2d01977e | -30.73481 | -54.1944 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| 441a8e85-7099-3047-b7fd-0e52da953c58 | -30.70774 | -54.18142 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| ceed969b-ec53-373c-8ea3-f1c257b0ace4 | -30.73126 | -54.18941 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 5aa47175-fa2b-32af-9d10-53587a0fab10 | -30.73098 | -54.19406 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 366cc33c-dc29-3e37-b461-6d898e3f6449 | -30.7148 | -54.16357 | 2025-03-21 05:29:00 | NPP-375D | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| cbfd42a4-313e-375b-b73b-077c5c4e4180 | -19.42573 | -54.78091 | 2025-03-21 05:44:00 | AQUA_M-M | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a882dcc0-cc81-3e4f-b20b-b5bf810fd322 | -19.43617 | -54.78307 | 2025-03-21 05:44:00 | AQUA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e36793ee-c36a-3e27-88e9-e0b9bcee5e12 | -13.66851 | -52.12641 | 2025-03-21 05:44:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2e96d16e-934e-39dc-975d-81b8e4cc3fb8 | 2.59712 | -61.29834 | 2025-03-21 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81e9ff9d-ec99-3139-a716-3534d2be2d0e | -0.2575 | -65.07442 | 2025-03-21 05:44:00 | NOAA-20 | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a05598d6-4455-3648-b483-80e416e93c02 | 3.87317 | -59.65514 | 2025-03-21 05:44:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b469584-11af-3b76-aa88-ff1d7736253f | 2.51778 | -60.99284 | 2025-03-21 05:44:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce4d2161-b866-3879-95b2-388af42d5901 | -30.72719 | -54.19142 | 2025-03-21 05:46:00 | AQUA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 7.7 |
| cb2162ed-c9e8-39e8-84a7-ddaaa3bc3c2f | -30.71102 | -54.17742 | 2025-03-21 05:46:00 | AQUA_M-M | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 9.6 |
| c75d9339-eff2-3070-9f32-f7c45c0cb306 | -7.93265 | -61.55627 | 2025-03-21 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 134c604c-24db-391c-9020-321697fdbff1 | -7.93001 | -61.55561 | 2025-03-21 05:46:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c966e0f-029b-3694-8dec-026d8b9398b3 | -12.25977 | -63.80214 | 2025-03-21 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c96a84a2-6deb-3cbb-9d6d-78f1b3b442e7 | -15.5954 | -57.33069 | 2025-03-21 05:48:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b6b682c-9d9a-3d62-bc0b-5a4d31f5cffb | -15.59488 | -57.33563 | 2025-03-21 05:48:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17dd4f45-8467-3892-ad27-98f26da7de15 | -12.2577 | -63.80397 | 2025-03-21 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cea3be66-9991-337b-a027-657ba3df3634 | -12.26155 | -63.80452 | 2025-03-21 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65421b6-ca6c-3e24-93ce-b67ac71dfd80 | -12.12775 | -63.66673 | 2025-03-21 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 976059fa-9f97-3410-bf79-a035f84f130f | -12.73322 | -57.26674 | 2025-03-21 05:48:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fb52011-2a3d-3a0a-978a-dcf2a050571d | -20.92183 | -56.5472 | 2025-03-21 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0081d290-a577-3026-93fc-9677aafa36ea | -20.9273 | -56.54743 | 2025-03-21 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91a1f600-1276-3389-96bb-0641a4ec6234 | -20.92046 | -56.54724 | 2025-03-21 05:50:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9bcd3ae-e7a4-3716-98f7-079a0afdff6f | -9.45269 | -36.80079 | 2025-03-21 12:06:00 | TERRA_M-T | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 5a02c4e3-b7ea-3984-9da8-86f95fb8b2f3 | -9.17003 | -38.45871 | 2025-03-21 12:06:00 | TERRA_M-T | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 51fc8c41-83e3-3557-ba36-88e6831c1541 | -10.82615 | -39.48929 | 2025-03-21 12:06:00 | TERRA_M-T | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f8b0b4b7-e3bc-3d96-a2d8-395925d80167 | -12.26611 | -38.83687 | 2025-03-21 12:06:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 5581f00a-678d-399a-b94a-aac1b95abec2 | -10.8248 | -39.49902 | 2025-03-21 12:06:00 | TERRA_M-T | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f01df838-e236-38b5-83ea-5d9f454d2839 | -12.4161 | -38.39342 | 2025-03-21 12:06:00 | TERRA_M-T | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 255e56fa-2f28-344d-8530-45094edb9374 | -10.08478 | -39.31813 | 2025-03-21 12:06:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 51.8 |
| b8ff0967-31a9-32a8-b107-da1c97c1f3e3 | -12.67545 | -38.28428 | 2025-03-21 12:06:00 | TERRA_M-T | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| fa1ecaff-adeb-3d5c-ae2e-1631c78bc5a4 | -12.31857 | -40.41967 | 2025-03-21 12:06:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ab366a80-23e8-3704-8626-3d963c440de6 | -12.31986 | -40.41036 | 2025-03-21 12:06:00 | TERRA_M-T | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| ab8c94ea-cdf6-3c38-8a49-36470ccc0c3a | -12.26753 | -38.82616 | 2025-03-21 12:06:00 | TERRA_M-T | CORAÇÃO DE MARIA | BAHIA | Brasil | 2908903 | 29 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 7eb3c041-da2a-3983-a084-b13d1e721aac | -10.09398 | -39.31942 | 2025-03-21 12:06:00 | TERRA_M-T | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 2842c71e-300e-3bb8-9ba6-c6d47d0b514f | -11.06929 | -38.60032 | 2025-03-21 12:06:00 | TERRA_M-T | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| ed99a878-e2b0-374a-916d-82872e6f9f9d | -16.03029 | -43.33987 | 2025-03-21 12:08:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2c74cfed-0e54-32ed-9269-5c8639d8fbe8 | -16.38311 | -39.43093 | 2025-03-21 12:08:00 | TERRA_M-T | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 817b22bb-c82d-307f-b5b8-18f3a2be5c88 | -13.68109 | -42.99696 | 2025-03-21 12:08:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 47.1 |
| 5da05013-1dd9-3900-bdad-51b0881a07b9 | -13.69144 | -42.99509 | 2025-03-21 12:08:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a3249890-2d87-3dd4-a8ae-c399033bc297 | -15.82133 | -40.19543 | 2025-03-21 12:08:00 | TERRA_M-T | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |


