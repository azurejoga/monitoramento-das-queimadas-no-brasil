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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03c596d3-f516-3581-bdb3-fbc17c28140e | -11.3939 | -44.97303 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29dacea2-490e-304b-86ea-21394fe00765 | -11.39166 | -44.96886 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00f808c6-d70c-322b-9fd8-79b4a07de3dc | -11.39113 | -44.97178 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3d77977-5e0f-31e8-b830-024441402fff | -11.13098 | -44.95129 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45b6a882-95b2-366b-92d9-453039255d42 | -10.79114 | -44.09292 | 2024-10-24 03:42:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 942f4744-307f-3323-bd66-abeb9d3a08e7 | -10.78805 | -44.09147 | 2024-10-24 03:42:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1999264-ea4d-3d52-ae41-e2192e9724bb | -10.77985 | -44.24923 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7169b58-8dd1-31dc-95c4-4fff0805e23a | -10.72207 | -44.87784 | 2024-10-24 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aabbb832-d527-3281-a8eb-d75957a82cbb | -10.71697 | -44.8768 | 2024-10-24 03:42:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 344b226f-3d40-38b8-817e-b213c0fd7c47 | -10.61184 | -44.27134 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ab1593d8-fa7d-3b65-af2a-9ae67b80f064 | -10.61081 | -44.27693 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e95f46bc-4510-3992-b2bd-82f7743d8e5b | -10.60979 | -44.28254 | 2024-10-24 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4bb8841a-1538-3370-a8a9-27c604f7d94f | -10.60691 | -44.27048 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 202f3124-1bb6-304f-aa05-45f859cfba2d | -10.6059 | -44.27598 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f783c9c4-77bf-3aa1-a510-f9695de3ca21 | -10.60488 | -44.28153 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 98f1c714-1dd9-365e-988d-24147eb5b4d3 | -10.60198 | -44.26966 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 872aa2e1-172f-3cba-916d-a208cada9c7f | -10.58318 | -44.28878 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9423ab06-fb34-37a9-a0b4-7c04c2cb6855 | -10.57929 | -44.28229 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1df43d03-7e98-398c-98ea-ef98e893cd4d | -10.57827 | -44.28782 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f3369d86-adb6-3d0c-826d-707927013a02 | -10.57722 | -44.29348 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| acebb7cd-2796-36b2-94ae-84af856c19e4 | -10.57335 | -44.28686 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cb3a678c-1991-3a6e-9f02-e3bf5b0c21d6 | -10.5723 | -44.29253 | 2024-10-24 03:42:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82034850-b4b1-312e-ab0b-540b0ce87b6a | -10.55799 | -45.14955 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf9ec57d-e677-3239-b614-d33ebf12de4c | -10.55739 | -45.15275 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d43e8367-b709-3458-960a-47a04ac0be21 | -10.50509 | -44.90933 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60667618-95dd-3368-a54a-3b5e0e70d978 | -10.49591 | -45.16417 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6c71a963-8c28-3f53-87d9-7e99e5ecea0a | -10.49572 | -45.16433 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4003a968-fcb8-3db4-9042-6502c2a337a9 | -10.4949 | -45.1106 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a794dd56-0830-3e72-bde6-c6951b19ca70 | -10.37455 | -45.08844 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5f1a1c3e-91d5-37b4-b99d-6cebb10783d7 | -10.37396 | -45.09163 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b37c6707-554e-3694-abdd-360e7cb4d82a | -10.37338 | -45.09483 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b7e1bc76-96ce-34c7-835b-c043c65ecca5 | -10.36654 | -45.07338 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4d1dd5b-1b1e-30a6-9be2-24518634f121 | -10.36134 | -45.07235 | 2024-10-24 03:42:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b79879a-f653-3b18-9d04-2bda7d465531 | -10.28561 | -36.3249 | 2024-10-24 03:42:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dbfa24f9-233e-3bdf-af78-8ca6359d69f8 | -9.88892 | -47.80906 | 2024-10-24 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5551e51a-5030-3668-93be-2b4d73c3f917 | -9.88695 | -47.80632 | 2024-10-24 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1d8bc1eb-7bd0-3b8a-8b17-df7eb4e4d7b0 | -9.8828 | -47.80714 | 2024-10-24 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 626a6bf7-750e-3cca-9a76-cb221b9e4a1d | -9.86999 | -48.56689 | 2024-10-24 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a9df60-6918-3aab-8c45-1f253f22c0d6 | -9.86348 | -48.56549 | 2024-10-24 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14808996-4ad6-35e4-819e-ca9125993996 | -9.60868 | -47.61193 | 2024-10-24 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38537aa8-e1dc-39dd-836d-9de2a02a78c8 | -9.60414 | -47.61187 | 2024-10-24 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84f068f4-1715-335f-9e7a-7033d8d6adb0 | -9.60252 | -47.61053 | 2024-10-24 03:42:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18ff969a-1a66-3d1f-a291-9253a246d3b5 | -9.24079 | -48.32468 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a7ec3ba-aafb-39e7-9187-91c4718ec0f9 | -9.23977 | -48.3255 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4481c98-7975-3079-a944-e28308344cf6 | -9.23537 | -48.31773 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb75ef3-7f52-35ae-a873-89c70d4127eb | -9.23439 | -48.31858 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c26d377-ed16-37d2-a74d-1ea7ce78b05a | -9.22887 | -48.31644 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0da9370-6b03-30c9-880d-971b980e257a | -9.20549 | -47.95595 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c88436cc-5358-375c-9d52-0dd09149ef68 | -9.20445 | -47.96122 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ea3ab17-de07-3460-ad90-45b82c48f169 | -9.20429 | -47.95285 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15e8aa39-fc4f-3def-bb31-cf9c69574ed8 | -9.20329 | -47.95811 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d5000cd-60d5-31c5-b147-21fba408c74d | -9.19918 | -47.95443 | 2024-10-24 03:42:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a4da4cf6-f5e1-30d9-b093-62379ae81b12 | -8.92472 | -47.05502 | 2024-10-24 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59a71f29-7e16-3b7a-8434-5221a9b4f3a6 | -8.91867 | -47.05384 | 2024-10-24 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f4d9f85-f966-3c9d-b5b9-37925b589a78 | -8.91778 | -47.05853 | 2024-10-24 03:42:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e0f477e-7710-3cc3-9132-cf7883ce22e5 | -8.58139 | -49.23103 | 2024-10-24 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3f9ce940-2739-3f99-ac48-aad8ccf55cd2 | -8.5758 | -49.22285 | 2024-10-24 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bf1fc61f-586f-34c0-878f-3d28997b9c6d | -8.57446 | -49.22972 | 2024-10-24 03:42:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f028c57-d1cb-380a-b81a-7ba5fab34734 | -8.51696 | -45.87695 | 2024-10-24 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47870a95-142c-3c0f-81e7-057ca4624dc6 | -8.51524 | -45.873 | 2024-10-24 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ee51e3d-1992-3ea3-ab7a-c91f99c75999 | -8.51453 | -45.8769 | 2024-10-24 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1501fff3-81ca-3bda-9c24-f2a87440b4b5 | -8.51189 | -45.87273 | 2024-10-24 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df3a0c84-17e6-38c5-8ea3-435b692b48af | -8.51118 | -45.87649 | 2024-10-24 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d3e0c50-f63e-3326-9e7e-60228027c535 | -8.02121 | -49.64592 | 2024-10-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcf4e067-f1d7-372a-ab23-204879f9fc2a | -8.0154 | -49.63783 | 2024-10-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33b961fb-68bb-3cde-b73c-1a202ea227c1 | -7.89304 | -46.68762 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a54fe65-a54c-3fbd-8b88-d91f3a46e10f | -7.8922 | -46.69218 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5bed392-4520-37ef-bb1a-055648da16d7 | -7.88703 | -46.68646 | 2024-10-24 03:42:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad18753f-3402-395b-8831-72abb6cb0145 | -7.63332 | -47.82965 | 2024-10-24 03:42:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b6a5cad-7244-394e-a95b-ab97a5167be0 | -7.63273 | -47.83042 | 2024-10-24 03:42:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45834a62-6356-3496-8ae6-8a9c15059dbd | -7.62686 | -47.82827 | 2024-10-24 03:42:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cce65c8-897e-3a90-9b00-d26900cafcf4 | -13.01258 | -49.56594 | 2024-10-24 03:42:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0162db7a-46b2-38a4-a90d-ec0000a26bf0 | -13.00605 | -49.56441 | 2024-10-24 03:42:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7abcd4a-76a0-34f6-88dc-bda097f5e59d | -12.88837 | -48.51617 | 2024-10-24 03:42:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ee2ba17d-ff45-3fee-a21c-3c532683377c | -12.88728 | -48.52146 | 2024-10-24 03:42:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 383e0389-6bd6-33e1-acd5-34856fae74f7 | -12.88321 | -48.51887 | 2024-10-24 03:42:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a98c08a-f94f-3296-9ccc-da0064bff06a | -12.88218 | -48.52403 | 2024-10-24 03:42:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9d2b8e5f-96f7-3256-92f5-6b80316ae619 | -12.8811 | -48.52017 | 2024-10-24 03:42:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eece45d6-7055-39fb-93fa-0d34484f0101 | -12.59283 | -48.77383 | 2024-10-24 03:42:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69e74954-e616-3927-aec0-cb1e07d3787b | -12.59174 | -48.77904 | 2024-10-24 03:42:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 927db0ca-e897-3716-9c53-68fde946dcf2 | -12.59029 | -48.7747 | 2024-10-24 03:42:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 544b4f97-c1e7-37dd-9750-eba5a9eeaaaf | -12.58923 | -48.77991 | 2024-10-24 03:42:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9affac54-f181-304a-b5c3-a034de0ac631 | -12.28907 | -46.72879 | 2024-10-24 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38656e9b-2193-30dd-a282-98e3284c2da0 | -12.28347 | -46.72767 | 2024-10-24 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc154257-a82e-3b0c-b6d0-609a4811c19d | -12.2827 | -46.73156 | 2024-10-24 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5787e809-69d8-32df-9d62-17b59aea68c2 | -12.28193 | -46.73545 | 2024-10-24 03:42:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4037200a-29de-3b1a-84b9-2bed28bc130d | -12.20634 | -48.06473 | 2024-10-24 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27f676da-befa-3337-8df5-89052a09b368 | -12.20479 | -47.49266 | 2024-10-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58dae32c-2634-3948-8b2e-93668ba7beb2 | -12.20448 | -46.7268 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c6a4d64-ccce-3fe6-ae07-fb0ab56aa595 | -12.20372 | -46.73068 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4a98cd67-7372-3bc6-a4e1-c6f9de3ba585 | -12.20306 | -47.49005 | 2024-10-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 072a6217-6207-3e43-b58e-daae9f10a487 | -12.20215 | -47.49454 | 2024-10-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f51e1448-edaf-3cf4-a063-9eee45807440 | -12.1989 | -47.49151 | 2024-10-24 03:42:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02682d8d-8dfc-3952-bcfb-2df20bacaab4 | -12.19888 | -46.72559 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc2d63fa-6b0e-32a9-82aa-e4c5a1331e45 | -12.19812 | -46.72947 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34147f9d-9afe-3402-9785-96df8869f059 | -12.17267 | -46.74028 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 085771a9-1349-3724-8849-0903269268c9 | -12.16705 | -46.73915 | 2024-10-24 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c09976e8-1dd3-3251-ad80-3a07fc1a4b9f | -12.07541 | -47.99045 | 2024-10-24 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d368908b-7c1e-32e3-81ff-8dfc087b7bc4 | -12.06933 | -47.98925 | 2024-10-24 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60b80fb5-ff66-3bdb-ad71-912ca9e18fb0 | -12.05668 | -48.34271 | 2024-10-24 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README23.md)
