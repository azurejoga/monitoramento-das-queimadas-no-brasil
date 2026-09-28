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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38c4e9fa-5f64-30dd-be12-42fdc63274df | -12.39906 | -50.65279 | 2026-09-28 16:24:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a54e3eb8-ce13-3240-9ae3-a802c712f7b2 | -15.39802 | -47.91323 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8c584d99-8432-3b17-9106-0db2534d78c4 | -14.11456 | -46.30264 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 65b4eb7b-71ac-3912-b615-dcfd0542f55a | -13.92746 | -47.84986 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2ad452c7-0622-387e-9590-dacf259c93da | -14.2981 | -39.91525 | 2026-09-28 16:24:00 | NOAA-20 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| fb0f0d40-25a1-32a4-8f77-9d9aad5bc0f8 | -12.00351 | -44.96317 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4b3275e7-61e5-3489-a7df-ab33cc79734d | -15.20845 | -46.1871 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 943a7d1e-2257-3fc5-bd29-7d63060753ad | -16.44404 | -40.26448 | 2026-09-28 16:24:00 | NOAA-20 | SANTO ANTÔNIO DO JACINTO | MINAS GERAIS | Brasil | 3160306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| bb8899eb-84da-3440-9690-a05354e2cb43 | -14.46141 | -40.3276 | 2026-09-28 16:24:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 6fe8d942-b048-3478-adaf-6568c75c7bd0 | -12.81168 | -54.00252 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 309eecf9-05ac-3f07-8b42-3c3b5cb73c6a | -12.07817 | -48.53268 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| dccf33eb-1347-3e23-879b-c839d15985c4 | -11.56206 | -47.40356 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 4c05c81d-b9c1-3d1a-9728-8eb00354c64a | -15.13361 | -43.62612 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 8e4aa204-93bc-350f-b26e-135057659252 | -13.94594 | -49.0773 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3120a1d9-aacd-38f3-9bf7-cc61c7f85374 | -11.19732 | -44.80625 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 5b02be7c-fd5f-3fdd-a698-7d7a9dca3797 | -11.52411 | -42.55976 | 2026-09-28 16:24:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ee893ccf-70b3-3820-ae69-f443f4e569f7 | -15.78562 | -38.97588 | 2026-09-28 16:24:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cebf0965-49c2-3dc2-b2e6-b227fc037492 | -15.19178 | -46.1544 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 38ace3b8-e1f4-3fa0-b194-e0c43c40d3a2 | -11.18473 | -44.79529 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 69066d6e-e206-3d53-90f7-880ca77bc038 | -13.70663 | -48.82259 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eb39ff90-9daf-3ac9-b5ca-e8da69f63257 | -12.7562 | -41.5537 | 2026-09-28 16:24:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d662fd31-0e5c-3a60-8467-86dd9442819b | -12.80968 | -54.00276 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 19d6101d-a7c5-316c-aadc-b09d268b083c | -12.36823 | -50.23439 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 81ee7a42-78f1-3712-b69c-307acaab1383 | -12.67337 | -46.98747 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d40f91e-ad42-3966-8fe8-4aec65152b76 | -13.94851 | -49.07816 | 2026-09-28 16:24:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ea1cc9a1-6140-30a8-b38d-41e1e885fef0 | -16.35605 | -42.57692 | 2026-09-28 16:24:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e4447dc6-e3bf-3d82-b304-8a8c7f61423c | -11.2925 | -43.54093 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d7eb79e4-b2fb-3030-b820-fca8cf03b8cd | -11.50339 | -47.38305 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d793054a-4c60-3021-b4f8-5cc91b8b452e | -13.40333 | -51.3206 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fbafd217-8747-39a5-b287-b2209b512fdd | -11.28963 | -43.54519 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 2073daa1-d4d6-380f-9d42-e4980a2f9895 | -12.74056 | -47.32798 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 71d174e2-b19e-3d91-955e-a508c0089a52 | -11.90773 | -49.9846 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d2ae4b51-c3b9-33d6-8efd-0142acd7af6b | -14.49614 | -41.44137 | 2026-09-28 16:24:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 71bc1b24-e3b2-3593-bbab-18e184ffa57c | -12.17894 | -50.42374 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f054e88f-134f-311e-934a-a81ab1d35f6c | -12.10841 | -47.39725 | 2026-09-28 16:24:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| da5c0aba-1357-3bd6-b740-2a9b925b9958 | -13.56747 | -46.36454 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 480d151c-cd8f-356b-a553-83cf2764bc1e | -14.33002 | -44.80853 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2518227e-92cd-3569-a9eb-5ea40a23c262 | -15.18167 | -46.14036 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 4aebdd5f-a5eb-3966-b8e0-b45cca5c2984 | -12.72965 | -47.27905 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2cf37505-a804-3396-a840-79889d2e4926 | -16.60301 | -49.24353 | 2026-09-28 16:24:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be86d0dd-e871-3190-bce8-5d5499561d1b | -12.37342 | -50.23375 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8937a481-b59d-361d-9fab-0178aa07cf38 | -13.37522 | -44.01759 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 18541f14-3834-3667-aff7-d8b72b2cfe2e | -11.5289 | -47.16127 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| d191c2e2-844c-38a1-a233-f7c272bb8850 | -12.98896 | -44.73367 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 563f7560-2a02-3691-a3a9-6440a77e251e | -12.43735 | -44.14607 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 8795840d-c2ee-3346-a066-693e85712c3f | -15.22025 | -46.18128 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 602b426c-7341-326f-861c-17744d3c298d | -12.63889 | -47.34074 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 0d80c652-773a-3927-a951-39ccbad41ecc | -16.9954 | -45.47118 | 2026-09-28 16:24:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 58384413-e7ac-354c-8b53-1711e9e7ab4d | -12.6574 | -39.28162 | 2026-09-28 16:24:00 | NOAA-20 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 0242fd59-8241-36c7-92c4-60ad7a3ba560 | -15.19419 | -46.17349 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 0e72381d-521e-3586-9c9d-34970a640a6c | -13.68709 | -48.82132 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b3cf6cf9-6544-3b32-8489-a5c9f235ee81 | -13.8925 | -53.66321 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f86d0c15-8ab1-38cb-9c1e-00137fec77e4 | -11.38702 | -43.42281 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e9573475-ff15-34b2-a786-41324b282e52 | -15.6912 | -48.10078 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3a8929f0-f44d-3bde-9152-d986f169a3ef | -11.54984 | -47.37698 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 1a8a350e-71e7-33b7-93e3-55749bc73d5c | -12.65224 | -39.83995 | 2026-09-28 16:24:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 224.6 |
| c7ac580f-f994-3c23-a7fc-e0c3c2af4063 | -12.10294 | -45.22011 | 2026-09-28 16:24:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 88051e4b-47df-33d4-aed1-37fee68fc79e | -11.22327 | -44.79533 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c87389e6-45d6-3ea0-ac0d-9619f13f1553 | -16.42032 | -43.29079 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5da5f75e-ab03-33cd-8933-c67232342305 | -11.71427 | -44.53594 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| da80da2f-2aba-31a4-9e2b-47db0a8f8016 | -13.92296 | -47.8505 | 2026-09-28 16:24:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2474b7ec-c3ec-311a-8660-7dd5ff8d6a90 | -12.74501 | -50.68645 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 228252ce-5e88-3ab1-85ba-aaaa8a50b1cf | -13.09999 | -48.20521 | 2026-09-28 16:24:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 7c5da6e8-0c4b-3862-a0d8-6d56c4ca8c6f | -15.40563 | -47.93792 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| b368a80c-4b40-3e26-a515-9107e46662f7 | -16.34083 | -47.69884 | 2026-09-28 16:24:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c2e56d4d-ca93-38d2-acd5-01e6c5451b47 | -12.39948 | -50.65618 | 2026-09-28 16:24:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dcd7f7a0-b3c5-39f5-901c-32f18a49a042 | -14.81054 | -41.73162 | 2026-09-28 16:24:00 | NOAA-20 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 235.3 |
| 09203ee2-1382-3066-a043-cc32dc0da5d9 | -14.24967 | -41.29174 | 2026-09-28 16:24:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 31.2 |
| 890d6356-ee5e-3873-a905-ce5db74fb91d | -12.31466 | -50.27015 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ea608dd-64a2-303f-8a83-d28aa3ae11e9 | -12.64936 | -47.26192 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| ea4527a0-fb45-3488-9e05-faeba5e38a31 | -12.62957 | -47.27172 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1c419e4f-14ce-33e3-9fcb-13efe8306996 | -14.53401 | -48.30711 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| f6b5f402-3fb9-311b-a151-311d0f4e1398 | -12.61198 | -45.07665 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f324fe42-d928-31ff-bff9-2a8af0f49eee | -11.70118 | -43.49084 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ef25fdbb-92a5-3501-9dfd-bac987d026f8 | -12.78639 | -54.01679 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 3e370250-dd13-3842-90d8-888825f2a09a | -12.62532 | -47.27232 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 261a4cf1-733e-3d2c-9fde-cdf8344823a9 | -12.72487 | -47.27578 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d47b9ba0-23ef-36f8-b1ef-50fc799ab255 | -11.17814 | -44.80051 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 2ca5af0a-db7c-38ad-9c60-58d4afb76b57 | -12.94092 | -46.63669 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 61b6434d-da0b-3dcf-9b3f-61f776a4d4b0 | -12.4399 | -48.22007 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 7afe649e-ff95-3241-a016-9768471d06df | -11.71737 | -44.51522 | 2026-09-28 16:24:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b2bbe0f2-4dc3-33e4-9dc4-768d5f2f741f | -13.55532 | -46.36643 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 347eb686-9ead-3296-93d0-f8a71c43dd60 | -12.88018 | -44.81002 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 5cf30659-af28-3a5b-9a99-470d5646009e | -15.15726 | -43.61409 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 73.8 |
| 745764c9-fd03-3b47-9f13-526fba5bd4ed | -14.50735 | -40.53581 | 2026-09-28 16:24:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 8c7bfbe7-60b2-3c80-bc01-898beee15b8b | -13.54043 | -40.84632 | 2026-09-28 16:24:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 0b7f9ab6-e5f1-3fab-a78d-f7d5a7e45d28 | -15.39991 | -47.92035 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0383a3c3-a8e1-3949-8e1b-4e4b8c773b85 | -16.18151 | -50.37371 | 2026-09-28 16:24:00 | NOAA-20 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 396a3416-5857-3b1e-80ab-dbba0a09bbb1 | -15.46778 | -46.14022 | 2026-09-28 16:24:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a96778c2-22cc-30fd-a22e-b1477afcb370 | -15.1624 | -43.60182 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 44.2 |
| c513ec1e-fbc0-3f37-bcf7-09dab6020926 | -13.08833 | -47.43618 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a44cc5ad-1018-366d-ae5d-ef579ff58b93 | -15.55427 | -47.93034 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| be8ac57c-901f-363e-b0e2-3bc71f698c2e | -11.44787 | -44.91449 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 114deb61-b5aa-364c-9f52-9992cd7cf6c2 | -13.37581 | -44.02172 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 37219f96-0982-37bb-85e2-aab637e39798 | -11.37626 | -43.4206 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 363e8bf1-7581-3e69-bb11-bdb86c6e77c3 | -12.68511 | -45.01649 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 95a8a09a-232b-3ffd-a604-6f4a41cfb502 | -14.49293 | -40.3115 | 2026-09-28 16:24:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c9327317-494c-37d7-9cde-0f3f4f34e463 | -14.51872 | -48.29887 | 2026-09-28 16:24:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b1bc549-b8d5-351c-8ea1-1dc86d50d996 | -12.22246 | -50.43143 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c7c38737-133d-34b7-a502-88946929532b | -15.20096 | -46.16101 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |


[Clique aqui para ver as próximas entradas](README100.md)
