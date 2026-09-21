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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c92938a-8792-3cc6-aa62-7bf4ddb446f0 | -10.47525 | -50.35363 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| da721ad1-ba91-3d56-a29d-ea652d7615c9 | -11.02561 | -54.14579 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| a258dd35-b8a1-3250-a5b0-19f89a4d18a7 | -10.77737 | -50.80955 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d7122844-3b45-3f09-86d2-eed51d84091d | -12.30277 | -50.17077 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 1564a98f-913b-38b4-af77-0c1520f63be0 | -10.98317 | -50.59897 | 2026-09-21 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d42a8f73-010e-3ead-91ae-e00801f216cf | -11.1358 | -54.01406 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 72a5c5f0-5281-3720-ad3d-e9bcaf357a9f | -12.27302 | -50.17551 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 98deecc9-52f8-3325-8050-0c021da15ffb | -11.93516 | -46.50148 | 2026-09-21 00:20:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3e60045b-2930-391d-aee1-5497cc10e26d | -8.83669 | -50.49634 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| d2a6c0a6-71ec-3d2f-8c31-6d1202e12fe0 | -11.68061 | -43.42886 | 2026-09-21 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 6499a714-ae4e-302b-b14f-a80d06a49b55 | -10.06074 | -50.25816 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d80ed383-71b1-3546-86b7-8a843df9f316 | -10.35064 | -50.20652 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9fdee820-e235-3f3c-82ee-317ea86b9822 | -10.91679 | -53.95727 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 8fef75cd-8998-3dff-b6c2-9f27f01f3f9d | -10.53775 | -54.49003 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 52603a11-d2eb-34a7-ba61-e649413391d3 | -11.36353 | -51.4368 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7348be48-da97-337d-9d8f-f1d53cf48b9d | -10.43133 | -50.33615 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 91482d69-3f93-3567-9134-29c840818073 | -15.45288 | -48.45165 | 2026-09-21 00:20:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d88b951a-31f8-3264-ba7a-60006c610a4d | -11.78676 | -49.80576 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f8c8fdbe-0fa0-3ddb-ae3a-721995890bf4 | -10.73347 | -50.71398 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 40abc3a0-c8e1-3da7-8c6d-14d52c9937a6 | -10.72214 | -50.7728 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 91f3493f-f66f-3ba3-9223-d7b0bbee66bf | -10.4312 | -50.32965 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4dec4a7d-6345-3d19-9840-5d014d2c0d16 | -9.0487 | -48.77325 | 2026-09-21 00:20:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 26.5 |
| e7628888-80b7-3b60-890f-ebdb30dda8ce | -11.25617 | -54.13995 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e3896906-6b67-371c-bfe0-73f4828f6dc3 | -14.66923 | -54.4757 | 2026-09-21 00:20:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6943741a-cd5d-3314-8bdf-c0a31dc783b9 | -7.38183 | -46.0463 | 2026-09-21 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 6019fd06-1774-3497-92f6-65b64edccf6a | -13.27025 | -51.80022 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 37c37ba4-b4b6-37ce-8d09-78fba9852ea1 | -7.41538 | -44.78454 | 2026-09-21 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 030f3b3f-8346-3e4b-8c55-4d8f279e0f01 | -15.07385 | -49.57966 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| eb653772-5378-3955-b221-a6644b91f87e | -14.61421 | -52.10914 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 15998c9f-07e8-3c56-8c89-a6421a0a66df | -11.04463 | -54.90065 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 07110dcd-8386-3311-b5c4-b91c44e42fd0 | -10.4551 | -50.35678 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| fca629a3-a476-3d26-8474-eac312ac2f20 | -10.891 | -54.09765 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3fc0e7e4-6c59-3748-8c45-bd7ac06d59a7 | -13.05492 | -50.62191 | 2026-09-21 00:20:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b6f06e64-8d50-3a2a-973c-2f6878445fed | -11.04572 | -54.16124 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 5f970dc3-8731-34e3-a680-be9b6eeeeccf | -11.04469 | -57.24445 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3b37a551-0228-3b98-8e52-454a996c9bc6 | -10.48666 | -50.98475 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 02f872c2-f620-388c-8a89-7991a9e135f5 | -10.87273 | -53.96358 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f0849e32-8411-3fd4-8fe2-f33816dcda73 | -10.98149 | -50.58767 | 2026-09-21 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2c85c398-e9f2-3a32-892c-5b27d85e1688 | -10.80344 | -50.83287 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a8b0f190-70f6-33fe-a3fb-06e563f580c0 | -11.04713 | -54.9193 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| e23689df-da49-3940-ae7b-6c2fbd43627b | -8.26768 | -50.87295 | 2026-09-21 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0831c11e-9c22-3ce6-8114-e4f70bf4f98c | -11.37285 | -51.43538 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 86c502e8-3fcc-3a14-a70e-2987795b3bc4 | -12.30753 | -50.68984 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4823b1ca-2a66-358e-9639-50e929b209cd | -9.67007 | -54.33885 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad2efbb4-1773-3e69-8949-59af4ea4c237 | -8.44397 | -46.39221 | 2026-09-21 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| eeb0e2c5-9763-3f1c-8dfa-625428c6b68b | -10.41598 | -53.79652 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ce21aae8-d7b2-3158-a6f0-d41f8dfd7717 | -13.92746 | -47.84726 | 2026-09-21 00:20:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 82d3a230-b3f8-3886-84dd-071fcc6c482f | -11.03296 | -57.23356 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ebd59570-7fa2-39b1-b350-5fdebb44d18b | -8.18953 | -54.77006 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5e356eee-a4a6-30e5-828a-6938b7ff9465 | -7.7381 | -49.39258 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 7f72709a-5871-324e-bd51-6ef7ef1bf9a5 | -9.67767 | -54.32869 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5d32cac5-6439-387b-97fe-275fc559fb75 | -10.4775 | -51.28802 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2a184731-0128-3857-9844-585ee9c3b857 | -10.46339 | -50.34332 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e8af8667-f5c0-3903-a98f-c2fbdfc266dd | -11.31614 | -47.29531 | 2026-09-21 00:20:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a29379e6-f3a4-3ab7-9759-79a00d2e7703 | -8.44801 | -46.41812 | 2026-09-21 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| f2db73e4-d9d8-35ad-b55a-aa9c2d170bb8 | -8.18862 | -54.69772 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25f8bb33-55a4-3186-b595-6a92c0babab7 | -10.04867 | -50.24755 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8c2506e0-b89d-3ab7-aac7-12b2b35f65cf | -11.09396 | -51.05705 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f6e45e49-e2f5-30ef-98d6-4a26a3ad7673 | -10.69414 | -54.15351 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 95a3839d-07bf-3efa-913a-960dcaebd5b3 | -12.54539 | -50.07787 | 2026-09-21 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 7435b70d-713b-3889-9c87-84521a690e9d | -11.3438 | -51.36729 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 1cb31eb0-d612-3a89-b8a4-9561b8896740 | -9.68893 | -54.34527 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 19536674-035a-397d-ad19-5883754612c8 | -12.31442 | -50.18074 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 9e6f1b3e-7a2b-3367-8adf-4900a896a3d1 | -16.32541 | -53.85028 | 2026-09-21 00:20:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c28a8cd8-0e56-3ed0-babb-f4ac3142c897 | -10.88276 | -53.97126 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fe7072a7-76eb-3e59-a621-4f45b9787461 | -12.36468 | -43.86125 | 2026-09-21 00:20:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| e0d774af-ae29-31d2-ba41-c30b74177e52 | -10.22173 | -59.3916 | 2026-09-21 00:20:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 07da7565-d725-3063-af26-26ec85c1b947 | -9.93372 | -53.9839 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5662cd28-99ab-33e0-852a-88b40cf14036 | -10.48143 | -51.28107 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bbc32ac2-9ec3-3a9c-9c5a-47af5170ab7e | -10.86055 | -57.15815 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a88a7015-4777-300a-ac1b-3393dca48a5a | -10.4211 | -50.33123 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 7439f902-2fba-3dbf-a043-27c9b299164f | -7.06769 | -49.90758 | 2026-09-21 00:20:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| d289e794-b7f1-356e-9b26-9484075253a4 | -10.74492 | -50.79196 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| b6d91455-6ea0-3856-80c4-96080a7f4150 | -10.45689 | -50.36864 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f6274364-6ff8-394d-b8c0-24c6ec2e3ca5 | -8.77859 | -48.73524 | 2026-09-21 00:20:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 13.4 |
| de101764-b898-354d-8ecb-9203e98a98f3 | -11.78863 | -49.81814 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 8b2819cf-2093-350a-a4b4-a837255deb6f | -7.88522 | -44.85606 | 2026-09-21 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b43a22f4-eaf8-30b8-ac99-ec346072a928 | -9.02768 | -51.53067 | 2026-09-21 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 3f8277e2-ae54-3ca1-ad1c-c9ab16231535 | -11.32993 | -51.33816 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8058d84c-e4a3-3afc-b774-89aefb733823 | -7.38284 | -51.76702 | 2026-09-21 00:20:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df9f541a-ef31-3fe1-8ca5-1f2532a3149c | -11.12575 | -54.00638 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 8549558d-c045-339f-8f1a-cf7c7b2c8613 | -10.38394 | -48.92004 | 2026-09-21 00:20:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 03afea95-1333-3708-8969-58ab49f757be | -9.4316 | -50.15732 | 2026-09-21 00:20:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bd546a8a-bef1-32de-9c11-4c37b79f1685 | -11.78817 | -51.12103 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a8226ad3-48c8-3e53-bf1d-a27e613c0b57 | -11.00919 | -48.26943 | 2026-09-21 00:20:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3719765f-11ca-3266-accf-034fc09c9229 | -9.66886 | -54.32996 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a7a49adc-d622-38e3-bfee-6a759d61e313 | -10.92682 | -53.96493 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 910dba18-5bcc-343b-b74d-b0c918ba3bd7 | -10.44142 | -50.33458 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 48f5db41-d2b9-3117-997f-94c4c8e8b715 | -8.17065 | -54.76366 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 5033dddb-de62-36ff-bd33-cf8e4fe36b07 | -12.54008 | -50.04284 | 2026-09-21 00:20:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a3f17f65-daa0-3f95-93b5-4775864a0d59 | -9.67646 | -54.31979 | 2026-09-21 00:20:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ff30427d-0e65-3f8b-b8de-a733bb163a68 | -10.71237 | -50.77432 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 44abc242-c2a1-3664-8996-b37b1079db70 | -8.18983 | -54.7066 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 408efcff-3719-3196-97c6-4932b44e65b4 | -11.25739 | -54.14895 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| afb0b26d-7186-388f-a621-a05ec0fa2467 | -8.34306 | -50.75835 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 14ccb6d3-c7b8-339e-8b1e-3e274de42c97 | -16.03427 | -52.98315 | 2026-09-21 00:20:00 | TERRA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5f6419c8-7b52-3744-aa3a-078ad6527e7c | -14.75933 | -48.43116 | 2026-09-21 00:20:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 975004e3-3a21-30f5-8491-ddd83a536319 | -7.38436 | -51.77764 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a4bbba8a-a352-3e3d-8993-4e5245753544 | -12.88603 | -52.08124 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3fabf084-0171-39a6-ac5e-16b1118657dd | -14.17305 | -51.79294 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README4.md)
