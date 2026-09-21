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
| 7e46b954-0164-3a94-babe-75b0127160df | -10.55223 | -57.45765 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2f8cbcde-9529-30a1-9d80-a1e5ad008753 | -10.88185 | -51.53667 | 2026-09-21 00:20:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eebd7fb7-d0a3-3180-b5b9-fc1c7c9ba3c4 | -11.17058 | -54.12197 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0a64d89e-3d42-3cc5-98af-e8ea9d293907 | -17.01816 | -47.13502 | 2026-09-21 00:20:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 2dc15b98-5b2b-3ba9-8ef5-abad949217d2 | -10.70796 | -54.17258 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5109023f-c460-32bc-a3d0-799aad1fa943 | -10.92438 | -53.94707 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d18fd0d5-4d1a-3b7e-a841-6bc9ab486a33 | -12.31713 | -50.68833 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 21bd3a97-0edd-3061-a14e-106022663474 | -16.01964 | -52.53182 | 2026-09-21 00:20:00 | TERRA_M-M | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 33b51d18-9618-31f1-87a0-e1ef7fd31ca6 | -10.45331 | -50.3449 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a5b38334-e54d-3e3c-896a-fcc46f9f3e84 | -13.92483 | -47.84205 | 2026-09-21 00:20:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ae336d7d-9010-3cb2-aab9-f4d6a8c25b6b | -12.68586 | -50.95201 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 44aa503c-dadd-3013-b812-0be4bf96f955 | -11.79887 | -49.81648 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 62a7bb4d-dfb0-382c-9940-e9b4acab51bb | -10.76763 | -50.81107 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 13ce0706-d4a3-3c92-9c27-9f5bd6d302ae | -8.53905 | -54.69646 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b134a98b-2f25-3aba-956f-a72ae3f65468 | -10.81634 | -50.78574 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4c151d1c-6f6f-3ac8-b9c2-cfc88cd6167f | -8.27335 | -49.50198 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 5676b3aa-e55b-3b7e-8d7c-1ee22e078620 | -10.87065 | -56.21914 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ff518b05-30f6-36a0-9735-bddd768d3386 | -10.77896 | -50.82059 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 5020b8ef-0771-34be-8ad8-dd4e37ea8a12 | -11.01176 | -48.28598 | 2026-09-21 00:20:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 2680b593-f826-38f3-ac8c-aacba55c2f10 | -11.35167 | -51.35567 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 36e4b250-90df-3dbb-bee4-7efbc0cb6f47 | -10.46452 | -51.3325 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e74bc34d-6939-305b-8987-0138a86857d5 | -7.12864 | -48.41942 | 2026-09-21 00:20:00 | TERRA_M-M | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ea5f0f4a-109f-3079-ad9a-608b54586c69 | -13.25221 | -51.80299 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2f32d6c8-f178-3d99-b1b8-4a2a053e7423 | -15.44221 | -48.45316 | 2026-09-21 00:20:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 813fbec3-2056-34ac-8212-fcaeb16cfa12 | -11.28175 | -54.06305 | 2026-09-21 00:20:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 92a78804-be91-33af-b38d-088617b642e8 | -6.83336 | -46.05711 | 2026-09-21 00:20:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 14d1d813-e5cd-39d3-9a7a-8c95be17e2c9 | -9.57585 | -55.13747 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ba4aa227-0434-30c7-a8bf-895e1e184450 | -11.95206 | -46.50465 | 2026-09-21 00:20:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| dbf10bf8-25c0-3940-9646-4dcce5453d2a | -7.40047 | -46.16449 | 2026-09-21 00:20:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 27401942-5f31-3a18-88e8-2f9217bb6a79 | -9.02616 | -51.52004 | 2026-09-21 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9a3853da-2a5c-3308-8831-d4a0488f6e46 | -10.39914 | -50.32245 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 623926ba-0ad9-363a-b9aa-4cafbf98acb4 | -11.28024 | -54.11819 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 18ca8bab-5ad9-31f0-a894-f3f1e22f4ecb | -12.3045 | -50.18232 | 2026-09-21 00:20:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 45ef2460-e2a1-3fdd-8fab-b57208b52897 | -9.84474 | -48.404 | 2026-09-21 00:20:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c3152fe4-fd8d-3ce4-8c3b-dcb96258bc75 | -8.05797 | -49.3025 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d34121cf-11d4-3d97-aa0d-de08c1674702 | -11.08907 | -51.0528 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7bf75967-0c82-3fbe-b8af-8f18c6b4bdc6 | -11.78665 | -51.11067 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d7dc1264-a3dd-32dc-b7f4-80763ed554b7 | -16.3151 | -53.84178 | 2026-09-21 00:20:00 | TERRA_M-M | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2323249c-fa52-3243-80d1-bd9db80de68a | -7.16474 | -47.46945 | 2026-09-21 00:20:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e625dce7-5f0a-33f4-9899-e557101ae7e5 | -13.27383 | -51.76083 | 2026-09-21 00:20:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1a339987-b68e-3db1-93e0-4fb89969caf7 | -16.18868 | -51.12407 | 2026-09-21 00:20:00 | TERRA_M-M | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0b6e4ff5-7c1d-37ee-8fe0-7bbced8f70b3 | -10.37466 | -50.22762 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 019fb7cd-8e57-3d22-9e2e-17c12e24fd61 | -11.66779 | -43.42612 | 2026-09-21 00:20:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 7f503c0e-c87d-31a8-800c-1080aa0ac6a4 | -11.34081 | -51.34693 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ae78640b-9076-37cf-965f-32a2e217a8b1 | -7.43183 | -44.78206 | 2026-09-21 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 6e751715-9f65-30ce-a496-4e0e50630b05 | -10.42285 | -50.34317 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bfdec592-f4cf-34fe-b20e-adda6f982bb6 | -16.82192 | -47.63391 | 2026-09-21 00:20:00 | TERRA_M-M | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 32.2 |
| 1327b028-86bd-3ffd-9f84-4f8f7d525374 | -11.04817 | -54.1792 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8f522e14-5f6b-33c4-8325-422d972d0de2 | -11.0906 | -51.06342 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 877548e2-1436-3a97-b235-a4ed875ea91c | -14.1744 | -51.80232 | 2026-09-21 00:20:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| dcf416c1-3862-3c63-b911-ce3f2046a084 | -10.58464 | -57.48499 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a04e0f73-bfb1-3b95-8ba0-eb190ba4fc41 | -11.40453 | -47.35235 | 2026-09-21 00:20:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 23a71aee-14ca-3c27-9a82-731d60ae64b2 | -11.36103 | -51.35424 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 559a6c20-fd32-32da-83b1-1ffd3d1aa615 | -10.87066 | -57.15681 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 05fbdcba-9065-32af-ad17-36e7d5f12ab9 | -11.02683 | -54.15476 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 4c67a343-85b0-30d5-9d68-a7642f8f985a | -9.01811 | -51.53188 | 2026-09-21 00:20:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 359257ad-581d-35a3-9c51-ee684be22b26 | -10.73511 | -50.72517 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 243193d3-ca5c-325e-af4e-ff36dd969f92 | -10.56181 | -51.30006 | 2026-09-21 00:20:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3928770d-2423-3ca0-8801-60455ea0569d | -10.54663 | -54.48882 | 2026-09-21 00:20:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7e01d37a-bf92-30ab-b94e-a538e22799aa | -7.71487 | -49.38637 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 1f778d89-273c-318e-b28e-37667a1005ad | -10.76924 | -50.82211 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| a0c01cd2-256f-38e8-90cd-74ba8b132ddf | -15.44437 | -48.4668 | 2026-09-21 00:20:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 67c16015-afa9-3fd6-87a4-b7318f61a8e8 | -10.91042 | -53.97639 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| c4e1b793-b157-3d46-98ee-296ed27c207e | -10.4954 | -50.35047 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1872238e-61e5-3080-8c76-c2c7a360b282 | -11.13457 | -54.0051 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| ed3e237e-9dbd-3790-9d83-3214504b841b | -11.11635 | -47.51662 | 2026-09-21 00:20:00 | TERRA_M-M | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 76ec8ceb-b998-38e0-8e7d-37cc3c9715b8 | -10.87759 | -50.93309 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| b362195f-2901-3947-8c2a-41a86e635c96 | -11.12698 | -54.01533 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| acd1a88e-32ba-349c-9432-6475375b60cf | -11.01555 | -54.13808 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 76a586e8-aec1-33af-88c1-7b45a0202e27 | -9.97998 | -50.26419 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| be4b8ec2-e03c-3958-83fd-1894e444cdf1 | -8.79275 | -48.7494 | 2026-09-21 00:20:00 | TERRA_M-M | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ca0e3470-ba6d-3d14-b71f-33179b0d3ecb | -10.89861 | -54.08745 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f87e14b9-d57b-3ee5-91bd-6ada986d4d90 | -13.89333 | -48.58171 | 2026-09-21 00:20:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8b9907ba-92b3-3dd4-a8d1-06b1e193a15a | -10.86957 | -54.08883 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 86c6bf33-550f-3b82-9678-f46882910190 | -11.10052 | -54.01913 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 465ccdef-e896-318a-bd7a-fef9d4e0feb9 | -10.43314 | -50.34805 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4d80b13d-9557-31a3-a00f-b9c174ba6607 | -8.05979 | -49.30813 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| afc62c0a-3149-3c25-b502-cb058399ad8e | -12.77444 | -52.85797 | 2026-09-21 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f30e6d7c-a67a-350f-a455-6c8886e68e94 | -14.92739 | -49.89672 | 2026-09-21 00:20:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b6f289ce-f9c0-351b-ae3e-99d3bee54ed3 | -7.71706 | -49.40133 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 78769ff9-d5a6-370a-88b1-da498cdc434f | -10.46696 | -50.36707 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ba0673fa-1b4d-3193-8ac3-0e65e4276e71 | -12.1427 | -47.03107 | 2026-09-21 00:20:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| d1872851-c1ff-397d-97cf-dd9c0c57a77e | -12.32951 | -50.68061 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 68b173f6-f49f-3dee-bd98-e5bd65fbad4e | -9.97005 | -47.99117 | 2026-09-21 00:20:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 4d97257a-11b8-38ff-9a4f-194d2bcb44e9 | -8.06036 | -49.31788 | 2026-09-21 00:20:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6f7ebed2-477b-3c9f-89d5-944a36460581 | -8.09413 | -55.35461 | 2026-09-21 00:20:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a74f402-c6b0-37cd-ab74-008a700de8bf | -10.58617 | -57.49747 | 2026-09-21 00:20:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bc71a8cf-f9ac-38e4-86b2-796308ee0a4b | -15.862 | -49.90902 | 2026-09-21 00:20:00 | TERRA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c0480a79-093d-3af7-8a5a-456e7d2ed2d8 | -10.78236 | -50.82488 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.4 |
| dd7d50df-5ade-337e-a61a-bd5f53ec9f72 | -9.05119 | -48.78955 | 2026-09-21 00:20:00 | TERRA_M-M | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 714fb791-3bd7-3996-beaa-bfc07a1f4856 | -10.47831 | -51.26004 | 2026-09-21 00:20:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5cd95577-4c93-3f68-b598-546f7f7ffd5f | -8.18588 | -54.7434 | 2026-09-21 00:20:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ce9b45be-d613-3516-8849-bfc498cf47b1 | -10.05148 | -50.25296 | 2026-09-21 00:20:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c7fa73bf-2c6b-3d7d-ba5a-4b18c1061869 | -10.70095 | -50.76471 | 2026-09-21 00:20:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 235.9 |
| 98a071a4-f178-3f44-983c-941535253268 | -10.81227 | -50.14109 | 2026-09-21 00:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 2d604b09-34f6-324d-b433-9ac8a83de2fd | -11.0841 | -54.03062 | 2026-09-21 00:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc64975a-91f8-3bc0-a626-df9d7340908e | -12.77318 | -52.84894 | 2026-09-21 00:20:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 3ef199fa-75b4-38b0-8398-7753af148fbc | -15.45708 | -48.47828 | 2026-09-21 00:20:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5e5b5b64-8361-3bbb-aa87-8af4a446afa3 | -11.36205 | -51.4267 | 2026-09-21 00:20:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3b6adf66-a46f-3dd8-8a45-6ee8d97a6b15 | -7.42571 | -44.78994 | 2026-09-21 00:20:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |


[Clique aqui para ver as próximas entradas](README6.md)
