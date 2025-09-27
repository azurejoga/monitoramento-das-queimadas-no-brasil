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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8bf4ce8-c539-3f85-8c5d-8205ee4ddd52 | -11.23986 | -45.56151 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6947f3c-7694-3c6f-99a7-d6b9dd5944c6 | -11.98015 | -47.90161 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| be33bd7a-8386-360f-8348-2d7f0c3cac66 | -12.87449 | -47.09003 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baf898ce-d41f-3b29-a907-9fdd38f4f96c | -10.23868 | -50.25356 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50621fa6-2a52-397a-ae8c-6333866387f9 | -10.93878 | -44.30529 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bab94453-22f3-399b-b2db-9afa9e4679e6 | -11.40567 | -44.9152 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05f179b7-aefc-3b46-95c5-f230ebc2a3d0 | -11.36218 | -45.01844 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de11af8-6a6c-3f77-b0d4-dc32566c8179 | -12.25731 | -47.16596 | 2025-09-27 04:23:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a947e861-d229-3cfd-8200-709d1c43c0a6 | -11.62406 | -44.42826 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd048e54-8a3f-3d98-b385-d3db5f3d0fbe | -11.49196 | -43.5309 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8da2e246-e6cc-3517-9d0f-f3f7e264c387 | -11.97567 | -46.59713 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d13c7d05-c3ce-388c-a5f0-69db12cd6aef | -11.69368 | -44.4505 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7b0869f-4b5d-3b3f-8e8c-1044a1e6aa21 | -11.35493 | -45.02094 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b25938d7-1ad2-3cc3-ad0a-1a709c99919b | -13.18383 | -47.39777 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cdbe8f1-b246-34a9-ac6f-e0103bd5c5a6 | -10.18562 | -49.51458 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 217ce44b-7ef6-3a74-8f02-3cc1e857a847 | -10.30775 | -45.21048 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab2619be-6fd1-3499-a306-3fe186071101 | -12.10114 | -44.31589 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50185f57-7044-344c-a042-f9a93ace3dd2 | -12.03103 | -47.07687 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e706983-1b0e-3be2-905c-ce7c4ac03166 | -12.9862 | -49.4344 | 2025-09-27 04:23:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d8cf9e4-2297-3f48-aadd-ab783076dbe8 | -10.91727 | -44.28691 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b2359ab-7ce9-3f34-8ad4-b1558ca019dd | -12.8806 | -47.09485 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc4e6424-4a59-3430-8d66-1a1888ba8864 | -12.06946 | -45.05222 | 2025-09-27 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4617c497-b79e-31ff-af68-61cb1807d425 | -11.43832 | -44.98259 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e9f93685-4a42-3cff-b978-e3659f9548d9 | -10.92011 | -44.29111 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a9339b3-8f04-3684-8bfb-baf79df0c1d8 | -9.96712 | -43.6153 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 424f07f7-308b-3e7e-b688-1561b8b7f3d2 | -9.05363 | -45.51297 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8aef59d-7eca-377a-b45d-def3d40726fb | -13.32562 | -47.30557 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18574c7f-b973-3de0-8a10-4d3f68d73f4e | -9.10987 | -48.90128 | 2025-09-27 04:23:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc8c0087-132a-3701-9bf6-2be831e47503 | -9.05086 | -45.50894 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0e22be8-0a6d-3123-9e92-d2d209323f4a | -9.9677 | -43.61153 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce1c5ab7-5f06-35b9-9f75-bf2fb9aa5ec4 | -12.26101 | -44.06639 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c90455d7-3fd2-38a8-a0ae-514a1624810f | -11.43441 | -44.98568 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2c333e57-a503-34c6-94bb-0181792ebcdf | -8.82193 | -46.26682 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5890b243-584a-38f0-b4d4-f9e958ac9647 | -10.13689 | -46.4794 | 2025-09-27 04:23:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3db86a82-2743-3a34-913a-0c78daa45e08 | -11.50416 | -43.54485 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43063c8f-9bd5-31ed-9c65-6c9960d2529f | -10.92935 | -48.82951 | 2025-09-27 04:23:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ada0373-b742-3106-8fa3-5f0431e07b24 | -10.39548 | -46.132 | 2025-09-27 04:23:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e74f33a7-df25-348f-93ed-6d37c5476af4 | -11.68803 | -44.46468 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e31c4392-9325-34bc-bcb1-74894d217278 | -11.71746 | -44.40899 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0bbb19c-322c-3b38-9f53-0f301e21efbc | -11.6777 | -44.30429 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1471fc85-01c6-37ab-940b-9e02851c5d50 | -12.0322 | -47.06964 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2d19b4ea-ce6c-3f9f-95a6-232e654d29cc | -11.97484 | -47.91241 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9985e5a-1adc-3b6c-a18c-eda8dde9613c | -12.26962 | -44.05611 | 2025-09-27 04:23:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84516703-200a-3568-8f36-71c9cb2b4e9b | -12.64708 | -48.15638 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 627ba6dd-2200-3b75-a912-dfcfa81f40a2 | -11.40623 | -44.91163 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fe2c9fe-475b-305a-97d7-46665dec3c0a | -8.65207 | -44.00907 | 2025-09-27 04:23:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 414e3647-cdc4-3b62-bd01-ff03c8b6a87d | -8.51508 | -44.61718 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37bc8c4a-77e4-37b0-8ede-74e701c1b5e4 | -11.96859 | -47.90746 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d47144ab-761c-3914-94f3-b3d5c4db37fe | -11.64896 | -52.87125 | 2025-09-27 04:23:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbad9006-b360-3513-96f1-bb02999c298d | -11.50066 | -43.54432 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4889c49f-035b-3cc4-a036-5a7e6c16755a | -10.17077 | -49.37547 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ad82ad3c-4823-3389-81af-6e935cfcb239 | -8.91517 | -46.10349 | 2025-09-27 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8568b06d-8ad6-330a-a11a-a6d3494cb139 | -11.9664 | -47.89931 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd633454-cd62-3230-abd2-095cd9ab8a64 | -10.28364 | -45.21703 | 2025-09-27 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc28f9b9-c596-3966-9365-b269ecb3e029 | -11.71236 | -44.41951 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ab5b6d9-8e01-3d89-a98b-15e361d9baba | -10.81274 | -45.38137 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 635ccda9-2bc4-3167-80ea-ca7db1824112 | -12.65259 | -51.67981 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cba7e86f-e9b8-31d6-977e-b99a01c6b26e | -7.93913 | -45.19905 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e48b70ce-c6f1-3d9b-bc4c-658100cc80f6 | -7.71732 | -47.30484 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ea21162-8bfa-3ee6-91b5-dc4af6b4dd33 | -13.2344 | -46.38471 | 2025-09-27 04:23:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6fe942f5-77d0-3069-b2bd-d213a4d1f33d | -12.49312 | -47.50067 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5417aebf-b8d6-3080-a66e-5077822ee4e6 | -11.69933 | -44.41369 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c3ed0f9-8b37-37a0-8e21-36cda1b48276 | -10.80441 | -45.36923 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b417d293-48e1-3a82-8e55-3f02ae4c2153 | -12.03045 | -47.08048 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64454c68-4539-3cf4-a67d-686e158831f4 | -11.29207 | -47.81162 | 2025-09-27 04:23:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae56aedc-e921-327d-96f7-38a791c00d67 | -12.97081 | -46.90698 | 2025-09-27 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a428214e-186c-3103-bdc8-2186a3ec4243 | -12.10209 | -44.19341 | 2025-09-27 04:23:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b3311bb-0c70-3491-a3c1-65be820b2bdc | -8.51563 | -44.61367 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d9a39fb-b60c-3953-9552-cea93ca25f19 | -11.24042 | -45.55799 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 016115d3-5fe3-3312-9b07-d73db10b646e | -7.67211 | -47.42569 | 2025-09-27 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a1f381c-59e0-3fd3-90a8-dfaee2a9023c | -8.13997 | -42.37406 | 2025-09-27 04:23:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b5737365-1f0f-390a-98bb-9249d0849b76 | -7.82835 | -45.14933 | 2025-09-27 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5c524d5-b15b-358b-b93e-035f5109f75e | -11.65661 | -45.34514 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc1d66ca-4899-366e-86eb-7e6023183a63 | -8.26374 | -44.94679 | 2025-09-27 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5822d1ca-4370-312d-b0a1-a1f5f11ff14b | -12.82858 | -44.68974 | 2025-09-27 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42dcf8f7-038c-3d7b-ad55-ed5f6716c2c1 | -9.96483 | -43.60723 | 2025-09-27 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0464ac8-6280-3aad-bf97-04d8bce5d602 | -11.43426 | -43.51008 | 2025-09-27 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 80679bbc-c264-372d-94a1-d01938d62a38 | -10.24047 | -43.94636 | 2025-09-27 04:23:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ffa18b-62dd-39c7-b8fb-5e6a780f9280 | -11.79379 | -44.91349 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27d2aa9a-3157-397f-bb97-f09a17c77d94 | -11.99065 | -46.61056 | 2025-09-27 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f653d097-4681-3749-b737-96f43410ebd6 | -11.43497 | -44.98206 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7fe3934a-0151-3a5e-8578-77b0f5e5ae15 | -10.81607 | -45.38191 | 2025-09-27 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 963957a3-6300-3f33-97b2-6aff8f1b3feb | -8.52512 | -44.64037 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 982598c6-50ab-378c-939a-0d66bc23d04d | -7.78401 | -46.94133 | 2025-09-27 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f35c5abc-9cd0-3e12-9fd6-5ac52a93e995 | -9.99598 | -44.17551 | 2025-09-27 04:23:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d34dba9d-b49a-3d7b-97c9-96ef7e24820e | -10.574 | -44.06942 | 2025-09-27 04:23:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e22680c8-6e8c-359a-aa16-4abdc9dd0ad6 | -12.62834 | -47.57223 | 2025-09-27 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce01bd8e-c5f4-3834-99e2-f5b3adf57341 | -11.37607 | -44.95099 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ed5935d-8fbc-3b60-ba69-07fe08355ec7 | -11.01147 | -44.35349 | 2025-09-27 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee79617b-3bdf-3414-87c5-66505b597202 | -11.69876 | -44.41738 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9f002a7f-889e-3005-8837-f9564e225dd6 | -7.76937 | -43.91389 | 2025-09-27 04:23:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1d84181-5745-3ab9-be16-53d3a26adeba | -12.03337 | -47.06241 | 2025-09-27 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45ccbad2-8b0d-357d-9154-acf0d1aef6bb | -7.22227 | -46.6154 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2b17ea8-957a-3ab6-bebf-76c40558af9b | -7.87774 | -44.02189 | 2025-09-27 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c19d30d-412e-3a66-ac03-9c543ef14d62 | -11.94613 | -47.8725 | 2025-09-27 04:23:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c8d0f00-a158-391e-b518-8bbf6f8a7613 | -11.78647 | -44.87149 | 2025-09-27 04:23:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c152606f-0373-3d21-a314-c28a56bafa2c | -11.6705 | -44.46569 | 2025-09-27 04:23:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8730354-00d0-33a3-a22b-efb463bbe6ac | -10.16998 | -49.38 | 2025-09-27 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b9490e1-009a-3560-a8d1-fc8b17cc5905 | -8.5279 | -44.64442 | 2025-09-27 04:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 054cb770-e797-364a-956d-045e72217b14 | -13.32502 | -47.30924 | 2025-09-27 04:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README35.md)
