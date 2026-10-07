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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c683b7-191d-38b2-a117-d0122479db03 | -6.202 | -40.80212 | 2026-10-07 16:03:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 56.0 |
| 5a7a615e-8aab-3a36-b453-2de6dc0ec548 | -3.95104 | -40.73705 | 2026-10-07 16:03:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 45a69055-b04a-3033-b705-8fba4e58b69e | -6.68555 | -44.94754 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d783e3c0-9191-34b1-91d2-06fde1e06321 | -5.95166 | -46.37681 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 7bd3c75e-7027-3254-8b8c-83c3d91b12f9 | -6.79802 | -41.24643 | 2026-10-07 16:03:00 | NOAA-21 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 28.4 |
| aacfa113-b9ec-3788-8fd9-82a6236197ec | -3.8948 | -44.11899 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 436e7a74-ab05-3184-82ed-bb7b4d6c1739 | -3.85848 | -42.23587 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 411cbfd1-d5a8-3f02-8bf8-7f77f68b8864 | -1.88198 | -45.42664 | 2026-10-07 16:03:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 190.5 |
| f5d84c42-f8f9-3533-9324-6f1ea4295b1a | -5.96967 | -43.5145 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 980c4af7-4d01-3ce4-9036-224dde06c782 | -7.56009 | -46.7177 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 77b9f95c-df49-313f-95e7-7b7e3dd55b8b | -6.93276 | -45.744 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 250d8304-8623-386b-bda2-aaba37c83480 | -6.99881 | -45.11739 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8250f7c4-542e-3a00-8e4a-8a17e660e244 | -3.90111 | -38.50059 | 2026-10-07 16:03:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 7232e594-cb7a-3b67-ba52-f1bdf3cece11 | -6.98264 | -40.03851 | 2026-10-07 16:03:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 77.7 |
| d80041b8-3583-3698-84b5-fc46e3df7843 | -6.44994 | -37.63199 | 2026-10-07 16:03:00 | NOAA-21 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 60991c7f-4f99-3ecb-98a4-c073ee2cd58a | -7.81205 | -44.59266 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| cfb2b474-eec6-3278-80f4-5433ef2a9872 | -5.71881 | -41.66611 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 84eec910-2cd3-3f8c-a572-698433b32a1e | -6.60106 | -37.88411 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 10.7 |
| a1fa7b6d-3a10-3ce1-bced-e63e51f38dda | -6.22094 | -44.83836 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 6df24ce9-c1a5-37d1-bbbb-3c29bb11fa5d | -8.10782 | -47.12429 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df8a858a-ba25-32a3-a1f2-85a39613506f | -7.30077 | -47.26669 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 240508b2-7b4e-3cbb-b86a-b3aee3eaa267 | -3.76894 | -41.78852 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| eeb02d50-5302-3e23-b5b5-e2a05f85ec37 | -6.98208 | -40.03474 | 2026-10-07 16:03:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 858c4975-616d-34fb-a7ff-4960ab8b2adb | -5.9514 | -43.03557 | 2026-10-07 16:03:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 014df5f9-5151-311d-bb94-a55a7f1235d3 | -5.09912 | -42.93084 | 2026-10-07 16:03:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7428f318-a95e-301f-bd60-a3e60893a47a | -5.94108 | -46.63391 | 2026-10-07 16:03:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 44ab30b3-439f-3572-af34-9727d19c77bb | -5.95032 | -46.40363 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3d7611f0-5286-3bcb-a506-6ce9d0bc99d8 | -8.28784 | -50.26932 | 2026-10-07 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a0ae8d37-65ba-3bf6-8eb0-1ab55221b4fa | -3.88648 | -44.12017 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 216e4055-fb09-3103-a1a7-c2cf90063a21 | -6.33083 | -43.83202 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f34dee5-1e74-3031-b648-53a8a15dc6e1 | -6.97808 | -40.0315 | 2026-10-07 16:03:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 6a5b4bbc-18d2-3fae-98e4-d25979dc0534 | -7.8068 | -45.49751 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2873d994-f4c7-3c22-b874-2545765993dc | -7.53004 | -45.8761 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 70b9f0cd-354a-3144-bc47-4ed52eaa12c2 | -6.92015 | -41.23817 | 2026-10-07 16:03:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 964ba026-dd96-37a9-9449-9ea4ff6729de | -3.55174 | -38.90788 | 2026-10-07 16:03:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 8be3e13b-7257-389e-9657-8e20b9aa1cdf | -5.95331 | -46.38849 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9016577b-faf4-36ab-a6ac-6cc48b8ef793 | -6.95039 | -45.30651 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1b69cbf4-c7c2-34a1-bfd0-8678f7964fdb | -5.99413 | -44.13131 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cc8df909-cd2e-3282-918f-5cf24455cd2b | -5.37854 | -45.92202 | 2026-10-07 16:03:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bd170b43-3689-3b12-9409-a0fe2768bffa | -3.76265 | -40.76558 | 2026-10-07 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c0c688bf-71cb-334b-8179-f64bd5583f91 | -6.60767 | -37.8831 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 3cf8f4d2-ab89-33e7-bd8e-0b5441a76887 | -7.37099 | -46.5498 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 46d863c2-283a-3dc9-9622-6590cdf24674 | -6.57475 | -36.24543 | 2026-10-07 16:03:00 | NOAA-21 | PICUÍ | PARAÍBA | Brasil | 2511400 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a9712a1c-ee4e-3955-b95e-b7c6197609ba | -2.05164 | -45.97254 | 2026-10-07 16:03:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7a3cbf2c-bec7-3a88-a99f-6ffb24ba5376 | -5.73101 | -41.74841 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b57a2bab-4d9c-3702-b23f-ddea3f4ba176 | -5.75214 | -45.17086 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 159bafa7-e2d5-31fb-9d5a-e790244f6567 | -5.03184 | -42.80305 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9f493e39-d013-32c8-8786-1da011cac68b | -7.48378 | -45.95492 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2eb82572-7057-3f62-92f5-c11c4c0ae06c | -3.26365 | -50.40462 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 5a887085-bdea-3cdb-bd91-a419d501517b | -5.95791 | -46.3849 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dadc05d2-d25a-3a46-b680-47dab356e147 | -3.80561 | -42.26131 | 2026-10-07 16:03:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 41a70cf6-0ae7-3c31-8aad-c2b589b69561 | -6.07312 | -44.11161 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ac00e92e-16f2-391a-8865-b83a1f5fee33 | -5.71146 | -37.71296 | 2026-10-07 16:03:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 836eca84-4312-370b-8bad-eb9109e2d9d4 | -5.8522 | -42.436 | 2026-10-07 16:03:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| e0f8e382-b4e1-3a46-bacd-9216e3fcc60e | -7.38755 | -45.61216 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d7c12c0b-f13f-3d5b-92bd-fdddf69bbd81 | -2.23465 | -51.92921 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 00061270-27f6-3a25-b7c6-dcd57f6c39b8 | -6.98686 | -43.21486 | 2026-10-07 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 7840eff0-6e1b-3353-badf-2a922f57fbff | -6.35609 | -42.55658 | 2026-10-07 16:03:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 1309f1d2-ab85-3c4c-a725-257131976888 | -5.24236 | -37.58113 | 2026-10-07 16:03:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 17.4 |
| d09ae387-081e-319c-ab7d-e29342eec8cf | -3.77418 | -41.87292 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.2 |
| e411a58f-f00a-3333-b755-b3736fb115a8 | -3.77615 | -41.78743 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 8da09630-8bbb-3e2d-be7c-5351442d6ec9 | -7.54205 | -46.04541 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 59d5bd72-8352-36e0-83d0-6b27ddb2a461 | -5.9809 | -40.94685 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| ca5e16f8-c0d0-30dd-8361-23f34349ce4e | -6.84468 | -41.76641 | 2026-10-07 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| c3156972-b1ac-36bf-b1a1-3a3610c8404e | -7.00017 | -45.12743 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 527eadc5-fd0b-3df0-b998-7d1f0cc598a1 | -4.05339 | -42.21462 | 2026-10-07 16:03:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| b70073c6-86e9-389a-8b2e-be5c3d8fc685 | -5.96377 | -46.39014 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 37a4405e-7bc8-3944-b0cd-51314ec56049 | -5.99351 | -44.1271 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 40892769-a707-368b-bdd8-83c1996cdcec | -7.86919 | -44.15613 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 866e3bfa-f93a-383a-a3a4-7e4973b3dae6 | -3.6089 | -50.20312 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 655acbb3-90e0-3e98-a420-1225a2a5b12c | -7.17592 | -44.3056 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82844c7b-ed89-3ee7-a3cb-1402e44c5431 | -3.73729 | -44.97583 | 2026-10-07 16:03:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 14fb8a6a-e155-3ac9-9175-76b6b8584336 | -3.44099 | -49.25764 | 2026-10-07 16:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2972ffc2-cc4e-323a-9b47-26ba08728d34 | -6.93879 | -45.29208 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7ec7c239-602a-3cf1-a7e1-2b333f814e75 | -6.6875 | -44.96158 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cacfee04-f82a-38e4-a5d3-b36a1d26f76e | -4.62458 | -43.50399 | 2026-10-07 16:03:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 531e753b-ced4-3261-89c3-16586361fbda | -4.31513 | -43.00466 | 2026-10-07 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7aa3ee70-7093-3929-813a-fdbfce83ae10 | -3.78814 | -50.74977 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 7737497e-9f6b-383b-acd1-9a8dcd70c43c | -7.1891 | -42.02811 | 2026-10-07 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| c8aa0278-d500-35c8-ab3c-8712a8831304 | -3.26119 | -50.40481 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f97134e8-dbea-36da-835c-4d449767d661 | -3.18323 | -50.55922 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| cedd1cd5-8c27-3c67-b789-d3ad3a441285 | -6.43601 | -44.80208 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 680d667b-c887-35ba-a63a-d2bc0bf608f2 | -7.40094 | -45.63822 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 8fffd9f6-3bb5-3080-8428-5eb31be7768b | -5.28124 | -42.74791 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 777890df-ea17-34fd-8ea9-80451f73afd6 | -4.08808 | -38.34454 | 2026-10-07 16:03:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1526c022-727f-3b8c-9185-5d507bc70c5e | -5.2059 | -48.34055 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 10c9cf38-61f6-3f46-b494-a858b40ea660 | -5.72236 | -41.74078 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 6f1616b7-2aa7-3092-8ac7-09809012de9d | -3.2864 | -42.26577 | 2026-10-07 16:03:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9e26b3e9-0f8b-3de4-aec6-4966d97e4483 | -7.7708 | -48.23973 | 2026-10-07 16:03:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 7fba70a3-bc16-3d04-bb07-ad6e099aa0e7 | -6.24186 | -44.34771 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7914d746-0002-3e79-abfc-2912fef7167e | -7.85976 | -44.15306 | 2026-10-07 16:03:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| c6824960-bc4a-3ec4-9665-378fad54d812 | -6.33506 | -43.83148 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4ecd1660-e1f5-3bbf-95e9-625b5fca98ae | -7.1745 | -47.8023 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| f889f0e0-0a51-32ba-b321-13cd5ac0f72b | -2.49015 | -49.41527 | 2026-10-07 16:03:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 459f84f6-a75c-3441-a038-77b9eb43980f | -3.50845 | -41.95219 | 2026-10-07 16:03:00 | NOAA-21 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 28d32545-e6fa-37bf-86dd-3bebf32da8fb | -3.73173 | -39.53469 | 2026-10-07 16:03:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 5319c144-7afe-350c-8189-94cef6f21275 | -5.2463 | -50.92156 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| d213319b-63dc-3818-b020-b3064b7e7049 | -3.81 | -51.04158 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 9b6eb8ba-b613-347b-a632-e8d3eaecbb14 | -5.9668 | -40.92446 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 71.6 |
| ba7326bb-b1d3-320b-bbc9-3807f8b4a487 | -7.18097 | -44.30938 | 2026-10-07 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |


[Clique aqui para ver as próximas entradas](README170.md)
