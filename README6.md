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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 325d2210-9f04-3146-ad9a-c7663df0e601 | -16.01772 | -47.94678 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 144.4 |
| ecd2516a-725d-3445-ad41-24805130cc25 | -11.98965 | -47.76313 | 2025-09-13 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7436dec2-5534-3815-a335-48d0b7037dbf | -12.92952 | -54.73898 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 0ca9d719-25f7-3309-82f7-ff71e48f6234 | -11.82889 | -50.55487 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 41a65dcf-c722-3f0a-987b-a128687b4467 | -20.10349 | -46.91607 | 2025-09-13 00:50:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f899a1a8-46f8-3f98-b901-f8dec49b3035 | -17.67646 | -47.86528 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6c780ee6-cd07-33f8-9585-aaafb1e1777a | -11.14078 | -51.47393 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| d3ed5659-f70e-32f3-897c-17bbd9fa8609 | -11.73937 | -46.61144 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0877c961-69a1-30af-a142-5384ca55e252 | -15.46006 | -47.32737 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| c88268e7-85b6-3f30-a4a6-728408bce35f | -17.4397 | -49.24911 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6cfb5f1c-7b39-33d2-b6e1-537062c9ad22 | -12.97377 | -54.74919 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 25d37925-420d-397c-948d-704d6a73adba | -11.03186 | -51.42142 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| eb00cc26-6289-3fe4-a76d-bad0bbb08fa3 | -14.4868 | -53.92368 | 2025-09-13 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 03689595-2a8c-3334-b962-8f64bf878c9d | -14.1971 | -46.2691 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 64e74cfa-8ec6-3a7d-af23-78d80a795100 | -12.84846 | -47.94543 | 2025-09-13 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 145c6c5f-f331-3c3a-9f6f-8784a3a37bd4 | -11.47932 | -43.6254 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 06b23cde-825b-364b-97fe-b0217dd806f9 | -16.41153 | -49.03844 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 14881100-76f9-34ad-8776-2fd07b37d07e | -10.85623 | -48.18455 | 2025-09-13 00:50:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0f4e481e-865b-381e-9d77-32b76724f5a9 | -16.49316 | -51.99871 | 2025-09-13 00:50:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 94fe1cd7-883d-324c-8016-0642c0a7b0cd | -15.1421 | -52.48748 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| f3979ea3-dc33-337d-aa55-0a0642d719b0 | -15.47067 | -47.32576 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9ed55a94-398e-3509-b7fa-61fba49ffdde | -20.60125 | -50.39561 | 2025-09-13 00:50:00 | TERRA_M-M | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 49775ea1-ccbe-3711-8c1f-58f96e16171a | -16.24973 | -50.06352 | 2025-09-13 00:50:00 | TERRA_M-M | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 42.2 |
| fc2a56d0-46fe-3b0e-9aff-d9319303d16e | -15.7066 | -50.57968 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 23e608f8-67ed-3a1d-a7ab-2bd09992d2d3 | -16.4675 | -48.86192 | 2025-09-13 00:50:00 | TERRA_M-M | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 669eeff1-e0ea-3c42-97c5-fb8311f26911 | -14.46219 | -55.95497 | 2025-09-13 00:50:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f0525dd1-b6c3-342f-8b0b-b416ed69c51a | -14.4367 | -46.40841 | 2025-09-13 00:50:00 | TERRA_M-M | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 73d146ff-12d5-33c7-b518-3b9377a3481a | -12.13151 | -44.8387 | 2025-09-13 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 880a6209-1b65-325c-a92e-e3f4e8257bef | -16.33846 | -51.5397 | 2025-09-13 00:50:00 | TERRA_M-M | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 26195bf1-d7c2-340d-80d0-e5c91a931c53 | -13.00419 | -44.13647 | 2025-09-13 00:50:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 7576b349-6008-323f-9703-eb3ed7ad506a | -15.77236 | -52.24868 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 590f0a3f-cc73-3ab8-bc6f-608cb9000d51 | -12.10153 | -44.87383 | 2025-09-13 00:50:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 0f54c652-1e53-3634-abfe-e745226079ce | -15.04735 | -50.16608 | 2025-09-13 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9e8a42b8-6fed-3703-8dca-55ef18cab45b | -12.91991 | -54.74024 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 79711691-6ae7-38c2-a88d-e08da88949a5 | -11.15842 | -51.4056 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 2efd60b7-94a2-31d7-9bb7-43f95a198132 | -11.73409 | -44.23616 | 2025-09-13 00:50:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| ad9793bf-45c3-326b-b086-f1dbe154d272 | -12.00054 | -47.76134 | 2025-09-13 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 32709ca9-f696-3594-bf4c-dd516756bcf4 | -18.59748 | -47.19672 | 2025-09-13 00:50:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a512409c-0c3c-325a-911d-ec13886a2502 | -20.87497 | -49.33263 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 648843ec-b745-37fe-ba07-7c209f705087 | -17.55121 | -44.55414 | 2025-09-13 00:50:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 23de617e-9812-372e-a647-bdb96f470939 | -10.1538 | -47.89036 | 2025-09-13 00:50:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 0bf3c8bb-2f39-3593-b2c7-628955f5b7aa | -16.02774 | -47.945 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 151.9 |
| cbd11bd8-1002-30a4-a6e3-160ef297b2eb | -15.0667 | -52.47648 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9f78779c-42db-39cc-9cf7-6c67c09f596e | -10.7747 | -50.52853 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d11f5723-17bd-38cd-909c-6679f1aaa432 | -16.0159 | -47.93492 | 2025-09-13 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 124.9 |
| ee50b2d8-7264-32c7-a4de-32af635800e9 | -15.15751 | -50.16265 | 2025-09-13 00:50:00 | TERRA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6804f393-41a9-32c3-a9b1-c9f7bc689d00 | -11.06282 | -51.51057 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fe11cdbd-59f0-369f-95e4-e812a7e75515 | -15.16882 | -52.48351 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e6507454-f884-3b9b-a3b3-1e43d7ce58c9 | -14.28738 | -46.06369 | 2025-09-13 00:50:00 | TERRA_M-M | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 29a60aed-9571-3e9a-adac-0b9d115ec9a0 | -17.3772 | -52.90297 | 2025-09-13 00:50:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fa6d6d6b-0c1e-3194-aaa6-2b312b3d6a49 | -15.68855 | -50.58835 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c595e23b-134d-36b1-835d-050e8edb129c | -10.65119 | -46.30107 | 2025-09-13 00:50:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| baa76806-e264-33eb-8d10-3be722a9875a | -14.97687 | -49.55326 | 2025-09-13 00:50:00 | TERRA_M-M | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| bdc64f0f-2038-398b-93ed-a906b349385b | -13.70046 | -49.91341 | 2025-09-13 00:50:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fd2d05ec-ba77-3ccc-845e-fc9aa288aee1 | -14.19484 | -46.28002 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| dab99a17-6813-3cfe-91fc-bfafea2626a3 | -16.41513 | -49.23305 | 2025-09-13 00:50:00 | TERRA_M-M | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 158425c3-bffa-35d2-ab0e-6ee695f8e04f | -10.764 | -50.52001 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 63ff479e-bc63-3e42-8d4f-12d96dcad5af | -11.72745 | -46.61376 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| d3efec19-d458-3879-b26a-cb0c5461939a | -15.55053 | -54.80289 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 31.6 |
| d35e22ac-37d7-3b37-a0fc-c20cd62f31fa | -11.80227 | -50.55483 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| bebd3705-3e24-39e9-ae7e-4a8eb94d1fa2 | -14.19749 | -46.29586 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 56454fa7-c418-3749-acd4-4f5125141cc2 | -11.81973 | -50.55627 | 2025-09-13 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 6513246f-d2c6-36b9-89c8-d8945638120f | -11.03949 | -51.41087 | 2025-09-13 00:50:00 | TERRA_M-M | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46cde7b9-f7a1-312a-88a5-28768d04de10 | -10.46659 | -50.01213 | 2025-09-13 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| bc9c0057-1823-3cd7-82fe-b5d36b0cc9a8 | -14.36894 | -52.96901 | 2025-09-13 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6420657b-9c0a-301e-a07a-d783381eb810 | -17.35821 | -42.70211 | 2025-09-13 00:50:00 | TERRA_M-M | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 054a8082-a684-322f-8674-47f57bb6ab28 | -11.13947 | -51.46476 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e5f90534-8f76-3b6b-aaa4-a24028699885 | -17.37852 | -52.91306 | 2025-09-13 00:50:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eb0a9352-f174-3208-8a1c-c3948a64ee46 | -15.28565 | -53.77906 | 2025-09-13 00:50:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 9a829570-42b0-3d29-a74b-aab4a830d237 | -14.45939 | -47.32248 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 29.7 |
| c48827db-03f3-3793-a630-b51c4909de0c | -20.41984 | -50.74364 | 2025-09-13 00:50:00 | TERRA_M-M | PALMEIRA D'OESTE | SÃO PAULO | Brasil | 3535200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.4 |
| 0db8fad5-0e5a-3193-8a01-00562d28d639 | -14.46797 | -55.96165 | 2025-09-13 00:50:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1e44b2ad-a9af-3251-ac1b-170fba19f272 | -10.74835 | -50.5427 | 2025-09-13 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| cc7fe200-56a2-392c-9bd5-dde583772970 | -15.53468 | -54.67472 | 2025-09-13 00:50:00 | TERRA_M-M | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| afac6f74-f251-3fec-be1f-2cae4dc00609 | -16.39093 | -49.06855 | 2025-09-13 00:50:00 | TERRA_M-M | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6a21dad3-2183-360e-b132-b4041b26f3b5 | -11.15101 | -51.48177 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| ab62409e-7b30-380a-99cd-052bfe15b790 | -11.27723 | -51.13868 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b68230eb-2ec1-38b8-a08d-83c662be93d6 | -13.13702 | -47.1419 | 2025-09-13 00:50:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0cfae8aa-4dc2-3bca-b145-cf05d863420f | -16.53355 | -51.75104 | 2025-09-13 00:50:00 | TERRA_M-M | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7020cea0-06ac-3cdd-8b35-c13590c214e3 | -15.78252 | -52.2567 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b16644fa-d0a9-3d0f-8609-a2be80f2f30b | -15.78125 | -52.24733 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 73b4b98f-6482-3072-89cf-5392d08e2e84 | -12.57566 | -45.67519 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 990bdf2f-52d6-39b6-b277-1e0d03fa1f6d | -19.98051 | -46.91934 | 2025-09-13 00:50:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 9c7841e6-9fa7-3877-b22b-953c360b97b2 | -14.17989 | -46.23713 | 2025-09-13 00:50:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e09858f9-91c1-3738-9bf4-f71f8e5e4fdf | -17.30729 | -48.73093 | 2025-09-13 00:50:00 | TERRA_M-M | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 102eaaf2-2278-3aa5-8c7c-a97b1d03f7cc | -17.42237 | -49.24794 | 2025-09-13 00:50:00 | TERRA_M-M | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 980c6ce5-5e2d-3eb5-a78e-274dec8d2d6e | -15.06423 | -52.45818 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2f3e6f38-7663-3cf0-967c-dfc5b4f2dc0f | -16.56093 | -49.22799 | 2025-09-13 00:50:00 | TERRA_M-M | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 3c6cd313-ee6c-3d48-a8b9-9c6c0d8b6a65 | -13.25627 | -57.33702 | 2025-09-13 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 27145643-3d31-360d-b3c7-144232696d7e | -20.09338 | -46.91753 | 2025-09-13 00:50:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 105e1e7c-da50-3eba-99ef-e4a8bc404514 | -11.1558 | -51.38718 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 95ddcf22-86cd-3740-990e-48fb977aa143 | -16.50689 | -55.12932 | 2025-09-13 00:50:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 35adaf4e-61c6-3119-a335-c6b5c1094576 | -11.1497 | -51.4726 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| adbfd7c6-cc4f-3c85-950a-ee43dc2a5347 | -20.87637 | -49.34228 | 2025-09-13 00:50:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 57aa635b-3c3c-38ae-b030-6a79dcc1440e | -15.77876 | -52.22886 | 2025-09-13 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 65cddb09-06d6-3e02-b16d-989be518248a | -17.23255 | -50.22589 | 2025-09-13 00:50:00 | TERRA_M-M | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5ea4dcc7-e27d-3293-85e3-29e703e72426 | -17.09796 | -48.85955 | 2025-09-13 00:50:00 | TERRA_M-M | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63cd2a83-1467-34e3-b5fe-3f5e4ed832eb | -12.10036 | -47.59211 | 2025-09-13 00:50:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| a5feb54e-d55f-3a75-b4e0-2ae360828a6f | -11.14146 | -50.70882 | 2025-09-13 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| fdb0aff3-d23a-348a-87fc-eaa1ca6c6d5e | -15.03412 | -50.13871 | 2025-09-13 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README7.md)
