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

## Dados Diários - Página 309

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d429fc34-86d3-394a-8819-a8dc292ac105 | -15.70949 | -41.01888 | 2026-10-08 16:35:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 105ec9de-2e1d-36ee-8f90-7ddd4a902b39 | -14.09669 | -40.0603 | 2026-10-08 16:35:00 | NOAA-20 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| fdc2e0b1-0836-34d3-8aea-d1c299550407 | -13.89513 | -40.76143 | 2026-10-08 16:35:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| e7ef925d-5460-3bdd-8f7a-d09f20334be2 | -15.69443 | -40.46619 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| 25b75664-3f4d-321c-bffa-58c3fcded7a2 | -16.74304 | -40.43198 | 2026-10-08 16:35:00 | NOAA-20 | PALMÓPOLIS | MINAS GERAIS | Brasil | 3146750 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 56256387-aee8-3780-82de-e56ecb7f877d | -14.4126 | -41.28816 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 05b9e177-9515-3b7b-a937-84986bf5235f | -14.67256 | -40.8089 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 4389bb27-5155-38b2-8b75-77a2f42d073e | -15.39389 | -44.33725 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 08d881de-cacd-37cd-8fcd-223ec86049fc | -14.20305 | -41.84139 | 2026-10-08 16:35:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| c41ade18-14fe-33c8-a0f4-049181a45403 | -15.53811 | -41.72152 | 2026-10-08 16:35:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| b774dc81-a46a-3a38-a8c0-0afaf4c0ad66 | -15.95521 | -41.10091 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5b71218a-9192-3283-b2cb-43670dc7f975 | -13.97033 | -44.8365 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 19c65b04-b749-3b11-ae56-29a060ef9a22 | -15.21444 | -46.01696 | 2026-10-08 16:35:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3d42794a-af1d-3e84-aae7-f6627075326e | -21.01276 | -44.46228 | 2026-10-08 16:35:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bef7914e-6278-3cd1-aef2-02f02cbb152d | -13.95973 | -44.85645 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 315b2b26-e84c-3fdd-919b-ec94e8b5e838 | -16.55714 | -51.07076 | 2026-10-08 16:35:00 | NOAA-20 | AMORINÓPOLIS | GOIÁS | Brasil | 5200902 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cbb65a4d-051c-3939-8c15-bd2c22403496 | -14.7342 | -40.28848 | 2026-10-08 16:35:00 | NOAA-20 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 10f8a7dc-fc1b-32f4-9ea8-28be786445e6 | -14.72926 | -41.60328 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 24.3 |
| fd3d7072-2a12-366a-a052-4ff5d1f0b2d0 | -16.91344 | -40.88887 | 2026-10-08 16:35:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 043381fd-360b-3734-842e-92812a0de9f1 | -13.97893 | -43.25893 | 2026-10-08 16:35:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7a115e76-faeb-3e1f-a28a-3ef55e7bb154 | -23.18533 | -52.08558 | 2026-10-08 16:35:00 | NOAA-20 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2a86440c-4b54-3f1b-bd38-2952776c53fc | -15.14396 | -44.05304 | 2026-10-08 16:35:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 003c3cdb-f3c9-3215-92dc-312ac808d7b3 | -15.69514 | -40.47041 | 2026-10-08 16:35:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.6 |
| f57369ca-0196-3e8e-a138-edf1f5b75a38 | -14.76064 | -39.8089 | 2026-10-08 16:35:00 | NOAA-20 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 255c842b-82d3-317c-9a5c-9d5b15cf9964 | -17.45155 | -45.05626 | 2026-10-08 16:35:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d8728fc1-f1c1-3d7c-af45-4a40d37450e0 | -17.02307 | -49.71079 | 2026-10-08 16:35:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd2f51ec-cb24-3c91-a46c-90743dfac6d9 | -22.57659 | -46.52491 | 2026-10-08 16:35:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ce10090d-1f42-331f-8118-0450b0fbe51b | -23.20128 | -51.55354 | 2026-10-08 16:35:00 | NOAA-20 | PITANGUEIRAS | PARANÁ | Brasil | 4119657 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3bb89616-6c7e-3160-9428-789342015875 | -17.244 | -41.97235 | 2026-10-08 16:35:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 42f8b109-c1dc-3bf5-a0ed-fbf1d79c7a15 | -16.05255 | -40.64562 | 2026-10-08 16:35:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 2a8d73c6-5902-36e7-bbb6-b74fba0fd546 | -21.4232 | -42.16824 | 2026-10-08 16:35:00 | NOAA-20 | MIRACEMA | RIO DE JANEIRO | Brasil | 3303005 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 17e137ec-bf3e-3d97-a19e-6bb51779054c | -16.90461 | -50.29978 | 2026-10-08 16:35:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cb12138d-5eb9-3a7d-adcd-5c31ce265587 | -15.63366 | -40.13227 | 2026-10-08 16:35:00 | NOAA-20 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 30884e61-acd0-3bf3-b317-9533d8e55212 | -15.54107 | -43.17231 | 2026-10-08 16:35:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 2ef527e3-a2e3-30f5-8149-a607ee524d64 | -20.61849 | -43.0975 | 2026-10-08 16:35:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9d763e2a-c4fc-3553-8fb3-21cd9dc1963f | -14.79156 | -42.83488 | 2026-10-08 16:35:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 3ea79b2a-6ede-3868-ae7e-b6112739d237 | -13.96144 | -44.84523 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| db9a6483-07b8-3640-a08a-06fff65b3087 | -16.24519 | -41.73406 | 2026-10-08 16:35:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| f86402aa-85e3-34c0-b755-c8e7232ea663 | -16.12565 | -43.75006 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5439cf42-ee3f-3ad2-98bb-01a947d1a2f2 | -15.04068 | -42.49165 | 2026-10-08 16:35:00 | NOAA-20 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 8cd568d7-602b-30d2-93a6-525a9c11e0be | -14.49887 | -40.71659 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f19f0ef4-0c62-39f0-adca-910909e6dd38 | -15.10939 | -43.62769 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.0 |
| dc2fc134-5eab-3cc8-8364-1048f3830bfa | -15.5681 | -44.52603 | 2026-10-08 16:35:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0486a25d-bc92-3bf3-8c59-4abacdb0038e | -15.99934 | -53.69682 | 2026-10-08 16:35:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64ea7254-dcf9-3c72-bc99-bbc19ecdabc4 | -16.14935 | -43.74991 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8f8771fb-8103-3878-a248-ba09b76990bd | -17.42152 | -43.52831 | 2026-10-08 16:35:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 019c375d-4e98-3c0a-8e93-3d6c8face271 | -14.65141 | -48.9725 | 2026-10-08 16:35:00 | NOAA-20 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 80e22857-2e80-3432-b264-b90f991ffc1a | -15.00159 | -44.05428 | 2026-10-08 16:35:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 28.0 |
| 5d4640e7-89e0-39ba-bb3e-f70d4b5e00c0 | -14.82341 | -39.40516 | 2026-10-08 16:35:00 | NOAA-20 | BARRO PRETO | BAHIA | Brasil | 2903300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 2e767541-3ce2-3849-8b9f-e6aec93ff5cb | -14.49309 | -40.50235 | 2026-10-08 16:35:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| d6cbfaed-0245-3764-801e-dcebcb0bbd4f | -15.7637 | -41.77166 | 2026-10-08 16:35:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| f52b45fb-cac1-3ea2-b3a0-b01edf12699e | -15.97039 | -40.69498 | 2026-10-08 16:35:00 | NOAA-20 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| f89878ff-b067-360b-8c3e-b0fcc5c9513c | -14.423 | -41.50693 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| af9796a6-a277-3c86-848f-1b13c3cde05d | -15.79143 | -44.68272 | 2026-10-08 16:35:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 193.5 |
| f11a5b04-c0e8-327f-a22c-8d736045fe8f | -20.95192 | -44.77682 | 2026-10-08 16:35:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 64adc0d8-68d0-3bc0-89b2-311530d4176d | -13.95308 | -44.85751 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9ed2cdde-528f-3335-a79a-58d63e7bb649 | -14.75371 | -48.362 | 2026-10-08 16:35:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5a948e2a-0b0d-39b6-a0dc-03d51399a8d8 | -20.54342 | -41.32658 | 2026-10-08 16:35:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8797efcc-cae6-3ddb-9043-4be9d688651f | -20.24416 | -42.07167 | 2026-10-08 16:35:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| c2730446-2075-3581-8ab3-cf271f6d7dd1 | -13.96476 | -44.84469 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4246dbef-4b1c-3a46-b6fe-0106facfea7b | -14.41193 | -41.28408 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| e353f132-d14a-3d37-8fb2-e83fcf91b087 | -14.44025 | -40.7887 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 24.4 |
| b759df45-1033-3f5c-af87-0f18a9504c38 | -15.60731 | -41.78122 | 2026-10-08 16:35:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| eed6eeb2-8c6b-3814-b661-fa1a25de0370 | -14.96934 | -48.18703 | 2026-10-08 16:35:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3776437f-864a-3f1a-8409-9062a19a4831 | -14.05678 | -43.82206 | 2026-10-08 16:35:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 02507e68-ab85-377d-b7b1-081215973973 | -17.13904 | -41.08822 | 2026-10-08 16:35:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 03c0f855-c339-3466-99fa-cab5750d7fd5 | -14.76527 | -39.81306 | 2026-10-08 16:35:00 | NOAA-20 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 57c2c89c-3838-38e1-aa77-7028ffa75a8c | -21.57153 | -44.14437 | 2026-10-08 16:35:00 | NOAA-20 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 18815228-90a8-31ae-ab21-7cbcc2bbe0fd | -14.86366 | -40.88049 | 2026-10-08 16:35:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 1f111e60-b2a2-3981-89a3-62ea7b57c7da | -16.68718 | -42.51697 | 2026-10-08 16:35:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 37be87fb-32ca-375c-b198-366e5bb52913 | -21.4039 | -44.02013 | 2026-10-08 16:35:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| db3f2537-028f-3d32-bb09-559ffa22f9cf | -19.97119 | -40.64038 | 2026-10-08 16:35:00 | NOAA-20 | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| db307ada-b3aa-3936-aec5-a6274436e0a3 | -20.08446 | -42.70687 | 2026-10-08 16:35:00 | NOAA-20 | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| f3e40dc3-b3ca-3c95-9d9a-389b710d12d6 | -15.82804 | -45.40154 | 2026-10-08 16:35:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 98267858-a376-3275-ac49-0ce1ce76ad4a | -14.99551 | -44.05891 | 2026-10-08 16:35:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 53.1 |
| a78fb93a-4b43-3b87-93ef-1e6fd4bdefa9 | -14.60177 | -44.91121 | 2026-10-08 16:35:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab1687db-e908-3772-95e6-89821d9e1e67 | -17.02952 | -41.06196 | 2026-10-08 16:35:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| ccd222b8-af92-398a-84d4-a5679c4e9b9e | -14.63748 | -41.53263 | 2026-10-08 16:35:00 | NOAA-20 | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d9a7966d-31cd-36d3-ac94-a3261fc25a3a | -15.34476 | -41.69556 | 2026-10-08 16:35:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2b683db3-3bb5-32fc-932e-46a9e441d369 | -15.98928 | -53.69932 | 2026-10-08 16:35:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 28b2032d-aae9-39d4-89b8-3b3cba506ff3 | -15.51388 | -42.65647 | 2026-10-08 16:35:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 9beca419-1e83-3a04-a7f5-cd94f8fc6520 | -22.76332 | -42.34718 | 2026-10-08 16:35:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 749302c2-266b-3f85-bbfa-0eaa32987a24 | -16.12808 | -48.46316 | 2026-10-08 16:35:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d772d37-cb67-3589-9a95-15b2109d2f8c | -15.63647 | -39.72718 | 2026-10-08 16:35:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| d1f4f6d7-82a2-320f-a7a3-48be05a51616 | -14.55723 | -44.07697 | 2026-10-08 16:35:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 8d6c18b4-1420-3b88-a27f-bb7153d31b7f | -16.06516 | -39.62165 | 2026-10-08 16:35:00 | NOAA-20 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 22073718-ed25-3def-b0e1-fb6c6da407e5 | -17.1081 | -41.34526 | 2026-10-08 16:35:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| de3e6a48-a78e-3f9e-901e-71dcdede440d | -16.90578 | -40.88612 | 2026-10-08 16:35:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| b7e2db29-928b-3290-8b29-636b8fb98360 | -15.10662 | -43.6318 | 2026-10-08 16:35:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 168.4 |
| 0162fa11-64ec-3e13-8fdb-af54ecb07b06 | -14.467 | -40.72678 | 2026-10-08 16:35:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 38.7 |
| 57f00e97-1cee-3f4e-be5d-43cdd353a131 | -15.95589 | -41.10498 | 2026-10-08 16:35:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 7bf5e08b-aed0-3211-9815-e08958bef4df | -16.13115 | -43.74186 | 2026-10-08 16:35:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| aaaaa7f4-d915-3807-b7b7-2457626af587 | -17.45549 | -45.05949 | 2026-10-08 16:35:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e739630-121e-3d81-9191-1e2293039772 | -13.43643 | -40.44626 | 2026-10-08 16:35:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| f35c3e47-dcee-332b-8992-fae89114318b | -14.62325 | -40.63068 | 2026-10-08 16:35:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d9b3f495-2cb9-3603-9a53-8b5afcc4ce13 | -23.39763 | -46.35192 | 2026-10-08 16:35:00 | NOAA-20 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 411b778d-cfe9-343e-b035-72ca8c91aa5f | -20.22973 | -42.06662 | 2026-10-08 16:35:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5f5155bd-a174-3b17-b38a-670e800a18f0 | -14.40906 | -41.28873 | 2026-10-08 16:35:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 4adfd493-1460-3ab0-acc6-e2440c354604 | -17.15261 | -40.93248 | 2026-10-08 16:35:00 | NOAA-20 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 73c8bed5-d54e-3773-b441-58bdf5c8f2f3 | -16.19405 | -44.56502 | 2026-10-08 16:35:00 | NOAA-20 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README310.md)
