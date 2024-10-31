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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 868bd4fe-d62f-32e1-9766-92e49af28915 | -24.024599 | -54.0877 | 2024-10-31 01:21:46 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40d3cb22-c8d8-3bf1-8348-9b2a37d87949 | -24.0263 | -54.0952 | 2024-10-31 01:21:46 | METOP-C | TERRA ROXA | PARANÁ | Brasil | 4127403 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8fbf4f9d-c176-353e-8372-431f2fe05b00 | -24.0133 | -54.082699 | 2024-10-31 01:21:46 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ede9530c-7cd0-391c-bbca-cfdaedaca562 | -24.0149 | -54.090199 | 2024-10-31 01:21:46 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e49709e-0c51-3ca1-9bbd-658bee952134 | -24.0165 | -54.097698 | 2024-10-31 01:21:46 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 45839be7-92d1-3a3c-a591-e8cf1d5af903 | -22.3454 | -48.217701 | 2024-10-31 01:21:50 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7c241e21-2d9d-32b5-9df8-5b3e3d902bdb | -22.3486 | -48.23 | 2024-10-31 01:21:50 | METOP-C | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f1c823d3-62a2-3787-972c-749c99514041 | -20.352301 | -49.986599 | 2024-10-31 01:22:30 | METOP-C | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c0fea3b1-639d-3b7a-90a7-e5d58895ffd9 | -20.3549 | -49.997101 | 2024-10-31 01:22:30 | METOP-C | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4f24e1b3-556e-341d-a970-9c0fa91b6268 | -20.3575 | -50.0075 | 2024-10-31 01:22:30 | METOP-C | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1f47df2e-86ce-3add-b92a-983991e55244 | -19.6654 | -56.630901 | 2024-10-31 01:23:05 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ceb95725-25ea-3bc9-902b-ea2b65f806c7 | -19.667 | -56.6385 | 2024-10-31 01:23:05 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2ef80a4a-c991-3440-ba7b-fd9e2b83c0c0 | -19.6653 | -56.678799 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8a374696-0560-3402-b179-0f9e9935cd60 | -19.666901 | -56.686401 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4e4ab3fc-dd3a-3e61-959a-47e04a70bc4c | -19.668501 | -56.694 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 41cb660e-4bd1-37c1-9e41-c08406fdaf43 | -19.6555 | -56.681099 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b35f3d44-1aab-34d3-b0eb-b1acd97744ef | -19.657101 | -56.688702 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 41d7c152-1239-3c82-a889-e3c3497d12bf | -19.658701 | -56.696301 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58543077-b2b0-31aa-b963-fae3ad8cf4d3 | -19.6604 | -56.703899 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 87fc780c-6ee1-3cfa-8f2f-4599bbcabe8c | -19.662001 | -56.711498 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 98ebfeb2-09f9-35cc-9118-14560e9a7870 | -19.6458 | -56.683399 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4e7beca3-ec7a-3d11-bb9e-f45e2ee6cd6b | -19.6474 | -56.691002 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 55350317-d91f-3a4c-ab88-00b9864c7368 | -19.649 | -56.698601 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e805b0d2-5a46-3266-aa58-c84076f903c6 | -19.6506 | -56.7062 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f70fc38b-10c3-3e4a-b6df-1af4c6a30878 | -19.652201 | -56.713799 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 497c6280-62e3-3600-8ef4-0ee2d01d783d | -19.653799 | -56.7215 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a57a16ac-cbf1-3a93-943b-c7985564b7a8 | -19.618299 | -56.6021 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8bdde50a-f37e-3a76-bc3c-ee2790121e8c | -19.6199 | -56.6096 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d290c313-3f1b-36c5-867f-ce418fd06a5e | -19.6215 | -56.617199 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f316e204-2d41-3eab-b9dd-4f74551b4b09 | -19.636 | -56.6856 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2bfea25a-fe0f-3b80-8240-c2e0d839110c | -19.6376 | -56.693199 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9b9327cc-1f65-3edb-81d9-081c9056f76f | -19.6392 | -56.700802 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7c9b9905-41f4-3ab1-b5d4-a49ccc84c7b9 | -19.6409 | -56.708401 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8be66f2e-ada4-3d4f-b657-cfe7f640973b | -19.6425 | -56.716 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eac75abd-069f-3ed2-9d08-64a571cc6190 | -19.6441 | -56.723701 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b0540f7e-067b-3f47-808c-47dd6bd66c0a | -19.6457 | -56.7313 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 16267b4e-6ab7-3b0f-84d5-96a77d856c90 | -19.6262 | -56.687901 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b961c126-c0b3-3f61-986b-ffc060732d24 | -19.6278 | -56.695499 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2f32d4b9-a1df-3b2a-a4c3-c886f5374c28 | -19.6294 | -56.703098 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b3d81613-01c6-3ae0-9a04-54163f5af102 | -19.6311 | -56.710701 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cbdb1a4-b3ce-3fd1-9543-58240357393c | -19.6327 | -56.7183 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ae7e6a3-8969-3d0d-a74c-41eab34a63b5 | -19.6343 | -56.726002 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1df1ac99-5789-3cf2-be37-8c46a3eccf7c | -19.6359 | -56.733601 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e2507f31-dfe7-3541-87db-4d22f40f5e01 | -19.637501 | -56.741199 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 667ed9dc-15d5-33a8-95b6-22d337de863d | -19.6164 | -56.690102 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 03a2f5f7-fc9e-345f-b1d6-da9f54587b2c | -19.618 | -56.697701 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a7c056fd-16b3-399f-b22b-88be732976a1 | -19.6196 | -56.705399 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b35bb26d-a620-3554-9c62-6db441627ac5 | -19.6213 | -56.713001 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c834dc61-4683-396b-8301-f6bf14fd2179 | -19.6229 | -56.7206 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cfe1baf5-5a19-35d1-9545-20ed9bffed4f | -19.6245 | -56.728199 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 48e6f79c-c8ea-34f0-9114-832926c57757 | -19.626101 | -56.735802 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1da9fac9-78a8-3934-9751-64026da6d573 | -19.627701 | -56.7435 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ef32db92-706e-3320-be42-1c61fd25c86c | -19.629299 | -56.751099 | 2024-10-31 01:23:06 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a4b30e5-1866-307f-a38b-eb05a87b6ac9 | -19.605 | -56.684799 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7c7d63de-498b-31f3-bdc4-b5769035c0fd | -19.6066 | -56.692402 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0fed9001-9055-3a4f-8787-bdc9d4ac40b2 | -19.6082 | -56.700001 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 10bb2953-e56d-3355-bc31-14607fd0af78 | -19.6098 | -56.707699 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5900e06f-dd21-399a-bc10-eb83518a3a82 | -19.6115 | -56.715302 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4cf3377a-bd78-3ad1-b291-98b510dd7c29 | -19.6131 | -56.7229 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| eaee1ace-9499-3bf3-9a69-0369d5d427aa | -19.6147 | -56.730499 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dd6edcb7-af92-3eab-86c1-b2775ede0441 | -19.616301 | -56.738098 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5d72436e-d1ba-3aa8-9fdf-e4d741616889 | -19.617901 | -56.7458 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a6b68033-31f1-333f-9c95-f265f24b362b | -19.619499 | -56.753399 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b946467b-f1c6-3af3-9b0e-b4d68c58a12d | -19.5952 | -56.687099 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 08dbc4bb-f604-3c64-a3a8-2e4e37a963c9 | -19.5968 | -56.694698 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cda0b092-a497-3b64-9d4f-849b71d2033a | -19.5984 | -56.702301 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| dbc2106d-d67c-352b-b0a3-ee50c3532661 | -19.6 | -56.709999 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c8cd52ac-9330-39e2-846c-f9bbefd64f9a | -19.575701 | -56.691601 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f02113be-a77b-3d52-9d9e-a71265b12a2f | -19.577299 | -56.6992 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f6556800-e883-3392-9a79-a856afab7077 | -19.578899 | -56.706799 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bcbe0c42-6213-3f58-92d2-4b69ea7a38ea | -19.5369 | -56.557598 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6bf62f00-4b3f-3c9d-9b64-873df154431c | -19.5385 | -56.565102 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 57f8ee9f-ef0c-3181-8785-647d16118251 | -19.5401 | -56.572701 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b988fb7c-4662-3995-b78f-6f22539d068c | -19.5417 | -56.5802 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9ae164c6-5131-398c-aefb-e0970e95d8d1 | -19.543301 | -56.587799 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 62bb6149-673d-36ce-b9ed-a65b027ed1a2 | -19.5627 | -56.678699 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 11e50630-03d5-330e-992d-0a3e7bc107f2 | -19.564301 | -56.686298 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9df8a751-8c41-33f2-94d1-20ff8f7839f8 | -19.565901 | -56.693901 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5c2071db-2b32-3c40-87de-c9e3b00fe991 | -19.567499 | -56.7015 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| fd99ab67-4401-3ace-b2f1-44e74c83258d | -19.569099 | -56.709099 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1df898bc-98e0-3693-b08a-e7db37adb82c | -19.5707 | -56.716702 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 08a70e10-90ec-3393-aafd-c0280b1897b0 | -19.5287 | -56.567402 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 229fda15-4029-3a1b-a2fa-1778fec41abf | -19.5303 | -56.575001 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4e94cb2a-3708-3b4b-813e-a0e57e0c5162 | -19.5319 | -56.5825 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| edd45252-6eb6-32e3-b55b-523c7a4ff47e | -19.533501 | -56.590099 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 975f8337-6d13-3797-9116-b0683e1cc092 | -19.554501 | -56.688599 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 28373b5d-9e67-301d-9fef-9d4af5b59f37 | -19.556101 | -56.696201 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 670344b3-18d4-372e-b29a-b488c95fcbb6 | -19.557699 | -56.7038 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 418b7ec0-7f5e-3c00-8e00-7f55c989631e | -19.559299 | -56.711399 | 2024-10-31 01:23:07 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 65a00e88-e877-35d5-b095-bf9fc219cafd | -19.5221 | -56.584702 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b5a4484b-8842-365b-a4d3-bec3362a7116 | -19.527 | -56.607399 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6eba8086-9631-366a-859f-88ffca3ca818 | -19.528601 | -56.615002 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| db7fcf12-3c6f-3211-9503-e8ef3a8a5ecc | -19.539801 | -56.667999 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| de46ae86-42a6-3b50-b64b-ccbcf80ff664 | -19.5415 | -56.675598 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1ec2e5ac-dbf1-3de1-9729-34e08097133f | -19.5431 | -56.683201 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0f2fed93-cbf4-3f27-b955-f85371692c91 | -19.544701 | -56.6908 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6a2cf446-67a4-3121-b6f0-343ee71a1bb6 | -19.546301 | -56.698399 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b14ca492-8d05-312a-8666-cb1fc84d5cd1 | -19.5156 | -56.6022 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ff79153c-1d15-31f9-bef3-65e0fa1d8b84 | -19.5172 | -56.609699 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 77a13d09-c173-31b8-a4ce-964b264a12b9 | -19.518801 | -56.617298 | 2024-10-31 01:23:08 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README10.md)
