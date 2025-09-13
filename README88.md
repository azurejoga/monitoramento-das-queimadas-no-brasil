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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e26947bc-8fe8-364e-8493-adb1285ffc84 | -10.53569 | -51.49772 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c57035b4-c60d-3ba1-8a0f-4671ba772df5 | -10.52321 | -51.50539 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b32c2e59-3333-39f6-9bb3-0495238eb78c | -10.85397 | -48.1824 | 2025-09-13 04:59:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91dad4ce-802a-37b5-989f-85de1c0bc5c4 | -16.25901 | -50.07245 | 2025-09-13 04:59:00 | NOAA-21 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89a5abd6-e280-3d6c-8b69-0d86acc73a6c | -15.84956 | -49.94405 | 2025-09-13 04:59:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b187e65d-365f-3329-aa05-7e938967a9d7 | -9.49335 | -55.97046 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8f9c154-5925-3d96-b5d5-06e6ec366be1 | -12.11013 | -47.59371 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 44d6c5fd-85ad-31ac-9147-64af27cefb61 | -11.56263 | -50.57122 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45df62c0-6e05-3525-b5e2-39746cf2e077 | -15.16507 | -52.47937 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a863b1c1-ff78-3c05-ab3c-b24834ccd10a | -12.96617 | -54.74702 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e3694c98-7e8c-3ebc-86fd-8b3d45e56692 | -10.47926 | -51.86686 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e184211a-288a-3bd2-b5da-bb4b5ae5aa52 | -14.39472 | -60.29084 | 2025-09-13 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8200425d-831d-35f6-8abd-5901de48fa53 | -15.77913 | -52.25351 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cb72e51f-83dc-3034-9bd8-2295df7fd356 | -11.4332 | -45.61303 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 4235b747-c224-3208-94a0-3d6c00aea43e | -10.5087 | -58.0341 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1298f9f1-3b7f-3ee2-9577-f1165dfe119b | -14.63748 | -52.10038 | 2025-09-13 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6d0cc29-5407-3f24-a59d-c72ec5f6b9e2 | -14.18063 | -46.281 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 48.3 |
| fbd62af4-ab62-33d5-bf44-373f85084b43 | -11.13571 | -51.4636 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bfc731b1-da82-3295-b1c6-36e7547b44f5 | -12.86474 | -52.97253 | 2025-09-13 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc7a7f20-939e-347c-89ba-76615325d40e | -11.42858 | -45.6044 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9ad20210-e7fd-30df-8e53-5f3a5a28b9bf | -9.5 | -55.97153 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ca161919-76bf-3dff-acf7-cb2ff5bdca78 | -11.13784 | -50.71792 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ec5506f-0ac2-3561-895d-7de2d1d14a12 | -10.69939 | -48.65325 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ef044024-7d86-307b-8776-f6ac8789d2df | -11.1981 | -55.08378 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e04f2bf3-bc6e-35cf-8d02-92e174df1b96 | -15.11464 | -52.50188 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 533e3976-713e-35ef-8a30-be5ed2cd56e1 | -15.13906 | -52.47475 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a87596f3-c655-3735-b288-c8f96a06c0a2 | -15.16095 | -52.39765 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 620d18e3-544e-3529-8f6e-2e36409093fe | -10.38005 | -50.49508 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2582178-23fb-3b6e-847d-07fbbdec07be | -12.79595 | -47.98376 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 77617372-539d-31cf-bc2e-920f5c55294b | -14.41864 | -46.40704 | 2025-09-13 04:59:00 | NOAA-21 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 483f3950-26c8-32e9-b4a3-561f10b56de0 | -10.5425 | -57.08297 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b88afe7c-da90-3021-af19-904cb1f43811 | -9.90697 | -57.05627 | 2025-09-13 04:59:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fac1ceb-2616-38cd-bba8-95ee276afe07 | -11.43455 | -43.53894 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea28e292-ee9e-3855-84d9-cad3bc730a24 | -10.41509 | -50.61514 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac0c6c2e-0438-32df-a2a7-abad48036477 | -13.47883 | -48.44422 | 2025-09-13 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 744a243c-942b-32e0-aeba-d8fb02a62644 | -14.19521 | -46.25059 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6bf0485e-70c9-3f4f-a0c3-ae3d70a01e0c | -11.83345 | -50.5739 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd31d2d-d8ae-3a5a-9678-b6ae49a8a7e3 | -10.42127 | -50.60001 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b590081-353e-372f-a045-7862c6bd4997 | -11.3358 | -50.79132 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 152d5729-a145-343d-a551-9f0c1d5a7318 | -15.57371 | -54.76981 | 2025-09-13 04:59:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 752e522e-e17f-3ddd-b130-179247115be7 | -12.80838 | -47.99635 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7db55344-c0ec-39b6-af0f-31ab2db5fa10 | -15.28703 | -53.77574 | 2025-09-13 04:59:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1819752b-b5a1-3765-8e02-79be7bcf4157 | -12.88448 | -62.10925 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 296c370a-e2d9-33d4-b05e-e4738122c1e2 | -10.44243 | -50.62093 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4ff7fdf-10ee-3e94-a7ac-417f1f1e997e | -14.43577 | -47.333 | 2025-09-13 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7576ba7e-a4db-3be1-ae6c-f04789d8cec9 | -15.68001 | -49.90354 | 2025-09-13 04:59:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0d737fe2-bdcf-3db5-9b55-c7b14bb0aa93 | -10.33703 | -54.31656 | 2025-09-13 04:59:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 426646e4-dad1-3be9-8dfc-427665bd0fb4 | -12.92441 | -54.75571 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a86cf07-240b-34e0-b3d3-40cd91b68329 | -9.26947 | -59.40026 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9f06117-3e32-3a32-a758-51dbb146ecfa | -12.80927 | -47.99471 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 90ca4b5b-d18f-3e8a-91a2-6d6f710ef9aa | -11.19594 | -51.42279 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2aa5c5d9-b013-31ad-917d-e520dd02f886 | -9.26734 | -59.4024 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1cd9922a-e690-3cb4-aacd-5ec5e5f2d2ee | -10.71889 | -48.60903 | 2025-09-13 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfecabf3-2aa8-3f69-afbf-5aebb2b2d2b1 | -13.89829 | -48.28815 | 2025-09-13 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 93dabc37-c751-38bb-8e88-bf7b62d37e4b | -9.27498 | -59.39126 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c97f9cf-913b-3070-a1a1-397e45a2f625 | -16.41391 | -49.03476 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 79f05b42-86e7-3f86-9a79-983f6259fb6d | -12.00045 | -47.76273 | 2025-09-13 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 8a1549dd-1e44-3c13-9faa-f6884487eab2 | -11.79433 | -50.54732 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a124c40-c1bb-310b-94a8-7838704907d1 | -15.86654 | -51.84514 | 2025-09-13 04:59:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28f95268-3e49-3535-9932-576447275c50 | -11.11486 | -51.3944 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c426450-43f7-3cbc-90ba-9a66d49bb419 | -12.57125 | -45.67226 | 2025-09-13 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d13bf6bc-39cb-30d7-a358-43ba3565a649 | -9.79553 | -61.50887 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17f83c5f-2cc7-386c-8f38-93a85e0de986 | -9.26561 | -59.39963 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 26a051f0-2be3-32d2-9177-14856e252bc7 | -10.52499 | -51.5463 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e2ffc774-ce16-3c38-a94c-9be8560a111f | -10.50262 | -51.54388 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d989b3e9-ee0c-3aaf-ac12-0e89fd185e04 | -15.13586 | -52.48621 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48c8c415-99ca-3079-ab39-348db01aac87 | -11.88245 | -50.57386 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 145f36db-94df-3bde-bd84-5cdc55866c41 | -10.20066 | -57.98529 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2e20b467-235d-3f2e-8cd5-e4fd78df1522 | -15.1072 | -52.50079 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7b0ebd43-441d-31c2-bf6d-509a1ef5c9fa | -11.43577 | -43.55442 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35810a83-513d-3040-9fcb-2dcd54f47c0a | -10.00555 | -59.97518 | 2025-09-13 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cc756ceb-6ac0-3601-baea-60fd6f11f3b1 | -11.13214 | -50.70152 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.9 |
| cd70c326-899f-3157-b2f6-44f386d20164 | -10.51259 | -51.55365 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4be21272-c549-39dc-be64-6cf3f55da2ec | -12.12719 | -44.84707 | 2025-09-13 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 088e7175-cd24-3d85-8de6-9b7124061954 | -15.77413 | -52.23332 | 2025-09-13 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb2e0c56-9655-36d1-9f0d-f0c1ef556be8 | -14.44278 | -48.41677 | 2025-09-13 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f7f2670-0692-372a-a7a4-a807ea58e5c1 | -14.19683 | -46.28609 | 2025-09-13 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ee26019-6a9a-39cd-9a8e-4dc18b5551e4 | -11.73539 | -44.2084 | 2025-09-13 04:59:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 008da89a-5f66-324e-a5ce-08331b753de0 | -10.38472 | -50.49055 | 2025-09-13 04:59:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 056ac0f2-2d3a-33a6-b570-261d62e45f18 | -11.42256 | -50.74401 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 80f87db8-02d0-3609-a4fa-81a2c2de7fc0 | -11.44411 | -43.56674 | 2025-09-13 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd07fe7e-2a0d-3717-bb22-e11f94280f1b | -14.29202 | -46.09158 | 2025-09-13 04:59:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e15e95cd-403d-3a63-a01a-df4ecfc65d2f | -11.42185 | -50.74911 | 2025-09-13 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a850a7cf-881b-33ed-83b9-b50d115cfc05 | -11.1766 | -55.0696 | 2025-09-13 04:59:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00567a7a-f848-3970-90f3-a462ce8fd9be | -16.43575 | -49.05259 | 2025-09-13 04:59:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20c11b98-2b46-3263-ba4e-e775609bd990 | -11.86498 | -50.58213 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 36acf7c1-6957-3657-8766-3356c4ee33e9 | -12.2731 | -53.91756 | 2025-09-13 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8bbc325d-4f51-37dd-ac4f-163e3b86f1bf | -12.82285 | -47.92756 | 2025-09-13 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0180647b-b4b1-3a86-ae37-b87558ca92e9 | -11.79834 | -50.5479 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 365ef43e-b970-3e35-8495-9358b6442fbf | -11.83583 | -50.55618 | 2025-09-13 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f8a076e6-54be-344a-bea1-1bec8ba978ef | -12.15636 | -60.7387 | 2025-09-13 04:59:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b0260a6-96f0-3fb4-9f43-d66c917fa477 | -9.96051 | -57.72208 | 2025-09-13 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35cadcaa-b49b-3a44-8694-9b10ce500feb | -9.26267 | -59.40662 | 2025-09-13 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 91a40619-f413-3813-a6cc-af65432521bc | -12.91888 | -54.76954 | 2025-09-13 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a04308cc-dab7-352f-8b0c-6416df821a9b | -10.50635 | -51.54425 | 2025-09-13 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ff82d39-4c42-3d34-b3d3-b5b81c90dedd | -11.15689 | -57.19149 | 2025-09-13 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11c6cdee-5eab-3722-9bea-450ac68950ea | -11.77111 | -51.51068 | 2025-09-13 04:59:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 75647bab-8e45-3a51-aabb-93b5f0a30a01 | -11.15893 | -50.71065 | 2025-09-13 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9efb02df-e44a-378c-a233-428803dfab3e | -12.88295 | -62.11774 | 2025-09-13 04:59:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e8ded2-658e-3c23-9387-418316327bc5 | -11.39603 | -50.47899 | 2025-09-13 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README89.md)
