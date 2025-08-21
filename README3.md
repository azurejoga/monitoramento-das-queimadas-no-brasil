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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54c8c6ed-2950-3d8a-894e-881dfd415db7 | -9.9268 | -48.68614 | 2025-08-21 00:28:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0db6e242-b25e-349a-9fcc-e85fbf196776 | -14.12481 | -45.39204 | 2025-08-21 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0c62b40d-773b-33f7-b784-c8554a4ea37f | -13.02195 | -45.15461 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d410d236-c5d1-3908-b3ef-f39143ae5f5b | -13.65463 | -42.47758 | 2025-08-21 00:28:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 37.1 |
| daeafc53-d71c-3ccb-9403-f0ca1344e408 | -14.49804 | -45.95777 | 2025-08-21 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 10cbab9c-c042-353d-b6f0-cf9ead41557c | -14.84688 | -47.94232 | 2025-08-21 00:28:00 | TERRA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 34662b6b-8d90-3932-93fe-af4d199a7122 | -12.95928 | -46.21555 | 2025-08-21 00:28:00 | TERRA_M-M | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 95e8a570-9f5b-3645-969a-aad9309ee5bf | -12.21913 | -45.40647 | 2025-08-21 00:28:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.2 |
| fe74e68e-8d21-3758-a4fb-787dbf569218 | -9.48546 | -47.33236 | 2025-08-21 00:28:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6a9e3d19-ff99-3176-8b44-bc7914fd96f6 | -12.89635 | -46.08689 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e9763fd8-db5b-3fdf-b5bf-b4fbc167e8fc | -10.99344 | -55.24641 | 2025-08-21 00:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 2994721d-80b1-3e98-91d0-a723647097f9 | -13.53358 | -47.05043 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 783eec7b-f310-3f73-a98b-5e9e2b084c75 | -13.54254 | -47.04914 | 2025-08-21 00:28:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 975f077c-428c-3312-ba29-fd612e00f8a9 | -14.507 | -45.9396 | 2025-08-21 00:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 0596d0d7-5aa1-3f89-b921-28de49bddbc2 | -12.9726 | -46.2389 | 2025-08-21 00:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 112.2 |
| d5d02e6f-1634-3a3c-9c47-6b8157901e3b | -13.1367 | -54.9171 | 2025-08-21 00:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 59957e61-a95e-3699-b107-816aaa5196e0 | -7.0166 | -44.6184 | 2025-08-21 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 06650f84-4f33-3a97-a31c-ae330c899e02 | -7.0354 | -44.6167 | 2025-08-21 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| fee2c551-de42-31de-8f77-4f9a51721511 | -5.9713 | -44.1312 | 2025-08-21 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4c494ab7-3b46-3fcd-b8fb-b52fde86e89c | -12.9528 | -46.2647 | 2025-08-21 00:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 04f9c325-aec9-3ed1-89cc-9b2283b21376 | -8.69 | -62.1153 | 2025-08-21 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 94948c5f-b6eb-3262-b269-69faf5aff441 | -8.8736 | -62.4115 | 2025-08-21 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 5fa48e6e-561b-386f-9d9c-22cb25edbd1c | -14.8543 | -47.9279 | 2025-08-21 00:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| fd90fc09-9c6a-3b4a-81b6-53ded81b762d | -12.9533 | -46.2419 | 2025-08-21 00:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 486.1 |
| a1ecd6a1-35b8-33c3-8a0f-6878288b5fb2 | -12.934 | -46.2448 | 2025-08-21 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 20c01fa0-6b56-3c6f-b4fc-b6918bdd302c | -12.9537 | -46.219 | 2025-08-21 00:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 3cf8235a-c3b9-3ce8-803e-b11ec7f78409 | -5.9526 | -44.1326 | 2025-08-21 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| edb92cbc-bc4d-30db-a5bd-8d443f478af8 | -15.9046 | -49.0043 | 2025-08-21 00:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 70b2a2f0-d6af-36d2-93b1-351428c12a1a | -15.8849 | -49.0076 | 2025-08-21 00:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a1a7886c-a1db-316b-b3ba-339e0bab3581 | -8.6715 | -62.1161 | 2025-08-21 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 122.9 |
| 93e5e960-61ef-3f0e-b6dd-6a39ed320baa | -12.973 | -46.216 | 2025-08-21 00:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7c54767e-54b6-3b48-af03-2fcf87943240 | -8.6901 | -62.0963 | 2025-08-21 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 2b3553a4-dfe5-3b2c-b52a-d0a1c9248b09 | -8.8737 | -62.3925 | 2025-08-21 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.6 |
| ba97042b-fea8-3799-8d47-257a8a288893 | -8.8551 | -62.4123 | 2025-08-21 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d167d2d2-0d2b-346e-8b72-5a5d87f2ebd2 | -7.0169 | -44.5954 | 2025-08-21 00:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3987a5a3-74cd-39f2-8732-6991b97d3a77 | -8.6716 | -62.0971 | 2025-08-21 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 168.7 |
| e7ec7110-b479-3e80-9425-a803caa235a2 | -8.03071 | -47.6792 | 2025-08-21 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 569abf0b-080b-39b0-a03c-aaed510692e6 | -8.37171 | -54.99838 | 2025-08-21 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 97c15bcb-253a-3d6d-b845-f0ecc70baafd | -3.99458 | -42.52457 | 2025-08-21 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 188e766a-ac66-34a8-afae-80fa60f3a148 | -4.64929 | -43.1303 | 2025-08-21 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1fbd55b0-1920-3097-9893-972ecbea8cb0 | -5.73533 | -49.13813 | 2025-08-21 00:30:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 2608bb0f-2db6-3ff7-bc7b-6a2bca903445 | -5.78863 | -43.61486 | 2025-08-21 00:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 250556d5-08e5-3037-ab24-8a384c3bac3d | -6.20768 | -43.33166 | 2025-08-21 00:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fd4d460b-fe06-3d19-8d83-3b17f9194462 | -7.11677 | -44.66156 | 2025-08-21 00:30:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9ffc8463-447b-357f-a863-2977b399b003 | -5.95551 | -44.1338 | 2025-08-21 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 171.5 |
| b9a44b39-fbc5-30a8-8741-35d73920b253 | -7.8635 | -46.73404 | 2025-08-21 00:30:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 8152b29e-568e-3e4b-9981-f9cea8cd74d0 | -7.6351 | -45.25816 | 2025-08-21 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7904ab64-9889-3fb2-bccf-9a410099bc7f | -6.95311 | -44.16875 | 2025-08-21 00:30:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 29e2d25c-22aa-3608-9d65-90fc97e82a74 | -6.21844 | -43.33001 | 2025-08-21 00:30:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e136f673-0544-3453-bcd3-ce2d0d434988 | -5.08724 | -47.71404 | 2025-08-21 00:30:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 48302f90-3609-3675-acd7-cd4a6443c9aa | -7.74105 | -45.73562 | 2025-08-21 00:30:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fe8efaa-79ce-3e18-966b-50321c37a8b5 | -7.59006 | -44.38803 | 2025-08-21 00:30:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 04511cbf-6eb2-3e0a-93e1-87ed9b283009 | -5.68062 | -43.87322 | 2025-08-21 00:30:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0a2ab6ef-9815-3e01-976e-4f87a6049c71 | -8.37422 | -54.99148 | 2025-08-21 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| f99ef97b-cde4-34e3-8a0c-939b9f720989 | -6.28809 | -43.88609 | 2025-08-21 00:30:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ac05e42a-704d-35e2-b988-ed7e4d0168a3 | -4.31813 | -48.0841 | 2025-08-21 00:30:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b30f7ff4-a96a-376e-a703-c595a7de9b27 | -5.08846 | -47.72284 | 2025-08-21 00:30:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7e27b142-aed0-3f0d-acc6-0848bb4e0264 | -7.02789 | -44.61508 | 2025-08-21 00:30:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 028fefb7-5c98-3c4c-b542-76d64837952c | -5.95721 | -44.14557 | 2025-08-21 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 6f8fbffb-943f-381b-a3c0-b780011f6c64 | -4.31053 | -48.09414 | 2025-08-21 00:30:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0db05f66-6f9c-382e-9760-1d0f21a31561 | -6.10023 | -45.41562 | 2025-08-21 00:30:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b31bd977-f6a6-36b3-b371-f4421d2abac1 | -5.87343 | -50.14836 | 2025-08-21 00:30:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 24941117-f770-3bc0-bbcd-68ed77964a9b | -5.10112 | -43.15763 | 2025-08-21 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 73424690-44c7-3fa6-aee0-40256482dd56 | -6.45449 | -53.39024 | 2025-08-21 00:30:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 8128574b-e53c-36fd-8812-86ce2e1bde37 | -5.8878 | -46.51247 | 2025-08-21 00:30:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 53720668-af27-3367-a725-a4851708b550 | -6.8093 | -50.09232 | 2025-08-21 00:30:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 56b2b2d0-5056-366a-a881-e3cdfa888742 | -7.02948 | -44.62606 | 2025-08-21 00:30:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 06cdf447-22ae-3c3b-a04c-1a5842edf6ac | -4.94205 | -47.46215 | 2025-08-21 00:30:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 365b26e7-a208-3636-8485-6a4e77aa6b3d | -4.95089 | -47.4609 | 2025-08-21 00:30:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 652cb13f-099b-3f0c-bacc-7a151180ffea | -3.98009 | -42.50946 | 2025-08-21 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| f113a3b4-1551-3cfd-a4d5-44ba233fe2da | -5.8806 | -48.12005 | 2025-08-21 00:30:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 603ccec8-6fbb-32e5-bfe6-b7de79cc2bfb | -4.31175 | -48.10293 | 2025-08-21 00:30:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 853ef63e-0ee2-3a81-8571-386753c42a66 | -5.87938 | -48.11118 | 2025-08-21 00:30:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f4b09cc0-cd19-3e3d-8375-e33e398df168 | -5.48541 | -42.16662 | 2025-08-21 00:30:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 0f03a0f5-20f5-3b36-92ed-d4d05b00f9f9 | -8.30758 | -49.02964 | 2025-08-21 00:30:00 | TERRA_M-M | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d4a1885f-4ccc-34b2-bbb2-3e28095c7a87 | -5.47432 | -44.70207 | 2025-08-21 00:30:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 85175c0c-c1d9-3c35-966b-dff2403e02d2 | -6.17699 | -44.74112 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 0c82ab64-b6d9-35e3-bd26-ce2eb64bcd8f | -5.67875 | -43.86057 | 2025-08-21 00:30:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9b8fe136-efad-3452-bb91-3eae3aa711dd | -7.279 | -49.39829 | 2025-08-21 00:30:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 6fae5952-484c-33e8-9b41-b3bd1d2c3250 | -3.82248 | -41.55743 | 2025-08-21 00:30:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| fa4996d2-defb-30b9-bffe-bf8270477f87 | -5.82335 | -51.69365 | 2025-08-21 00:30:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8e6dabb4-c8ac-3515-a760-4c35710a02b1 | -7.28831 | -49.39699 | 2025-08-21 00:30:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 16b98416-844b-343c-bf47-1943072afc03 | -5.87581 | -42.40276 | 2025-08-21 00:30:00 | TERRA_M-M | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 598a2a5e-fb21-3337-bbb7-275a3552868d | -6.01852 | -44.358 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fcdcbb4a-3110-3533-8d19-391b27da867a | -8.16158 | -47.35814 | 2025-08-21 00:30:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| cc0b9901-2912-377f-ad2d-89ed938f5fab | -7.38907 | -45.98353 | 2025-08-21 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1da91e27-712b-3911-b61f-275f64314208 | -5.95892 | -44.15747 | 2025-08-21 00:30:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 36fcec6b-7f33-3104-81ba-e67e756c0bd5 | -6.42405 | -44.67524 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d03eee11-95a5-34e7-95e5-e4057b28c98d | -5.10352 | -43.16553 | 2025-08-21 00:30:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ec85e4b2-733a-3fc2-8712-0e90b3e1582f | -6.41393 | -43.55827 | 2025-08-21 00:30:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 267b858e-29d0-3063-b07b-107b7885c478 | -7.66303 | -45.25427 | 2025-08-21 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ddf7ac92-43f9-3258-b871-5d8d6e5c633f | -7.64945 | -46.2627 | 2025-08-21 00:30:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6ae74946-e961-3ade-94ac-69de7f090359 | -7.66161 | -45.24437 | 2025-08-21 00:30:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6cd41fa9-da5a-3299-ba0f-8121cfd6be6d | -7.89007 | -46.73019 | 2025-08-21 00:30:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 9e552237-e847-3d93-aff5-702fdcd127fe | -7.7958 | -49.32726 | 2025-08-21 00:30:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 33aa98df-cae1-3ce7-bafd-afabede3f47c | -6.42089 | -44.67088 | 2025-08-21 00:30:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 85d7e5b1-aae1-3a30-b1d9-8634b6dff06a | -5.17011 | -37.98865 | 2025-08-21 00:30:00 | TERRA_M-M | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 55.4 |
| cffbc396-9bb9-3c04-b2e2-989c3b54dff6 | -4.71457 | -47.21706 | 2025-08-21 00:30:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1231e6b3-5384-34ed-8f1f-cd2b8caed799 | -5.93553 | -47.31657 | 2025-08-21 00:30:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d6c37dd7-d5b2-3fcf-8ae8-802232c60eeb | -6.26468 | -43.7243 | 2025-08-21 00:30:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README4.md)
