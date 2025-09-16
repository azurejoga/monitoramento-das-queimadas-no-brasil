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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3197473-d456-3de5-aeb2-ada07f9bc24e | -16.66187 | -41.73354 | 2025-09-16 12:00:00 | TERRA_M-T | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 7ee374f8-73a5-3684-9d2d-0b7149dae1c7 | -12.50973 | -44.22834 | 2025-09-16 12:00:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 626abf56-f1a4-3eef-8948-b80f40fdc0bc | -14.08884 | -43.90596 | 2025-09-16 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| fa25acfa-4670-3cec-9a74-b5a00d9b5037 | -12.73573 | -47.20956 | 2025-09-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 907d145e-ed54-37d8-a975-c99d7c1daece | -12.68853 | -45.30123 | 2025-09-16 12:00:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ba5b2890-7c32-3f2b-a190-8334ae097ae5 | -12.00593 | -46.64972 | 2025-09-16 12:00:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 77d308fc-1026-3e64-bb61-688065c13cfd | -11.71411 | -46.88209 | 2025-09-16 12:00:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| bcb8ebc5-7246-3d0e-a2d6-e86bc9a942cb | -14.09911 | -43.89809 | 2025-09-16 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0d016c1b-8524-3296-92d9-71f49178aac2 | -13.83766 | -43.67094 | 2025-09-16 12:00:00 | TERRA_M-T | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| adf1e24d-71bd-3177-b6a5-3fb6708a8580 | -14.16871 | -46.13431 | 2025-09-16 12:00:00 | TERRA_M-T | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8600c8e4-2fb6-3e81-b2fc-768a9d984d90 | -20.79373 | -45.52822 | 2025-09-16 12:00:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 2f1bb355-ca0c-39e7-97ca-e76f50eb703a | -19.82049 | -41.31659 | 2025-09-16 12:00:00 | TERRA_M-T | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 0086c03c-424e-3b7c-8ab6-ceba8aa6bc54 | -21.18409 | -45.63421 | 2025-09-16 12:00:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 15.8 |
| e20da9fa-dfca-3551-aad0-82c4367846e3 | -21.71355 | -46.16074 | 2025-09-16 12:02:00 | TERRA_M-T | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4c4fb967-1a9e-34f9-b22c-ceca51a9974f | -22.71812 | -43.23359 | 2025-09-16 12:02:00 | TERRA_M-T | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 493df8e4-454e-375d-b68f-3938de446ef1 | -22.06683 | -45.14478 | 2025-09-16 12:02:00 | TERRA_M-T | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b203b4ab-f7be-317c-81e6-01a8d30327ac | -21.92587 | -45.67007 | 2025-09-16 12:02:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e8161794-fd72-346c-92d6-34a1594b0d1d | -21.74484 | -46.43872 | 2025-09-16 12:02:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| bf4531dd-980a-3971-bbda-297a69e462b0 | -21.99971 | -45.6034 | 2025-09-16 12:02:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 06f2ffc4-3dcb-3dd0-a9ef-ce1a7e8bf98b | -21.93479 | -45.67155 | 2025-09-16 12:02:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 15849117-a932-3b9e-a73a-b0f1dce5cf07 | -22.034 | -45.43216 | 2025-09-16 12:02:00 | TERRA_M-T | LAMBARI | MINAS GERAIS | Brasil | 3137809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f9195ffb-4e31-3313-b771-54226df00ef2 | -21.7433 | -46.44875 | 2025-09-16 12:02:00 | TERRA_M-T | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| db750460-6c36-351a-9f83-3a33a390258f | -21.4333 | -48.5781 | 2025-09-16 12:02:00 | TERRA_M-T | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| 48f8cee4-da27-3d22-8c3a-84721f9cb8aa | -22.06618 | -45.34575 | 2025-09-16 12:02:00 | TERRA_M-T | JESUÂNIA | MINAS GERAIS | Brasil | 3135902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 66b18626-2db6-339b-a756-67b102783350 | -21.93631 | -46.57713 | 2025-09-16 12:02:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| e206c833-9e6d-3421-8d9f-1b1db3c2f1c2 | -22.00862 | -45.60482 | 2025-09-16 12:02:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.7 |
| 18331c75-f5fa-3ee2-bc74-147c333accfd | -21.82212 | -45.43362 | 2025-09-16 12:02:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4fdee504-4f9e-305d-b41a-999a9a767544 | -21.93787 | -46.56694 | 2025-09-16 12:02:00 | TERRA_M-T | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.3 |
| b4a5100e-fc33-30a5-ad6f-7060b7b0a541 | -22.08761 | -45.26147 | 2025-09-16 12:02:00 | TERRA_M-T | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 08bba5f5-9da9-3af4-9ae1-f3d197d7c60f | -21.93335 | -45.6812 | 2025-09-16 12:02:00 | TERRA_M-T | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 1faf7974-ad8a-3c1d-bb8d-3f2192bfb5d6 | -21.88092 | -45.35159 | 2025-09-16 12:02:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 46d425a0-851c-3771-9e24-cd549c99523a | -22.52446 | -45.10434 | 2025-09-16 12:02:00 | TERRA_M-T | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d5906910-90d5-397a-bc95-3ddab85b885c | -13.2801 | -54.2228 | 2025-09-16 12:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 38a96a21-5371-33e3-9002-a738f18c7d73 | -9.1047 | -44.8871 | 2025-09-16 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 7fa00c00-9bf1-3d59-9289-3a72aa6f39c1 | -7.1505 | -47.9786 | 2025-09-16 12:10:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| b9b6476a-54be-3a17-9605-0abf682a098d | -8.907 | -45.5252 | 2025-09-16 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 632ca5ef-4df1-3c2e-8f17-935df23328f0 | -8.9259 | -45.5231 | 2025-09-16 12:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d090a21b-a469-3caf-863b-1466affed1b9 | -12.6909 | -47.9899 | 2025-09-16 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 028fc836-c96f-374b-9323-fea8a5a551ce | -12.6356 | -45.7422 | 2025-09-16 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 92a51fc1-a2c2-3efb-b8f0-c071ebcc5552 | -8.613 | -46.39 | 2025-09-16 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a32ea702-6987-3baa-8ee2-d5d2f548332b | -9.086 | -44.8663 | 2025-09-16 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 106.9 |
| f09345a1-d9bb-3e91-a912-5b032f55a445 | -11.4853 | -43.5929 | 2025-09-16 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 1171e387-4617-32d8-a12c-0f3d51094643 | -4.5934 | -43.3239 | 2025-09-16 12:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 3cacd2e5-5ced-3d5f-880f-e9448a497c0d | -9.152 | -46.9812 | 2025-09-16 12:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6327b1d4-67d4-37ed-ae93-7126078d06ca | -8.0007 | -45.6638 | 2025-09-16 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| b6d44930-9326-3db6-adea-85ce3f6f8045 | -7.9822 | -45.643 | 2025-09-16 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 08c86caf-ff22-318b-b5a7-ffef893e513d | -12.6352 | -45.7652 | 2025-09-16 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 1b585a24-d76c-3b76-91dc-7ef61b6cd1de | -9.105 | -44.8641 | 2025-09-16 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b522acee-cc4a-3c75-9b23-c9df72657784 | -10.7302 | -46.5082 | 2025-09-16 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 8cc0c014-a71f-30a6-9ee2-58856b3581cf | -5.7858 | -43.9378 | 2025-09-16 12:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| e92179b2-6dc7-3075-aaa4-d9e18b959b13 | -11.4849 | -43.6166 | 2025-09-16 12:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| b5b2a041-bb10-3acb-9c17-be1775667e4a | -8.0196 | -45.662 | 2025-09-16 12:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 307.0 |
| 956ce6b5-1c06-33c4-8d44-a3eed925ff2b | -12.6729 | -47.9258 | 2025-09-16 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| edc15623-4770-328b-b619-8fe75c056051 | -9.5309 | -45.523 | 2025-09-16 12:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 53af3e29-7a34-3424-aedf-dcc3bbc5bd60 | -9.0857 | -44.8893 | 2025-09-16 12:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 5ff40fab-b765-377b-8bb9-cb54bdc99d01 | -12.6906 | -48.0121 | 2025-09-16 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 272.5 |
| 80c955f4-00a3-3fcc-a91b-e02496c870d0 | -8.6127 | -46.4124 | 2025-09-16 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 7a6e25e1-0be5-3bbf-acbe-eeefa4d6bbf5 | -11.4853 | -43.5929 | 2025-09-16 12:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8b902dfa-d2bf-3aba-b590-57e9dd720782 | -8.0007 | -45.6638 | 2025-09-16 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 250.9 |
| d9894749-f8d2-3594-aabe-0342e81351b1 | -8.5939 | -46.4143 | 2025-09-16 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b1590b5b-fd3e-3022-8cf5-9c7387899894 | -12.6356 | -45.7422 | 2025-09-16 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.5 |
| bac9610c-6823-32e7-ad21-54ca57f5191a | -8.907 | -45.5252 | 2025-09-16 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.5 |
| d4a44651-c5ff-33d4-985c-fc79dcc359e4 | -9.7406 | -48.1326 | 2025-09-16 12:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 4bbd320c-87ec-38c3-a20a-7917a2435f0b | -13.2801 | -54.2228 | 2025-09-16 12:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| ee74d87f-86cb-322b-9125-7b9f09285d42 | -8.0196 | -45.662 | 2025-09-16 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 305.7 |
| 6b11e2e5-72de-3e5e-b517-8e2cd9060ff2 | -8.9259 | -45.5231 | 2025-09-16 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 89a3b806-923e-3bd2-8e2c-d082c606c730 | -12.6906 | -48.0121 | 2025-09-16 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 261.3 |
| 5506c4dc-2d69-32ed-83b8-9c005cd8f1bd | -5.7858 | -43.9378 | 2025-09-16 12:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 39fd225f-cb12-34dc-98c8-86af0bfd7fce | -10.9004 | -47.8027 | 2025-09-16 12:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 74051aee-8e82-31c4-80bc-16db2dc02503 | -8.6127 | -46.4124 | 2025-09-16 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 180.8 |
| b0a03d3b-f3e8-38c8-9053-29d112edfc71 | -8.9568 | -46.0398 | 2025-09-16 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b4c90468-f37e-37ad-b381-9675565fca76 | -7.9822 | -45.643 | 2025-09-16 12:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 3836413f-c647-3280-9294-4a7f0ba209aa | -8.9571 | -46.0172 | 2025-09-16 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 15e94784-ae25-313e-ad7b-ab7527207bc0 | -10.7302 | -46.5082 | 2025-09-16 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 9edb1c0e-6470-3861-92e4-98d6e3808a8d | -8.613 | -46.39 | 2025-09-16 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 3081c6ba-7f80-3e2d-a54c-6d6334709cde | -12.6909 | -47.9899 | 2025-09-16 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| cc3bac25-7b3d-3967-b5be-e6dcb534e2fe | -9.5309 | -45.523 | 2025-09-16 12:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 2cfba76b-bbc5-3f28-ae4c-3301399ca114 | -12.6953 | -47.7446 | 2025-09-16 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 2c670f39-aab9-3b78-9e6d-b459b871b1f6 | -5.8086 | -43.4956 | 2025-09-16 12:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b715d27c-55c3-325f-86da-8067e2c4f6aa | -9.7409 | -48.1106 | 2025-09-16 12:20:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 1f222b19-030d-3dc3-b364-c4e15c1ea505 | -12.6352 | -45.7652 | 2025-09-16 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 133.5 |
| b82d386d-4e7b-3e10-bf90-836b743e7ee5 | -4.5934 | -43.3239 | 2025-09-16 12:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a3f10dc1-1791-31ed-a321-76dda0c42e2d | -8.9757 | -46.0378 | 2025-09-16 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e7be661c-455f-3dde-b7c8-646b01260728 | -8.5939 | -46.4143 | 2025-09-16 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| afa75da0-b84d-3a41-832d-595ed7e39422 | -14.329 | -46.0857 | 2025-09-16 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 125c1d6a-ee94-3237-81dc-70571a6e6226 | -12.6909 | -47.9899 | 2025-09-16 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6da5c687-bac1-33b2-a505-87eb24e728d0 | -7.9822 | -45.643 | 2025-09-16 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| c8eb949e-d568-3a52-84d4-967cf1c58df8 | -8.0007 | -45.6638 | 2025-09-16 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 258.6 |
| 45f4cfc3-cfc4-3818-af81-885491826385 | -10.7489 | -46.5283 | 2025-09-16 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d97d0f5c-250d-3c56-b8cd-3571ade65079 | -8.613 | -46.39 | 2025-09-16 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c19b0ab3-a129-3a89-baec-0f44431f73b9 | -8.001 | -45.6412 | 2025-09-16 12:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1a1f0bf9-1752-37b3-91f7-1a12c9df4554 | -12.6352 | -45.7652 | 2025-09-16 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 196.3 |
| e57834ef-0d42-3c6b-a609-dc89a622ddfb | -14.3295 | -46.0626 | 2025-09-16 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| b5879158-ba46-34ae-b354-f08b54c56153 | -4.5934 | -43.3239 | 2025-09-16 12:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f796dafc-814d-35be-824a-e4abbdde74d0 | -12.6906 | -48.0121 | 2025-09-16 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 07962396-f16d-3626-b49a-c264c7e623af | -5.8086 | -43.4956 | 2025-09-16 12:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 9aa7cde4-9a45-3eec-9f86-054b91a27bfc | -4.6121 | -43.3227 | 2025-09-16 12:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 284b12f5-c038-3550-9714-32e44deca8d8 | -8.6127 | -46.4124 | 2025-09-16 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 097a0670-fb4a-305d-8a84-afef05bac00f | -6.337 | -43.1727 | 2025-09-16 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 46e314a5-a926-3267-93fb-54ccee21fe1b | -6.3372 | -43.1492 | 2025-09-16 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |


[Clique aqui para ver as próximas entradas](README91.md)
