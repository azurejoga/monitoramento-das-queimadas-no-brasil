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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 701fb559-01aa-3783-b182-bdb5eb927a9c | -11.0802 | -54.0302 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 330.4 |
| 43056c54-9780-3618-8020-ffa565430969 | -9.6665 | -54.3332 | 2026-09-20 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 796e39a2-aaf8-323e-b62b-3adaf4185a95 | -10.2748 | -50.5592 | 2026-09-20 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 118.7 |
| d753d2b9-fa29-330b-a1e0-f39cac39aa1f | -3.6076 | -59.0769 | 2026-09-20 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d4c61194-d2c7-3302-8609-1d4b08b1813d | -10.2784 | -50.2818 | 2026-09-20 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 18e2fd53-d203-3b72-8f6e-267fd0884c86 | -1.1345 | -49.2123 | 2026-09-20 15:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| b4c94bde-12bd-3282-9bc9-1dc60b359c02 | -10.1145 | -48.4205 | 2026-09-20 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 452cc918-cd41-32c9-b39c-ad5d2f47f3b2 | -2.8974 | -57.8181 | 2026-09-20 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bc4803cb-253c-32c4-b3f9-5e1bf3a71396 | -6.7666 | -59.1129 | 2026-09-20 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.0 |
| c567b0c3-edce-3e8d-bce7-5c174a72dd94 | -11.0989 | -54.049 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 6e4cab97-4629-39e7-a70d-6487b5e4a37e | -3.3494 | -59.8097 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5310b65c-5924-3967-8b57-7d15f9a4065d | -11.118 | -54.0268 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 278.5 |
| 6f6b3e14-b478-38be-ad48-ab774a64d84c | -6.3655 | -58.316 | 2026-09-20 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 0b5019c6-d440-33f3-9862-8da64f26e818 | -9.6853 | -54.3318 | 2026-09-20 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e193b218-6a34-3e46-9489-1df46d470fe8 | -1.7499 | -54.9516 | 2026-09-20 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2c4c3391-01bd-3666-bdfe-8bc54dda4c57 | -10.5535 | -57.4567 | 2026-09-20 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0323f194-ef38-3e3f-b482-cfb2ecd7ee14 | -9.6855 | -54.3114 | 2026-09-20 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 29252eb7-73dd-3766-8a76-ac21b50f08be | -5.9423 | -52.2272 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8dc8c2de-b417-3775-8031-64da7693ec68 | -4.5045 | -54.9646 | 2026-09-20 15:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| ae44a861-4a23-3b67-8818-84a5f499951d | -10.8569 | -57.1568 | 2026-09-20 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 67b477c5-85e6-3440-a789-4fd2ccfdecca | -7.5703 | -57.6962 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 5e644a75-6bcd-37dd-8f17-757b8e82199c | -3.4003 | -61.2898 | 2026-09-20 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 8bad57f4-96ca-344a-bf7a-ead2ccbac02d | -10.7466 | -50.5959 | 2026-09-20 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| cf899ab8-f473-3860-90da-ebb3fef4ff01 | -11.4541 | -45.3662 | 2026-09-20 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| e12d59c3-1d02-3e12-b24b-be6057f1eff5 | -11.3793 | -51.3989 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 315.5 |
| 5158848c-4b38-39d0-b09c-16ecf0258207 | -9.0239 | -48.1622 | 2026-09-20 15:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a815dafa-779d-35c4-9825-266c46fd23e0 | -3.0535 | -61.2578 | 2026-09-20 15:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8ff121d8-72a3-3648-bbbb-7c5d89ed7070 | -3.3311 | -59.8101 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4fd97eba-f3e7-39c9-9108-d94e5f46e3f8 | -11.8947 | -49.9312 | 2026-09-20 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| b0743375-4c8c-3bdb-830b-bfadb7a5ec0f | -10.2787 | -50.2605 | 2026-09-20 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 944aea7e-d649-3d19-8a0c-9319f91f4472 | -6.4587 | -58.1373 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 5344abaf-69ee-3cd5-87bf-105ca06fd15c | -11.3796 | -51.3777 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 2d65df6d-5c00-3798-954a-809970afcbc5 | -9.5515 | -45.4067 | 2026-09-20 15:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1af2261b-ccd8-336b-95e0-f295b44a1985 | -3.2955 | -59.4284 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| fee274ce-4516-3eb5-bd56-4257f6dc6361 | -10.2598 | -50.2624 | 2026-09-20 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 23c2e798-0500-3db4-a414-6b5f5782d626 | -8.1686 | -54.7634 | 2026-09-20 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 219.5 |
| a912d8cd-acb0-3ded-b297-110e45018f93 | -6.4302 | -59.9724 | 2026-09-20 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.4 |
| 5b109842-f501-3c83-8bac-c6510c6cc8b9 | -6.7863 | -58.8995 | 2026-09-20 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e8bc5514-472e-3ee8-952f-1edf9b45a26d | -10.8668 | -56.2176 | 2026-09-20 15:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8589cb49-04f6-32f8-a8d3-9b75534f4209 | -7.3289 | -55.2155 | 2026-09-20 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 1b3ca54d-dc8d-3e0c-aa9b-0221969e148e | -10.7466 | -50.5959 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 5801b88e-7e4e-3a8e-9c1f-87a5844d78d5 | -5.7431 | -57.5814 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e762c99c-f7ad-346e-a16c-d0ff59e41403 | -5.9814 | -57.7867 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 58f17ef7-9ec3-3f7f-90b3-27cc6d04c95f | -11.4736 | -45.3405 | 2026-09-20 15:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 452.7 |
| ae164d52-013c-3a8b-8b60-f6740e10b996 | -6.0196 | -51.7893 | 2026-09-20 15:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| d308d59d-7e27-315a-bff7-c6a4d4a73447 | -3.3494 | -59.8097 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| ac2123d8-6ff2-3b8e-a212-13c18cc8213d | -9.6855 | -54.3114 | 2026-09-20 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 03f82adb-1b6d-37a1-b493-6234b67613fc | -6.4028 | -55.2442 | 2026-09-20 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 057044a7-e597-33cb-a1bc-bcd4de606519 | -10.7609 | -50.9345 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| ecab93c7-7c9d-3c99-b333-f47a61e92c28 | -10.8921 | -53.9857 | 2026-09-20 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.4 |
| e1ab89cb-9050-3902-9c2c-0abca54aa30c | -2.8779 | -58.2828 | 2026-09-20 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 90993ad0-b609-3aa3-8a7e-e471f833c7ad | -3.7347 | -59.4002 | 2026-09-20 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| c7a2cded-e1ce-382a-9b93-031836cd5020 | -6.8433 | -55.7602 | 2026-09-20 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c927bc0e-5f93-37fd-b73e-15131bc4f095 | -10.6143 | -50.5884 | 2026-09-20 15:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a660d3b2-5cdf-3371-aed5-3fc7c9c967da | -6.1109 | -57.684 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ae475c35-31e0-32c9-b3ba-a077e06a6b77 | -11.0223 | -54.1379 | 2026-09-20 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 37a596e8-9057-3756-9e67-9cfc36639328 | -2.9157 | -57.7983 | 2026-09-20 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| b7cdc815-caf4-3870-a81e-d412ce43d178 | -6.3471 | -58.2973 | 2026-09-20 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b2ee18c4-91d3-358a-b402-475f67de631e | -10.0956 | -48.4226 | 2026-09-20 15:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 34aa3d11-9eae-3691-81b5-8f57c593391f | -9.2865 | -48.2453 | 2026-09-20 15:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| afe8a522-2b44-36aa-a83f-321fe27bad83 | -6.0928 | -57.6262 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| ea515056-f4a5-3392-87a5-347115ecbb60 | -2.7713 | -57.0229 | 2026-09-20 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8be61ec7-6d2b-3dcf-9af9-30c0ff330dfb | -2.8961 | -58.3018 | 2026-09-20 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ee9d7995-baf8-38f5-aaff-21858eea41f6 | -6.0925 | -57.6847 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 646d8ccd-4742-3147-9125-a6e98736a22c | -3.3504 | -59.4465 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 771aa51e-114d-37af-a61e-e85f07baaf2e | -10.8856 | -56.2161 | 2026-09-20 15:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 081bbe3c-5cfd-3d9b-aaee-502646456298 | -10.1145 | -48.4205 | 2026-09-20 15:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 71.0 |
| e4265637-14b1-3eab-9729-9bd77f1ea40d | -3.5893 | -59.0773 | 2026-09-20 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| b530cb0f-3af6-3809-ba3e-09f1adb170cc | -1.7316 | -54.9518 | 2026-09-20 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 39648c94-0074-320f-931a-5839b16416d9 | -10.7463 | -50.6172 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.5 |
| b39baa6c-1e34-33bf-bbe6-74392a90c693 | -10.2748 | -50.5592 | 2026-09-20 15:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| fc542853-ecac-3f69-8649-9f2db7d545c8 | -11.1225 | -49.4601 | 2026-09-20 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 40d56c5f-744f-337d-9f83-f416bea40151 | -3.3311 | -59.8101 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 9334b19d-c732-3dfa-8e0b-737391371e65 | -3.1079 | -61.408 | 2026-09-20 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| d9f93115-b59d-3bd7-9e91-13b31c751534 | -11.379 | -51.42 | 2026-09-20 15:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 189.1 |
| d777c960-9a45-3380-afb1-713a58c11fdb | -1.75 | -54.9317 | 2026-09-20 15:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| cc258bc9-5cba-3cfa-8f06-0c52c92043ec | -6.3197 | -59.9764 | 2026-09-20 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 593dece2-e042-37d3-83a7-8aa34a47e9f9 | -3.5356 | -58.6939 | 2026-09-20 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fa377251-0dd6-3c9e-bebd-8789474f0b4b | -3.6763 | -60.6029 | 2026-09-20 15:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| ad2a0a2f-612c-3c2b-9363-36e4f2e07539 | -9.6853 | -54.3318 | 2026-09-20 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b57ad521-46d0-373b-b8c4-b4260904e612 | -3.7347 | -59.4194 | 2026-09-20 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f4bddeff-7a00-3449-971c-7f1e20601a7c | -10.8672 | -56.1775 | 2026-09-20 15:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 4356a209-7b95-3904-a229-19711ecf1176 | -10.4103 | -48.9112 | 2026-09-20 15:40:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 30509232-15f9-3247-9772-4759ac113e47 | -9.6665 | -54.3332 | 2026-09-20 15:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| dde16b95-c730-3169-b941-1a2f49034c21 | -10.2793 | -50.2177 | 2026-09-20 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4ecfbea3-ed70-315a-9827-89bebbd1ca60 | -3.3138 | -59.4472 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 51f3723c-ca3c-3cd4-a1ec-894f7e91cdc9 | -12.1332 | -47.0185 | 2026-09-20 15:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| d1f14eed-a164-37e6-9929-30a977bb0f21 | -2.8975 | -57.7793 | 2026-09-20 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 91c30f8d-5d55-39a6-9594-e2c95fecc62a | 2.7269 | -60.2966 | 2026-09-20 15:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 023e1707-17f3-30c6-b6b2-d78e27b5cd52 | -2.9143 | -58.3401 | 2026-09-20 15:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 0d253ff5-378d-36eb-90c6-578de45916df | -6.1113 | -57.6255 | 2026-09-20 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5240f8fd-6d5e-3cfb-b8b4-963c88a2377c | -10.9665 | -49.7583 | 2026-09-20 15:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 91476240-d835-3b69-8cbf-97de49ff9fa7 | -9.0353 | -48.7704 | 2026-09-20 15:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 37b9f790-91b1-3509-b69d-c63d8a86f56a | -3.331 | -59.8292 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8e8ea9fd-6dc6-390e-b1d7-8e060c5b6e5b | -10.7612 | -50.9132 | 2026-09-20 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 10afa48a-ebc8-3d76-8cfc-f79bd0f20f1e | -3.6077 | -59.0577 | 2026-09-20 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 15831c85-2a42-36d9-8548-20cec0b977e2 | -8.0708 | -55.3321 | 2026-09-20 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| d0a048ee-3a19-3d5b-8145-a2b8e427dabd | -3.2955 | -59.4476 | 2026-09-20 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bd31a257-51a8-3c0d-9e9a-e92c4d50d273 | -6.3656 | -58.2966 | 2026-09-20 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| a71b4dd2-f48b-35fa-a38a-6681ccb624b7 | -6.8032 | -59.1693 | 2026-09-20 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |


[Clique aqui para ver as próximas entradas](README140.md)
