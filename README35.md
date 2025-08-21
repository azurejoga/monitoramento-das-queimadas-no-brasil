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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c373ca8-d43f-3138-8bea-92ca621d0295 | -14.12807 | -45.40031 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fbdd1249-1117-3f1a-bf3e-e73587ebc6a6 | -13.64687 | -45.71624 | 2025-08-21 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80c97aab-86da-30b8-ae49-0b881df9470a | -13.15312 | -46.90294 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc5294f6-404d-3321-ad5d-de283e476a70 | -13.57283 | -47.05104 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9d491ba-cecd-3778-9aa9-79c02b95765e | -14.8856 | -48.06063 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 962ef550-e7c2-308c-8cb8-95e4529f4a32 | -14.85923 | -47.94846 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 107b9af0-2723-35e4-b212-0d2b89829459 | -13.04905 | -46.83337 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0d622b6-76b2-3cbe-9589-fc6a7c740f49 | -13.40328 | -46.34734 | 2025-08-21 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de5d58de-7f10-31a9-a33d-530faaf27565 | -14.12865 | -45.39672 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c70a8101-3146-36e1-b041-ba716a377e26 | -11.32511 | -55.21969 | 2025-08-21 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f613b1f-5223-31a1-990c-8f8f3ff2e68b | -13.40669 | -46.34796 | 2025-08-21 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5a10504-4636-3b0b-b64c-e8cbe070f879 | -13.15384 | -46.89872 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75551ec6-cb53-3b36-a6eb-3ec1c899b02d | -13.19413 | -46.89397 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d983998-cb57-3652-9a25-ed0c3521ef62 | -13.0387 | -45.1934 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa57a3b8-2ddc-30c6-b35e-25046657e56a | -12.94669 | -46.2317 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d55589a1-d944-3eb7-babf-9a1d0c0d9bdc | -13.58713 | -47.00868 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6149ec73-7e73-326e-b246-ecc39d0c6b7f | -13.1465 | -54.93372 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5c14f9e-1a33-37f9-a277-6f74673cc813 | -13.16894 | -46.8729 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b92c25d5-1bda-350a-b32d-760bd7c5048f | -13.55048 | -47.05538 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd53c8c8-b18e-3f1b-8a96-6152a9971a6f | -13.6422 | -43.80678 | 2025-08-21 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d0661d5-4714-3c31-a3bf-dd4eeff41def | -14.84566 | -47.94135 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e38d6976-6894-3874-bd58-13dd5c666044 | -13.03756 | -45.20055 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c466880a-b023-391f-9737-c8066f3ed9fe | -13.15941 | -46.90831 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bb575ca-d466-3004-8bd1-ef2e62b853df | -13.38501 | -47.49737 | 2025-08-21 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b7ed40b0-8ecf-32b1-9c5a-ea8facc1e47f | -13.59278 | -47.01789 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b872c452-778d-3e31-80ba-db38dbaff9fc | -12.9516 | -46.24457 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b53d6724-c005-35fa-9c49-1f05e7ee064e | -12.94568 | -46.17409 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a39b903-22d1-3e55-a324-859c630018d2 | -13.15802 | -46.89519 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0420d5de-d1df-312d-93df-b3e01328ba1e | -13.535 | -47.04044 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1fa9f0c1-030d-36fc-a2b5-d8d672a15e6c | -14.49527 | -45.95535 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5e64357-8690-356d-ab33-cf68361abbe9 | -14.12366 | -45.37358 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3b889470-2621-3491-8019-5d45276e85ec | -14.85779 | -47.95692 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9728a7ba-44f8-3bdd-bf3a-b9686df6907b | -14.49863 | -45.95592 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d47c0db-ce71-3c4e-9f44-a5843fbac519 | -13.91928 | -49.52434 | 2025-08-21 04:19:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8043b9-4078-389b-9863-702e45f4f91b | -13.14664 | -54.92614 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3f781af-84eb-3059-b18e-aac3386ad107 | -13.48258 | -47.04858 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aed74896-a839-3a47-acfd-c63ac478cc1e | -13.38026 | -46.2314 | 2025-08-21 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7ca8bf8-206b-379e-8cdf-687a5493d562 | -14.45943 | -48.47369 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dae2c3f1-4794-3756-b1ce-bc5dc6eaf448 | -13.49459 | -47.06302 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d40b3c7c-99ca-312f-97ea-7fffef8bc7b6 | -12.89484 | -46.08141 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78cc640c-d2ca-395f-93d4-98bec92ab20a | -13.14504 | -54.93427 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd4d8afd-9a24-30e2-a92c-9391a26e8711 | -14.46666 | -48.36508 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d262ecfc-c868-3c86-9059-1b1cfa249a2d | -13.53782 | -47.04502 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de9b667a-1589-36a8-955c-30138ff4693c | -13.04214 | -45.17196 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 176b0304-836f-39b9-8789-15e24a2af8bd | -12.95872 | -46.22268 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 49fed1fa-8afb-3fba-8a79-4f32093f0b40 | -13.03365 | -45.20356 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7cfe5bb2-c1e9-37ab-a77a-d5fc05b330f1 | -14.12647 | -45.38899 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a793ff0-c4a0-3bc5-b890-b7de23956d3d | -13.38426 | -47.50176 | 2025-08-21 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cfec30e-be5f-319d-baee-656a1f1c5a09 | -13.58956 | -43.35291 | 2025-08-21 04:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ef16d896-94a8-35f9-9ee5-78469751411d | -12.93982 | -46.18834 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9efd0dd3-4af6-32b2-a016-87e2276f468c | -13.17062 | -46.90572 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c027649a-0557-3bd2-a4cc-9f2e6385c650 | -14.50139 | -45.96015 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52a05e20-7833-3bbf-b635-4bc475c5c026 | -13.03307 | -45.20713 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| db97b11c-fee6-3cb1-8925-1a10a6f9795e | -15.31843 | -41.99236 | 2025-08-21 04:19:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 72f376bc-9612-32f4-878a-55b08627b030 | -13.03846 | -46.8111 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee1fa195-8273-39b1-988a-99617f6fa2bc | -14.84711 | -47.93283 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ccbe2e53-f1ef-3a0c-8d1b-80f10fea727d | -12.93058 | -46.20183 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df3b986e-7aa4-3a02-8e82-3429bb2e89d0 | -14.85141 | -47.92929 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c66d097-4d08-3a99-b827-0152f5a6dc04 | -13.03537 | -45.19284 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b754d1a1-a7c8-3316-89b6-e984ec6c699d | -13.57067 | -47.04246 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f22e5e17-7cdc-3867-9184-26ca5131bbed | -14.85353 | -47.9385 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62dea1af-7795-34a1-baeb-af9ec6d89e0c | -13.86749 | -45.55619 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6da194ea-fc5a-31ce-ad53-614f0091e5ad | -12.89144 | -46.08086 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93b0c4ad-e587-3be7-a188-3a1eaa2f15b5 | -13.81182 | -44.19699 | 2025-08-21 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cfae83c-95d5-39ce-8c3a-9acadf054f43 | -13.04689 | -46.82488 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3a27186-9f8d-3e6f-bc79-b5bb9d0c7bdd | -13.57 | -47.04641 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b7d2bed-d86b-354d-b797-c7fef23237a8 | -12.94322 | -46.18902 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e3f9c7b-7d99-3ae5-a717-000f3d907a60 | -14.9229 | -42.80737 | 2025-08-21 04:19:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea5ffc3f-3faa-3e7a-a0e8-29f1f8d7bba0 | -13.03709 | -45.18212 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9ecb5b4c-d988-3674-ab3e-3ac828f5afb6 | -14.85135 | -47.95131 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 374ef55b-3deb-313c-bafe-8cc217d28460 | -14.50259 | -45.95282 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 967c9ad8-ef38-3f93-b837-82836b9f621b | -13.49242 | -47.05445 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a645ce3a-e232-3269-91a2-ae54aa9fe6fa | -13.03318 | -45.18513 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 990907fd-e488-3365-b9c3-a635e8b567af | -11.32002 | -55.21397 | 2025-08-21 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37938ef7-ea1c-3c7f-8a2b-cd6ba2169879 | -13.02306 | -45.20546 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d0b7e70-8232-38ba-88e5-80a607f385c3 | -13.81452 | -43.22579 | 2025-08-21 04:19:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 465c7daa-f717-3782-ac08-36a7ec918e0a | -14.88201 | -48.05996 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44ca9f3e-29f9-3d58-a43e-2a515ed16314 | -13.27661 | -43.91675 | 2025-08-21 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a518e183-472f-3d18-8fb5-7319c2353ce6 | -13.65466 | -42.48166 | 2025-08-21 04:19:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b74f7cc7-e430-3bd3-9fd6-155e624fd478 | -13.16291 | -46.90888 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b42f6bf-03c4-34b5-92bf-8399e689d817 | -12.96027 | -46.23458 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba03ece5-91b2-32e9-b019-bffe0af25d94 | -13.53715 | -47.04898 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd20123a-1343-303b-ab7c-e358ee0333bf | -13.0449 | -45.1761 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c6c23657-22b8-35fa-a830-c6d579d492cc | -13.02858 | -45.21373 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3ce94d23-1a5e-3c77-aebb-00b2608938dc | -13.3886 | -47.49788 | 2025-08-21 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93ad013c-a111-3e3d-aa0c-613efd27792c | -13.0326 | -45.1887 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e968e29e-7441-341a-9842-cc324a8a7598 | -13.32786 | -54.40915 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2cd521fc-864c-3fe8-ba45-0b6e2b48fd37 | -12.93398 | -46.20243 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 918ac568-5f6a-3660-a2f9-30e088fe0a3f | -13.63672 | -46.88324 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed263281-7441-3c38-a59b-ac0741a7ee68 | -14.05975 | -43.53535 | 2025-08-21 04:19:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9f5d299d-3a23-3226-b69d-6a460993d5fa | -14.49803 | -45.95958 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b95aad5-ed04-3667-93dc-ca9741e035b9 | -14.12413 | -45.39207 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbc08d2d-6596-3e27-bd9d-ba7b7c1ecda2 | -12.89205 | -46.07711 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd67cd0c-2921-31c3-ada0-9eca48f5630e | -13.03641 | -45.2077 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 82144853-5691-3fbd-9384-429ebd900312 | -13.04207 | -46.83218 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5368e97-5e7e-32a3-a304-7884b54a512c | -15.64176 | -41.02675 | 2025-08-21 04:19:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a5a8e74c-c9f0-3b65-a768-7fb8e2e493cd | -13.59062 | -47.0093 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bdc4cf3-094f-3c41-aace-82c8c0824ca6 | -13.59344 | -47.01391 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b1cc0d5-9afb-33a9-91d6-62d0294305fc | -14.05583 | -43.53847 | 2025-08-21 04:19:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 562a4e05-db13-3d99-b926-a7e791a87959 | -13.03823 | -45.17497 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |


[Clique aqui para ver as próximas entradas](README36.md)
