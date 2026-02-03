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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55840058-5841-3299-9147-fbc817c1b5dd | -4.39195 | -37.94717 | 2026-02-03 04:06:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 311a9b97-ee03-3936-9080-0454ed267fb7 | -3.27403 | -42.38112 | 2026-02-03 04:06:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c465b990-0446-311d-b40b-d35b648ae622 | -1.86618 | -46.28352 | 2026-02-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62ba5310-d56b-360d-a3e0-76994dc4a241 | -2.50887 | -47.81684 | 2026-02-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66f9dd53-3877-3db6-89bb-56561cb8f833 | -5.59254 | -40.58432 | 2026-02-03 04:06:00 | NPP-375D | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6b18fcfe-cb5c-3d69-bd63-b27d74f1fc86 | -3.25849 | -42.54934 | 2026-02-03 04:06:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af6c645f-fc79-3af4-944e-bafc7e67a6cf | -5.96328 | -43.53199 | 2026-02-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c0f2188-9bd8-3b14-b40f-0acc5d65665a | -6.06049 | -43.73749 | 2026-02-03 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad2aa201-55f8-3174-8460-357d1bc6dad2 | -3.25875 | -42.54863 | 2026-02-03 04:06:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1be20a6f-6089-35ac-bcff-8f840abef112 | -2.50848 | -47.81693 | 2026-02-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3749847b-0be6-3ecf-9111-bd94fffbe496 | -4.92512 | -44.04638 | 2026-02-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7df89be8-4c09-3d58-b22a-a3999a620972 | -3.82012 | -44.42606 | 2026-02-03 04:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| badb4676-aec6-3ec4-88a3-16133c1c4ca3 | -6.58784 | -37.49748 | 2026-02-03 04:06:00 | NPP-375D | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f6ce9712-cd33-37e4-8214-dbec77b3d73d | -5.793 | -43.7433 | 2026-02-03 04:06:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f31d3a1-5277-3633-b0c6-da61832e5252 | -5.98121 | -43.56209 | 2026-02-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 321e108d-4d9a-353c-a7b5-288bb5f8548b | -1.86538 | -46.28849 | 2026-02-03 04:06:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 292d885f-ba4d-3254-bc33-0221341e136a | -5.11381 | -40.50472 | 2026-02-03 04:06:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d269c66-e835-3e3d-b860-aa8b9a9dfe5e | -5.95883 | -43.53584 | 2026-02-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2daf691c-f32b-3cab-bec5-c35bd7a26d1d | -3.82049 | -44.42691 | 2026-02-03 04:06:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef891225-4c59-3439-b50d-7b9237c6fe1d | -4.92124 | -44.04575 | 2026-02-03 04:06:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4aa7705-4943-367e-92a8-59b4d9c6ccf3 | -5.96254 | -43.53644 | 2026-02-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d7aa746-8e9e-3264-92a2-327490b2225d | -3.26977 | -42.38466 | 2026-02-03 04:06:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ada305df-8f4a-333c-923f-884e1ff7499b | -4.98861 | -41.85091 | 2026-02-03 04:06:00 | NPP-375D | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0dd2cc8a-542b-34f1-b1a9-c1cf5688936c | -3.27043 | -42.38052 | 2026-02-03 04:06:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29d5ef74-c772-3083-af18-153a8fb9e32d | -5.83648 | -39.81374 | 2026-02-03 04:06:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d378eea-9c80-3df1-adf3-0c9cd5c82912 | -6.06122 | -43.73301 | 2026-02-03 04:06:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 664e47e5-21f9-33b5-b523-49dc1143765d | -6.0213 | -40.0135 | 2026-02-03 04:06:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ef166415-e0b2-3c9a-ac86-f7f98a9db713 | -3.84205 | -38.42855 | 2026-02-03 04:06:00 | NPP-375D | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 816a8076-ff32-3838-a2f2-3199d60ab893 | -5.01348 | -40.56082 | 2026-02-03 04:06:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ed90358b-1e1c-3c89-a747-d4546b5830da | -5.9775 | -43.56147 | 2026-02-03 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91e636fb-604a-3ec0-8652-98202d139996 | -4.56468 | -40.02494 | 2026-02-03 04:06:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 59d88568-7f40-332e-bae4-393a6837e7c7 | -3.01079 | -43.21217 | 2026-02-03 04:06:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| acdaaf72-d8f8-3110-9894-f4dd2e02f3f1 | -3.27338 | -42.38526 | 2026-02-03 04:06:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dce42a6-2013-3bf4-9ef0-52774524e248 | -6.58514 | -34.99545 | 2026-02-03 04:06:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 48611871-842c-32d3-8ada-805ec408a11d | -2.52755 | -47.80083 | 2026-02-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ccaf86cb-2c0d-3bb6-81ec-486030762e1f | -2.53273 | -47.80174 | 2026-02-03 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d63603c2-210c-3dc0-9868-1713ff35088d | -11.54807 | -37.84106 | 2026-02-03 04:08:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 965dc8b6-2917-3d0e-81bc-9e3609903b21 | -8.67535 | -36.27359 | 2026-02-03 04:08:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5c737368-52cc-3c0d-a68d-7c1188fcccf8 | -13.36172 | -39.90416 | 2026-02-03 04:08:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e93a392b-be55-3297-aca6-dfb67eba78ec | -10.11131 | -36.18542 | 2026-02-03 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d8102fdd-4a67-3802-aad9-904b435d51ea | -7.25781 | -43.93171 | 2026-02-03 04:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84acb91d-e228-35e1-b991-569454c2984e | -6.24391 | -42.79268 | 2026-02-03 04:08:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 27dec830-5732-38bb-aa18-1182c41b5030 | -13.38788 | -40.05375 | 2026-02-03 04:08:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4319b9a8-bf8f-3e6a-83e3-6eda56bc8a59 | -10.05123 | -36.52359 | 2026-02-03 04:08:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1292be76-c8ec-30f2-b01f-896842904a2f | -9.25898 | -35.66407 | 2026-02-03 04:08:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| befb3dc3-2dda-3da8-8009-a88d45a31803 | -9.42465 | -37.00072 | 2026-02-03 04:08:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 97016df8-3f8d-39a3-b3e3-0770fb54ec1c | -12.50797 | -41.59424 | 2026-02-03 04:08:00 | NPP-375D | PALMEIRAS | BAHIA | Brasil | 2923506 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1abee5da-9d43-3fdb-89ee-07cf8cd1c1d1 | -10.53531 | -36.89891 | 2026-02-03 04:08:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4cf80fe7-12c5-3ba8-a09f-a3ba5cbcd1b2 | -13.35888 | -39.89975 | 2026-02-03 04:08:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 69980934-b84e-3472-a0d2-dc7f2c2783d1 | -11.14225 | -38.36744 | 2026-02-03 04:08:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1f9ca29c-b7b9-3610-96c4-515a96552710 | -13.38665 | -41.3229 | 2026-02-03 04:08:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 86b93c2c-f0a0-3e2f-91c6-2d7abb6884b1 | -9.25493 | -35.6635 | 2026-02-03 04:08:00 | NPP-375D | SÃO LUÍS DO QUITUNDE | ALAGOAS | Brasil | 2708501 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e73d4289-3748-321f-a685-c7dec40b73d6 | -6.24588 | -42.79594 | 2026-02-03 04:08:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9054a4ae-c269-3b4d-8da3-4ada0336621b | -10.11455 | -36.1911 | 2026-02-03 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 640330a3-e7a7-3b5e-9bd9-aa67c662030d | -6.24326 | -42.79671 | 2026-02-03 04:08:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3f5adf58-ac37-363f-ad3f-a8a1c000a8f1 | -8.69379 | -35.11235 | 2026-02-03 04:08:00 | NPP-375D | RIO FORMOSO | PERNAMBUCO | Brasil | 2611903 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 96a53931-fc62-3576-8b41-4488649ebcb2 | -7.25757 | -43.92852 | 2026-02-03 04:08:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 768a688d-624b-3ee3-999e-7d4bdf6f3d4b | -9.99853 | -42.33236 | 2026-02-03 04:08:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| da79536c-cd6b-3592-a442-9e51aafd5f7a | -13.35831 | -39.9035 | 2026-02-03 04:08:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4df351fa-cbf9-333c-92f1-0dc6dacb19cb | -10.18078 | -39.05525 | 2026-02-03 04:08:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| db9a6d0a-aba6-3363-842b-46725e7a812b | -10.09618 | -36.29193 | 2026-02-03 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 966d8048-b390-3712-889a-f807e9e2d7d6 | -8.55431 | -35.70594 | 2026-02-03 04:08:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c6c59f6-dc78-3d4f-86c5-f4d96f212738 | -10.7211 | -40.33895 | 2026-02-03 04:08:00 | NPP-375D | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| e31ab4f5-cf6b-31c3-b4cc-f7cfa753db8d | -13.38846 | -40.05001 | 2026-02-03 04:08:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| e576ebfc-beaa-325c-9af5-72fb9ab53973 | -8.6727 | -36.27001 | 2026-02-03 04:08:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b35caf9-a7ff-3f5c-a617-9fb3e682e946 | -9.42478 | -37.0029 | 2026-02-03 04:08:00 | NPP-375D | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4b5e99ed-a6f0-3d08-a687-eaa5584f1f09 | -10.11059 | -36.19055 | 2026-02-03 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 609df557-d3b3-35ee-adb3-58f1a5b1d4e3 | -10.10011 | -36.29256 | 2026-02-03 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e5596821-daff-33c4-8ddc-543743bc5bab | -7.0864 | -40.0795 | 2026-02-03 04:08:00 | NPP-375D | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2d785f54-b226-3db2-8ed8-900c0840caa2 | -7.75361 | -35.31937 | 2026-02-03 04:08:00 | NPP-375D | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e0665980-fb42-374d-913d-756c12c5048d | -10.79943 | -44.48452 | 2026-02-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2026bc6d-2467-3438-bcf0-1d2b3bbefbda | -11.14603 | -42.24014 | 2026-02-03 04:08:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10ad6bc8-e48d-37da-861b-a3273f0f1bed | -8.67656 | -36.27063 | 2026-02-03 04:08:00 | NPP-375D | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 36541e64-f76e-3793-a6a8-2332de3558bb | -8.84052 | -35.72364 | 2026-02-03 04:08:00 | NPP-375D | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 49bff21a-2b96-3824-8005-15f47c714b32 | -10.8031 | -44.48516 | 2026-02-03 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bff96bcf-8817-3e18-a577-db1bf45a7fd2 | -10.18136 | -39.0515 | 2026-02-03 04:08:00 | NPP-375D | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 5fe599b3-d8f4-3f74-a8c0-906bc5cf7e7e | -17.66504 | -39.20551 | 2026-02-03 04:10:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4d95d4da-3429-394c-9e73-d149685c04d7 | -26.5106 | -52.19522 | 2026-02-03 04:14:00 | NPP-375D | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2bf7cdc5-03e8-355b-82b6-2a0e89796386 | -27.64719 | -51.03905 | 2026-02-03 04:14:00 | NPP-375D | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 770b0efb-b5c7-3e02-8bfc-75ffc66a4b0d | -27.09756 | -50.53033 | 2026-02-03 04:14:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 664a83b4-d5da-32ea-89d9-cb3e77045710 | -28.17495 | -50.76933 | 2026-02-03 04:14:00 | NPP-375D | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4a62b11a-34b8-384f-9cb1-a3db58bf8b8e | -27.01098 | -50.56648 | 2026-02-03 04:14:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9a946c94-66d0-3408-a437-fca11b29f9ab | -30.28849 | -50.924 | 2026-02-03 04:14:00 | NPP-375D | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| c0830cd5-3cb5-3309-b887-d6ef1bb0af41 | -28.17095 | -50.76853 | 2026-02-03 04:14:00 | NPP-375D | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6c0b821e-793a-30ca-9c08-34de1a68b212 | -27.65125 | -51.04002 | 2026-02-03 04:14:00 | NPP-375D | ANITA GARIBALDI | SANTA CATARINA | Brasil | 4201000 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5f0291f4-f0b3-324d-be05-a76ad5b342b4 | -27.01175 | -50.56265 | 2026-02-03 04:14:00 | NPP-375D | SANTA CECÍLIA | SANTA CATARINA | Brasil | 4215505 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ccfebe75-17a7-3823-b518-0eee7b544cdb | -2.85043 | -46.71872 | 2026-02-03 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f405d2be-9553-34ff-a694-fa68c5e4ccf9 | -3.03589 | -48.41908 | 2026-02-03 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9688065-8616-3f56-a224-9a3f6338979f | -1.19048 | -48.83292 | 2026-02-03 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89174d5-98a8-374b-872d-b5c212008a22 | -1.57844 | -53.99548 | 2026-02-03 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1bd3e98-094c-3722-8249-0621f6c23e7d | -2.23502 | -52.09681 | 2026-02-03 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f1dbdce-d23f-3edd-91a9-23546d7d1dda | -3.82088 | -44.42773 | 2026-02-03 04:25:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06385cfa-354d-36ff-9bb8-21cff58fd8fc | -2.50935 | -47.81701 | 2026-02-03 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 939e6706-506b-3132-a34b-9fdd641146dd | -2.07376 | -52.04173 | 2026-02-03 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82b9404c-f58a-3788-9abb-43f7affdf483 | -2.53928 | -51.92063 | 2026-02-03 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e435960-40d4-36f3-92b7-97d0b4fc9c6c | -1.86664 | -46.28391 | 2026-02-03 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33ba57dd-c447-3879-b17f-55d32e6ec2e3 | -2.25642 | -47.86102 | 2026-02-03 04:25:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91bbabcf-2c20-3c96-b924-3d72df9a5c17 | -3.1058 | -42.46259 | 2026-02-03 04:25:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8440a0d2-2597-348c-a561-4a1a632755a3 | -3.64515 | -40.63388 | 2026-02-03 04:25:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 091cf075-5d9a-3551-8e55-f9c461957e3e | -2.85377 | -46.71924 | 2026-02-03 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README3.md)
