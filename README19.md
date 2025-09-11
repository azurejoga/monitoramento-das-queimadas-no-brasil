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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29fca8c8-930b-3424-8bbb-063a46831ac4 | -8.23629 | -47.8648 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d98e4b50-f09b-318d-bbc9-b4d5505d24e5 | -6.56676 | -44.20995 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 661b046b-0fed-3562-b383-5a74ffbd36fb | -13.16579 | -45.28327 | 2025-09-11 03:55:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9376a472-340b-33ff-8129-c4064c24e702 | -11.48996 | -43.65466 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9026f786-000e-3b3f-ae2a-bab929ae0945 | -9.30048 | -46.76302 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c39ae4bb-9cea-3d59-b9a6-1764ff49680c | -7.23901 | -44.47419 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f17519a9-cd87-38ab-8c7d-a4e93fa00812 | -11.3171 | -50.7564 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| fc072d20-e89e-3531-a7bd-cac2f28ea0c5 | -11.43809 | -43.57432 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3d19c8c7-ad13-346f-8bf8-878629f9e6b5 | -11.48368 | -43.69178 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c86e3f35-2a47-3257-96a4-9140afb14b31 | -6.25719 | -43.41696 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4db46c1b-4a35-383c-a968-32da4471a201 | -12.14189 | -44.86261 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35666f8e-8632-327a-850e-cc46efa4502d | -8.0434 | -48.1525 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea19ca03-76d6-3dfa-81a9-d36b7eafc5f2 | -9.08915 | -49.85278 | 2025-09-11 03:55:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d30f65c8-05eb-3e89-bcfd-c6275d851610 | -8.74964 | -47.10616 | 2025-09-11 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 93913e88-3889-32e0-be3a-18b7aba0312e | -9.52432 | -43.06013 | 2025-09-11 03:55:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f2d9038b-3a63-3eb9-b8e3-310b8900d6ff | -6.8558 | -47.87953 | 2025-09-11 03:55:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5fc65333-e87d-3422-a783-476a827e66be | -7.72967 | -35.13245 | 2025-09-11 03:55:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b300f3b-870e-3291-ae50-c90c93e15e68 | -12.42285 | -47.80826 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 668295cb-51e0-360a-8860-33b82599b350 | -11.3925 | -45.58495 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16d606c0-8d62-33d8-a663-16e2f3118973 | -10.0636 | -50.38047 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88956856-d411-3a66-8ad7-6a1301df9e49 | -9.45426 | -46.42821 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7c9ab54-f328-3c84-85fb-d20601632f20 | -8.81073 | -48.09954 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e73fbbc2-b789-39ea-bcad-218ad40d3d71 | -6.24369 | -43.49728 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f38496cf-19f2-30fb-bd9c-8e3710d481d7 | -9.30523 | -46.76396 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0c976779-4d92-33a5-a2e8-789f1ff75f0a | -7.31044 | -44.36132 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c37f727a-7996-33dc-8f86-cecd65e7667b | -8.1014 | -48.24477 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dbc2277-53b8-3d78-b245-e93c7e35fe9d | -6.83663 | -45.61173 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d1e4be35-8562-3bf9-9091-434ae322122b | -7.05735 | -46.23225 | 2025-09-11 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39dea5b2-2683-35e9-91b6-ba33654113a2 | -9.08382 | -47.08702 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a459e60c-f2dd-3a57-aadf-af3b859c07be | -11.08396 | -51.32985 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5b6c4517-73eb-3158-9196-b6891d487842 | -9.05743 | -46.96521 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 984d9c22-3e26-3895-9c5b-433dcdc298a1 | -6.25262 | -43.4197 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bf51ed9-c915-3c28-a98a-a36d9455339b | -6.66776 | -44.12872 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 37f8df5d-42fc-361a-bb04-55871f3f773a | -9.45963 | -46.69814 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6bbf132d-e7ac-3123-b3e0-507ba21b1b9f | -6.21797 | -43.49496 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d9d7e7ff-e64f-3209-859c-60ab058dade1 | -9.10006 | -45.69659 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 877be3fb-37a2-3d6b-b967-62991d38f40f | -11.14814 | -45.24533 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bc8e59b-2d28-36d9-87c4-ce9de014eb2e | -13.25862 | -43.78896 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fc99bc9-7cad-3c33-bcf8-c961f074524b | -8.03791 | -48.67868 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20615061-166d-38ea-843d-76c09d233834 | -6.63141 | -44.0803 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42eed66b-30b3-3b25-aeeb-fcd13e68e530 | -6.39995 | -43.50888 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72806e58-e9f9-3702-889e-c7ae43b6b505 | -8.03939 | -48.67069 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 425436c3-193d-3284-bf0c-f2413663c17c | -12.47609 | -39.55331 | 2025-09-11 03:55:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0baa295a-0039-3ef5-8fae-2315515f4901 | -11.10476 | -48.41544 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4693849-1556-3271-a25b-dc1abf1d296e | -11.02596 | -45.06696 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e341a696-9062-3967-805b-bb9aa60323b2 | -6.85943 | -47.85876 | 2025-09-11 03:55:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32c8ac49-e380-31d4-9b3b-0affa36af783 | -10.08524 | -48.18116 | 2025-09-11 03:55:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94d7e472-b632-3c59-ba46-5217e5690dd6 | -7.87192 | -46.7274 | 2025-09-11 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f29cfffc-abd8-3112-b60c-9b4f47d333a6 | -8.20132 | -50.10074 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d72cbf6c-46d9-3f1c-80cb-30c019550e6c | -11.36777 | -46.53699 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 724da853-7e38-3b1a-be20-a7fbe2491c53 | -7.56388 | -48.21416 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11c6051c-da63-3857-9b0a-8bf6d49d4d83 | -9.70859 | -43.53584 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bae45d65-a43d-3e94-bd62-445f31b6c62b | -6.85764 | -47.86904 | 2025-09-11 03:55:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 764b6493-d540-30f7-87eb-e76d7627a614 | -8.03947 | -49.04824 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b4841d5d-abb8-3e47-a320-4c13dd765473 | -11.86164 | -46.75849 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 78fa4daf-2740-359f-9540-cec0f7b01b93 | -11.14467 | -48.4582 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f4968ce-ee68-3158-96ba-f9edcbc0b3cf | -7.42381 | -45.87309 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6978ca42-8328-3a35-a307-87120c8309c9 | -9.4505 | -46.42247 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9869afaa-fcc9-3925-9ed6-5e3f2d42ce90 | -11.39498 | -43.52612 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91e72c84-602d-3fe5-af8c-a21e693f4ed4 | -8.07999 | -50.18082 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2814563b-bad8-3a2b-9459-69e48172a732 | -10.7336 | -46.13876 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba7bfd54-5909-3c6f-a31d-1064374bba56 | -12.53195 | -45.3391 | 2025-09-11 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2549e49-40bf-31fd-87d6-c5020f6482e4 | -7.08307 | -43.87717 | 2025-09-11 03:55:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45837306-e7e7-378f-b150-def5650c77ed | -6.3493 | -44.08358 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a54d2aab-f22f-3d84-b238-887804db2aca | -11.37708 | -43.51839 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0eb3daf-5c10-345f-b830-5473db3fa348 | -6.53831 | -44.77821 | 2025-09-11 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff4572b5-42a3-3095-95d1-0f17d98f36cf | -6.16457 | -45.81207 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db685e67-1dfe-364d-9fbe-262ae8b6cc51 | -5.81623 | -45.68179 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ee43afb-6659-3d2a-8826-ccab05945d92 | -6.08303 | -44.81945 | 2025-09-11 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75b53a16-82b4-3501-bbff-4edfd51300f4 | -9.80181 | -47.76577 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e05197bb-563c-328b-bb42-8811ad3290bc | -11.36212 | -46.51687 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 70fb6e10-7ccb-388e-9b9e-76ac98279441 | -11.38042 | -45.57902 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 07b4c35b-de8a-3352-9bd6-233561f7cf58 | -10.14366 | -46.16607 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f8172fe-3e92-3a4c-9a0e-f12aca9990bb | -8.4247 | -47.27342 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 549ad0b5-d37b-312c-b923-40476afdc2f1 | -8.04511 | -49.04938 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 34232451-cb25-379e-acf7-2f32df8184d5 | -6.39478 | -43.5152 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8b3de08-3259-339a-b95d-a9a018ecf246 | -5.94304 | -45.71548 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24430c5d-e187-32d9-b2c1-87ca9488f434 | -6.20932 | -43.49732 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f699220-c39b-3247-8758-90a487df0f83 | -7.48217 | -45.28797 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d94dec69-9ae2-300c-b229-2db29ec88251 | -9.6651 | -43.52103 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 604b3b41-4a45-3553-9f5e-0435a2f9fab9 | -11.43514 | -43.56913 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82919b8f-ddf9-3311-abe6-0d468c082aa9 | -10.17658 | -46.19009 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00f912b4-d89d-367b-9f23-cda3629b469f | -9.02038 | -49.77509 | 2025-09-11 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 925c5548-26cf-3845-bd51-25e2eb1230fa | -11.09253 | -48.45133 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4ca8427-034a-392b-b618-faf601d8bdf4 | -6.40176 | -44.02628 | 2025-09-11 03:55:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 518c5738-cd77-3c4b-870a-c197a8e4cb67 | -13.23554 | -40.9528 | 2025-09-11 03:55:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fa2b3b5a-bd8e-34c2-8649-18b2e79adb85 | -10.17371 | -46.18005 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 472c1579-2ae0-3ec0-8ad5-6c953f73eb57 | -10.37408 | -50.52803 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a58b0ddc-63cf-3495-8a08-febe2e66ca7f | -8.65238 | -45.72136 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74485b75-6644-3af8-a013-f08690f607d9 | -9.0766 | -47.08408 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| be238962-20c0-3e21-9344-1720a84a8855 | -9.45515 | -46.42321 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c407105c-28ea-3c38-ac24-77e98335eae1 | -7.78577 | -50.76669 | 2025-09-11 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 022e3e6b-5289-36f6-9994-dec057e8051a | -11.45228 | -43.58145 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0e7a2f24-64da-313d-872f-382e202cd9e9 | -6.8599 | -44.90749 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6acecb60-38b9-3f69-8d41-aa90c9d22767 | -8.16806 | -46.07074 | 2025-09-11 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc4b18b4-15aa-3ca0-b31e-99987f3e40b1 | -8.20654 | -50.1063 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b42d04a-556f-3bfd-8d31-55742df714a5 | -11.42997 | -43.56968 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 120bef23-c6ba-3b81-8406-dc55a87ccdd1 | -8.03047 | -48.6592 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7d3a4c3-e904-3a22-892d-863e415315ec | -9.89414 | -50.16773 | 2025-09-11 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 118a03b3-39ee-3e2f-9cc2-a4f96b1d09a4 | -11.08296 | -51.33479 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README20.md)
