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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ef9fd36-16e6-36c4-8a78-3663332e623e | -11.48348 | -43.61458 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e33ec7f0-d8ef-3fe4-9443-8f62d401ceb9 | -11.43705 | -43.56066 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4bd50e2-f484-37e6-83d5-c855fdad15fc | -7.57342 | -42.64492 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c32fe58f-e808-3e09-af8e-97f3d9b3b0b8 | -11.43835 | -43.5543 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d79d8ddd-62e8-328d-ad03-bee4a826919e | -7.57369 | -42.64418 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 004f557b-425e-3e15-bea8-7342fed41469 | -11.43288 | -43.55116 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b75d7b05-ce9b-3a15-aae1-caae91226fde | -11.49456 | -43.69838 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa191874-6044-3a78-a1a6-f02bafb80634 | -11.44385 | -43.56639 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 28a98acc-a5df-3816-885c-195d1a76019b | -8.02759 | -39.58929 | 2025-09-13 03:17:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df75e584-3e42-3fda-b8b5-e030b25a4c8b | -11.43151 | -43.55309 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5f305901-5a0e-3297-b69a-35ea03b8af9d | -11.4328 | -43.5468 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2fb5ed09-f610-3272-9408-cd1f1ed23d62 | -11.44933 | -43.57406 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a384126-49bd-3589-a8cd-74c2255c9f3e | -11.44808 | -43.57605 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca18fc94-fa29-3bd4-9dac-3c081e3ccd2f | -11.45612 | -43.57553 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6f8eca8-4546-3f97-b39c-0e0dd11a3fb7 | -7.55965 | -42.64241 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3320b04c-498d-3f10-8fbe-6c7f95434f04 | -8.32833 | -38.09326 | 2025-09-13 03:17:00 | NOAA-21 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bbc5befd-7c93-3da4-ae0b-5ed670d94516 | -11.48638 | -43.70337 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2a0f00f-4fd9-309b-a3b3-54861b75cf51 | -7.55424 | -42.63393 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6491e652-3537-377c-8791-317196a21f45 | -11.43838 | -43.55867 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b8564d9a-0492-3a57-9d67-e477c880d9ed | -11.45488 | -43.57754 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd3621fc-963a-35bf-aa45-f4ee165e140f | -11.42728 | -43.53916 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79313694-526a-32d4-9df0-d074f01b855b | -11.36313 | -43.50693 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a9ea370-eb03-3192-8ca7-e9e76d25267a | -8.02999 | -39.58894 | 2025-09-13 03:17:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f992241e-8543-3b51-b876-c9288c873b26 | -11.47668 | -43.61304 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9200551-f22b-360b-ab81-b49765b692e4 | -7.5628 | -42.66283 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a86f2d65-92d2-368f-9653-dcdbf76c440e | -7.56443 | -42.65553 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e129f9db-c874-3105-9f77-a305b08217b4 | -10.77251 | -41.33845 | 2025-09-13 03:17:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0d26d59b-e781-3127-9b16-0310b1dc148c | -7.56653 | -42.64368 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 396b16c8-becf-3c63-b16e-6eeb070346ce | -11.46989 | -43.61151 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cac39c3f-6859-3c05-ae59-d52bc0d78716 | -11.36447 | -43.50058 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 98766212-16ed-34ba-bf78-66df07a17c5d | -6.91408 | -38.25375 | 2025-09-13 03:17:00 | NOAA-21 | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87a7b255-d7a0-381a-baf1-453da4f9a042 | -7.5632 | -42.66206 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8ac6a5fc-935a-3cda-b3ec-b03ff9453352 | -9.41577 | -43.40628 | 2025-09-13 03:17:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 72768388-5a76-3c6b-9071-baf6f684a1c3 | -11.36191 | -43.50598 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cb0cbbd0-2851-3f28-834c-f95351438e39 | -8.32778 | -38.09631 | 2025-09-13 03:17:00 | NOAA-21 | BETÂNIA | PERNAMBUCO | Brasil | 2601805 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a1658905-edfe-3df6-b7d2-477ac17805f7 | -7.56407 | -42.65631 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 828de86c-f327-3613-a5ea-00ecfafcac23 | -11.44385 | -43.56208 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d521d47b-b0f1-390d-a79c-746131f7586e | -7.56531 | -42.64993 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8f5a78b5-3db7-3443-87e9-edcef9192fa0 | -9.85323 | -43.14529 | 2025-09-13 03:17:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7ea68593-777f-3451-b746-49a52c46ed21 | -7.55401 | -42.63477 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f5b0a047-2313-333e-9eaf-bc6ed27b0179 | -11.43154 | -43.55747 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37a03460-f569-3c74-a1af-5e5344ab8084 | -7.63104 | -40.45347 | 2025-09-13 03:17:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4c1cd6bc-8087-3496-80c8-d344a5f48708 | -17.35949 | -42.69848 | 2025-09-13 03:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 34692857-5207-3f47-9165-35730598e697 | -16.28133 | -45.68312 | 2025-09-13 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b2cf887-b3b6-3eb9-b562-62f398db6cdb | -18.47415 | -39.7606 | 2025-09-13 03:19:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| fd25bfe2-22b5-35b8-a0ac-2ae1d4821521 | -17.2875 | -46.09863 | 2025-09-13 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 881e68ec-e0fc-3283-93d1-ac4d7d6d6364 | -13.58249 | -44.89476 | 2025-09-13 03:19:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e7109cfa-a161-3970-a40b-cec135b5bd38 | -16.28495 | -45.68688 | 2025-09-13 03:19:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 90ff8347-da17-3a30-87bb-c612e3b42ca9 | -12.39902 | -43.82571 | 2025-09-13 03:19:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9cabdcd8-b732-36dd-92e2-9ad073fbc0ee | -16.78212 | -41.71616 | 2025-09-13 03:19:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f23c9ccd-ab60-3d09-a490-b305e8989a84 | -16.81678 | -42.21598 | 2025-09-13 03:19:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a76c213e-b7a6-3439-82f2-95b9a8c7bc42 | -11.93631 | -44.29468 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e9da525-95a4-330a-ac47-b8234868b905 | -11.73243 | -44.20805 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d10c0cd-9401-3b88-aa03-5e491941c691 | -16.85355 | -41.53822 | 2025-09-13 03:19:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4b43d2d0-b799-39c7-9570-00b640e65586 | -18.06984 | -45.45678 | 2025-09-13 03:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7fb02573-efd1-32bf-975b-5c93d9b4e216 | -11.73533 | -44.2166 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5c002b15-316a-3e3d-be91-faf84fcef23a | -17.54504 | -44.54486 | 2025-09-13 03:19:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e44d6e15-acd2-3df9-81c5-0df8d61adbbc | -15.2421 | -44.06326 | 2025-09-13 03:19:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cc803830-3409-3268-8c97-fb89f4e5500f | -12.40077 | -43.82352 | 2025-09-13 03:19:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9e1aae6-7db5-3731-a85d-86474b584ba5 | -17.91718 | -44.45946 | 2025-09-13 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1e76ba0-bcdd-34de-94da-4cd88f57d054 | -15.32422 | -42.05143 | 2025-09-13 03:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1c13df55-6342-3245-a425-cbcf5c064dde | -17.35859 | -42.70268 | 2025-09-13 03:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2fbf5efb-d6a1-30a1-8df6-221e70e7e85a | -16.5271 | -43.73639 | 2025-09-13 03:19:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 824655e7-c2f4-34b5-94e7-30bdd512b9f8 | -15.53722 | -42.57166 | 2025-09-13 03:19:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22b5f9ab-16d8-3355-a981-c713cf3474cc | -16.97715 | -45.81575 | 2025-09-13 03:19:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f761687b-9989-36bf-8d10-14679b4bb83e | -13.00523 | -44.11816 | 2025-09-13 03:19:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 757eecd1-c6e3-3548-92f8-78615973cb9b | -17.36339 | -42.70879 | 2025-09-13 03:19:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f32667de-108c-362d-9ed7-388427fba9a1 | -15.05422 | -42.24923 | 2025-09-13 03:19:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a91fe7fc-410a-3a9e-889f-f167f777bbf7 | -14.68783 | -43.66584 | 2025-09-13 03:19:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee75508c-8c65-34f5-b697-3db3f9e068f9 | -17.91852 | -44.45358 | 2025-09-13 03:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| acfd5655-8711-39f5-b1a9-5e39b48d3d78 | -17.36378 | -42.70203 | 2025-09-13 03:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| c1f91927-2065-32a2-8617-21950319bbee | -17.35699 | -42.70509 | 2025-09-13 03:19:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| de9babe0-607a-357f-ba7c-c17e40f4f963 | -14.2274 | -43.51279 | 2025-09-13 03:19:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69a04f37-5c5a-3690-a7e6-eb2cdeff36c0 | -17.95299 | -42.52613 | 2025-09-13 03:19:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 972acfd8-6aa2-3053-9fbf-1cb701bb8616 | -11.73945 | -44.20949 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09d39fb4-459a-3844-bb16-6a13eba57442 | -17.35763 | -42.70717 | 2025-09-13 03:19:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cca95a96-ca0e-382f-99a5-683a1d8158e3 | -17.35528 | -42.63269 | 2025-09-13 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8019d219-3ebe-3760-9628-886e1439b872 | -16.84406 | -40.86224 | 2025-09-13 03:19:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 56d74bdc-c5bf-3d63-a00c-875626be6b3d | -17.28268 | -46.10448 | 2025-09-13 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 6fb7c88b-6298-3582-acc1-baee99617aa4 | -16.84859 | -40.86694 | 2025-09-13 03:19:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 95355f17-53b7-33eb-834d-d4d655509b63 | -17.35794 | -42.70079 | 2025-09-13 03:19:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5b988574-601b-3ce8-8fde-1839944c2914 | -17.5437 | -44.55073 | 2025-09-13 03:19:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2c74b670-662e-3a2f-9c6c-cd3bcd683c58 | -18.05511 | -45.45916 | 2025-09-13 03:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bddf716-c676-3ca2-a6c6-48c2fb593c9b | -14.22093 | -43.51139 | 2025-09-13 03:19:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88fcb903-b060-30e1-a00c-03b83bbe4d9d | -18.28033 | -42.59954 | 2025-09-13 03:19:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d26376fd-c0ab-3d31-8ba4-34852b793466 | -13.58405 | -44.88766 | 2025-09-13 03:19:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4d2df39d-544b-398d-aa6e-98ed8b411e4d | -11.738 | -44.21646 | 2025-09-13 03:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 319f8b28-63bf-3c67-9f81-94f10a8a65de | -17.36441 | -42.70401 | 2025-09-13 03:19:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1ef0f6f1-1d7a-366e-95ce-dafd7672f5a9 | -17.3495 | -42.63132 | 2025-09-13 03:19:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ebb0e54a-b9fb-3daa-ab64-55f2c3cb1266 | -18.4431 | -45.93424 | 2025-09-13 03:19:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c096167-6034-3146-ab34-d4e164bfd831 | -16.53339 | -43.73777 | 2025-09-13 03:19:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5bb4d79b-65bf-3763-b8cb-23253b97387c | -15.32339 | -42.05183 | 2025-09-13 03:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 333c5862-f42d-3272-824b-2c7263fb336e | -16.84939 | -40.86304 | 2025-09-13 03:19:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| bc3b6dbe-fb63-3a62-9960-e1ac31a2e109 | -18.06528 | -45.45511 | 2025-09-13 03:19:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37a76576-5e58-3326-af4d-1dc122bfaba2 | -16.32505 | -43.75883 | 2025-09-13 03:19:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9af5d636-13d5-3556-af59-734ed8d81bf3 | -16.97544 | -45.82308 | 2025-09-13 03:19:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d6f02cd-18f0-3467-8ac7-c59d87ec5d24 | -17.27835 | -46.10604 | 2025-09-13 03:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a7df9eae-623b-36fa-9d69-44a5da497394 | -14.69428 | -43.66733 | 2025-09-13 03:19:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 36525d9e-4789-3681-a345-9d51384a78cc | -15.24079 | -44.06913 | 2025-09-13 03:19:00 | NOAA-21 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cb89620-96be-32bb-bcc9-7cd55c1284cd | -17.46941 | -43.72506 | 2025-09-13 03:19:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README19.md)
