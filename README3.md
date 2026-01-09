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
| 34f548d5-6d81-3278-973e-330cdbc28653 | -9.96367 | -36.37428 | 2026-01-09 03:36:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 7ecb37ce-6005-3888-8442-58c8a26f8a8d | -9.96659 | -36.37925 | 2026-01-09 03:36:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cde711d3-2125-3fac-b5da-edb743fb3de0 | -9.96293 | -36.37862 | 2026-01-09 03:36:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0dc7d850-f344-3a04-90d8-63998c34879b | -10.92629 | -37.5106 | 2026-01-09 03:36:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6246359-b009-31ab-bf0f-0d7e1d6918d0 | -9.96441 | -36.36996 | 2026-01-09 03:36:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 25f91abf-92a6-3f02-ae41-57940ac1215b | -25.56984 | -49.8333 | 2026-01-09 03:40:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f5a577a-c0f0-395f-9b24-992c0e598568 | -22.08094 | -43.17514 | 2026-01-09 03:40:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 29319376-bf31-34d5-b688-d884fbda493d | -22.74302 | -49.34884 | 2026-01-09 03:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 47aabc87-79b3-3a30-aca3-87ab7427eebc | -22.73672 | -49.34666 | 2026-01-09 03:40:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab7e709d-2cf4-34cb-a7ba-0572d9963385 | -25.57604 | -49.8351 | 2026-01-09 03:40:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4e0c5399-ed6e-360a-8c4a-4ffb1dc75825 | -3.35644 | -39.13513 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 6d0c186a-797c-3bec-ad13-4c783eed78b5 | -3.35701 | -39.13156 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 48b515cd-6bb1-3143-99a1-bb91ed37619e | -3.35365 | -39.13103 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| f6ccc141-e33b-3096-866a-766b80303de1 | -3.35308 | -39.13459 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4e720ecf-3614-391d-a423-4a40995b40ef | -3.36038 | -39.13209 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c440e361-51a7-344d-b71d-74b86da981b7 | -3.35422 | -39.12746 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 21f7ff8e-f1d3-362a-8c6e-e3f51af50f90 | -2.83662 | -40.17537 | 2026-01-09 03:53:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 22a14c1a-a63e-361f-8972-97f2fe33473b | -3.53101 | -39.08992 | 2026-01-09 03:53:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7ea89731-d919-34dc-9fcb-cbc84e2044cf | -3.35759 | -39.12799 | 2026-01-09 03:53:00 | NOAA-20 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 09a8ccc0-c326-36d0-8daa-c0e592fe73a2 | -9.96334 | -36.37267 | 2026-01-09 03:55:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4dbba212-59a1-3b67-818d-6809471ffafa | -4.40909 | -43.46878 | 2026-01-09 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1495493f-e9ec-37d1-99aa-d15b7158da37 | -5.87129 | -43.58447 | 2026-01-09 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51ebeb33-ff00-395b-bf5a-b83c01a58788 | -4.67969 | -43.24653 | 2026-01-09 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dc37652-2daa-3c18-b6b0-1f2f18f72a07 | -3.58222 | -40.97614 | 2026-01-09 03:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1fe3a354-5d88-3a92-8d9b-04dc51a2c4bc | -5.5682 | -36.25668 | 2026-01-09 03:55:00 | NOAA-20 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 29f1ab97-2e87-330a-af4a-90535c66c9b6 | -9.65012 | -42.9553 | 2026-01-09 03:55:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2be14da6-27d6-3d0d-a346-72ed8e7fedab | -4.26982 | -43.78516 | 2026-01-09 03:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd443433-18f7-3750-b597-f29537e7d7ef | -4.32414 | -45.35192 | 2026-01-09 03:55:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838da6ca-738a-392f-aef4-375c041a7cbf | -4.443 | -38.93051 | 2026-01-09 03:55:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9a6f38a7-c41f-33b8-bfc6-7fe8fc0962af | -9.96631 | -36.37731 | 2026-01-09 03:55:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3a0c0353-9059-3e89-b092-f25ac4a86854 | -8.89005 | -35.39879 | 2026-01-09 03:55:00 | NOAA-20 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22e3da87-cd90-33d1-8951-80c51f6daa49 | -6.56117 | -44.47263 | 2026-01-09 03:55:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fc866be-a2dd-399a-889d-657a238f915b | -5.24286 | -38.49104 | 2026-01-09 03:55:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b21c08c4-cf24-39de-b71c-bf3bcea55c90 | -3.26009 | -42.54485 | 2026-01-09 03:55:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d7dbeca-1af0-3b8b-8eea-ef69fd0f1433 | -6.28963 | -43.13496 | 2026-01-09 03:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a00c2476-c583-3288-91ac-b4ddb8fb69d3 | -3.57927 | -40.97149 | 2026-01-09 03:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd703255-b025-3c1f-9cd3-d97ea1128269 | -3.58397 | -40.97467 | 2026-01-09 03:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 53e418f8-13b5-38b7-8cd9-d3df7d5adb90 | -6.5661 | -44.46945 | 2026-01-09 03:55:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b98c79b7-33c9-30c9-a197-7d1207835bb1 | -6.06443 | -43.25468 | 2026-01-09 03:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2c32904-923d-34e5-a1b7-827bd38a584b | -6.85053 | -35.69654 | 2026-01-09 03:55:00 | NOAA-20 | SERRARIA | PARAÍBA | Brasil | 2515906 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d10a803-f9a2-36b4-95f8-e6ebaba8be34 | -4.98797 | -38.01975 | 2026-01-09 03:55:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ff93824-adc9-3c89-998c-94b2a8256b31 | -3.44865 | -42.25095 | 2026-01-09 03:55:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eab61659-e949-3144-94ce-247245645a64 | -7.7252 | -45.63468 | 2026-01-09 03:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 475e9873-da67-3d34-ac66-2812c78c2202 | -3.81206 | -38.43134 | 2026-01-09 03:55:00 | NOAA-20 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e097296-f965-355e-8c4d-b0cfe0b9c1f4 | -3.1148 | -43.27397 | 2026-01-09 03:55:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f229298-5938-3114-9eef-67e30d09a821 | -4.40434 | -43.47176 | 2026-01-09 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5604ec4e-28ca-3c95-a742-cb2324cea44c | -4.50213 | -43.69094 | 2026-01-09 03:55:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b992d9e-2642-3628-a0fd-3a31d4671761 | -10.51776 | -40.33179 | 2026-01-09 03:55:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0118e365-bbe1-3ee1-b89d-3ea2e877b07c | -5.33205 | -38.70041 | 2026-01-09 03:55:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| eb971359-3030-30c6-8ed7-dd6670583ead | -5.90623 | -43.85045 | 2026-01-09 03:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f352b8d0-174c-3ede-99a1-50652c64ab8f | -7.57737 | -34.95258 | 2026-01-09 03:55:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bff2093b-41c0-3646-bf8f-bba9a6aafbe8 | -6.33452 | -39.61324 | 2026-01-09 03:55:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b3fb24b-6503-3b06-9bde-f821622ae46c | -5.8745 | -43.58737 | 2026-01-09 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dcb4d29a-3496-358e-b342-61831e488e16 | -5.87536 | -43.58518 | 2026-01-09 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4a1da90-8c69-30d8-b2e0-976bbe237c78 | -5.84018 | -41.05047 | 2026-01-09 03:55:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 05ba4d64-bd0f-34a8-8088-0947235604db | -6.8331 | -35.06647 | 2026-01-09 03:55:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7d2d9326-5104-33dc-976b-c033083a3642 | -5.7482 | -35.39033 | 2026-01-09 03:55:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00a0f2f3-b543-3139-a8b1-ae991fe7fcb1 | -5.74883 | -35.38627 | 2026-01-09 03:55:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8dbe7c0e-d53c-3ec2-a73f-d590ae238c35 | -6.56362 | -35.24523 | 2026-01-09 03:55:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6536e51c-9b23-3b53-9276-c45f21df7eaf | -6.31651 | -38.31796 | 2026-01-09 03:55:00 | NOAA-20 | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7d7418f-6014-35b3-918b-f82bfd4c44a8 | -6.30533 | -39.39517 | 2026-01-09 03:55:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7552af10-de48-30a7-a80f-916c10f27064 | -3.89813 | -38.42363 | 2026-01-09 03:55:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4e9ce64d-8d5e-3ba9-b708-ff41b70bbe06 | -4.74937 | -43.25476 | 2026-01-09 03:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fddfcd52-4f66-38b0-b6c9-7826c7f31d24 | -4.38202 | -40.06495 | 2026-01-09 03:55:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2f01e284-eb93-3c8e-8ba8-56c4f7190e9e | -3.85475 | -42.25175 | 2026-01-09 03:55:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b05ddb42-cb3b-3d4c-a57f-82195718ee4f | -7.63826 | -35.03099 | 2026-01-09 03:55:00 | NOAA-20 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a79e882f-f395-3731-bbf2-5616662732f1 | -4.38546 | -40.06548 | 2026-01-09 03:55:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd8bebed-da99-31e2-b1c9-8ab4dc283c79 | -6.2422 | -39.70428 | 2026-01-09 03:55:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 770e7a14-06e7-3fbf-9ae1-77c40e692fa5 | -4.8814 | -38.67163 | 2026-01-09 03:55:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d39abdca-416e-362a-a4f1-6761252ff68a | -5.57164 | -36.25721 | 2026-01-09 03:55:00 | NOAA-20 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 797bdac5-ceaa-3239-8485-105b5ef49c18 | -4.53495 | -40.47015 | 2026-01-09 03:55:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5b507a9-7f79-3c00-99ef-9547f9287322 | -5.55308 | -43.8133 | 2026-01-09 03:55:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db364054-79ce-34ab-a76d-0b940b74d003 | -7.71337 | -35.09924 | 2026-01-09 03:55:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1075a57-ee54-38be-ad8f-1293c17fda4f | -8.56058 | -41.41233 | 2026-01-09 03:55:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11f79901-6546-3932-a517-d680238729d0 | -6.4647 | -39.78017 | 2026-01-09 03:55:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 96ddf5ab-ae79-334b-84db-a09fb0439997 | -6.33806 | -43.38228 | 2026-01-09 03:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95f975a6-7e1f-3ac6-847b-d45e5e9c5561 | -3.60571 | -39.63609 | 2026-01-09 03:55:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4b51bdc-42c6-38ca-a934-6fb636c9dd2d | -4.25354 | -43.77841 | 2026-01-09 03:55:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 621ee117-21a8-3855-b8d0-5574ad958705 | -3.53976 | -41.03349 | 2026-01-09 03:55:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b970c5e8-032d-3216-b1c9-19434eb9109a | -5.10502 | -39.22911 | 2026-01-09 03:55:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 936f8837-e828-3cba-9e6e-7033c35fa067 | -7.71614 | -45.63309 | 2026-01-09 03:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55015fbd-4636-3592-a76c-dfc2486c2f19 | -5.75398 | -39.79958 | 2026-01-09 03:55:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3419c22b-5cc0-3330-9ed1-46f32db153bb | -10.92393 | -37.51145 | 2026-01-09 03:55:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e9aef183-d2da-380d-ab94-1890b5a72afd | -7.33626 | -34.95434 | 2026-01-09 03:55:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fb672f2-fd03-34e2-a1b4-8a8a91049ef5 | -4.3957 | -43.5749 | 2026-01-09 03:55:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f9c918c-61b4-3517-b8cd-a01b7cbfd61b | -6.33787 | -39.61376 | 2026-01-09 03:55:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9bdf4ab4-6d8f-3cc9-973f-b31cacd6c2c0 | -6.17212 | -39.3339 | 2026-01-09 03:55:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 702a9530-d486-3dd9-aa5f-aaab7baa11db | -5.8707 | -43.58809 | 2026-01-09 03:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21abc9fb-9af3-3df7-a5f9-4bbbdc53dd34 | -5.01603 | -44.64549 | 2026-01-09 03:55:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53450904-fdde-30c4-ad3e-827969745ade | -7.72067 | -45.6339 | 2026-01-09 03:55:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d01b3e83-29ba-37b8-af6a-7bfe90f17dc5 | -5.52846 | -37.77876 | 2026-01-09 03:55:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67b298f0-8d71-3ae0-b7e8-8b9542d77225 | -6.34342 | -39.62193 | 2026-01-09 03:55:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 19f7c959-8dca-3fa2-830d-da2bf6c14456 | -6.58091 | -38.5801 | 2026-01-09 03:55:00 | NOAA-20 | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f42c4450-0525-3972-9ada-8344d9f38dc8 | -5.17213 | -43.27325 | 2026-01-09 03:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a51d4a4b-38fd-3ac1-a7d6-aa9a6053e958 | -5.06609 | -37.63168 | 2026-01-09 03:55:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e83dc173-bb81-3e0c-b603-6278dcb940c4 | -3.60232 | -39.63548 | 2026-01-09 03:55:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d6bb6922-3434-329c-973e-82e6368555be | -10.91992 | -37.51471 | 2026-01-09 03:55:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| d4dae8f3-65d2-34b7-8e43-370daaae8478 | -6.58657 | -44.62237 | 2026-01-09 03:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a2ff0601-8a0d-3ef9-8300-3c0c5b76d20a | -6.83007 | -35.06155 | 2026-01-09 03:55:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a96ba7b0-85ec-320b-92e2-84bfd377ca59 | -3.85396 | -42.25656 | 2026-01-09 03:55:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README4.md)
