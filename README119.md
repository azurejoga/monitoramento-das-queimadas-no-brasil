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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ea08fb-571a-3e00-bcf7-861eee984ca7 | -6.98333 | -35.27902 | 2024-10-25 15:09:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| 26a7f8a2-ab35-3470-8175-93920c514e65 | -8.33325 | -36.12284 | 2024-10-25 15:09:00 | NOAA-21 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7072ca96-c9f1-301d-a32d-aff5cf250b4f | -9.27672 | -35.48079 | 2024-10-25 15:09:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2832cf96-82f1-3224-9747-47eab6b5b6db | -9.0251 | -35.91645 | 2024-10-25 15:09:00 | NOAA-21 | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 96ab7999-cb8f-3679-aa6c-77c92ec901b0 | -8.62492 | -36.15938 | 2024-10-25 15:09:00 | NOAA-21 | IBIRAJUBA | PERNAMBUCO | Brasil | 2606705 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 7f3ba4dd-4136-38cf-ad5a-203631a2a599 | -8.31883 | -35.66689 | 2024-10-25 15:09:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 37415085-9e2f-3631-a50f-60fa3f895fc0 | -8.31633 | -35.6667 | 2024-10-25 15:09:00 | NOAA-21 | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| d6b98e00-bb44-38a2-8535-16c376885600 | -8.21734 | -35.60881 | 2024-10-25 15:09:00 | NOAA-21 | GRAVATÁ | PERNAMBUCO | Brasil | 2606408 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 6295a85c-dc94-3bf4-884b-979c888d90a1 | -9.65616 | -35.87022 | 2024-10-25 15:09:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.9 |
| 8a59b5f1-5086-38cb-9184-6d21ad5e35e2 | -9.65553 | -35.86509 | 2024-10-25 15:09:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.9 |
| d5e50cc7-79a2-370a-90fd-69d4d07498bb | -6.12313 | -36.75005 | 2024-10-25 15:09:00 | NOAA-21 | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 15ad353d-6d8f-37da-b7bb-23232a1c1200 | -6.1212 | -36.7496 | 2024-10-25 15:09:00 | NOAA-21 | FLORÂNIA | RIO GRANDE DO NORTE | Brasil | 2403806 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60d990c2-057f-33a6-afad-586fe4937e99 | -7.31538 | -37.26073 | 2024-10-25 15:09:00 | NOAA-21 | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a6b854f1-2495-3967-9f8f-8c815b4211a4 | -6.66653 | -36.66338 | 2024-10-25 15:09:00 | NOAA-21 | PARELHAS | RIO GRANDE DO NORTE | Brasil | 2408904 | 24 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 40d112ca-10ce-3317-bf21-226df401ff2b | -9.11677 | -36.80794 | 2024-10-25 15:09:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0c048539-e087-3b17-bc23-6c77e903830b | -9.11667 | -36.80611 | 2024-10-25 15:09:00 | NOAA-21 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f6f7366a-0148-345f-99a9-eec00d12c4b6 | -8.76525 | -37.22344 | 2024-10-25 15:09:00 | NOAA-21 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 4c352b5d-304a-3c18-8616-07e9dbace9c8 | -8.67055 | -37.09586 | 2024-10-25 15:09:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 2e83dfc5-4a2d-3085-897e-b50692f47325 | -8.58212 | -37.61536 | 2024-10-25 15:09:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 6815966d-806b-3cf9-8096-3562606092ed | -9.69366 | -37.34542 | 2024-10-25 15:09:00 | NOAA-21 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 30defbb0-b906-31e2-9d9c-e3b6630f07c3 | -9.68889 | -37.34204 | 2024-10-25 15:09:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 776324ba-41e2-3c01-a74f-3f1c3563ec84 | -10.20024 | -36.80577 | 2024-10-25 15:09:00 | NOAA-21 | PORTO REAL DO COLÉGIO | ALAGOAS | Brasil | 2707503 | 27 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e4123521-74c9-339a-9a7a-f4056e6fb245 | -11.69805 | -37.54512 | 2024-10-25 15:09:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| b63f0258-5c02-3402-8a90-c9261408946f | -11.69649 | -37.54607 | 2024-10-25 15:09:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| a9c0254b-01d7-3dcd-bd93-6234f4f81683 | -11.10878 | -37.36111 | 2024-10-25 15:09:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| c7f11ebc-f323-3a7c-a4fd-333b88cbedca | -11.10806 | -37.35487 | 2024-10-25 15:09:00 | NOAA-21 | ESTÂNCIA | SERGIPE | Brasil | 2802106 | 28 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 8d07459c-b172-32ad-9990-fc09e3df7c1e | -6.4511 | -38.49917 | 2024-10-25 15:09:00 | NOAA-21 | JOCA CLAUDINO | PARAÍBA | Brasil | 2513653 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f617c5e5-54c8-38a3-a876-6d5c43b44908 | -6.45007 | -38.49635 | 2024-10-25 15:09:00 | NOAA-21 | JOCA CLAUDINO | PARAÍBA | Brasil | 2513653 | 25 | 33 | nan | nan | nan | Caatinga | 7.9 |
| f14f30a4-1b65-33f7-a417-868a79fe4fda | -6.33124 | -37.72171 | 2024-10-25 15:09:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 6a2b5bde-d835-3287-a04c-990b66357058 | -6.32931 | -37.72403 | 2024-10-25 15:09:00 | NOAA-21 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8ff7cb21-b1e2-3acd-81d6-a5cd0b8451dd | -6.13127 | -37.95867 | 2024-10-25 15:09:00 | NOAA-21 | SERRINHA DOS PINTOS | RIO GRANDE DO NORTE | Brasil | 2413557 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1b4b0524-1331-38b8-b1b2-bcb94bbedb9c | -6.12448 | -37.95908 | 2024-10-25 15:09:00 | NOAA-21 | SERRINHA DOS PINTOS | RIO GRANDE DO NORTE | Brasil | 2413557 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3b439e5e-37d3-3d46-a917-4bf87a31ce46 | -7.91828 | -37.98928 | 2024-10-25 15:09:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 655c649f-fe1d-39d3-8b24-f9dbc4530921 | -7.84702 | -37.9786 | 2024-10-25 15:09:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 47.6 |
| 64be82a0-3888-3775-a110-81e321d134f6 | -7.84634 | -37.97922 | 2024-10-25 15:09:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 61.1 |
| bfca7480-56d1-3137-9ad0-f0548f0c7893 | -7.84621 | -37.97206 | 2024-10-25 15:09:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 47.6 |
| e8f1686f-1c49-34c4-a7ee-6eb8b1d00ed7 | -7.84549 | -37.97267 | 2024-10-25 15:09:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 60.9 |
| f4d3c82c-2d49-3e40-8533-9d8ebedf3c07 | -7.78888 | -37.85731 | 2024-10-25 15:09:00 | NOAA-21 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 75f39ada-4cb5-3934-8bc1-46d6f2e9a999 | -7.78345 | -38.03751 | 2024-10-25 15:09:00 | NOAA-21 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 10.4 |
| c0016e58-3ea2-3354-a42a-c0967f9202bc | -7.67978 | -37.93804 | 2024-10-25 15:09:00 | NOAA-21 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 15.8 |
| bc05e6ee-d26d-3bff-972e-130f4f1ea024 | -7.67795 | -37.93513 | 2024-10-25 15:09:00 | NOAA-21 | PRINCESA ISABEL | PARAÍBA | Brasil | 2512309 | 25 | 33 | nan | nan | nan | Caatinga | 20.5 |
| ac29880b-e2dd-3a9e-90ec-f772751848b1 | -7.36441 | -38.77457 | 2024-10-25 15:09:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ba60ed5f-2ab1-3db0-8d06-5828b683807c | -7.36189 | -38.78218 | 2024-10-25 15:09:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| d7135313-af00-3705-956e-3d5cac9c2677 | -7.1529 | -38.5429 | 2024-10-25 15:09:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 9.1 |
| e5a4c030-cf34-3460-b577-af69cba9ba8b | -7.02608 | -38.10613 | 2024-10-25 15:09:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 48.0 |
| bb7f9ca0-07e8-34c3-b276-34bcc71edb91 | -7.0253 | -38.10002 | 2024-10-25 15:09:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 622bce60-1bd4-34b4-bf4b-ce4ea8be11c6 | -7.02453 | -38.10304 | 2024-10-25 15:09:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 84cca9fd-4f49-36c2-9b45-ef5e632248f3 | -7.01914 | -38.1064 | 2024-10-25 15:09:00 | NOAA-21 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 12.6 |
| c2a9ec1f-d92e-3447-a1e9-a0fa49e664de | -6.77309 | -38.38407 | 2024-10-25 15:09:00 | NOAA-21 | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6812bbd4-ac49-3151-8feb-76bbb2ade180 | -6.68356 | -37.59289 | 2024-10-25 15:09:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bae404e9-2f56-39b5-91f2-f7315cc7489a | -6.63489 | -37.66663 | 2024-10-25 15:09:00 | NOAA-21 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9bca570f-7ea3-36ad-b116-4a41380f47f8 | -6.58507 | -38.01466 | 2024-10-25 15:09:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 694ae822-845c-3243-b1f6-519145fc6f2d | -6.58429 | -38.00858 | 2024-10-25 15:09:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 4da22647-a547-3900-9216-fa9d9fb895c2 | -6.58289 | -38.01567 | 2024-10-25 15:09:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 39.4 |
| b2abc973-177d-32ed-9ab5-0a7feb85f69d | -6.58207 | -38.00962 | 2024-10-25 15:09:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 850b7a6a-3122-34f7-81b8-59f484abff6e | -6.54512 | -38.09541 | 2024-10-25 15:09:00 | NOAA-21 | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 62c2e320-602f-3d31-b6f1-8ab8635424c2 | -8.17545 | -38.18674 | 2024-10-25 15:09:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 345ff6ea-292a-35e2-a903-83d2b18ef89b | -4.59464 | -38.93066 | 2024-10-25 15:12:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 1745030e-6080-3f3c-bd89-e25a1baf25aa | -4.5937 | -38.92406 | 2024-10-25 15:12:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 41aeab17-c267-3ccc-875e-5594dd08da6c | -4.5932 | -38.92736 | 2024-10-25 15:12:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 24.5 |
| 63015435-be17-344f-a9c4-7322a0a64ffa | -5.50881 | -39.13584 | 2024-10-25 15:12:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 0f977ea1-0351-3227-b04f-38380870bf7e | -5.50494 | -39.13553 | 2024-10-25 15:12:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 12aaab5e-264f-3f47-91dc-77b17caff77c | -5.16927 | -38.81006 | 2024-10-25 15:12:00 | NOAA-21 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 14743665-9baa-38f8-9652-cabab0cbe52e | -20.57371 | -40.94587 | 2024-10-25 15:29:00 | NPP-375 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 4527b231-36af-3b30-8f04-58149609869b | -12.47918 | -43.71847 | 2024-10-25 15:31:00 | NPP-375 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e4690d9a-032d-3759-8cad-4d17c657b775 | -12.45617 | -43.55151 | 2024-10-25 15:31:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2df6fad3-f48f-3815-a40a-fa96ec4b655a | -12.41479 | -43.96482 | 2024-10-25 15:31:00 | NPP-375 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a3eb3982-46cc-3a4f-9fa4-19ef9bf03b9b | -12.41416 | -43.95885 | 2024-10-25 15:31:00 | NPP-375 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 1e2a7f70-fb7b-343b-8f7b-690345d6005b | -13.73288 | -43.60717 | 2024-10-25 15:31:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e98994a9-3d9f-3ef0-9fc1-da60ab798e3d | -13.29377 | -43.96238 | 2024-10-25 15:31:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5711b3ee-56a6-3b54-906b-0fffa9aa9ff7 | -13.29173 | -43.96368 | 2024-10-25 15:31:00 | NPP-375 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae223b6f-37a9-345e-a04b-4ce5197b5d4f | -14.14771 | -43.89389 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 8ca3b28a-2c83-3f8e-b492-91734a19f7e7 | -14.14627 | -43.89495 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 50705dc9-d1bc-3f32-98b8-01e9d22ae18b | -14.05124 | -43.74848 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53cabc67-ae5e-3437-9c59-b826ac418918 | -14.02394 | -43.9217 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7927833e-a80f-3d8a-ac73-ce04116d4075 | -14.02324 | -43.91423 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b541ed35-f550-36b7-a9a2-afe5d8b026a9 | -14.02322 | -43.91922 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| bff33142-6b66-3d4d-9ff0-a1273fdcec4f | -14.01666 | -43.9224 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 759f9587-f984-37e8-a120-e07e182e50d9 | -14.01596 | -43.91494 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5d20ae44-964c-3294-8fd6-67f6947d0994 | -14.01593 | -43.91988 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 82b5cbba-7615-336e-9d45-5f021773e14d | -13.84589 | -43.77478 | 2024-10-25 15:31:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 28a1d087-9204-3792-8d7b-45a2a12c563e | -12.20658 | -38.24809 | 2024-10-25 15:31:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b4fbf45b-fbde-3ab2-be4f-6747f5190be7 | -12.20159 | -38.24876 | 2024-10-25 15:31:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 65ae587d-7923-3a44-8e6f-ff23a3bbe81b | -12.20088 | -38.24306 | 2024-10-25 15:31:00 | NPP-375 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| 6b804eb1-8e20-3c99-9b22-49e6f48dc48e | -11.69156 | -37.55674 | 2024-10-25 15:31:00 | NPP-375 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 403731c1-b56c-3e26-9f34-01b1dd5d10d4 | -11.69091 | -37.55173 | 2024-10-25 15:31:00 | NPP-375 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 018c5775-7981-3d25-80ac-d2f015767146 | -17.84864 | -39.88058 | 2024-10-25 15:31:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 5252db69-2925-33ca-8f63-865d2d6efbe7 | -17.8482 | -39.87598 | 2024-10-25 15:31:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| b38f81d7-891f-3a5e-b60f-d1d8faaa1199 | -11.79737 | -38.66899 | 2024-10-25 15:31:00 | NPP-375 | ÁGUA FRIA | BAHIA | Brasil | 2900405 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| d6e2c21b-998d-352f-ba1b-40aff404a9f2 | -12.20461 | -39.30389 | 2024-10-25 15:31:00 | NPP-375 | IPECAETÁ | BAHIA | Brasil | 2913804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f788987b-0d6b-39cd-bf4b-7ec0f2e08dba | -12.17355 | -38.64977 | 2024-10-25 15:31:00 | NPP-375 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 94887850-e5d1-3613-8078-bd97a6bf9a66 | -13.69223 | -40.42194 | 2024-10-25 15:31:00 | NPP-375 | LAFAIETE COUTINHO | BAHIA | Brasil | 2918704 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f1877c61-cd1f-3030-bdfb-8d9545531c62 | -15.74845 | -40.58961 | 2024-10-25 15:31:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6f47a600-2b20-369e-b6ee-fae1cb8d59ed | -19.00429 | -41.37698 | 2024-10-25 15:31:00 | NPP-375 | SÃO GERALDO DO BAIXIO | MINAS GERAIS | Brasil | 3161650 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 49fb6e4c-bcdc-374e-8d73-d6bbb2ee76e4 | -19.0008 | -41.38 | 2024-10-25 15:31:00 | NPP-375 | SÃO GERALDO DO BAIXIO | MINAS GERAIS | Brasil | 3161650 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| b0bedbb5-4a1f-3eea-aa12-dbb570d600cb | -12.22575 | -40.91514 | 2024-10-25 15:31:00 | NPP-375 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e127499f-d23d-33f1-ba0b-04f68f7ebda7 | -13.55322 | -40.79737 | 2024-10-25 15:31:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 273fcf60-bfd0-340f-8862-388c864e08cc | -13.39791 | -40.89481 | 2024-10-25 15:31:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fbbb7d1b-6e9f-3100-a007-39277f75171a | -13.396 | -40.8939 | 2024-10-25 15:31:00 | NPP-375 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| afc31bb5-1e5c-398a-b9e8-108f30cb025c | -13.37788 | -40.5448 | 2024-10-25 15:31:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |


[Clique aqui para ver as próximas entradas](README120.md)
