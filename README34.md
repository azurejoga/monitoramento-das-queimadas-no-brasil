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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea4fdac-edc0-3857-b07f-27a77f14ecda | -12.71358 | -45.3833 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be1867f4-f6a7-34f3-87e4-f40514c0c18e | -22.56848 | -43.92622 | 2025-11-18 04:23:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64d26759-7541-35d6-b8b9-1db4abef3508 | -12.6995 | -46.79557 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8ef37352-dc0a-36e1-8b4b-3c5f2a277b26 | -11.84663 | -49.22498 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 63fa702b-b56d-35f6-bb19-6ea47bd68322 | -13.09345 | -42.96938 | 2025-11-18 04:23:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 03a5cf26-47d6-36cd-8215-ee95cbddbbf9 | -12.00433 | -49.26838 | 2025-11-18 04:23:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1b3b6635-db1f-327e-a981-64a1389beb93 | -12.71966 | -45.3879 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 06f36c3f-fa2b-3de0-a4e4-db6bb329f967 | -12.69788 | -46.78434 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e60e8cae-2502-301b-90e6-f0f5fc632f50 | -13.68438 | -42.02849 | 2025-11-18 04:23:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c7f08872-c077-38a1-ae08-acf0c64d22a7 | -16.10301 | -45.94901 | 2025-11-18 04:23:00 | NOAA-21 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2483712c-faa5-3eb7-ae90-05f243b4e823 | -12.01717 | -46.76312 | 2025-11-18 04:23:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d27f8fd-a4a3-3580-a3c4-f52cc5b60dbf | -12.70282 | -46.79612 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 32485d9c-e1a4-3fac-bf64-33fa7a904e77 | -12.60333 | -43.25405 | 2025-11-18 04:23:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f14299a-9371-3d57-98bf-9a0a61fc4c6a | -12.74565 | -45.39572 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5dbdd2f4-6fa6-37ed-b439-9a9991c218d5 | -12.26324 | -46.77841 | 2025-11-18 04:23:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d377985-12cb-3c1c-babc-268e817aff65 | -13.21356 | -53.76964 | 2025-11-18 04:23:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1c50427-e3e9-373b-a626-46398b776950 | -13.55167 | -47.37928 | 2025-11-18 04:23:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a11bc35a-a7b8-30d6-86e1-d42879aca979 | -12.43253 | -47.88214 | 2025-11-18 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c323d5e2-957a-3386-b886-4376feb1dbed | -11.2061 | -49.41678 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a3ccb544-db77-3099-a7a0-b6997e126b26 | -12.86358 | -46.40469 | 2025-11-18 04:23:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2f367aa-bf28-33ca-bd57-7b804822d4e3 | -13.86139 | -43.87843 | 2025-11-18 04:23:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee1b5db-1427-3d7b-97d7-d21f117acaa9 | -13.80007 | -46.82854 | 2025-11-18 04:23:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7e2ce49-65f6-3c43-a50c-8572e00648b2 | -12.40564 | -47.55618 | 2025-11-18 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86cdb15c-76e4-3382-b1ea-3807bf2943e5 | -11.4718 | -49.73354 | 2025-11-18 04:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6740f574-b8e2-3abf-a9aa-117cdeea3658 | -12.0166 | -46.76668 | 2025-11-18 04:23:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d71f6d1-5043-314a-97d1-3808d103d5e9 | -11.92947 | -44.80227 | 2025-11-18 04:23:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f905fbb4-bc72-3cd3-9445-60212c60cfa0 | -12.8576 | -41.4837 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 867d64f2-6bf5-3be0-b84a-0c96bcb1ad1b | -12.66201 | -46.75292 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36cec7ea-9478-3988-90c1-38d1d20e2c70 | -12.43192 | -47.88589 | 2025-11-18 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e8a59f8-5790-3551-b4a4-5a0c4e3cfc82 | -11.83955 | -47.5955 | 2025-11-18 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5000a9d6-2de0-3ff6-b3f5-d2b63e734bee | -11.817 | -45.29031 | 2025-11-18 04:23:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b747bf89-0f35-3679-b975-5406a07870ea | -15.50945 | -41.53759 | 2025-11-18 04:23:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 45583fb1-fad4-3713-a53b-9b2632c789de | -12.855 | -41.47392 | 2025-11-18 04:23:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2924a83d-c6cc-329f-b153-f19208436ba6 | -10.99211 | -50.92574 | 2025-11-18 04:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea4b5385-2444-3d8a-94cf-52c2d958878a | -12.74233 | -45.39518 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ab6aaf18-ad23-308c-a90d-4d0c61a7656a | -12.73901 | -45.39465 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a90444-8589-3727-a0ac-c1236b5fe97e | -13.84007 | -41.79421 | 2025-11-18 04:23:00 | NOAA-21 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c1834a5-eaae-3a80-996a-7b65f448fae9 | -12.73847 | -45.39819 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15864d43-a31b-3776-ac5a-af2535d696ee | -15.50138 | -41.53659 | 2025-11-18 04:23:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cc2cb443-3a84-3489-b6a3-b48e3f39beb0 | -11.83894 | -47.59923 | 2025-11-18 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1fb88065-3cbf-3411-8b42-ce4f421a99da | -11.20981 | -49.41739 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 01af8a3b-7d39-3ca8-8639-f11ef853102f | -10.99617 | -50.92646 | 2025-11-18 04:23:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c8eb056f-a7df-3ff1-9934-dcd605645b0f | -12.70291 | -46.77422 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb7bcf36-73e5-36ff-9317-efc37eb59126 | -12.69959 | -46.77367 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 182b7eb3-c5ec-31f3-b400-a823c7ca7823 | -11.59481 | -48.60529 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7fe10a20-0d28-388d-87f9-0ca8a7b8261d | -12.40504 | -47.55986 | 2025-11-18 04:23:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bffbfa6-654f-390b-9b7d-e7a4bdeb96d3 | -11.52301 | -48.95523 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bdc89b95-bb46-3d6c-9f5f-ae20e730fdb3 | -12.89664 | -54.72516 | 2025-11-18 04:23:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f405077-226e-3b08-af2d-fc418494536c | -11.2024 | -49.41616 | 2025-11-18 04:23:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b29e48b8-e4bc-3b7b-8c96-268f3931b297 | -15.89281 | -42.17094 | 2025-11-18 04:23:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6a5dbd2-5ba5-3d75-9f4c-1e7e95df71ac | -11.84294 | -47.59608 | 2025-11-18 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 833ff9d9-5b25-36e9-9da2-eef06c914781 | -12.7158 | -45.39092 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b93084b-37d5-308b-9e3c-62e1ed727c39 | -12.00221 | -43.83536 | 2025-11-18 04:23:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8598bb2-938b-34c7-8e2d-783f31e82e70 | -12.70615 | -46.79666 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f98f781-8e2f-3f85-9d6a-561b3bbf0194 | -12.73353 | -45.4301 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bcef6121-1243-3880-92a7-7cb6a4e189ee | -12.69902 | -46.77723 | 2025-11-18 04:23:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 33356d7d-e917-3ae0-adda-00c43db0356c | -11.93281 | -44.80279 | 2025-11-18 04:23:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b27b873-a4b5-3b5f-8044-6f76e9f04272 | -12.06954 | -48.19085 | 2025-11-18 04:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d203c41-0678-3d44-8d80-1adc569544d1 | -14.47538 | -42.89571 | 2025-11-18 04:23:00 | NOAA-21 | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2f41085a-aab5-3679-ac05-4ec01b1e7384 | -11.57366 | -48.14518 | 2025-11-18 04:23:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5053744-c748-38e0-8b28-56663de52e66 | -12.88036 | -46.06068 | 2025-11-18 04:23:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 309f08ff-cf02-328e-a697-6a9ad38d2349 | -11.84234 | -47.59982 | 2025-11-18 04:23:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6969899a-8cd3-32e8-a6af-b5b739479c80 | -22.94391 | -42.91721 | 2025-11-18 04:23:00 | NOAA-21 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1355e660-245c-32e7-81e9-6c3e45ab460f | -29.89007 | -51.23439 | 2025-11-18 04:25:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 8d036e8d-9297-31b9-b21f-bd530cf9380e | -31.79263 | -52.6234 | 2025-11-18 04:25:00 | NOAA-21 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 5e7d823a-7240-3bbd-97d9-97d37a0702ac | -9.3969 | -48.4523 | 2025-11-18 04:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 0de18a5d-2354-3954-b343-a70da096470b | -1.9292 | -48.7946 | 2025-11-18 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 7d08f437-a6f8-3c7b-8f32-06366480be84 | -4.6547 | -47.9444 | 2025-11-18 04:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d0b2f02e-cd1f-3435-8168-867e58c20257 | -1.9107 | -48.795 | 2025-11-18 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| c9f63330-454d-3bdb-a774-612590cea53a | -1.3373 | -49.3159 | 2025-11-18 04:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 493bfdc9-ec78-37eb-a2f6-360b0fc349c3 | -9.3969 | -48.4523 | 2025-11-18 04:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 89ecdadc-a796-3a5f-a56a-bd3a3188abfb | -11.6563 | -44.7371 | 2025-11-18 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| ec8f738b-5a98-3893-a902-c6af45a7eea6 | -11.6755 | -44.7342 | 2025-11-18 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| c977cc7f-b4c4-386b-b6ee-67360c0e4c64 | -4.6361 | -47.9453 | 2025-11-18 04:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 27853ee6-84ed-3557-8718-dec85e42c6b1 | -4.1764 | -44.2257 | 2025-11-18 04:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 2246ed2a-414f-30e0-a389-f118a55e5583 | 0.81131 | -51.8471 | 2025-11-18 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4aa611dd-8cea-33d5-a433-5f24dfab54b9 | 0.81193 | -51.85101 | 2025-11-18 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 760dc48f-c636-3af7-93ca-1a99368ec09a | 0.81203 | -51.84793 | 2025-11-18 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d3e662e9-7c83-3ded-bcd2-f58d7fd8c865 | 3.66099 | -51.29763 | 2025-11-18 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df78237d-0843-3d17-bb73-7e4c76824d4d | 3.65747 | -51.29817 | 2025-11-18 04:46:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f471efc3-9236-343f-853e-ea3ffd5353e6 | 0.50611 | -50.16729 | 2025-11-18 04:46:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e04e6b-d7a6-3b6f-b4c8-3e8d508863b6 | 0.81264 | -51.85184 | 2025-11-18 04:46:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 871533e5-72dd-32cb-a53e-fca7e682083c | 0.65928 | -51.53862 | 2025-11-18 04:46:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25ad2739-d075-3841-adb6-1b3abae23a84 | -2.9972 | -51.06274 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 009cf4cc-8760-360d-a7e4-ab855e5a342a | -3.51792 | -50.32178 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1fa9dbb-cfe4-3283-b997-b334174dbd76 | -3.48513 | -52.35549 | 2025-11-18 04:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5330d5f-e3ec-31e2-855d-f588e36c130b | -3.17578 | -48.02921 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b99a9b84-aae7-3388-8d54-8ca974121d5e | -1.68147 | -53.19589 | 2025-11-18 04:48:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5efc73-7684-3319-a9c2-b4148ea77a1e | -2.34052 | -55.79593 | 2025-11-18 04:48:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88be2b94-ca70-353b-b754-1b0f44b2dd6b | -3.02837 | -47.83929 | 2025-11-18 04:48:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f9ac64d1-4053-3c43-be34-b37bd6581a96 | -2.85555 | -49.60867 | 2025-11-18 04:48:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 983e9a89-0a3b-3f23-b576-c728bcaeeba8 | -3.21312 | -50.92163 | 2025-11-18 04:48:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c662551a-40eb-3df0-a75d-0e8288555a36 | -3.13012 | -49.24008 | 2025-11-18 04:48:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 293ebe7c-c6cd-3991-82c9-6fdfd3a7a5d1 | -3.67054 | -50.21504 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e21a6647-7d83-34d5-a62d-f3de1d8823ac | -5.21727 | -49.58375 | 2025-11-18 04:48:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6d0ad3e-d0f4-362d-8168-7fa591979084 | -6.4399 | -43.81263 | 2025-11-18 04:48:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6887b392-7307-3758-ab60-c0a1f8861405 | -5.17283 | -44.34157 | 2025-11-18 04:48:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13b6a010-8ce5-3cc2-8633-320cdb5b16e9 | -3.40107 | -50.4414 | 2025-11-18 04:48:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ebd06b9-6d67-328e-8578-2ed0085c23de | -6.2153 | -46.88849 | 2025-11-18 04:48:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd17bbb3-979e-3443-9f77-3deb27c21c0e | -2.9226 | -47.84761 | 2025-11-18 04:48:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README35.md)
