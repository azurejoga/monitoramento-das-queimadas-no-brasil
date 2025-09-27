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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b252560-8749-337b-9984-90f87eeca1b2 | -5.80132 | -42.83234 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 80e9f3b5-ee81-3f3b-8b22-745a2b71797c | -5.07285 | -44.86005 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9b4e3aa9-8d61-39db-a021-26acb30f757d | -4.79069 | -43.19857 | 2025-09-27 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c751dc73-93a7-3049-8ac6-3812b56ed08c | -5.47537 | -43.0747 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e8362a87-2d2b-3b03-89e9-7fdb45f37e87 | -5.4985 | -42.19412 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c361d416-0b01-311f-8595-a6e445c519a1 | -6.06752 | -44.07181 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38a97012-6a8c-3161-adb9-50393724dbda | -6.27531 | -44.07701 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ddabf841-79eb-3cb8-aee0-45af1909e70b | -5.08336 | -44.85244 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 38014d8f-80dd-3efc-8cbb-7210c010ccf6 | -5.08262 | -44.85687 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f354b3f3-7399-3690-a84d-a172f8c612f2 | -5.47822 | -43.08221 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 358c2978-32fb-3463-bcb0-83323346836e | -5.40134 | -42.26547 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d0d738fb-1ab8-3ab3-bc1b-fb2841645caa | -5.47027 | -43.08094 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 9b4e6314-fb74-3510-be11-1f4afdb3b2c6 | -5.80214 | -42.82739 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4fc90c1f-16b9-3158-8a46-89544f6ee28d | -5.26478 | -43.49223 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3975861a-b3c2-3acf-a3be-72b0011fe8a8 | -4.44407 | -40.97058 | 2025-09-27 03:53:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 556ac78d-67cd-3627-8a10-95962d061a20 | -4.06075 | -38.43348 | 2025-09-27 03:53:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d404846-ee77-31fb-b038-4ae2e9a81126 | -6.24147 | -44.09895 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d2054c7-0f82-3b13-a652-803c42ecc689 | -5.48219 | -43.08287 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6d6a8345-3dae-33ad-9e18-9ce3e4dba1a8 | -4.00297 | -46.96238 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0b3e0aa-5da1-3f8d-9d9c-7608e6995e4b | -4.6469 | -50.96955 | 2025-09-27 03:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a4b43eb-3ecb-3a9e-8c24-2eb5e2250f35 | -3.8676 | -38.4311 | 2025-09-27 03:53:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49aaec1c-f3d8-3574-a49f-7d50f969d13f | -3.58174 | -44.25477 | 2025-09-27 03:53:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3dc685a2-2787-36f9-9e83-5159a0afe2c9 | -6.06683 | -44.07592 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00a58395-b534-386d-a91b-ef8984893c68 | -5.4074 | -42.27601 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 781829f4-3ce9-3659-9477-6ebb1cdeaeed | -6.06981 | -43.20374 | 2025-09-27 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 58a9e814-7e5e-3533-a9b6-26e8458ab0ac | -5.99868 | -43.80596 | 2025-09-27 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27a07581-3d98-30b7-acfa-e85fd9b04f66 | -4.57803 | -44.07448 | 2025-09-27 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04ff5b05-0526-3d1a-bf8b-a3da5cbdeb5a | -6.01355 | -42.5148 | 2025-09-27 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6720993b-5aea-321e-a023-0ba13d2eaf24 | -3.72556 | -39.65243 | 2025-09-27 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c6760df5-f714-350f-9141-8f6eec7c2c91 | -5.5264 | -43.87808 | 2025-09-27 03:53:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9b9290d3-9783-37f4-ab93-d5d964fc9416 | -4.00173 | -46.96953 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 110b5c77-f40c-398f-9499-0dc03beafc39 | -5.73982 | -44.98375 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b1f0ba47-8f0a-389d-881a-68731c74fc16 | -5.8363 | -43.92341 | 2025-09-27 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba599634-2132-37bb-8ede-87644c6e9d4d | -5.51446 | -43.8724 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f42f1247-a5da-3921-a3f5-39116278e286 | -6.06872 | -44.87803 | 2025-09-27 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ee1e99-b712-3552-9908-d77a163039b3 | -4.14487 | -39.99861 | 2025-09-27 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f827e73d-c153-3ada-9ab6-e9cdbcfb565a | -5.47306 | -43.0639 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7dd000db-c9c9-399d-9991-15a48276e75e | -6.2319 | -44.18105 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 938141e0-abcf-3215-acf1-c5d5d0e819ea | -6.42556 | -43.07655 | 2025-09-27 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d725b061-2d4a-388c-9c03-11730002218b | -6.26569 | -42.49308 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1efee372-1b5d-3d1c-a566-e69ff608c7d1 | -5.46975 | -41.07252 | 2025-09-27 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e7fc1317-ecff-3f5e-863b-f8991a6335e9 | -5.4663 | -43.08026 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b019990e-927f-3077-90a6-0b821be56173 | -4.00264 | -46.96916 | 2025-09-27 03:53:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86488497-89f0-3c42-a8cb-8c8db89ecab0 | -5.76739 | -42.7965 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 05dab5ac-6dd3-3e10-b7ae-e310281f17d6 | -4.35892 | -40.73344 | 2025-09-27 03:53:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fbd8ec2f-5785-3a36-b65b-7de7405f6fa4 | -5.49862 | -43.08216 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b1ea876b-12b4-3828-a7cf-aa2133ad4bf7 | -5.91602 | -43.96748 | 2025-09-27 03:53:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 276e68bd-7929-3fb6-9b45-afed6a98f7a8 | -4.79039 | -45.3432 | 2025-09-27 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 369653a9-c0d6-3491-878f-dda5fa2db621 | -5.80703 | -42.44681 | 2025-09-27 03:53:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 28b7c0b8-688d-3ef1-8b98-0347a9adf6cd | -5.1472 | -42.67151 | 2025-09-27 03:53:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ec6b3c9-a668-3bef-8aad-8e647584dc2c | -4.266 | -48.55457 | 2025-09-27 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 750058c4-8ae1-3ca5-9651-d75e9f585ec5 | -2.55498 | -48.40623 | 2025-09-27 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d41680b-9d39-3272-b863-08bbd3aad9f3 | -5.74223 | -44.98242 | 2025-09-27 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8dc4061-b6b5-3d10-acd0-74fec7b2e779 | -5.4714 | -43.07406 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 56532bea-3fe9-3ccd-a3d8-e012e2094aeb | -3.23787 | -46.79953 | 2025-09-27 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a22440a-247d-32ab-94ba-22c739797954 | -5.59859 | -45.81226 | 2025-09-27 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0f6797a-25e2-387d-8985-49464c7dac04 | -5.57014 | -43.44132 | 2025-09-27 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 059659fa-f717-305a-8b6c-99969ee7d429 | -3.80328 | -41.56865 | 2025-09-27 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8fcf29b8-554d-3dfc-9bc7-9b36674b9da0 | -4.71552 | -40.68563 | 2025-09-27 03:53:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d4ecad5a-f2d0-30eb-b708-135827b1d7cb | -3.83114 | -40.33579 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d665601b-cb32-36fe-9075-a6268cf3fd8d | -6.33297 | -43.36141 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b69d418d-7500-327d-9996-5bb3fd9c5c0f | -6.09927 | -43.19806 | 2025-09-27 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf61e4e5-14e2-3504-a04d-9ad2b014487c | -5.08786 | -44.85315 | 2025-09-27 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3406c001-91b0-3e3e-9dfb-4eeaf942a7c8 | -3.92769 | -40.75433 | 2025-09-27 03:53:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d314f2bc-7ead-3eec-b5b5-13ef1300a293 | -4.48157 | -47.67442 | 2025-09-27 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16dc3ef6-3931-3c5b-ab83-50243c13ed06 | -5.14587 | -37.74174 | 2025-09-27 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 6000c15d-6008-3e1e-8801-614f9c70cd7e | -6.12875 | -43.45282 | 2025-09-27 03:53:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cdad3ae3-1db7-3e59-a9ed-b29c045e2050 | -5.76498 | -42.80417 | 2025-09-27 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 55ac3688-9bbd-39e9-b5b2-7b696cdba69f | -5.49918 | -43.0787 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 40557d65-1d8d-30b2-9f53-032fb5f3f344 | -5.50609 | -43.8711 | 2025-09-27 03:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd37ecba-dd7c-37ff-977a-01bf35623cf6 | -6.26518 | -42.49639 | 2025-09-27 03:53:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 933bdd49-d598-3aa4-aa26-8169c4bff3e0 | -3.35808 | -43.37856 | 2025-09-27 03:53:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d35924d8-0419-303c-81fa-01c532fb3c75 | -3.89925 | -38.55289 | 2025-09-27 03:53:00 | NOAA-21 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 218fcd77-1234-3d85-947a-8ab2df79a6f1 | -5.56952 | -43.44495 | 2025-09-27 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1eeb67d9-40f4-3518-8249-393ac92f538f | -6.32008 | -43.45244 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2f3d3b9b-4e09-3cdf-b409-58f07fe71409 | -5.36803 | -42.30308 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 39c2560b-baa1-32dd-a1c1-66a719afacc7 | -5.47758 | -43.06119 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3de24b84-a86c-30e4-b4b1-d66dad5b4515 | -5.73167 | -42.64341 | 2025-09-27 03:53:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66e54bc6-085e-3e4d-8588-abf49c19dc46 | -5.30857 | -47.22237 | 2025-09-27 03:53:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bceafe11-b2c7-3819-b6e4-ee4a1c8772ae | -4.45345 | -40.98037 | 2025-09-27 03:53:00 | NOAA-21 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8b9f65ca-dbd1-3938-a678-f9e5b7e69c80 | -4.32461 | -45.27817 | 2025-09-27 03:53:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5524b73c-ab43-3267-894c-6255fa86fb26 | -4.3293 | -45.27896 | 2025-09-27 03:53:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b81b993f-5d27-3fef-b520-b8feeacacae1 | -2.44639 | -49.02826 | 2025-09-27 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4d028412-c343-3fe2-b234-534373c7c89e | -5.0905 | -40.23718 | 2025-09-27 03:53:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae0bc9af-0faf-3d82-bc99-27a007b1a4b8 | -5.80324 | -42.44616 | 2025-09-27 03:53:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 899fb1db-6dae-36f7-b933-6f23928e89da | -4.17897 | -44.27895 | 2025-09-27 03:53:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8a8d10f-0a39-30e4-96be-e619cfde8cc6 | -4.61362 | -40.20896 | 2025-09-27 03:53:00 | NOAA-21 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1bcca2c3-d278-3729-a46d-741b978da51e | -6.87773 | -39.26432 | 2025-09-27 03:53:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7a641ccb-745a-3de5-ae91-20e19c9d2676 | -4.14546 | -39.99487 | 2025-09-27 03:53:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2519a677-0d7c-35f7-b01f-baa16cdc138b | -5.40814 | -42.2714 | 2025-09-27 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 60b8703b-3ae2-3f14-b2a9-d4bc60447b6f | -6.3195 | -43.45599 | 2025-09-27 03:53:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a805a81a-aab6-34ce-b47e-c3b6869778b3 | -3.59065 | -43.10071 | 2025-09-27 03:53:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c31bca3-24ee-3c57-8cdb-b2cba5a2f8f9 | -5.46687 | -43.07684 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| da0b23dd-e7d3-3bff-9fef-de5b16518006 | -5.97302 | -44.11673 | 2025-09-27 03:53:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d6b1a74-7359-3219-8201-ed0c0d825136 | -5.47879 | -43.07875 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 5e98413c-2564-354d-8423-d6f3f5898b10 | -3.86313 | -40.33686 | 2025-09-27 03:53:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4442e9cf-f169-36f8-ae11-505be9726a1f | -5.46854 | -43.06662 | 2025-09-27 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| fec2e91f-80e7-3ad6-83fa-887b3a55e285 | -6.19985 | -44.24166 | 2025-09-27 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf629ad7-199e-3511-9db3-a8d45f93c206 | -6.22983 | -44.19329 | 2025-09-27 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47537341-a2e9-3e41-8d63-095b0bb0afd8 | -4.4819 | -40.7829 | 2025-09-27 03:53:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README14.md)
