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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc9c72c7-f28b-3928-8b88-55e02223d641 | -3.51517 | -48.03484 | 2026-06-23 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ac18063-44d3-3c4d-a8c1-ccbf5dc11b5b | -5.82247 | -45.06154 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cff3bac2-799c-31a8-8494-acda9c934d16 | -3.50869 | -48.03804 | 2026-06-23 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3b583ad-dfc9-3510-a07d-a40d86a119f7 | -5.82932 | -45.07073 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 07c3efdd-6f60-3ff3-b249-08320c1ad9f2 | -3.51457 | -48.0389 | 2026-06-23 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23fb9158-9983-3069-9312-c6449c8d37b6 | -4.34978 | -47.76348 | 2026-06-23 05:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0c1a92d-2afc-33a6-9584-313bbdd0f9cc | -5.8298 | -45.06203 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b222c38a-f9b6-39b5-bd18-a342af44df9d | -5.82149 | -45.06871 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6906312a-4a06-32d8-8560-f858a407c41c | -3.50812 | -48.04182 | 2026-06-23 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f931a7a-0f37-3a6c-b847-262ec1cd08fb | -5.82881 | -45.06924 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e56180d4-fbf7-39ca-83db-9065eca3675f | -5.82349 | -45.0541 | 2026-06-23 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 85367931-ded2-3d27-84d0-48778b7de6a9 | -9.36852 | -50.53657 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b219891-df75-3a39-a78a-73ef0033f39a | -10.87987 | -49.54454 | 2026-06-23 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4999898-c783-3e71-88ec-6567a00b23ba | -11.8055 | -52.52563 | 2026-06-23 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b141aac4-ab02-3801-86da-dd141f0bb5c3 | -9.77749 | -48.97779 | 2026-06-23 05:27:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ae82dc0-e649-3264-80a0-b76c0a5f2c98 | -12.02772 | -47.80221 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2197dc2b-163b-3c11-8e20-6e8cda8d3f89 | -11.8719 | -57.83324 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 216379b6-12b8-3e96-9105-9025dfd1ec77 | -10.38797 | -56.71669 | 2026-06-23 05:27:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1b52586-9dba-37d1-b246-74fcfe29db53 | -6.93626 | -51.93869 | 2026-06-23 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72dce78c-b883-31e9-8190-2a88baf298d1 | -9.38523 | -58.20577 | 2026-06-23 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ac824b6-bc4e-32bd-84c8-975b35ebcb0c | -12.29582 | -57.5716 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a9704ba-8f03-3463-8425-c82b639c5fb9 | -10.87933 | -49.54874 | 2026-06-23 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 64746bbd-cc12-3521-8b36-c611b52d1fc9 | -12.42912 | -58.41111 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7b3fdf2-78a4-337b-8029-092c31de7a47 | -13.52293 | -52.1704 | 2026-06-23 05:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dee4b15-5919-3eea-9ec0-9185682ca351 | -10.93362 | -56.84748 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbbc7bba-8bb5-30f2-ae0e-96ccac8271a5 | -11.94523 | -57.70301 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d4cecbb-4a93-301c-bde1-d98d076076e1 | -11.80571 | -47.34996 | 2026-06-23 05:27:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57d4301b-bf9e-3bb2-91c7-f20f4085e5b8 | -6.935 | -51.94207 | 2026-06-23 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17c9f1e7-0784-3b9b-b1ff-d61c1e88e55e | -12.03433 | -47.8036 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4db6a2e-c9e6-345e-a9af-3715acc5569d | -11.51225 | -56.1285 | 2026-06-23 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8b7a5c5-ca68-39e3-9afc-a0d9b8cb90e2 | -13.51779 | -52.16973 | 2026-06-23 05:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1524b3f-b688-3283-98e2-d623249ff484 | -13.50048 | -56.57546 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 826c591b-a041-310b-b14e-1a188c44effb | -10.02037 | -59.34788 | 2026-06-23 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cfb1f07-87cd-3d04-afb7-ff48740841b2 | -11.81393 | -47.33858 | 2026-06-23 05:27:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3c9e714-7879-3768-be34-648f5f9fce56 | -6.93427 | -51.94703 | 2026-06-23 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 448ad59b-0df2-3b61-9751-8cde37b7b061 | -8.87073 | -46.94114 | 2026-06-23 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f3018d4-87df-35e5-8fb3-eecd996f9066 | -10.90395 | -54.13787 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 754d7da0-5685-3b57-b95f-148adad23fb8 | -11.80479 | -52.53112 | 2026-06-23 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57054969-639c-3a62-9755-5d5fc38edde5 | -11.57977 | -47.43584 | 2026-06-23 05:27:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4739c956-642b-376b-b1c4-f56549650c22 | -11.046 | -52.46902 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5576c0ab-3176-3639-9868-a72fc2c8c409 | -10.27219 | -60.54826 | 2026-06-23 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8301838-6d6b-3a90-a500-d0d5d4f3fc47 | -12.28444 | -57.57413 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b2b939a-3834-3017-9d60-741c25a5fb62 | -11.87602 | -57.8285 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a2562d0-48f3-376b-a18a-976fa09e9dbd | -10.77295 | -54.11024 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbaaad33-5d4e-316f-b217-00abff571a80 | -10.93728 | -56.84801 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89f5368f-be9e-33f0-bc95-4623fd2b92b7 | -9.17781 | -58.05713 | 2026-06-23 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b40fb6f-5bc9-3e7d-84c9-2dd3bfc503f5 | -11.8006 | -52.52494 | 2026-06-23 05:27:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa141739-1631-39c8-b77c-455f4b455f28 | -11.9453 | -57.04366 | 2026-06-23 05:27:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c43ed25-2e77-37bb-9dc5-a5a09fbf9c1d | -12.29101 | -57.57937 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6af94a10-756f-3916-9dd3-e0cf5c8067f3 | -12.51707 | -48.30021 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 0e83c156-00d8-3a3d-8e1b-7b578d518088 | -8.86328 | -46.94595 | 2026-06-23 05:27:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c30b611f-e88f-3203-90e8-241aa3953c3a | -11.05156 | -52.46441 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4c547c5-6b53-382b-8f2c-dcc2dab8a5ff | -12.43376 | -58.40394 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a537e7d7-391e-3bef-ae6e-178caca93453 | -12.65505 | -47.68556 | 2026-06-23 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11e367cf-b0bf-3012-90cb-bb76cc1e01e2 | -13.51539 | -52.17208 | 2026-06-23 05:27:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79af0fb3-2c9a-3394-91bf-9230dc345d72 | -9.77878 | -48.97506 | 2026-06-23 05:27:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d443ec9b-54d5-3b5e-a206-7c06c32f109c | -9.12648 | -50.93475 | 2026-06-23 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d81deba8-d161-38d0-b277-dd4493716ca3 | -13.50432 | -56.57602 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e4f8cff-932c-308e-9bc2-e462b0b3617d | -12.66118 | -47.67987 | 2026-06-23 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5abeaad6-ea81-37da-af01-4e74f4735ff2 | -12.42853 | -58.41497 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a4cc55c-1cf0-3e47-8414-ee8baff75f1e | -12.43317 | -58.40779 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d11befd8-caa2-341e-bfd0-974d36100618 | -12.42448 | -58.41827 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6eaf6d4-c5d1-33e1-9f97-9d86cf3554b4 | -10.94003 | -56.85085 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4dd6958-ded4-3bba-930f-0c4846345476 | -10.92931 | -56.85121 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d9067503-e655-34d9-afea-d1f10c7efdfa | -10.87759 | -49.54855 | 2026-06-23 05:27:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deaf1396-989f-3774-b312-fdc544f8285a | -12.54791 | -57.19401 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b460848-b675-3637-9af5-f67e402a10cf | -11.05642 | -52.46513 | 2026-06-23 05:27:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4508974b-1c7e-358d-96cd-aefd5787b3f9 | -11.51609 | -56.12909 | 2026-06-23 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b71703-2230-373e-80da-0038c9137d10 | -12.6557 | -47.67947 | 2026-06-23 05:27:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e23c447-bd12-3efa-b11f-8d673c42b2c0 | -11.47026 | -46.68208 | 2026-06-23 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c312d33-8418-3fc2-b28c-a0e012530acb | -11.87482 | -57.83778 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34e7ce83-ba6c-3efa-b97c-6ecbf9d5bb7c | -8.8679 | -46.94374 | 2026-06-23 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a15c2ed-6074-3812-a470-687fb5cccf5f | -11.60785 | -55.33155 | 2026-06-23 05:27:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba6684d5-d36f-31d6-b913-64af87d19a58 | -12.54487 | -57.18912 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7f40982-d0ab-3e2d-98ce-164dd9ab8e21 | -11.62725 | -55.19067 | 2026-06-23 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| acadcfe5-7073-3d1e-b07a-a97b97cc694d | -12.50108 | -48.26883 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46eb3c10-7c5c-3050-8dc2-beb435ecb7ce | -12.54665 | -57.20272 | 2026-06-23 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1439b727-02af-3841-8869-216721e8d4c7 | -12.50758 | -48.26974 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 383843d3-01f4-352f-b75b-583ab6dfe07d | -10.97698 | -48.1563 | 2026-06-23 05:27:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 483c1646-72e5-301f-a328-2dd0d7fa563a | -12.43259 | -58.41165 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52d8ca14-4d29-351f-82c5-fbfeafc793ba | -12.42565 | -58.41057 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6be0cab6-5958-390c-b91f-7fe36adb49d7 | -10.77669 | -54.11502 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5b305a10-cba1-3553-bf64-1b8b9da8c4bc | -11.51158 | -56.13326 | 2026-06-23 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13f41a0d-6653-3676-855c-2e2a7b7a00a8 | -11.47657 | -46.68962 | 2026-06-23 05:27:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 13247f70-a5a2-3fd8-a2b8-e195e8ebbea8 | -9.60458 | -56.92741 | 2026-06-23 05:27:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e8ba4087-c087-34ef-8613-47ed393aca1e | -10.77237 | -54.11438 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd72e150-e647-31bc-a898-4d6670d66e47 | -8.12683 | -47.89474 | 2026-06-23 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcdc74bb-62d4-3876-b330-4d7737de6469 | -11.87484 | -57.83654 | 2026-06-23 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a806043d-af2e-343f-96f8-1f1428e3abb7 | -10.90828 | -54.13849 | 2026-06-23 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9768c8c8-ab2c-3330-b323-dcc8630e07ae | -11.81324 | -47.34467 | 2026-06-23 05:27:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36fc6dc8-ef98-3590-a94f-244a71161bc5 | -10.3886 | -56.71241 | 2026-06-23 05:27:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c81044a-2128-3e92-ac0c-356af434ca50 | -12.4297 | -58.40726 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 011319e7-4f78-3e12-a535-0b2b843a35e5 | -12.42507 | -58.41442 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ccf06374-decc-3e26-9103-4a8447a397b4 | -12.50716 | -48.27072 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ec608552-d38a-34db-b855-8fda4a701690 | -10.39228 | -56.71285 | 2026-06-23 05:27:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55523a5c-5844-3400-ad94-93de304257d1 | -12.43435 | -58.40009 | 2026-06-23 05:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ea34985-e16e-3036-8baa-2b83113052df | -10.02093 | -59.34435 | 2026-06-23 05:27:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 661737e0-461c-3615-acb2-c18a86add77e | -12.50654 | -48.2763 | 2026-06-23 05:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ad91c2e7-18fd-3c70-b317-32bbed18de76 | -12.46771 | -55.12438 | 2026-06-23 05:27:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c3f7747-020d-346a-8ed5-118f3cb63e05 | -9.77824 | -48.97945 | 2026-06-23 05:27:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README16.md)
