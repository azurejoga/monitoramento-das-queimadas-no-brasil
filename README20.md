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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1aae8b04-37c8-3a59-b583-365f118d1267 | -18.02453 | -47.63678 | 2026-09-27 04:10:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4da6163-fcb8-3bc8-95be-ddb7865cf985 | -12.704 | -47.31685 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27ec0591-75cb-3f0b-a5ea-f3bc01b650c9 | -15.42165 | -47.90706 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96865ffd-b06f-3f01-860e-fd94bd3fedc8 | -14.12007 | -46.3312 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 836b6efe-ef5b-3a03-8154-bf7f435ed899 | -11.05181 | -51.32433 | 2026-09-27 04:10:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75716027-f1e5-3bf9-8fbb-5f7e499ccad1 | -12.30209 | -50.2988 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 07893fd7-a15f-355f-be83-609baf7dad61 | -11.93488 | -50.54687 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f9851f9a-5fb8-3329-b2b1-7e4c0e7d9052 | -11.94137 | -50.54137 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ccd00aaf-6d49-3e37-8732-fbe5a685f8c4 | -13.37607 | -51.32022 | 2026-09-27 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6d2410d5-67e5-3b38-9f7f-b1c834d5cb39 | -11.23681 | -49.85267 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f797548e-7c8c-3083-86e5-e9d8faa82233 | -11.81727 | -50.51085 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 1db4b42d-9321-3779-9bdf-be5f60dff25c | -12.14026 | -50.32635 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afdc1b95-f291-3bda-ab70-5bbc3eb53fc7 | -12.23276 | -50.71654 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64f14035-cbcf-3dae-9dad-d558e0f9025f | -12.96864 | -42.41487 | 2026-09-27 04:10:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6ce11cf1-8324-3146-8e58-d8656efe16c8 | -11.87854 | -50.52861 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d567a0ce-0e0a-34c6-a2fb-b74c847d4b73 | -11.94684 | -50.56983 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 920465ec-3658-3506-b2e6-a16265d4a337 | -17.78748 | -47.16374 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a1542b4-832a-3072-87ab-f63845da0a9c | -11.77112 | -51.01212 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| aadabf72-5dc9-3468-82ed-2ffb55f3a012 | -13.0871 | -47.40933 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bfd03e8b-421b-3a0d-9699-26074cf6607d | -11.88656 | -50.51814 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ba500715-391f-3fb9-8c2f-4ae64249f225 | -11.93592 | -50.51307 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1a49799-bf54-3cf2-8501-c71da77a2671 | -12.07118 | -50.23388 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce52dbaa-e943-3c43-97cc-0f23714023f3 | -11.9378 | -50.50327 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 513c6afe-135a-316e-a394-37deee2767eb | -11.93655 | -50.5098 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 42b36257-cff6-3f6f-a4db-2b1791a2871e | -14.78868 | -45.95238 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2659164a-51df-368d-acd9-f125cf99b43a | -11.88533 | -50.5247 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ec89b615-48eb-3f70-a9f3-9a494887f730 | -14.41609 | -52.805 | 2026-09-27 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47071a96-447b-307f-873c-9d3cfbf32281 | -13.43745 | -43.82064 | 2026-09-27 04:10:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d35e91e5-fc4d-3a55-807a-fc583a3f407b | -15.41861 | -47.89185 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e006a3b-9b0c-32b5-9c71-309fbb8221a2 | -15.9276 | -42.3722 | 2026-09-27 04:10:00 | NOAA-20 | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 03567367-714b-32df-9718-616f12eb8570 | -11.88506 | -50.52312 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 701b791d-b923-37a6-9982-f862c776f63d | -13.69466 | -43.13414 | 2026-09-27 04:10:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02509ba8-f8f8-3a0b-87c1-391799780221 | -15.41546 | -47.89432 | 2026-09-27 04:10:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4991eaee-00b4-3e11-938f-25849c663539 | -11.95222 | -50.51299 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2922a704-ba49-3caa-8847-e44a0d37c4ed | -15.47299 | -46.15597 | 2026-09-27 04:10:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48ab8379-ce26-38b8-9e87-6ff0d41e7656 | -12.20508 | -50.37885 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1aa276ec-7918-38cf-a1e8-1c68d878e2fb | -12.05096 | -50.59212 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7ff02123-b2a3-3154-85f6-72e767f34174 | -14.39992 | -43.77602 | 2026-09-27 04:10:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 609c737e-9126-3b5d-889b-eae3e352e4a0 | -11.57324 | -50.51149 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a312d83e-2b93-3b7b-9bd5-3f309216307e | -12.29757 | -50.29465 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| ff855b98-011e-380c-84fe-3e3ca7951b08 | -11.9854 | -50.56744 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e383c57-fc3c-326e-9af9-45254dfa2917 | -14.11796 | -46.3207 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d837b91-527f-346b-bac4-895836e41b81 | -12.71652 | -47.31925 | 2026-09-27 04:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| abdcdf0c-e980-3208-8540-f5c9d7a24ec3 | -11.8533 | -50.52158 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 803b2329-9c3d-36d4-ba76-ab4457b1799c | -11.87983 | -50.52205 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 57cbc15c-8ce6-3916-ace7-86076c0bf762 | -17.57273 | -46.90746 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27608a15-ede3-3a85-a622-7eec07121b88 | -14.49686 | -48.33347 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c7fc9c9-8660-339f-9a64-066989318c01 | -12.05033 | -50.59542 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 737cd19b-286c-3ee1-9319-e124e02d21e1 | -11.93195 | -50.50546 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b35a885-18a5-38c4-8da5-ab60df45d87b | -11.88595 | -50.52143 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5427966b-3e33-3f5d-b168-52a95f2ba3c0 | -14.81127 | -43.30772 | 2026-09-27 04:10:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 23455ae1-8900-3a18-a282-faa94392a3ff | -11.96755 | -50.54673 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2bda478-6138-33d7-bc80-f85ad76be41f | -12.2792 | -50.30712 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 9bee4afa-e798-35d9-a554-5a9e499e1782 | -17.57648 | -46.90831 | 2026-09-27 04:10:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42b0f47f-3a54-3bd4-a06c-faf2c4db7e9e | -12.27494 | -50.69072 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b67c7ced-2f66-3f90-a6e1-c421f7593b47 | -12.27594 | -50.69083 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44201957-d1be-36fb-bf32-5b2a6058e9e6 | -11.88718 | -50.51485 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 43e14605-8744-3c8e-93a2-6b162f6a2c20 | -11.97166 | -50.57944 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 680e2f04-d20f-3166-b245-9d2695f7f145 | -14.21947 | -48.50634 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 170a36be-300c-3c04-bd3e-733ddcbabcf5 | -12.56699 | -44.14022 | 2026-09-27 04:10:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 199cac8b-1d00-3e3d-a003-ab4c9e15e761 | -15.60487 | -41.35477 | 2026-09-27 04:10:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| cdfe0f13-bf98-3678-8f9e-0e2051ed1b13 | -13.09877 | -47.41663 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d49ad8fd-c943-3403-a6a3-c9743757e3aa | -16.58811 | -41.84102 | 2026-09-27 04:10:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 1e1577c1-218e-33dd-8db1-9c9e2edaaee2 | -14.49605 | -48.33781 | 2026-09-27 04:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8916db05-87ff-30b2-b5b3-c5f248c28d76 | -11.89029 | -50.52418 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e7be835e-bdea-3c8b-9247-68514ba2a745 | -16.49913 | -43.53273 | 2026-09-27 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5cec3de-536c-37d5-8644-096381f62f92 | -11.85268 | -50.52486 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 24b5aaf2-171d-3c0e-bfd7-6f1a9ae64d60 | -14.40949 | -52.80774 | 2026-09-27 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63d14dce-5e90-300a-a993-909703960c69 | -12.13842 | -50.33579 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0fa12ea-0d55-3f03-98b4-3c00468edf98 | -14.12093 | -46.32633 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7da47b6f-6998-39dd-a15f-026d7824b600 | -16.78067 | -39.43131 | 2026-09-27 04:10:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7744e926-70d6-3d69-b3bd-4532aa1c0c5f | -12.03334 | -50.5988 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5559e95a-49e9-3119-835b-1016a6515c53 | -11.77058 | -51.02083 | 2026-09-27 04:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c7e4a42-b587-379f-b5d3-b3b49c9cbc2a | -12.47381 | -47.48114 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 198347e4-f2bf-3b75-a41d-dc4859c6b453 | -18.55033 | -43.58413 | 2026-09-27 04:10:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2b56eac8-1a2a-34cc-b59f-198229654fa7 | -15.68441 | -48.22533 | 2026-09-27 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d2b5bcd-297b-3c59-8ed8-4aff38f920cd | -11.9261 | -50.50766 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fca89721-2a8b-34d3-9ac6-f5365628bab1 | -17.44057 | -44.06891 | 2026-09-27 04:10:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb237d3c-593b-3ebf-aba6-868adc9e033e | -12.68093 | -47.32154 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9dbb041e-37a9-3ebd-ac90-96ffddab5827 | -11.94302 | -50.50433 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 24b45c42-4506-3291-ac1a-6b554f8fd7f0 | -15.52331 | -42.35156 | 2026-09-27 04:10:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e3737582-0ba8-36ef-838b-ac1df6ebd3fe | -13.09055 | -47.41425 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31a4ad8a-ec87-3fe9-9b57-152153ccb5e4 | -12.57115 | -44.13688 | 2026-09-27 04:10:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 50a06ebd-8aa4-3298-bda3-1ec361ce7b83 | -12.29125 | -50.29984 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae14f72e-63a8-3d2b-8716-6e2aadedeff2 | -16.56641 | -53.06809 | 2026-09-27 04:10:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3fe51ae-9622-3c2b-928e-944172c849c9 | -18.4635 | -43.1284 | 2026-09-27 04:10:00 | NOAA-20 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2f63e278-7e18-39c3-8bd0-8e84ac87763c | -14.53934 | -52.79002 | 2026-09-27 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 01b14dd7-6a1b-362a-b3c5-04765cbde123 | -14.1171 | -46.32555 | 2026-09-27 04:10:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 387bf13f-fdae-3060-8e1a-fab3e40914bb | -12.29146 | -50.74593 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65cd13bf-5245-38b9-bd6c-eb72ca85c4db | -14.78655 | -45.95002 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11668d13-ece7-3c6e-8bd0-6114c3323628 | -12.42472 | -44.14558 | 2026-09-27 04:10:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6967986e-940f-3eb4-bede-3ff56f652b39 | -12.27006 | -50.69305 | 2026-09-27 04:10:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4853cd8-f460-3d5b-92b4-fdfd3f1c63ae | -12.67822 | -47.31243 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 730ef6cf-fb61-3f45-9cda-8e0d32241863 | -10.41539 | -53.82333 | 2026-09-27 04:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c7f5ef8-c79f-3e8a-bfa1-2be7ab440909 | -14.80063 | -45.95736 | 2026-09-27 04:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8cd0d65b-b2ca-3286-a4c8-b9c8c249bf26 | -14.80354 | -45.96266 | 2026-09-27 04:10:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8f41eb2e-696c-3084-8091-9870c82cfae6 | -11.88779 | -50.51157 | 2026-09-27 04:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e9caf2fa-f84f-3d4b-8332-0a5cd409a105 | -10.78784 | -48.72522 | 2026-09-27 04:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daebe083-6438-34d7-bc76-80942613a8e2 | -12.89672 | -47.69264 | 2026-09-27 04:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16b7ee24-f0fa-39c2-9c01-3286a1cbb2f1 | -11.23967 | -49.85487 | 2026-09-27 04:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README21.md)
