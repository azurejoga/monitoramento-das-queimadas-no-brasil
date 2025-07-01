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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 750f8d4b-74e9-3daf-b345-dfea14764c98 | -10.29762 | -57.13179 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c3cbd04-5c5a-3dc9-8d5c-2e8d826e5d52 | -11.57684 | -54.56622 | 2025-07-01 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6df3c88d-550c-3ea3-9aaf-325ffbb5c9ec | -9.25292 | -58.7541 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 12463684-0cb0-38bc-9e4f-497e6b13a24f | -7.61233 | -45.7538 | 2025-07-01 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3dbac627-9b7f-3aa4-8b14-d10cad099ebb | -9.23102 | -58.74548 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db152243-a413-377d-b0f6-9ed37ac6c91f | -9.24755 | -58.758 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb77bc35-0c10-3bcb-a925-6b41ab5cdc2d | -10.07955 | -52.75378 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f027ad77-12d9-36a2-9dc8-751e42886f41 | -5.43479 | -47.13852 | 2025-07-01 04:46:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82b5bb9a-bbb9-354f-9c51-5d84e785fba5 | -11.58074 | -52.12094 | 2025-07-01 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66e68342-6075-3a4b-bb0b-299a631871cc | -8.38012 | -51.07152 | 2025-07-01 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ee9194a-fb3c-39ee-921a-593eb96db9ac | -11.5762 | -54.57006 | 2025-07-01 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1a358fa-47e1-351e-8837-78443bb5a8f1 | -9.24383 | -58.75251 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32b112e1-0d96-3e7b-8386-38c9d04b1927 | -10.55308 | -52.0381 | 2025-07-01 04:46:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c330b41c-00e0-3912-b052-f762d3b6eac5 | -10.87986 | -56.4375 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f63e7dd6-0a0d-3187-a9dc-577bfe28ffad | -10.11995 | -52.34725 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b07d1c32-a2bd-31b2-9d24-133dfdf51dba | -8.88758 | -50.17674 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 683555a2-bd54-3f5d-9fd2-53e42df05a1a | -10.87744 | -56.45177 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 731e9fd2-39c6-3c60-b736-a1b26b6f4d71 | -10.87479 | -53.76239 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeaba96b-77dd-3960-9b6a-ab1419e251f7 | -11.56854 | -47.45095 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9aacfab5-35e4-321f-81ed-156bb0af4386 | -9.24671 | -58.76271 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 996f4df2-008f-3231-a55a-f5387503543f | -6.20988 | -43.36273 | 2025-07-01 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 57b1fe35-dc83-3b16-a541-32dbdcf9ffba | -6.21625 | -43.35261 | 2025-07-01 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 87e0bd0b-36c9-31e1-9ff0-f33cf40c4296 | -7.55128 | -45.82318 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 224b02be-54cb-3b15-b13b-1677f56e6e6c | -8.72774 | -47.99245 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f8be4ad-8347-3afa-8f54-7cc892b4fc45 | -11.07158 | -55.37977 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f4bfb0bf-2458-32c5-ab0a-723a0f237e73 | -10.08011 | -52.75026 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba1d10db-02eb-3277-a3e7-4110775532c7 | -10.86146 | -53.73765 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee62d75c-3833-365e-8644-b88cbb144b79 | -10.87023 | -53.76916 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89e89f54-4f46-3bd8-bd54-d67d2952b4ad | -10.65279 | -46.82929 | 2025-07-01 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ed72b76-f746-32f8-bbd4-fc1a62fe21c1 | -10.86745 | -53.76493 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a76b5516-6001-3d93-afed-36627d3547cc | -9.23557 | -58.74625 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8903edbb-8bd0-3f1b-b18e-6221d4e08665 | -5.57119 | -45.21698 | 2025-07-01 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2d72acb6-c98f-36dc-9421-3d4157364953 | -11.8382 | -47.504 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3e7d3b06-b953-36ad-bef5-b93e89e062f6 | -10.81161 | -55.85578 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 97af8b6c-585e-340e-b3a2-36e902e1d8c7 | -10.86821 | -53.73876 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c2a307f-b23e-343c-8bf8-37aaba039124 | -7.16116 | -49.51128 | 2025-07-01 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71809b8e-c18b-3fcb-9b3d-5188659a45da | -10.93433 | -55.32729 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ac63087-ab3f-3f2b-b10d-65ffe096f919 | -11.20429 | -49.00304 | 2025-07-01 04:46:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6fad0ed-abf3-3d23-b3ce-47d7e42dffd3 | -7.61653 | -45.75446 | 2025-07-01 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 28ff4fe1-31e9-3ab6-aae0-ad6a3937ae05 | -9.97768 | -48.23804 | 2025-07-01 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5cf77baa-a4f1-3339-9c2e-c5ce8c5f2c00 | -9.11544 | -59.05328 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3af88824-e5bf-3b1c-a69d-794c567bbf3c | -10.08178 | -52.73969 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 9e829094-529e-3d83-b73d-9ede1c4eca25 | -10.86483 | -53.7382 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddf5a591-a746-3629-8937-19f9f5a3a251 | -10.06549 | -49.65876 | 2025-07-01 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c79492e0-f5c1-3032-a229-57ba85abdf3c | -9.25008 | -48.33021 | 2025-07-01 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e011bdc-b29a-3b30-b573-99a3f9936051 | -11.1436 | -53.92728 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f861a4d5-2dc4-3dac-acf4-f103238669dd | -11.20326 | -55.92234 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e01697a6-7751-3a28-9eb6-91c9c4607f00 | -8.02512 | -46.3283 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77c43c9d-7461-3d58-a170-6baa17e32b0c | -10.87639 | -53.77397 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c3dd15c-3890-35e2-8908-553881518019 | -8.88813 | -50.1731 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b68a6f94-3657-33cd-a202-884c45074fd2 | -10.2964 | -57.13886 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff7c3e9d-acee-3f83-a686-8595a11da4b9 | -11.20104 | -55.91294 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea551e51-9119-3a4f-b8df-98378f7b424d | -7.31913 | -46.73507 | 2025-07-01 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f1dc93c3-ad8d-360e-b321-5ed40636e41a | -6.29286 | -43.67851 | 2025-07-01 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 458109a5-9839-3e2d-b23c-5628971221bc | -10.12325 | -52.34778 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0e8350c-f173-3e5d-aa6f-f537a7bd9dac | -10.12826 | -57.77923 | 2025-07-01 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91f814f2-8aab-3f50-8fc7-ed1a19396de9 | -5.65434 | -46.59713 | 2025-07-01 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef01d1e6-27ba-3043-9a0f-15d7cf78b1a2 | -7.55019 | -45.83109 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 46a6aea2-850e-3ae0-8d58-29d3ec6b8a6f | -10.87767 | -49.54744 | 2025-07-01 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf8b6f88-4702-34a6-b4a7-4452f7921086 | -10.06202 | -49.65823 | 2025-07-01 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 548b8d28-ee60-3caf-8103-ce522f8cdeb3 | -8.30834 | -55.10435 | 2025-07-01 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4e8f4365-4840-3e2e-a2dd-c8abe13ebedc | -8.3104 | -46.31271 | 2025-07-01 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 485c8523-e79a-3f73-8132-dba16f043cb9 | -10.30224 | -57.12896 | 2025-07-01 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a1f2d0c4-462b-3394-9e52-9a97b052359c | -7.31988 | -46.73008 | 2025-07-01 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5654e0c1-d589-33ce-bd0f-760f2cfe0afd | -10.1271 | -52.34482 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bd39bcf5-ff35-31be-8af2-3b5f53e69ac4 | -9.24067 | -46.61255 | 2025-07-01 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a9a0a80-56e7-323a-96bc-230480868788 | -9.08589 | -59.47335 | 2025-07-01 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dae377ea-e552-3327-9441-c7862028d243 | -5.5706 | -45.22092 | 2025-07-01 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 84bd4052-cbe5-326c-bbea-4084b62f837e | -8.97669 | -49.86282 | 2025-07-01 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d7bb4c6-9b8f-3f36-b140-3358063e7a76 | -10.88588 | -56.4483 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eeeb8173-6194-362a-9398-82a14e20b6e5 | -10.87082 | -53.76549 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e006038f-4679-3105-8c01-861a80d643dd | -10.12473 | -57.77461 | 2025-07-01 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9555d17b-247c-3d84-a402-cd28ef37bebc | -11.20695 | -55.92299 | 2025-07-01 04:46:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7c5c233-3e61-3a00-94c0-e98bf681a903 | -10.55534 | -47.25576 | 2025-07-01 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fe3356a-eec9-3a9f-b303-f749cf92d4a2 | -12.02477 | -47.77151 | 2025-07-01 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84961c15-2091-31ff-9c50-e6a6bbe57e25 | -10.88207 | -56.44765 | 2025-07-01 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e3d31cd4-f861-3647-bd45-7d6ef2f34241 | -9.24215 | -58.76197 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c0cdcc4-a23d-396d-b565-196f67ee35be | -9.24838 | -58.75331 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed93313f-2b1b-3eb4-b230-362884f15736 | -9.38964 | -57.52273 | 2025-07-01 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5450690e-a346-3cdc-83aa-0fe07b51ad88 | -9.24299 | -58.75724 | 2025-07-01 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22a66624-a66f-311f-9a32-1b615fe5a88b | -10.87698 | -53.77029 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c6225d6-7aff-3233-ae88-f2caf7fcc796 | -10.28458 | -52.83434 | 2025-07-01 04:46:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2a7e37a7-4233-3f3d-845a-eb5a984eedd0 | -10.87099 | -53.74296 | 2025-07-01 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38c7b0bf-4da4-3cde-b73d-fe99c1d682ae | -14.38029 | -50.32539 | 2025-07-01 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0d05dc5d-2656-3131-b64f-6268932ef74a | -11.83186 | -62.76972 | 2025-07-01 04:49:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe45576b-e896-38d8-8bf4-e5c4bc95e643 | -12.26827 | -54.53127 | 2025-07-01 04:49:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5bb667d6-2ad0-3528-a558-b082a716fe48 | -17.93701 | -48.92059 | 2025-07-01 04:49:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a69c46d-4445-31d2-ba77-31fc5bf2838d | -14.4433 | -48.86994 | 2025-07-01 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0483d72-8a59-3d9d-baaa-ca525e3d8162 | -13.00892 | -53.42304 | 2025-07-01 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbf15d1e-3349-3835-a0fe-fccddd546dcb | -12.62262 | -54.21339 | 2025-07-01 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fdf4606-d2d0-34c6-94a4-6bd08c3b1b76 | -12.82984 | -47.36652 | 2025-07-01 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df63c715-bde8-3784-86f2-23e0328312ea | -13.01223 | -53.42358 | 2025-07-01 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f1a5fab-2fa9-3f5a-9edd-b73452a2f76d | -13.00948 | -53.41948 | 2025-07-01 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51aab437-d25a-3d7a-a1d7-e2beb4c32906 | -15.0138 | -47.60291 | 2025-07-01 04:49:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e660079-db26-3f2d-b38d-39b9728e4ea6 | -14.49143 | -46.98122 | 2025-07-01 04:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8bb6be4f-d45a-3dd8-a026-0faa679ff0de | -13.0128 | -53.42003 | 2025-07-01 04:49:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a64013e-adfb-3690-94de-654b5a8de72d | -18.44707 | -47.34982 | 2025-07-01 04:49:00 | NOAA-21 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bef727d2-657e-38c5-96b5-280b40d2b86b | -14.22357 | -45.50183 | 2025-07-01 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c881ae2-c526-3533-b43b-86709f96f59e | -16.28433 | -48.63624 | 2025-07-01 04:49:00 | NOAA-21 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffb4dfb4-cd02-3fb1-a06a-403b818cc4bc | -13.41401 | -47.82991 | 2025-07-01 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README12.md)
