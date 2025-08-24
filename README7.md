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
| 99cf23cd-a566-3ac0-8821-1f8f86e54d05 | -3.586 | -47.5159 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78a9928e-dfea-3b3f-b641-6eb3fc400418 | -8.7529 | -46.753799 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3ba93d0-a38a-3845-8a7c-d4ee1c7c438e | -17.3867 | -42.633999 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5fc4adc7-8d58-3ae3-b272-2ee6679e7b15 | -5.4156 | -44.980598 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a99c8556-767e-3b6c-81d3-fd71bbdecfa9 | -5.7388 | -45.350201 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37e15212-73d9-334f-9b24-5a807c76f167 | -5.4075 | -44.9902 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d0ef049-7f14-3aff-970a-9fd2c1e26dd6 | -6.0901 | -44.6856 | 2025-08-24 00:34:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93da61d0-734b-3cd0-8ed1-5556ca4620d8 | -17.384899 | -42.626499 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3596d1fb-1762-326e-a401-61d1b69cc888 | -3.6928 | -39.578602 | 2025-08-24 00:34:00 | METOP-C | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| de4695bb-b860-3a12-b6e3-fa83e36660ea | -16.802099 | -51.364201 | 2025-08-24 00:34:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e0789d0e-814d-3c12-a260-23e1af113003 | -8.7612 | -46.744701 | 2025-08-24 00:34:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c32d29e-7562-3b2f-a6e9-f877afb0323c | -5.8548 | -52.0676 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 879c63f4-e0c1-3a11-b38e-d0164bf7c52a | -4.4753 | -47.6618 | 2025-08-24 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f676508-0374-363c-ad38-563842a96d06 | -11.1206 | -44.7901 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1e26dc7-41c6-372f-a663-12bf63e30e49 | -20.341101 | -51.682899 | 2025-08-24 00:34:00 | METOP-C | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 306ba4f3-aac1-38db-ac1f-bdf2358767d0 | -17.6075 | -44.290699 | 2025-08-24 00:34:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e43fa263-ae8e-3412-87ee-a4c08b3312fa | -4.9622 | -55.8284 | 2025-08-24 00:34:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 005d8df5-73d1-31dc-a9c1-3f0f76f0c052 | -10.5991 | -50.194199 | 2025-08-24 00:34:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d02d89b4-8dd0-3155-839e-3c7019651d18 | -20.082399 | -46.1063 | 2025-08-24 00:34:00 | METOP-C | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d603d103-e706-3770-b3ad-672a6020287d | -22.5464 | -43.715599 | 2025-08-24 00:34:00 | METOP-C | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab093f8f-d6b4-3880-9b9b-481e930018b6 | -7.0768 | -44.622799 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 83b03e7f-0a2b-3ce2-8bec-480131ea75d1 | -7.6951 | -42.124802 | 2025-08-24 00:34:00 | METOP-C | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4b1c0cf-c1df-3d53-a0e6-2f3fbfe6d848 | -9.833 | -47.759399 | 2025-08-24 00:34:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6b4d33c-1e74-32db-ae91-cc54abb66e4c | -3.381 | -47.611801 | 2025-08-24 00:34:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6289a1b-865c-3c8b-9ec2-8dac23db717b | -8.5181 | -48.8787 | 2025-08-24 00:34:00 | METOP-C | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 787302e7-0757-39e1-8e05-4d0c91452f45 | -6.9109 | -43.781502 | 2025-08-24 00:34:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f10276aa-7bf5-39be-917f-e02acb8fc376 | -13.0329 | -45.215099 | 2025-08-24 00:34:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38fb8cf2-2c2c-3da9-976c-f63152ef97de | -17.610701 | -44.305 | 2025-08-24 00:34:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d0c58c9-dc10-30a1-82db-e79c4de0f169 | -7.0163 | -44.629002 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a53037c0-2097-332c-964f-87b157cab97d | -10.6023 | -44.3339 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 388da6c2-38f9-32ec-9c6f-7f4240a982a4 | -11.5491 | -51.903999 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c893e14-c2c1-3504-b17d-21453f2af5bc | -11.3324 | -47.844799 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b2fd2e81-d1f6-323a-b63b-222638350a84 | -20.7782 | -43.441502 | 2025-08-24 00:34:00 | METOP-C | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 972498a8-bc47-3843-aea3-57057d3452b1 | -7.0197 | -44.6437 | 2025-08-24 00:34:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebc583d6-7e41-3b1f-b568-c9a4e4bd1887 | -5.6593 | -45.140701 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4404f06-94fe-3239-8a41-9f4f7fdc97fa | -12.2086 | -47.106701 | 2025-08-24 00:34:00 | METOP-C | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac963002-75b4-3d0b-b6dd-4df7a7308dbf | -4.4768 | -47.668701 | 2025-08-24 00:34:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 956111f1-f80f-35aa-9af1-696b293ede81 | -11.3226 | -47.846901 | 2025-08-24 00:34:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e17ed45a-2a73-305b-8263-1d8959123395 | -22.1429 | -43.657299 | 2025-08-24 00:34:00 | METOP-C | RIO DAS FLORES | RIO DE JANEIRO | Brasil | 3304508 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1dacaf9c-b735-3c77-b16a-9be0b346af9d | -21.0909 | -47.049198 | 2025-08-24 00:34:00 | METOP-C | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d346c05-6302-3298-aabc-2dc988012bd5 | -19.767599 | -43.1605 | 2025-08-24 00:34:00 | METOP-C | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28e2c12d-84c0-3c93-aff3-194a792d3298 | -10.7564 | -48.263901 | 2025-08-24 00:34:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 17ce6eac-a293-32c2-a627-886ab38aff85 | -8.847 | -49.908501 | 2025-08-24 00:34:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e46aa9f3-59ee-348b-b65b-7f714a8e2273 | -2.9241 | -53.676102 | 2025-08-24 00:34:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0829aa-ac47-3f86-a055-82f3c7c28e6d | -10.6007 | -44.326698 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96fa0c14-01e3-3c25-a4f9-4c6912cbf5a0 | -10.6088 | -44.3172 | 2025-08-24 00:34:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d9d1ebd-9637-36c2-b572-a13873695a3f | -8.2223 | -45.111198 | 2025-08-24 00:34:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 264c55ff-72bb-370f-b635-7047f55183e8 | -10.8076 | -46.406898 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a128084f-9474-3e7d-95c6-2c93341b33ce | -5.8572 | -52.078499 | 2025-08-24 00:34:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcca6f42-340f-3645-ad4e-81a04b030965 | -10.8126 | -46.383701 | 2025-08-24 00:34:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8cd94f77-7ce1-30cd-9984-7d019e385ee5 | -15.7034 | -41.9361 | 2025-08-24 00:34:00 | METOP-C | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4285bc0a-2922-3996-9118-741f5cca963a | -5.5014 | -47.5047 | 2025-08-24 00:34:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8db1161d-0c5a-3ead-92c2-6bcfb91e199d | -17.404499 | -42.621601 | 2025-08-24 00:34:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8cbebd60-e91b-3678-886a-9003cc4353e9 | -14.812 | -47.945099 | 2025-08-24 00:34:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7f7a8ff5-6163-3b9d-808c-e1f27702ca43 | -15.9681 | -43.022099 | 2025-08-24 00:34:00 | METOP-C | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 14aaa832-2379-3217-8660-dbc5ecfe5bb7 | -20.375 | -46.738098 | 2025-08-24 00:34:00 | METOP-C | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d40b94b4-2ec6-33f5-a2d6-563c42929e24 | -6.0335 | -44.001701 | 2025-08-24 00:34:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dea9e335-b071-3a6c-8070-8e59451b4987 | -3.4387 | -49.038502 | 2025-08-24 00:34:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 779d3ca0-9d7c-37ce-9f87-e8bce3120232 | -4.958 | -55.809399 | 2025-08-24 00:34:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14263ea5-e4ce-3a12-a335-7fb26d7fcd34 | -9.6378 | -40.592602 | 2025-08-24 00:34:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e63b518e-f4e0-38fe-87fb-c26760f24f9f | -3.059 | -49.497898 | 2025-08-24 00:34:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21d5b821-ac79-35d1-867c-870a38021638 | -3.7927 | -47.562801 | 2025-08-24 00:34:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8471ac-0314-3ffc-bf14-bc4169b02419 | -19.630699 | -43.194302 | 2025-08-24 00:34:00 | METOP-C | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f760396-670d-3ff1-8b37-6a442bce001f | -5.4093 | -44.997601 | 2025-08-24 00:34:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa9022e5-2602-3421-bdda-ce3d743e6575 | -9.0046 | -65.6988 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 5a2261df-b68f-3e4c-b0e7-fc7dffa15759 | -9.0232 | -65.6982 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 9a9076b7-e747-3849-8f81-17edbec376a9 | -20.3396 | -51.6839 | 2025-08-24 00:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 123.3 |
| a5e1bf30-3041-3c00-a11d-58b9476edb79 | -16.7965 | -51.3637 | 2025-08-24 00:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 3731f526-2cf9-3dc7-ad47-a68894dbe785 | -9.0246 | -65.3807 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 52593c88-cac5-32fb-a857-28dc20d86ea1 | -17.6183 | -44.2738 | 2025-08-24 00:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 7dbc797b-a2cb-393a-8bba-b99520fea464 | -8.9106 | -62.4289 | 2025-08-24 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 496a3c44-ffbc-34de-9ce4-f51272abce3c | -16.797 | -51.3419 | 2025-08-24 00:40:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 1551bdd2-45f6-37a2-8bdc-60f96e4847c9 | -3.5995 | -47.5142 | 2025-08-24 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 443dd13b-f44d-3aa4-846e-72d4cddb5922 | -10.5819 | -50.1863 | 2025-08-24 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| fc8b556f-6695-310d-a38f-a4acca11f806 | -17.6176 | -44.298 | 2025-08-24 00:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 123.5 |
| fa7a20f2-7ba0-3ab0-97c6-f4b0b8ce5737 | -17.3844 | -42.6235 | 2025-08-24 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 56c4c082-995f-3b7e-af56-d5a1efc8495b | -22.065 | -53.8023 | 2025-08-24 00:40:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 166.7 |
| 690336e6-09d1-318d-b279-2ea51fa16154 | -3.7847 | -47.5719 | 2025-08-24 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d2f902f5-2ce7-377e-8799-192dae1c92a7 | -9.0231 | -65.7169 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 154.3 |
| a6fef348-2224-3e2f-9ec8-ab633b1394ee | -10.6128 | -44.3284 | 2025-08-24 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| edff9801-978e-3320-9c17-d151e0aa5d3d | -17.7962 | -40.1692 | 2025-08-24 00:40:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 104.7 |
| a5e0c8c7-e04c-305e-aae7-fdd490846dce | -5.4547 | -60.1964 | 2025-08-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| ff5c8a1c-8d93-3935-b693-794b37088a4a | -8.6131 | -62.5929 | 2025-08-24 00:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 29a2b0a6-c193-3944-913d-a19feef70c7b | -11.5055 | -51.8705 | 2025-08-24 00:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4479971b-3d8a-38cd-8ca1-7d1c8ac4c1bb | -17.5975 | -44.3027 | 2025-08-24 00:40:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 38dfc408-3c78-3e45-bd80-dfe4fe79e815 | -9.0416 | -65.7163 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 287cf1d4-4e24-3f4a-a12b-e5b0d9fc5657 | -9.1441 | -60.7765 | 2025-08-24 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a6afac6d-2ff1-37a9-8afd-ae5773a03da6 | -4.9421 | -55.8233 | 2025-08-24 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9b2577c8-3c1e-318e-bc13-00c4f3009944 | -11.5429 | -51.9086 | 2025-08-24 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9fbfd9cc-3a96-3d5f-b673-accddecf3933 | -9.0061 | -65.3813 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| db8b7874-e686-3968-b1e4-011dde0e9ae5 | -17.4045 | -42.6186 | 2025-08-24 00:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b0487eaf-f736-34da-8a2f-de23512b7c72 | -9.0045 | -65.7174 | 2025-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 80af4f0d-7f03-33ce-b86f-5f9885c47bcc | -20.3594 | -51.7023 | 2025-08-24 00:40:00 | GOES-19 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 5c75db6c-73e8-3b00-a0d9-90f4d8293c0d | -11.5245 | -51.8685 | 2025-08-24 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 65f75046-ab63-396a-bdf1-ade03ead4d32 | -4.9605 | -55.8226 | 2025-08-24 00:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 21245779-8626-3622-9df5-60000d90135b | -22.0655 | -53.7802 | 2025-08-24 00:40:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 186.4 |
| b9889197-62ce-3254-899f-2fc8de9e6745 | -5.4365 | -60.1588 | 2025-08-24 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b5133948-b31b-39af-b027-3d2dd2b2788a | -9.1998 | -60.793 | 2025-08-24 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 1e3966b5-a261-30bf-a9dc-2487b4845959 | -22.0862 | -53.7763 | 2025-08-24 00:40:00 | GOES-19 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 231.7 |
| 9184e62d-12ce-37ef-b8b5-08f23ccf2f9f | -7.5534 | -63.8556 | 2025-08-24 00:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |


[Clique aqui para ver as próximas entradas](README8.md)
