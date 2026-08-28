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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28058569-714b-3f77-bfab-cb79fe17c9ee | -15.85503 | -48.95538 | 2026-08-28 17:26:00 | NPP-375 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1af3c3ea-8bfe-3bee-a42e-932bd38c810d | -15.196 | -53.85497 | 2026-08-28 17:26:00 | NPP-375 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 522f5eee-e448-3a5e-a4ed-5fde483d77e4 | -15.60116 | -56.3858 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e6cc78bc-1f0f-3cd8-9519-6d67cbfc2a86 | -14.79416 | -42.83401 | 2026-08-28 17:26:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ad452f97-3548-34f8-af8d-f97828fc26e5 | -13.83569 | -54.05933 | 2026-08-28 17:26:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ef627f11-4da0-3e04-8f07-93b908af755a | -15.99672 | -54.92124 | 2026-08-28 17:26:00 | NPP-375 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d6724c6-cffe-321d-afdb-c23b7c51894a | -14.26824 | -53.25035 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 63c9dd7c-ac70-3582-8829-073f41bbd5c8 | -11.53904 | -45.51001 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b77e2cd2-2d90-3202-a12d-102a9d57107d | -11.48219 | -45.06965 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 03f86920-6b0a-3263-88e4-f6e66cd20284 | -11.03067 | -49.65245 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4d63dba4-6006-34b9-bc31-ff704dde3458 | -11.58191 | -45.51858 | 2026-08-28 17:26:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| f3aba373-f790-3c7b-8a55-c30b705fb7ea | -12.91329 | -59.87732 | 2026-08-28 17:26:00 | NPP-375 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f231278e-2078-37f2-9413-2b833ca2a05b | -11.00811 | -49.65206 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ef65dd33-ff0b-334d-8f66-adc21ea6598b | -11.2393 | -47.05462 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6f451f0f-f261-3b18-a090-da685a4510fa | -14.59445 | -53.14784 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| d4c6fe0d-a5b5-3fb9-a592-47ff7c33dd6e | -13.33289 | -46.90607 | 2026-08-28 17:26:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c1726860-ee83-3e78-b7c6-b403d489169e | -10.29575 | -49.9519 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c6f5f238-2cb8-333b-a12e-2f2d5992d90a | -11.1966 | -53.99553 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 23ee485e-5d88-3bf2-b6d3-ca82deb4a334 | -11.65304 | -55.68977 | 2026-08-28 17:26:00 | NPP-375 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 7296310d-a957-3861-a895-981e8ccf3a48 | -11.22467 | -53.99482 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bd2d8f4f-9c9c-386e-9182-fbed60237223 | -14.47698 | -53.39779 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53dfe83b-c98f-36bf-9431-59e16b65ffa4 | -14.19661 | -52.85296 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 131.7 |
| e834e70a-0457-3990-8e17-9883901d4458 | -14.49039 | -52.14153 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 449d74fe-c6d2-3dad-8042-72b9d413140b | -14.46436 | -41.2218 | 2026-08-28 17:26:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 72567e77-baeb-36b8-bc84-60cfcdd82698 | -13.88381 | -53.24435 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 952c9cc5-f2fc-3b9d-aba0-41108c6c53f3 | -16.57811 | -49.78155 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| d3d569db-dae8-3e41-966b-abaecb81bc5d | -14.92224 | -41.25824 | 2026-08-28 17:26:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| 0401115a-33a4-321b-89dd-73976a0584c3 | -11.2396 | -54.00005 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 69775c7b-aa0b-38fb-a455-a364208aa94a | -11.02631 | -49.65322 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0f061d48-06ce-3745-a14d-9172ae2d5511 | -11.59743 | -47.06899 | 2026-08-28 17:26:00 | NPP-375 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b15b3e06-c5de-3635-ba4b-0de059badb40 | -12.78668 | -46.45298 | 2026-08-28 17:26:00 | NPP-375 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 284f138b-3a18-36e9-89f2-075ee8f87187 | -14.17182 | -52.83287 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 61f5de5a-8b40-3f88-98a8-50eb4a2cb6d2 | -13.6053 | -45.77586 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 8cd96ad9-c1d3-33f4-8ae2-c9ce4851c23d | -14.23312 | -51.76725 | 2026-08-28 17:26:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 54191b29-2bc3-3074-bba5-74e51c493c99 | -12.91329 | -45.86253 | 2026-08-28 17:26:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 55bf4c66-40e5-3f85-96f6-4534b1a555c3 | -14.19313 | -52.85358 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 466a5ccd-594f-38b0-8198-e171f9a93abc | -12.38983 | -48.20554 | 2026-08-28 17:26:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| a37bea0c-e4a6-323a-b20e-0486e9d457fa | -14.46186 | -58.51733 | 2026-08-28 17:26:00 | NPP-375 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 31.0 |
| f2e68ae5-db70-326d-ba03-b834c10223f0 | -12.19787 | -50.55768 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b5c3b17a-369d-33d0-9bda-55c98984b749 | -11.22527 | -53.99858 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 27e91982-f1cf-387b-b93a-30f885c758f2 | -11.60744 | -50.1987 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 99f6f577-e788-3aeb-86a0-dde6ea0d5970 | -13.6006 | -45.78039 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f06a7f64-0c69-3523-9f2d-0bae677ea1ba | -11.46638 | -46.94433 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a57c962b-a641-38b8-bbbf-3349ce002e99 | -14.18837 | -52.84633 | 2026-08-28 17:26:00 | NPP-375 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bf41353e-f616-3f53-875e-af71121641a9 | -13.6614 | -47.75137 | 2026-08-28 17:26:00 | NPP-375 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 299accae-1f1e-39be-8923-630081aa3047 | -16.303 | -47.6405 | 2026-08-28 17:26:00 | NPP-375 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| daabeb6b-a358-3e84-848f-c737ba5d9505 | -14.63448 | -57.01132 | 2026-08-28 17:26:00 | NPP-375 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 2ed9b1dd-b1c3-33af-bd18-2de2cce143b5 | -11.20244 | -55.09226 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 65e2393d-8dd7-31bd-bfcf-cccec3c8ea2c | -14.50289 | -40.33128 | 2026-08-28 17:26:00 | NPP-375 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 4438da17-f01d-308e-94c4-e8c2e8c2b3b4 | -13.42385 | -51.7687 | 2026-08-28 17:26:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d5b15333-5212-3ca7-b04f-4f73a3e25eaf | -10.30304 | -49.96772 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8069f48c-73ac-339b-aed7-97ffe71709d3 | -11.22931 | -54.00177 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2bc09aaa-9f32-3299-b294-cfe033ba4c32 | -11.17232 | -51.24135 | 2026-08-28 17:26:00 | NPP-375 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2d1e0641-466f-3e21-a453-36a22002f692 | -13.58301 | -45.77613 | 2026-08-28 17:26:00 | NPP-375 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| a584f416-ff77-3c7b-a507-1e33b365ce04 | -13.8832 | -53.24052 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 50fca069-f4be-3071-b7d0-90335fb8faae | -11.22708 | -54.00986 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 8bcaaa43-92bc-363a-a90b-258d7d45ae8e | -15.73185 | -51.18097 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 27664244-7ae3-3321-b9f2-443ae3e90a8b | -16.57417 | -49.78227 | 2026-08-28 17:26:00 | NPP-375 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 2c18591f-610a-31d5-9818-0c5ebd17221a | -10.99708 | -49.64084 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9cfbc995-4a47-331d-b5bc-4b965a5829bb | -11.22689 | -53.9867 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 98da2b8a-5dc9-3397-8868-ec584fd4c2e5 | -11.017 | -49.67656 | 2026-08-28 17:26:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 0f66314d-bccd-356b-8a17-2b07496404ac | -11.61534 | -46.7317 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3b0092d2-7825-35fc-8339-eb168332df39 | -15.99338 | -54.92178 | 2026-08-28 17:26:00 | NPP-375 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 05acf7f8-da01-3cc7-8bf7-d386a2089bc2 | -17.58603 | -51.64537 | 2026-08-28 17:26:00 | NPP-375 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 3ac2076a-a538-3d2e-8b99-28c9454af204 | -11.1963 | -55.09691 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f224f38c-f960-37e5-a2c2-d11878985f43 | -11.88886 | -57.10895 | 2026-08-28 17:26:00 | NPP-375 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 123a9ccc-5211-3da0-8bd4-cb6b28fe7d8f | -15.72892 | -51.18608 | 2026-08-28 17:26:00 | NPP-375 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c87e87d5-091e-33e2-acb8-98f58b0c30ab | -16.3135 | -47.85008 | 2026-08-28 17:26:00 | NPP-375 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6c57ee4c-db75-38fd-915d-a94c6fa03fe0 | -13.88664 | -53.23993 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 76d1b949-d246-3f6a-9cbc-f359e2663d1e | -11.19074 | -55.08319 | 2026-08-28 17:26:00 | NPP-375 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 46eb19bf-d835-39f1-90fb-5135afc9994e | -14.33739 | -47.24157 | 2026-08-28 17:26:00 | NPP-375 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b382bb4a-5441-369d-ab31-2d5ed6819171 | -11.4825 | -46.94016 | 2026-08-28 17:26:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9792bfa-ce45-3d5c-8a8d-348ae71ec76d | -14.56468 | -53.20376 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3085e272-bb9e-3b04-b4e1-b53d6b9e84bb | -11.80085 | -47.67351 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 4cdf63f2-6fb7-3926-bdaa-285ba5f5022b | -12.21277 | -50.54767 | 2026-08-28 17:26:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| da8998a6-9f3a-3a72-abf9-e7b309921e0a | -11.29821 | -54.03677 | 2026-08-28 17:26:00 | NPP-375 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e522123d-762e-3725-a655-bde8346081d3 | -9.68588 | -46.56213 | 2026-08-28 17:26:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 37ed011d-3c9e-38ed-81c9-506447858748 | -10.32392 | -49.95982 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d14738be-03e3-301e-82cb-caee9be2ec68 | -14.61631 | -53.15204 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ca5040b9-d832-30b2-ac91-bbe1b78a2dd8 | -10.90378 | -46.64897 | 2026-08-28 17:26:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7984372f-bc6f-399b-b76e-650d8a4f7c89 | -16.16643 | -58.58153 | 2026-08-28 17:26:00 | NPP-375 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4616a5fe-7e1d-3fe2-89bd-6137f91655bd | -15.60427 | -53.11275 | 2026-08-28 17:26:00 | NPP-375 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ec781d8f-3db5-3c55-a1cc-ea47eca42543 | -14.87964 | -52.63501 | 2026-08-28 17:26:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 3a819e67-04c0-31a7-a71e-f04292f163b0 | -16.34368 | -48.92522 | 2026-08-28 17:26:00 | NPP-375 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6c9d54d5-b43e-3aa6-9e53-4de61a11db9b | -11.84038 | -47.21679 | 2026-08-28 17:26:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2002c2ac-9f34-384a-99d3-8304d95e4bb3 | -10.44717 | -43.77373 | 2026-08-28 17:26:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e13b76cd-0c39-38d0-824a-d5ae01486c23 | -15.61071 | -56.40354 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9719c866-9acf-3f0b-a6cc-f1c6a9a5b6c0 | -11.83326 | -46.77281 | 2026-08-28 17:26:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 489c4da4-767a-3873-ab52-b20f252d8bc4 | -11.16542 | -54.01627 | 2026-08-28 17:26:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 10b74705-917c-306f-a350-7b340970518a | -11.21696 | -55.07533 | 2026-08-28 17:26:00 | NPP-375 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c3eae92a-5a58-3fd3-8c1c-6d74a6d12691 | -14.24455 | -45.27231 | 2026-08-28 17:26:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01a1b746-1d5e-3280-a8db-5101eb5a2a26 | -14.42902 | -53.44492 | 2026-08-28 17:26:00 | NPP-375 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 64d862d6-f0e5-397d-866f-6e44c4376a98 | -10.47963 | -49.95385 | 2026-08-28 17:26:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f8afa746-5d74-3995-bed8-e4224fec31f2 | -12.06903 | -47.15664 | 2026-08-28 17:26:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b2afdc8-baf0-321a-afb4-da2ea8aec4e7 | -10.02154 | -45.82135 | 2026-08-28 17:26:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e3df419-65e8-3171-8cbc-3ae742ff8471 | -14.91504 | -56.30989 | 2026-08-28 17:26:00 | NPP-375 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| f2a41bc6-6f06-3b99-97dd-0c8da262ec38 | -11.36729 | -45.15353 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8010173f-a8c4-3690-a473-a9c8b201480e | -15.7639 | -56.4497 | 2026-08-28 17:26:00 | NPP-375 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70c1998e-e91d-3761-b7a5-a2c7e272f9a1 | -11.70264 | -47.61407 | 2026-08-28 17:26:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2728898e-32e5-3c99-9120-3f0528158513 | -11.21738 | -45.05181 | 2026-08-28 17:26:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |


[Clique aqui para ver as próximas entradas](README108.md)
