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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 965dffdf-d633-3de5-858e-12809aaea965 | -23.08623 | -46.60796 | 2024-10-09 04:19:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f40e8033-2bc7-3eb4-9a98-0b2183d41f87 | -23.44769 | -45.92382 | 2024-10-09 04:19:00 | NOAA-21 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a0dd00d-5768-3227-a7b4-99fd90fd9c1e | -23.44491 | -45.91942 | 2024-10-09 04:19:00 | NOAA-21 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 75b44dab-8b1b-3623-98e0-3ec422f34a9f | -23.44435 | -45.92323 | 2024-10-09 04:19:00 | NOAA-21 | SANTA BRANCA | SÃO PAULO | Brasil | 3546009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5447443a-03b2-33e8-bb3b-13a17f9de34d | -18.99288 | -46.65611 | 2024-10-09 04:19:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b3d556f6-0c43-3dae-830e-2f6de285c572 | -18.99229 | -46.65976 | 2024-10-09 04:19:00 | NOAA-21 | CRUZEIRO DA FORTALEZA | MINAS GERAIS | Brasil | 3120706 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31cefbb8-2b62-3e69-b063-242ecf957f1d | -18.91145 | -47.01137 | 2024-10-09 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23e8be89-6a33-3e8a-a16b-ab1d3646477f | -22.82888 | -48.42325 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57c5ca44-9ef4-3416-baec-d870ac7b8249 | -22.82676 | -48.41514 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7b7f403-073d-3bfc-b392-cc3376827711 | -22.82614 | -48.41888 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9821f3c7-42a0-3ef4-aec3-0991f04772c6 | -22.82424 | -48.43027 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 23530f07-f008-3ea0-bf95-c93e085517e4 | -22.82359 | -48.43414 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9cbd7155-c744-3109-b425-0ef3aef2fa04 | -22.82339 | -48.41453 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b61791de-9bc2-37e7-b9a4-75d1906f8ba2 | -22.82214 | -48.42208 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bf770e21-68d5-3701-bf96-e5dcb129b3f1 | -22.82023 | -48.43351 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbc30f7c-54db-3b57-a12a-cb824d220f77 | -22.81877 | -48.42148 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6d2cb7ce-99d7-3a6d-9bcd-b7077caf6f7b | -22.81705 | -48.42122 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 016dad71-1ff3-3619-829f-8795ecd4e6fc | -22.81687 | -48.43289 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 39eeb806-dd1b-33a2-a4d4-c8a45cef73fa | -22.81516 | -48.43264 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb7448ad-8e79-311a-b430-3535d4e13eac | -22.81431 | -48.4168 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23687bd2-911a-3f0c-b3ea-6c43cacd7fc8 | -22.81427 | -48.44841 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4542beb7-330d-38ef-a91a-34b92292a3ca | -22.81369 | -48.4206 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2157eff6-6321-388e-9388-7617528bb9ee | -22.8136 | -48.45235 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a1be989-96b9-357e-b5db-c61dd1918675 | -22.81324 | -48.44426 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e95bb604-b2e1-3511-b0cc-11bac97e72d4 | -22.81306 | -48.42437 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 40655711-579f-3f79-8cb2-e99f490aaad6 | -22.81294 | -48.45628 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f6f3288-87df-3d85-999a-234d9587852e | -22.8126 | -48.44817 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1fea5b1-96f3-30a7-beae-597663358e1a | -22.81244 | -48.42814 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d897f3a5-76c8-39f6-a0a2-ee8378c51177 | -22.81195 | -48.45211 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70fcd92a-cc8c-31b6-82c6-d2e5099ba8c0 | -22.8118 | -48.43201 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3589a287-b229-392c-90ce-2cef71ca111a | -22.81096 | -48.41615 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ba860b9-e574-38a8-8d90-5383266829af | -22.80988 | -48.44364 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7241350-1de5-3616-acf2-0ca97f216959 | -22.80971 | -48.42373 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2afceec9-8bfa-3ac3-ac38-23473ca7f887 | -22.80924 | -48.44753 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b885130-f397-3451-b63e-f2e45ad98285 | -22.80859 | -48.45148 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 865401f8-e99f-3dc6-b4c2-ef29a1dcbdde | -22.80844 | -48.43137 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| adbf33ac-609c-321e-ac8c-8ffe64ed5622 | -22.80652 | -48.44302 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea58cbdd-5df5-3a07-8c74-55245dcb9b69 | -22.80588 | -48.44689 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46385509-9349-3513-9fab-d35f20ac958a | -22.80523 | -48.45084 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cd46275-69dd-3c23-b0ef-ffe25fed240b | -22.80509 | -48.43073 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e072644a-1876-3d39-8eed-24718dff63f4 | -22.80458 | -48.45478 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46b43e24-9477-39b6-90b2-348131a510d0 | -22.80444 | -48.43466 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d30546fb-7e10-3e0e-9446-3b4b51e84292 | -22.80253 | -48.44623 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff002c66-51c9-307a-9659-ec13ba4fd582 | -22.80188 | -48.45017 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc79448-68bb-30c8-9474-e9a975ad3c25 | -22.80173 | -48.4301 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 81f1dc39-1706-3292-9a10-fc50580938d8 | -22.80123 | -48.45411 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97fd344d-2e58-36f8-95e5-a53fcc8f2e16 | -22.7998 | -48.44176 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e2fe001-dddb-391e-93c1-e0a7b1934742 | -22.79917 | -48.44556 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b8162dc-6805-3457-b3f4-40187f9cb80f | -22.79852 | -48.44949 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59991a4f-3f54-319d-aa40-c7c705f9a463 | -22.79837 | -48.42949 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 24b5fbe3-bede-3d47-8bac-dbfc4df8f906 | -22.79772 | -48.43341 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3a517dd6-61ef-3a7f-b3e2-076e5c770576 | -22.79644 | -48.44113 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce6fc9cc-a0b9-3cae-9327-c27b48f38106 | -22.79581 | -48.44492 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffce3607-bdc7-310f-a4b4-9a8acb0274bf | -22.79517 | -48.44881 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7a0da07-73c8-3865-acf4-5d24810d1472 | -22.79501 | -48.42887 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c4cfbc9a-0236-38a2-b029-9c2d602db1ba | -22.79436 | -48.43279 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765097fe-342b-38ef-bb13-203323cc5e69 | -22.79245 | -48.4443 | 2024-10-09 04:19:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8dbc3f64-b8f8-3472-8c1c-21198cea0df2 | -23.98421 | -48.91914 | 2024-10-09 04:19:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f412fa5b-13e2-348d-b020-10ee19559e23 | -23.14954 | -49.79718 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3acc557f-16ac-3445-bac3-1b425ea5afc7 | -23.23928 | -48.99331 | 2024-10-09 04:19:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 917aa1ac-aa1e-3274-a255-e62897762646 | -23.1528 | -49.81973 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d4ef1c6c-94bb-3f09-a0bb-c216c666287f | -23.15208 | -49.82384 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ee788326-fa2e-393a-9783-a842fbb33396 | -23.1503 | -49.79285 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 73850c6f-d912-3656-b3e8-af04ad961cf7 | -23.14878 | -49.80148 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4d503432-ffb9-335d-9904-a2601ca28fb4 | -23.14607 | -49.7964 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c8f2d75a-cfa7-36df-a51d-127bb1b059ab | -23.14529 | -49.80078 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b192e596-63e4-3678-8b0c-544c11beaea8 | -23.14513 | -49.82222 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4c510d40-dd09-3b3b-90ca-5020a990d56d | -23.13889 | -49.81662 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b46432ba-f8e4-324d-82e1-b3bf16b6d754 | -23.13609 | -49.81193 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8fe51902-b1a5-3148-b24e-335d31e2c91c | -23.13539 | -49.81595 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e78ef48a-d9d6-34ea-bc1b-d0eb0621fd12 | -23.13468 | -49.81999 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| d6b4ca5c-fa06-3320-8907-8449ab992793 | -22.97466 | -49.79551 | 2024-10-09 04:19:00 | NOAA-21 | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 51cf8336-0f1a-3e85-97f9-77b48489574a | -22.97392 | -49.79972 | 2024-10-09 04:19:00 | NOAA-21 | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f2bc81c3-b499-3b0d-9ec3-fa9989b733b6 | -24.50319 | -50.26112 | 2024-10-09 04:19:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a6083e8-dafe-3961-8859-cb70bdd869ad | -24.72404 | -49.58116 | 2024-10-09 04:19:00 | NOAA-21 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d12ee280-a6b9-3b01-8d77-af18495bfaf1 | -24.57997 | -50.46436 | 2024-10-09 04:19:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 539f8e84-537d-300a-bc0e-d176543cee71 | -24.5757 | -50.4678 | 2024-10-09 04:19:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 2782fa57-cb75-3b90-a169-a70642a36c01 | -24.09737 | -50.2891 | 2024-10-09 04:19:00 | NOAA-21 | VENTANIA | PARANÁ | Brasil | 4128534 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3825c72a-21a7-39f1-a2f3-e9cd11a3026a | -23.20813 | -50.89802 | 2024-10-09 04:19:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| a4d37684-c890-31ff-b0b1-739563bff1ac | -22.66141 | -50.9402 | 2024-10-09 04:19:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c2bba7ee-51e7-30ad-bb33-8050d4f0cac7 | -24.62713 | -50.97649 | 2024-10-09 04:19:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 62adb4b5-1a95-3ec1-a894-9aa2533d9df1 | -24.53005 | -50.78392 | 2024-10-09 04:19:00 | NOAA-21 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8fcb7210-629c-3643-b1e2-0707376bf7f9 | -17.16983 | -51.68397 | 2024-10-09 04:19:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08e2ccc8-8676-3add-b9ae-1ab363084629 | -23.37211 | -52.04784 | 2024-10-09 04:19:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38a00165-65c6-3a09-bf7b-c5e4753a5989 | -23.29284 | -52.1226 | 2024-10-09 04:19:00 | NOAA-21 | PRESIDENTE CASTELO BRANCO | PARANÁ | Brasil | 4120408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9edbd7ec-cafd-3dce-865b-12e8cbf4a0f1 | -16.50669 | -52.87692 | 2024-10-09 04:19:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c0af5e1-bdc7-3bfa-9207-6a9f930655c8 | -16.00342 | -53.07236 | 2024-10-09 04:19:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f451b2cf-2355-3ef7-9fc2-f4c640ee035a | -23.3478 | -53.90905 | 2024-10-09 04:19:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 354bee6a-3b37-3c5b-a757-01aa46779cb7 | -23.34688 | -53.91351 | 2024-10-09 04:19:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 5e42fd8d-a104-396f-a07a-65509e46b011 | -23.34651 | -53.91077 | 2024-10-09 04:19:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 6fe9f37d-ae3a-36cc-9b21-98f5308aa735 | -23.34008 | -53.90253 | 2024-10-09 04:19:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0bdfed6d-6c77-3ca2-9c65-92c75d18b3b6 | -23.33916 | -53.90702 | 2024-10-09 04:19:00 | NOAA-21 | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 13587395-e8a9-3bc1-93c7-7fb846abc851 | -17.75166 | -53.78432 | 2024-10-09 04:19:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c2775735-d4d0-3bfa-ab72-fa731557f079 | -17.7492 | -53.79667 | 2024-10-09 04:19:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 58f365da-6769-3abf-aa06-4f6f61948206 | -17.74799 | -53.80278 | 2024-10-09 04:19:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf12979d-2180-3850-801f-ee8197a050b6 | -17.74561 | -53.78965 | 2024-10-09 04:19:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6b29b8e4-10ed-369a-88d2-06a251941d80 | -17.74438 | -53.79586 | 2024-10-09 04:19:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 55f08e5a-cf75-3777-bb98-7a8bd6f24562 | -17.34323 | -55.02519 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c5622490-3b65-3573-b95e-e30e9663b25a | -17.33873 | -55.02065 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c90dccde-bfd9-3fc0-a92f-5eb1a9a582d2 | -17.33803 | -55.024 | 2024-10-09 04:19:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |


[Clique aqui para ver as próximas entradas](README103.md)
