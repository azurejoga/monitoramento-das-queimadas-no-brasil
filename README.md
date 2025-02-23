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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6006ad59-6769-3cc2-afaa-c0b228b3b227 | -12.1035 | -51.2339 | 2025-02-23 00:00:00 | GOES-16 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| f534d3ea-1398-36b4-8b2d-537811298c81 | -10.6 | -45.1158 | 2025-02-23 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 620b7b6f-2dc2-3640-bdb2-98ad947eeae4 | -10.6004 | -45.0928 | 2025-02-23 00:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9d70f64d-9cb2-3594-9b9a-e7a04a45e7f5 | -10.6125 | -45.112499 | 2025-02-23 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 773256cd-0425-3f73-8b2f-4f0544b98e93 | -17.0854 | -39.429501 | 2025-02-23 00:02:00 | METOP-C | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bb6b45f1-5cba-381c-926b-ae370e85d07c | -10.1832 | -36.691601 | 2025-02-23 00:02:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 080b4ddc-e66c-36cd-b184-4a50feabae59 | -17.087299 | -39.438801 | 2025-02-23 00:02:00 | METOP-C | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 706e7313-9183-3237-b451-54eabf2b3b9d | -10.6091 | -45.0956 | 2025-02-23 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b6ce018d-979f-3bd8-a943-fe492063eb88 | -11.8984 | -38.228199 | 2025-02-23 00:02:00 | METOP-C | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45818595-8ac0-342e-b98b-e66f90eea640 | -10.5994 | -45.097599 | 2025-02-23 00:02:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37a728e3-ab5c-3c8c-90e4-771bf6d1e516 | -10.483 | -42.4142 | 2025-02-23 00:02:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ba977a4a-1872-31c5-b5ca-c013cf65e9ab | -6.986 | -34.9659 | 2025-02-23 00:02:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8b52358-6857-3790-aca1-26d2da61146e | -6.9879 | -34.9739 | 2025-02-23 00:02:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2ce6728a-2605-3f33-b8aa-99bb0e50731f | -10.1847 | -36.698601 | 2025-02-23 00:02:00 | METOP-C | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| d13f468b-9541-3aa3-affb-5a9fd616cb35 | -12.8472 | -43.822102 | 2025-02-23 00:02:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 955cd86d-5283-349b-ac56-4b1c1f535b4d | -9.3842 | -38.214901 | 2025-02-23 00:02:00 | METOP-C | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| aaf6cde1-fc89-3e0b-9675-54a8e6a2238b | -12.8569 | -43.820202 | 2025-02-23 00:02:00 | METOP-C | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3c65fe1f-9529-37f9-a4f5-5f98ea6f3b4f | -10.6191 | -45.1132 | 2025-02-23 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| f3e346cc-5cd4-3fcd-a7ee-d37a1ba1f61e | -10.6 | -45.1158 | 2025-02-23 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 50f89f6f-1ea9-3c31-a1db-68ef021b7d3d | -6.5631 | -51.1126 | 2025-02-23 00:10:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 22ada890-58c1-3632-a817-7e70f026e7e4 | -10.6195 | -45.0902 | 2025-02-23 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3342dcb6-4ce5-3107-b0d1-99200db322e4 | -10.6004 | -45.0928 | 2025-02-23 00:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5e8824e6-46e2-3827-b796-1ec156f7448a | -10.6191 | -45.1132 | 2025-02-23 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 6d2aedfc-1e23-33ad-b7b6-c0099796c307 | -10.6004 | -45.0928 | 2025-02-23 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e4b6627d-ee97-3247-a2ac-a439ce09ef9b | -10.6 | -45.1158 | 2025-02-23 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 9dc922c4-9f5c-3f66-a5ba-9f80aba1a243 | -10.6195 | -45.0902 | 2025-02-23 00:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| f3ef5a4f-856c-3679-a939-c82ca48a9789 | -20.8978 | -46.16655 | 2025-02-23 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| de78203f-1425-339f-987b-6e99577ffe5c | -20.06613 | -40.7503 | 2025-02-23 00:28:00 | TERRA_M-M | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 2a4d0f98-f2af-361e-b423-f587609e4fcb | -19.82245 | -40.10181 | 2025-02-23 00:28:00 | TERRA_M-M | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| bab5671e-81e6-3f89-8de3-18a46c8a06f3 | -20.6933 | -43.9412 | 2025-02-23 00:28:00 | TERRA_M-M | QUELUZITO | MINAS GERAIS | Brasil | 3153806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| 638e1040-35cc-393c-932f-c7be95ca4efe | -20.89329 | -46.15789 | 2025-02-23 00:28:00 | TERRA_M-M | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 47edac0a-d79a-3f01-843c-efaf24681fee | -19.1312 | -42.95937 | 2025-02-23 00:28:00 | TERRA_M-M | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 2c94eb35-9c62-3a16-a5c6-e2c8678222e2 | -19.54096 | -45.91664 | 2025-02-23 00:28:00 | TERRA_M-M | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9e170fc9-1061-3606-b02b-39222da905af | -20.06752 | -40.75993 | 2025-02-23 00:28:00 | TERRA_M-M | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 572c460e-4e4f-35d7-974f-d79052d8b69d | -10.6195 | -45.0902 | 2025-02-23 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| e1ec2e19-d574-3688-b41c-ec28773994e3 | -10.6191 | -45.1132 | 2025-02-23 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| f3df5de8-7b3a-3bfc-b2b4-e55acda193b2 | -10.6 | -45.1158 | 2025-02-23 00:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b5f993b5-cae6-3a2e-964d-754025cc2f0b | -16.64697 | -49.37208 | 2025-02-23 00:30:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| b770353d-43ec-3ca8-98aa-165dc4f6784e | -15.68121 | -42.44439 | 2025-02-23 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 200faf4f-0c2e-35c4-9091-19eaed1b56c9 | -15.04156 | -45.61917 | 2025-02-23 00:30:00 | TERRA_M-M | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 69ca905a-e5f3-3ea9-8514-48924eb71904 | -15.67992 | -42.43523 | 2025-02-23 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a40e7440-44bb-3ed9-92fe-f4007bbd991f | -15.87928 | -42.60717 | 2025-02-23 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| b364240e-4b1c-3192-bc44-31cfa2b9347a | -17.08213 | -39.43737 | 2025-02-23 00:30:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.7 |
| b50c35c9-4b12-31a2-89ed-d1993befb5ef | -15.58409 | -42.40954 | 2025-02-23 00:30:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7760fbb9-4aea-379c-87eb-f725f509d092 | -17.60291 | -42.09377 | 2025-02-23 00:30:00 | TERRA_M-M | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 1cfbf19a-ba5d-3cf5-856b-ceedb1e8ed74 | -10.47909 | -42.42556 | 2025-02-23 00:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 23a70e50-1b74-3eb7-a752-bd25e94734a1 | -10.47771 | -42.41609 | 2025-02-23 00:32:00 | TERRA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 3540448e-480c-3e95-84d2-3725d2f88360 | -13.6238 | -44.42737 | 2025-02-23 00:32:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3384311-ecda-34d8-ac2c-91047afc2358 | -11.88979 | -41.29282 | 2025-02-23 00:32:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 10.0 |
| ca3de16d-411e-36a9-9a77-d296e57805b7 | -10.61283 | -45.10102 | 2025-02-23 00:32:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d3ed6cd4-7119-3c3a-a7fe-cc2b4da498c9 | -11.89132 | -41.30308 | 2025-02-23 00:32:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d14d393b-4778-32f1-ae23-080a4487bb2b | -13.62505 | -44.43676 | 2025-02-23 00:32:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 71c71427-6f9b-33e2-8263-7c1e9a1e0e4c | -12.85155 | -43.82855 | 2025-02-23 00:32:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| de1b749c-15ec-3eb0-863e-6406062ecd18 | -12.8427 | -43.82984 | 2025-02-23 00:32:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 916f123b-13a7-3752-8582-11b471f37e66 | -12.02324 | -40.62344 | 2025-02-23 00:32:00 | TERRA_M-M | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c85ee6d0-3ee7-37c2-9118-b566942b40fd | -10.60383 | -45.10227 | 2025-02-23 00:32:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| dfd58113-76cc-39f0-a9c9-ed6f99d65506 | -10.60508 | -45.11155 | 2025-02-23 00:32:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 19d92776-e00b-3843-a532-af335bb56a00 | -10.61409 | -45.11031 | 2025-02-23 00:32:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 789cbb4a-d2c0-3f46-8fd1-91fa67aa553e | -16.660801 | -49.356602 | 2025-02-23 00:43:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bb7cafdf-6ab6-3897-bbbd-6990effb28c4 | -15.3016 | -53.2052 | 2025-02-23 00:43:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cbb5b93-a2dd-300f-849d-3b636a4d9b76 | -29.8241 | -51.325699 | 2025-02-23 00:43:00 | METOP-B | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | nan |
| c8706966-6b3a-33fd-b4d2-d8fc66033ddb | -15.3001 | -53.198002 | 2025-02-23 00:43:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c3b7fd48-c8b9-3072-af0a-9e1bef965963 | -29.825701 | -51.334301 | 2025-02-23 00:43:00 | METOP-B | NOVA SANTA RITA | RIO GRANDE DO SUL | Brasil | 4313375 | 43 | 33 | nan | nan | nan | Pampa | nan |
| e3faf5c8-4ac1-3942-8dc9-3f0caa03dcef | -10.6102 | -45.091801 | 2025-02-23 00:43:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70a7ad83-1a1f-3a9e-b334-ed840925df8e | -16.6588 | -49.3484 | 2025-02-23 00:43:00 | METOP-B | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba68432a-22eb-316f-9f69-9a3d1a89063e | -15.2985 | -53.190899 | 2025-02-23 00:43:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c40192a1-d055-3868-8d8d-88683192a631 | -12.1141 | -51.2164 | 2025-02-23 00:43:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 20259c49-f6c8-323e-b594-74d0298c7c76 | -12.1158 | -51.223999 | 2025-02-23 00:43:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36fa931e-59aa-3c0f-ae8b-81d56d0a24e8 | 4.3197 | -60.828899 | 2025-02-23 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce85ee6e-e643-3cac-8402-0b753bc25e97 | 2.9937 | -61.309601 | 2025-02-23 00:46:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e70fda5b-5c61-31b9-8ced-348021aaafe1 | 4.3218 | -60.82 | 2025-02-23 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e4a9acea-4e6f-387d-a1d4-42a7d1e09bb8 | 2.9914 | -61.3195 | 2025-02-23 00:46:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a875b8c7-5732-33b9-894b-07c96a960aec | -10.6004 | -45.0928 | 2025-02-23 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| fc521710-f4fc-3057-bf30-80d816dd171f | -10.6195 | -45.0902 | 2025-02-23 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7bc33efa-13a5-3fe2-abc3-f0b0a9bf9e37 | -10.6191 | -45.1132 | 2025-02-23 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 34566dd5-000f-38e5-ba91-ed05f197e97a | -10.6 | -45.1158 | 2025-02-23 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| c52a5b7d-606d-30ab-b089-c21c3fbd53c2 | -15.8775 | -42.6053 | 2025-02-23 01:10:00 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 9029a51b-4ca6-30e4-94d9-64b93c4baafa | -10.6195 | -45.0902 | 2025-02-23 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c0057745-6be2-3df0-a96a-897d949d1644 | -10.6191 | -45.1132 | 2025-02-23 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 7231e0fc-5491-36cd-bf31-772a54290d34 | -10.6 | -45.1158 | 2025-02-23 01:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 5c38495e-3231-3b0c-b4c2-f1f0abcb6331 | -15.8775 | -42.6053 | 2025-02-23 01:20:00 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 4d1adfab-b1eb-3211-b099-6005bed35b06 | -15.8973 | -42.6009 | 2025-02-23 01:20:00 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 60.8 |
| 19eaf4ed-6ae2-3d41-83fd-850848dec755 | -10.6191 | -45.1132 | 2025-02-23 01:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 35f189f8-abfd-3a9f-b0d7-92752a2cb76e | -10.6 | -45.1158 | 2025-02-23 01:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 21942f8b-2466-37d9-bd99-816f1d9d0826 | -10.6 | -45.1158 | 2025-02-23 01:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 37deae1c-6bcb-353f-9ede-5813b4823a28 | -10.6004 | -45.0928 | 2025-02-23 01:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 8bc8b0e1-607d-3fc5-a260-a56c2c9af597 | -10.6195 | -45.0902 | 2025-02-23 01:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 663ac6c5-a354-381b-bfce-00cc7dfc3817 | -9.80264 | -37.94596 | 2025-02-23 03:06:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 206bfe4e-7ebf-3c5d-8761-2d02c19c1a98 | -11.89273 | -38.23004 | 2025-02-23 03:06:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 34650609-a852-3c6a-b154-e12e5cf8f6d7 | -11.88666 | -38.22924 | 2025-02-23 03:06:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| db630697-81a0-3dbe-938a-39f5a0461942 | -9.80174 | -37.95066 | 2025-02-23 03:06:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 67ec118e-cd5a-36a6-862f-f1bc457934a3 | -20.0652 | -40.75335 | 2025-02-23 03:08:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0274854b-f8fd-3c71-8924-56c932ba4727 | -20.06667 | -40.7539 | 2025-02-23 03:08:00 | NOAA-21 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e22f71d9-3a9a-3d5c-90ce-75642548bca2 | -19.82368 | -40.09873 | 2025-02-23 03:08:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 431111b7-eb48-36f2-958b-72ce362208bd | -8.17267 | -34.98054 | 2025-02-23 03:29:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 10ca6160-6fc7-3dfe-bd93-4b70fbb3a994 | -4.17234 | -42.0283 | 2025-02-23 03:29:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c34671c-61f0-3860-b6e0-ac820b294c43 | -7.90558 | -39.7279 | 2025-02-23 03:29:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 69eb9a44-fd97-31da-a667-56710ecb889a | -4.17163 | -42.03247 | 2025-02-23 03:29:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f7a6d9a-552f-399a-8379-3f8d43c51236 | -10.47773 | -42.41556 | 2025-02-23 03:32:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0c0fa5ac-e619-3377-8109-1a1c45a84793 | -11.89275 | -38.23409 | 2025-02-23 03:32:00 | NPP-375D | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README2.md)
