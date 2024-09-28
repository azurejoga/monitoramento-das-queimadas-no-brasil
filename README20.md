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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d991abc8-0d1f-3613-a3e0-83734e50fd87 | -10.5721 | -46.024101 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3399601a-e7e3-302b-908b-4f8b16acbf78 | -10.5755 | -46.037601 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 622c8f14-022e-31df-ace8-77eda3c8f2ea | -10.5789 | -46.051201 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bccb7926-2e55-303a-85e9-9dfbce72b1c3 | -10.5823 | -46.064701 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2eff0345-e61b-33dc-adaf-2ce6bb4c99a8 | -10.5857 | -46.078098 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 15d1c50b-3dde-3ca9-b237-9171da220ea7 | -10.5624 | -46.026501 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8682bdc1-912e-3ba2-a9f3-9b422cdb0b74 | -10.5658 | -46.0401 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 492675f4-b4f1-36f1-98b9-0500d113cd55 | -10.5692 | -46.0536 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa5fd32a-b715-3c2b-88ee-bb9d5b058a5b | -10.5726 | -46.067101 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 394266aa-6db3-3965-874c-7815c00a01e4 | -10.576 | -46.080601 | 2024-09-28 01:07:58 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8614bebf-16ae-35bd-8f74-5e70494d727e | -13.2875 | -58.184101 | 2024-09-28 01:07:59 | METOP-C | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| df4ffb5b-62a8-3c16-8fcb-f13be45ba2d9 | -11.0165 | -50.183701 | 2024-09-28 01:08:07 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f04a609-0e2c-3998-beff-597ea4a6495f | -11.0067 | -50.1861 | 2024-09-28 01:08:07 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce29ae2-27e7-3d96-b719-657543657253 | -11.0086 | -50.193901 | 2024-09-28 01:08:07 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 822ed950-3a5d-34e8-ae44-a6cd2074e860 | -10.9914 | -50.164902 | 2024-09-28 01:08:08 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fe41cdab-1111-3b66-a08c-9ce15df1c2d8 | -10.9932 | -50.172699 | 2024-09-28 01:08:08 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ecf9fee4-13f3-36e5-82c9-57be8df8754a | -10.9834 | -50.175098 | 2024-09-28 01:08:08 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ef8e08a-ba03-306e-8bb9-439b1a5aae36 | -10.9853 | -50.182899 | 2024-09-28 01:08:08 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8e6d4ea-e282-3ec7-b368-fa93b6ff7c8e | -10.951 | -50.124901 | 2024-09-28 01:08:08 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e16337c-5eae-3793-a24e-0604e0598577 | -10.7638 | -49.8577 | 2024-09-28 01:08:10 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5709176f-472c-30f3-9b8f-8f7cea8702ec | -10.8853 | -50.459801 | 2024-09-28 01:08:10 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1174219-e00b-3a21-a08f-3ad14db15922 | -10.6425 | -49.912498 | 2024-09-28 01:08:12 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73a5efe0-967e-388d-8999-7dcff9a44662 | -11.6776 | -54.441299 | 2024-09-28 01:08:12 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be492d5c-1fa4-350d-a17b-7f1ad0661a86 | -10.6327 | -49.914799 | 2024-09-28 01:08:12 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b57906c3-fe44-3dde-925b-47d02579d36d | -10.7116 | -50.952801 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d02abcb0-d5c4-3e1a-91f8-c66ffb5e01ab | -10.7133 | -50.960201 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5742441b-81d8-3fee-b0aa-539d11c5a42a | -10.715 | -50.967602 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ca4ae64a-2f85-3205-bd19-638f0f2efd2e | -10.7167 | -50.974998 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbb78fca-fde3-3563-86e0-4fbf794a49e9 | -10.7035 | -50.962502 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f76e160-ecea-38e1-bec7-2e1ddae3b37c | -10.7052 | -50.969898 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dac07887-c4a5-3b00-b185-eeb99adcdc0f | -10.7069 | -50.977299 | 2024-09-28 01:08:15 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c485a0dd-e80a-317c-95a4-34c05fb463e3 | -10.6084 | -51.085899 | 2024-09-28 01:08:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7336d27-7a7f-33c2-aa16-d4f31eb53169 | -10.6101 | -51.093201 | 2024-09-28 01:08:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 443e525b-c453-3223-9bf5-e7953368d0a7 | -10.6118 | -51.100498 | 2024-09-28 01:08:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 841d4b1c-5f6e-34ad-b7ea-aed6e1554110 | -10.5986 | -51.0881 | 2024-09-28 01:08:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4badbd7-77f2-3e5e-9705-7f44065e3e93 | -10.6003 | -51.095501 | 2024-09-28 01:08:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5a8652b1-a41f-3b3e-b311-98e4d8e6cc74 | -10.602 | -51.102798 | 2024-09-28 01:08:17 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6eda19fd-11fa-314a-a624-fdc9f93c12b5 | -11.1873 | -53.898499 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65a8e6cc-7e51-39a3-8e18-1ae414582d54 | -11.1889 | -53.905602 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67c4f77a-d647-326c-aeec-555e86439d5e | -11.1905 | -53.9128 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6c3380-2fcf-330f-8cd6-98b6aae2ac9d | -10.5399 | -51.101898 | 2024-09-28 01:08:18 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd56a255-9de1-32ab-90a6-07add55a8951 | -11.1759 | -53.893501 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46404725-94b8-3271-a19e-aa17aa9611f6 | -11.1775 | -53.9006 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b087286-0cc0-3c1f-8bdb-0f57938ef6cb | -11.1791 | -53.907799 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69551113-5551-3062-a9e9-65e30642d9f8 | -11.1807 | -53.915001 | 2024-09-28 01:08:18 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1923dce6-d0b8-380d-be7a-e3ba2c2e5237 | -10.4574 | -50.7929 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f03c40b-0189-3135-be4b-432b3b87edab | -10.4592 | -50.8004 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1f181573-3f40-37ca-8be1-5217f547f9d2 | -10.5301 | -51.104198 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6e062a3-3836-3f53-8b0d-3a06db91864f | -10.4476 | -50.7952 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 18da3bf1-c4d2-3d21-8c76-4d8617f5406f | -10.5076 | -51.1404 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cfe30ab-974c-3c03-bb42-5c5e10c9bcbb | -10.5093 | -51.1478 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bec6acac-1584-3ca6-8ab7-3cb020aac00c | -10.4995 | -51.150101 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ef1d0e9-3aa7-38ba-8744-70ce3724d397 | -10.488 | -51.145 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b780b34d-6d3e-32b4-9194-2f9ff2b16428 | -10.4897 | -51.152401 | 2024-09-28 01:08:19 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11fd8a49-267a-38f6-a02e-f0799de9ff21 | -9.7231 | -48.020802 | 2024-09-28 01:08:20 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cffc924b-611a-3329-a6ae-9267e2d5b5c3 | -9.7256 | -48.0313 | 2024-09-28 01:08:20 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad2f38ff-b726-3035-b806-305600c04e93 | -10.4752 | -51.178799 | 2024-09-28 01:08:20 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b85500ef-ab65-390d-ae75-9d7983785d84 | -10.1461 | -49.997002 | 2024-09-28 01:08:21 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6d73f5e0-acbd-3768-817d-aea6a46a1bb2 | -10.148 | -50.0051 | 2024-09-28 01:08:21 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 64ae08fb-d92d-3aa2-aa94-be6512cdc8f6 | -10.1363 | -49.999298 | 2024-09-28 01:08:21 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6f34b28-e091-3cfb-a473-042c0d651f4f | -11.2244 | -54.7631 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 261f351e-f2ec-303b-b7aa-54386f1774a4 | -11.226 | -54.770699 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 633aabf8-2dc8-3223-81f2-358c14a6dcee | -11.2277 | -54.778301 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f0cb208-f7ba-3580-9ecc-c34dd3982fc4 | -11.2096 | -54.742599 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3784638b-62ef-3e6a-83f4-ad3a7a398999 | -11.2112 | -54.750198 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 752e11b3-c8fe-3271-b91b-201564bdcf24 | -11.2129 | -54.757702 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf0f86cb-58fc-3009-94b1-06a65cf1e99f | -11.2146 | -54.765301 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32633180-9e81-3840-91ca-302150ed675a | -11.2162 | -54.7729 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d086689f-b4c8-3a95-b442-251fba94d802 | -11.2179 | -54.780499 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1d05d7c2-7062-33d8-aa0d-84da659fc148 | -12.8406 | -62.7243 | 2024-09-28 01:08:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 97288f87-b504-344d-8fbd-3ed53b33c224 | -12.8452 | -62.749001 | 2024-09-28 01:08:21 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd6122e4-c507-38ba-9128-381ea6cd235f | -11.2014 | -54.7523 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 167d00ce-0012-3160-bd49-daf750e2e5a2 | -11.2031 | -54.759899 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 779ea246-a2f1-3250-9e63-4e20580725e4 | -11.2048 | -54.767399 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81c35d00-f84e-3196-a184-b7acdbb94edb | -11.2064 | -54.775002 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 730a05b7-4c51-312c-92b8-007f7ec98120 | -11.2081 | -54.7826 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07d78628-cf82-3f10-833c-e930eb783be4 | -11.2098 | -54.790199 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 865cc43e-45c9-3d54-ad1a-eab7e05ec0b5 | -10.107 | -50.006302 | 2024-09-28 01:08:21 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 34599795-118c-3660-8f3b-37d8f4cad79a | -11.1835 | -54.764198 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d36b892-3191-3f27-99a4-39ab02716513 | -11.1852 | -54.771801 | 2024-09-28 01:08:21 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d6d4377b-f5b4-3688-8956-0392c0d68fd5 | -11.1737 | -54.766399 | 2024-09-28 01:08:22 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d13e5218-c5fa-300f-bca0-a252fdbcf37d | -11.1754 | -54.773899 | 2024-09-28 01:08:22 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 24467c4e-a122-3663-a20e-8af5ebcb481a | -12.7775 | -62.7617 | 2024-09-28 01:08:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35913ffa-4af2-3006-996b-76fa3a8381be | -12.7678 | -62.7635 | 2024-09-28 01:08:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3312ab9d-7dde-38ab-937a-4789ffa3e852 | -12.7724 | -62.7883 | 2024-09-28 01:08:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 915dfa71-1f33-399b-8878-dab266aa822b | -12.7581 | -62.7654 | 2024-09-28 01:08:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac1c2d2-2b5c-368c-ba8f-ddf6e8c0f5a5 | -12.7627 | -62.790199 | 2024-09-28 01:08:22 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1e1ba019-02df-3009-925d-9c64b65c9fc1 | -12.7578 | -62.816799 | 2024-09-28 01:08:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6894bb0e-cd64-3551-a8fc-89e828ed00ad | -12.7625 | -62.841801 | 2024-09-28 01:08:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 80aa3a8e-566d-3e6c-9716-2886adc0480d | -12.7528 | -62.843601 | 2024-09-28 01:08:23 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d8ce1f95-ffd4-340e-9e11-62f2f018d39a | -9.7586 | -49.107899 | 2024-09-28 01:08:23 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9eaf2bf-3a1e-33d1-b7ea-b62dd0918447 | -9.7608 | -49.116901 | 2024-09-28 01:08:23 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 10f8769d-b6c8-337e-ab1b-7e0121f45a9b | -9.8993 | -50.132301 | 2024-09-28 01:08:25 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c9a6c78e-d343-3417-a1ef-48db7d80b4f9 | -9.7708 | -50.069302 | 2024-09-28 01:08:27 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 619f7a6b-cc16-3eb9-b0b7-2c0ed4ed6bd5 | -10.5709 | -54.225498 | 2024-09-28 01:08:29 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f15f458c-c5d7-3a99-a275-cdae2de98daf | -10.5725 | -54.2328 | 2024-09-28 01:08:29 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d36c3f9-79df-3de9-aaa0-df5c77b15e7c | -12.0068 | -61.215302 | 2024-09-28 01:08:30 | METOP-C | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a75396ce-3665-39dc-b5ce-ec612879fd9b | -11.9971 | -61.217201 | 2024-09-28 01:08:30 | METOP-C | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8036df0-d5a6-3fdc-8c53-8519d0ec0438 | -9.5674 | -50.126202 | 2024-09-28 01:08:30 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ebe82b0-ec67-332c-a870-5fa423ebef06 | -9.5612 | -50.187302 | 2024-09-28 01:08:31 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README21.md)
