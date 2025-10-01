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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 999adace-3f59-3856-b6a5-85debb916b4d | -18.43018 | -43.79726 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac4bd37f-8cee-3a32-83d6-7d3df167a4b9 | -15.60732 | -46.90566 | 2025-10-01 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a546532e-7a56-33fe-9dc0-aea38df39874 | -16.40511 | -47.05742 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d47b21a7-8442-3b14-9189-63c1f03ad040 | -18.42047 | -43.81792 | 2025-10-01 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb5bd4a5-7c13-3ce1-b548-221973a959e9 | -22.06648 | -43.07616 | 2025-10-01 03:32:00 | NOAA-20 | CHIADOR | MINAS GERAIS | Brasil | 3116209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1e580cb1-6ae7-32b5-8142-5e7b59512660 | -18.27214 | -43.71505 | 2025-10-01 03:32:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a29b6f8f-7211-346e-a488-b6e06a0631aa | -15.83418 | -46.25137 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70dfeef3-04e2-37a6-b715-7cd37ec3bf51 | -19.17442 | -40.43076 | 2025-10-01 03:32:00 | NOAA-20 | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8eae414f-da88-3de8-8e75-9c392400e709 | -20.49025 | -43.95692 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 43b85d38-e278-3108-b30b-29b2e713443e | -17.38592 | -47.14987 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc4229bb-5141-3db3-a09d-8a38bdf4828e | -19.16305 | -44.52783 | 2025-10-01 03:32:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b9045ca4-27ba-32a0-b5cd-d1777f7a087f | -20.58665 | -45.88285 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28078528-2b31-38b2-9528-af9c36c52e59 | -21.77683 | -45.52388 | 2025-10-01 03:32:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aba58259-2752-3d28-aa6f-a17d16ca3ecd | -19.86727 | -42.59362 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| addbeaca-90fe-3816-9273-3ef53e9e7bbd | -14.7036 | -48.27717 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d5c6677-43b3-3638-83bb-a9b231040ae0 | -15.48831 | -45.91273 | 2025-10-01 03:32:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 817b80c1-0176-36d0-81f9-bf3a4d633b86 | -13.93642 | -48.11058 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8927b05d-1cd6-314e-8e2e-19f2dcb41e24 | -18.27715 | -43.7166 | 2025-10-01 03:32:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9064341-8657-3b7a-9f88-ada6d525a454 | -19.86255 | -43.8283 | 2025-10-01 03:32:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 507fa13a-2f1f-3215-b6e0-0a36bf848cea | -20.61456 | -46.21426 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b314eada-ddea-3297-a56f-e38c68671398 | -16.4008 | -47.04629 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13836a48-3e67-3ac7-8da1-1fcceb75aa3f | -15.6344 | -46.26436 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e0ec000-8454-3143-a527-5dda2da6ed0e | -14.68855 | -45.27574 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d391f71d-6c1b-3214-a5dc-ff18b56b4006 | -18.95894 | -43.70701 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0fccc8df-38c0-3a88-b4d3-832ed4a5dde9 | -21.77134 | -45.52341 | 2025-10-01 03:32:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| d2ab7b45-3b1a-3b42-9d8f-b72bc683ec69 | -20.12594 | -46.33736 | 2025-10-01 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 79e5f128-0e23-30ba-84a1-d41ed1a54fe2 | -14.87431 | -48.32877 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1798ee70-38b8-3be2-b96e-f0b084e9d491 | -19.93106 | -43.90031 | 2025-10-01 03:32:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ff9f8610-a74c-36a2-9e28-e891d82e949c | -15.78273 | -43.68589 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32676f0c-5cb3-3faa-8709-6b0b1b4356af | -20.62407 | -46.21803 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 22137633-86a1-3d55-afcf-5f45ed0623f2 | -14.67727 | -46.96788 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9979ce64-0f27-31b9-b316-f92d89ed4968 | -18.80489 | -47.5553 | 2025-10-01 03:32:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ada5636-33bd-3742-ae3f-2af7f8c1c27b | -21.0408 | -45.67842 | 2025-10-01 03:32:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de2d5095-f0d4-3e59-9332-18ab413896a0 | -14.67327 | -46.95438 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db28bbb0-32e3-366c-b3f6-2985142a0197 | -14.75831 | -45.75462 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b603c50-041c-3eba-a5d2-6c9d2c63a813 | -20.49899 | -43.94011 | 2025-10-01 03:32:00 | NOAA-20 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 37e2523a-f082-3ec8-b717-6aa669fcf637 | -14.60141 | -48.32097 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85519d29-03dd-3ade-be55-b5a4c72681ae | -20.5285 | -43.4458 | 2025-10-01 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 797a62f9-67a4-325b-80d0-94981dddf9bc | -15.75278 | -43.72327 | 2025-10-01 03:32:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d439fb-3c42-387d-b5bd-c24fbd40bde5 | -13.93241 | -48.12846 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0730238-83a8-310a-83c5-ac0ef96b54a0 | -15.3061 | -46.4019 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d229eafb-0273-38f3-836e-8ffc7ba7cb86 | -17.40575 | -47.15104 | 2025-10-01 03:32:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58b93de7-8a5f-3891-a26e-89c722348318 | -14.70845 | -48.22238 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ad0f283-e8fc-3e66-9bcc-506ba04b1cac | -15.13153 | -46.45658 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed4b88ee-e30f-3b7b-babe-5950564ac770 | -15.24812 | -46.97101 | 2025-10-01 03:32:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06a61507-44fa-35f3-8a29-a3975d291909 | -14.96 | -46.87055 | 2025-10-01 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b32908-e999-391f-9efd-49bb9a511c98 | -15.106 | -44.95116 | 2025-10-01 03:32:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77fd5551-cf12-3862-a335-029714ace086 | -16.39441 | -47.04458 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e40f4e26-0e04-3363-a513-7914d9708176 | -15.76143 | -43.68116 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e65360b-4425-35ba-b432-e8c657f1c29f | -15.76285 | -43.67424 | 2025-10-01 03:32:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46e5c7d1-066d-3143-9958-e4bd911a426b | -15.27651 | -46.4156 | 2025-10-01 03:32:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab4e4af1-187c-3f4b-b010-70e97c18ddae | -14.89115 | -48.13679 | 2025-10-01 03:32:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 129cb3a7-f5fd-38f5-9c69-4806f0ec3887 | -13.92307 | -48.09103 | 2025-10-01 03:32:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c30b941-fe0a-3443-8c34-2bf271a247bf | -18.33579 | -41.80326 | 2025-10-01 03:32:00 | NOAA-20 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 805b1744-724a-30e9-8299-a46d00bfd551 | -14.92027 | -47.82257 | 2025-10-01 03:32:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e9830416-462b-3ab9-8de8-dfe3787f3f63 | -15.39272 | -40.31862 | 2025-10-01 03:32:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ef41e862-9df7-3a5a-a527-769203b6c419 | -17.96814 | -45.01897 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f85c5dd-9581-39f0-b0df-f8fa4f749164 | -16.37855 | -47.02457 | 2025-10-01 03:32:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1e5ecdf5-91dc-329b-b329-de5c0ad7e968 | -20.69926 | -41.56709 | 2025-10-01 03:32:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 00154390-a824-3a51-9049-8838376c2e89 | -17.96515 | -45.0154 | 2025-10-01 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c455e26f-baf2-3d48-b0e8-f7d312581625 | -20.34774 | -43.33667 | 2025-10-01 03:32:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3f13088d-f98d-37e7-a8bc-811bb2664d49 | -18.3241 | -44.77442 | 2025-10-01 03:32:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91d6a036-0637-3b01-b2b9-2a5db3ad7820 | -20.59399 | -45.88678 | 2025-10-01 03:32:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c94c9fe-5268-3d71-9015-0381534eafff | -14.68031 | -48.23462 | 2025-10-01 03:32:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fbe392a-4fbf-35c0-a04c-95ed7f0d8258 | -20.22777 | -43.89485 | 2025-10-01 03:32:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6102ddc6-a29b-32ce-931d-73c190ec770c | -19.88787 | -42.62748 | 2025-10-01 03:32:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3771a303-f9e0-3464-bfc5-8a4d3832df01 | -20.61741 | -46.22116 | 2025-10-01 03:32:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a0c03688-6abd-3a72-a718-db5cfbed8e43 | -14.78999 | -45.78749 | 2025-10-01 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 022aa6ad-846a-3e79-b0c3-92ca30adba79 | -18.80396 | -47.55234 | 2025-10-01 03:32:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25083b83-964f-3a1d-b9ed-d4746617ceee | -21.01709 | -45.18503 | 2025-10-01 03:32:00 | NOAA-20 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 221dbe5b-478f-372c-a9bf-b763feceec63 | -22.11844 | -44.68721 | 2025-10-01 03:32:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2fa3df63-a943-3508-96df-e581ca16b979 | -23.33451 | -46.86856 | 2025-10-01 03:34:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 187a7458-ca41-3d4b-8ef7-cb637380c4ce | -22.26292 | -46.72218 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a21462a3-3a26-3e7f-b6eb-1c20fbf6b7ea | -23.58835 | -46.21964 | 2025-10-01 03:34:00 | NOAA-20 | MOGI DAS CRUZES | SÃO PAULO | Brasil | 3530607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8324fe77-b376-3b2b-ae3b-8aca96fb0311 | -22.27198 | -46.72692 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ad86778f-4a5f-3586-bb4a-74d9a0cd0b3b | -23.38095 | -46.4188 | 2025-10-01 03:34:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 669e0caa-874b-32b4-9b03-f2b03f9df91a | -22.60861 | -44.51211 | 2025-10-01 03:34:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a387489a-cd77-362b-8f82-670a3519cd36 | -22.7712 | -47.61256 | 2025-10-01 03:34:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5c9ec3e0-99c1-3c03-82e0-99c7aa9c8768 | -23.05901 | -47.03363 | 2025-10-01 03:34:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ceecdb2f-eab3-3a6e-b71a-671c08d47141 | -23.16799 | -45.73463 | 2025-10-01 03:34:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85ff6744-c290-3622-87e2-6b6d6dec39e8 | -22.2731 | -46.72189 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0c12465-5e1d-3077-a5bc-a28627f3d2fe | -22.58113 | -46.78118 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d3512351-8e90-3144-aadc-41cf13f7da09 | -22.64281 | -46.75418 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0acfca8-98dd-39ac-9af0-0c106dc9d168 | -22.5867 | -46.78288 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 8f0bfefe-6d30-33a8-af5f-a228d7422a48 | -22.21816 | -46.14334 | 2025-10-01 03:34:00 | NOAA-20 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a41d9d90-d898-3ca5-88c2-1774e2e0a80f | -23.16719 | -45.73817 | 2025-10-01 03:34:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 63c89223-19c3-32c0-b767-09136289402a | -22.27437 | -46.72435 | 2025-10-01 03:34:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 739fad70-3bb9-3279-8e33-779600b109c1 | -23.38178 | -46.41511 | 2025-10-01 03:34:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b19a726-4ebc-3fa7-bf2b-ae3c47f6a0a7 | -22.92351 | -45.50659 | 2025-10-01 03:34:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5b6ab1d4-1517-3e29-93e4-1ff005d960d8 | -23.32626 | -46.86464 | 2025-10-01 03:34:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a0a042b4-a36b-3d19-8b7a-a4d0fe439a40 | -23.05841 | -47.02945 | 2025-10-01 03:34:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18776c1b-e9ba-35c7-9b72-5949665d7adc | -22.58233 | -46.78422 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| db61a372-3124-3273-9f2c-e9741a041de2 | -22.64187 | -46.75831 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ed00216d-1146-3748-a461-820ae6dd63a5 | -22.91007 | -43.76869 | 2025-10-01 03:34:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d1863098-1cf0-3d8a-9f54-2e9efe6bd4ee | -22.58013 | -46.78562 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8ab5f6b1-4bcd-3584-9d9f-dbc4b026b692 | -22.219 | -46.13964 | 2025-10-01 03:34:00 | NOAA-20 | BORDA DA MATA | MINAS GERAIS | Brasil | 3108305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6f95a17c-07d4-318e-a8c1-54638e447176 | -22.58335 | -46.77985 | 2025-10-01 03:34:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9eff8807-2b43-381a-8a1a-46eb7096317c | -22.43531 | -48.31768 | 2025-10-01 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b08d7e3-d522-311e-99a1-9c86b10b0419 | -23.39947 | -47.05791 | 2025-10-01 03:34:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 24f67c55-b47e-374c-a481-e4c2cf0dcee6 | -23.06004 | -47.02924 | 2025-10-01 03:34:00 | NOAA-20 | VINHEDO | SÃO PAULO | Brasil | 3556701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
