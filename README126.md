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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b1f6e86-57f8-3d5b-92b5-891f3390bc3a | -11.94323 | -50.15013 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed089cb9-07f1-3cbd-b584-452f07df0ce2 | -11.94259 | -50.15461 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e9cdd2a-bab0-3af4-814e-464974af82fe | -11.93951 | -50.14957 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc09c822-4886-3201-b89a-4ddf6dc1b237 | -11.93887 | -50.15405 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7a35dd7-11cf-3720-b004-88a956d136f0 | -11.93823 | -50.15852 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b46e429-dba5-3161-b7a6-fb944249bb0c | -11.93515 | -50.1535 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e7e2c75-e589-38a2-9652-4b2b98695a29 | -11.9308 | -50.15741 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54873b3f-2df0-3a7f-88a3-444b4f74753b | -11.90347 | -50.15091 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e115e123-9386-33b7-800d-b84d08e87379 | -11.9017 | -50.14846 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e2acdb0-0721-395a-a2f5-9063c1753bd5 | -11.10886 | -49.61363 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dafa754d-d751-3b16-923d-3967105d012d | -11.10818 | -49.61826 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a8960813-323f-39ad-863d-614d289396e2 | -11.09437 | -49.60675 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bca27abb-fe11-3868-9779-3c94d041dbd0 | -11.09369 | -49.6114 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84d48687-1bd2-3603-b0c5-33672bf89ad3 | -11.09125 | -49.60151 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 274183b9-0477-3b08-b99b-03365d4c1f5a | -11.09057 | -49.60617 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e71f129-a2f4-305c-8f1a-42861376eb62 | -11.08881 | -49.59162 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f2e13ca-eb01-3ec7-b4da-76bb1a0f4677 | -11.08813 | -49.59628 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43c0f70f-5d55-3050-87c4-9189cdaa82e7 | -11.08746 | -49.60094 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc1fbfe3-e99e-33ce-b22f-e4100e745fcc | -11.08678 | -49.6056 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26730639-7a8f-395c-96bc-6064c68fe685 | -11.08502 | -49.59105 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea17ceef-eb07-366f-9ccc-16fc6e15aa22 | -11.08434 | -49.59571 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b540a899-f3a1-3699-bf06-d72b6799942d | -11.08367 | -49.60037 | 2024-10-03 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a56c5317-c198-3928-8614-bfd491d889f0 | -10.97298 | -50.15361 | 2024-10-03 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 463ef7b7-92dd-3b34-b248-d7a80d69757a | -10.97235 | -50.15795 | 2024-10-03 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40862659-2727-38fa-bc3f-3c92bb456d17 | -10.95819 | -50.17802 | 2024-10-03 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab350ef5-d324-3bf4-a5d2-5b46d91dd125 | -13.63638 | -51.18713 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f5f68fa-641b-32e9-bed6-27e73d3f2dfc | -13.63279 | -51.18659 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a29536a5-a495-39e5-ba7a-2a4c5b66e75e | -13.61841 | -51.1844 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d2f0c71-c752-3f49-9add-215e534bf410 | -13.61422 | -51.18805 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7712917-417d-3c14-8a48-4c195f47ec91 | -13.60462 | -51.22925 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65017b23-bec8-3df1-91ef-10dd76ffd028 | -13.56603 | -51.23351 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 651b6d3f-917e-338a-bdfd-e0c9de56551b | -13.56244 | -51.23297 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0f90e20-d8d7-3e6f-b03c-e15f2505c70a | -13.56122 | -51.24128 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 660f6738-f523-367f-8ce5-e2e913594db2 | -13.55764 | -51.24073 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba7cae40-8c61-3d2f-822f-eaa32f42513e | -13.55109 | -51.23549 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee6649cc-7231-3bb9-baf0-74456ffd4ad5 | -13.5498 | -51.2692 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a973528c-4181-39d6-824e-7b48953dc5a6 | -13.54919 | -51.27334 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 138a9abc-f1f8-3682-a6a3-5cbe83fc18b8 | -13.52855 | -51.13819 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 545694f8-319d-3f9b-a316-1827d15eda80 | -13.52795 | -51.14238 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 063dbb98-2673-3a82-ab90-a5fa44354893 | -13.52734 | -51.14657 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 535914c5-92f1-3103-90ea-6434c02b1f48 | -13.52665 | -51.202 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 792c351d-55ba-3d76-879c-ae6f2102d736 | -13.52605 | -51.20617 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fde24ebe-5f41-3bc2-8c6c-7a0591a93480 | -13.52556 | -51.13346 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 915610f3-9c2f-3e22-9ba2-0fad983768c5 | -13.52495 | -51.13764 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9881b6ad-0801-36ba-bc11-e3cead23c4ee | -13.52435 | -51.14184 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 17d804f2-d831-3e7a-a1e3-0106d1dd0a7f | -13.52374 | -51.14603 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c9241e0-7c2f-3b0c-a367-78725690d4bb | -13.52307 | -51.20145 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79f748f0-e036-3cb0-810b-87b7fcae71c5 | -13.52246 | -51.20562 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 941ee11d-9fc6-3d6f-8a54-8db91129ed3c | -13.52196 | -51.13291 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8fe02c64-f8e2-3ad0-bb14-dea1bff61910 | -13.52136 | -51.1371 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 15813435-680b-3aba-a27e-755822539906 | -13.52075 | -51.14129 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20a340bc-66b1-3ed6-ae68-6a7ba54e52b4 | -13.51896 | -51.12817 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 53a1cd41-37f5-311e-8b28-2a0191bc290d | -13.51836 | -51.13236 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 342ea396-b504-3549-8f25-dc6c5d239c69 | -13.51776 | -51.13655 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 06180392-f56e-32ed-bf92-286bca43c10f | -13.51536 | -51.12762 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f7c2cb1f-600a-3be8-9501-60d4b4dfe0dd | -13.51476 | -51.13181 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b229ef85-b2e1-31df-bb5b-052793d8ede3 | -13.51177 | -51.12707 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| fa5d8c8e-1b37-374a-b5d9-4f4c03dcd2d9 | -13.26032 | -51.2234 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3a3f0e91-1d6e-3e6e-94ff-89ecde995cca | -13.25675 | -51.22285 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82dd182e-a1a7-375d-b9d3-5ae997a9b438 | -13.23543 | -51.20424 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33438aa7-3930-3744-9e41-2c230c389f00 | -13.21221 | -51.18802 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e76563a1-96df-3a28-846b-6ece1f52b4de | -13.20863 | -51.18747 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c777c118-62fe-363d-b234-616afa5b6fb6 | -13.1973 | -51.18998 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbd24688-7015-33d7-88c4-2e50498999c2 | -13.1967 | -51.19413 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e608333b-f321-3e42-9d8b-a373434facba | -13.1961 | -51.19827 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a5a1721-c0e1-3204-ab98-735287ed8e60 | -13.1955 | -51.20239 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c3e6fbc-52c7-3ee3-b8f7-d38aed9be635 | -13.19312 | -51.19358 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 633f2b1d-56e5-3b84-af02-e443cca15b27 | -13.19252 | -51.19772 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c3af55f-b897-31c3-86d0-d5a8b389722b | -13.19132 | -51.20597 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f31cf321-2328-35c8-ba16-f382f3197fa6 | -12.33367 | -50.43133 | 2024-10-03 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6dcadd5-19e2-3567-82bd-7cea1e60ac67 | -13.07697 | -50.84002 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 961843ff-e98d-3a46-9731-0723a99207ad | -13.07634 | -50.84427 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8987376f-6ac3-3bf9-a398-0f109b2c8768 | -13.07271 | -50.84373 | 2024-10-03 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d9c8695-d5cc-368c-93e6-965d9d921140 | -13.05038 | -51.1453 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59419d05-a7ce-31a2-8a8f-971368dbc637 | -13.04891 | -51.1436 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 2f30a86e-aff8-3d6c-8238-0cb27ff7692b | -13.04803 | -51.13649 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| fefd7ef7-fce8-3253-bcaf-7db67fff2459 | -13.04741 | -51.14062 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 7dee1c6d-05f4-36c7-ad4b-99c8d8278357 | -13.0468 | -51.14476 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 622a8213-97e4-35dc-9864-6641fe355e01 | -13.04445 | -51.13594 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 40293129-0c13-3cf0-9a42-b6fc6f0eb627 | -13.04383 | -51.14008 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 49e75e4f-07ac-30e8-8c11-978f36c51077 | -13.04322 | -51.14421 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f11e40d7-79a3-3ccd-8d68-5cf41d0a2edd | -13.04087 | -51.1354 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 72fa43ab-5827-3e2b-96e3-751449c111b0 | -13.04025 | -51.13954 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 9e6743da-3288-35e7-9579-0cdd40506b0c | -13.03964 | -51.14367 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c75ee7b-15d6-34a5-827b-6bc1d0914ca5 | -13.03729 | -51.13486 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 8cf0cc16-3ad4-312f-adba-f34de8151df4 | -13.03668 | -51.139 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 28e1e1f0-fd25-3160-af00-bb257d87d8b3 | -13.03606 | -51.14314 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 451872e9-e90d-3360-8baa-94efcd9d6a2d | -13.03371 | -51.13432 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8f9fc558-bc7a-3c3b-ba34-462f47323554 | -13.0331 | -51.13845 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3e99442f-b680-3b22-bae6-0a95f7ced0ff | -13.03013 | -51.13377 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5aede2c9-a1af-32b3-96cc-ab40cc909fbf | -13.02952 | -51.13791 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| aa5db2c0-aaf1-3fc0-9e7e-d27c294e1d6d | -13.02594 | -51.13737 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ec0265b-68cd-3622-9742-d03d40f8767a | -13.02297 | -51.13268 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 557cf60e-7491-3343-a2ef-8829ac5a834e | -13.02236 | -51.13683 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 669ada54-9ef5-3a23-8207-707ad3aa09e9 | -13.01939 | -51.13214 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec4e4fec-a4fc-3be6-9729-b3ad29017700 | -13.01878 | -51.13628 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bcb2cb3-9f23-30b9-be8a-0ddb411447d7 | -13.01283 | -51.12691 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6ecf074-0ce9-337f-a19b-b43eb9204c38 | -13.00925 | -51.12637 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57dcb7a6-8362-3de1-a204-a23439503399 | -13.00628 | -51.12168 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f037a8fa-27b9-3188-9b8e-b45a94eb7a21 | -13.00567 | -51.12582 | 2024-10-03 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README127.md)
