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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6fd8b385-f253-3d72-801a-f7dfebee49c4 | -9.49253 | -45.62789 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e06fb08-eef2-3143-bff8-2a134f1198ae | -5.95814 | -44.79414 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ffda06aa-03ee-39a9-baae-7f3824c7c66f | -14.04599 | -41.73972 | 2026-08-28 16:05:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 008771fb-7c30-3441-bd43-8a848f5e259c | -7.78934 | -38.30423 | 2026-08-28 16:05:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 576bf2a8-2cde-31eb-8515-662807b12566 | -7.28059 | -49.94764 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 9369f495-e0c3-3ce8-8f92-1f83e8471191 | -17.57465 | -46.50944 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08ef1123-ca48-35eb-ac3f-84b8cb9dff24 | -11.40709 | -40.30003 | 2026-08-28 16:05:00 | NOAA-20 | SERROLÂNDIA | BAHIA | Brasil | 2930600 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 46f1673a-ce7b-3f72-a409-50ff05ba2362 | -14.7969 | -42.8345 | 2026-08-28 16:05:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 58e45220-fbff-321a-8105-0edb91b88ba9 | -12.09155 | -47.17081 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| e256e3f8-46ef-374d-8fd8-264dc13d5c15 | -15.76412 | -42.45987 | 2026-08-28 16:05:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2311388f-0803-3190-9716-252b679e0d7a | -13.18009 | -43.47149 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e6e21b7-ce87-330f-aaee-e81b7754d57c | -19.18807 | -44.91367 | 2026-08-28 16:05:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a2195097-1de1-39e4-b042-2cb5540ba552 | -7.08249 | -42.80923 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| 109eb0da-5f15-3bb0-a990-1720de18ddc1 | -7.78131 | -46.14441 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 369d02b7-5b92-3717-bec8-99a86d7956e6 | -8.08184 | -45.83502 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 102e6147-fb38-312b-8cdf-fc60b090ceef | -15.47554 | -40.91762 | 2026-08-28 16:05:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 91cd8f2f-8327-3b63-a3f6-0fbd96eab186 | -6.92284 | -41.62778 | 2026-08-28 16:05:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 0e74cb87-1301-3482-ac3a-119d3feb070c | -7.12605 | -42.77098 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3e9f7cf3-da52-3ef4-a4ea-8e4485fcc220 | -15.71633 | -41.34423 | 2026-08-28 16:05:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 57adb9d3-3ae0-3f1f-8018-f2099d8a32bb | -14.18606 | -48.78003 | 2026-08-28 16:05:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 58006585-8354-3e92-8ef0-779cdf8e52f0 | -5.95767 | -44.80585 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| f694b3dc-ef92-3ccc-93e6-eb738c403528 | -13.28052 | -40.34326 | 2026-08-28 16:05:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f88c7677-d26a-3232-a091-e1516f723f3a | -8.67747 | -49.55093 | 2026-08-28 16:05:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| aa7a3779-3818-365f-bff3-95e6a92890ac | -7.67504 | -43.94457 | 2026-08-28 16:05:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 35f66b16-0c2e-3e38-9e86-101e590ee83a | -7.09611 | -43.70914 | 2026-08-28 16:05:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e9d5998-1331-3423-bad3-7db9ad1f875d | -13.65249 | -47.74377 | 2026-08-28 16:05:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 619c1e68-3334-3773-a048-8e0fc358318a | -14.90956 | -40.94417 | 2026-08-28 16:05:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3ee1ae0c-8057-3304-9db8-f7b845627b66 | -16.41292 | -43.05516 | 2026-08-28 16:05:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8bd1462a-ea62-3e8e-98f5-6375c8074711 | -7.28061 | -49.95404 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 1f121f81-4b26-3790-a2b3-257068f7d8c7 | -7.09058 | -42.21044 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| 94c072e7-22ab-3943-959f-32d2e8251577 | -5.33541 | -37.03545 | 2026-08-28 16:05:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ba712dca-5c36-3748-9bfb-0546282d0624 | -7.11048 | -42.83374 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be8128d4-016f-3a2c-a997-6ea9d0d9633c | -9.49332 | -45.63375 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 531ee4e9-78db-347d-94f6-06604c75d10b | -8.09447 | -47.58109 | 2026-08-28 16:05:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5764d1ea-a8a0-3e54-889f-d9592dccd4d3 | -7.12429 | -43.16843 | 2026-08-28 16:05:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| f05478dd-8c23-3c56-a446-7c9c4b1407cd | -8.02441 | -38.78614 | 2026-08-28 16:05:00 | NOAA-20 | MIRANDIBA | PERNAMBUCO | Brasil | 2609303 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| cc6720ca-d54b-3a68-84f1-02729649cb8f | -14.31058 | -41.44844 | 2026-08-28 16:05:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 67671a13-0607-3106-b4a1-e56459d4799e | -9.48866 | -45.63721 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 90a6549b-9c9f-330a-8b24-77611c3ae236 | -12.78118 | -45.95058 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 573a555f-fa3a-3326-aa99-5e947d13f6bc | -14.20934 | -45.27611 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b47448c-b981-3965-9517-ad2dbfd3bef4 | -8.17281 | -46.1633 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 27991390-270e-39ab-bfff-e6cc1233f7cc | -8.16474 | -46.18051 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 731b53c4-d5bd-3acf-8d1a-8bbce07bd99f | -13.34613 | -46.90617 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 41fec6b6-8b6c-359c-9132-8ad7f4547d60 | -15.75319 | -42.59455 | 2026-08-28 16:05:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d468d128-5a76-3938-ae69-a369c3f63936 | -18.32269 | -43.96712 | 2026-08-28 16:05:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02409f8d-4cdf-3d5b-9e81-8f2ae53bf6a9 | -17.9084 | -39.39427 | 2026-08-28 16:05:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| fa8ebbf3-f9d1-30b7-8b6f-59dc84b41557 | -7.58126 | -44.01244 | 2026-08-28 16:05:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1fca8b9f-e966-3f59-a38f-8349c0ab02ae | -19.59014 | -46.53532 | 2026-08-28 16:05:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 11f8f1fb-9271-3288-94bf-f5f301fb2c8a | -14.49498 | -49.11343 | 2026-08-28 16:05:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4aa1f30b-4400-3050-be51-330588c0ef90 | -6.40342 | -44.97206 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 87e6e938-2bc6-35fe-a59e-90d07d177e59 | -7.12309 | -42.75036 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d536f035-24f1-35a9-9f3f-703162a56f87 | -7.28628 | -44.56385 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3441ad63-3ab6-34ab-8b54-ab5c4e3c23b9 | -14.18956 | -41.24631 | 2026-08-28 16:05:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0ef62180-2c1a-3e9d-8d1e-4abac93ae30b | -7.60519 | -45.82689 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e9d54402-d4ed-33e4-9a74-ba740721710b | -6.55756 | -45.3274 | 2026-08-28 16:05:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5b930fb7-b4b7-3cb5-88ad-03474d412d19 | -8.06843 | -45.84885 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 33ab66d6-4fea-3b23-907a-4e26b6ca43d0 | -8.08683 | -45.83429 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d34c1146-50a5-3296-b97c-69861f19c164 | -14.49836 | -40.34055 | 2026-08-28 16:05:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| acfaa9eb-6cd4-3ae1-b4ef-88371f1fad83 | -9.15887 | -49.97196 | 2026-08-28 16:05:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| c67e8db6-a6a4-323b-865b-42024fb9db10 | -11.94508 | -41.32651 | 2026-08-28 16:05:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 65c1a43d-c5f3-3a8c-ad06-95d6a9a7e41a | -7.98704 | -45.50112 | 2026-08-28 16:05:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| dd15faa9-0651-3773-9d1b-21f2b96e3e45 | -16.3096 | -39.27393 | 2026-08-28 16:05:00 | NOAA-20 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 77dc9bb6-7d1e-3126-9752-5e33ba685cdc | -7.61184 | -45.82909 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 51499cab-7709-32d9-a90a-bba0b287375d | -6.77769 | -39.27095 | 2026-08-28 16:05:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d66711f-cfc5-39bf-919d-2c854644caa0 | -7.08913 | -42.21378 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 0b057c85-8734-3366-b399-70f97a36d75e | -14.20525 | -45.28669 | 2026-08-28 16:05:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1fe4d0ef-75be-3688-b6ca-9e5c04e3290b | -15.38954 | -40.86578 | 2026-08-28 16:05:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c75c5005-79ca-321b-b21b-41d407faa9ab | -17.13852 | -44.77146 | 2026-08-28 16:05:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1a12a3a-28ae-345c-a8ea-820974bacffb | -17.57818 | -46.50835 | 2026-08-28 16:05:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1159fc71-6b33-392a-aa47-9fda3080b1e1 | -5.95238 | -44.7857 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 33cfb0fd-fa38-30a1-84e2-3876ce7e4766 | -13.3125 | -46.91911 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 33788f4d-546d-39b5-b7b0-0b5afa0421e2 | -14.21048 | -45.28591 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bd2fc18c-f1e0-3c91-b8a1-489d188eaafa | -13.60764 | -45.78175 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 76bcb53d-d2a4-3f27-99c0-7c413663b5f6 | -6.50134 | -38.31281 | 2026-08-28 16:05:00 | NOAA-20 | UIRAÚNA | PARAÍBA | Brasil | 2516904 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c0611a8d-e13f-34a8-934b-d51d83311bba | -7.27636 | -49.86198 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| c410302c-193b-3c13-afad-ca72430fd012 | -13.59076 | -45.77728 | 2026-08-28 16:05:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| fe9c0ddc-b0ab-3429-8c74-bf3552183710 | -14.21457 | -45.27535 | 2026-08-28 16:05:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da18dd3b-b1ec-329d-b71b-0cf6e2e7981e | -7.27265 | -49.84475 | 2026-08-28 16:05:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| cb3ae981-f899-35f2-8e94-d4a2e126e343 | -7.10532 | -42.20333 | 2026-08-28 16:05:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 7c634fa6-f7fb-3277-b72b-0c589837b374 | -16.41233 | -43.05024 | 2026-08-28 16:05:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4621b9e2-36c4-3dea-a333-0ba4fd328a40 | -8.96767 | -42.69879 | 2026-08-28 16:05:00 | NOAA-20 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5bf60c5b-1f37-3633-97a1-471a2223f501 | -6.93945 | -45.68589 | 2026-08-28 16:05:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a99597b0-b111-371c-80e8-a330a4c079ae | -5.33931 | -37.0385 | 2026-08-28 16:05:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0d4246ea-9ad7-3e26-9403-ab01617fa77b | -8.07226 | -45.83946 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8cc86b97-e47c-361d-8755-81617473572a | -15.39611 | -44.30738 | 2026-08-28 16:05:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 25.9 |
| dcbe3271-52ea-305f-ac11-c75759dec4bf | -13.32591 | -46.93423 | 2026-08-28 16:05:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e75e2b8-ef56-3661-b8c1-fa654ab73841 | -7.21188 | -42.75778 | 2026-08-28 16:05:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| f40884f3-a3fb-3ac0-a4cf-6225b3c2e8f1 | -8.07493 | -45.85941 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 709e2719-1cc7-31b7-b2a5-23e3ee421d88 | -16.51927 | -47.73253 | 2026-08-28 16:05:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 819b9a32-3a64-3ea3-bc98-1c57aa0b8b51 | -13.64642 | -47.7448 | 2026-08-28 16:05:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d3350f55-a7d3-3369-bc71-8527a1851632 | -17.07814 | -47.18525 | 2026-08-28 16:05:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 98a72c3d-5f76-37c8-9068-fff5dc65768f | -13.1805 | -43.47365 | 2026-08-28 16:05:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f0507240-7e92-3f6c-b1c7-e1e3c711624f | -8.51011 | -39.58561 | 2026-08-28 16:05:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 3332581b-9432-3830-b81f-7487be804227 | -7.74138 | -44.74027 | 2026-08-28 16:05:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 459b693d-7b10-38b5-864d-54dcc2ea4202 | -14.17892 | -48.77507 | 2026-08-28 16:05:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 17bd8ce4-6bd3-34e7-b122-c1df4cafa651 | -5.95424 | -44.79917 | 2026-08-28 16:05:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ce5008be-82b3-3c8d-9961-a87cb611efe8 | -12.78078 | -45.94722 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3f06154c-f1b0-3e24-a0b0-41b2837cd365 | -8.08801 | -45.84301 | 2026-08-28 16:05:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 24201929-7946-3568-a95a-d0e8dbb2ef40 | -9.50191 | -45.65954 | 2026-08-28 16:05:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2d82c4b4-79cc-3395-89ad-a4ca63b62154 | -12.78575 | -45.94314 | 2026-08-28 16:05:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |


[Clique aqui para ver as próximas entradas](README91.md)
