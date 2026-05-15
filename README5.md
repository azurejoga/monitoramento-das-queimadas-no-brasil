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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad0be03d-20b1-35d1-8399-55e7053195bc | -12.0515 | -45.28094 | 2026-05-15 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bd5bc04-4dfc-3f99-8ab8-9bb69cb6da09 | -11.87053 | -43.86497 | 2026-05-15 04:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f459af06-9f19-375c-91ab-370f8ea4257c | -11.86648 | -43.86438 | 2026-05-15 04:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a77a875-ed74-3566-b656-0a87631efc4c | -11.75957 | -47.06743 | 2026-05-15 04:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e58e4bf9-c60c-3eda-83e7-5c1f2a0ba5f0 | -10.49785 | -42.4058 | 2026-05-15 04:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83f42bc8-924f-357b-b3ee-9b7824dfac95 | -12.85105 | -43.76098 | 2026-05-15 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 032ce5f9-091c-3029-b694-cca6a7a9c7c3 | -11.12386 | -45.12363 | 2026-05-15 04:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 492e254a-3b76-3e66-9616-4ae83d2d7145 | -12.0767 | -51.25498 | 2026-05-15 04:36:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce3783f2-0fd7-375c-b97f-8d50e280cd80 | -12.48055 | -45.43758 | 2026-05-15 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6647f9c-8f24-38cb-86a9-928ad7a04d2a | -10.649 | -42.31886 | 2026-05-15 04:36:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbe1d519-cbe3-3427-9b39-6b1a0ca0073b | -10.38467 | -49.45045 | 2026-05-15 04:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9139ff36-5a2a-3b53-9bb1-eaf9b8aee15c | -12.04778 | -45.28039 | 2026-05-15 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8bcc858-eb90-30cc-857e-80e13687b8d0 | -12.61135 | -44.50817 | 2026-05-15 04:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecb70ff7-257b-3ce9-93bc-0d56b040b47f | -12.48239 | -43.78585 | 2026-05-15 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3b1354f-4057-3570-9bbc-7fdbb203242c | -12.05214 | -45.27642 | 2026-05-15 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e6d4d4ae-4f5e-3bdb-af31-aa86658a5a1b | -10.65017 | -42.31019 | 2026-05-15 04:36:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f650b03e-e115-32f1-accb-ad7b0f9c250b | -12.84744 | -43.75656 | 2026-05-15 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8f42163-2fdc-356f-bd27-412d205d2876 | -12.60742 | -44.50761 | 2026-05-15 04:36:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27c72c68-359e-3b56-a679-82311cbcd669 | -11.31214 | -54.03319 | 2026-05-15 04:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 26b3a94a-b125-3305-b9e8-642d36698360 | -11.93881 | -47.88469 | 2026-05-15 04:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3f7f7b8-4b0d-3633-af2d-3e50644548b2 | -11.97948 | -46.79154 | 2026-05-15 04:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5c0b1d2a-f767-3bea-bea6-51d0a69bba58 | -11.30746 | -54.03608 | 2026-05-15 04:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eacc1ce8-3444-3d41-901d-2836abaa582c | -10.14272 | -47.62953 | 2026-05-15 04:36:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cbcf1c6-5e56-3150-a41a-827493460203 | -10.64517 | -42.31391 | 2026-05-15 04:36:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f3d186d-e17f-33eb-aebe-840c9a1bd336 | -10.49796 | -42.40842 | 2026-05-15 04:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 76605407-da10-363f-ac66-0f6a9d77baba | -12.4725 | -45.44091 | 2026-05-15 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c64f6389-4138-379d-b144-553847b2f24d | -11.75615 | -47.06689 | 2026-05-15 04:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d7da16e-750b-3562-857c-ec8a35c6a44b | -9.81612 | -48.52028 | 2026-05-15 04:36:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23b587a5-7c67-3319-90a5-f67660d95ee6 | -11.763 | -47.06796 | 2026-05-15 04:36:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d09069dd-fb91-39a5-bd46-1398b1a7dc2c | -10.39969 | -49.44202 | 2026-05-15 04:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1b137fa-50ff-3f1f-bebc-8fe3e6a70b73 | -10.6696 | -49.68642 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c523ab58-863c-3426-8c76-fc2276060999 | -10.67122 | -49.69766 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75525b27-b3aa-32ea-8828-109ae7174bb8 | -11.63479 | -47.87804 | 2026-05-15 04:36:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 087d162f-75ae-3b39-be8e-fbc73da87bf4 | -12.48362 | -45.44264 | 2026-05-15 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f354b94b-3343-3abe-b271-1b5deedc4510 | -12.04595 | -45.28233 | 2026-05-15 04:36:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e40f905f-d59c-3ad4-b7cc-e3ca8dd441a1 | -10.66846 | -49.69355 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcbb8c82-a2f1-3b1a-8bb2-562a701dc66a | -12.48426 | -45.43816 | 2026-05-15 04:36:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d9d3ac9-f16e-341c-9d29-602f63d51899 | -13.03545 | -49.93452 | 2026-05-15 04:36:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e926ad-67d1-36c5-86bd-bf57bc43ab32 | -12.85157 | -43.75717 | 2026-05-15 04:36:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0e3ad633-cba4-38d5-ada4-6817d5384a00 | -11.93322 | -47.87644 | 2026-05-15 04:36:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2528670c-ea5b-339f-a780-b391d20a4824 | -10.67628 | -49.68752 | 2026-05-15 04:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d53e0300-8751-33fd-840a-acba63ba2638 | -11.73759 | -44.52539 | 2026-05-15 04:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d5a50003-35bf-3122-9242-7c1e570c57c8 | -12.50137 | -43.76943 | 2026-05-15 04:36:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f5036b1-1422-377d-a92b-94735121d4b3 | -10.55184 | -42.43814 | 2026-05-15 04:36:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 8dd9ee34-80ef-370f-9ed3-8c04d894f069 | -13.03213 | -49.93397 | 2026-05-15 04:36:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64e727dd-d6e5-3a8e-8ed9-10977ce22879 | -13.04814 | -43.86428 | 2026-05-15 04:36:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 278d75f3-d971-377a-9fb5-71a3ee9b9448 | -9.45418 | -47.82133 | 2026-05-15 04:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba2b0534-66a2-3390-8817-3c691a409ba3 | -9.47253 | -40.33827 | 2026-05-15 04:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| d711f549-a5f4-35e7-b824-a7db4e2ca1f5 | -8.72535 | -48.33075 | 2026-05-15 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa131b3c-22fb-388e-97c7-83242a610992 | -8.2344 | -47.69601 | 2026-05-15 04:36:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53306644-7017-37dd-9a11-5276b400903d | -8.54711 | -45.98833 | 2026-05-15 04:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e0cd9de-4807-304b-8839-a9d305b24228 | -8.69961 | -47.97694 | 2026-05-15 04:36:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5a75307-381a-3804-9031-e911e7306b1b | -9.46756 | -40.33757 | 2026-05-15 04:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| 9932d525-2a7d-3ace-b001-9ce9afe9d0c7 | -8.96469 | -45.66933 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ccb300c-0ab3-3f2a-b7c5-1f5c8388d7b4 | -9.30634 | -45.48386 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1b26f22-3164-3261-98db-7853812976be | -9.30007 | -45.48385 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18813046-f008-3cad-9d6f-68e1545d7696 | -9.1466 | -49.84017 | 2026-05-15 04:36:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f584225-252e-388a-bae8-6bf93a6d38f7 | -8.7248 | -48.33423 | 2026-05-15 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3aff1a7f-7b81-36f8-bcc9-14af98234708 | -8.08831 | -44.16305 | 2026-05-15 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32ece202-f4a6-363d-a469-db79a18cc47a | -8.54828 | -45.98069 | 2026-05-15 04:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76e0355c-79f0-3113-a4ae-aeac67267fe4 | -9.30721 | -45.4849 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0702b7fa-a40a-3ed3-8e0e-8d7c13c0d183 | -7.71483 | -44.55162 | 2026-05-15 04:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3db2a61d-83f2-3742-98ab-bbdfc6a54077 | -9.31288 | -45.48901 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 008e2b14-539a-391a-a6e8-6a2f7e39e8df | -8.81496 | -44.78874 | 2026-05-15 04:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fa54f06-6085-3e54-aeee-749ffa7d4c4a | -8.55057 | -45.98888 | 2026-05-15 04:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45f4c628-4964-3fb9-b3fc-247dfbe5bbab | -8.54481 | -45.98018 | 2026-05-15 04:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4d3c31f-e7e7-3c54-8475-bffb5b8270d0 | -8.72204 | -48.33022 | 2026-05-15 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ef162fdb-4e9a-3c43-9899-e048126ab686 | -9.30931 | -45.48848 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8292809a-d00a-3c35-b040-630ab0d4f0d1 | -9.45696 | -47.82536 | 2026-05-15 04:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 85b09761-490c-35a3-a86c-2d063bc467a1 | -9.45751 | -47.82186 | 2026-05-15 04:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2408d884-4e3f-342f-951d-4064e1d8d3b7 | -8.72259 | -48.32674 | 2026-05-15 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ef545e7-7740-36bc-94fe-a4698d7979e0 | -9.13986 | -49.83906 | 2026-05-15 04:36:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f48526f-dbe9-34da-9390-0919e9a11ebb | -7.71519 | -44.55304 | 2026-05-15 04:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2099bd20-1c3f-3de7-aac3-5c3d86797869 | -8.08609 | -44.15166 | 2026-05-15 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da04de3d-e264-39a3-af70-abb6aa05c33c | -8.54135 | -45.97964 | 2026-05-15 04:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a163b6eb-5840-382e-8682-c67d88bef88f | -8.5477 | -45.98452 | 2026-05-15 04:36:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 56895eb1-3a7f-3c41-a7b8-ce6d268b80ce | -8.81671 | -44.80221 | 2026-05-15 04:36:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69c21011-8513-3b65-9c6e-3f292f51e7cb | -9.31227 | -45.49311 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6475112f-479f-3760-a35f-2f8f1e90f9a6 | -8.7259 | -48.32727 | 2026-05-15 04:36:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c61cc931-b7d5-33e2-960e-c0629c783852 | -8.70292 | -47.97747 | 2026-05-15 04:36:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3efee117-95a3-3648-adb3-96b1334e2746 | -9.46834 | -40.3319 | 2026-05-15 04:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 39.7 |
| d7e37089-021e-3a93-8bb0-13c807d2d4b9 | -9.30277 | -45.48333 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f60dabd3-af54-3e3b-ab78-00bddc6603e0 | -8.4994 | -46.38966 | 2026-05-15 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6381ec44-fc23-3a56-9a0f-133316a9996f | -9.30574 | -45.48796 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6334dcf-36f3-36bc-93fd-88f590e131f4 | -8.08898 | -44.15842 | 2026-05-15 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3eb6a1b-fa0b-39fa-9923-006053e022e8 | -7.53852 | -47.19616 | 2026-05-15 04:36:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 331e9f62-0d53-3955-89da-6a38115bcf6f | -8.96891 | -47.25266 | 2026-05-15 04:36:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4b302e3-c2f8-3567-a283-a2622b36e495 | -9.30364 | -45.48438 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05770e27-7a1b-3cb1-96b6-baf87bb9e7d6 | -9.14323 | -49.83961 | 2026-05-15 04:36:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b63bd1a-6d22-3a3e-b20a-65197b6c4a3e | -8.70347 | -47.97398 | 2026-05-15 04:36:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1599f2ae-5c47-3e12-8d7c-f743c254303b | -8.50055 | -46.38222 | 2026-05-15 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96891c83-2ef6-394c-b3e2-b8712966943c | -8.50339 | -46.38645 | 2026-05-15 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85a3b76c-a854-3563-8740-a8f6dcba7922 | -8.08847 | -44.16148 | 2026-05-15 04:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0af2d40e-fbc9-31ed-806e-9da19afe5a42 | -9.30659 | -45.48899 | 2026-05-15 04:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f2f761a-5ce0-3a50-8e7b-aacfe669dcaa | -9.14382 | -49.83598 | 2026-05-15 04:36:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 033e3743-ca3c-3fcc-804e-3838b74f716f | -8.50397 | -46.38272 | 2026-05-15 04:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7197ea0e-3f48-354a-bf2a-e13b1dea77d6 | -17.2533 | -47.08088 | 2026-05-15 04:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dea791e7-ad49-39a8-899a-4b979be05ce5 | -14.33327 | -45.54336 | 2026-05-15 04:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06fdfdb7-f33d-32b4-b3e3-501061af59b6 | -15.05318 | -42.95572 | 2026-05-15 04:38:00 | NOAA-20 | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12f155d8-6818-3028-aaaa-7dda604f9dc7 | -15.64536 | -47.92767 | 2026-05-15 04:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README6.md)
