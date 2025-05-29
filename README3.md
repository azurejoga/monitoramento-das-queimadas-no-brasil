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
| 4e924c03-d700-3835-aaa6-7d24489e9cdf | -6.2362 | -43.3719 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b8a2647a-5562-302b-b41b-ed7e6dc87b72 | -10.67173 | -44.4127 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d86ab45c-6d3c-3acc-b5b4-c4bd413663aa | -7.24683 | -43.10286 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| dfe5a41e-288e-388e-aa64-244fd995ca17 | -10.66201 | -44.41182 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51c17cd0-d57b-3db0-9b99-4f811f18616f | -10.67637 | -44.40923 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b520e117-8607-3716-931c-43d6920ef211 | -10.67821 | -44.41484 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 63a8365a-5d01-39aa-b99f-fa7fbb0d6fc7 | -6.34677 | -43.37468 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9120afd8-9a93-3065-bf98-1e4f13a37967 | -7.53879 | -43.3623 | 2025-05-29 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eebafe2-74c8-32df-8171-1674365e2097 | -10.66512 | -44.41116 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9377cd8f-598e-30fa-9706-29b0904d1e6b | -6.24288 | -43.37328 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 821592ac-f4f8-3d8b-8049-e2d0975730ba | -6.23836 | -43.38311 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 69716072-c252-30a7-bfa9-9b778fc08103 | -10.67516 | -44.41513 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f42381a-af08-313e-9eb9-256872e9379c | -7.18605 | -43.10351 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 3f739f02-30cb-3c24-9ae1-38db5724dfcb | -11.58427 | -37.65741 | 2025-05-29 03:23:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f13274de-2646-3fef-8bb7-6bc87a79bbc8 | -7.61795 | -43.4122 | 2025-05-29 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ff5bc7a5-a4a6-377e-b4c4-c7a7ff8592d3 | -7.19153 | -43.11018 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 9e96dcdf-c9e4-3803-ab39-b646128ae22c | -6.2237 | -43.34941 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 87e6854b-d69e-3254-90ed-fd6358e753b7 | -6.53556 | -44.4654 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06d86974-6f69-3b10-9055-3f5c8b719b9b | -6.33891 | -43.37969 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 303df514-13b6-32b6-ba89-2961686718c6 | -6.22476 | -43.34364 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 36.1 |
| eb7ba8d4-21a5-3a3d-9c90-a4f138ebeaea | -7.19265 | -43.10849 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d32da529-227c-3c8e-8ea2-7059d90af959 | -6.53682 | -44.45874 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49470e3e-c5b5-378e-8d84-8092839de9f4 | -7.24033 | -43.10164 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f077e7b0-984b-3b89-a94b-7866ccd36a1a | -8.89573 | -44.78564 | 2025-05-29 03:23:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f607033-8135-3ac5-b959-2e9e97bee4fa | -6.34349 | -43.3713 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 17bd7c42-db85-3d05-afd1-69169be12a03 | -7.54083 | -43.36103 | 2025-05-29 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f2d4075c-7038-3492-b2f4-28b5e0d1a192 | -7.23484 | -43.09494 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 9af99141-862f-3e2d-b203-ec8ce6f2f5e5 | -10.65522 | -44.49569 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5e029050-48d3-3958-80ec-1d34cce9b023 | -10.65823 | -44.49747 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 65aff1d1-4890-3c9b-8e8b-0a3bd8ce2542 | -7.18614 | -43.10721 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| eb1425c1-bd61-386f-adf0-a8ba3abf0990 | -6.24177 | -43.37919 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 539be9ab-ca15-3707-a962-7e430492d74e | -7.24135 | -43.09616 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f0358be4-7a41-35da-82c1-6d5316590d56 | -7.54189 | -43.35533 | 2025-05-29 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bb3cd129-fae4-3eec-9d96-e66c94fd75c1 | -7.6169 | -43.41778 | 2025-05-29 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dd59c3f-39d5-383b-a6d5-04e2211b13df | -6.24057 | -43.37102 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 671d6fc8-5d89-33de-8edb-1eb614879b1e | -6.34006 | -43.37342 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ecca9ce7-c012-3ab7-bf0e-c1a35f181bb0 | -10.66864 | -44.4132 | 2025-05-29 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8431dd0a-dd2d-3786-9d42-0d955c9f0854 | -6.34231 | -43.37747 | 2025-05-29 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3fae45d5-9658-36a5-aef5-bdf1d3c2a2c5 | -7.28014 | -44.2217 | 2025-05-29 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 885a7570-6ed3-30c6-ae8b-49ad6411eb0c | -7.5399 | -43.3566 | 2025-05-29 03:23:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f969c13e-17d6-3737-9790-d38bc4c906be | -7.18515 | -43.11265 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| f609864d-c055-3079-9091-f28e93867ecc | -7.19257 | -43.10471 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 122f5c55-24ff-3447-88f0-ec878bf9cb50 | -6.2395 | -43.37689 | 2025-05-29 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2e4aba46-6c06-376d-a0d8-587ac5c77095 | -7.19365 | -43.10296 | 2025-05-29 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 2e75994f-c5be-3a26-a8bd-18c42a69a167 | -14.67377 | -45.08982 | 2025-05-29 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e62125ca-d3fd-38fd-ab90-0173b8cde983 | -13.08499 | -45.28397 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b61d629c-f3d7-3426-ac1a-3b5da38d7856 | -11.91822 | -44.55579 | 2025-05-29 03:25:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da1d29dd-2f61-35af-b81b-a22b83dad74c | -15.80495 | -43.5723 | 2025-05-29 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f56264ec-6a6b-34fc-8474-7dad5aca902c | -11.81712 | -44.26624 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| ffad8523-9b35-38d8-a4f5-83f6b9d34104 | -13.08128 | -45.28829 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 98f55b12-1b6b-32f9-8dc9-e81a9edcb569 | -18.24065 | -45.63194 | 2025-05-29 03:25:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 430b9e40-0b8e-3f7e-bfae-52cea094c71f | -15.80586 | -43.56806 | 2025-05-29 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44d6940c-8499-3e08-952c-59a0b68de774 | -11.92478 | -44.55711 | 2025-05-29 03:25:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19633efe-90c3-317a-ba10-0bf9074510f7 | -14.66736 | -45.08822 | 2025-05-29 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 75830d8b-88e2-3621-af3d-2373eaab2776 | -15.91854 | -41.36774 | 2025-05-29 03:25:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6526e93a-d78e-3ac8-977c-6701f74ba3f9 | -11.80303 | -44.26924 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f2a222c-6969-3495-850d-d3481083c473 | -11.80372 | -44.26542 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34d9f105-b706-3fe4-a6ae-3f3bb227a5cb | -13.08925 | -45.28362 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eaf29da4-0d6b-3e65-adc7-04cd9afb0c30 | -14.67609 | -45.39548 | 2025-05-29 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 215782b9-dbd4-3a51-801f-505062578276 | -13.08631 | -45.27783 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c62ac5d3-a958-324f-afa5-02daf93eea9f | -13.08256 | -45.28216 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b56b3b2-7b71-3910-bb8d-166d1f5c17f7 | -15.4815 | -41.8997 | 2025-05-29 03:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95bd933b-a98d-3a72-89f3-3b2e577ff683 | -13.08367 | -45.2901 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 652b041a-8003-3dc9-83ee-a983b8edbedb | -15.80549 | -43.56946 | 2025-05-29 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| adef23f7-31ca-3049-b9fe-d0013efc10fa | -11.80418 | -44.26369 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f60e2c98-6f95-3bd9-a929-b212ada51d59 | -15.47692 | -41.89534 | 2025-05-29 03:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6f416ebd-fba9-3f8b-a217-15e46f5d67b1 | -11.81826 | -44.26072 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6770db73-1feb-30ea-a882-a1f36a42c7f7 | -11.92005 | -44.55453 | 2025-05-29 03:25:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a52e4704-bcec-3855-84db-8fa1749dda90 | -13.08797 | -45.28976 | 2025-05-29 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3daabc1-776a-392b-b51b-93d63a973c40 | -14.68138 | -45.40285 | 2025-05-29 03:25:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f87bb72-cce7-31cd-a5d9-5a0c56d1ab53 | -11.82359 | -44.26754 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 761d53e3-59bd-33d2-bfa2-0470a707f03e | -15.07998 | -43.37635 | 2025-05-29 03:25:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 41f19fce-b7a0-3e26-a646-40f103d82dbd | -11.81598 | -44.27179 | 2025-05-29 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 0d9f3d3d-7ca8-3e14-8836-312d770cf61a | -15.91796 | -41.37071 | 2025-05-29 03:25:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e052c55e-6275-309c-9dc8-7bff3755fd14 | -3.13334 | -40.99099 | 2025-05-29 03:47:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c368e5d8-57cf-3793-afe8-39d6bee9404b | -3.12932 | -40.99033 | 2025-05-29 03:47:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8aa75cc9-b0a9-39e8-8364-4ff32431a5ab | -7.19342 | -43.10454 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc481cc0-d458-3f49-aa5a-979eb38ed841 | -7.58852 | -45.95878 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f554a8c6-69a7-3e4b-a098-1446d7a9039b | -4.48732 | -47.79402 | 2025-05-29 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9892f7e-29e7-3b04-b28e-8e0d8373e13e | -5.96584 | -43.76073 | 2025-05-29 03:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07c61cb8-a132-384a-a7f4-a9d3191c3189 | -8.01234 | -49.6835 | 2025-05-29 03:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c34394fd-44e3-3595-85c6-f6625f1c3229 | -7.06992 | -44.93523 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 401e8421-8d04-3dd2-b334-19f6197a7891 | -4.46843 | -41.61164 | 2025-05-29 03:49:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 56fa52d5-dd88-3f59-9a69-6e9bb61d9a80 | -9.39164 | -48.4224 | 2025-05-29 03:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd7bf1d6-f1a4-32f7-9fbe-a36ff7afe94a | -6.22541 | -43.34355 | 2025-05-29 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 220944a4-a5c1-3ad3-a3e6-613ed3d09129 | -7.23219 | -43.09288 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 5a63cf1e-f693-3530-8767-f7c98be91d76 | -7.58796 | -45.96201 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d0a5d04-541f-327b-82e1-077b7bd378e4 | -2.65629 | -48.80329 | 2025-05-29 03:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ae9b6b3-c3d1-3590-b160-f12ac92808ce | -5.76469 | -43.48599 | 2025-05-29 03:49:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d0b7f25-0209-3704-8316-d262d481a442 | -4.48306 | -47.79112 | 2025-05-29 03:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc485bdf-1214-388f-8f96-49b7d1e3736d | -7.62483 | -45.75088 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 428cb67a-e373-35c2-889e-6db8d5871b71 | -7.23942 | -43.10262 | 2025-05-29 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 96cc8fc6-0999-3eb2-b188-6072d817e498 | -7.62539 | -45.74768 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7deeabc6-4f5b-35ae-85b7-21b4d047e352 | -6.80568 | -45.36442 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba6cf50f-23a1-33bb-a7ec-f7d3375cc10c | -7.67717 | -46.09885 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 015d3448-b96b-3761-8d14-dfbd87a20e27 | -7.67155 | -46.09113 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6c604c0-4d07-36d5-b213-9f66ae240367 | -7.62076 | -45.74374 | 2025-05-29 03:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11d221a3-03cd-3bd0-9dab-e1d0116ad73d | -7.58363 | -45.95515 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0136da86-d6d3-3e4b-9dda-9403ff4cbe99 | -7.07683 | -44.92475 | 2025-05-29 03:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 97f64259-8fe1-34fe-9902-e637fcada3ed | -7.58441 | -45.95146 | 2025-05-29 03:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
