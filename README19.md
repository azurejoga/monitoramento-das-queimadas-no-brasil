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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88dbcaea-0119-3367-8ec7-3f5387ecc68c | -11.1443 | -44.4865 | 2026-08-25 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 208.8 |
| 1692087c-f6f9-398d-96f5-e7bb282bfc9a | -7.0057 | -59.2575 | 2026-08-25 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 037c4f6b-6dd0-3a61-82be-cc1d6f617ad3 | -11.1447 | -44.4632 | 2026-08-25 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 4461949d-56f0-320f-8014-6f49f7968e66 | -3.5406 | -48.1889 | 2026-08-25 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 147.2 |
| 33159df2-6039-351a-bea1-25accafb4ae5 | -3.5222 | -48.168 | 2026-08-25 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 88648540-b326-3a11-b1ca-7d4740773663 | -11.1252 | -44.4892 | 2026-08-25 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 0fa882bb-95d6-3b8f-9888-91a1390a362b | -7.2901 | -45.3683 | 2026-08-25 03:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ca844ec7-ebf5-379d-840c-886946c14739 | -6.9872 | -59.2582 | 2026-08-25 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 7b768cd5-f87c-32a3-81fa-244588ebcf29 | -3.5407 | -48.1673 | 2026-08-25 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 4448f07c-ce3f-3b6a-ac30-594697ec6e8f | -6.6226 | -58.4995 | 2026-08-25 03:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| cdb81203-9f0b-36c2-9e15-6ad8ddfc45b5 | -3.5407 | -48.1673 | 2026-08-25 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 20f65d1b-8c8c-3ce7-8cbd-ff68057f0ef4 | -7.2903 | -45.3456 | 2026-08-25 04:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 9cbbfcaa-e5aa-3208-94c0-3bde84a14be0 | -3.5221 | -48.1896 | 2026-08-25 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| d2937469-6f9a-3b1c-b623-c9f0a62b3a35 | -6.9872 | -59.2582 | 2026-08-25 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.0 |
| d786b950-07f3-352c-a470-3715b97bc8c0 | -6.641 | -58.4987 | 2026-08-25 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 27cf1e3d-daa6-3d56-b2f8-2db51adeed04 | -6.9873 | -59.2389 | 2026-08-25 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 83975b0c-99a9-3585-80a4-0b5dcea5736e | -11.1252 | -44.4892 | 2026-08-25 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 67fca7e1-e2bc-3620-8436-dbf55d14ba80 | -3.5406 | -48.1889 | 2026-08-25 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 60422499-8a69-33a6-b35e-a9928fceeb68 | -10.3727 | -45.0537 | 2026-08-25 04:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 0cd2e358-3be1-327a-a3c9-677ca57d0d3c | -7.0057 | -59.2575 | 2026-08-25 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 229.2 |
| 0ac54f1c-8110-300b-9389-d1e0b142eff6 | -3.5222 | -48.168 | 2026-08-25 04:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 3f380044-b160-32fc-b558-ac20e774d0d3 | -7.2901 | -45.3683 | 2026-08-25 04:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2b5afa69-ca95-3467-9da8-31bf4bf7db8d | -11.1447 | -44.4632 | 2026-08-25 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 223.7 |
| f2315a86-768f-3098-b3ed-c0f511f111a2 | -7.0058 | -59.2382 | 2026-08-25 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 201.9 |
| 4aab587d-81f0-3684-92ba-9e2ba34e5367 | -11.1256 | -44.4659 | 2026-08-25 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d39d839a-15fe-3f7d-9c72-d130347d280c | -11.1443 | -44.4865 | 2026-08-25 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 176.0 |
| 9c6fd9d9-6d32-3df4-9a88-79f4673d0cd7 | -6.6226 | -58.4995 | 2026-08-25 04:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| ba1966c9-4dff-3152-834d-03e7df8dd0c2 | -8.05187 | -42.0471 | 2026-08-25 04:06:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ab4592ae-6d69-336e-940f-9ffe9c332e7e | -5.39302 | -43.60828 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acd57122-b5a4-3d16-afcc-d383a218ca18 | -4.76729 | -41.799 | 2026-08-25 04:06:00 | NPP-375D | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| edb758ad-82e5-3e4b-a03f-1fea102a4177 | -6.29785 | -43.79909 | 2026-08-25 04:06:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d48ca985-8401-3ae8-b48b-ce5b9e961d54 | -7.06151 | -42.93171 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc1f4921-aa96-3792-aacc-a8cafd524443 | -7.42747 | -43.11739 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 393fe14a-2ed8-37b3-a012-17d34784455a | -7.14388 | -42.75796 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2fa86b01-06f1-3642-8dab-79aad7bbaccf | -7.43711 | -43.08398 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1ece2db2-7fc7-3fc0-8b65-8011e2be69ff | -6.45969 | -41.55453 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fbd70f5-b9f4-3f59-b171-9ff4b85abe0a | -7.48922 | -44.93932 | 2026-08-25 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5623c18d-2943-37a8-a53d-400962f31004 | -7.19813 | -42.76218 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 93862afe-8c0c-3aa3-a690-5e1e2b1dd812 | -6.94266 | -42.68998 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3cf084fa-69c4-3d2f-99aa-04f8cf262b6f | -7.13068 | -42.78937 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 05fbb79f-dd6c-376f-8fe8-143bcb140ffa | -7.43218 | -43.11314 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 64f1d998-520c-362d-89ca-022a0a452daa | -7.25558 | -45.85464 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4fdfa77c-0fb3-3b2d-8d81-cccb32003790 | -4.46542 | -38.50868 | 2026-08-25 04:06:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ba3b1a52-81be-315a-a923-14cd9d8faed8 | -3.3051 | -43.40628 | 2026-08-25 04:06:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4a1ef3d-6398-3640-92ca-76bfde6d279d | -7.15388 | -42.74524 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4cd7acb-a7b0-3cb8-ad35-05ae8eab7a25 | -3.9697 | -41.52089 | 2026-08-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7f1e4bda-7fe2-378f-bbc3-7f2cee22f302 | -6.41041 | -51.71441 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a78ef1d-ee86-3ca1-a0bf-d75bad325119 | -3.0448 | -48.98334 | 2026-08-25 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72a5cd0b-1e39-394b-b3f8-c6aab10a4ff4 | -7.15241 | -43.43847 | 2026-08-25 04:06:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 373c22f9-8063-324d-a0b8-35aa6341f7f6 | -5.29587 | -42.71001 | 2026-08-25 04:06:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 876e0c81-29e7-34ed-a866-607c90cf108f | -7.28444 | -44.0818 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 80bcadfc-cef5-34dd-ba36-88b01bb027e0 | -7.4469 | -43.12066 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bceab586-0412-3c7a-b6ca-3f404d6e64e3 | -5.73587 | -43.27904 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9e32ee8-cb21-3e0c-978c-53f44b2a2b51 | -5.61196 | -47.00522 | 2026-08-25 04:06:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f3761ee-08b2-386b-9217-70990894d241 | -6.41733 | -43.07286 | 2026-08-25 04:06:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7bf3c197-6ee1-3559-b8f3-ed14527d4294 | -5.65456 | -43.38894 | 2026-08-25 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8ffd909-be1a-3327-970d-24df166df682 | -3.97342 | -41.52148 | 2026-08-25 04:06:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 53b84715-0bc7-3ed1-9c21-68f52438feb0 | -7.25377 | -45.85234 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 80bdf2f4-2bb5-3762-92af-58f4abdabe07 | -7.44631 | -43.10045 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a729178c-2014-360d-875a-3198ecaa9162 | -2.60577 | -47.35545 | 2026-08-25 04:06:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c86458a-2532-3aa6-bcc1-36383821b0fc | -3.8947 | -38.37519 | 2026-08-25 04:06:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 41935c20-1687-3eec-86b1-5a84605ad37e | -5.29505 | -42.71152 | 2026-08-25 04:06:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1abb1077-52cf-3d47-9f27-73689bd6e91b | -7.28043 | -45.36568 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 813ca6fc-9d4a-3a96-ace3-90213c58e8bc | -7.14006 | -42.75729 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1b2e7fed-84d8-32cb-8d09-4f4dd1bef375 | -6.97445 | -42.08102 | 2026-08-25 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 27a35e09-1deb-3e79-83fd-0da1678b1567 | -6.97748 | -34.96238 | 2026-08-25 04:06:00 | NPP-375D | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5e3050a5-09c7-36ac-95d6-2a70fc2c150c | -1.59315 | -47.3621 | 2026-08-25 04:06:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43bac4b0-0ee2-30ae-871a-24454ae72f8c | -7.26112 | -45.8506 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 291c562c-354c-322e-96bd-a8ae38d6ee14 | -5.91971 | -43.64182 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| be88ed83-4cf4-3107-99e3-dbd7ca6be266 | -7.31543 | -42.97666 | 2026-08-25 04:06:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 84d7202f-e1a6-352b-80f4-5b5c24482be7 | -4.43747 | -43.40697 | 2026-08-25 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35cc8636-8505-3829-ba09-7cd53033e5c3 | -8.0555 | -42.04773 | 2026-08-25 04:06:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7f6cc5d6-ccfc-3e67-9cb7-85970bf66d0f | -6.45113 | -41.56163 | 2026-08-25 04:06:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8120bed8-f200-35e1-aa36-14c737525cf4 | -6.97228 | -42.09418 | 2026-08-25 04:06:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 250e68d6-ed8b-3aeb-bd0d-76e055815463 | -7.26024 | -45.85552 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 60fe661f-d4b6-3c60-99cf-b61f20f79829 | -7.48233 | -44.46675 | 2026-08-25 04:06:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15ce4098-399b-3d89-8bbd-2bce47544af2 | -2.89385 | -48.80434 | 2026-08-25 04:06:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3c9478a8-3224-3b14-86ce-750060d62405 | -7.42664 | -43.12228 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5de6b726-811e-34d2-81c8-12a5e514f5c0 | -7.28121 | -45.36113 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f81b016b-986a-3566-a4df-d1616b34b796 | -7.27264 | -44.07601 | 2026-08-25 04:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba7be18c-5f0c-3377-a8e5-9cb4a4a9e40a | -5.89143 | -46.91492 | 2026-08-25 04:06:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71c108df-9286-32a0-aa6b-564dd82347d7 | -7.4369 | -43.10887 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 67a973ed-5419-37b1-a3ab-170d60324396 | -3.01353 | -51.05268 | 2026-08-25 04:06:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47f9f9c4-9e3e-3e94-92cf-1e680d2a2c14 | -7.28201 | -45.35652 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d959562c-13b4-3487-9fe7-9d8fdbb72674 | -7.25293 | -45.85725 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0a2cbcfc-a5d7-3ace-b19c-795e523f2f31 | -7.63708 | -42.72615 | 2026-08-25 04:06:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bcb4cf85-a285-300d-ab68-beaa029fdb10 | -7.15468 | -42.74054 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7395ee82-4c1e-30d0-83a1-13b847b1d486 | -7.28922 | -44.07874 | 2026-08-25 04:06:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b6580e5-9a73-3a6b-b373-a29681592700 | -2.95338 | -40.35931 | 2026-08-25 04:06:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 67e101a8-4c92-3d60-94fc-b43fabd94d8b | -7.28029 | -44.08112 | 2026-08-25 04:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f38329f-6aaf-346a-823f-7bbd3ebe1a33 | -7.13991 | -42.78136 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e6a29903-1dac-3d10-94e3-920db6e21752 | -6.40347 | -51.71344 | 2026-08-25 04:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a10e2494-d78f-37df-897b-c17a5ea1501e | -7.25005 | -45.85866 | 2026-08-25 04:06:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 26081901-3c01-376d-981b-a1748f4906cc | -7.29474 | -45.36356 | 2026-08-25 04:06:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6a77dc2b-a694-3a43-8129-144dc85fbb1d | -6.65296 | -43.90459 | 2026-08-25 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea199913-4114-3f2e-9951-deebaae17fc8 | -6.65232 | -43.90831 | 2026-08-25 04:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbef0ea5-ad1e-38cc-b5f4-3b7290fd5156 | -7.44219 | -43.12492 | 2026-08-25 04:06:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7695df87-e0ff-38d0-94d0-c3ed0d9e7640 | -7.14467 | -42.75331 | 2026-08-25 04:06:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 157653d2-d9df-3d27-8386-f4685f35ec21 | -5.77523 | -45.79414 | 2026-08-25 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c0dd3ca-7c4e-3105-9748-2d846646a51c | -7.25468 | -45.37989 | 2026-08-25 04:06:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README20.md)
