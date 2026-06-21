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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9a34bb1-c3ae-31d5-9c29-fa3cf667c3f1 | -10.68949 | -47.7039 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90276b76-9478-3c31-a1fe-d0aa2892d923 | -11.09927 | -54.14468 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 8b81d696-7fa4-34ff-9d57-d79ba92bb625 | -11.93853 | -43.389 | 2026-06-21 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0c2bb46-5975-380d-82dd-5a76f1f1b0ce | -18.7742 | -40.90483 | 2026-06-21 04:25:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c8871f52-c117-3abc-a2bd-be3bba79a87e | -11.1976 | -46.77897 | 2026-06-21 04:25:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2c0f27c-cb4c-3e73-8f8f-312f7d6c830c | -12.42472 | -54.18224 | 2026-06-21 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c11c0b5d-0ce8-3b1c-882b-f5337d86154b | -11.89037 | -43.83082 | 2026-06-21 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dcb4ea9f-8087-31e8-a314-dd6289450ae3 | -16.94226 | -47.1414 | 2026-06-21 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6a55ea7-b273-3136-8dc6-c9d0aa834414 | -11.91101 | -43.41066 | 2026-06-21 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b6423d3-0d7c-332b-89c4-1d05f762d232 | -10.80491 | -48.56986 | 2026-06-21 04:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ebc112f-74fd-361a-80bb-005ef979ed5f | -11.89154 | -43.83421 | 2026-06-21 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6466459c-ba3e-39de-8680-26dcc0c9614b | -10.87843 | -46.33138 | 2026-06-21 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c71652da-77ff-399f-a62b-9d072161e95f | -13.56237 | -43.51014 | 2026-06-21 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f6cc03e-9a75-374a-93f3-6eb873e92437 | -11.64103 | -48.5261 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93c2e4e8-cd81-3693-9b76-87c9cc6f8959 | -15.95632 | -42.16022 | 2026-06-21 04:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2796a7da-b294-32f1-a183-383267472f89 | -11.63488 | -48.53932 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b53af36-8d73-31a3-abfc-1bdcda4585be | -10.51256 | -51.93768 | 2026-06-21 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b490834e-2c1b-3d6c-a88c-0397d98d5f21 | -11.09996 | -54.14108 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 161fcef2-1cd9-3a7d-ab69-7b6089772b2c | -18.77013 | -40.90423 | 2026-06-21 04:25:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a124834-6c74-3117-84d5-70215a64b68d | -11.55041 | -48.26651 | 2026-06-21 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bde12d17-412c-3ce8-9e01-b8cc72cf7594 | -11.11019 | -54.14708 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d26c854a-742d-3c52-b511-8eaaa8e40802 | -12.51502 | -48.30084 | 2026-06-21 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b7bb637f-301f-39d6-8f41-9a910c53b9df | -11.10136 | -54.13389 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33239993-b9a5-3388-8986-a1221b70c712 | -11.79589 | -42.63676 | 2026-06-21 04:25:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b2c5d1be-5556-309c-b46f-2f69124a7392 | -11.10066 | -54.13748 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 82f9eb46-8f67-335b-b292-a9fa4f3b69ff | -17.61355 | -46.69579 | 2026-06-21 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ad4bfd8-9dea-359e-9eb1-254fcca17437 | -11.94618 | -43.96711 | 2026-06-21 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 863499f3-d58e-3bb2-bcc5-58eef51c4dff | -11.1116 | -54.1398 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d5e16c5a-bc4e-32ab-b4c8-588fa81ff55c | -11.64024 | -48.53073 | 2026-06-21 04:25:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68acef81-d589-3c03-8444-681aeb78cdbd | -12.51426 | -48.30527 | 2026-06-21 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 50af798b-09f6-3fa9-bcbf-1c330ae25ea5 | -11.89209 | -43.83065 | 2026-06-21 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ba648b1b-d818-35e2-9712-a144fc9949f3 | -10.15705 | -51.65087 | 2026-06-21 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0331299-631c-3723-9b04-c4549fe02bcf | -11.009 | -45.20746 | 2026-06-21 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42b4dc62-1ac8-3320-b9c3-08ebca12f468 | -13.82714 | -47.12243 | 2026-06-21 04:25:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 791b74d4-0ea1-369f-ad9c-b48696ad2569 | -13.49878 | -54.43349 | 2026-06-21 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6be53b6d-f1fb-3f89-9073-f7f1ef6f3542 | -10.54237 | -47.71135 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe07b494-dbd2-335d-8b18-a5b4f8c79256 | -10.05474 | -48.09427 | 2026-06-21 04:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60810097-ee14-3545-96cf-d0642e140f65 | -10.90159 | -46.31966 | 2026-06-21 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b2c4841-7059-3118-8d98-59ddc6c5673d | -10.25288 | -49.60512 | 2026-06-21 04:25:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 740b6613-3ae8-33d6-86b1-98c059a83cb3 | -11.09236 | -54.15088 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 80d726fb-1d1f-34db-a20b-3e4f2b470b1a | -18.77331 | -40.90365 | 2026-06-21 04:25:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1fd81f28-06bb-35fc-bfc7-92ad09a16247 | -17.6163 | -46.70004 | 2026-06-21 04:25:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2edad4b9-8532-3cbe-b747-2a9930b8d1d4 | -10.05551 | -48.08974 | 2026-06-21 04:25:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7fb73464-cd94-3bff-b7a2-96799d963f2e | -14.09082 | -52.19653 | 2026-06-21 04:25:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdd36e2b-1520-32d7-aef8-701f27b468bd | -16.93674 | -47.13274 | 2026-06-21 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05ddf78d-5609-35a6-bc26-5e81cdc92665 | -10.83607 | -49.12416 | 2026-06-21 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33ffebb4-e3fc-364b-9101-5643c228b256 | -11.10684 | -54.13499 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 48f40cb2-fd89-3ad1-8958-7e3f48eed7c5 | -11.08493 | -43.18156 | 2026-06-21 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae878e51-cc65-3bcf-a21d-beb7283d0361 | -11.09308 | -54.14718 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e141faf5-c0c9-31bf-82e0-2aade3dc3172 | -16.93337 | -47.13212 | 2026-06-21 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 791c5e07-0746-3513-b2f6-8b6c58651cd4 | -11.10259 | -54.15693 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd6207a0-20d5-3c8a-9bd8-f21d7037f928 | -11.10473 | -54.14587 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| cde4bce8-b2f6-3011-aae1-edf59a535cd8 | -11.1109 | -54.14343 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a66559e4-2fe2-35f5-9d50-aa2c9669c0f7 | -11.03798 | -47.04618 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 410de0a1-68af-3747-8207-20437442e1d4 | -12.23472 | -43.21029 | 2026-06-21 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5058c85b-a1a2-3cd0-9a83-04a66732bdf8 | -13.85797 | -45.89588 | 2026-06-21 04:25:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c85f211-8e05-3bc8-a245-4effccfd8f6d | -9.18544 | -58.0618 | 2026-06-21 04:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d79e9529-6bb7-347d-8750-564ba064a302 | -10.25275 | -47.34572 | 2026-06-21 04:25:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 744c8b09-14c2-3848-95da-719085ec7425 | -11.10948 | -54.15074 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1f98737a-861b-39e7-8659-84cb93952dc4 | -11.10401 | -54.14957 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2ab2a66f-2dc1-30a9-b091-f7feef596c35 | -13.56293 | -43.50644 | 2026-06-21 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ed72fc-ad10-3079-8114-9e5ff17d03fc | -11.09782 | -54.15211 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3f8f1237-314f-35f3-82b3-935f161e2177 | -10.83211 | -49.12346 | 2026-06-21 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c43d2db-37af-3f4d-9617-471d1db335c6 | -12.42406 | -54.18563 | 2026-06-21 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d6616573-1308-3a62-b9ab-4941468a8d78 | -12.82951 | -49.796 | 2026-06-21 04:25:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e1497ad-6ae3-378c-9d49-346965e0e8d2 | -11.09379 | -54.14357 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 097b41c6-bc12-37bd-ac08-2ade1ccfa916 | -16.05864 | -42.0896 | 2026-06-21 04:25:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b0e23737-6f69-3b3a-837a-6e2e98c03447 | -12.4187 | -54.18447 | 2026-06-21 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0be334a-bc45-3bd2-a252-4f05cf841328 | -10.8098 | -44.56505 | 2026-06-21 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50cffee3-09c7-391a-bb6a-173ea0cd5177 | -11.10808 | -54.15798 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f287e300-8ef2-363e-ae0f-7946fecbaf1e | -13.85855 | -45.89228 | 2026-06-21 04:25:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b0707be0-94d9-3d82-95d2-6527669dcfcd | -12.4543 | -46.52539 | 2026-06-21 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d396f13-dde7-3968-ac60-1377f24d0378 | -10.51577 | -51.93943 | 2026-06-21 04:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3fa18293-6f34-342a-88b4-cbbabdc9d3d6 | -15.95997 | -42.16082 | 2026-06-21 04:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4d30842e-7647-3d8e-9baf-2609ae54aa72 | -14.37046 | -45.21432 | 2026-06-21 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 32e014d3-f39a-324d-8942-8464ebda1ec9 | -10.53502 | -47.73236 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d61f6a3c-9a63-3984-9185-b25607972526 | -10.54164 | -47.71564 | 2026-06-21 04:25:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ed8bb17-f6b4-3d1d-ab91-2896142eb149 | -16.06231 | -42.09019 | 2026-06-21 04:25:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 5cd55ac7-2880-3c3d-95ad-a436014debb0 | -12.41805 | -54.18785 | 2026-06-21 04:25:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d6b09ea-eff1-3267-8047-7e08db6cd0d3 | -11.10878 | -54.1544 | 2026-06-21 04:25:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cad9fe45-3d9b-3d45-ab9d-60f0e127bf73 | -11.00843 | -45.21101 | 2026-06-21 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18478164-64b8-3c27-b0ae-dcdf05d452ac | -23.45343 | -46.74488 | 2026-06-21 04:27:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2eeaf4de-e6eb-3093-a2db-452584f0ebc8 | -20.81816 | -41.92589 | 2026-06-21 04:27:00 | NPP-375D | PORCIÚNCULA | RIO DE JANEIRO | Brasil | 3304102 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 242cf586-d130-3b1c-ab15-4a97de258f68 | -21.58962 | -45.45018 | 2026-06-21 04:27:00 | NPP-375D | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3decce1e-025a-31a5-bf2e-76a6aaf56e2d | -26.617 | -48.7703 | 2026-06-21 04:29:00 | NPP-375D | SÃO JOÃO DO ITAPERIÚ | SANTA CATARINA | Brasil | 4216354 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b3c8f3b3-2ff6-3630-9944-1d1a63f9e0a0 | -24.94199 | -53.4478 | 2026-06-21 04:29:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46519fbb-7164-3253-a6d2-645aef934a4f | -11.1168 | -54.1294 | 2026-06-21 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| c99e0f00-fc6d-3c98-af9d-19872bac62e1 | -11.0979 | -54.1311 | 2026-06-21 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 480982d9-dc0a-3f92-87ed-64c7565985dd | -11.1165 | -54.1499 | 2026-06-21 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 00f6b1a7-bec4-3456-8623-a7c436609653 | -11.0976 | -54.1516 | 2026-06-21 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.8 |
| ae2ae606-0ae5-3de1-ac98-874e977e5726 | -11.0979 | -54.1311 | 2026-06-21 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.1 |
| bf836738-4947-3c3e-91bc-5b3b7fc3a69f | -11.0976 | -54.1516 | 2026-06-21 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 471395d4-e50b-3ab0-91b4-9444810ec5c8 | -11.1165 | -54.1499 | 2026-06-21 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 63754c7f-0d82-37e9-95b7-e7fa01ba609d | -11.1168 | -54.1294 | 2026-06-21 04:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.4 |
| e011c270-fc33-3b23-9fb4-fae3aeb01094 | -1.32229 | -50.64227 | 2026-06-21 04:42:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9d83582-1f28-3b6f-ac6e-c01c9ef9b9c4 | -2.90517 | -49.64061 | 2026-06-21 04:42:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9486ac1a-8e6a-3721-9661-71537323233f | -5.96155 | -43.49245 | 2026-06-21 04:42:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5ef25d3-1dd9-3236-94e4-7350f61b15d8 | -5.82091 | -45.07596 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 017b092c-0767-319f-9e31-6685d23df724 | -5.81858 | -45.07782 | 2026-06-21 04:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5338f62-8df8-36fa-94fc-8bd9607129ee | -6.95564 | -42.06497 | 2026-06-21 04:42:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
