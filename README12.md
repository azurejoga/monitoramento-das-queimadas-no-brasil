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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ef462f1-a1cf-3524-aab9-8f8c5a64180a | -8.45658 | -44.19211 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b150b61-d70f-3c76-9584-d43db38cb402 | -7.57503 | -42.69642 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad2338ba-4e37-3dab-b20b-2672b9f6d67e | -8.27979 | -43.39523 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1c610a8d-1a05-37bf-9c94-c9e99a47fd59 | -4.42073 | -47.7569 | 2025-10-15 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57fb3360-803f-39ce-b049-4b2aeaa6e97a | -8.20923 | -43.32635 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eda5bf38-8977-33e1-9a11-bb66f7987e54 | -6.53799 | -41.48043 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0b751bd4-15b8-3307-b927-0e71aa4b9118 | -4.82428 | -45.44785 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c08fb08-4a27-376b-8531-c1b1f65e25ff | -8.06033 | -45.92139 | 2025-10-15 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 478bcc2c-60b1-37e9-acf3-d369b70e2997 | -7.50767 | -46.6464 | 2025-10-15 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0613986a-60c2-356f-8d1d-5562181228bc | -8.28487 | -43.4232 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 57158045-3401-38cc-a009-f859c1d78410 | -8.21017 | -43.32093 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6a2e7e3c-8646-391a-a4c6-36aba4db7f8c | -8.22191 | -44.09597 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f91ad661-0519-3a3b-a0b9-6ee5b4e08109 | -6.44655 | -43.81922 | 2025-10-15 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a69b9db1-8277-3118-a3be-1a226a90f84c | -6.14948 | -41.77781 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4d31e6b-434f-3962-b4bf-bd75049e488a | -5.63226 | -42.68398 | 2025-10-15 03:47:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 89ec38b0-2500-3b54-bf19-3f1d7ad6be01 | -5.42854 | -41.33769 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b35c03b2-8957-345b-8444-616cc020ebf5 | -4.82058 | -45.44785 | 2025-10-15 03:47:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf46c32b-e31e-3a74-9b63-de315732c7c2 | -8.19916 | -43.99124 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77ced36c-3bca-3a0e-81d9-990786808650 | -4.90047 | -43.46939 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d112f64-ab8b-34b7-84ae-5c8f8023078b | -7.94898 | -44.13871 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2a8e1d1-1205-3695-912f-79cb5f635ced | -6.05345 | -41.90097 | 2025-10-15 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bda20418-0751-30f7-a8ba-a74ae1008bdf | -5.67348 | -44.25374 | 2025-10-15 03:47:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ff07750-d423-335e-920e-2f36255df18b | -5.4249 | -44.22647 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6056b3f4-3590-3a2c-9d65-bbc576001650 | -7.95356 | -44.14268 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| da7ccf7e-9a48-3b01-96ab-f1b9884ed969 | -4.8674 | -45.54741 | 2025-10-15 03:47:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c41b557e-8ed4-3be3-aebe-faef4f27ca6a | -5.39039 | -41.16564 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 29fd89db-2150-3443-811f-5648e7f1884b | -4.65252 | -43.12379 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b46945f6-1162-3a8a-9376-d08425288263 | -6.23379 | -44.17123 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a4d3e93-a07a-3b64-9c5e-92292a53115c | -8.21736 | -44.09216 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77224498-6bee-3ffd-b640-c8ecd363676c | -4.89693 | -43.45911 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 98382563-5219-3bea-b642-23300cf404cb | -8.06104 | -45.9175 | 2025-10-15 03:47:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6264f37c-9219-3677-8b70-330e01f92a92 | -6.45494 | -41.88575 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76aedd44-1215-3c44-ba42-7387d0662ad0 | -4.77149 | -45.73345 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2fe2fdeb-4617-3a36-9c18-66f6f9f6d983 | -8.22406 | -44.0841 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eda47641-cd0b-36f2-8ed0-1ff46c9d2dda | -5.83418 | -42.32999 | 2025-10-15 03:47:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 84d8cf2e-0282-37ba-875f-2cc709062ac3 | -5.34175 | -43.74442 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84dee128-bcd9-3d01-bd39-47718d64e125 | -7.94334 | -44.14076 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33fc0125-6f9a-38e6-a9d6-f91c108c24ac | -8.18029 | -44.01793 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3d3fbeb-47d8-3f9f-b844-51102e29ea0f | -6.23544 | -44.16817 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| feb9a99c-d6b0-3b85-923f-8c6ec325ad79 | -10.80797 | -43.94691 | 2025-10-15 03:47:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af7ab700-94c8-39b3-9f97-7d6414cec1be | -5.3176 | -42.91586 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df7bf833-278a-3afc-99a4-9db117612764 | -5.31669 | -42.92117 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9224e88c-9214-366c-a1c4-326a39c58fd2 | -6.54673 | -44.7208 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b67dd8f7-b23e-3d98-b0a8-e62f47c11e20 | -6.99379 | -38.44677 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb11b215-c3ec-30cc-991f-762365fdc3af | -6.22827 | -41.55666 | 2025-10-15 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a697b32-9e96-32bd-a77e-780c5229c047 | -4.99923 | -44.49746 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98b13ecb-a7b2-35d5-b0bc-95143c3a9228 | -6.05876 | -41.89714 | 2025-10-15 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 776a5197-d665-3ee0-8be1-e21d1bea9942 | -5.97556 | -42.93271 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| eee28f05-6920-3675-801e-df9bc01604c4 | -7.75488 | -42.44963 | 2025-10-15 03:47:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9e2cadee-ac2a-36ac-82a2-2f55466033a4 | -7.57418 | -42.68902 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5e63d4a-f99b-3b39-b072-62f7217283ba | -4.27221 | -44.36456 | 2025-10-15 03:47:00 | NPP-375D | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0618b5d7-cf3f-34ae-8f7d-a985a6fdcff9 | -5.61555 | -42.72436 | 2025-10-15 03:47:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 02eb2867-ddef-3839-b3e5-78e8d7ad1708 | -7.5398 | -42.69307 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f7542b2b-6bdf-347c-bd4d-895e7af7a23c | -7.95088 | -44.14114 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a2ae046-4dbb-3716-a1b4-0b1609455aea | -5.86323 | -43.86434 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76380729-288c-3883-9991-2abb2651ce14 | -8.20819 | -43.32178 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7acf17c-c691-3fbc-a849-21088f5760f9 | -8.20367 | -43.99505 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d288c375-1efe-3df3-b39c-d6f0cb5c017f | -7.93929 | -44.13377 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e266dff9-17b6-3950-a98f-c118cc596c21 | -8.46724 | -44.19128 | 2025-10-15 03:47:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2f3d00e5-b4de-32e8-8d5b-9dc9dfa3a96f | -15.41749 | -42.01784 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 259d5f46-12a4-3869-a33f-c8fd8baccd8b | -9.90801 | -36.38446 | 2025-10-15 03:47:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 38a944c8-6190-3823-b76f-ddeb4ae3532a | -7.95545 | -44.14507 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d0edc8-b2ab-3fe0-adf1-04f9bbe931b7 | -8.18319 | -43.97201 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 491fe8b7-beac-3901-94f7-dd24a012ef21 | -6.22962 | -44.17039 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 582cbbff-d73a-39d4-b170-9ca9c8bf1a9b | -5.42842 | -41.34366 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3f1403a-db10-3bfd-8c35-2dd391161823 | -7.57328 | -42.70629 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59867c19-4415-3445-ad5a-515fbc990d8a | -8.28455 | -43.4412 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 730c4e04-4761-3f3a-8c63-7e7c0c77da99 | -7.18722 | -41.3948 | 2025-10-15 03:47:00 | NPP-375D | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3037909b-9297-31cb-bb83-a279fe6e6d75 | -5.18615 | -42.90838 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cea9f81d-3cc5-3019-9909-fdd9c63030e3 | -5.42925 | -41.3336 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ce1c363-6dc6-33ce-9d3c-4e1a7c23bfcd | -8.2198 | -43.32276 | 2025-10-15 03:47:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b34e642f-4de1-33c3-9691-83191dbaefcd | -5.45557 | -42.3653 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 154a478c-ed30-3cc8-a46d-0869343ccc0a | -5.34748 | -43.742 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9dc7f41-dca2-3ff3-ae69-b94238dc6419 | -5.86491 | -43.85447 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7622707b-a05e-3f02-b00b-e1c8b63ef803 | -5.05951 | -44.44424 | 2025-10-15 03:47:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a1b05f-a8b8-3703-bdb1-6ca2bec44b73 | -5.42908 | -44.23428 | 2025-10-15 03:47:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5d184fd9-20e9-3c4b-a304-1cd595034377 | -4.92388 | -41.53786 | 2025-10-15 03:47:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8772813b-5e21-356d-ac14-cfb4b14c531f | -6.44709 | -43.81612 | 2025-10-15 03:47:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5a399b8-3bf2-33c2-a4c1-50868e75aa05 | -8.20657 | -44.00769 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cecc649c-5f1c-355c-b326-b33aecf09792 | -5.28207 | -43.24381 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f28083f2-e5d1-3ec3-b24a-37e6fdb6f0aa | -7.5725 | -42.69886 | 2025-10-15 03:47:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5d69d264-094f-3eb4-86b9-e99fb64f47af | -6.23069 | -44.16418 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 879691d8-21f5-309a-8e7f-da14dbdf96bd | -5.90272 | -38.15438 | 2025-10-15 03:47:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dec94725-83d8-3f25-9f22-008be5ed7992 | -5.16536 | -45.16904 | 2025-10-15 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54542aa1-8c31-3cee-abc9-48bda012bf5c | -5.68003 | -46.42649 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bcf6ef1b-cd04-35ac-b5d0-9fc481c3a02a | -4.11164 | -48.02718 | 2025-10-15 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 35b23152-6a47-351c-8cff-38c389900178 | -5.26332 | -41.01674 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 382d5dd8-7c4f-3b8a-84c9-04cc7dbdbd7f | -4.35772 | -46.78276 | 2025-10-15 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62d2d368-d183-3bdc-9cfc-972e09721658 | -4.65807 | -43.12173 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1a478d24-47cc-3d00-8666-b9cb40b297a5 | -6.8882 | -43.96519 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab0019bb-6c29-3e36-8d60-3767378d5c64 | -6.22962 | -44.16413 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c71f078d-8bf2-353c-8560-f75c2f96e68a | -9.90857 | -36.38095 | 2025-10-15 03:47:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2b3bbde9-41e4-34b0-9ac9-4827d686d99a | -5.47358 | -44.66003 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1faee406-9d14-3016-b44e-43096de0d940 | -6.91428 | -42.23936 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4a2abd73-f8c0-3c20-b2a8-774bbab91337 | -8.21237 | -44.03312 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b452032-1529-3bb2-8a9c-93785829c614 | -5.15455 | -45.16322 | 2025-10-15 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1c1bd3b-ecdc-325f-8c61-73a5272fe308 | -8.2179 | -44.08916 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 933be657-18a8-3966-b7c4-5577824ed46a | -4.32159 | -44.54289 | 2025-10-15 03:47:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a749e4d-8ba9-3a9c-bbe8-779b077f360a | -5.57731 | -44.7476 | 2025-10-15 03:47:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca46d52b-f416-31be-b3d7-a26ff06dfa95 | -5.00474 | -44.49841 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
